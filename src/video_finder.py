from PySide6 import QtCore
from pathlib import Path
from utils import video_length, total_duration, audio_track_count


VIDEO_FORMATS = ("mp4", "mkv")

class VideoFinder(QtCore.QRunnable):

    
    def __init__(self, path):
        super().__init__()

        self.directory_path = path
        self.video_files_found = {}
        self._max_audio_tracks = 1
        self._running = True
        self.signals = VideoFinderSignals()



    def run(self):
        self.search_directory(self.directory_path)
        self.signals.finished.emit(self.video_files_found, self._max_audio_tracks)


    def search_directory(self, directory_path: Path):
        directory_elements = directory_path.iterdir()
        
        for item in directory_elements:
            if str(item).endswith(VIDEO_FORMATS):
                self.add_recording(item)


            elif item.is_dir():
                self.search_directory(item)


    def add_recording(self, path):
        self.video_files_found[path] = video_length(path)
        track_count = audio_track_count(path)
        if track_count > self._max_audio_tracks:
            self._max_audio_tracks = track_count
        self.signals.partially_finished.emit(len(self.video_files_found), total_duration(self.video_files_found))

class VideoFinderSignals(QtCore.QObject):

    partially_finished = QtCore.Signal(int, str)
    finished = QtCore.Signal(object, int)