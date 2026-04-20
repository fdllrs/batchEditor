from PySide6 import QtWidgets, QtCore, QtGui


_STEPS = [
    (
        "1 — Select a root directory",
        "Click <b>Select root directory</b> and choose the folder that contains "
        "your video files. The app will recursively scan it and display the "
        "number of files found along with their total duration.",
    ),
    (
        "2 — (Optional) Edit selected files",
        "Click <b>Edit selected files</b> to open the file list. "
        "Use the checkboxes to include or exclude individual videos from the batch "
        "before processing starts.",
    ),
    (
        "3 — Configure export options",
        "Switch to the <b>Configure</b> tab and choose the NLE you want to export "
        "for (Premiere Pro, DaVinci Resolve, etc.). "
        "Set the <b>margin</b> to control how many seconds of padding are kept "
        "around each loud segment.",
    ),
    (
        "4 — Tune audio thresholds",
        "Click <b>Configure silence thresholds</b> to open the multitrack tuner. "
        "Each audio stream gets its own slider. "
        "Higher values mark more of the audio as silence; lower values are more "
        "permissive. Disable a track entirely to exclude it from the silence "
        "detection logic.",
    ),
    (
        "5 — (Optional) Save / Load config",
        "Use <b>Save config</b> to persist the current settings to a <code>.txt</code> "
        "file. Use <b>Load config</b> later to restore them. "
        "This is useful when switching between different recording setups.",
    ),
    (
        "6 — Preview the command",
        "Click <b>Show command</b> to see the exact <code>auto-editor</code> "
        "command that will be run. You can copy it to the clipboard and run it "
        "manually if needed.",
    ),
    (
        "7 — Start processing",
        "Click <b>Start</b> to open the processing window. "
        "A table shows every file with its current status (<i>Queued</i>, "
        "<i>Processing</i>, <i>Done</i>, or <i>Failed</i>) and a live progress "
        "percentage updated in real time. "
        "Hit <b>Cancel</b> at any time to stop after the current file finishes. "
        "When the batch completes, the window shows a summary with the total "
        "number of files processed and the elapsed time.",
    ),
]


class HelpDialog(QtWidgets.QDialog):
    """Modal dialog that walks the user through how to use Batch Editor."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("How to use Batch Editor")
        self.setMinimumWidth(480)
        self.setMinimumHeight(340)
        self.setSizeGripEnabled(True)
        self._build_ui()

    def _build_ui(self):
        root = QtWidgets.QVBoxLayout(self)
        root.setSpacing(12)
        root.setContentsMargins(16, 16, 16, 16)

        # Scrollable area for all steps
        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        content = QtWidgets.QWidget()
        steps_layout = QtWidgets.QVBoxLayout(content)
        steps_layout.setSpacing(10)
        steps_layout.setContentsMargins(0, 0, 8, 0)

        for title, body in _STEPS:
            steps_layout.addWidget(self._make_step_widget(title, body))

        steps_layout.addStretch()
        scroll.setWidget(content)
        root.addWidget(scroll)

        # Close button
        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(self.reject)
        root.addWidget(buttons)

    @staticmethod
    def _make_step_widget(title: str, body: str) -> QtWidgets.QFrame:
        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        layout = QtWidgets.QVBoxLayout(frame)
        layout.setSpacing(4)
        layout.setContentsMargins(10, 8, 10, 8)

        title_label = QtWidgets.QLabel(title)
        title_font = title_label.font()
        title_font.setBold(True)
        title_label.setFont(title_font)

        body_label = QtWidgets.QLabel(body)
        body_label.setWordWrap(True)
        body_label.setTextFormat(QtCore.Qt.TextFormat.RichText)

        layout.addWidget(title_label)
        layout.addWidget(body_label)
        return frame
