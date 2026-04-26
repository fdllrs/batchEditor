import sys
import re
import threading
from PySide6 import QtCore
from processing_options import ProcessingOptions
from pathlib import Path
import subprocess


def _auto_editor_base_cmd(path: Path) -> list[str]:
    """Return the base auto-editor invocation for *path*.

    When frozen (PyInstaller .exe), auto-editor is expected on the system PATH.
    When running from source, the current interpreter's installed package is used.
    """
    if getattr(sys, 'frozen', False):
        return ["auto-editor", str(path)]
    return [sys.executable, "-m", "auto_editor", str(path)]


def _build_edit_expr(track_thresholds: list[float]) -> str:
    """Build the --edit expression from a list of per-track thresholds.

    Tracks with threshold < 0.0 are disabled (internal sentinel).
    Falls back to auto-editor's default 'audio' when no tracks are active.
    """
    active = [
        f"audio:stream={i},threshold={t / 100}"
        for i, t in enumerate(track_thresholds)
        if t >= 0.0
    ]
    if len(active) > 1:
        return f"(or {' '.join(active)})"
    return active[0] if active else "audio"


def build_command(options: ProcessingOptions, path: Path) -> list[str]:
    """Return the full auto-editor command list for a single file."""
    base = _auto_editor_base_cmd(path)
    export_arg = f'{options.export_option}:name="{path.stem}"'

    if options.split_only:
        return base + [
            "--when-silent", "nil",
            "--when-normal", "nil",
            "--export", export_arg,
        ]

    return base + [
        "--margin", f"{options.margin}sec",
        "--edit", _build_edit_expr(options.track_thresholds),
        "--export", export_arg,
    ]


class VideoProcessorSignals(QtCore.QObject):
    finished = QtCore.Signal()
    cancelled = QtCore.Signal()
    file_started = QtCore.Signal(str)                      # str(path)
    file_finished = QtCore.Signal(str, bool, str, float)   # str(path), success, error_hint, edited_seconds


class _WorkerRunnable(QtCore.QRunnable):
    """Thin QRunnable wrapper so a VideoProcessorWorker can run in a QThreadPool."""

    def __init__(self, worker: "VideoProcessorWorker",
                 on_start, on_done):
        super().__init__()
        self._worker = worker
        self._on_start = on_start
        self._on_done = on_done

    def run(self):
        self._on_start(self._worker)
        try:
            self._worker.run()
        finally:
            self._on_done(self._worker)


class VideoProcessor(QtCore.QRunnable):
    """Queues every file as an individual worker inside an inner thread pool,
    allowing up to *max_parallel* files to be processed at the same time."""

    def __init__(self, options: ProcessingOptions, video_files_to_edit: dict,
                 max_parallel: int = 2):
        super().__init__()
        self.signals = VideoProcessorSignals()
        self.options = options
        self.video_files_to_edit = video_files_to_edit
        self._max_parallel = max_parallel
        self._cancel_event = threading.Event()
        self._lock = threading.Lock()
        self._active_workers: set["VideoProcessorWorker"] = set()

    def cancel(self):
        """Signal cancellation and terminate any running subprocesses."""
        self._cancel_event.set()
        with self._lock:
            for worker in list(self._active_workers):
                worker.terminate()

    # ------------------------------------------------------------------
    # Worker registration — called from worker threads
    # ------------------------------------------------------------------

    def _register(self, worker: "VideoProcessorWorker"):
        with self._lock:
            self._active_workers.add(worker)

    def _unregister(self, worker: "VideoProcessorWorker"):
        with self._lock:
            self._active_workers.discard(worker)

    # ------------------------------------------------------------------

    def run(self):
        inner_pool = QtCore.QThreadPool()
        inner_pool.setMaxThreadCount(self._max_parallel)

        for file_path in self.video_files_to_edit:
            if self._cancel_event.is_set():
                break
            worker = VideoProcessorWorker(
                options=self.options,
                path=file_path,
                cancel_event=self._cancel_event,
                signals=self.signals,
            )
            runnable = _WorkerRunnable(worker, self._register, self._unregister)
            inner_pool.start(runnable)

        inner_pool.waitForDone()

        if self._cancel_event.is_set():
            self.signals.cancelled.emit()
        else:
            self.signals.finished.emit()


