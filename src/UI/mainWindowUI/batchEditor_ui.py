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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_BatchEditor(object):
    def setupUi(self, BatchEditor):
        if not BatchEditor.objectName():
            BatchEditor.setObjectName(u"BatchEditor")
        BatchEditor.resize(400, 500)
        BatchEditor.setMinimumSize(QSize(400, 500))
        BatchEditor.setDocumentMode(False)
        self.centralwidget = QWidget(BatchEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.helpButton = QToolButton(self.centralwidget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        self.helpButton.setAutoFillBackground(False)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QSize(17, 17))
        self.helpButton.setAutoRepeat(False)
        self.helpButton.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        self.verticalLayout_2.addWidget(self.helpButton)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setDocumentMode(False)
        self.selectionTab = QWidget()
        self.selectionTab.setObjectName(u"selectionTab")
        self.verticalLayout = QVBoxLayout(self.selectionTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(46)
        self.totalLength = QLabel(self.selectionTab)
        self.totalLength.setObjectName(u"totalLength")
        self.totalLength.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.totalLength, 3, 1, 1, 1)

        self.line_2 = QFrame(self.selectionTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 3)

        self.totalLengthToEdit = QLabel(self.selectionTab)
        self.totalLengthToEdit.setObjectName(u"totalLengthToEdit")
        self.totalLengthToEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.totalLengthToEdit, 3, 0, 1, 1)

        self.filesToEdit = QLabel(self.selectionTab)
        self.filesToEdit.setObjectName(u"filesToEdit")
        self.filesToEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.filesToEdit, 2, 0, 1, 1)

        self.filesFound = QLabel(self.selectionTab)
        self.filesFound.setObjectName(u"filesFound")
        self.filesFound.setSizeIncrement(QSize(107, 0))
        self.filesFound.setBaseSize(QSize(38, 0))
        self.filesFound.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.filesFound, 2, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.selectRootDirectoryButton = QPushButton(self.selectionTab)
        self.selectRootDirectoryButton.setObjectName(u"selectRootDirectoryButton")

        self.horizontalLayout_4.addWidget(self.selectRootDirectoryButton)

        self.rootDirectoryLabel = QLineEdit(self.selectionTab)
        self.rootDirectoryLabel.setObjectName(u"rootDirectoryLabel")
        self.rootDirectoryLabel.setReadOnly(True)
        self.rootDirectoryLabel.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_4.addWidget(self.rootDirectoryLabel)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 3)

        self.editSelectedFilesButton = QPushButton(self.selectionTab)
        self.editSelectedFilesButton.setObjectName(u"editSelectedFilesButton")
        self.editSelectedFilesButton.setEnabled(False)
        self.editSelectedFilesButton.setCheckable(False)
        self.editSelectedFilesButton.setChecked(False)
        self.editSelectedFilesButton.setFlat(False)

        self.gridLayout_3.addWidget(self.editSelectedFilesButton, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.selectionTab, "")
        self.optionsTab = QWidget()
        self.optionsTab.setObjectName(u"optionsTab")
        self.horizontalLayout = QHBoxLayout(self.optionsTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.optionsGrid = QGridLayout()
        self.optionsGrid.setObjectName(u"optionsGrid")
        self.optionsGrid.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.optionsGrid.setVerticalSpacing(2)
        self.marginSpinbox = QDoubleSpinBox(self.optionsTab)
        self.marginSpinbox.setObjectName(u"marginSpinbox")
        self.marginSpinbox.setSingleStep(0.500000000000000)

        self.optionsGrid.addWidget(self.marginSpinbox, 1, 1, 1, 1)

        self.marginLabel = QLabel(self.optionsTab)
        self.marginLabel.setObjectName(u"marginLabel")
        self.marginLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.marginLabel.setMargin(3)

        self.optionsGrid.addWidget(self.marginLabel, 1, 0, 1, 1)

        self.exportOptionLabel = QLabel(self.optionsTab)
        self.exportOptionLabel.setObjectName(u"exportOptionLabel")
        self.exportOptionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.exportOptionLabel.setMargin(3)

        self.optionsGrid.addWidget(self.exportOptionLabel, 0, 0, 1, 1)

        self.multitrackTuningButton = QPushButton(self.optionsTab)
        self.multitrackTuningButton.setObjectName(u"multitrackTuningButton")
        self.multitrackTuningButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.multitrackTuningButton.sizePolicy().hasHeightForWidth())
        self.multitrackTuningButton.setSizePolicy(sizePolicy2)

        self.optionsGrid.addWidget(self.multitrackTuningButton, 2, 0, 1, 2)

        self.line = QFrame(self.optionsTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.optionsGrid.addWidget(self.line, 3, 0, 1, 2)

        self.separateTracks = QCheckBox(self.optionsTab)
        self.separateTracks.setObjectName(u"separateTracks")
        self.separateTracks.setChecked(True)

        self.optionsGrid.addWidget(self.separateTracks, 4, 0, 1, 1)

        self.splitOnly = QCheckBox(self.optionsTab)
        self.splitOnly.setObjectName(u"splitOnly")
        sizePolicy.setHeightForWidth(self.splitOnly.sizePolicy().hasHeightForWidth())
        self.splitOnly.setSizePolicy(sizePolicy)
        self.splitOnly.setSizeIncrement(QSize(0, 0))

        self.optionsGrid.addWidget(self.splitOnly, 5, 0, 1, 1)

        self.exportSelector = QComboBox(self.optionsTab)
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.addItem("")
        self.exportSelector.setObjectName(u"exportSelector")

        self.optionsGrid.addWidget(self.exportSelector, 0, 1, 1, 1)


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
        self.saveConfigButton = QPushButton(self.centralwidget)
        self.saveConfigButton.setObjectName(u"saveConfigButton")
        self.saveConfigButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.saveConfigButton.sizePolicy().hasHeightForWidth())
        self.saveConfigButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.saveConfigButton, 0, 1, 1, 1)

        self.loadConfigButton = QPushButton(self.centralwidget)
        self.loadConfigButton.setObjectName(u"loadConfigButton")
        self.loadConfigButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.loadConfigButton.sizePolicy().hasHeightForWidth())
        self.loadConfigButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.loadConfigButton, 0, 0, 1, 1)

        self.showCommandButton = QPushButton(self.centralwidget)
        self.showCommandButton.setObjectName(u"showCommandButton")
        self.showCommandButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.showCommandButton.sizePolicy().hasHeightForWidth())
        self.showCommandButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.showCommandButton, 0, 3, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.startButton, 1, 0, 1, 4)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 4)


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
        self.helpButton.setText("")
        self.totalLength.setText(QCoreApplication.translate("BatchEditor", u"0 min total", None))
        self.totalLengthToEdit.setText(QCoreApplication.translate("BatchEditor", u"0 min to edit", None))
        self.filesToEdit.setText(QCoreApplication.translate("BatchEditor", u"0 files to edit", None))
        self.filesFound.setText(QCoreApplication.translate("BatchEditor", u"0 files found", None))
