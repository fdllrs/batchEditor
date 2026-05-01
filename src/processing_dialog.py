import time
from pathlib import Path
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt
from utils import format_duration


class ProcessingDialog(QtWidgets.QDialog):
    """Modal dialog showing per-file status during batch editing.

    While running an indeterminate progress bar pulses at the bottom.
    On completion it stops and a stats summary is shown.
    """

    _COL_FILE = 0
    _COL_STATUS = 1
    _COL_ORIG_LEN = 2
    _COL_EDIT_LEN = 3

    _STATUS_QUEUED = "Queued"
    _STATUS_PROCESSING = "⏳ Processing"
    _STATUS_DONE = "✓ Done"
    _STATUS_FAILED = "✗ Failed"
    _STATUS_SKIPPED = "⚠ Skipped"
    _STATUS_CANCELLED = "⊘ Cancelled"

    def __init__(self, files: dict, cancel_callback, parent=None):
        super().__init__(parent)
        self._cancel_callback = cancel_callback
        self._reset_status()

        self._setup_ui()
        self._populate_table(files)

        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._update_elapsed)
        self._timer.start(1000)

    def _reset_status(self):
        # path_key -> original seconds
        self._orig_secs_map: dict[str, float] = {}
        self._row_map: dict[str, int] = {}          # path_key -> table row
        self._start_time = time.monotonic()
        self._is_running = True
        self._success_count = 0
        self._fail_count = 0
        self._skip_count = 0
        self._total_orig_secs = 0.0
        self._total_edit_secs = 0.0

    def _setup_ui(self):
        self.setWindowTitle("Processing Files")
        self.setMinimumSize(700, 420)
        self.resize(760, 480)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self._setup_table_widget(layout)
        self._setup_progress_bar(layout)
        self._setup_stats_layout(layout)
        self._setup_buttons(layout)

    def _setup_buttons(self, layout):
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()

        self._cancel_btn = QtWidgets.QPushButton("Cancel")
        self._cancel_btn.setToolTip(
            "Stop processing after the current file finishes")
        self._cancel_btn.clicked.connect(self._on_cancel_clicked)

        self._close_btn = QtWidgets.QPushButton("Close")
        self._close_btn.setVisible(False)
        self._close_btn.clicked.connect(self.accept)

        btn_layout.addWidget(self._cancel_btn)
        btn_layout.addWidget(self._close_btn)
        layout.addLayout(btn_layout)

    def _setup_stats_layout(self, layout):
        stats_layout = QtWidgets.QHBoxLayout()
        self._elapsed_label = QtWidgets.QLabel("⏱ Elapsed: 0:00")
        self._result_label = QtWidgets.QLabel()
        stats_layout.addWidget(self._elapsed_label)
        stats_layout.addStretch()
        stats_layout.addWidget(self._result_label)
        layout.addLayout(stats_layout)

    def _setup_progress_bar(self, layout):
        self._progress_bar = QtWidgets.QProgressBar()
        self._progress_bar.setRange(0, 0)   # indeterminate / pulse
        self._progress_bar.setTextVisible(False)
        self._progress_bar.setFixedHeight(6)
        layout.addWidget(self._progress_bar)

    def _setup_table_widget(self, layout):
        self._table = QtWidgets.QTableWidget(0, 4)
        self._table.setHorizontalHeaderLabels(
            ["File", "Status", "Length", "Edited"])
        self._table.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self._table.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection
        )
        self._table.setAlternatingRowColors(True)
        self._table.verticalHeader().setVisible(False)
        header = self._table.horizontalHeader()
        header.setSectionResizeMode(
            self._COL_FILE,
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        for col in (self._COL_STATUS, self._COL_ORIG_LEN, self._COL_EDIT_LEN):
            header.setSectionResizeMode(
                col, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self._table.setColumnWidth(self._COL_STATUS, 140)
        self._table.setColumnWidth(self._COL_ORIG_LEN, 80)
        self._table.setColumnWidth(self._COL_EDIT_LEN, 80)
        layout.addWidget(self._table)

    def _populate_table(self, files: dict):
        for path, orig_secs in files.items():
            path_key = str(path)
            row = self._table.rowCount()
            self._table.insertRow(row)
            self._row_map[path_key] = row
            self._orig_secs_map[path_key] = orig_secs

            name_item = QtWidgets.QTableWidgetItem(Path(path).name)

            status_item = QtWidgets.QTableWidgetItem(self._STATUS_QUEUED)
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            orig_item = QtWidgets.QTableWidgetItem(format_duration(orig_secs))
            orig_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            edit_item = QtWidgets.QTableWidgetItem("—")
            edit_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self._table.setItem(row, self._COL_FILE, name_item)
            self._table.setItem(row, self._COL_STATUS, status_item)
            self._table.setItem(row, self._COL_ORIG_LEN, orig_item)
            self._table.setItem(row, self._COL_EDIT_LEN, edit_item)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _elapsed_str(self) -> str:
        total = int(time.monotonic() - self._start_time)
        m, s = divmod(total, 60)
        return f"{m}:{s:02d}"

    def _update_elapsed(self):
        self._elapsed_label.setText(f"⏱ Elapsed: {self._elapsed_str()}")

    def _set_cell(self, row: int, col: int, text: str,
                  color: str | None = None, tooltip: str = ""):
        item = self._table.item(row, col)
        if item is None:
            item = QtWidgets.QTableWidgetItem()
            self._table.setItem(row, col, item)
        item.setText(text)
        if color:
            item.setForeground(QtGui.QColor(color))
        if tooltip:
            item.setToolTip(tooltip)

    def _set_status(self, row: int, text: str, color: str, tooltip: str = ""):
        self._set_cell(row, self._COL_STATUS, text, color, tooltip)

    def _mark_remaining_queued_as_cancelled(self):
        for row in range(self._table.rowCount()):
            status = self._table.item(row, self._COL_STATUS)
            if status and status.text() in (self._STATUS_QUEUED, self._STATUS_PROCESSING):
                self._set_status(row, self._STATUS_CANCELLED, "#cc7700")

    def _finish(self, cancelled: bool):
        self._is_running = False
        self._timer.stop()
        self._update_elapsed()

        # Stop the progress bar pulse.
        self._progress_bar.setRange(0, 1)
        self._progress_bar.setValue(1)

        parts: list[str] = []

        if cancelled:
            self._mark_remaining_queued_as_cancelled()
            parts.append(
                f"⊘ Cancelled after {
                    self._elapsed_str()}  |  {
                    self._success_count} done")
        else:
            total_files = self._success_count + self._fail_count + self._skip_count
            parts.append(
                f"✓ {self._success_count}/{total_files} completed in {self._elapsed_str()}")
            if self._skip_count:
                parts.append(f"{self._skip_count} skipped (missing track)")
            if self._fail_count:
                parts.append(f"{self._fail_count} failed")

        # Length / reduction summary (only if we have completed files with XML
        # data).
        if self._total_edit_secs > 0:
            pct_saved = (1 - self._total_edit_secs /
                         self._total_orig_secs) * 100
            parts.append(
                f"Total: {format_duration(self._total_orig_secs)} → "
                f"{format_duration(self._total_edit_secs)} "
                f"(−{pct_saved:.1f}%)"
            )

        self._result_label.setText("  |  ".join(parts))
        self._cancel_btn.setVisible(False)
        self._close_btn.setVisible(True)

    def _on_cancel_clicked(self):
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.setText("Cancelling…")
        self._cancel_callback()

    def closeEvent(self, event: QtCore.QEvent):
        if self._is_running:
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
        self._table.scrollToItem(self._table.item(row, self._COL_FILE))

    def on_file_finished(self, path_key: str, success: bool,
                         error_hint: str = "", edited_seconds: float = -1.0):
        row = self._row_map.get(path_key)
        if row is None:
            return

        if success:
            self._success_count += 1
            self._set_status(row, self._STATUS_DONE, "#2ea043")
            if edited_seconds >= 0:
                orig = self._orig_secs_map.get(path_key, 0.0)
                self._total_orig_secs += orig
                self._total_edit_secs += edited_seconds
                self._set_cell(
                    row,
                    self._COL_EDIT_LEN,
                    format_duration(edited_seconds))
        elif error_hint == "missing_track":
            self._skip_count += 1
            self._set_status(
                row, self._STATUS_SKIPPED, "#cc7700",
                tooltip="Audio stream not found — check threshold settings",
            )
        elif error_hint == "cancelled":
            self._set_status(row, self._STATUS_CANCELLED, "#cc7700")
        else:
            self._fail_count += 1
            self._set_status(row, self._STATUS_FAILED, "#d9534f")

    def on_all_finished(self):
        self._finish(cancelled=False)

    def on_cancelled(self):
        self._finish(cancelled=True)
