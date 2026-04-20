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
    """
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

    return [
        sys.executable, "-m", "auto_editor",
        str(path),
        "--margin", f"{options.margin}sec",
        "--edit", edit_expr,
        "--export", f"{options.export_option}:name={path.stem}",
    ]


class VideoProcessorSignals(QtCore.QObject):
    finished = QtCore.Signal()
    cancelled = QtCore.Signal()
    file_started = QtCore.Signal(str)          # str(path)
    file_progress = QtCore.Signal(str, float)  # str(path), percentage 0–100
    file_finished = QtCore.Signal(str, bool)   # str(path), success


class VideoProcessor(QtCore.QRunnable):

    def __init__(self, options: ProcessingOptions, video_files_to_edit: dict):
        super().__init__()
        self.signals = VideoProcessorSignals()
        self.options = options
        self.video_files_to_edit = video_files_to_edit
        self._cancel_event = threading.Event()
        self._current_worker: "VideoProcessorWorker | None" = None

    def cancel(self):
        """Request cancellation. Stops the next file from starting and
        terminates any subprocess that is currently running."""
        self._cancel_event.set()
        if self._current_worker is not None:
            self._current_worker.terminate()

    def run(self):
        for file_path in self.video_files_to_edit:
            if self._cancel_event.is_set():
                break
            self._current_worker = VideoProcessorWorker(
                options=self.options,
                path=file_path,
                cancel_event=self._cancel_event,
                signals=self.signals,
            )
            self._current_worker.run()

        self._current_worker = None
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
                        m = re.search(r'(\d+(?:\.\d+)?)\s*%', buf)
                        if m:
                            self._signals.file_progress.emit(path_key, float(m.group(1)))
                    buf = ""
                else:
                    buf += char

            self._process.wait()
            success = (self._process.returncode == 0
                       and not self._cancel_event.is_set())
            if success:
                self._fix_xml_pathurls()
        except Exception as e:
            print(f"Error in {self.path}: {e}")
        finally:
            self._process = None

        self._signals.file_finished.emit(path_key, success)

    def _fix_xml_pathurls(self):
        """Rewrite bare Windows paths in the generated XML to file:/// URIs.

        auto-editor writes <pathurl>C:/...</pathurl> which Premiere cannot
        resolve automatically. Converting to file:///C:/... makes the import
        link the media without any manual intervention.
        """
        xml_path = self.path.parent / f"{self.path.stem}_ALTERED.xml"
        if not xml_path.exists():
            return
        try:
            text = xml_path.read_text(encoding="utf-8")
            # Replace any pathurl that starts with a drive letter (no scheme yet).
            fixed = re.sub(
                r'(<pathurl>)([A-Za-z]:)',
                lambda m: m.group(1) + "file:///" + m.group(2),
                text,
            )
            if fixed != text:
                xml_path.write_text(fixed, encoding="utf-8")
                print(f"Fixed pathurl URIs in {xml_path.name}")
        except Exception as e:
            print(f"Warning: could not fix pathurls in {xml_path.name}: {e}")
