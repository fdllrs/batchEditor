import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from pathlib import Path
from utils import total_duration, audio_track_count
from video_finder import VideoFinder
from video_processor import VideoProcessor, build_command
from processing_options import ProcessingOptions
from audio_threshold_tuner import AudioThresholdTuner
from batch_editor_window import BatchEditorWindow, EXPORT_OPTIONS
from clip_selector_dialog import ClipSelectorDialog
import config_manager

class BatchEditorController:

    def __init__(self):
        self.view = BatchEditorWindow(self)

        self._setup_threadpool()
        self._reset_editing_state()

        self._apply_config(config_manager.default_config())

    def _reset_editing_state(self):
        self.max_audio_channels = 1
        self.track_thresholds: list[float] = [0.0]
        self.video_files_found = {}
        self.video_files_to_edit = {}
        self.to_edit_length = 0
        self.view.multitrackTuningButton.setEnabled(False)

    def _setup_threadpool(self):
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(1)

    def startProcessing(self):
        options = ProcessingOptions(
            export_option=EXPORT_OPTIONS[self.view.exportSelector.currentText()],
            directory=self.view.rootDirectoryLabel.text(),
            track_thresholds=self.track_thresholds,
            margin=self.view.marginSpinbox.value(),
            files_into_folders=self.view.organizeIntoFolders.isChecked(),
            split_only=self.view.splitOnly.isChecked(),
            separate_tracks=self.view.separateTracks.isChecked(),
        )

        self._processed_files_count = 0
        self._total_files_to_process = len(self.video_files_to_edit)

        self.view.progressBar.setRange(0, 0)  # indeterminate / endless loop
        self._update_progress_text()
        self.view.startButton.setEnabled(False)
        self._start_video_processor(options)

    def _update_progress_text(self):
        self.view.startButton.setText('{}/{} done'.format(self._processed_files_count, self._total_files_to_process))



    def _start_video_processor(self, options):
        self.processor = VideoProcessor(options=options, to_edit=self.video_files_to_edit)
        self.processor.signals.finished.connect(self.on_processing_finished)
        self.processor.signals.partially_finished.connect(self.on_processing_partially_finished)
        self.threadpool.start(self.processor)

    def on_processing_partially_finished(self):
        self._processed_files_count += 1
        self._update_progress_text()

    def on_processing_finished(self):
        self.view.progressBar.setRange(0, 1)
        self.view.progressBar.setValue(1)
        self.view.startButton.setText('Start')
        self.view.startButton.setEnabled(True)


    def set_root_directory(self):
        self.video_files_found = {}
        self.video_files_to_edit = {}

        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self.view, "Select Root Directory")

        if folder_path:
            self.view.rootDirectoryLabel.setText(folder_path)
            self.view.startButton.setEnabled(True)
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
        self.view.filesFound.setText(str(files_count))
        self.view.totalLength.setText(current_len_str + ' min')
        self.view.totalLengthToEdit.setText(current_len_str + ' min')

        
    def on_search_finished(self, files_found):
        self.video_files_found = files_found
        self.update_to_edit_files()
        self.view.totalLength.setText(total_duration(self.video_files_found) + ' min')
        self._probe_max_audio_tracks()


    def _probe_max_audio_tracks(self):
        """Probe all found files, store the highest audio stream count,
        and resize track_thresholds to match (padding with 0.0)."""
        max_tracks = max(
            (audio_track_count(path) for path in self.video_files_found),
            default=1,
        )
        self.max_audio_channels = max_tracks
        current = self.track_thresholds
        self.track_thresholds = [
            current[i] if i < len(current) else 0.0
            for i in range(max_tracks)
        ]




    def update_to_edit_files(self):
        self.video_files_to_edit = dict(self.video_files_found)
        self._refresh_to_edit_stats()


    def _refresh_to_edit_stats(self):
        """Recompute to_edit_length and push updated counts to the UI."""
        self.to_edit_length = sum(self.video_files_to_edit.values())
        has_files = len(self.video_files_to_edit) > 0
        self.view.totalLengthToEdit.setText(total_duration(self.video_files_to_edit) + " min")
        self.view.editSelectedFilesButton.setEnabled(has_files)
        self.view.multitrackTuningButton.setEnabled(has_files)


    def open_clip_selector_dialog(self):
        root = Path(self.view.rootDirectoryLabel.text())
        dialog = ClipSelectorDialog(self.video_files_to_edit, root=root, parent=self.view)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.video_files_to_edit = dialog.get_selected_files()
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
            files_into_folders=self.view.organizeIntoFolders.isChecked(),
            split_only=self.view.splitOnly.isChecked(),
            separate_tracks=self.view.separateTracks.isChecked(),
        )
        placeholder = Path("<file>")
        command_str = " ".join(build_command(options, placeholder))

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
            "files_into_folders": self.view.organizeIntoFolders.isChecked(),
            "split_only": self.view.splitOnly.isChecked(),
            "separate_tracks": self.view.separateTracks.isChecked(),
        }
        config_manager.save_config(Path(path), config)


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
                loaded[i] if i < len(loaded) else 0.0
                for i in range(n)
            ]

        if "margin" in config:
            self.view.marginSpinbox.setValue(config["margin"])

        if "files_into_folders" in config:
            self.view.organizeIntoFolders.setChecked(config["files_into_folders"])

        if "split_only" in config:
            self.view.splitOnly.setChecked(config["split_only"])

        if "separate_tracks" in config:
            self.view.separateTracks.setChecked(config["separate_tracks"])
