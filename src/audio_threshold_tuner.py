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

    def __init__(
        self,
        num_tracks: int,
        thresholds: list[float],
        parent: QtWidgets.QWidget | None = None,
    ):
        super().__init__(parent)
        self._num_tracks = num_tracks
        self._initial_thresholds = list(thresholds)
        self._sliders: list[QtWidgets.QSlider] = []
        self._spinboxes: list[QtWidgets.QDoubleSpinBox] = []
        self._setup_ui()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_thresholds(self) -> list[float]:
        """Return current threshold values (%) from each spin-box."""
        return [sb.value() for sb in self._spinboxes]

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
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        container = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(container)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(8)
        grid.setContentsMargins(10, 10, 10, 10)

        for i in range(self._num_tracks):
            label = QtWidgets.QLabel(f"Track {i + 1} silence threshold:")
            label.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
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

            initial = (
                self._initial_thresholds[i]
                if i < len(self._initial_thresholds)
                else 0.0
            )
            # Set spinbox first (no signal yet), then sync slider silently.
            spinbox.setValue(initial)
            slider.setValue(int(initial * self._SLIDER_SCALE))

            # Two-way sync — use default-argument capture to avoid late-binding.
            slider.valueChanged.connect(
                lambda val, sb=spinbox: self._on_slider_changed(val, sb)
            )
            spinbox.valueChanged.connect(
                lambda val, sl=slider: self._on_spinbox_changed(val, sl)
            )

            self._sliders.append(slider)
            self._spinboxes.append(spinbox)

            grid.addWidget(label, i, 0)
            grid.addWidget(slider, i, 1)
            grid.addWidget(spinbox, i, 2)

        # Label col fixed; slider col stretches; spinbox col fixed.
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

    def _on_slider_changed(self, value: int, spinbox: QtWidgets.QDoubleSpinBox):
        spinbox.blockSignals(True)
        spinbox.setValue(value / self._SLIDER_SCALE)
        spinbox.blockSignals(False)

    def _on_spinbox_changed(self, value: float, slider: QtWidgets.QSlider):
        slider.blockSignals(True)
        slider.setValue(int(value * self._SLIDER_SCALE))
        slider.blockSignals(False)
