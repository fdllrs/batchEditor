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


def _check_python() -> bool:
    """Return True if python or py is available on the system."""
    import shutil
    return bool(shutil.which("python") or shutil.which("python3") or shutil.which("py"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    is_frozen = getattr(sys, 'frozen', False)

    if is_frozen and not _check_python():
        QtWidgets.QMessageBox.critical(
            None,
            "Missing dependency — Python",
            "<b>Python</b> was not found on this system."
            "<br><br>"
            "This application requires Python to run <b>auto-editor</b>.<br>"
            "Please install Python from <a href='https://www.python.org/downloads/'>python.org</a> "
            "and ensure it is added to your system PATH."
            "<br><br>"
            "The application will now exit.",
        )
        sys.exit(1)

    if not _check_auto_editor():
        msg = (
            "<b>auto-editor</b> was not found on this system.<br><br>"
            "Please install auto-editor from <a href='https://github.com/WyattBlue/auto-editor/releases/'>github.com</a> "
            "<br><br>"
            "The application will now exit."
        )

        QtWidgets.QMessageBox.critical(
            None,
            "Missing dependency — auto-editor",
            msg,
        )
        sys.exit(1)

    controller = BatchEditorController()
    controller.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