#if QT_CONFIG(tooltip)
        self.selectRootDirectoryButton.setToolTip(QCoreApplication.translate("BatchEditor", u"Browse and select the base folder containing the videos you want to process", None))
#endif // QT_CONFIG(tooltip)
        self.selectRootDirectoryButton.setText(QCoreApplication.translate("BatchEditor", u"select root directory", None))
        self.rootDirectoryLabel.setPlaceholderText(QCoreApplication.translate("BatchEditor", u"no directory selected", None))
#if QT_CONFIG(tooltip)
        self.editSelectedFilesButton.setToolTip(QCoreApplication.translate("BatchEditor", u"Open the file list to manually enable/disable certain videos from the batch", None))
#endif // QT_CONFIG(tooltip)
        self.editSelectedFilesButton.setText(QCoreApplication.translate("BatchEditor", u"edit selected files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectionTab), QCoreApplication.translate("BatchEditor", u"Select", None))
        self.marginSpinbox.setSuffix(QCoreApplication.translate("BatchEditor", u" seconds", None))
        self.marginLabel.setText(QCoreApplication.translate("BatchEditor", u"margin:", None))
        self.exportOptionLabel.setText(QCoreApplication.translate("BatchEditor", u"Export option:", None))
#if QT_CONFIG(tooltip)
        self.multitrackTuningButton.setToolTip(QCoreApplication.translate("BatchEditor", u"<html><head/><body><p>Configure silence detection thresholds for individual audio tracks. The threshold determines the percentage of volume from which auto-editor considers loudness. A 0% threshold means the entire video is loud and no cuts will be made. On the other hand, a 100% threshold means the entire video is considered silent and results in an empty timeline</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.multitrackTuningButton.setText(QCoreApplication.translate("BatchEditor", u"configure silence thresholds", None))
#if QT_CONFIG(tooltip)
        self.separateTracks.setToolTip(QCoreApplication.translate("BatchEditor", u"Don't merge the audio tracks", None))
#endif // QT_CONFIG(tooltip)
        self.separateTracks.setText(QCoreApplication.translate("BatchEditor", u"keep audio tracks separate", None))
#if QT_CONFIG(tooltip)
        self.splitOnly.setToolTip(QCoreApplication.translate("BatchEditor", u"create a sequence with cuts but don't delete the silent clips", None))
#endif // QT_CONFIG(tooltip)
        self.splitOnly.setText(QCoreApplication.translate("BatchEditor", u"split clips only", None))
        self.exportSelector.setItemText(0, QCoreApplication.translate("BatchEditor", u"Premiere Pro", None))
        self.exportSelector.setItemText(1, QCoreApplication.translate("BatchEditor", u"Da Vinci Resolve", None))
        self.exportSelector.setItemText(2, QCoreApplication.translate("BatchEditor", u"Final Cut Pro", None))
        self.exportSelector.setItemText(3, QCoreApplication.translate("BatchEditor", u"ShotCut", None))
        self.exportSelector.setItemText(4, QCoreApplication.translate("BatchEditor", u"Kdenlive", None))
        self.exportSelector.setItemText(5, QCoreApplication.translate("BatchEditor", u"clip sequence", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), QCoreApplication.translate("BatchEditor", u"Configure", None))
#if QT_CONFIG(tooltip)
        self.saveConfigButton.setToolTip(QCoreApplication.translate("BatchEditor", u"Save your current configuration layout and choices to a text file", None))
#endif // QT_CONFIG(tooltip)
        self.saveConfigButton.setText(QCoreApplication.translate("BatchEditor", u"Save config", None))
#if QT_CONFIG(tooltip)
        self.loadConfigButton.setToolTip(QCoreApplication.translate("BatchEditor", u"Restore your previously saved configurations from a text file", None))
#endif // QT_CONFIG(tooltip)
        self.loadConfigButton.setText(QCoreApplication.translate("BatchEditor", u"Load config", None))
#if QT_CONFIG(tooltip)
        self.showCommandButton.setToolTip(QCoreApplication.translate("BatchEditor", u"Preview and copy the underlying auto-editor terminal command", None))
#endif // QT_CONFIG(tooltip)
        self.showCommandButton.setText(QCoreApplication.translate("BatchEditor", u"show command", None))
#if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate("BatchEditor", u"Start batch processing over all selected videos using the current configuration", None))
#endif // QT_CONFIG(tooltip)
        self.startButton.setText(QCoreApplication.translate("BatchEditor", u"Start", None))
    # retranslateUi

