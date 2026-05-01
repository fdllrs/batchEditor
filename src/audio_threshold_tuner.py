from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class AudioThresholdTuner(QtWidgets.QDialog):
    """Per-track audio silence threshold dialog.

    Displays one row per audio track, each with a label, a horizontal slider,
    and a linked QDoubleSpinBox (0.00 – 100.00 %).

    Args:
        num_tracks:  Number of audio tracks to show rows for.
        thresholds:  Pre-populated threshold values (in %). Tracks beyond
                     the length of this list default to 0.0.
        parent:      Optional parent widget.
    """

    # Each integer unit on the slider represents 0.01 %.
    _SLIDER_SCALE = 100
    _DEFAULT_THRESHOLD = 4.0

    def __init__(
        self,
        num_tracks: int,
        thresholds: list[float],
        parent: QtWidgets.QWidget | None = None,
    ):
        super().__init__(parent)
        self._num_tracks = num_tracks
        self._initial_thresholds = list(thresholds)
        self._checkboxes: list[QtWidgets.QCheckBox] = []
        self._sliders: list[QtWidgets.QSlider] = []
        self._spinboxes: list[QtWidgets.QDoubleSpinBox] = []
        self._setup_ui()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_thresholds(self) -> list[float]:
        """Return current threshold values (%) from spin-boxes (or -1.0 if excluded)."""
        return [
            sb.value() if cb.isChecked() else -1.0
            for cb, sb in zip(self._checkboxes, self._spinboxes)
        ]

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _setup_ui(self):
        self.setWindowTitle("Multitrack Audio Threshold Tuning")
        self.setMinimumWidth(540)

        outer_layout = QtWidgets.QVBoxLayout(self)

        # Scroll area so the dialog stays compact even with many tracks ---
        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        container = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(container)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(8)
        grid.setContentsMargins(10, 10, 10, 10)

        for i in range(self._num_tracks):
            self._add_track_row(grid, i)

        # check col fixed; slider col stretches; spinbox col fixed.
        grid.setColumnStretch(0, 0)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 0)

        scroll.setWidget(container)
        outer_layout.addWidget(scroll)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok
            | QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        outer_layout.addWidget(button_box)

    def _add_track_row(self, grid: QtWidgets.QGridLayout, index: int):
        checkbox = QtWidgets.QCheckBox(f"Include Track {index + 1}")
        checkbox.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )

        slider = QtWidgets.QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 10000)
        slider.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )

        spinbox = QtWidgets.QDoubleSpinBox()
        spinbox.setRange(0.00, 100.00)
        spinbox.setDecimals(2)
        spinbox.setSingleStep(0.01)
        spinbox.setSuffix(" %")
        spinbox.setFixedWidth(120)

        initial_raw = (
            self._initial_thresholds[index]
            if index < len(self._initial_thresholds)
            else -1.0
        )

        # -1.0 is the definitive "excluded" marker.
        is_enabled = (initial_raw >= 0.0)
        display_val = initial_raw if is_enabled else self._DEFAULT_THRESHOLD

        spinbox.setValue(display_val)
        slider.setValue(int(display_val * self._SLIDER_SCALE))

        checkbox.setChecked(is_enabled)
        slider.setEnabled(is_enabled)
        spinbox.setEnabled(is_enabled)

        slider.valueChanged.connect(
            lambda val, sb=spinbox: self._on_slider_changed(val, sb)
        )
        spinbox.valueChanged.connect(
            lambda val, sl=slider: self._on_spinbox_changed(val, sl)
        )
        checkbox.toggled.connect(slider.setEnabled)
        checkbox.toggled.connect(spinbox.setEnabled)

        self._checkboxes.append(checkbox)
        self._sliders.append(slider)
        self._spinboxes.append(spinbox)

        grid.addWidget(checkbox, index, 0)
        grid.addWidget(slider, index, 1)
        grid.addWidget(spinbox, index, 2)

    def _on_slider_changed(self, value: int,
                           spinbox: QtWidgets.QDoubleSpinBox):
        spinbox.blockSignals(True)
        spinbox.setValue(value / self._SLIDER_SCALE)
        spinbox.blockSignals(False)

    def _on_spinbox_changed(self, value: float, slider: QtWidgets.QSlider):
        slider.blockSignals(True)
        slider.setValue(int(value * self._SLIDER_SCALE))
        slider.blockSignals(False)
