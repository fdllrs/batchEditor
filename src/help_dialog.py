from PySide6 import QtWidgets, QtCore, QtGui
from version import __version__


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
        "for (Premiere Pro, DaVinci Resolve, etc.) or clip-sequence to export a video file. "
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
        "file and set them as the <b>startup configuration</b>. "
        "The next time you open the app, your last saved settings will be "
        "restored automatically. "
        "Use <b>Load config</b> to restore settings from any previously saved file. "
        "If no saved configuration is found at startup, the app will notify you "
        "and fall back to default settings.",
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
        "<i>Processing</i>, <i>Done</i>, or <i>Failed</i>). "
        "Hit <b>Cancel</b> at any time to stop after the current file finishes. "
        "When the batch completes, the window shows a summary with the total "
        "number of files processed and the elapsed time.",
    ),
]


class HelpDialog(QtWidgets.QDialog):
    """Modal dialog that walks the user through how to use Batch Editor."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help")
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

        # Contact Panel
        contact_frame = QtWidgets.QFrame()
        contact_frame.setObjectName("ContactFrame")
        contact_frame.setStyleSheet("""
            QFrame#ContactFrame {
                background-color: rgba(128, 128, 128, 0.1);
                border: 1px solid rgba(128, 128, 128, 0.3);
                border-radius: 6px;
            }
        """)
        contact_layout = QtWidgets.QVBoxLayout(contact_frame)
        contact_layout.setContentsMargins(12, 12, 12, 12)
        
        contact_title = QtWidgets.QLabel("Contact & Support")
        contact_title_font = contact_title.font()
        contact_title_font.setBold(True)
        contact_title.setFont(contact_title_font)
        
        contact_body = QtWidgets.QLabel(
            "If you encounter issues or have feature requests, please report them on "
            "<a href='https://github.com/fdllrs/batchEditor/issues'>GitHub Issues</a>.<br>"
            "You can also reach out on Discord: <b>fdllrs</b>."
        )
        contact_body.setWordWrap(True)
        contact_body.setTextFormat(QtCore.Qt.TextFormat.RichText)
        contact_body.setOpenExternalLinks(True)
        
        contact_layout.addWidget(contact_title)
        contact_layout.addWidget(contact_body)
        
        steps_layout.addWidget(contact_frame)
        
        # Tutorial Title
        tutorial_title = QtWidgets.QLabel("How to use Batch Editor")
        tutorial_title_font = tutorial_title.font()
        tutorial_title_font.setBold(True)
        tutorial_title_font.setPointSize(tutorial_title_font.pointSize() + 2)
        tutorial_title.setFont(tutorial_title_font)
        tutorial_title.setContentsMargins(0, 8, 0, 4)
        
        steps_layout.addWidget(tutorial_title)

        for title, body in _STEPS:
            steps_layout.addWidget(self._make_step_widget(title, body))

        steps_layout.addStretch()
        scroll.setWidget(content)
        root.addWidget(scroll)

        # Footer with version and close button
        footer_layout = QtWidgets.QHBoxLayout()
        
        version_label = QtWidgets.QLabel(f"v{__version__} - made by fdllrs")
        version_label.setStyleSheet("color: gray;")
        
        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(self.reject)
        
        footer_layout.addWidget(version_label)
        footer_layout.addWidget(buttons)
        
        root.addLayout(footer_layout)

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
        body_label.setOpenExternalLinks(True)

        layout.addWidget(title_label)
        layout.addWidget(body_label)
        return frame
