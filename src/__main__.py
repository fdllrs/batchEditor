import sys
from PySide6 import QtWidgets
from batch_editor_controller import BatchEditorController


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = BatchEditorController()
    controller.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
