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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
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
        self.SelectionGrid = QGridLayout()
        self.SelectionGrid.setSpacing(8)
        self.SelectionGrid.setObjectName(u"SelectionGrid")
        self.progressBarLabel = QLabel(self.centralwidget)
        self.progressBarLabel.setObjectName(u"progressBarLabel")
        self.progressBarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.progressBarLabel, 1, 4, 1, 1)

        self.totalLengthFoundSpinbox = QLineEdit(self.centralwidget)
        self.totalLengthFoundSpinbox.setObjectName(u"totalLengthFoundSpinbox")
        self.totalLengthFoundSpinbox.setMaximumSize(QSize(60, 16777215))
        self.totalLengthFoundSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalLengthFoundSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.totalLengthFoundSpinbox, 5, 1, 1, 1)

        self.filesFoundSpinbox = QLineEdit(self.centralwidget)
        self.filesFoundSpinbox.setObjectName(u"filesFoundSpinbox")
        self.filesFoundSpinbox.setMaximumSize(QSize(60, 16777215))
        self.filesFoundSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filesFoundSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesFoundSpinbox, 3, 1, 1, 1)

        self.videoFilesFoundLabel = QLabel(self.centralwidget)
        self.videoFilesFoundLabel.setObjectName(u"videoFilesFoundLabel")
        self.videoFilesFoundLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.videoFilesFoundLabel, 3, 0, 1, 1)

        self.minLabel_2 = QLabel(self.centralwidget)
        self.minLabel_2.setObjectName(u"minLabel_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minLabel_2.sizePolicy().hasHeightForWidth())
        self.minLabel_2.setSizePolicy(sizePolicy)
        self.minLabel_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel_2, 6, 2, 1, 1)

        self.filesToEditSpinbox = QLineEdit(self.centralwidget)
        self.filesToEditSpinbox.setObjectName(u"filesToEditSpinbox")
        self.filesToEditSpinbox.setMaximumSize(QSize(60, 16777215))
        self.filesToEditSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filesToEditSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesToEditSpinbox, 4, 1, 1, 1)

        self.foundFilesProgressBar = QProgressBar(self.centralwidget)
        self.foundFilesProgressBar.setObjectName(u"foundFilesProgressBar")
        self.foundFilesProgressBar.setAcceptDrops(False)
        self.foundFilesProgressBar.setValue(0)
        self.foundFilesProgressBar.setTextVisible(False)

        self.SelectionGrid.addWidget(self.foundFilesProgressBar, 1, 0, 1, 4)

        self.filesLongerThanLabel = QLabel(self.centralwidget)
        self.filesLongerThanLabel.setObjectName(u"filesLongerThanLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filesLongerThanLabel.sizePolicy().hasHeightForWidth())
        self.filesLongerThanLabel.setSizePolicy(sizePolicy1)
        self.filesLongerThanLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.filesLongerThanLabel, 2, 0, 1, 1)

        self.editSelectedFilesButton = QPushButton(self.centralwidget)
        self.editSelectedFilesButton.setObjectName(u"editSelectedFilesButton")
        self.editSelectedFilesButton.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editSelectedFilesButton.sizePolicy().hasHeightForWidth())
        self.editSelectedFilesButton.setSizePolicy(sizePolicy2)
        self.editSelectedFilesButton.setCheckable(False)
        self.editSelectedFilesButton.setChecked(False)
        self.editSelectedFilesButton.setFlat(False)

        self.SelectionGrid.addWidget(self.editSelectedFilesButton, 2, 3, 1, 2)

        self.totalLengthToEditLabel = QLabel(self.centralwidget)
        self.totalLengthToEditLabel.setObjectName(u"totalLengthToEditLabel")
        self.totalLengthToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthToEditLabel, 6, 0, 1, 1)

        self.totalLengthFoundLabel = QLabel(self.centralwidget)
        self.totalLengthFoundLabel.setObjectName(u"totalLengthFoundLabel")
        self.totalLengthFoundLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthFoundLabel, 5, 0, 1, 1)

        self.selectRootDirectoryButton = QPushButton(self.centralwidget)
        self.selectRootDirectoryButton.setObjectName(u"selectRootDirectoryButton")

        self.SelectionGrid.addWidget(self.selectRootDirectoryButton, 0, 0, 1, 1)

        self.minLabel_3 = QLabel(self.centralwidget)
        self.minLabel_3.setObjectName(u"minLabel_3")
        sizePolicy.setHeightForWidth(self.minLabel_3.sizePolicy().hasHeightForWidth())
        self.minLabel_3.setSizePolicy(sizePolicy)
        self.minLabel_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel_3, 2, 2, 1, 1)

        self.videoFilesToEditLabel = QLabel(self.centralwidget)
        self.videoFilesToEditLabel.setObjectName(u"videoFilesToEditLabel")
        self.videoFilesToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.videoFilesToEditLabel, 4, 0, 1, 1)

        self.minLengthSpinbox = QSpinBox(self.centralwidget)
        self.minLengthSpinbox.setObjectName(u"minLengthSpinbox")
        sizePolicy2.setHeightForWidth(self.minLengthSpinbox.sizePolicy().hasHeightForWidth())
        self.minLengthSpinbox.setSizePolicy(sizePolicy2)
        self.minLengthSpinbox.setMaximumSize(QSize(60, 16777215))
        self.minLengthSpinbox.setMinimum(0)
        self.minLengthSpinbox.setMaximum(9999)

        self.SelectionGrid.addWidget(self.minLengthSpinbox, 2, 1, 1, 1)

        self.rootDirectoryLabel = QLineEdit(self.centralwidget)
        self.rootDirectoryLabel.setObjectName(u"rootDirectoryLabel")
        self.rootDirectoryLabel.setReadOnly(True)
        self.rootDirectoryLabel.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.SelectionGrid.addWidget(self.rootDirectoryLabel, 0, 1, 1, 4)

        self.minLabel = QLabel(self.centralwidget)
        self.minLabel.setObjectName(u"minLabel")
        sizePolicy.setHeightForWidth(self.minLabel.sizePolicy().hasHeightForWidth())
        self.minLabel.setSizePolicy(sizePolicy)
        self.minLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel, 5, 2, 1, 1)

        self.totalLengthToEditSpinbox = QLineEdit(self.centralwidget)
        self.totalLengthToEditSpinbox.setObjectName(u"totalLengthToEditSpinbox")
        self.totalLengthToEditSpinbox.setEnabled(True)
        self.totalLengthToEditSpinbox.setMaximumSize(QSize(60, 16777215))
        self.totalLengthToEditSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalLengthToEditSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.totalLengthToEditSpinbox, 6, 1, 1, 1)


        self.gridLayout.addLayout(self.SelectionGrid, 0, 0, 1, 1)

        self.optionsLabel = QLabel(self.centralwidget)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.optionsLabel.sizePolicy().hasHeightForWidth())
        self.optionsLabel.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.optionsLabel.setFont(font)
        self.optionsLabel.setAutoFillBackground(False)
        self.optionsLabel.setFrameShape(QFrame.Shape.Panel)
        self.optionsLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.optionsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.optionsLabel, 2, 0, 1, 1)

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


        self.gridLayout.addLayout(self.StartGrid, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.optionsGrid = QGridLayout()
        self.optionsGrid.setObjectName(u"optionsGrid")
        self.optionsGrid.setHorizontalSpacing(8)
        self.optionsGrid.setVerticalSpacing(10)
        self.exportSelector = QComboBox(self.centralwidget)
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.setObjectName(u"exportSelector")

        self.optionsGrid.addWidget(self.exportSelector, 0, 1, 1, 4)

        self.audioThresholdSpinbox = QDoubleSpinBox(self.centralwidget)
        self.audioThresholdSpinbox.setObjectName(u"audioThresholdSpinbox")
        self.audioThresholdSpinbox.setSingleStep(0.500000000000000)

        self.optionsGrid.addWidget(self.audioThresholdSpinbox, 1, 3, 1, 1)

        self.separateTracks = QCheckBox(self.centralwidget)
        self.separateTracks.setObjectName(u"separateTracks")
        self.separateTracks.setChecked(True)

        self.optionsGrid.addWidget(self.separateTracks, 3, 0, 1, 5)

        self.multitrackTuningButton = QPushButton(self.centralwidget)
        self.multitrackTuningButton.setObjectName(u"multitrackTuningButton")
        self.multitrackTuningButton.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.multitrackTuningButton.sizePolicy().hasHeightForWidth())
        self.multitrackTuningButton.setSizePolicy(sizePolicy4)

        self.optionsGrid.addWidget(self.multitrackTuningButton, 1, 4, 1, 1)

        self.exportOptionLabel = QLabel(self.centralwidget)
        self.exportOptionLabel.setObjectName(u"exportOptionLabel")
        self.exportOptionLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.optionsGrid.addWidget(self.exportOptionLabel, 0, 0, 1, 1)

        self.audioThresholdLabel = QLabel(self.centralwidget)
        self.audioThresholdLabel.setObjectName(u"audioThresholdLabel")
        self.audioThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.optionsGrid.addWidget(self.audioThresholdLabel, 1, 0, 1, 1)

        self.audiothresholdSlider = QSlider(self.centralwidget)
        self.audiothresholdSlider.setObjectName(u"audiothresholdSlider")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(9)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.audiothresholdSlider.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider.setSizePolicy(sizePolicy5)
        self.audiothresholdSlider.setMouseTracking(False)
        self.audiothresholdSlider.setTabletTracking(False)
        self.audiothresholdSlider.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider.setAcceptDrops(False)
        self.audiothresholdSlider.setAutoFillBackground(True)
        self.audiothresholdSlider.setMinimum(1)
        self.audiothresholdSlider.setMaximum(10000)
        self.audiothresholdSlider.setValue(1)
        self.audiothresholdSlider.setSliderPosition(1)
        self.audiothresholdSlider.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider.setInvertedAppearance(False)
        self.audiothresholdSlider.setInvertedControls(False)
        self.audiothresholdSlider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider.setTickInterval(1)

        self.optionsGrid.addWidget(self.audiothresholdSlider, 1, 1, 1, 2)

        self.organizeIntoFolders = QCheckBox(self.centralwidget)
        self.organizeIntoFolders.setObjectName(u"organizeIntoFolders")
        self.organizeIntoFolders.setChecked(True)
        self.organizeIntoFolders.setTristate(False)

        self.optionsGrid.addWidget(self.organizeIntoFolders, 2, 0, 1, 5)

        self.preview = QCheckBox(self.centralwidget)
        self.preview.setObjectName(u"preview")

        self.optionsGrid.addWidget(self.preview, 4, 0, 1, 5)

        self.splitOnly = QCheckBox(self.centralwidget)
        self.splitOnly.setObjectName(u"splitOnly")

        self.optionsGrid.addWidget(self.splitOnly, 5, 0, 1, 5)


        self.gridLayout.addLayout(self.optionsGrid, 3, 0, 1, 1)

        self.editConfigLayout = QHBoxLayout()
        self.editConfigLayout.setObjectName(u"editConfigLayout")
        self.editConfigLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.saveConfig = QPushButton(self.centralwidget)
        self.saveConfig.setObjectName(u"saveConfig")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.saveConfig.sizePolicy().hasHeightForWidth())
        self.saveConfig.setSizePolicy(sizePolicy6)

        self.editConfigLayout.addWidget(self.saveConfig)

        self.resetConfig = QPushButton(self.centralwidget)
        self.resetConfig.setObjectName(u"resetConfig")
        sizePolicy6.setHeightForWidth(self.resetConfig.sizePolicy().hasHeightForWidth())
        self.resetConfig.setSizePolicy(sizePolicy6)

        self.editConfigLayout.addWidget(self.resetConfig)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editConfigLayout.addItem(self.horizontalSpacer)

        self.resetConfig_2 = QPushButton(self.centralwidget)
        self.resetConfig_2.setObjectName(u"resetConfig_2")
        self.resetConfig_2.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.resetConfig_2.sizePolicy().hasHeightForWidth())
        self.resetConfig_2.setSizePolicy(sizePolicy6)

        self.editConfigLayout.addWidget(self.resetConfig_2)


        self.gridLayout.addLayout(self.editConfigLayout, 6, 0, 1, 1)

        BatchEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(BatchEditor)
        self.statusbar.setObjectName(u"statusbar")
        BatchEditor.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.selectRootDirectoryButton, self.rootDirectoryLabel)
        QWidget.setTabOrder(self.rootDirectoryLabel, self.editSelectedFilesButton)
        QWidget.setTabOrder(self.editSelectedFilesButton, self.minLengthSpinbox)
        QWidget.setTabOrder(self.minLengthSpinbox, self.filesFoundSpinbox)
        QWidget.setTabOrder(self.filesFoundSpinbox, self.filesToEditSpinbox)
        QWidget.setTabOrder(self.filesToEditSpinbox, self.totalLengthFoundSpinbox)
        QWidget.setTabOrder(self.totalLengthFoundSpinbox, self.totalLengthToEditSpinbox)
        QWidget.setTabOrder(self.totalLengthToEditSpinbox, self.exportSelector)
        QWidget.setTabOrder(self.exportSelector, self.audiothresholdSlider)
        QWidget.setTabOrder(self.audiothresholdSlider, self.audioThresholdSpinbox)
        QWidget.setTabOrder(self.audioThresholdSpinbox, self.multitrackTuningButton)
        QWidget.setTabOrder(self.multitrackTuningButton, self.organizeIntoFolders)
        QWidget.setTabOrder(self.organizeIntoFolders, self.separateTracks)
        QWidget.setTabOrder(self.separateTracks, self.saveConfig)
        QWidget.setTabOrder(self.saveConfig, self.resetConfig)
        QWidget.setTabOrder(self.resetConfig, self.startButton)

        self.retranslateUi(BatchEditor)

        QMetaObject.connectSlotsByName(BatchEditor)
    # setupUi

    def retranslateUi(self, BatchEditor):
        BatchEditor.setWindowTitle(QCoreApplication.translate("BatchEditor", u"Batch Editor", None))
        self.actionasdasddas.setText(QCoreApplication.translate("BatchEditor", u"asdasddas", None))
        self.progressBarLabel.setText(QCoreApplication.translate("BatchEditor", u"working...", None))
        self.totalLengthFoundSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.filesFoundSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.videoFilesFoundLabel.setText(QCoreApplication.translate("BatchEditor", u"video files found:", None))
        self.minLabel_2.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.filesToEditSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.foundFilesProgressBar.setFormat("")
        self.filesLongerThanLabel.setText(QCoreApplication.translate("BatchEditor", u"Select files longer than: ", None))
        self.editSelectedFilesButton.setText(QCoreApplication.translate("BatchEditor", u"edit selected files", None))
        self.totalLengthToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"total length to edit: ", None))
        self.totalLengthFoundLabel.setText(QCoreApplication.translate("BatchEditor", u"total length found: ", None))
        self.selectRootDirectoryButton.setText(QCoreApplication.translate("BatchEditor", u"select root directory", None))
        self.minLabel_3.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.videoFilesToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"video files to edit: ", None))
        self.rootDirectoryLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"no directory selected", None))
        self.minLabel.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.totalLengthToEditSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.optionsLabel.setText(QCoreApplication.translate("BatchEditor", u"OPTIONS", None))
        self.startButton.setText(QCoreApplication.translate("BatchEditor", u"Start", None))
        self.exportSelector.setItemText(0, QCoreApplication.translate("BatchEditor", u"Premiere Pro", None))
        self.exportSelector.setItemText(1, QCoreApplication.translate("BatchEditor", u"Da Vinci Resolve", None))
        self.exportSelector.setItemText(2, QCoreApplication.translate("BatchEditor", u"Final Cut Pro", None))
        self.exportSelector.setItemText(3, QCoreApplication.translate("BatchEditor", u"ShotCut", None))
        self.exportSelector.setItemText(4, QCoreApplication.translate("BatchEditor", u"Kdenlive", None))
        self.exportSelector.setItemText(5, QCoreApplication.translate("BatchEditor", u"clip seuqence", None))

        self.separateTracks.setText(QCoreApplication.translate("BatchEditor", u"keep audio tracks separate", None))
        self.multitrackTuningButton.setText(QCoreApplication.translate("BatchEditor", u"multitrack tuning", None))
        self.exportOptionLabel.setText(QCoreApplication.translate("BatchEditor", u"Export option:", None))
        self.audioThresholdLabel.setText(QCoreApplication.translate("BatchEditor", u"Audio threshold (%):", None))
        self.organizeIntoFolders.setText(QCoreApplication.translate("BatchEditor", u"Organize files into folders", None))
        self.preview.setText(QCoreApplication.translate("BatchEditor", u"preview before starting", None))
        self.splitOnly.setText(QCoreApplication.translate("BatchEditor", u"split clips only", None))
        self.saveConfig.setText(QCoreApplication.translate("BatchEditor", u"Save config", None))
        self.resetConfig.setText(QCoreApplication.translate("BatchEditor", u"reset config", None))
        self.resetConfig_2.setText(QCoreApplication.translate("BatchEditor", u"show command", None))
    # retranslateUi

