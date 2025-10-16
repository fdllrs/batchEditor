# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batchEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_BatchEditor(object):
    def setupUi(self, BatchEditor):
        if not BatchEditor.objectName():
            BatchEditor.setObjectName(u"BatchEditor")
        BatchEditor.resize(438, 583)
        BatchEditor.setDocumentMode(False)
        self.actionasdasddas = QAction(BatchEditor)
        self.actionasdasddas.setObjectName(u"actionasdasddas")
        self.centralwidget = QWidget(BatchEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.optionsLabel = QLabel(self.centralwidget)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionsLabel.sizePolicy().hasHeightForWidth())
        self.optionsLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.optionsLabel.setFont(font)
        self.optionsLabel.setAutoFillBackground(False)
        self.optionsLabel.setFrameShape(QFrame.Shape.Panel)
        self.optionsLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.optionsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.optionsLabel, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.optionsGrid = QGridLayout()
        self.optionsGrid.setObjectName(u"optionsGrid")
        self.optionsGrid.setHorizontalSpacing(8)
        self.optionsGrid.setVerticalSpacing(10)
        self.organizeIntoFolders = QCheckBox(self.centralwidget)
        self.organizeIntoFolders.setObjectName(u"organizeIntoFolders")
        self.organizeIntoFolders.setChecked(True)
        self.organizeIntoFolders.setTristate(False)

        self.optionsGrid.addWidget(self.organizeIntoFolders, 3, 0, 1, 5)

        self.audiothresholdSlider = QSlider(self.centralwidget)
        self.audiothresholdSlider.setObjectName(u"audiothresholdSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(9)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.audiothresholdSlider.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider.setSizePolicy(sizePolicy1)
        self.audiothresholdSlider.setMouseTracking(False)
        self.audiothresholdSlider.setTabletTracking(False)
        self.audiothresholdSlider.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider.setAcceptDrops(False)
        self.audiothresholdSlider.setAutoFillBackground(True)
        self.audiothresholdSlider.setMinimum(1)
        self.audiothresholdSlider.setMaximum(100)
        self.audiothresholdSlider.setValue(10)
        self.audiothresholdSlider.setSliderPosition(10)
        self.audiothresholdSlider.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider.setInvertedAppearance(False)
        self.audiothresholdSlider.setInvertedControls(False)
        self.audiothresholdSlider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider.setTickInterval(10)

        self.optionsGrid.addWidget(self.audiothresholdSlider, 2, 1, 1, 2)

        self.exportForLabel = QLabel(self.centralwidget)
        self.exportForLabel.setObjectName(u"exportForLabel")
        self.exportForLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.optionsGrid.addWidget(self.exportForLabel, 1, 0, 1, 1)

        self.separateTracks = QCheckBox(self.centralwidget)
        self.separateTracks.setObjectName(u"separateTracks")
        self.separateTracks.setChecked(True)

        self.optionsGrid.addWidget(self.separateTracks, 6, 0, 1, 5)

        self.splitOnly = QCheckBox(self.centralwidget)
        self.splitOnly.setObjectName(u"splitOnly")

        self.optionsGrid.addWidget(self.splitOnly, 4, 0, 1, 5)

        self.audioThresholdSpinbox = QSpinBox(self.centralwidget)
        self.audioThresholdSpinbox.setObjectName(u"audioThresholdSpinbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.audioThresholdSpinbox.sizePolicy().hasHeightForWidth())
        self.audioThresholdSpinbox.setSizePolicy(sizePolicy2)
        self.audioThresholdSpinbox.setMinimumSize(QSize(7, 24))
        self.audioThresholdSpinbox.setMaximumSize(QSize(30, 16777215))
        self.audioThresholdSpinbox.setSizeIncrement(QSize(0, 0))
        self.audioThresholdSpinbox.setWrapping(False)
        self.audioThresholdSpinbox.setFrame(False)
        self.audioThresholdSpinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.audioThresholdSpinbox.setAccelerated(True)
        self.audioThresholdSpinbox.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.audioThresholdSpinbox.setKeyboardTracking(True)
        self.audioThresholdSpinbox.setProperty(u"showGroupSeparator", False)
        self.audioThresholdSpinbox.setValue(6)

        self.optionsGrid.addWidget(self.audioThresholdSpinbox, 2, 3, 1, 1)

        self.exportSelector = QComboBox(self.centralwidget)
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.setObjectName(u"exportSelector")

        self.optionsGrid.addWidget(self.exportSelector, 1, 1, 1, 4)

        self.preview = QCheckBox(self.centralwidget)
        self.preview.setObjectName(u"preview")

        self.optionsGrid.addWidget(self.preview, 5, 0, 1, 5)

        self.multitrackTuning = QPushButton(self.centralwidget)
        self.multitrackTuning.setObjectName(u"multitrackTuning")
        sizePolicy2.setHeightForWidth(self.multitrackTuning.sizePolicy().hasHeightForWidth())
        self.multitrackTuning.setSizePolicy(sizePolicy2)

        self.optionsGrid.addWidget(self.multitrackTuning, 2, 4, 1, 1)

        self.audioThresholdLabel = QLabel(self.centralwidget)
        self.audioThresholdLabel.setObjectName(u"audioThresholdLabel")
        self.audioThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.optionsGrid.addWidget(self.audioThresholdLabel, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.optionsGrid, 3, 0, 1, 1)

        self.editConfigLayout = QHBoxLayout()
        self.editConfigLayout.setObjectName(u"editConfigLayout")
        self.editConfigLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.saveConfig = QPushButton(self.centralwidget)
        self.saveConfig.setObjectName(u"saveConfig")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.saveConfig.sizePolicy().hasHeightForWidth())
        self.saveConfig.setSizePolicy(sizePolicy3)

        self.editConfigLayout.addWidget(self.saveConfig)

        self.resetConfig = QPushButton(self.centralwidget)
        self.resetConfig.setObjectName(u"resetConfig")
        sizePolicy3.setHeightForWidth(self.resetConfig.sizePolicy().hasHeightForWidth())
        self.resetConfig.setSizePolicy(sizePolicy3)

        self.editConfigLayout.addWidget(self.resetConfig)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editConfigLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.editConfigLayout, 4, 0, 1, 1)

        self.StartGrid = QVBoxLayout()
        self.StartGrid.setSpacing(12)
        self.StartGrid.setObjectName(u"StartGrid")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(False)

        self.StartGrid.addWidget(self.startButton)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.StartGrid.addWidget(self.progressBar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.StartGrid.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.StartGrid, 5, 0, 1, 1)

        self.SelectionGrid = QGridLayout()
        self.SelectionGrid.setSpacing(8)
        self.SelectionGrid.setObjectName(u"SelectionGrid")
        self.minLabel_3 = QLabel(self.centralwidget)
        self.minLabel_3.setObjectName(u"minLabel_3")
        self.minLabel_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel_3, 2, 2, 1, 1)

        self.totalLengthFoundSpinbox = QLineEdit(self.centralwidget)
        self.totalLengthFoundSpinbox.setObjectName(u"totalLengthFoundSpinbox")
        self.totalLengthFoundSpinbox.setMaximumSize(QSize(60, 16777215))
        self.totalLengthFoundSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalLengthFoundSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.totalLengthFoundSpinbox, 5, 1, 1, 1)

        self.totalLengthFoundLabel = QLabel(self.centralwidget)
        self.totalLengthFoundLabel.setObjectName(u"totalLengthFoundLabel")
        self.totalLengthFoundLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthFoundLabel, 5, 0, 1, 1)

        self.videoFilesToEditLabel = QLabel(self.centralwidget)
        self.videoFilesToEditLabel.setObjectName(u"videoFilesToEditLabel")
        self.videoFilesToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.videoFilesToEditLabel, 4, 0, 1, 1)

        self.totalLengthToEditSpinbox = QLineEdit(self.centralwidget)
        self.totalLengthToEditSpinbox.setObjectName(u"totalLengthToEditSpinbox")
        self.totalLengthToEditSpinbox.setEnabled(True)
        self.totalLengthToEditSpinbox.setMaximumSize(QSize(60, 16777215))
        self.totalLengthToEditSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalLengthToEditSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.totalLengthToEditSpinbox, 6, 1, 1, 1)

        self.rootDirectoryLabel = QLineEdit(self.centralwidget)
        self.rootDirectoryLabel.setObjectName(u"rootDirectoryLabel")
        self.rootDirectoryLabel.setReadOnly(True)
        self.rootDirectoryLabel.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.SelectionGrid.addWidget(self.rootDirectoryLabel, 0, 1, 1, 4)

        self.videoFilesFoundLabel = QLabel(self.centralwidget)
        self.videoFilesFoundLabel.setObjectName(u"videoFilesFoundLabel")
        self.videoFilesFoundLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.videoFilesFoundLabel, 3, 0, 1, 1)

        self.filesToEditSpinbox = QLineEdit(self.centralwidget)
        self.filesToEditSpinbox.setObjectName(u"filesToEditSpinbox")
        self.filesToEditSpinbox.setMaximumSize(QSize(60, 16777215))
        self.filesToEditSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filesToEditSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesToEditSpinbox, 4, 1, 1, 1)

        self.minLabel_2 = QLabel(self.centralwidget)
        self.minLabel_2.setObjectName(u"minLabel_2")
        self.minLabel_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel_2, 6, 2, 1, 1)

        self.minLabel = QLabel(self.centralwidget)
        self.minLabel.setObjectName(u"minLabel")
        self.minLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel, 5, 2, 1, 1)

        self.selectRootDirectoryButton = QPushButton(self.centralwidget)
        self.selectRootDirectoryButton.setObjectName(u"selectRootDirectoryButton")

        self.SelectionGrid.addWidget(self.selectRootDirectoryButton, 0, 0, 1, 1)

        self.minLengthSpinbox = QSpinBox(self.centralwidget)
        self.minLengthSpinbox.setObjectName(u"minLengthSpinbox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.minLengthSpinbox.sizePolicy().hasHeightForWidth())
        self.minLengthSpinbox.setSizePolicy(sizePolicy4)
        self.minLengthSpinbox.setMinimumSize(QSize(60, 0))
        self.minLengthSpinbox.setMaximumSize(QSize(60, 16777215))
        self.minLengthSpinbox.setMinimum(0)
        self.minLengthSpinbox.setMaximum(9999)

        self.SelectionGrid.addWidget(self.minLengthSpinbox, 2, 1, 1, 1)

        self.filesLongerThanLabel = QLabel(self.centralwidget)
        self.filesLongerThanLabel.setObjectName(u"filesLongerThanLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.filesLongerThanLabel.sizePolicy().hasHeightForWidth())
        self.filesLongerThanLabel.setSizePolicy(sizePolicy5)
        self.filesLongerThanLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.filesLongerThanLabel, 2, 0, 1, 1)

        self.totalLengthToEditLabel = QLabel(self.centralwidget)
        self.totalLengthToEditLabel.setObjectName(u"totalLengthToEditLabel")
        self.totalLengthToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthToEditLabel, 6, 0, 1, 1)

        self.editSelectedFilesButton = QPushButton(self.centralwidget)
        self.editSelectedFilesButton.setObjectName(u"editSelectedFilesButton")
        self.editSelectedFilesButton.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.editSelectedFilesButton.sizePolicy().hasHeightForWidth())
        self.editSelectedFilesButton.setSizePolicy(sizePolicy6)
        self.editSelectedFilesButton.setCheckable(False)
        self.editSelectedFilesButton.setChecked(False)
        self.editSelectedFilesButton.setFlat(False)

        self.SelectionGrid.addWidget(self.editSelectedFilesButton, 2, 3, 1, 2)

        self.progressBarLabel = QLabel(self.centralwidget)
        self.progressBarLabel.setObjectName(u"progressBarLabel")
        self.progressBarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.progressBarLabel, 1, 4, 1, 1)

        self.foundFilesProgressBar = QProgressBar(self.centralwidget)
        self.foundFilesProgressBar.setObjectName(u"foundFilesProgressBar")
        self.foundFilesProgressBar.setAcceptDrops(False)
        self.foundFilesProgressBar.setValue(0)
        self.foundFilesProgressBar.setTextVisible(False)

        self.SelectionGrid.addWidget(self.foundFilesProgressBar, 1, 0, 1, 4)

        self.filesFoundSpinbox = QLineEdit(self.centralwidget)
        self.filesFoundSpinbox.setObjectName(u"filesFoundSpinbox")
        self.filesFoundSpinbox.setMaximumSize(QSize(60, 16777215))
        self.filesFoundSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filesFoundSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesFoundSpinbox, 3, 1, 1, 1)

        self.SelectionGrid.setColumnStretch(0, 1)
        self.SelectionGrid.setColumnStretch(1, 2)
        self.SelectionGrid.setColumnMinimumWidth(1, 1)

        self.gridLayout.addLayout(self.SelectionGrid, 0, 0, 1, 1)

        BatchEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(BatchEditor)
        self.statusbar.setObjectName(u"statusbar")
        BatchEditor.setStatusBar(self.statusbar)

        self.retranslateUi(BatchEditor)
        self.audiothresholdSlider.valueChanged.connect(self.audioThresholdSpinbox.setValue)
        self.audioThresholdSpinbox.valueChanged.connect(self.audiothresholdSlider.setValue)

        QMetaObject.connectSlotsByName(BatchEditor)
    # setupUi

    def retranslateUi(self, BatchEditor):
        BatchEditor.setWindowTitle(QCoreApplication.translate("BatchEditor", u"Batch Editor", None))
        self.actionasdasddas.setText(QCoreApplication.translate("BatchEditor", u"asdasddas", None))
        self.optionsLabel.setText(QCoreApplication.translate("BatchEditor", u"OPTIONS", None))
        self.organizeIntoFolders.setText(QCoreApplication.translate("BatchEditor", u"Organize files into folders", None))
        self.exportForLabel.setText(QCoreApplication.translate("BatchEditor", u"Export option:", None))
        self.separateTracks.setText(QCoreApplication.translate("BatchEditor", u"keep audio tracks separate", None))
        self.splitOnly.setText(QCoreApplication.translate("BatchEditor", u"split clips only", None))
        self.exportSelector.setItemText(0, QCoreApplication.translate("BatchEditor", u"Premiere Pro", None))
        self.exportSelector.setItemText(1, QCoreApplication.translate("BatchEditor", u"Da Vinci Resolve", None))
        self.exportSelector.setItemText(2, QCoreApplication.translate("BatchEditor", u"Final Cut Pro", None))
        self.exportSelector.setItemText(3, QCoreApplication.translate("BatchEditor", u"ShotCut", None))
        self.exportSelector.setItemText(4, QCoreApplication.translate("BatchEditor", u"Kdenlive", None))
        self.exportSelector.setItemText(5, QCoreApplication.translate("BatchEditor", u"clip seuqence", None))

        self.preview.setText(QCoreApplication.translate("BatchEditor", u"preview before starting", None))
        self.multitrackTuning.setText(QCoreApplication.translate("BatchEditor", u"multitrack tuning", None))
        self.audioThresholdLabel.setText(QCoreApplication.translate("BatchEditor", u"Audio threshold (%):", None))
        self.saveConfig.setText(QCoreApplication.translate("BatchEditor", u"Save config as default", None))
        self.resetConfig.setText(QCoreApplication.translate("BatchEditor", u"reset config", None))
        self.startButton.setText(QCoreApplication.translate("BatchEditor", u"Start", None))
        self.minLabel_3.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.totalLengthFoundSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.totalLengthFoundLabel.setText(QCoreApplication.translate("BatchEditor", u"total length found: ", None))
        self.videoFilesToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"video files to edit: ", None))
        self.totalLengthToEditSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.rootDirectoryLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"no directory selected", None))
        self.videoFilesFoundLabel.setText(QCoreApplication.translate("BatchEditor", u"video files found:", None))
        self.filesToEditSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.minLabel_2.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.minLabel.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.selectRootDirectoryButton.setText(QCoreApplication.translate("BatchEditor", u"select root directory", None))
        self.filesLongerThanLabel.setText(QCoreApplication.translate("BatchEditor", u"Select files longer than: ", None))
        self.totalLengthToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"total length to edit: ", None))
        self.editSelectedFilesButton.setText(QCoreApplication.translate("BatchEditor", u"edit selected files", None))
        self.progressBarLabel.setText(QCoreApplication.translate("BatchEditor", u"working...", None))
        self.foundFilesProgressBar.setFormat("")
        self.filesFoundSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
    # retranslateUi

