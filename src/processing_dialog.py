import time
from pathlib import Path
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt


class ProcessingDialog(QtWidgets.QDialog):
    """Modal dialog showing real-time per-file progress during batch editing.

    While running, displays a table with the status and progress of each file
    and a Cancel button. On completion, this button becomes Close and a stats
    summary is shown.
    """

    _COL_FILE = 0
    _COL_STATUS = 1
    _COL_PROGRESS = 2

    _STATUS_QUEUED = "Queued"
    _STATUS_PROCESSING = "⏳ Processing"
    _STATUS_DONE = "✓ Done"
    _STATUS_FAILED = "✗ Failed"
    _STATUS_SKIPPED = "⚠ Skipped"
    _STATUS_CANCELLED = "⊘ Cancelled"

    def __init__(self, files: dict, cancel_callback, parent=None):
        super().__init__(parent)
        self._cancel_callback = cancel_callback
        self._row_map: dict[str, int] = {}  # str(path) -> table row
        self._start_time = time.monotonic()
        self._is_running = True
        self._success_count = 0
        self._fail_count = 0
        self._skip_count = 0

        self._setup_ui()
        self._populate(files)

        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._update_elapsed)
        self._timer.start(1000)

    # ------------------------------------------------------------------
    # UI Setup
    # ------------------------------------------------------------------

    def _setup_ui(self):
        self.setWindowTitle("Processing Files")
        self.setMinimumSize(600, 400)
        self.resize(680, 460)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        # Table -------------------------------------------------------
        self._table = QtWidgets.QTableWidget(0, 3)
        self._table.setHorizontalHeaderLabels(["File", "Status", "Progress"])
        self._table.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self._table.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection
        )
        self._table.setAlternatingRowColors(True)
        self._table.verticalHeader().setVisible(False)
        header = self._table.horizontalHeader()
        header.setSectionResizeMode(self._COL_FILE, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(self._COL_STATUS, QtWidgets.QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(self._COL_PROGRESS, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self._table.setColumnWidth(self._COL_STATUS, 140)
        self._table.setColumnWidth(self._COL_PROGRESS, 80)
        layout.addWidget(self._table)

        # Stats row ---------------------------------------------------
        stats_layout = QtWidgets.QHBoxLayout()
        self._elapsed_label = QtWidgets.QLabel("⏱ Elapsed: 0:00")
        self._result_label = QtWidgets.QLabel()
        stats_layout.addWidget(self._elapsed_label)
        stats_layout.addStretch()
        stats_layout.addWidget(self._result_label)
        layout.addLayout(stats_layout)

        # Buttons -----------------------------------------------------
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()

        self._cancel_btn = QtWidgets.QPushButton("Cancel")
        self._cancel_btn.setToolTip("Stop processing after the current file finishes")
        self._cancel_btn.clicked.connect(self._on_cancel_clicked)

        self._close_btn = QtWidgets.QPushButton("Close")
        self._close_btn.setVisible(False)
        self._close_btn.clicked.connect(self.accept)

        btn_layout.addWidget(self._cancel_btn)
        btn_layout.addWidget(self._close_btn)
        layout.addLayout(btn_layout)

    def _populate(self, files: dict):
        for path in files:
            path_key = str(path)
            row = self._table.rowCount()
            self._table.insertRow(row)
            self._row_map[path_key] = row

            name_item = QtWidgets.QTableWidgetItem(Path(path).name)
            status_item = QtWidgets.QTableWidgetItem(self._STATUS_QUEUED)
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            progress_item = QtWidgets.QTableWidgetItem("—")
            progress_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self._table.setItem(row, self._COL_FILE, name_item)
            self._table.setItem(row, self._COL_STATUS, status_item)
            self._table.setItem(row, self._COL_PROGRESS, progress_item)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _elapsed_str(self) -> str:
        total = int(time.monotonic() - self._start_time)
        m, s = divmod(total, 60)
        return f"{m}:{s:02d}"

    def _update_elapsed(self):
        self._elapsed_label.setText(f"⏱ Elapsed: {self._elapsed_str()}")

    def _set_status(self, row: int, text: str, color: str):
        item = self._table.item(row, self._COL_STATUS)
        if item is None:
            item = QtWidgets.QTableWidgetItem()
            self._table.setItem(row, self._COL_STATUS, item)
        item.setText(text)
        item.setForeground(QtGui.QColor(color))

    def _set_progress(self, row: int, text: str):
        item = self._table.item(row, self._COL_PROGRESS)
        if item is None:
            item = QtWidgets.QTableWidgetItem()
            self._table.setItem(row, self._COL_PROGRESS, item)
        item.setText(text)

    def _mark_remaining_queued_as_cancelled(self):
        for row in range(self._table.rowCount()):
            status = self._table.item(row, self._COL_STATUS)
            if status and status.text() in (self._STATUS_QUEUED, self._STATUS_PROCESSING):
                self._set_status(row, self._STATUS_CANCELLED, "#cc7700")

    def _finish(self, cancelled: bool):
        self._is_running = False
        self._timer.stop()
        self._update_elapsed()

        if cancelled:
            self._mark_remaining_queued_as_cancelled()
            self._result_label.setText(
                f"⊘ Cancelled after {self._elapsed_str()}  |  {self._success_count} done"
            )
        else:
            total = self._success_count + self._fail_count + self._skip_count
            parts = [f"✓ {self._success_count}/{total} completed in {self._elapsed_str()}"]
            if self._skip_count:
                parts.append(f"{self._skip_count} skipped (missing track)")
            if self._fail_count:
                parts.append(f"{self._fail_count} failed")
            self._result_label.setText("  |  ".join(parts))

        self._cancel_btn.setVisible(False)
        self._close_btn.setVisible(True)

    def _on_cancel_clicked(self):
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.setText("Cancelling…")
        self._cancel_callback()

    def closeEvent(self, event: QtCore.QEvent):
        if self._is_running:
            # Don't let the user close mid-run; request cancel and wait.
            self._on_cancel_clicked()
            event.ignore()
        else:
            event.accept()

    # ------------------------------------------------------------------
    # Slots connected to VideoProcessor signals
    # ------------------------------------------------------------------

    def on_file_started(self, path_key: str):
        row = self._row_map.get(path_key)
        if row is None:
            return
        self._set_status(row, self._STATUS_PROCESSING, "#0078d7")
        self._set_progress(row, "0%")
        self._table.scrollToItem(self._table.item(row, self._COL_FILE))

    def on_file_progress(self, path_key: str, pct: float):
        row = self._row_map.get(path_key)
        if row is None:
            return
        self._set_progress(row, f"{pct:.0f}%")

    def on_file_finished(self, path_key: str, success: bool, error_hint: str = ""):
        row = self._row_map.get(path_key)
        if row is None:
            return
        if success:
            self._success_count += 1
            self._set_status(row, self._STATUS_DONE, "#2ea043")
            self._set_progress(row, "100%")
        elif error_hint == "missing_track":
            self._skip_count += 1
            self._set_status(row, self._STATUS_SKIPPED, "#cc7700")
            self._set_progress(row, "—")
            item = self._table.item(row, self._COL_STATUS)
            if item:
                item.setToolTip("Audio stream not found — check threshold settings")
        else:
            self._fail_count += 1
            self._set_status(row, self._STATUS_FAILED, "#d9534f")
            self._set_progress(row, "—")

    def on_all_finished(self):
        self._finish(cancelled=False)

    def on_cancelled(self):
        self._finish(cancelled=True)
