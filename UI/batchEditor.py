import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
from batchEditor_ui import Ui_BatchEditor
from pathlib import Path
from utils import * 

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

class batchEditorWindow(QtWidgets.QMainWindow, Ui_BatchEditor):

    options = {}
    send_to_worker = QtCore.Signal(Path)  

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.videoFilesFound = {}
        self.startButton.clicked.connect(self.start)
        self.selectRootDirectoryButton.clicked.connect(self.setRootDirectory)


    def start(self):
        self.options['exportOption'] = self.exportSelector.currentText()
        self.options['directory'] = self.rootDirectoryLabel.text() 
        self.options['threshold'] = self.audioThresholdSpinbox.value()


        print(self.audiothresholdSlider.value())
        print(self.options)


        # self.startButton.setText('working...')
        # self.startButton.setEnabled(False)




    def setRootDirectory(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Root Directory")


        if folder_path:
            self.rootDirectoryLabel.setText(folder_path)
            self.startButton.setEnabled(True)


            self.searchVideoFiles(folder_path)




        else:
            self.rootDirectoryLabel.setText(self.rootDirectoryLabel.placeholderText())
            self.startButton.setEnabled(False)




    def searchVideoFiles(self, folder_path):
        self.mythread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.mythread)

        self.send_to_worker.connect(self.worker.searchDirectory)


        self.mythread.started.connect(self.worker.searchDirectory)
        self.worker.finished.connect(self.onSearchFinished)
        self.worker.finished.connect(self.mythread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.mythread.finished.connect(self.mythread.deleteLater)

        # start
        self.mythread.start()
        self.send_to_worker.emit(Path(folder_path))



    def onSearchFinished(self, result):
        
        self.videoFilesFound = result
        self.filesFoundLabel.setText(str(len(self.videoFilesFound)))

    



    def updateToEditVideoFiles(self, newThreshholdMinutes):

        self.toEditLength = 0

        filtered_dict = {}

        newThreshholdSeconds = newThreshholdMinutes *60
        for file_path, duration in self.videoFilesFound.items():
            if duration > newThreshholdSeconds:
                filtered_dict[file_path] = duration
                self.toEditLength += duration

        
        self.videoFilesToEdit = filtered_dict
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = batchEditorWindow()
    window.show()
    sys.exit(app.exec())







