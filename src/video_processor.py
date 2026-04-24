import sys
import re
import threading
from PySide6 import QtCore
from processing_options import ProcessingOptions
from pathlib import Path
import subprocess


def build_command(options: ProcessingOptions, path: Path) -> list[str]:
    """Return the auto-editor command list for a single file.

    Tracks with threshold < 0.0 are excluded — negative values are the
    internal sentinel for "this track is disabled".
    The -u flag forces Python to run unbuffered so progress output is
    emitted in real time even when stdout is piped.
    """
    base_command = [
        sys.executable, "-m", "auto_editor",
        str(path),
    ]
    if options.split_only:
        return base_command + [
            "--when-silent nil --when-normal nil",
            "--export", f"{options.export_option}:name={path.stem}",
        ]


    active_clauses = [
        f"audio:stream={i},threshold={t / 100}"
        for i, t in enumerate(options.track_thresholds)
        if t >= 0.0
    ]

    if len(active_clauses) == 1:
        edit_expr = active_clauses[0]
    elif len(active_clauses) > 1:
        edit_expr = f"(or {' '.join(active_clauses)})"
    else:
        # No active streams — fall back to auto-editor's default audio edit.
        edit_expr = "audio"

    return base_command + [
        "--margin", f"{options.margin}sec",
        "--edit", edit_expr,
        "--export", f"{options.export_option}:name={path.stem}",
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
            self._process.terminate()

    def run(self):
        path_key = str(self.path)
        self._signals.file_started.emit(path_key)
        cmd = build_command(self.options, self.path)
        print(f"Running command: {' '.join(cmd)}")
        success = False
        error_hint = ""
        edited_seconds = -1.0
        error_lines: list[str] = []
        try:
            self._process = subprocess.Popen(
                cmd, cwd=self.path.parent,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding="utf-8",
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
            success = (self._process.returncode == 0
                       and not self._cancel_event.is_set())
            if success:
                edited_seconds = self._post_process_xml()
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
