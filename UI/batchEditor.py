import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from batchEditor_ui import Ui_BatchEditor
from pathlib import Path
from utils import * 
from worker import Worker



class batchEditorWindow(QtWidgets.QMainWindow, Ui_BatchEditor):

    options = {}
    send_to_worker = QtCore.Signal(Path)  

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.videoFilesFound = {}
        self.videoFilesToEdit = {}
        self.foundFilesProgressBar.setVisible(False)
        self.progressBarLabel.setVisible(False)

        self.startButton.clicked.connect(self.start)
        self.selectRootDirectoryButton.clicked.connect(self.setRootDirectory)
        self.minLengthSpinbox.valueChanged.connect(self.updateToEditFiles)


        self.audiothresholdSlider.valueChanged.connect(self.__updateSpinboxFromSlider)
        self.audioThresholdSpinbox.valueChanged.connect(self.__updateSliderFromSpinbox)


    def start(self):
        self.options['exportOption'] = self.exportSelector.currentText()
        self.options['directory'] = self.rootDirectoryLabel.text() 
        self.options['threshold'] = self.audioThresholdSpinbox.value()
        self.options['filesIntoFolders'] = self.organizeIntoFolders.isChecked()
        self.options['splitOnly'] = self.splitOnly.isChecked()
        self.options['preview'] = self.preview.isChecked()
        self.options['separateTracks'] = self.separateTracks.isChecked()



        print(self.options)


        # self.startButton.setEnabled(False)



    def __updateSpinboxFromSlider(self, value):
        self.audioThresholdSpinbox.blockSignals(True)
        self.audioThresholdSpinbox.setValue(value / 100)
        self.audioThresholdSpinbox.blockSignals(False)

    def __updateSliderFromSpinbox(self, value):
        self.audiothresholdSlider.blockSignals(True)
        self.audiothresholdSlider.setValue(value * 100)
        self.audiothresholdSlider.blockSignals(False)



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
        self.foundFilesProgressBar.reset()

        self.progressBarLabel.setVisible(True)
        self.progressBarLabel.setText('Working...')
        self.foundFilesProgressBar.setVisible(True)

        self.foundFilesProgressBar.setRange(0,0)


        self.__prepareThread()

        self.send_to_worker.emit(Path(folder_path))
        self.mythread.start()



    def onPartiallyFinished(self, filesFound):
        
        self.videoFilesFound = filesFound
        self.filesFoundSpinbox.setText(str(len(self.videoFilesFound)))

        
    def onSearchFinished(self):

        self.progressBar.reset()
        self.progressBarDone()

        self.updateToEditFiles(self.minLengthSpinbox.value())
        self.totalLengthFoundSpinbox.setText(str(self.totalLengthOf(self.videoFilesFound)))

    def progressBarDone(self):
        self.progressBarLabel.setText('Done!')
        self.foundFilesProgressBar.setRange(0, 100)
        self.foundFilesProgressBar.setValue(100)




    def updateToEditFiles(self, minLengthMinutes):

        self.toEditLength = 0
        self.videoFilesToEdit = {}
        minLengthSeconds = minLengthMinutes * 60


        for file_path, duration in self.videoFilesFound.items():
            

            if duration > minLengthSeconds:
                self.videoFilesToEdit[file_path] = duration
                self.toEditLength += duration

        self.filesToEditSpinbox.setText(str(len(self.videoFilesToEdit)))
        self.totalLengthToEditSpinbox.setText(str(self.totalLengthOf(self.videoFilesToEdit)))


    def totalLengthOf(self, dict):
        return round(sum(dict.values()) / 60, 2 )

   




    def __prepareThread(self):
        self.mythread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.mythread)
        self.send_to_worker.connect(self.worker.startSearch)
        
        
        self.worker.partiallyFinished.connect(self.onPartiallyFinished)

        self.worker.finished.connect(self.mythread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.mythread.finished.connect(self.mythread.deleteLater)
        self.mythread.finished.connect(self.onSearchFinished)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = batchEditorWindow()
    window.show()
    sys.exit(app.exec())
