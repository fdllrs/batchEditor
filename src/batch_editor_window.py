import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from UI.mainWindowUI.batchEditor_ui import Ui_BatchEditor
from pathlib import Path
from utils import total_length_minutes
from video_finder import VideoFinder
from video_processor import VideoProcessor
from processing_options import ProcessingOptions
from audio_threshold_tuner import AudioThresholdTuner

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

        self.foundFilesProgressBar.setVisible(False)
        self.progressBarLabel.setVisible(False)

        self.startButton.clicked.connect(self.controller.start)
        self.multitrackTuningButton.clicked.connect(self.controller.open_audio_threshold_tuner_dialog)
        self.selectRootDirectoryButton.clicked.connect(self.controller.set_root_directory)
        self.minLengthSpinbox.valueChanged.connect(self.controller.update_to_edit_files)
        self.saveConfigButton.clicked.connect(self.controller.save_config)
        self.loadConfigButton.clicked.connect(self.controller.load_config)
        self.showCommandButton.clicked.connect(self.controller.show_command)

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
