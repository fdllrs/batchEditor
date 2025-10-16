from PySide6 import QtCore
from pathlib import Path
from utils import videoLength


VIDEOFORMATS= ("mp4", "mkv")


class Worker(QtCore.QObject):

    partiallyFinished = QtCore.Signal(object) 
    finished = QtCore.Signal()         # emits result

    def __init__(self, *args):
        super().__init__()

        self.videoFilesFound = {}
        self._running = True


    def startSearch(self, directoryPath: Path):

        self.searchDirectory(directoryPath)
        self.finished.emit()



    def searchDirectory(self, directoryPath: Path):
        directoryElements = directoryPath.iterdir()
        for item in directoryElements:
            if str(item).endswith(VIDEOFORMATS):
                self.addRecording(item)


            elif item.is_dir():
                self.searchDirectory(item)
        self.partiallyFinished.emit(self.videoFilesFound)


    def addRecording(self, itemPath):

        duration = videoLength(itemPath)
        self.videoFilesFound[itemPath] = duration

    def stop(self):
        self._running = False