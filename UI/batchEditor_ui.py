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
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_BatchEditor(object):
    def setupUi(self, BatchEditor):
        if not BatchEditor.objectName():
            BatchEditor.setObjectName(u"BatchEditor")
        BatchEditor.resize(634, 576)
        BatchEditor.setDocumentMode(False)
        self.actionasdasddas = QAction(BatchEditor)
        self.actionasdasddas.setObjectName(u"actionasdasddas")
        self.centralwidget = QWidget(BatchEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.selectionTab = QWidget()
        self.selectionTab.setObjectName(u"selectionTab")
        self.verticalLayout = QVBoxLayout(self.selectionTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SelectionGrid = QGridLayout()
        self.SelectionGrid.setObjectName(u"SelectionGrid")
        self.SelectionGrid.setHorizontalSpacing(25)
        self.SelectionGrid.setVerticalSpacing(19)
        self.SelectionGrid.setContentsMargins(5, 5, 5, 5)
        self.filesToEditSpinbox = QLineEdit(self.selectionTab)
        self.filesToEditSpinbox.setObjectName(u"filesToEditSpinbox")
        self.filesToEditSpinbox.setMaximumSize(QSize(60, 16777215))
        self.filesToEditSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filesToEditSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesToEditSpinbox, 6, 1, 1, 1)

        self.foundFilesProgressBar = QProgressBar(self.selectionTab)
        self.foundFilesProgressBar.setObjectName(u"foundFilesProgressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.foundFilesProgressBar.sizePolicy().hasHeightForWidth())
        self.foundFilesProgressBar.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        self.foundFilesProgressBar.setPalette(palette)
        self.foundFilesProgressBar.setAcceptDrops(False)
        self.foundFilesProgressBar.setValue(0)
        self.foundFilesProgressBar.setTextVisible(False)

        self.SelectionGrid.addWidget(self.foundFilesProgressBar, 1, 0, 1, 4)

        self.totalLengthToEditSpinbox = QLineEdit(self.selectionTab)
        self.totalLengthToEditSpinbox.setObjectName(u"totalLengthToEditSpinbox")
        self.totalLengthToEditSpinbox.setEnabled(True)
        self.totalLengthToEditSpinbox.setMaximumSize(QSize(60, 16777215))
        self.totalLengthToEditSpinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalLengthToEditSpinbox.setReadOnly(True)

        self.SelectionGrid.addWidget(self.totalLengthToEditSpinbox, 7, 1, 1, 1)

        self.filesFoundLabel = QLabel(self.selectionTab)
        self.filesFoundLabel.setObjectName(u"filesFoundLabel")
        self.filesFoundLabel.setIndent(0)

        self.SelectionGrid.addWidget(self.filesFoundLabel, 3, 0, 1, 1)

        self.editSelectedFilesButton = QPushButton(self.selectionTab)
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

        self.SelectionGrid.addWidget(self.editSelectedFilesButton, 5, 3, 1, 2)

        self.filesLongerThanLabel = QLabel(self.selectionTab)
        self.filesLongerThanLabel.setObjectName(u"filesLongerThanLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.filesLongerThanLabel.sizePolicy().hasHeightForWidth())
        self.filesLongerThanLabel.setSizePolicy(sizePolicy3)
        self.filesLongerThanLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.filesLongerThanLabel, 5, 0, 1, 1)

        self.totalLengthToEditLabel = QLabel(self.selectionTab)
        self.totalLengthToEditLabel.setObjectName(u"totalLengthToEditLabel")
        self.totalLengthToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthToEditLabel, 7, 0, 1, 1)

        self.rootDirectoryLabel = QLineEdit(self.selectionTab)
        self.rootDirectoryLabel.setObjectName(u"rootDirectoryLabel")
        self.rootDirectoryLabel.setReadOnly(True)
        self.rootDirectoryLabel.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.SelectionGrid.addWidget(self.rootDirectoryLabel, 0, 1, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SelectionGrid.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.videoFilesToEditLabel = QLabel(self.selectionTab)
        self.videoFilesToEditLabel.setObjectName(u"videoFilesToEditLabel")
        self.videoFilesToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.videoFilesToEditLabel, 6, 0, 1, 1)

        self.minLengthSpinbox = QSpinBox(self.selectionTab)
        self.minLengthSpinbox.setObjectName(u"minLengthSpinbox")
        sizePolicy2.setHeightForWidth(self.minLengthSpinbox.sizePolicy().hasHeightForWidth())
        self.minLengthSpinbox.setSizePolicy(sizePolicy2)
        self.minLengthSpinbox.setMaximumSize(QSize(60, 16777215))
        self.minLengthSpinbox.setMinimum(0)
        self.minLengthSpinbox.setMaximum(9999)
        self.minLengthSpinbox.setValue(3)

        self.SelectionGrid.addWidget(self.minLengthSpinbox, 5, 1, 1, 1)

        self.filesFound = QLabel(self.selectionTab)
        self.filesFound.setObjectName(u"filesFound")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.filesFound.sizePolicy().hasHeightForWidth())
        self.filesFound.setSizePolicy(sizePolicy4)
        self.filesFound.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.filesFound, 3, 1, 1, 1)

        self.selectRootDirectoryButton = QPushButton(self.selectionTab)
        self.selectRootDirectoryButton.setObjectName(u"selectRootDirectoryButton")

        self.SelectionGrid.addWidget(self.selectRootDirectoryButton, 0, 0, 1, 1)

        self.totalLength = QLabel(self.selectionTab)
        self.totalLength.setObjectName(u"totalLength")
        sizePolicy4.setHeightForWidth(self.totalLength.sizePolicy().hasHeightForWidth())
        self.totalLength.setSizePolicy(sizePolicy4)
        self.totalLength.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.totalLength, 2, 1, 1, 1)

        self.minLabel_3 = QLabel(self.selectionTab)
        self.minLabel_3.setObjectName(u"minLabel_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.minLabel_3.sizePolicy().hasHeightForWidth())
        self.minLabel_3.setSizePolicy(sizePolicy5)
        self.minLabel_3.setLineWidth(0)
        self.minLabel_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel_3, 5, 2, 1, 1)

        self.totalLengthLabel = QLabel(self.selectionTab)
        self.totalLengthLabel.setObjectName(u"totalLengthLabel")
        self.totalLengthLabel.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.totalLengthLabel.sizePolicy().hasHeightForWidth())
        self.totalLengthLabel.setSizePolicy(sizePolicy4)
        self.totalLengthLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthLabel, 2, 0, 1, 1)

        self.progressBarLabel = QLabel(self.selectionTab)
        self.progressBarLabel.setObjectName(u"progressBarLabel")
        self.progressBarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.progressBarLabel, 1, 4, 1, 1)

        self.minLabel_2 = QLabel(self.selectionTab)
        self.minLabel_2.setObjectName(u"minLabel_2")
        sizePolicy5.setHeightForWidth(self.minLabel_2.sizePolicy().hasHeightForWidth())
        self.minLabel_2.setSizePolicy(sizePolicy5)
        self.minLabel_2.setLineWidth(0)
        self.minLabel_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.minLabel_2, 7, 2, 1, 1)


        self.verticalLayout.addLayout(self.SelectionGrid)

        self.tabWidget.addTab(self.selectionTab, "")
        self.optionsTab = QWidget()
        self.optionsTab.setObjectName(u"optionsTab")
        self.horizontalLayout = QHBoxLayout(self.optionsTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.optionsGrid = QGridLayout()
        self.optionsGrid.setObjectName(u"optionsGrid")
        self.optionsGrid.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.optionsGrid.setHorizontalSpacing(6)
        self.optionsGrid.setVerticalSpacing(2)
        self.optionsGrid.setContentsMargins(5, 5, 5, 5)
        self.audiothresholdSlider = QSlider(self.optionsTab)
        self.audiothresholdSlider.setObjectName(u"audiothresholdSlider")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(9)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.audiothresholdSlider.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider.setSizePolicy(sizePolicy6)
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

        self.audioThresholdLabel = QLabel(self.optionsTab)
        self.audioThresholdLabel.setObjectName(u"audioThresholdLabel")
        self.audioThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel.setMargin(3)

        self.optionsGrid.addWidget(self.audioThresholdLabel, 1, 0, 1, 1)

        self.multitrackTuningButton = QPushButton(self.optionsTab)
        self.multitrackTuningButton.setObjectName(u"multitrackTuningButton")
        self.multitrackTuningButton.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.multitrackTuningButton.sizePolicy().hasHeightForWidth())
        self.multitrackTuningButton.setSizePolicy(sizePolicy7)

        self.optionsGrid.addWidget(self.multitrackTuningButton, 1, 4, 1, 1)

        self.exportSelector = QComboBox(self.optionsTab)
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.setObjectName(u"exportSelector")

        self.optionsGrid.addWidget(self.exportSelector, 0, 1, 1, 4)

        self.marginSpinbox = QDoubleSpinBox(self.optionsTab)
        self.marginSpinbox.setObjectName(u"marginSpinbox")
        self.marginSpinbox.setSingleStep(0.500000000000000)

        self.optionsGrid.addWidget(self.marginSpinbox, 2, 1, 1, 1)

        self.audioThresholdSpinbox = QDoubleSpinBox(self.optionsTab)
        self.audioThresholdSpinbox.setObjectName(u"audioThresholdSpinbox")
        self.audioThresholdSpinbox.setSingleStep(0.500000000000000)

        self.optionsGrid.addWidget(self.audioThresholdSpinbox, 1, 3, 1, 1)

        self.marginLabel = QLabel(self.optionsTab)
        self.marginLabel.setObjectName(u"marginLabel")
        self.marginLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.marginLabel.setMargin(3)

        self.optionsGrid.addWidget(self.marginLabel, 2, 0, 1, 1)

        self.exportOptionLabel = QLabel(self.optionsTab)
        self.exportOptionLabel.setObjectName(u"exportOptionLabel")
        self.exportOptionLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.exportOptionLabel.setMargin(3)

        self.optionsGrid.addWidget(self.exportOptionLabel, 0, 0, 1, 1)

        self.organizeIntoFolders = QCheckBox(self.optionsTab)
        self.organizeIntoFolders.setObjectName(u"organizeIntoFolders")
        self.organizeIntoFolders.setChecked(True)
        self.organizeIntoFolders.setTristate(False)

        self.optionsGrid.addWidget(self.organizeIntoFolders, 3, 0, 1, 2)

        self.separateTracks = QCheckBox(self.optionsTab)
        self.separateTracks.setObjectName(u"separateTracks")
        self.separateTracks.setChecked(True)

        self.optionsGrid.addWidget(self.separateTracks, 4, 0, 1, 2)

        self.splitOnly = QCheckBox(self.optionsTab)
        self.splitOnly.setObjectName(u"splitOnly")

        self.optionsGrid.addWidget(self.splitOnly, 5, 0, 1, 2)

        self.optionsGrid.setColumnStretch(0, 1)

        self.horizontalLayout.addLayout(self.optionsGrid)

        self.tabWidget.addTab(self.optionsTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)

        self.resetConfigButton = QPushButton(self.centralwidget)
        self.resetConfigButton.setObjectName(u"resetConfigButton")
        self.resetConfigButton.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.resetConfigButton.sizePolicy().hasHeightForWidth())
        self.resetConfigButton.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.resetConfigButton, 0, 0, 1, 1)

        self.saveConfigButton = QPushButton(self.centralwidget)
        self.saveConfigButton.setObjectName(u"saveConfigButton")
        self.saveConfigButton.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.saveConfigButton.sizePolicy().hasHeightForWidth())
        self.saveConfigButton.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.saveConfigButton, 0, 1, 1, 1)

        self.showCommandButton = QPushButton(self.centralwidget)
        self.showCommandButton.setObjectName(u"showCommandButton")
        self.showCommandButton.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.showCommandButton.sizePolicy().hasHeightForWidth())
        self.showCommandButton.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.showCommandButton, 0, 4, 1, 1)

        self.previewButton = QPushButton(self.centralwidget)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.previewButton.sizePolicy().hasHeightForWidth())
        self.previewButton.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.previewButton, 0, 3, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy9)

        self.gridLayout_2.addWidget(self.startButton, 1, 0, 1, 5)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        BatchEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(BatchEditor)
        self.statusbar.setObjectName(u"statusbar")
        BatchEditor.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.selectRootDirectoryButton, self.minLengthSpinbox)
        QWidget.setTabOrder(self.minLengthSpinbox, self.editSelectedFilesButton)
        QWidget.setTabOrder(self.editSelectedFilesButton, self.filesToEditSpinbox)
        QWidget.setTabOrder(self.filesToEditSpinbox, self.totalLengthToEditSpinbox)

        self.retranslateUi(BatchEditor)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BatchEditor)
    # setupUi

    def retranslateUi(self, BatchEditor):
        BatchEditor.setWindowTitle(QCoreApplication.translate("BatchEditor", u"Batch Editor", None))
        self.actionasdasddas.setText(QCoreApplication.translate("BatchEditor", u"asdasddas", None))
        self.filesToEditSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.foundFilesProgressBar.setFormat("")
        self.totalLengthToEditSpinbox.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.filesFoundLabel.setText(QCoreApplication.translate("BatchEditor", u"video files found:", None))
        self.editSelectedFilesButton.setText(QCoreApplication.translate("BatchEditor", u"edit selected files", None))
        self.filesLongerThanLabel.setText(QCoreApplication.translate("BatchEditor", u"Select files longer than: ", None))
        self.totalLengthToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"total length to edit: ", None))
        self.rootDirectoryLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"no directory selected", None))
        self.videoFilesToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"video files to edit: ", None))
        self.filesFound.setText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.selectRootDirectoryButton.setText(QCoreApplication.translate("BatchEditor", u"select root directory", None))
        self.totalLength.setText(QCoreApplication.translate("BatchEditor", u"0.0 min", None))
        self.minLabel_3.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.totalLengthLabel.setText(QCoreApplication.translate("BatchEditor", u"total length: ", None))
        self.progressBarLabel.setText(QCoreApplication.translate("BatchEditor", u"not processing", None))
        self.minLabel_2.setText(QCoreApplication.translate("BatchEditor", u"min", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectionTab), QCoreApplication.translate("BatchEditor", u"selection", None))
        self.audioThresholdLabel.setText(QCoreApplication.translate("BatchEditor", u"Audio threshold (%):", None))
        self.multitrackTuningButton.setText(QCoreApplication.translate("BatchEditor", u"multitrack tuning", None))
        self.exportSelector.setItemText(0, QCoreApplication.translate("BatchEditor", u"Premiere Pro", None))
        self.exportSelector.setItemText(1, QCoreApplication.translate("BatchEditor", u"Da Vinci Resolve", None))
        self.exportSelector.setItemText(2, QCoreApplication.translate("BatchEditor", u"Final Cut Pro", None))
        self.exportSelector.setItemText(3, QCoreApplication.translate("BatchEditor", u"ShotCut", None))
        self.exportSelector.setItemText(4, QCoreApplication.translate("BatchEditor", u"Kdenlive", None))
        self.exportSelector.setItemText(5, QCoreApplication.translate("BatchEditor", u"clip seuqence", None))

        self.marginLabel.setText(QCoreApplication.translate("BatchEditor", u"margin (seconds):", None))
        self.exportOptionLabel.setText(QCoreApplication.translate("BatchEditor", u"Export option:", None))
        self.organizeIntoFolders.setText(QCoreApplication.translate("BatchEditor", u"Organize files into folders", None))
        self.separateTracks.setText(QCoreApplication.translate("BatchEditor", u"keep audio tracks separate", None))
        self.splitOnly.setText(QCoreApplication.translate("BatchEditor", u"split clips only", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), QCoreApplication.translate("BatchEditor", u"options", None))
        self.resetConfigButton.setText(QCoreApplication.translate("BatchEditor", u"reset config", None))
        self.saveConfigButton.setText(QCoreApplication.translate("BatchEditor", u"Save config", None))
        self.showCommandButton.setText(QCoreApplication.translate("BatchEditor", u"show command", None))
        self.previewButton.setText(QCoreApplication.translate("BatchEditor", u"preview", None))
        self.startButton.setText(QCoreApplication.translate("BatchEditor", u"Start", None))
    # retranslateUi

