from PySide6 import QtCore
from pathlib import Path
from utils import videoLength


VIDEOFORMATS= ("mp4", "mkv")


class videoFinder(QtCore.QRunnable):

    def __init__(self, path):
        super().__init__()

        self.directoryPath = path
        self.videoFilesFound = {}
        self._running = True
        self.signals = videoFinderSignals()
        



    def run(self):

        self.searchDirectory(self.directoryPath)
        self.signals.finished.emit()


    def searchDirectory(self, directoryPath: Path):
        directoryElements = directoryPath.iterdir()
        for item in directoryElements:
            if str(item).endswith(VIDEOFORMATS):
                self.addRecording(item)


            elif item.is_dir():
                self.searchDirectory(item)
        self.signals.partiallyFinished.emit(self.videoFilesFound)


    def addRecording(self, itemPath):

        duration = videoLength(itemPath)
        self.videoFilesFound[itemPath] = duration





class videoFinderSignals(QtCore.QObject):

    partiallyFinished = QtCore.Signal(object)
    finished = QtCore.Signal()