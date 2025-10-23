# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batchEditor_audioThresholdTuner.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_audioThresholdTunerDialog(object):
    def setupUi(self, audioThresholdTunerDialog):
        if not audioThresholdTunerDialog.objectName():
            audioThresholdTunerDialog.setObjectName(u"audioThresholdTunerDialog")
        audioThresholdTunerDialog.resize(397, 499)
        self.verticalLayout = QVBoxLayout(audioThresholdTunerDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.threshold1Layout = QHBoxLayout()
        self.threshold1Layout.setObjectName(u"threshold1Layout")
        self.audioThresholdLabel = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel.setObjectName(u"audioThresholdLabel")
        self.audioThresholdLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel.setMargin(3)

        self.threshold1Layout.addWidget(self.audioThresholdLabel)

        self.audiothresholdSlider = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider.setObjectName(u"audiothresholdSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audiothresholdSlider.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider.setSizePolicy(sizePolicy)
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

        self.threshold1Layout.addWidget(self.audiothresholdSlider)

        self.audioThresholdSpinbox = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox.setObjectName(u"audioThresholdSpinbox")
        self.audioThresholdSpinbox.setSingleStep(0.500000000000000)

        self.threshold1Layout.addWidget(self.audioThresholdSpinbox)


        self.verticalLayout.addLayout(self.threshold1Layout)

        self.threshold2Layout = QHBoxLayout()
        self.threshold2Layout.setObjectName(u"threshold2Layout")
        self.audioThresholdLabel_2 = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel_2.setObjectName(u"audioThresholdLabel_2")
        self.audioThresholdLabel_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel_2.setMargin(3)

        self.threshold2Layout.addWidget(self.audioThresholdLabel_2)

        self.audiothresholdSlider_2 = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider_2.setObjectName(u"audiothresholdSlider_2")
        sizePolicy.setHeightForWidth(self.audiothresholdSlider_2.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider_2.setSizePolicy(sizePolicy)
        self.audiothresholdSlider_2.setMouseTracking(False)
        self.audiothresholdSlider_2.setTabletTracking(False)
        self.audiothresholdSlider_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider_2.setAcceptDrops(False)
        self.audiothresholdSlider_2.setAutoFillBackground(True)
        self.audiothresholdSlider_2.setMinimum(1)
        self.audiothresholdSlider_2.setMaximum(10000)
        self.audiothresholdSlider_2.setValue(1)
        self.audiothresholdSlider_2.setSliderPosition(1)
        self.audiothresholdSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider_2.setInvertedAppearance(False)
        self.audiothresholdSlider_2.setInvertedControls(False)
        self.audiothresholdSlider_2.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider_2.setTickInterval(1)

        self.threshold2Layout.addWidget(self.audiothresholdSlider_2)

        self.audioThresholdSpinbox_2 = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox_2.setObjectName(u"audioThresholdSpinbox_2")
        self.audioThresholdSpinbox_2.setSingleStep(0.500000000000000)

        self.threshold2Layout.addWidget(self.audioThresholdSpinbox_2)


        self.verticalLayout.addLayout(self.threshold2Layout)

        self.threshold3Layout = QHBoxLayout()
        self.threshold3Layout.setObjectName(u"threshold3Layout")
        self.audioThresholdLabel_3 = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel_3.setObjectName(u"audioThresholdLabel_3")
        self.audioThresholdLabel_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel_3.setMargin(3)

        self.threshold3Layout.addWidget(self.audioThresholdLabel_3)

        self.audiothresholdSlider_3 = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider_3.setObjectName(u"audiothresholdSlider_3")
        sizePolicy.setHeightForWidth(self.audiothresholdSlider_3.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider_3.setSizePolicy(sizePolicy)
        self.audiothresholdSlider_3.setMouseTracking(False)
        self.audiothresholdSlider_3.setTabletTracking(False)
        self.audiothresholdSlider_3.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider_3.setAcceptDrops(False)
        self.audiothresholdSlider_3.setAutoFillBackground(True)
        self.audiothresholdSlider_3.setMinimum(1)
        self.audiothresholdSlider_3.setMaximum(10000)
        self.audiothresholdSlider_3.setValue(1)
        self.audiothresholdSlider_3.setSliderPosition(1)
        self.audiothresholdSlider_3.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider_3.setInvertedAppearance(False)
        self.audiothresholdSlider_3.setInvertedControls(False)
        self.audiothresholdSlider_3.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider_3.setTickInterval(1)

        self.threshold3Layout.addWidget(self.audiothresholdSlider_3)

        self.audioThresholdSpinbox_3 = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox_3.setObjectName(u"audioThresholdSpinbox_3")
        self.audioThresholdSpinbox_3.setSingleStep(0.500000000000000)

        self.threshold3Layout.addWidget(self.audioThresholdSpinbox_3)


        self.verticalLayout.addLayout(self.threshold3Layout)

        self.threshold4Layout_2 = QHBoxLayout()
        self.threshold4Layout_2.setObjectName(u"threshold4Layout_2")
        self.audioThresholdLabel_5 = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel_5.setObjectName(u"audioThresholdLabel_5")
        self.audioThresholdLabel_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel_5.setMargin(3)

        self.threshold4Layout_2.addWidget(self.audioThresholdLabel_5)

        self.audiothresholdSlider_5 = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider_5.setObjectName(u"audiothresholdSlider_5")
        sizePolicy.setHeightForWidth(self.audiothresholdSlider_5.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider_5.setSizePolicy(sizePolicy)
        self.audiothresholdSlider_5.setMouseTracking(False)
        self.audiothresholdSlider_5.setTabletTracking(False)
        self.audiothresholdSlider_5.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider_5.setAcceptDrops(False)
        self.audiothresholdSlider_5.setAutoFillBackground(True)
        self.audiothresholdSlider_5.setMinimum(1)
        self.audiothresholdSlider_5.setMaximum(10000)
        self.audiothresholdSlider_5.setValue(1)
        self.audiothresholdSlider_5.setSliderPosition(1)
        self.audiothresholdSlider_5.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider_5.setInvertedAppearance(False)
        self.audiothresholdSlider_5.setInvertedControls(False)
        self.audiothresholdSlider_5.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider_5.setTickInterval(1)

        self.threshold4Layout_2.addWidget(self.audiothresholdSlider_5)

        self.audioThresholdSpinbox_5 = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox_5.setObjectName(u"audioThresholdSpinbox_5")
        self.audioThresholdSpinbox_5.setSingleStep(0.500000000000000)

        self.threshold4Layout_2.addWidget(self.audioThresholdSpinbox_5)


        self.verticalLayout.addLayout(self.threshold4Layout_2)

        self.threshold5Layout = QHBoxLayout()
        self.threshold5Layout.setObjectName(u"threshold5Layout")
        self.audioThresholdLabel_6 = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel_6.setObjectName(u"audioThresholdLabel_6")
        self.audioThresholdLabel_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel_6.setMargin(3)

        self.threshold5Layout.addWidget(self.audioThresholdLabel_6)

        self.audiothresholdSlider_6 = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider_6.setObjectName(u"audiothresholdSlider_6")
        sizePolicy.setHeightForWidth(self.audiothresholdSlider_6.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider_6.setSizePolicy(sizePolicy)
        self.audiothresholdSlider_6.setMouseTracking(False)
        self.audiothresholdSlider_6.setTabletTracking(False)
        self.audiothresholdSlider_6.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider_6.setAcceptDrops(False)
        self.audiothresholdSlider_6.setAutoFillBackground(True)
        self.audiothresholdSlider_6.setMinimum(1)
        self.audiothresholdSlider_6.setMaximum(10000)
        self.audiothresholdSlider_6.setValue(1)
        self.audiothresholdSlider_6.setSliderPosition(1)
        self.audiothresholdSlider_6.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider_6.setInvertedAppearance(False)
        self.audiothresholdSlider_6.setInvertedControls(False)
        self.audiothresholdSlider_6.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider_6.setTickInterval(1)

        self.threshold5Layout.addWidget(self.audiothresholdSlider_6)

        self.audioThresholdSpinbox_6 = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox_6.setObjectName(u"audioThresholdSpinbox_6")
        self.audioThresholdSpinbox_6.setSingleStep(0.500000000000000)

        self.threshold5Layout.addWidget(self.audioThresholdSpinbox_6)


        self.verticalLayout.addLayout(self.threshold5Layout)

        self.threshold6Layout = QHBoxLayout()
        self.threshold6Layout.setObjectName(u"threshold6Layout")
        self.audioThresholdLabel_7 = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel_7.setObjectName(u"audioThresholdLabel_7")
        self.audioThresholdLabel_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel_7.setMargin(3)

        self.threshold6Layout.addWidget(self.audioThresholdLabel_7)

        self.audiothresholdSlider_7 = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider_7.setObjectName(u"audiothresholdSlider_7")
        sizePolicy.setHeightForWidth(self.audiothresholdSlider_7.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider_7.setSizePolicy(sizePolicy)
        self.audiothresholdSlider_7.setMouseTracking(False)
        self.audiothresholdSlider_7.setTabletTracking(False)
        self.audiothresholdSlider_7.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider_7.setAcceptDrops(False)
        self.audiothresholdSlider_7.setAutoFillBackground(True)
        self.audiothresholdSlider_7.setMinimum(1)
        self.audiothresholdSlider_7.setMaximum(10000)
        self.audiothresholdSlider_7.setValue(1)
        self.audiothresholdSlider_7.setSliderPosition(1)
        self.audiothresholdSlider_7.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider_7.setInvertedAppearance(False)
        self.audiothresholdSlider_7.setInvertedControls(False)
        self.audiothresholdSlider_7.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider_7.setTickInterval(1)

        self.threshold6Layout.addWidget(self.audiothresholdSlider_7)

        self.audioThresholdSpinbox_7 = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox_7.setObjectName(u"audioThresholdSpinbox_7")
        self.audioThresholdSpinbox_7.setSingleStep(0.500000000000000)

        self.threshold6Layout.addWidget(self.audioThresholdSpinbox_7)


        self.verticalLayout.addLayout(self.threshold6Layout)

        self.threshold7Layout = QHBoxLayout()
        self.threshold7Layout.setObjectName(u"threshold7Layout")
        self.audioThresholdLabel_8 = QLabel(audioThresholdTunerDialog)
        self.audioThresholdLabel_8.setObjectName(u"audioThresholdLabel_8")
        self.audioThresholdLabel_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.audioThresholdLabel_8.setMargin(3)

        self.threshold7Layout.addWidget(self.audioThresholdLabel_8)

        self.audiothresholdSlider_8 = QSlider(audioThresholdTunerDialog)
        self.audiothresholdSlider_8.setObjectName(u"audiothresholdSlider_8")
        sizePolicy.setHeightForWidth(self.audiothresholdSlider_8.sizePolicy().hasHeightForWidth())
        self.audiothresholdSlider_8.setSizePolicy(sizePolicy)
        self.audiothresholdSlider_8.setMouseTracking(False)
        self.audiothresholdSlider_8.setTabletTracking(False)
        self.audiothresholdSlider_8.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.audiothresholdSlider_8.setAcceptDrops(False)
        self.audiothresholdSlider_8.setAutoFillBackground(True)
        self.audiothresholdSlider_8.setMinimum(1)
        self.audiothresholdSlider_8.setMaximum(10000)
        self.audiothresholdSlider_8.setValue(1)
        self.audiothresholdSlider_8.setSliderPosition(1)
        self.audiothresholdSlider_8.setOrientation(Qt.Orientation.Horizontal)
        self.audiothresholdSlider_8.setInvertedAppearance(False)
        self.audiothresholdSlider_8.setInvertedControls(False)
        self.audiothresholdSlider_8.setTickPosition(QSlider.TickPosition.NoTicks)
        self.audiothresholdSlider_8.setTickInterval(1)

        self.threshold7Layout.addWidget(self.audiothresholdSlider_8)

        self.audioThresholdSpinbox_8 = QDoubleSpinBox(audioThresholdTunerDialog)
        self.audioThresholdSpinbox_8.setObjectName(u"audioThresholdSpinbox_8")
        self.audioThresholdSpinbox_8.setSingleStep(0.500000000000000)

        self.threshold7Layout.addWidget(self.audioThresholdSpinbox_8)


        self.verticalLayout.addLayout(self.threshold7Layout)

        self.buttonBox = QDialogButtonBox(audioThresholdTunerDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(audioThresholdTunerDialog)
        self.buttonBox.accepted.connect(audioThresholdTunerDialog.accept)
        self.buttonBox.rejected.connect(audioThresholdTunerDialog.reject)

        QMetaObject.connectSlotsByName(audioThresholdTunerDialog)
    # setupUi

    def retranslateUi(self, audioThresholdTunerDialog):
        audioThresholdTunerDialog.setWindowTitle(QCoreApplication.translate("audioThresholdTunerDialog", u"Dialog", None))
        self.audioThresholdLabel.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 1 threshold (%):", None))
        self.audioThresholdLabel_2.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 2 threshold (%):", None))
        self.audioThresholdLabel_3.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 3 threshold (%):", None))
        self.audioThresholdLabel_5.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 4 threshold (%):", None))
        self.audioThresholdLabel_6.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 5 threshold (%):", None))
        self.audioThresholdLabel_7.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 6 threshold (%):", None))
        self.audioThresholdLabel_8.setText(QCoreApplication.translate("audioThresholdTunerDialog", u"Track 7 threshold (%):", None))
    # retranslateUi

