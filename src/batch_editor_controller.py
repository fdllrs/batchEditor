import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from pathlib import Path
from utils import total_duration
from video_finder import VideoFinder
from video_processor import VideoProcessor, build_command
from processing_options import ProcessingOptions
from audio_threshold_tuner import AudioThresholdTuner
from batch_editor_window import BatchEditorWindow, EXPORT_OPTIONS
from clip_selector_dialog import ClipSelectorDialog
from processing_dialog import ProcessingDialog
import config_manager
import update_checker

_DEFAULT_MIN_LENGTH_MINUTES = 1

class BatchEditorController:

    def __init__(self):
        self.view = BatchEditorWindow(self)

        self._setup_threadpool()
        self._reset_editing_state()
        self._reset_labels()

        self._apply_config(config_manager.default_config())
        self._load_last_saved_config_on_startup()
        QtCore.QTimer.singleShot(0, self._check_for_updates)

    def _load_last_saved_config_on_startup(self):
        """Load the last auto-saved config. Show a warning dialog if not found."""
        last_saved = config_manager.last_saved_config()
        if last_saved is not None:
            self._apply_config(last_saved)
        else:
            QtWidgets.QMessageBox.information(
                self.view,
                "No saved configuration found",
                "Couldn't find a saved configuration.\n"
                "Default settings will be used.",
            )

    def _check_for_updates(self):
        """Trigger a non-blocking background update check."""
        update_checker.check_for_updates(self.view)


    def _reset_labels(self):
        self._update_filesFound_text('0')
        self._update_filesToEdit_text('0')
        self._update_totalLength_text('0')
        self._update_toEditLength_text('0')

    def _reset_editing_state(self):
        self.max_audio_channels = 1
        self.track_thresholds: list[float] = [-1.0]
        self.video_files_found = {}
        self.video_files_to_edit = {}
        self.to_edit_length = 0

    def _setup_threadpool(self):
        self.threadpool = QtCore.QThreadPool()

    def startProcessing(self):
        options = ProcessingOptions(
            export_option=EXPORT_OPTIONS[self.view.exportSelector.currentText()],
            directory=self.view.rootDirectoryLabel.text(),
            track_thresholds=self.track_thresholds,
            margin=self.view.marginSpinbox.value(),
            split_only=self.view.splitOnly.isChecked(),
        )

        self.processor = VideoProcessor(
            options=options,
            video_files_to_edit=self.video_files_to_edit,
            max_parallel=options.max_parallel,
        )

        dialog = ProcessingDialog(
            files=self.video_files_to_edit,
            cancel_callback=self.processor.cancel,
            parent=self.view,
        )
        self.processor.signals.file_started.connect(dialog.on_file_started)
        self.processor.signals.file_finished.connect(dialog.on_file_finished)
        self.processor.signals.finished.connect(dialog.on_all_finished)
        self.processor.signals.cancelled.connect(dialog.on_cancelled)

        self.threadpool.start(self.processor)
        dialog.exec()


    def set_root_directory(self):
        self.video_files_found = {}
        self.video_files_to_edit = {}

        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self.view, "Select Root Directory")

        if folder_path:
            self.view.rootDirectoryLabel.setText(folder_path)
            self._reset_labels()
            self.view.startButton.setEnabled(False)
            self.search_video_files_in_folder(folder_path)
        else:
            self.view.rootDirectoryLabel.setText(self.view.rootDirectoryLabel.placeholderText())
            self.view.startButton.setEnabled(False)


    def search_video_files_in_folder(self, folder_path):

        self.video_finder = VideoFinder(path=Path(folder_path))
        self.video_finder.signals.partially_finished.connect(self.on_partially_finished)
        self.video_finder.signals.finished.connect(self.on_search_finished)
        self.threadpool.start(self.video_finder)


    def on_partially_finished(self, files_count, current_len_str):
        self._update_filesFound_text(files_count)
        self._update_totalLength_text(current_len_str)

    def _update_toEditLength_text(self, current_len_str):
        self.view.totalLengthToEdit.setText(current_len_str + ' min to edit')

    def _update_totalLength_text(self, current_len_str):
        self.view.totalLength.setText(current_len_str + ' min total')
        
    def _update_filesFound_text(self, files_count):
        self.view.filesFound.setText(str(files_count) + ' files found')

    def _update_filesToEdit_text(self, files_to_edit):
        self.view.filesToEdit.setText(str(files_to_edit) + ' files to edit')

        
    def on_search_finished(self, files_found, max_audio_tracks):
        self.video_files_found = files_found
        self._apply_max_audio_tracks(max_audio_tracks)
        self.update_to_edit_files()
        self._update_totalLength_text(total_duration(self.video_files_found))

        self.view.editSelectedFilesButton.setEnabled(bool(self.video_files_found))


    def _apply_max_audio_tracks(self, max_tracks: int):
        """Resize track_thresholds to match the highest audio stream count found,
        padding with -1.0 for any newly discovered tracks."""
        self.max_audio_channels = max_tracks
        current = self.track_thresholds
        self.track_thresholds = [
            current[i] if i < len(current) else -1.0
            for i in range(max_tracks)
        ]


    def update_to_edit_files(self):
        threshold_secs = _DEFAULT_MIN_LENGTH_MINUTES * 60
        self.video_files_to_edit = {
            path: dur
            for path, dur in self.video_files_found.items()
            if dur > threshold_secs
        }
        self._refresh_to_edit_stats()


    def _refresh_to_edit_stats(self):
        """Recompute to_edit_length and push updated counts to the UI."""

        self.to_edit_length = sum(self.video_files_to_edit.values())
        self._update_filesFound_text(str(len(self.video_files_found)))
        self._update_filesToEdit_text(str(len(self.video_files_to_edit)))

        self._update_toEditLength_text(total_duration(self.video_files_to_edit))
        self.view.startButton.setEnabled(bool(self.video_files_to_edit))


    def open_clip_selector_dialog(self):
        root = Path(self.view.rootDirectoryLabel.text())
        previous_selection = dict(self.video_files_to_edit)
        dialog = ClipSelectorDialog(
            self.video_files_found,
            root=root,
            selected=self.video_files_to_edit,
            min_length=_DEFAULT_MIN_LENGTH_MINUTES,
            on_selection_changed=self._on_clip_selection_changed,
            parent=self.view,
        )
        if dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            # User cancelled — restore the selection as it was before the dialog opened.
            self.video_files_to_edit = previous_selection
        self._refresh_to_edit_stats()

    def _on_clip_selection_changed(self, selected_files: dict):
        """Live callback from ClipSelectorDialog — updates filesFound instantly."""
        self.video_files_to_edit = selected_files
        self._refresh_to_edit_stats()


    def open_audio_threshold_tuner_dialog(self):
        dialog = AudioThresholdTuner(
            num_tracks=self.max_audio_channels,
            thresholds=self.track_thresholds,
            parent=self.view,
        )
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.track_thresholds = dialog.get_thresholds()


    def show_command(self):
        options = ProcessingOptions(
            export_option=EXPORT_OPTIONS[self.view.exportSelector.currentText()],
            directory=self.view.rootDirectoryLabel.text(),
            track_thresholds=self.track_thresholds,
            margin=self.view.marginSpinbox.value(),
            split_only=self.view.splitOnly.isChecked(),
        )
        placeholder = Path("<file>")
        cmd_list = build_command(options, placeholder)

        import os
        if os.name == 'nt':
            # Format specifically for PowerShell: native EXEs require "" for literal quotes.
            formatted_cmd = []
            for arg in cmd_list:
                if 'name="' in arg:
                    # Convert premiere:name="file" to 'premiere:name=""file""'
                    arg = f"'{arg.replace('\"', '\"\"')}'"
                elif " " in arg:
                    arg = f'"{arg}"'
                formatted_cmd.append(arg)
            command_str = " ".join(formatted_cmd)
        else:
            import shlex
            command_str = shlex.join(cmd_list)

        dialog = QtWidgets.QDialog(self.view)
        dialog.setWindowTitle("Command Preview")
        dialog.setMinimumWidth(600)

        layout = QtWidgets.QVBoxLayout(dialog)

        text_edit = QtWidgets.QPlainTextEdit(command_str)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        copy_button = QtWidgets.QPushButton("Copy to Clipboard")
        copy_button.clicked.connect(
            lambda: QtWidgets.QApplication.clipboard().setText(command_str)
        )
        layout.addWidget(copy_button)

        dialog.exec()


    def save_config(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.view, "Save Config", "config.txt", "Text files (*.txt)"
        )
        if not path:
            return

        export_value = EXPORT_OPTIONS[self.view.exportSelector.currentText()]
        config = {
            "export_option": export_value,
            "track_thresholds": self.track_thresholds,
            "margin": self.view.marginSpinbox.value(),
            "split_only": self.view.splitOnly.isChecked(),
        }
        config_manager.save_config(Path(path), config)

        # Mirror to the auto-save location so next startup picks it up.
        auto_save_path = config_manager.last_saved_config_path()
        auto_save_path.parent.mkdir(parents=True, exist_ok=True)
        config_manager.save_config(auto_save_path, config)


    def load_config(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.view, "Load Config", "", "Text files (*.txt)"
        )
        if not path:
            return

        config = config_manager.load_config(Path(path))
        self._apply_config(config)


    def _apply_config(self, config: dict):
        """Push a loaded config dict into the UI widgets and controller state."""
        _export_reverse = {v: k for k, v in EXPORT_OPTIONS.items()}

        if "export_option" in config:
            label = _export_reverse.get(config["export_option"])
            if label:
                self.view.exportSelector.setCurrentText(label)

        if "track_thresholds" in config:
            loaded = config["track_thresholds"]
            # To ensure we don't truncate loaded settings on startup, we take the 
            # loaded values. We ensure it's at least padded to the current max known tracks.
            n = max(len(loaded), self.max_audio_channels)
            self.track_thresholds = [
                loaded[i] if i < len(loaded) else -1.0
                for i in range(n)
            ]

        if "margin" in config:
            self.view.marginSpinbox.setValue(config["margin"])

        if "split_only" in config:
            self.view.splitOnly.setChecked(config["split_only"])

