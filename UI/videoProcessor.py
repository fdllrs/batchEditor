import os
from PySide6 import QtCore
from utils import * 
from pathlib import Path
import subprocess



class videoProcessor(QtCore.QObject):


    send_to_worker = QtCore.Signal(Path)  


    def __init__(self, options):
        super().__init__()
        
        self.options = options


    def process(self, path):

        self.__prepareThread()

        self.send_to_worker.emit(path)
        self.mythread.start()




    def __prepareThread(self):
        self.mythread = QtCore.QThread()
        self.worker = processorWorker()
        self.worker.moveToThread(self.mythread)
        self.send_to_worker.connect(self.worker.runcommand)
        
        
        self.worker.partiallyFinished.connect(self.onPartiallyFinished)

        self.worker.finished.connect(self.mythread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.mythread.finished.connect(self.mythread.deleteLater)
        self.mythread.finished.connect(self.onSearchFinished)



    def onPartiallyFinished(self):
        print("partially done")



    def onSearchFinished(self):
        print("done")




class processorWorker(QtCore.QObject):

    partiallyFinished = QtCore.Signal(object) 
    finished = QtCore.Signal()         # emits result




    def runcommand(self, videoPath: Path):
        autoEditorCommand = f'py -m auto_editor {videoPath} --margin 0.03sec --edit  "(or audio:stream=0 audio:threshold=0.7%, audio:stream=1 audio:threshold=2%, audio:stream=2 audio:threshold=1%)" --export premiere'
        try:
            subprocess.run(
                autoEditorCommand,
                cwd=videoPath.cwd(),
                check=True,
                text=True,
                encoding="utf-8",
            )

        except subprocess.CalledProcessError as e:
            print(f"Error in {videoPath}: {e.stderr}")


        self.finished.emit()
    