import os
from PySide6 import QtCore
from utils import * 
from pathlib import Path
import subprocess



class videoProcessor(QtCore.QRunnable):

    def __init__(self, options, toEdit):
        super().__init__()
        self.signals = videoProcessorSignals()
        self.options = options
        self.videoFilesToEdit = toEdit
        self.threadpool = QtCore.QThreadPool()


    def run(self):
        for filePath in self.videoFilesToEdit.keys():
            
            self.worker = videoProcessorWorker(options=self.options, path=filePath, signal=self.signals.partiallyFinished)
            self.threadpool.start(self.worker)


        self.signals.finished.emit()





class videoProcessorSignals(QtCore.QObject):
    partiallyFinished = QtCore.Signal() 
    finished = QtCore.Signal()



class videoProcessorWorker(QtCore.QRunnable):


    def __init__(self, options, path, signal):
        super().__init__()
        self.options = options
        self.path = path
        self.signal = signal


    def run(self):
        self.runcommand()
        self.signal.emit()


    def runcommand(self):
        autoEditorCommand = f'py -m auto_editor {self.path} --margin 0.03sec --edit  "(or audio:stream=0 audio:threshold=0.7%, audio:stream=1 audio:threshold=2%, audio:stream=2 audio:threshold=1%)" --export premiere'
        try:
            subprocess.run(
                autoEditorCommand,
                cwd=self.path.cwd(),
                check=True,
                text=True,
                encoding="utf-8",
            )

        except subprocess.CalledProcessError as e:
            print(f"Error in {self.path}: {e}")
