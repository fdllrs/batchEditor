"""Background update checker that queries the GitHub Releases API.

Usage
-----
Call ``check_for_updates(parent_widget)`` once after the main window is shown.
If a newer release is found the user is shown a dialog; network errors are
silently ignored so a missing connection never blocks the app.
"""

import urllib.request
import urllib.error
import json
from packaging.version import Version

from PySide6 import QtCore, QtWidgets

from version import __version__

_RELEASES_API_URL = (
    "https://api.github.com/repos/fdllrs/batchEditor/releases/latest"
)
_RELEASES_PAGE_URL = "https://github.com/fdllrs/batchEditor/releases/latest"
_REQUEST_TIMEOUT_SECS = 10


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

class _UpdateWorker(QtCore.QRunnable):
    """Fetches the latest release tag in a thread-pool thread."""

    class Signals(QtCore.QObject):
        update_available = QtCore.Signal(str)   # latest version string
        up_to_date = QtCore.Signal()
        error = QtCore.Signal(str)              # error message (ignored by UI)

    def __init__(self):
        super().__init__()
        self.signals = _UpdateWorker.Signals()

    @QtCore.Slot()
    def run(self):
        try:
            req = urllib.request.Request(
                _RELEASES_API_URL,
                headers={"Accept": "application/vnd.github+json"},
            )
            with urllib.request.urlopen(req, timeout=_REQUEST_TIMEOUT_SECS) as resp:
                data = json.loads(resp.read().decode())

            latest_tag = data.get("tag_name", "").lstrip("v")
            if not latest_tag:
                self.signals.error.emit("Empty tag_name in API response.")
                return

            if Version(latest_tag) > Version(__version__):
                self.signals.update_available.emit(latest_tag)
            else:
                self.signals.up_to_date.emit()

        except Exception as exc:  # network errors, JSON errors, etc.
            self.signals.error.emit(str(exc))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def check_for_updates(parent: QtWidgets.QWidget) -> None:
    """Launch a background update check. Shows a dialog only when an update
    is found; all errors are silently swallowed.

    Parameters
    ----------
    parent:
        The widget that will own any dialog that appears.
    """
    pool = QtCore.QThreadPool.globalInstance()
    worker = _UpdateWorker()
    worker.signals.update_available.connect(
        lambda latest: _show_update_dialog(parent, latest)
    )
    pool.start(worker)


def _show_update_dialog(parent: QtWidgets.QWidget, latest_version: str) -> None:
    msg_box = QtWidgets.QMessageBox(parent)
    msg_box.setWindowTitle("Update available")
    msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg_box.setText(
        f"A new version of <b>Batch Editor</b> is available: <b>v{latest_version}</b><br>"
        f"(current: v{__version__})"
    )
    msg_box.setInformativeText(
        f'<a href="{_RELEASES_PAGE_URL}">Open releases page</a>'
    )
    msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ignore)
    msg_box.button(QtWidgets.QMessageBox.StandardButton.Ignore).setText("Dismiss")
    msg_box.exec()
