import sys
from PySide6 import QtWidgets
from UI.mainWindowUI.batchEditor_ui import Ui_BatchEditor

EXPORT_OPTIONS = {
    'Premiere Pro': 'premiere',
    'Da Vinci Resolve': 'resolve',
    'Final Cut Pro': 'final-cut-pro',
    'ShotCut': 'shotcut',
    'Kdenlive': 'kdenlive',
    'clip sequence': 'clip-secuence',
}


class BatchEditorWindow(QtWidgets.QMainWindow, Ui_BatchEditor):

    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller


        self.startButton.clicked.connect(self.controller.startProcessing)
        self.multitrackTuningButton.clicked.connect(self.controller.open_audio_threshold_tuner_dialog)
        self.selectRootDirectoryButton.clicked.connect(self.controller.set_root_directory)
        self.saveConfigButton.clicked.connect(self.controller.save_config)
        self.loadConfigButton.clicked.connect(self.controller.load_config)
        self.showCommandButton.clicked.connect(self.controller.show_command)
        self.editSelectedFilesButton.clicked.connect(self.controller.open_clip_selector_dialog)
        
        self.audiothresholdSlider.valueChanged.connect(self.__update_spinbox_from_slider)
        self.audioThresholdSpinbox.valueChanged.connect(self.__update_slider_from_spinbox)


    def __update_spinbox_from_slider(self, value):
        self.audioThresholdSpinbox.blockSignals(True)
        self.audioThresholdSpinbox.setValue(value / 100)
        self.audioThresholdSpinbox.blockSignals(False)

    def __update_slider_from_spinbox(self, value):
        self.audiothresholdSlider.blockSignals(True)
        self.audiothresholdSlider.setValue(value * 100)
        self.audiothresholdSlider.blockSignals(False)



if __name__ == "__main__":
    from batch_editor_controller import BatchEditorController
    app = QtWidgets.QApplication(sys.argv)
    controller = BatchEditorController()
    controller.view.show()
    sys.exit(app.exec())
