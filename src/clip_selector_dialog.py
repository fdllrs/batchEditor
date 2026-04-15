from pathlib import Path

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from utils import format_duration

class ClipSelectorDialog(QtWidgets.QDialog):
    """Modal dialog that lists all clips queued for editing.

    Each row shows the file name, full path (tooltip), and duration.
    Rows can be checked/unchecked to include or exclude a clip.
    Call :meth:`get_selected_files` after ``exec()`` returns ``Accepted``
    to retrieve the surviving selection.
    """

    _COL_NAME = 0
    _COL_PATH = 1
    _COL_DURATION = 2

    def __init__(self, files: dict, root: Path | None = None, min_length: int = 0,
                 parent: QtWidgets.QWidget | None = None):
        """
        Args:
            files: Mapping of ``Path -> duration_seconds`` to display.
            root: Root directory used to compute relative paths for the Path column.
            min_length: Initial minimum length filter in minutes.
            parent: Parent widget for the dialog.
        """
        super().__init__(parent)
        self._files = dict(files)
        self._root = Path(root) if root else None
        self._min_length = min_length
        self._setup_ui()
        self._populate(files)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_selected_files(self) -> dict:
        """Return a ``{Path: float}`` dict containing only the checked clips."""
        selected = {}
        root = self._tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if item.checkState(self._COL_NAME) == Qt.CheckState.Checked:
                path = item.data(self._COL_NAME, Qt.ItemDataRole.UserRole)
                selected[path] = self._files[path]
        return selected

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _setup_ui(self):
        self.setWindowTitle("Edit Selected Files")
        self.setMinimumSize(441, 337)
        self.resize(441, 337)
        
        layout = QtWidgets.QVBoxLayout(self)

        # Tree widget -------------------------------------------------
        self._tree = QtWidgets.QTreeWidget()
        self._tree.setHeaderLabels(["File Name", "Path", "Duration"])
        self._tree.setRootIsDecorated(False)
        self._tree.setAlternatingRowColors(True)
        self._tree.setSortingEnabled(True)
        self._tree.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self._tree.header().setSectionResizeMode(self._COL_NAME, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self._tree.header().setSectionResizeMode(self._COL_PATH, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self._tree.header().setSectionResizeMode(self._COL_DURATION, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        layout.addWidget(self._tree)

        # Min-length filter row --------------------------------------
        filter_layout = QtWidgets.QHBoxLayout()
        filter_layout.addWidget(QtWidgets.QLabel("Select files longer than:"))
        self._min_length_spinbox = QtWidgets.QSpinBox()
        self._min_length_spinbox.setRange(0, 9999)
        self._min_length_spinbox.setSuffix(" min")
        self._min_length_spinbox.setValue(self._min_length)
        self._min_length_spinbox.valueChanged.connect(self._apply_length_filter)
        filter_layout.addWidget(self._min_length_spinbox)
        filter_layout.addStretch()
        layout.addLayout(filter_layout)

        # Bulk-action row ---------------------------------------------
        bulk_layout = QtWidgets.QHBoxLayout()
        select_all_btn = QtWidgets.QPushButton("Select All")
        deselect_all_btn = QtWidgets.QPushButton("Deselect All")
        select_all_btn.clicked.connect(self._select_all)
        deselect_all_btn.clicked.connect(self._deselect_all)
        bulk_layout.addWidget(select_all_btn)
        bulk_layout.addWidget(deselect_all_btn)
        bulk_layout.addStretch()

        self._selection_label = QtWidgets.QLabel()
        bulk_layout.addWidget(self._selection_label)

        layout.addLayout(bulk_layout)

        # Dialog buttons ----------------------------------------------
        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok
            | QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def _populate(self, files: dict):
        self._tree.setUpdatesEnabled(False)
        for path, duration in files.items():
            item = QtWidgets.QTreeWidgetItem()
            item.setData(self._COL_NAME, Qt.ItemDataRole.UserRole, path)
            item.setText(self._COL_NAME, Path(path).name)
            item.setToolTip(self._COL_NAME, str(path))

            try:
                rel = Path(path).relative_to(self._root.parent) if self._root else None
            except ValueError:
                rel = None
            path_text = str(rel.parent) if rel is not None else str(Path(path).parent)

            item.setText(self._COL_PATH, path_text)
            item.setToolTip(self._COL_PATH, str(path))
            item.setText(self._COL_DURATION, format_duration(duration))
            item.setCheckState(self._COL_NAME, Qt.CheckState.Checked)
            # Right-align duration
            item.setTextAlignment(self._COL_DURATION, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self._tree.addTopLevelItem(item)
        self._tree.setUpdatesEnabled(True)
        self._tree.itemChanged.connect(self._on_item_changed)
        self._update_selection_label()

    def _apply_length_filter(self, minutes: int):
        """Auto-check rows longer than *minutes*, uncheck the rest."""
        threshold_seconds = minutes * 60
        self._tree.itemChanged.disconnect(self._on_item_changed)
        root = self._tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            path = item.data(self._COL_NAME, Qt.ItemDataRole.UserRole)
            state = (
                Qt.CheckState.Checked
                if self._files[path] > threshold_seconds
                else Qt.CheckState.Unchecked
            )
            item.setCheckState(self._COL_NAME, state)
        self._tree.itemChanged.connect(self._on_item_changed)
        self._update_selection_label()

    def _set_all_checked(self, state: Qt.CheckState):
        self._tree.itemChanged.disconnect(self._on_item_changed)
        root = self._tree.invisibleRootItem()
        for i in range(root.childCount()):
            root.child(i).setCheckState(self._COL_NAME, state)
        self._tree.itemChanged.connect(self._on_item_changed)
        self._update_selection_label()

    def _select_all(self):
        self._set_all_checked(Qt.CheckState.Checked)

    def _deselect_all(self):
        self._set_all_checked(Qt.CheckState.Unchecked)

    def _on_item_changed(self, item, column):
        if column == self._COL_NAME:
            self._update_selection_label()

    def _update_selection_label(self):
        total = self._tree.topLevelItemCount()
        checked = sum(
            1
            for i in range(total)
            if self._tree.topLevelItem(i).checkState(self._COL_NAME) == Qt.CheckState.Checked
        )
        self._selection_label.setText(f"{checked} / {total} selected")
