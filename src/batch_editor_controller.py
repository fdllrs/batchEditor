import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from UI.mainWindowUI.batchEditor_ui import Ui_BatchEditor
from pathlib import Path
from utils import total_length_minutes
from video_finder import VideoFinder
from video_processor import VideoProcessor, build_command
from processing_options import ProcessingOptions
from audio_threshold_tuner import AudioThresholdTuner
from batch_editor_window import BatchEditorWindow, EXPORT_OPTIONS
import config_manager

class BatchEditorController:

    def __init__(self):
        self.view = BatchEditorWindow(self)

        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(1)
        self.max_audio_channels = 1

        self.video_files_found = {}
        self.video_files_to_edit = {}
        self.to_edit_length = 0

        self._apply_config(config_manager.load_default_config())

    def start(self):
        options = ProcessingOptions(
            export_option=EXPORT_OPTIONS[self.view.exportSelector.currentText()],
            directory=self.view.rootDirectoryLabel.text(),
            threshold=self.view.audioThresholdSpinbox.value(),
            margin=self.view.marginSpinbox.value(),
            files_into_folders=self.view.organizeIntoFolders.isChecked(),
            split_only=self.view.splitOnly.isChecked(),
            separate_tracks=self.view.separateTracks.isChecked(),
        )

        self._processing_done = 0
        self._processing_total = len(self.video_files_to_edit)

        self.view.progressBar.setRange(0, 0)  # indeterminate / endless loop
        self.view.startButton.setText('0/{} done'.format(self._processing_total))
        self.view.startButton.setEnabled(False)
        self._start_video_processor(options)


    def _start_video_processor(self, options):
        self.processor = VideoProcessor(options=options, to_edit=self.video_files_to_edit)
        self.processor.signals.finished.connect(self.on_processing_finished)
        self.processor.signals.partially_finished.connect(self.on_processing_partially_finished)
        self.threadpool.start(self.processor)

    def on_processing_partially_finished(self):
        self._processing_done += 1
        self.view.startButton.setText('{}/{} done'.format(self._processing_done, self._processing_total))


    def on_processing_finished(self):
        self.view.progressBar.setRange(0, 1)
        self.view.progressBar.setValue(1)
        self.view.startButton.setText('Start')
        self.view.startButton.setEnabled(True)
        print('done')


    def set_root_directory(self):
        self.video_files_found = {}
        self.video_files_to_edit = {}

        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self.view, "Select Root Directory")

        if folder_path:
            self.view.rootDirectoryLabel.setText(folder_path)
            self.view.startButton.setEnabled(True)
            self.search_video_files(folder_path)
        else:
            self.view.rootDirectoryLabel.setText(self.view.rootDirectoryLabel.placeholderText())
            self.view.startButton.setEnabled(False)


    def search_video_files(self, folder_path):
        self.view.foundFilesProgressBar.reset()

        self.view.progressBarLabel.setVisible(True)
        self.view.progressBarLabel.setText('Working...')
        self.view.foundFilesProgressBar.setVisible(True)

        self.view.foundFilesProgressBar.setRange(0, 0)

        self.video_finder = VideoFinder(path=Path(folder_path))
        self.video_finder.signals.partially_finished.connect(self.on_partially_finished)
        self.video_finder.signals.finished.connect(self.on_search_finished)
        self.threadpool.start(self.video_finder)


    def on_partially_finished(self, files_found):
        self.video_files_found = files_found
        self.view.filesFound.setText(str(len(self.video_files_found)))

        
    def on_search_finished(self):
        self.view.foundFilesProgressBar.reset()
        self.set_progress_bar_done()

        self.update_to_edit_files(self.view.minLengthSpinbox.value())
        self.view.totalLength.setText(total_length_minutes(self.video_files_found) + ' min')


    def set_progress_bar_done(self):
        self.view.progressBarLabel.setText('Done!')
        self.view.foundFilesProgressBar.setRange(0, 100)
        self.view.foundFilesProgressBar.setValue(100)


    def update_to_edit_files(self, min_length_minutes):
        self.to_edit_length = 0
        self.video_files_to_edit = {}
        min_length_seconds = min_length_minutes * 60

        for file_path, duration in self.video_files_found.items():
            if duration > min_length_seconds:
                self.video_files_to_edit[file_path] = duration
                self.to_edit_length += duration

        self.view.filesToEditSpinbox.setText(str(len(self.video_files_to_edit)))
        self.view.totalLengthToEditSpinbox.setText(total_length_minutes(self.video_files_to_edit))


    def open_audio_threshold_tuner_dialog(self):
        self.threshold_dialog = AudioThresholdTuner(self.view)
        self.threshold_dialog.exec()


    def show_command(self):
        options = ProcessingOptions(
            export_option=EXPORT_OPTIONS[self.view.exportSelector.currentText()],
            directory=self.view.rootDirectoryLabel.text(),
            threshold=self.view.audioThresholdSpinbox.value(),
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
            "threshold": self.view.audioThresholdSpinbox.value(),
            "margin": self.view.marginSpinbox.value(),
            "min_length": self.view.minLengthSpinbox.value(),
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
        """Push a loaded config dict into the UI widgets."""
        _export_reverse = {v: k for k, v in EXPORT_OPTIONS.items()}

        if "export_option" in config:
            label = _export_reverse.get(config["export_option"])
            if label:
                self.view.exportSelector.setCurrentText(label)

        if "threshold" in config:
            self.view.audioThresholdSpinbox.setValue(config["threshold"])

        if "margin" in config:
            self.view.marginSpinbox.setValue(config["margin"])

        if "min_length" in config:
            self.view.minLengthSpinbox.setValue(config["min_length"])

        if "files_into_folders" in config:
            self.view.organizeIntoFolders.setChecked(config["files_into_folders"])

        if "split_only" in config:
            self.view.splitOnly.setChecked(config["split_only"])

        if "separate_tracks" in config:
            self.view.separateTracks.setChecked(config["separate_tracks"])
