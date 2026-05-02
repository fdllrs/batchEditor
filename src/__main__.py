import sys
import subprocess
from PySide6 import QtWidgets, QtCore
from batch_editor_controller import BatchEditorController


from utils import get_auto_editor_path, get_auto_editor_version


def _is_valid_auto_editor(exe_path: str) -> bool:
    """Check if the given path points to a valid auto-editor executable."""
    try:
        result = get_auto_editor_version(exe_path)

        return result.returncode == 0
    except Exception:
        return False


def _check_auto_editor() -> bool:
    """Return True if the configured auto-editor is valid."""
    return _is_valid_auto_editor(get_auto_editor_path())


def _check_python() -> bool:
    """Return True if python or py is available on the system."""
    import shutil
    return bool(shutil.which("python") or shutil.which(
        "python3") or shutil.which("py"))


def main():
    app = QtWidgets.QApplication(sys.argv)

    is_frozen = getattr(sys, 'frozen', False)

    if is_frozen and not _check_python():
        msg = (
            "<b>Python</b> was not found on this system."
            "<br><br>"
            "This application requires Python to run <b>auto-editor</b>.<br>"
            "Please install Python from <a href='https://www.python.org/downloads/'>python.org</a> "
            "and ensure it is added to your system PATH."
            "<br><br>"
            "The application will now exit.")
        QtWidgets.QMessageBox.critical(
            None,
            "Missing dependency — Python",
            msg,
        )
        sys.exit(1)

    while not _check_auto_editor():
        msg = (
            "<b>auto-editor</b> was not found on this system.<br><br>"
            "Please install auto-editor from <a href='https://github.com/WyattBlue/auto-editor/releases/'>github.com</a> and add it to your system PATH.<br><br>"
            "or manually locate the executable."
        )

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Missing dependency — auto-editor")
        msg_box.setText(msg)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)

        locate_btn = msg_box.addButton(
            "Locate Executable",
            QtWidgets.QMessageBox.ButtonRole.ActionRole)
        exit_btn = msg_box.addButton(
            "Exit", QtWidgets.QMessageBox.ButtonRole.RejectRole)

        msg_box.exec()

        if msg_box.clickedButton() == locate_btn:
            exe_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                None, "Locate auto-editor Executable", "", "Executables (*.exe);;All Files (*)"
            )
            if exe_path:
                if _is_valid_auto_editor(exe_path):
                    settings = QtCore.QSettings("fdllrs", "BatchEditor")
                    settings.setValue("auto_editor_path", exe_path)
                else:
                    QtWidgets.QMessageBox.warning(
                        None,
                        "Invalid Executable",
                        f"The file you selected does not appear to be a valid auto-editor executable.<br><br>"
                        f"Please ensure it is the correct file and try again."
                    )
            else:
                sys.exit(1)
        else:
            sys.exit(1)

    controller = BatchEditorController()
    controller.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
