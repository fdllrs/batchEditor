import sys
from PySide6 import QtCore
from processing_options import ProcessingOptions
from pathlib import Path
import subprocess


def build_command(options: ProcessingOptions, path: Path) -> list[str]:
    """Return the auto-editor command list for a single file."""
    track_clauses = " ".join(
        f"audio:stream={i},threshold={t}%"
        for i, t in enumerate(options.track_thresholds)
    )
    edit_expr = f"(or {track_clauses})"
    cmd = [
        sys.executable, "-m", "auto_editor",
        str(path),
        "--margin", f"{options.margin}sec",
        "--edit", edit_expr,
        "--export", f'{options.export_option}:name="{path.stem}"',
    ]
    return cmd


class VideoProcessor(QtCore.QRunnable):

    def __init__(self, options: ProcessingOptions, to_edit):
        super().__init__()
        self.signals = VideoProcessorSignals()
        self.options = options
        self.video_files_to_edit = to_edit
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(1)


    def run(self):
        for file_path in self.video_files_to_edit.keys():
            print(str(file_path))
            self.worker = VideoProcessorWorker(options=self.options, path=file_path, signal=self.signals.partially_finished)
            self.threadpool.start(self.worker)

        self.threadpool.waitForDone()
        self.signals.finished.emit()






class VideoProcessorSignals(QtCore.QObject):
    partially_finished = QtCore.Signal() 
    finished = QtCore.Signal()



class VideoProcessorWorker(QtCore.QRunnable):


    def __init__(self, options: ProcessingOptions, path: Path, signal):
        super().__init__()
        self.options = options
        self.path = path
        self.signal = signal


    def run(self):
        self.run_command()
        self.signal.emit()

    def run_command(self):
        print(f"Processing: {self.path.stem}")
        cmd = build_command(self.options, self.path)
        print(f"Running command: {' '.join(cmd)}")
        try:
            subprocess.run(cmd, cwd=self.path.cwd(), check=True, text=True, encoding="utf-8")
        except subprocess.CalledProcessError as e:
            print(f"Error in {self.path}: {e}")
