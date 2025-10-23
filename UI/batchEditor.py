import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from batchEditor_ui import Ui_BatchEditor
from pathlib import Path
from utils import * 
from videoFinder import videoFinder
from videoProcessor import videoProcessor
from batchEditor_audioThresholdTuner_ui import Ui_audioThresholdTunerDialog


EXPORT_OPTIONS = {'Premiere Pro': 'premiere',
                  'Da Vinci Resolve': 'resolve',
                  'Final Cut Pro': 'final-cut-pro',
                  'ShotCut': 'shotcut',
                  'Kdenlive': 'kdenlive',
                  'clip sequence': 'clip-secuence'}
class batchEditorWindow(QtWidgets.QMainWindow, Ui_BatchEditor):

    options = {}
    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.videoFilesFound = {}
        self.videoFilesToEdit = {}
        self.threadpool = QtCore.QThreadPool()
        self.maxAudioChannels = 1
        print(f'multithreading with maximum {self.threadpool.maxThreadCount()} threads')
    
    
    
        # self.foundFilesProgressBar.setVisible(False)
        # self.progressBarLabel.setVisible(False)

        self.startButton.clicked.connect(self.start)
        self.multitrackTuningButton.clicked.connect(self.openAudioThresholdTunerDialog)
        self.selectRootDirectoryButton.clicked.connect(self.setRootDirectory)
        self.minLengthSpinbox.valueChanged.connect(self.updateToEditFiles)


        self.audiothresholdSlider.valueChanged.connect(self.__updateSpinboxFromSlider)
        self.audioThresholdSpinbox.valueChanged.connect(self.__updateSliderFromSpinbox)


    def start(self):
        self.options['exportOption'] = EXPORT_OPTIONS[self.exportSelector.currentText()]
        self.options['directory'] = self.rootDirectoryLabel.text() 
        self.options['threshold'] = self.audioThresholdSpinbox.value()
        self.options['filesIntoFolders'] = self.organizeIntoFolders.isChecked()
        self.options['splitOnly'] = self.splitOnly.isChecked()
        self.options['separateTracks'] = self.separateTracks.isChecked()
        self.progressBar.reset()
        self.progressBar.setRange(0, len(self.videoFilesToEdit))


        # print(self.options)
        self.startButton.setEnabled(False)
        self.processor = videoProcessor(options=self.options, toEdit=self.videoFilesToEdit)
        self.processor.signals.finished.connect(self.onProcessingFinished)
        self.processor.signals.partiallyFinished.connect(self.onProcessingPartiallyFinished)
        self.threadpool.start(self.processor)

    def onProcessingPartiallyFinished(self):
        self.progressBar.setValue(self.progressBar.value() + 1)




    def onProcessingFinished(self):
       print('done')


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


        self.videoFinder = videoFinder(path=Path(folder_path))
        self.videoFinder.signals.partiallyFinished.connect(self.onPartiallyFinished)
        self.videoFinder.signals.finished.connect(self.onSearchFinished)
        self.threadpool.start(self.videoFinder)



    def onPartiallyFinished(self, filesFound):
        self.videoFilesFound = filesFound
        self.filesFound.setText(str(len(self.videoFilesFound)))

        
    def onSearchFinished(self, maxAudioChannels):

        self.foundFilesProgressBar.reset()
        self.progressBarDone()

        self.updateToEditFiles(self.minLengthSpinbox.value())
        self.totalLength.setText(totalLengthMinutes(self.videoFilesFound) + ' min')




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
        self.totalLengthToEditSpinbox.setText(totalLengthMinutes(self.videoFilesToEdit))


    def openAudioThresholdTunerDialog(self):
        self.dialogWindow = QtWidgets.QDialog()
        self.thresholdTuner = Ui_audioThresholdTunerDialog()
        self.thresholdTuner.setupUi(self.dialogWindow)
        self.dialogWindow.show()

    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = batchEditorWindow()
    window.show()
    sys.exit(app.exec())
