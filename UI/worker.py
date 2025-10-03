from PySide6 import QtCore
from pathlib import Path
from utils import videoLength


VIDEOFORMATS= ("mp4", "mkv")


class Worker(QtCore.QObject):
    finished = QtCore.Signal(object)         # emits result

    def __init__(self, *args):
        super().__init__()

        self.videoFilesFound = {}
        self._running = True





    def searchDirectory(self, directoryPath: Path):
        directoryElements = directoryPath.iterdir()
        print(len(self.videoFilesFound))
        for item in directoryElements:
            if str(item).endswith(VIDEOFORMATS):
                self.addRecording(item)


            elif item.is_dir():
                self.searchDirectory(item)
        self.finished.emit(self.videoFilesFound)


    def addRecording(self, itemPath):

        duration = videoLength(itemPath)
        self.videoFilesFound[itemPath] = duration

    def stop(self):
        self._running = False