import sys
import subprocess
from PySide6 import QtWidgets
from batch_editor_controller import BatchEditorController


def _check_auto_editor() -> bool:
    """Return True if auto-editor is importable from the current Python."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "auto_editor", "--version"],
            capture_output=True, timeout=10,
        )
        return result.returncode == 0
    except Exception:
        return False


def main():
    app = QtWidgets.QApplication(sys.argv)

    if not _check_auto_editor():
        QtWidgets.QMessageBox.critical(
            None,
            "Missing dependency — auto-editor",
            "<b>auto-editor</b> was not found for the current Python interpreter."
            "<br><br>"
            "Install it by running:<br>"
            f"<code>&nbsp;&nbsp;{sys.executable} -m pip install auto-editor</code>"
            "<br><br>"
            "The application will now exit.",
        )
        sys.exit(1)

    controller = BatchEditorController()
    controller.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