class VideoProcessorWorker:

    def __init__(self, options: ProcessingOptions, path: Path,
                 cancel_event: threading.Event, signals: VideoProcessorSignals):
        self.options = options
        self.path = path
        self._cancel_event = cancel_event
        self._signals = signals
        self._process: subprocess.Popen | None = None

    def terminate(self):
        """Terminate the running subprocess if any."""
        if self._process is not None:
            import os
            import signal
            if hasattr(signal, 'CTRL_BREAK_EVENT'):
                try:
                    os.kill(self._process.pid, signal.CTRL_BREAK_EVENT)
                except Exception:
                    self._process.terminate()
            else:
                self._process.terminate()

    def run(self):
        if self._cancel_event.is_set():
            return

        path_key = str(self.path)
        self._signals.file_started.emit(path_key)
        cmd = build_command(self.options, self.path)
        print(f"Running command: {' '.join(cmd)}")
        success = False
        error_hint = ""
        edited_seconds = -1.0
        error_lines: list[str] = []
        kwargs = {}
        flags = 0
        if hasattr(subprocess, 'CREATE_NO_WINDOW'):
            flags |= subprocess.CREATE_NO_WINDOW
        if hasattr(subprocess, 'CREATE_NEW_PROCESS_GROUP'):
            flags |= subprocess.CREATE_NEW_PROCESS_GROUP
        if flags:
            kwargs['creationflags'] = flags

        try:
            self._process = subprocess.Popen(
                cmd, cwd=self.path.parent,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding="utf-8",
                **kwargs
            )
            # Read stdout char-by-char to handle both \r (progress bars) and \n.
            buf = ""
            while True:
                char = self._process.stdout.read(1)
                if not char:
                    break
                if char in ('\r', '\n'):
                    if buf.strip():
                        print(buf)
                        if "Error" in buf or "error" in buf:
                            error_lines.append(buf.strip())
                    buf = ""
                else:
                    buf += char

            self._process.wait()
            is_cancelled = self._cancel_event.is_set()
            success = (self._process.returncode == 0 and not is_cancelled)
            if success:
                edited_seconds = self._post_process_xml()
            elif is_cancelled:
                error_hint = "cancelled"
            elif error_lines:
                combined = " ".join(error_lines)
                if re.search(r"audio stream .+ does not exist", combined, re.IGNORECASE):
                    error_hint = "missing_track"
        except Exception as e:
            print(f"Error in {self.path}: {e}")
        finally:
            self._process = None

        self._signals.file_finished.emit(path_key, success, error_hint, edited_seconds)

    def _post_process_xml(self) -> float:
        """Fix file:/// URIs and return the edited sequence duration in seconds.

        Reads the top-level <duration> (frames) and <timebase> (fps) from the
        sequence element.  Returns -1.0 if the XML is absent or unparseable.
        """
        xml_path = self.path.parent / f"{self.path.stem}_ALTERED.xml"
        if not xml_path.exists():
            return -1.0
        try:
            import xml.etree.ElementTree as ET
            text = xml_path.read_text(encoding="utf-8")

            # Fix bare Windows pathurls so Premiere links media automatically.
            fixed = re.sub(
                r'(<pathurl>)([A-Za-z]:)',
                lambda m: m.group(1) + "file:///" + m.group(2),
                text,
            )
            if fixed != text:
                xml_path.write_text(fixed, encoding="utf-8")
                print(f"Fixed pathurl URIs in {xml_path.name}")

            # Parse the sequence duration.
            root = ET.fromstring(fixed)
            seq = root.find("sequence")
            if seq is None:
                return -1.0
            duration_el = seq.find("duration")
            timebase_el = seq.find("rate/timebase")
            if duration_el is None or timebase_el is None:
                return -1.0
            return int(duration_el.text) / int(timebase_el.text)
        except Exception as e:
            print(f"Warning: could not post-process {xml_path.name}: {e}")
            return -1.0
