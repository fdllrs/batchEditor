import sys
from PySide6 import QtWidgets
from UI.mainWindowUI.batchEditor_ui import Ui_BatchEditor
from help_dialog import HelpDialog

EXPORT_OPTIONS = {
    'Premiere Pro': 'premiere',
    'Da Vinci Resolve': 'resolve',
    'Final Cut Pro': 'final-cut-pro',
    'ShotCut': 'shotcut',
    'Kdenlive': 'kdenlive',
    'clip sequence': 'clip-sequence',
}


class BatchEditorWindow(QtWidgets.QMainWindow, Ui_BatchEditor):

    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        # Add tooltips for MainWindow buttons

        self.tabWidget.setCornerWidget(self.helpButton)


        self.startButton.clicked.connect(self.controller.startProcessing)
        self.multitrackTuningButton.clicked.connect(self.controller.open_audio_threshold_tuner_dialog)
        self.selectRootDirectoryButton.clicked.connect(self.controller.set_root_directory)
        self.saveConfigButton.clicked.connect(self.controller.save_config)
        self.loadConfigButton.clicked.connect(self.controller.load_config)
        self.showCommandButton.clicked.connect(self.controller.show_command)
        self.editSelectedFilesButton.clicked.connect(self.controller.open_clip_selector_dialog)
        self.helpButton.clicked.connect(self._show_help)
        



    def _show_help(self):
        HelpDialog(parent=self).exec()


if __name__ == "__main__":
    from batch_editor_controller import BatchEditorController
    app = QtWidgets.QApplication(sys.argv)
    controller = BatchEditorController()
    controller.view.show()
    sys.exit(app.exec())
