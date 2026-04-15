from PySide6 import QtWidgets
from UI.thresholdTunerUI.batchEditor_audioThresholdTuner_ui import Ui_audioThresholdTunerDialog


MAX_AUDIO_TRACKS = 7


class AudioThresholdTuner(QtWidgets.QDialog, Ui_audioThresholdTunerDialog):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sliders = []
        self.spinboxes = []
        for i in range(1, MAX_AUDIO_TRACKS + 1):
            slider = getattr(self, f'audiothresholdSlider_{i}')
            spinbox = getattr(self, f'audioThresholdSpinbox_{i}')
            self.sliders.append(slider)
            self.spinboxes.append(spinbox)

            slider.valueChanged.connect(lambda value, idx=i: self.__update_spinbox_from_slider(value, idx-1))
            spinbox.valueChanged.connect(lambda value, idx=i: self.__update_slider_from_spinbox(value, idx-1))


    def __update_spinbox_from_slider(self, value, i):
        spinbox = self.spinboxes[i]
        spinbox.blockSignals(True)
        spinbox.setValue(value / 100)
        spinbox.blockSignals(False)

    def __update_slider_from_spinbox(self, value, i):
        slider = self.sliders[i]
        slider.blockSignals(True)
        slider.setValue(value * 100)
        slider.blockSignals(False)
