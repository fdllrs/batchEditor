import sys
import subprocess
from PySide6 import QtWidgets
from batch_editor_controller import BatchEditorController


def _get_auto_editor_base_cmd() -> list[str]:
    """Return the base command to invoke auto-editor."""
    import sys
    if getattr(sys, 'frozen', False):
        return ["auto-editor"]
    return [sys.executable, "-m", "auto_editor"]


def _check_auto_editor() -> bool:
    """Return True if auto-editor is importable or in PATH."""
    try:
        cmd = _get_auto_editor_base_cmd() + ["--version"]
        kwargs = {}
        if hasattr(subprocess, 'CREATE_NO_WINDOW'):
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW

        result = subprocess.run(
            cmd,
            capture_output=True, timeout=10,
            **kwargs
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
