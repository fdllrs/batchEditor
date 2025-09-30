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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_BatchEditor(object):
    def setupUi(self, BatchEditor):
        if not BatchEditor.objectName():
            BatchEditor.setObjectName(u"BatchEditor")
        BatchEditor.resize(500, 500)
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

        self.gridLayout.addWidget(self.optionsLabel, 1, 0, 1, 1)

        self.optionsGrid = QGridLayout()
        self.optionsGrid.setObjectName(u"optionsGrid")
        self.optionsGrid.setVerticalSpacing(16)
        self.exportForLabel = QLabel(self.centralwidget)
        self.exportForLabel.setObjectName(u"exportForLabel")

        self.optionsGrid.addWidget(self.exportForLabel, 1, 0, 1, 1)

        self.multitrackTuning = QPushButton(self.centralwidget)
        self.multitrackTuning.setObjectName(u"multitrackTuning")

        self.optionsGrid.addWidget(self.multitrackTuning, 2, 2, 1, 1)

        self.exportSelector = QComboBox(self.centralwidget)
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.setObjectName(u"exportSelector")

        self.optionsGrid.addWidget(self.exportSelector, 1, 1, 1, 2)

        self.preview = QCheckBox(self.centralwidget)
        self.preview.setObjectName(u"preview")

        self.optionsGrid.addWidget(self.preview, 5, 0, 1, 3)

        self.organizeIntoFolders = QCheckBox(self.centralwidget)
        self.organizeIntoFolders.setObjectName(u"organizeIntoFolders")
        self.organizeIntoFolders.setChecked(True)
        self.organizeIntoFolders.setTristate(False)

        self.optionsGrid.addWidget(self.organizeIntoFolders, 3, 0, 1, 3)

        self.splitOnly = QCheckBox(self.centralwidget)
        self.splitOnly.setObjectName(u"splitOnly")

        self.optionsGrid.addWidget(self.splitOnly, 4, 0, 1, 3)

        self.separateTracks = QCheckBox(self.centralwidget)
        self.separateTracks.setObjectName(u"separateTracks")
        self.separateTracks.setChecked(True)

        self.optionsGrid.addWidget(self.separateTracks, 6, 0, 1, 3)

        self.audioThresholdLabel = QLabel(self.centralwidget)
        self.audioThresholdLabel.setObjectName(u"audioThresholdLabel")

        self.optionsGrid.addWidget(self.audioThresholdLabel, 2, 0, 1, 1)

        self.audiothresholdSlider = QSlider(self.centralwidget)
        self.audiothresholdSlider.setObjectName(u"audiothresholdSlider")
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
        self.audiothresholdSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.audiothresholdSlider.setTickInterval(10)

        self.optionsGrid.addWidget(self.audiothresholdSlider, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.optionsGrid, 2, 0, 1, 1)

        self.StartGrid = QVBoxLayout()
        self.StartGrid.setSpacing(12)
        self.StartGrid.setObjectName(u"StartGrid")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")

        self.StartGrid.addWidget(self.startButton)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.StartGrid.addWidget(self.progressBar)


        self.gridLayout.addLayout(self.StartGrid, 4, 0, 1, 1)

        self.editConfigLayout = QHBoxLayout()
        self.editConfigLayout.setObjectName(u"editConfigLayout")
        self.editConfigLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.saveConfig = QPushButton(self.centralwidget)
        self.saveConfig.setObjectName(u"saveConfig")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveConfig.sizePolicy().hasHeightForWidth())
        self.saveConfig.setSizePolicy(sizePolicy1)

        self.editConfigLayout.addWidget(self.saveConfig)

        self.resetConfig = QPushButton(self.centralwidget)
        self.resetConfig.setObjectName(u"resetConfig")
        sizePolicy1.setHeightForWidth(self.resetConfig.sizePolicy().hasHeightForWidth())
        self.resetConfig.setSizePolicy(sizePolicy1)

        self.editConfigLayout.addWidget(self.resetConfig)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editConfigLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.editConfigLayout, 3, 0, 1, 1)

        self.SelectionGrid = QGridLayout()
        self.SelectionGrid.setSpacing(8)
        self.SelectionGrid.setObjectName(u"SelectionGrid")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.label_3, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(110, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.SelectionGrid.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.selectRootDirectoryButton = QPushButton(self.centralwidget)
        self.selectRootDirectoryButton.setObjectName(u"selectRootDirectoryButton")

        self.SelectionGrid.addWidget(self.selectRootDirectoryButton, 0, 0, 1, 1)

        self.rootDirectoryLabel = QLineEdit(self.centralwidget)
        self.rootDirectoryLabel.setObjectName(u"rootDirectoryLabel")
        self.rootDirectoryLabel.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.SelectionGrid.addWidget(self.rootDirectoryLabel, 0, 1, 1, 3)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.label_1, 2, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.SelectionGrid.addWidget(self.label_2, 4, 0, 1, 1)

        self.minLengthSpinbox = QSpinBox(self.centralwidget)
        self.minLengthSpinbox.setObjectName(u"minLengthSpinbox")

        self.SelectionGrid.addWidget(self.minLengthSpinbox, 2, 1, 1, 1)

        self.filesFoundLabel = QLineEdit(self.centralwidget)
        self.filesFoundLabel.setObjectName(u"filesFoundLabel")
        self.filesFoundLabel.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesFoundLabel, 4, 1, 1, 1)

        self.filesToEditLabel = QLineEdit(self.centralwidget)
        self.filesToEditLabel.setObjectName(u"filesToEditLabel")
        self.filesToEditLabel.setReadOnly(True)

        self.SelectionGrid.addWidget(self.filesToEditLabel, 5, 1, 1, 1)

        self.editSelectedFilesButton = QPushButton(self.centralwidget)
        self.editSelectedFilesButton.setObjectName(u"editSelectedFilesButton")
        self.editSelectedFilesButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.editSelectedFilesButton.sizePolicy().hasHeightForWidth())
        self.editSelectedFilesButton.setSizePolicy(sizePolicy1)
        self.editSelectedFilesButton.setCheckable(False)
        self.editSelectedFilesButton.setChecked(False)
        self.editSelectedFilesButton.setFlat(False)

        self.SelectionGrid.addWidget(self.editSelectedFilesButton, 2, 3, 1, 1)

        self.SelectionGrid.setColumnStretch(0, 2)

        self.gridLayout.addLayout(self.SelectionGrid, 0, 0, 1, 1)

        BatchEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(BatchEditor)
        self.statusbar.setObjectName(u"statusbar")
        BatchEditor.setStatusBar(self.statusbar)

        self.retranslateUi(BatchEditor)

        QMetaObject.connectSlotsByName(BatchEditor)
    # setupUi

    def retranslateUi(self, BatchEditor):
        BatchEditor.setWindowTitle(QCoreApplication.translate("BatchEditor", u"Batch Editor", None))
        self.actionasdasddas.setText(QCoreApplication.translate("BatchEditor", u"asdasddas", None))
        self.optionsLabel.setText(QCoreApplication.translate("BatchEditor", u"OPTIONS", None))
        self.exportForLabel.setText(QCoreApplication.translate("BatchEditor", u"Export option:", None))
        self.multitrackTuning.setText(QCoreApplication.translate("BatchEditor", u"multitrack tuning", None))
        self.exportSelector.setItemText(0, QCoreApplication.translate("BatchEditor", u"Premiere Pro", None))
        self.exportSelector.setItemText(1, QCoreApplication.translate("BatchEditor", u"Da Vinci Resolve", None))
        self.exportSelector.setItemText(2, QCoreApplication.translate("BatchEditor", u"Final Cut Pro", None))
        self.exportSelector.setItemText(3, QCoreApplication.translate("BatchEditor", u"ShotCut", None))
        self.exportSelector.setItemText(4, QCoreApplication.translate("BatchEditor", u"Kdenlive", None))
        self.exportSelector.setItemText(5, QCoreApplication.translate("BatchEditor", u"clip seuqence", None))

        self.preview.setText(QCoreApplication.translate("BatchEditor", u"preview before starting", None))
        self.organizeIntoFolders.setText(QCoreApplication.translate("BatchEditor", u"Organize files into folders", None))
        self.splitOnly.setText(QCoreApplication.translate("BatchEditor", u"split clips only", None))
        self.separateTracks.setText(QCoreApplication.translate("BatchEditor", u"keep audio tracks separate", None))
        self.audioThresholdLabel.setText(QCoreApplication.translate("BatchEditor", u"Audio threshold:", None))
        self.startButton.setText(QCoreApplication.translate("BatchEditor", u"Start", None))
        self.saveConfig.setText(QCoreApplication.translate("BatchEditor", u"Save config as default", None))
        self.resetConfig.setText(QCoreApplication.translate("BatchEditor", u"reset config", None))
        self.label_3.setText(QCoreApplication.translate("BatchEditor", u"video files to edit: ", None))
        self.selectRootDirectoryButton.setText(QCoreApplication.translate("BatchEditor", u"select root directory", None))
        self.rootDirectoryLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"no directory selected", None))
        self.label_1.setText(QCoreApplication.translate("BatchEditor", u"Select files longer than (minutes:) ", None))
        self.label_2.setText(QCoreApplication.translate("BatchEditor", u"video files found:", None))
        self.filesFoundLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.filesToEditLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"0", None))
        self.editSelectedFilesButton.setText(QCoreApplication.translate("BatchEditor", u"edit selection", None))
    # retranslateUi

