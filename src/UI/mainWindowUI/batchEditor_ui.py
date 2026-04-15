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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_BatchEditor(object):
    def setupUi(self, BatchEditor):
        if not BatchEditor.objectName():
            BatchEditor.setObjectName(u"BatchEditor")
        BatchEditor.resize(455, 467)
        BatchEditor.setDocumentMode(False)
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
        self.tabWidget.setDocumentMode(False)
        self.selectionTab = QWidget()
        self.selectionTab.setObjectName(u"selectionTab")
        self.verticalLayout = QVBoxLayout(self.selectionTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SelectionGrid = QGridLayout()
        self.SelectionGrid.setObjectName(u"SelectionGrid")
        self.SelectionGrid.setHorizontalSpacing(25)
        self.SelectionGrid.setVerticalSpacing(30)
        self.SelectionGrid.setContentsMargins(5, 5, 5, 5)
        self.filesFound = QLabel(self.selectionTab)
        self.filesFound.setObjectName(u"filesFound")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filesFound.sizePolicy().hasHeightForWidth())
        self.filesFound.setSizePolicy(sizePolicy1)
        self.filesFound.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.filesFound, 1, 1, 1, 1)

        self.totalLengthToEditLabel = QLabel(self.selectionTab)
        self.totalLengthToEditLabel.setObjectName(u"totalLengthToEditLabel")
        self.totalLengthToEditLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthToEditLabel, 3, 0, 1, 1)

        self.editSelectedFilesButton = QPushButton(self.selectionTab)
        self.editSelectedFilesButton.setObjectName(u"editSelectedFilesButton")
        self.editSelectedFilesButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editSelectedFilesButton.sizePolicy().hasHeightForWidth())
        self.editSelectedFilesButton.setSizePolicy(sizePolicy2)
        self.editSelectedFilesButton.setCheckable(False)
        self.editSelectedFilesButton.setChecked(False)
        self.editSelectedFilesButton.setFlat(False)

        self.SelectionGrid.addWidget(self.editSelectedFilesButton, 1, 2, 1, 1)

        self.totalLength = QLabel(self.selectionTab)
        self.totalLength.setObjectName(u"totalLength")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.totalLength.sizePolicy().hasHeightForWidth())
        self.totalLength.setSizePolicy(sizePolicy3)
        self.totalLength.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.totalLength, 2, 1, 1, 1)

        self.rootDirectoryLabel = QLineEdit(self.selectionTab)
        self.rootDirectoryLabel.setObjectName(u"rootDirectoryLabel")
        self.rootDirectoryLabel.setReadOnly(True)
        self.rootDirectoryLabel.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.SelectionGrid.addWidget(self.rootDirectoryLabel, 0, 1, 1, 2)

        self.filesFoundLabel = QLabel(self.selectionTab)
        self.filesFoundLabel.setObjectName(u"filesFoundLabel")
        self.filesFoundLabel.setIndent(0)

        self.SelectionGrid.addWidget(self.filesFoundLabel, 1, 0, 1, 1)

        self.selectRootDirectoryButton = QPushButton(self.selectionTab)
        self.selectRootDirectoryButton.setObjectName(u"selectRootDirectoryButton")

        self.SelectionGrid.addWidget(self.selectRootDirectoryButton, 0, 0, 1, 1)

        self.totalLengthToEdit = QLabel(self.selectionTab)
        self.totalLengthToEdit.setObjectName(u"totalLengthToEdit")
        sizePolicy1.setHeightForWidth(self.totalLengthToEdit.sizePolicy().hasHeightForWidth())
        self.totalLengthToEdit.setSizePolicy(sizePolicy1)
        self.totalLengthToEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SelectionGrid.addWidget(self.totalLengthToEdit, 3, 1, 1, 1)

        self.totalLengthLabel = QLabel(self.selectionTab)
        self.totalLengthLabel.setObjectName(u"totalLengthLabel")
        self.totalLengthLabel.setEnabled(True)
        self.totalLengthLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.totalLengthLabel, 2, 0, 1, 1)


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
        self.marginSpinbox = QDoubleSpinBox(self.optionsTab)
        self.marginSpinbox.setObjectName(u"marginSpinbox")
        self.marginSpinbox.setSingleStep(0.500000000000000)

        self.optionsGrid.addWidget(self.marginSpinbox, 2, 1, 1, 1)

        self.audioThresholdSpinbox = QDoubleSpinBox(self.optionsTab)
        self.audioThresholdSpinbox.setObjectName(u"audioThresholdSpinbox")
        self.audioThresholdSpinbox.setSingleStep(0.500000000000000)

        self.optionsGrid.addWidget(self.audioThresholdSpinbox, 1, 2, 1, 1)

        self.audioThresholdLabel = QLabel(self.optionsTab)
        self.audioThresholdLabel.setObjectName(u"audioThresholdLabel")
        self.audioThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel.setMargin(3)

        self.optionsGrid.addWidget(self.audioThresholdLabel, 1, 0, 1, 1)

        self.separateTracks = QCheckBox(self.optionsTab)
        self.separateTracks.setObjectName(u"separateTracks")
        self.separateTracks.setChecked(True)

        self.optionsGrid.addWidget(self.separateTracks, 4, 0, 1, 2)

        self.audiothresholdSlider = QSlider(self.optionsTab)
        self.audiothresholdSlider.setObjectName(u"audiothresholdSlider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(9)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.audiothresholdSlider.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider.setSizePolicy(sizePolicy4)
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

        self.optionsGrid.addWidget(self.audiothresholdSlider, 1, 1, 1, 1)

        self.organizeIntoFolders = QCheckBox(self.optionsTab)
        self.organizeIntoFolders.setObjectName(u"organizeIntoFolders")
        self.organizeIntoFolders.setChecked(True)
        self.organizeIntoFolders.setTristate(False)

        self.optionsGrid.addWidget(self.organizeIntoFolders, 3, 0, 1, 2)

        self.exportOptionLabel = QLabel(self.optionsTab)
        self.exportOptionLabel.setObjectName(u"exportOptionLabel")
        self.exportOptionLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.exportOptionLabel.setMargin(3)

        self.optionsGrid.addWidget(self.exportOptionLabel, 0, 0, 1, 1)

        self.marginLabel = QLabel(self.optionsTab)
        self.marginLabel.setObjectName(u"marginLabel")
        self.marginLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.marginLabel.setMargin(3)

        self.optionsGrid.addWidget(self.marginLabel, 2, 0, 1, 1)

        self.splitOnly = QCheckBox(self.optionsTab)
        self.splitOnly.setObjectName(u"splitOnly")

        self.optionsGrid.addWidget(self.splitOnly, 5, 0, 1, 2)

        self.exportSelector = QComboBox(self.optionsTab)
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.setObjectName(u"exportSelector")

        self.optionsGrid.addWidget(self.exportSelector, 0, 1, 1, 3)

        self.multitrackTuningButton = QPushButton(self.optionsTab)
        self.multitrackTuningButton.setObjectName(u"multitrackTuningButton")
        self.multitrackTuningButton.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.multitrackTuningButton.sizePolicy().hasHeightForWidth())
        self.multitrackTuningButton.setSizePolicy(sizePolicy5)

        self.optionsGrid.addWidget(self.multitrackTuningButton, 1, 3, 1, 1)

        self.optionsGrid.setColumnStretch(0, 1)

        self.horizontalLayout.addLayout(self.optionsGrid)

        self.tabWidget.addTab(self.optionsTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

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

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 4)

        self.loadConfigButton = QPushButton(self.centralwidget)
        self.loadConfigButton.setObjectName(u"loadConfigButton")
        self.loadConfigButton.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.loadConfigButton.sizePolicy().hasHeightForWidth())
        self.loadConfigButton.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.loadConfigButton, 0, 0, 1, 1)

        self.showCommandButton = QPushButton(self.centralwidget)
        self.showCommandButton.setObjectName(u"showCommandButton")
        self.showCommandButton.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.showCommandButton.sizePolicy().hasHeightForWidth())
        self.showCommandButton.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.showCommandButton, 0, 3, 1, 1)

        self.saveConfigButton = QPushButton(self.centralwidget)
        self.saveConfigButton.setObjectName(u"saveConfigButton")
        self.saveConfigButton.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.saveConfigButton.sizePolicy().hasHeightForWidth())
        self.saveConfigButton.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.saveConfigButton, 0, 1, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.startButton, 1, 0, 1, 4)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        BatchEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(BatchEditor)
        self.statusbar.setObjectName(u"statusbar")
        BatchEditor.setStatusBar(self.statusbar)

        self.retranslateUi(BatchEditor)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BatchEditor)
    # setupUi

    def retranslateUi(self, BatchEditor):
        BatchEditor.setWindowTitle(QCoreApplication.translate("BatchEditor", u"Batch Editor", None))
        self.filesFound.setText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.totalLengthToEditLabel.setText(QCoreApplication.translate("BatchEditor", u"total length to edit: ", None))
        self.editSelectedFilesButton.setText(QCoreApplication.translate("BatchEditor", u"edit selected files", None))
        self.totalLength.setText(QCoreApplication.translate("BatchEditor", u"0 min", None))
        self.rootDirectoryLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"no directory selected", None))
        self.filesFoundLabel.setText(QCoreApplication.translate("BatchEditor", u"video files found:", None))
        self.selectRootDirectoryButton.setText(QCoreApplication.translate("BatchEditor", u"select root directory", None))
        self.totalLengthToEdit.setText(QCoreApplication.translate("BatchEditor", u"0 min", None))
        self.totalLengthLabel.setText(QCoreApplication.translate("BatchEditor", u"total length: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectionTab), QCoreApplication.translate("BatchEditor", u"Select", None))
        self.audioThresholdLabel.setText(QCoreApplication.translate("BatchEditor", u"Audio threshold (%):", None))
        self.separateTracks.setText(QCoreApplication.translate("BatchEditor", u"keep audio tracks separate", None))
        self.organizeIntoFolders.setText(QCoreApplication.translate("BatchEditor", u"Organize files into folders", None))
        self.exportOptionLabel.setText(QCoreApplication.translate("BatchEditor", u"Export option:", None))
        self.marginLabel.setText(QCoreApplication.translate("BatchEditor", u"margin (seconds):", None))
        self.splitOnly.setText(QCoreApplication.translate("BatchEditor", u"split clips only", None))
        self.exportSelector.setItemText(0, QCoreApplication.translate("BatchEditor", u"Premiere Pro", None))
        self.exportSelector.setItemText(1, QCoreApplication.translate("BatchEditor", u"Da Vinci Resolve", None))
        self.exportSelector.setItemText(2, QCoreApplication.translate("BatchEditor", u"Final Cut Pro", None))
        self.exportSelector.setItemText(3, QCoreApplication.translate("BatchEditor", u"ShotCut", None))
        self.exportSelector.setItemText(4, QCoreApplication.translate("BatchEditor", u"Kdenlive", None))
        self.exportSelector.setItemText(5, QCoreApplication.translate("BatchEditor", u"clip seuqence", None))

        self.multitrackTuningButton.setText(QCoreApplication.translate("BatchEditor", u"multitrack tuning", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), QCoreApplication.translate("BatchEditor", u"Configure", None))
        self.loadConfigButton.setText(QCoreApplication.translate("BatchEditor", u"Load config", None))
        self.showCommandButton.setText(QCoreApplication.translate("BatchEditor", u"show command", None))
        self.saveConfigButton.setText(QCoreApplication.translate("BatchEditor", u"Save config", None))
        self.startButton.setText(QCoreApplication.translate("BatchEditor", u"Start", None))
    # retranslateUi

