import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
from batchEditor_ui import Ui_BatchEditor



class XXX(QtWidgets.QMainWindow, Ui_BatchEditor):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.startButton.clicked.connect(self.start)



    def start(self):
        print("starting")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = XXX()
    window.show()
    sys.exit(app.exec())