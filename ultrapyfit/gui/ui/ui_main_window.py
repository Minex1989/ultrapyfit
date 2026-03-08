# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTextBrowser, QToolBox,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from ultrapyfit.gui.widgets.mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 792)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(7680, 4320))
        MainWindow.setBaseSize(QSize(1280, 800))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actImport = QAction(MainWindow)
        self.actImport.setObjectName(u"actImport")
        self.actExport = QAction(MainWindow)
        self.actExport.setObjectName(u"actExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabMain = QTabWidget(self.centralwidget)
        self.tabMain.setObjectName(u"tabMain")
        self.pageDataExplorer = QWidget()
        self.pageDataExplorer.setObjectName(u"pageDataExplorer")
        self.verticalLayout_11 = QVBoxLayout(self.pageDataExplorer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.grpViewAndExport = QGroupBox(self.pageDataExplorer)
        self.grpViewAndExport.setObjectName(u"grpViewAndExport")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.grpViewAndExport.sizePolicy().hasHeightForWidth())
        self.grpViewAndExport.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.grpViewAndExport)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 9, -1, -1)
        self.lblViewMode = QLabel(self.grpViewAndExport)
        self.lblViewMode.setObjectName(u"lblViewMode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblViewMode.sizePolicy().hasHeightForWidth())
        self.lblViewMode.setSizePolicy(sizePolicy2)
        self.lblViewMode.setMinimumSize(QSize(0, 28))
        self.lblViewMode.setMaximumSize(QSize(16777215, 28))
        self.lblViewMode.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lblViewMode)

        self.cbViewMode = QComboBox(self.grpViewAndExport)
        self.cbViewMode.addItem("")
        self.cbViewMode.addItem("")
        self.cbViewMode.addItem("")
        self.cbViewMode.setObjectName(u"cbViewMode")
        self.cbViewMode.setEnabled(False)
        self.cbViewMode.setMinimumSize(QSize(200, 28))
        self.cbViewMode.setMaximumSize(QSize(200, 28))

        self.horizontalLayout_12.addWidget(self.cbViewMode)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.btnExportPlot = QPushButton(self.grpViewAndExport)
        self.btnExportPlot.setObjectName(u"btnExportPlot")
        self.btnExportPlot.setEnabled(False)
        self.btnExportPlot.setMinimumSize(QSize(121, 28))
        self.btnExportPlot.setMaximumSize(QSize(121, 28))

        self.horizontalLayout_12.addWidget(self.btnExportPlot)


        self.verticalLayout_11.addWidget(self.grpViewAndExport)

        self.mplWidget = MplWidget(self.pageDataExplorer)
        self.mplWidget.setObjectName(u"mplWidget")
        sizePolicy.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.mplWidget)

        self.stackedViewModeOptions = QStackedWidget(self.pageDataExplorer)
        self.stackedViewModeOptions.setObjectName(u"stackedViewModeOptions")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedViewModeOptions.sizePolicy().hasHeightForWidth())
        self.stackedViewModeOptions.setSizePolicy(sizePolicy3)
        self.stackedViewModeOptions.setMinimumSize(QSize(0, 61))
        self.stackedViewModeOptions.setMaximumSize(QSize(16777215, 61))
        self.page3DOptions = QWidget()
        self.page3DOptions.setObjectName(u"page3DOptions")
        self.page3DOptions.setMinimumSize(QSize(0, 0))
        self.page3DOptions.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.page3DOptions)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.grp3DOptions = QGroupBox(self.page3DOptions)
        self.grp3DOptions.setObjectName(u"grp3DOptions")
        self.grp3DOptions.setMinimumSize(QSize(0, 61))
        self.grp3DOptions.setMaximumSize(QSize(16777215, 61))
        self.horizontalLayout_10 = QHBoxLayout(self.grp3DOptions)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.lblColorMaps3D = QLabel(self.grp3DOptions)
        self.lblColorMaps3D.setObjectName(u"lblColorMaps3D")
        sizePolicy2.setHeightForWidth(self.lblColorMaps3D.sizePolicy().hasHeightForWidth())
        self.lblColorMaps3D.setSizePolicy(sizePolicy2)
        self.lblColorMaps3D.setMinimumSize(QSize(0, 26))
        self.lblColorMaps3D.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_10.addWidget(self.lblColorMaps3D)

        self.cbColormaps3D = QComboBox(self.grp3DOptions)
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.setObjectName(u"cbColormaps3D")
        self.cbColormaps3D.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cbColormaps3D.sizePolicy().hasHeightForWidth())
        self.cbColormaps3D.setSizePolicy(sizePolicy2)
        self.cbColormaps3D.setMinimumSize(QSize(121, 26))
        self.cbColormaps3D.setMaximumSize(QSize(121, 26))

        self.horizontalLayout_10.addWidget(self.cbColormaps3D)

        self.lblViewStyle3D = QLabel(self.grp3DOptions)
        self.lblViewStyle3D.setObjectName(u"lblViewStyle3D")
        sizePolicy2.setHeightForWidth(self.lblViewStyle3D.sizePolicy().hasHeightForWidth())
        self.lblViewStyle3D.setSizePolicy(sizePolicy2)
        self.lblViewStyle3D.setMinimumSize(QSize(0, 26))
        self.lblViewStyle3D.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_10.addWidget(self.lblViewStyle3D)

        self.cbStyle3D = QComboBox(self.grp3DOptions)
        self.cbStyle3D.addItem("")
        self.cbStyle3D.addItem("")
        self.cbStyle3D.addItem("")
        self.cbStyle3D.setObjectName(u"cbStyle3D")
        self.cbStyle3D.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cbStyle3D.sizePolicy().hasHeightForWidth())
        self.cbStyle3D.setSizePolicy(sizePolicy2)
        self.cbStyle3D.setMinimumSize(QSize(121, 26))
        self.cbStyle3D.setMaximumSize(QSize(121, 26))

        self.horizontalLayout_10.addWidget(self.cbStyle3D)

        self.lblRenderQuality3D = QLabel(self.grp3DOptions)
        self.lblRenderQuality3D.setObjectName(u"lblRenderQuality3D")
        sizePolicy2.setHeightForWidth(self.lblRenderQuality3D.sizePolicy().hasHeightForWidth())
        self.lblRenderQuality3D.setSizePolicy(sizePolicy2)
        self.lblRenderQuality3D.setMinimumSize(QSize(0, 26))
        self.lblRenderQuality3D.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_10.addWidget(self.lblRenderQuality3D)

        self.sbRenderQuality3D = QSpinBox(self.grp3DOptions)
        self.sbRenderQuality3D.setObjectName(u"sbRenderQuality3D")
        self.sbRenderQuality3D.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.sbRenderQuality3D.sizePolicy().hasHeightForWidth())
        self.sbRenderQuality3D.setSizePolicy(sizePolicy2)
        self.sbRenderQuality3D.setMinimumSize(QSize(91, 26))
        self.sbRenderQuality3D.setMaximumSize(QSize(121, 26))
        self.sbRenderQuality3D.setMinimum(1)
        self.sbRenderQuality3D.setMaximum(10)

        self.horizontalLayout_10.addWidget(self.sbRenderQuality3D)

        self.lblResetView3D = QLabel(self.grp3DOptions)
        self.lblResetView3D.setObjectName(u"lblResetView3D")
        sizePolicy2.setHeightForWidth(self.lblResetView3D.sizePolicy().hasHeightForWidth())
        self.lblResetView3D.setSizePolicy(sizePolicy2)
        self.lblResetView3D.setMinimumSize(QSize(0, 26))
        self.lblResetView3D.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_10.addWidget(self.lblResetView3D)

        self.btnResetView3D = QToolButton(self.grp3DOptions)
        self.btnResetView3D.setObjectName(u"btnResetView3D")
        self.btnResetView3D.setEnabled(False)
        self.btnResetView3D.setMinimumSize(QSize(28, 26))
        self.btnResetView3D.setMaximumSize(QSize(28, 28))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRestore))
        self.btnResetView3D.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.btnResetView3D)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.grp3DOptions)

        self.stackedViewModeOptions.addWidget(self.page3DOptions)
        self.pageSpectraOptions = QWidget()
        self.pageSpectraOptions.setObjectName(u"pageSpectraOptions")
        self.horizontalLayout_4 = QHBoxLayout(self.pageSpectraOptions)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.grpTimeSelectionSpectra = QGroupBox(self.pageSpectraOptions)
        self.grpTimeSelectionSpectra.setObjectName(u"grpTimeSelectionSpectra")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.grpTimeSelectionSpectra.sizePolicy().hasHeightForWidth())
        self.grpTimeSelectionSpectra.setSizePolicy(sizePolicy4)
        self.gridLayout_4 = QGridLayout(self.grpTimeSelectionSpectra)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rbAllSpectra = QRadioButton(self.grpTimeSelectionSpectra)
        self.rbAllSpectra.setObjectName(u"rbAllSpectra")
        self.rbAllSpectra.setMinimumSize(QSize(0, 26))
        self.rbAllSpectra.setChecked(True)

        self.gridLayout_4.addWidget(self.rbAllSpectra, 0, 0, 1, 1)

        self.rbAutomaticSpectra = QRadioButton(self.grpTimeSelectionSpectra)
        self.rbAutomaticSpectra.setObjectName(u"rbAutomaticSpectra")
        self.rbAutomaticSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.rbAutomaticSpectra, 1, 0, 1, 1)

        self.lblNumberOfSpectra = QLabel(self.grpTimeSelectionSpectra)
        self.lblNumberOfSpectra.setObjectName(u"lblNumberOfSpectra")
        sizePolicy2.setHeightForWidth(self.lblNumberOfSpectra.sizePolicy().hasHeightForWidth())
        self.lblNumberOfSpectra.setSizePolicy(sizePolicy2)
        self.lblNumberOfSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.lblNumberOfSpectra, 2, 0, 1, 1)

        self.sbNumberOfSpectra = QSpinBox(self.grpTimeSelectionSpectra)
        self.sbNumberOfSpectra.setObjectName(u"sbNumberOfSpectra")
        self.sbNumberOfSpectra.setEnabled(False)
        self.sbNumberOfSpectra.setMinimumSize(QSize(0, 26))
        self.sbNumberOfSpectra.setMaximum(1024)
        self.sbNumberOfSpectra.setValue(8)

        self.gridLayout_4.addWidget(self.sbNumberOfSpectra, 2, 1, 1, 1)

        self.chkAtWavelengthSpectra = QCheckBox(self.grpTimeSelectionSpectra)
        self.chkAtWavelengthSpectra.setObjectName(u"chkAtWavelengthSpectra")
        self.chkAtWavelengthSpectra.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.chkAtWavelengthSpectra.sizePolicy().hasHeightForWidth())
        self.chkAtWavelengthSpectra.setSizePolicy(sizePolicy2)
        self.chkAtWavelengthSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.chkAtWavelengthSpectra, 3, 0, 1, 1)

        self.dsbAtWavelengthSpectra = QDoubleSpinBox(self.grpTimeSelectionSpectra)
        self.dsbAtWavelengthSpectra.setObjectName(u"dsbAtWavelengthSpectra")
        self.dsbAtWavelengthSpectra.setEnabled(False)
        self.dsbAtWavelengthSpectra.setMinimumSize(QSize(0, 26))
        self.dsbAtWavelengthSpectra.setMaximum(10000.000000000000000)

        self.gridLayout_4.addWidget(self.dsbAtWavelengthSpectra, 3, 1, 1, 1)

        self.rbCustomSpectra = QRadioButton(self.grpTimeSelectionSpectra)
        self.rbCustomSpectra.setObjectName(u"rbCustomSpectra")
        self.rbCustomSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.rbCustomSpectra, 4, 0, 1, 1)

        self.leCustomTimesSpectral = QLineEdit(self.grpTimeSelectionSpectra)
        self.leCustomTimesSpectral.setObjectName(u"leCustomTimesSpectral")
        self.leCustomTimesSpectral.setEnabled(False)
        self.leCustomTimesSpectral.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.leCustomTimesSpectral, 5, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.grpTimeSelectionSpectra)

        self.grpProcessingAndRangesSpectra = QGroupBox(self.pageSpectraOptions)
        self.grpProcessingAndRangesSpectra.setObjectName(u"grpProcessingAndRangesSpectra")
        sizePolicy4.setHeightForWidth(self.grpProcessingAndRangesSpectra.sizePolicy().hasHeightForWidth())
        self.grpProcessingAndRangesSpectra.setSizePolicy(sizePolicy4)
        self.verticalLayout_4 = QVBoxLayout(self.grpProcessingAndRangesSpectra)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chkTimeRangeSpectra = QCheckBox(self.grpProcessingAndRangesSpectra)
        self.chkTimeRangeSpectra.setObjectName(u"chkTimeRangeSpectra")
        self.chkTimeRangeSpectra.setMinimumSize(QSize(0, 26))
        self.chkTimeRangeSpectra.setMaximumSize(QSize(262, 16777215))

        self.verticalLayout_4.addWidget(self.chkTimeRangeSpectra)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lblTimeRangeStartSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblTimeRangeStartSpectra.setObjectName(u"lblTimeRangeStartSpectra")
        sizePolicy2.setHeightForWidth(self.lblTimeRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.lblTimeRangeStartSpectra.setSizePolicy(sizePolicy2)
        self.lblTimeRangeStartSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.lblTimeRangeStartSpectra)

        self.dsbTimeRangeStartSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbTimeRangeStartSpectra.setObjectName(u"dsbTimeRangeStartSpectra")
        self.dsbTimeRangeStartSpectra.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dsbTimeRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.dsbTimeRangeStartSpectra.setSizePolicy(sizePolicy5)
        self.dsbTimeRangeStartSpectra.setMinimumSize(QSize(0, 26))
        self.dsbTimeRangeStartSpectra.setMinimum(-10.000000000000000)
        self.dsbTimeRangeStartSpectra.setMaximum(100000.000000000000000)

        self.horizontalLayout_5.addWidget(self.dsbTimeRangeStartSpectra)

        self.lblTimeRangeStopSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblTimeRangeStopSpectra.setObjectName(u"lblTimeRangeStopSpectra")
        sizePolicy2.setHeightForWidth(self.lblTimeRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.lblTimeRangeStopSpectra.setSizePolicy(sizePolicy2)
        self.lblTimeRangeStopSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.lblTimeRangeStopSpectra)

        self.dsbTimeRangeStopSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbTimeRangeStopSpectra.setObjectName(u"dsbTimeRangeStopSpectra")
        self.dsbTimeRangeStopSpectra.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.dsbTimeRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.dsbTimeRangeStopSpectra.setSizePolicy(sizePolicy5)
        self.dsbTimeRangeStopSpectra.setMinimumSize(QSize(0, 26))
        self.dsbTimeRangeStopSpectra.setMinimum(-10.000000000000000)
        self.dsbTimeRangeStopSpectra.setMaximum(100000.000000000000000)

        self.horizontalLayout_5.addWidget(self.dsbTimeRangeStopSpectra)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.chkFromMaxToMinSpectra = QCheckBox(self.grpProcessingAndRangesSpectra)
        self.chkFromMaxToMinSpectra.setObjectName(u"chkFromMaxToMinSpectra")
        self.chkFromMaxToMinSpectra.setMinimumSize(QSize(0, 26))

        self.verticalLayout_4.addWidget(self.chkFromMaxToMinSpectra)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lblAverageSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblAverageSpectra.setObjectName(u"lblAverageSpectra")
        sizePolicy2.setHeightForWidth(self.lblAverageSpectra.sizePolicy().hasHeightForWidth())
        self.lblAverageSpectra.setSizePolicy(sizePolicy2)
        self.lblAverageSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_7.addWidget(self.lblAverageSpectra)

        self.sbAverageSpectra = QSpinBox(self.grpProcessingAndRangesSpectra)
        self.sbAverageSpectra.setObjectName(u"sbAverageSpectra")
        sizePolicy5.setHeightForWidth(self.sbAverageSpectra.sizePolicy().hasHeightForWidth())
        self.sbAverageSpectra.setSizePolicy(sizePolicy5)
        self.sbAverageSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_7.addWidget(self.sbAverageSpectra)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.chkMaskRangeSpectra = QCheckBox(self.grpProcessingAndRangesSpectra)
        self.chkMaskRangeSpectra.setObjectName(u"chkMaskRangeSpectra")
        self.chkMaskRangeSpectra.setMinimumSize(QSize(0, 26))

        self.verticalLayout_4.addWidget(self.chkMaskRangeSpectra)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lblMaskRangeStartSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblMaskRangeStartSpectra.setObjectName(u"lblMaskRangeStartSpectra")
        sizePolicy2.setHeightForWidth(self.lblMaskRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.lblMaskRangeStartSpectra.setSizePolicy(sizePolicy2)
        self.lblMaskRangeStartSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.lblMaskRangeStartSpectra)

        self.dsbMaskRangeStartSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbMaskRangeStartSpectra.setObjectName(u"dsbMaskRangeStartSpectra")
        self.dsbMaskRangeStartSpectra.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.dsbMaskRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.dsbMaskRangeStartSpectra.setSizePolicy(sizePolicy5)
        self.dsbMaskRangeStartSpectra.setMinimumSize(QSize(0, 26))
        self.dsbMaskRangeStartSpectra.setMaximum(10000.000000000000000)

        self.horizontalLayout_6.addWidget(self.dsbMaskRangeStartSpectra)

        self.lblMaskRangeStopSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblMaskRangeStopSpectra.setObjectName(u"lblMaskRangeStopSpectra")
        sizePolicy2.setHeightForWidth(self.lblMaskRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.lblMaskRangeStopSpectra.setSizePolicy(sizePolicy2)
        self.lblMaskRangeStopSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.lblMaskRangeStopSpectra)

        self.dsbMaskRangeStopSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbMaskRangeStopSpectra.setObjectName(u"dsbMaskRangeStopSpectra")
        self.dsbMaskRangeStopSpectra.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.dsbMaskRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.dsbMaskRangeStopSpectra.setSizePolicy(sizePolicy5)
        self.dsbMaskRangeStopSpectra.setMinimumSize(QSize(0, 26))
        self.dsbMaskRangeStopSpectra.setMaximum(10000.000000000000000)

        self.horizontalLayout_6.addWidget(self.dsbMaskRangeStopSpectra)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.grpProcessingAndRangesSpectra)

        self.grpStyleSpectra = QGroupBox(self.pageSpectraOptions)
        self.grpStyleSpectra.setObjectName(u"grpStyleSpectra")
        sizePolicy4.setHeightForWidth(self.grpStyleSpectra.sizePolicy().hasHeightForWidth())
        self.grpStyleSpectra.setSizePolicy(sizePolicy4)
        self.grpStyleSpectra.setMaximumSize(QSize(211, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.grpStyleSpectra)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblColormapsSpectra = QLabel(self.grpStyleSpectra)
        self.lblColormapsSpectra.setObjectName(u"lblColormapsSpectra")

        self.verticalLayout_2.addWidget(self.lblColormapsSpectra)

        self.cbColormapsSpectra = QComboBox(self.grpStyleSpectra)
        self.cbColormapsSpectra.addItem("")
        self.cbColormapsSpectra.addItem("")
        self.cbColormapsSpectra.addItem("")
        self.cbColormapsSpectra.addItem("")
        self.cbColormapsSpectra.addItem("")
        self.cbColormapsSpectra.setObjectName(u"cbColormapsSpectra")
        sizePolicy5.setHeightForWidth(self.cbColormapsSpectra.sizePolicy().hasHeightForWidth())
        self.cbColormapsSpectra.setSizePolicy(sizePolicy5)
        self.cbColormapsSpectra.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.cbColormapsSpectra)

        self.lblLegendSpectra = QLabel(self.grpStyleSpectra)
        self.lblLegendSpectra.setObjectName(u"lblLegendSpectra")

        self.verticalLayout_2.addWidget(self.lblLegendSpectra)

        self.cbLegendSpectra = QComboBox(self.grpStyleSpectra)
        self.cbLegendSpectra.addItem("")
        self.cbLegendSpectra.addItem("")
        self.cbLegendSpectra.addItem("")
        self.cbLegendSpectra.setObjectName(u"cbLegendSpectra")
        sizePolicy5.setHeightForWidth(self.cbLegendSpectra.sizePolicy().hasHeightForWidth())
        self.cbLegendSpectra.setSizePolicy(sizePolicy5)
        self.cbLegendSpectra.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.cbLegendSpectra)

        self.lblStyleSpectra = QLabel(self.grpStyleSpectra)
        self.lblStyleSpectra.setObjectName(u"lblStyleSpectra")

        self.verticalLayout_2.addWidget(self.lblStyleSpectra)

        self.cbStyleSpectra = QComboBox(self.grpStyleSpectra)
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.addItem("")
        self.cbStyleSpectra.setObjectName(u"cbStyleSpectra")
        sizePolicy5.setHeightForWidth(self.cbStyleSpectra.sizePolicy().hasHeightForWidth())
        self.cbStyleSpectra.setSizePolicy(sizePolicy5)
        self.cbStyleSpectra.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.cbStyleSpectra)


        self.horizontalLayout_3.addWidget(self.grpStyleSpectra)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedViewModeOptions.addWidget(self.pageSpectraOptions)
        self.pageTracesOptions = QWidget()
        self.pageTracesOptions.setObjectName(u"pageTracesOptions")
        self.horizontalLayout_8 = QHBoxLayout(self.pageTracesOptions)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.grpWavelengthSelectionTrace = QGroupBox(self.pageTracesOptions)
        self.grpWavelengthSelectionTrace.setObjectName(u"grpWavelengthSelectionTrace")
        self.grpWavelengthSelectionTrace.setMinimumSize(QSize(0, 149))
        self.grpWavelengthSelectionTrace.setMaximumSize(QSize(16777215, 149))
        self.verticalLayout_5 = QVBoxLayout(self.grpWavelengthSelectionTrace)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 9)
        self.rbAllTrace = QRadioButton(self.grpWavelengthSelectionTrace)
        self.rbAllTrace.setObjectName(u"rbAllTrace")
        sizePolicy2.setHeightForWidth(self.rbAllTrace.sizePolicy().hasHeightForWidth())
        self.rbAllTrace.setSizePolicy(sizePolicy2)
        self.rbAllTrace.setMinimumSize(QSize(111, 26))
        self.rbAllTrace.setMaximumSize(QSize(111, 26))
        self.rbAllTrace.setChecked(True)

        self.verticalLayout_5.addWidget(self.rbAllTrace)

        self.rbAutomaticTrace = QRadioButton(self.grpWavelengthSelectionTrace)
        self.rbAutomaticTrace.setObjectName(u"rbAutomaticTrace")
        sizePolicy2.setHeightForWidth(self.rbAutomaticTrace.sizePolicy().hasHeightForWidth())
        self.rbAutomaticTrace.setSizePolicy(sizePolicy2)
        self.rbAutomaticTrace.setMinimumSize(QSize(111, 26))
        self.rbAutomaticTrace.setMaximumSize(QSize(111, 26))
        self.rbAutomaticTrace.setChecked(False)

        self.verticalLayout_5.addWidget(self.rbAutomaticTrace)

        self.rbCustomTrace = QRadioButton(self.grpWavelengthSelectionTrace)
        self.rbCustomTrace.setObjectName(u"rbCustomTrace")
        sizePolicy2.setHeightForWidth(self.rbCustomTrace.sizePolicy().hasHeightForWidth())
        self.rbCustomTrace.setSizePolicy(sizePolicy2)
        self.rbCustomTrace.setMinimumSize(QSize(111, 26))
        self.rbCustomTrace.setMaximumSize(QSize(111, 26))

        self.verticalLayout_5.addWidget(self.rbCustomTrace)

        self.leCustomWavelengthTrace = QLineEdit(self.grpWavelengthSelectionTrace)
        self.leCustomWavelengthTrace.setObjectName(u"leCustomWavelengthTrace")
        self.leCustomWavelengthTrace.setEnabled(False)
        self.leCustomWavelengthTrace.setMinimumSize(QSize(0, 26))
        self.leCustomWavelengthTrace.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_5.addWidget(self.leCustomWavelengthTrace)


        self.horizontalLayout_8.addWidget(self.grpWavelengthSelectionTrace)

        self.grpStyleTrace = QGroupBox(self.pageTracesOptions)
        self.grpStyleTrace.setObjectName(u"grpStyleTrace")
        self.grpStyleTrace.setMinimumSize(QSize(0, 149))
        self.grpStyleTrace.setMaximumSize(QSize(16777215, 149))
        self.verticalLayout_6 = QVBoxLayout(self.grpStyleTrace)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 0, 9, -1)
        self.lblLegendTrace = QLabel(self.grpStyleTrace)
        self.lblLegendTrace.setObjectName(u"lblLegendTrace")
        sizePolicy2.setHeightForWidth(self.lblLegendTrace.sizePolicy().hasHeightForWidth())
        self.lblLegendTrace.setSizePolicy(sizePolicy2)
        self.lblLegendTrace.setMinimumSize(QSize(111, 26))
        self.lblLegendTrace.setMaximumSize(QSize(111, 26))

        self.verticalLayout_6.addWidget(self.lblLegendTrace)

        self.cbLegendTrace = QComboBox(self.grpStyleTrace)
        self.cbLegendTrace.addItem("")
        self.cbLegendTrace.addItem("")
        self.cbLegendTrace.addItem("")
        self.cbLegendTrace.setObjectName(u"cbLegendTrace")
        sizePolicy5.setHeightForWidth(self.cbLegendTrace.sizePolicy().hasHeightForWidth())
        self.cbLegendTrace.setSizePolicy(sizePolicy5)
        self.cbLegendTrace.setMinimumSize(QSize(0, 26))
        self.cbLegendTrace.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_6.addWidget(self.cbLegendTrace)

        self.lblStyleTrace = QLabel(self.grpStyleTrace)
        self.lblStyleTrace.setObjectName(u"lblStyleTrace")
        sizePolicy2.setHeightForWidth(self.lblStyleTrace.sizePolicy().hasHeightForWidth())
        self.lblStyleTrace.setSizePolicy(sizePolicy2)
        self.lblStyleTrace.setMinimumSize(QSize(111, 26))
        self.lblStyleTrace.setMaximumSize(QSize(111, 26))

        self.verticalLayout_6.addWidget(self.lblStyleTrace)

        self.cbStyleTrace = QComboBox(self.grpStyleTrace)
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.addItem("")
        self.cbStyleTrace.setObjectName(u"cbStyleTrace")
        sizePolicy5.setHeightForWidth(self.cbStyleTrace.sizePolicy().hasHeightForWidth())
        self.cbStyleTrace.setSizePolicy(sizePolicy5)
        self.cbStyleTrace.setMinimumSize(QSize(0, 26))
        self.cbStyleTrace.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_6.addWidget(self.cbStyleTrace)


        self.horizontalLayout_8.addWidget(self.grpStyleTrace)

        self.stackedViewModeOptions.addWidget(self.pageTracesOptions)

        self.verticalLayout_11.addWidget(self.stackedViewModeOptions)

        self.tabMain.addTab(self.pageDataExplorer, "")
        self.pageSvd = QWidget()
        self.pageSvd.setObjectName(u"pageSvd")
        self.verticalLayout_7 = QVBoxLayout(self.pageSvd)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.svdMplWidget = MplWidget(self.pageSvd)
        self.svdMplWidget.setObjectName(u"svdMplWidget")
        sizePolicy.setHeightForWidth(self.svdMplWidget.sizePolicy().hasHeightForWidth())
        self.svdMplWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.svdMplWidget)

        self.grpSvdSettings = QGroupBox(self.pageSvd)
        self.grpSvdSettings.setObjectName(u"grpSvdSettings")
        sizePolicy1.setHeightForWidth(self.grpSvdSettings.sizePolicy().hasHeightForWidth())
        self.grpSvdSettings.setSizePolicy(sizePolicy1)
        self.grpSvdSettings.setMinimumSize(QSize(0, 61))
        self.grpSvdSettings.setMaximumSize(QSize(16777215, 61))
        self.horizontalLayout_9 = QHBoxLayout(self.grpSvdSettings)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.lblSvdCalcComps = QLabel(self.grpSvdSettings)
        self.lblSvdCalcComps.setObjectName(u"lblSvdCalcComps")
        sizePolicy2.setHeightForWidth(self.lblSvdCalcComps.sizePolicy().hasHeightForWidth())
        self.lblSvdCalcComps.setSizePolicy(sizePolicy2)
        self.lblSvdCalcComps.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_9.addWidget(self.lblSvdCalcComps)

        self.sbSvdCalcComps = QSpinBox(self.grpSvdSettings)
        self.sbSvdCalcComps.setObjectName(u"sbSvdCalcComps")
        self.sbSvdCalcComps.setEnabled(False)
        self.sbSvdCalcComps.setMinimumSize(QSize(0, 26))
        self.sbSvdCalcComps.setMaximumSize(QSize(16777215, 26))
        self.sbSvdCalcComps.setMinimum(2)
        self.sbSvdCalcComps.setMaximum(50)
        self.sbSvdCalcComps.setValue(15)

        self.horizontalLayout_9.addWidget(self.sbSvdCalcComps)

        self.line = QFrame(self.grpSvdSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.lblSvdShowComps = QLabel(self.grpSvdSettings)
        self.lblSvdShowComps.setObjectName(u"lblSvdShowComps")
        sizePolicy2.setHeightForWidth(self.lblSvdShowComps.sizePolicy().hasHeightForWidth())
        self.lblSvdShowComps.setSizePolicy(sizePolicy2)
        self.lblSvdShowComps.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_9.addWidget(self.lblSvdShowComps)

        self.sldSvdShowComps = QSlider(self.grpSvdSettings)
        self.sldSvdShowComps.setObjectName(u"sldSvdShowComps")
        self.sldSvdShowComps.setEnabled(False)
        self.sldSvdShowComps.setMinimumSize(QSize(0, 26))
        self.sldSvdShowComps.setMaximumSize(QSize(16777215, 26))
        self.sldSvdShowComps.setMinimum(1)
        self.sldSvdShowComps.setMaximum(10)
        self.sldSvdShowComps.setPageStep(1)
        self.sldSvdShowComps.setValue(3)
        self.sldSvdShowComps.setOrientation(Qt.Orientation.Horizontal)
        self.sldSvdShowComps.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sldSvdShowComps.setTickInterval(1)

        self.horizontalLayout_9.addWidget(self.sldSvdShowComps)

        self.sbSvdShowComps = QSpinBox(self.grpSvdSettings)
        self.sbSvdShowComps.setObjectName(u"sbSvdShowComps")
        self.sbSvdShowComps.setEnabled(False)
        self.sbSvdShowComps.setMinimumSize(QSize(0, 26))
        self.sbSvdShowComps.setMaximumSize(QSize(16777215, 26))
        self.sbSvdShowComps.setMinimum(1)
        self.sbSvdShowComps.setMaximum(10)
        self.sbSvdShowComps.setValue(3)

        self.horizontalLayout_9.addWidget(self.sbSvdShowComps)

        self.line_2 = QFrame(self.grpSvdSettings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_2)

        self.chkSvdLogScale = QCheckBox(self.grpSvdSettings)
        self.chkSvdLogScale.setObjectName(u"chkSvdLogScale")
        self.chkSvdLogScale.setEnabled(False)
        self.chkSvdLogScale.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_9.addWidget(self.chkSvdLogScale)


        self.verticalLayout_7.addWidget(self.grpSvdSettings)

        self.tabMain.addTab(self.pageSvd, "")
        self.pageFitting = QWidget()
        self.pageFitting.setObjectName(u"pageFitting")
        self.verticalLayout_9 = QVBoxLayout(self.pageFitting)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.grpFittingType = QGroupBox(self.pageFitting)
        self.grpFittingType.setObjectName(u"grpFittingType")
        sizePolicy1.setHeightForWidth(self.grpFittingType.sizePolicy().hasHeightForWidth())
        self.grpFittingType.setSizePolicy(sizePolicy1)
        self.grpFittingType.setMinimumSize(QSize(0, 48))
        self.grpFittingType.setMaximumSize(QSize(16777215, 48))
        self.horizontalLayout_11 = QHBoxLayout(self.grpFittingType)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 9, -1, -1)
        self.lblFittingType = QLabel(self.grpFittingType)
        self.lblFittingType.setObjectName(u"lblFittingType")
        sizePolicy2.setHeightForWidth(self.lblFittingType.sizePolicy().hasHeightForWidth())
        self.lblFittingType.setSizePolicy(sizePolicy2)
        self.lblFittingType.setMinimumSize(QSize(0, 26))
        self.lblFittingType.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_11.addWidget(self.lblFittingType)

        self.cbFittingType = QComboBox(self.grpFittingType)
        self.cbFittingType.addItem("")
        self.cbFittingType.addItem("")
        self.cbFittingType.setObjectName(u"cbFittingType")
        self.cbFittingType.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.cbFittingType.sizePolicy().hasHeightForWidth())
        self.cbFittingType.setSizePolicy(sizePolicy5)
        self.cbFittingType.setMinimumSize(QSize(201, 26))
        self.cbFittingType.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_11.addWidget(self.cbFittingType)


        self.verticalLayout_9.addWidget(self.grpFittingType)

        self.fittingPreviewMplWidget = MplWidget(self.pageFitting)
        self.fittingPreviewMplWidget.setObjectName(u"fittingPreviewMplWidget")
        sizePolicy.setHeightForWidth(self.fittingPreviewMplWidget.sizePolicy().hasHeightForWidth())
        self.fittingPreviewMplWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.fittingPreviewMplWidget)

        self.hBoxLayoutFittingSettings = QHBoxLayout()
        self.hBoxLayoutFittingSettings.setObjectName(u"hBoxLayoutFittingSettings")
        self.grpFitDataSelection = QGroupBox(self.pageFitting)
        self.grpFitDataSelection.setObjectName(u"grpFitDataSelection")
        sizePolicy1.setHeightForWidth(self.grpFitDataSelection.sizePolicy().hasHeightForWidth())
        self.grpFitDataSelection.setSizePolicy(sizePolicy1)
        self.grpFitDataSelection.setMinimumSize(QSize(0, 221))
        self.grpFitDataSelection.setMaximumSize(QSize(16777215, 221))
        self.verticalLayout_8 = QVBoxLayout(self.grpFitDataSelection)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 9)
        self.stackedFitDataSelection = QStackedWidget(self.grpFitDataSelection)
        self.stackedFitDataSelection.setObjectName(u"stackedFitDataSelection")
        sizePolicy3.setHeightForWidth(self.stackedFitDataSelection.sizePolicy().hasHeightForWidth())
        self.stackedFitDataSelection.setSizePolicy(sizePolicy3)
        self.stackedFitDataSelection.setMinimumSize(QSize(0, 0))
        self.pageGlobalFitSettings = QWidget()
        self.pageGlobalFitSettings.setObjectName(u"pageGlobalFitSettings")
        self.formLayout = QFormLayout(self.pageGlobalFitSettings)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.rbGlobalFitSvd = QRadioButton(self.pageGlobalFitSettings)
        self.rbGlobalFitSvd.setObjectName(u"rbGlobalFitSvd")
        self.rbGlobalFitSvd.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.rbGlobalFitSvd.sizePolicy().hasHeightForWidth())
        self.rbGlobalFitSvd.setSizePolicy(sizePolicy2)
        self.rbGlobalFitSvd.setMinimumSize(QSize(141, 26))
        self.rbGlobalFitSvd.setMaximumSize(QSize(141, 26))
        self.rbGlobalFitSvd.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.rbGlobalFitSvd)

        self.sbGlobalFitSvdComps = QSpinBox(self.pageGlobalFitSettings)
        self.sbGlobalFitSvdComps.setObjectName(u"sbGlobalFitSvdComps")
        self.sbGlobalFitSvdComps.setEnabled(False)
        self.sbGlobalFitSvdComps.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.sbGlobalFitSvdComps.setWrapping(False)
        self.sbGlobalFitSvdComps.setMinimum(1)
        self.sbGlobalFitSvdComps.setMaximum(20)
        self.sbGlobalFitSvdComps.setValue(3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sbGlobalFitSvdComps)

        self.rbGlobalFitRegion = QRadioButton(self.pageGlobalFitSettings)
        self.rbGlobalFitRegion.setObjectName(u"rbGlobalFitRegion")
        self.rbGlobalFitRegion.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.rbGlobalFitRegion.sizePolicy().hasHeightForWidth())
        self.rbGlobalFitRegion.setSizePolicy(sizePolicy2)
        self.rbGlobalFitRegion.setMinimumSize(QSize(141, 26))
        self.rbGlobalFitRegion.setMaximumSize(QSize(141, 26))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.rbGlobalFitRegion)

        self.hBoxLayoutRegion = QHBoxLayout()
        self.hBoxLayoutRegion.setSpacing(6)
        self.hBoxLayoutRegion.setObjectName(u"hBoxLayoutRegion")
        self.hBoxLayoutRegion.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.sbGlobalFitRegionMin = QSpinBox(self.pageGlobalFitSettings)
        self.sbGlobalFitRegionMin.setObjectName(u"sbGlobalFitRegionMin")
        self.sbGlobalFitRegionMin.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.sbGlobalFitRegionMin.sizePolicy().hasHeightForWidth())
        self.sbGlobalFitRegionMin.setSizePolicy(sizePolicy5)
        self.sbGlobalFitRegionMin.setMinimumSize(QSize(0, 26))
        self.sbGlobalFitRegionMin.setMaximumSize(QSize(16777215, 26))
        self.sbGlobalFitRegionMin.setMaximum(10000)

        self.hBoxLayoutRegion.addWidget(self.sbGlobalFitRegionMin)

        self.lbldash = QLabel(self.pageGlobalFitSettings)
        self.lbldash.setObjectName(u"lbldash")
        sizePolicy2.setHeightForWidth(self.lbldash.sizePolicy().hasHeightForWidth())
        self.lbldash.setSizePolicy(sizePolicy2)
        self.lbldash.setMinimumSize(QSize(0, 26))
        self.lbldash.setMaximumSize(QSize(6, 16777215))

        self.hBoxLayoutRegion.addWidget(self.lbldash)

        self.sbGlobalFitRegionMax = QSpinBox(self.pageGlobalFitSettings)
        self.sbGlobalFitRegionMax.setObjectName(u"sbGlobalFitRegionMax")
        self.sbGlobalFitRegionMax.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.sbGlobalFitRegionMax.sizePolicy().hasHeightForWidth())
        self.sbGlobalFitRegionMax.setSizePolicy(sizePolicy5)
        self.sbGlobalFitRegionMax.setMinimumSize(QSize(0, 26))
        self.sbGlobalFitRegionMax.setMaximumSize(QSize(16777215, 26))
        self.sbGlobalFitRegionMax.setMaximum(10000)

        self.hBoxLayoutRegion.addWidget(self.sbGlobalFitRegionMax)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.hBoxLayoutRegion)

        self.rbGlobalFitTraces = QRadioButton(self.pageGlobalFitSettings)
        self.rbGlobalFitTraces.setObjectName(u"rbGlobalFitTraces")
        self.rbGlobalFitTraces.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.rbGlobalFitTraces.sizePolicy().hasHeightForWidth())
        self.rbGlobalFitTraces.setSizePolicy(sizePolicy2)
        self.rbGlobalFitTraces.setMinimumSize(QSize(141, 26))
        self.rbGlobalFitTraces.setMaximumSize(QSize(141, 26))
        self.rbGlobalFitTraces.setChecked(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.rbGlobalFitTraces)

        self.leGlobalFitTraces = QLineEdit(self.pageGlobalFitSettings)
        self.leGlobalFitTraces.setObjectName(u"leGlobalFitTraces")
        self.leGlobalFitTraces.setEnabled(False)
        self.leGlobalFitTraces.setMinimumSize(QSize(0, 26))
        self.leGlobalFitTraces.setMaximumSize(QSize(16777215, 26))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.leGlobalFitTraces)

        self.lblGlobalFitAverage = QLabel(self.pageGlobalFitSettings)
        self.lblGlobalFitAverage.setObjectName(u"lblGlobalFitAverage")
        sizePolicy2.setHeightForWidth(self.lblGlobalFitAverage.sizePolicy().hasHeightForWidth())
        self.lblGlobalFitAverage.setSizePolicy(sizePolicy2)
        self.lblGlobalFitAverage.setMinimumSize(QSize(141, 26))
        self.lblGlobalFitAverage.setMaximumSize(QSize(141, 26))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblGlobalFitAverage)

        self.sbGlobalFitAverage = QSpinBox(self.pageGlobalFitSettings)
        self.sbGlobalFitAverage.setObjectName(u"sbGlobalFitAverage")
        self.sbGlobalFitAverage.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.sbGlobalFitAverage)

        self.lblGlobalFitMasking = QLabel(self.pageGlobalFitSettings)
        self.lblGlobalFitMasking.setObjectName(u"lblGlobalFitMasking")
        sizePolicy2.setHeightForWidth(self.lblGlobalFitMasking.sizePolicy().hasHeightForWidth())
        self.lblGlobalFitMasking.setSizePolicy(sizePolicy2)
        self.lblGlobalFitMasking.setMinimumSize(QSize(141, 26))
        self.lblGlobalFitMasking.setMaximumSize(QSize(141, 26))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblGlobalFitMasking)

        self.leGlobalFitMasking = QLineEdit(self.pageGlobalFitSettings)
        self.leGlobalFitMasking.setObjectName(u"leGlobalFitMasking")
        self.leGlobalFitMasking.setEnabled(False)
        self.leGlobalFitMasking.setToolTipDuration(-1)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.leGlobalFitMasking)

        self.stackedFitDataSelection.addWidget(self.pageGlobalFitSettings)
        self.pageSingleFitSettings = QWidget()
        self.pageSingleFitSettings.setObjectName(u"pageSingleFitSettings")
        self.formLayout_2 = QFormLayout(self.pageSingleFitSettings)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblSingleFitWave = QLabel(self.pageSingleFitSettings)
        self.lblSingleFitWave.setObjectName(u"lblSingleFitWave")
        self.lblSingleFitWave.setMinimumSize(QSize(0, 26))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblSingleFitWave)

        self.sbSingleFitWave = QSpinBox(self.pageSingleFitSettings)
        self.sbSingleFitWave.setObjectName(u"sbSingleFitWave")
        self.sbSingleFitWave.setMaximum(10000)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sbSingleFitWave)

        self.lblSingleFitAverage = QLabel(self.pageSingleFitSettings)
        self.lblSingleFitAverage.setObjectName(u"lblSingleFitAverage")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblSingleFitAverage)

        self.sbSingleFitAverage = QSpinBox(self.pageSingleFitSettings)
        self.sbSingleFitAverage.setObjectName(u"sbSingleFitAverage")
        self.sbSingleFitAverage.setMaximum(99)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sbSingleFitAverage)

        self.stackedFitDataSelection.addWidget(self.pageSingleFitSettings)

        self.verticalLayout_8.addWidget(self.stackedFitDataSelection)


        self.hBoxLayoutFittingSettings.addWidget(self.grpFitDataSelection)

        self.grpFitInitialParam = QGroupBox(self.pageFitting)
        self.grpFitInitialParam.setObjectName(u"grpFitInitialParam")
        sizePolicy1.setHeightForWidth(self.grpFitInitialParam.sizePolicy().hasHeightForWidth())
        self.grpFitInitialParam.setSizePolicy(sizePolicy1)
        self.grpFitInitialParam.setMinimumSize(QSize(0, 221))
        self.grpFitInitialParam.setMaximumSize(QSize(16777215, 221))
        self.formLayout_3 = QFormLayout(self.grpFitInitialParam)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(9, 0, 9, 0)
        self.lblExpNo = QLabel(self.grpFitInitialParam)
        self.lblExpNo.setObjectName(u"lblExpNo")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblExpNo)

        self.sbExpNo = QSpinBox(self.grpFitInitialParam)
        self.sbExpNo.setObjectName(u"sbExpNo")
        self.sbExpNo.setEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sbExpNo)

        self.lblIRFw = QLabel(self.grpFitInitialParam)
        self.lblIRFw.setObjectName(u"lblIRFw")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblIRFw)

        self.dsbIRFw = QDoubleSpinBox(self.grpFitInitialParam)
        self.dsbIRFw.setObjectName(u"dsbIRFw")
        self.dsbIRFw.setEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dsbIRFw)

        self.lblIRFmu = QLabel(self.grpFitInitialParam)
        self.lblIRFmu.setObjectName(u"lblIRFmu")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblIRFmu)

        self.dsbIRFmu = QDoubleSpinBox(self.grpFitInitialParam)
        self.dsbIRFmu.setObjectName(u"dsbIRFmu")
        self.dsbIRFmu.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dsbIRFmu)

        self.lblInitialTau = QLabel(self.grpFitInitialParam)
        self.lblInitialTau.setObjectName(u"lblInitialTau")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblInitialTau)

        self.leInitialTau = QLineEdit(self.grpFitInitialParam)
        self.leInitialTau.setObjectName(u"leInitialTau")
        self.leInitialTau.setEnabled(False)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.leInitialTau)

        self.chkTauInf = QCheckBox(self.grpFitInitialParam)
        self.chkTauInf.setObjectName(u"chkTauInf")
        self.chkTauInf.setEnabled(False)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.chkTauInf)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.btnRunFit = QPushButton(self.grpFitInitialParam)
        self.btnRunFit.setObjectName(u"btnRunFit")
        self.btnRunFit.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.btnRunFit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.formLayout_3.setLayout(5, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_3.setItem(4, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer_7)


        self.hBoxLayoutFittingSettings.addWidget(self.grpFitInitialParam)

        self.grpFittingProgress = QGroupBox(self.pageFitting)
        self.grpFittingProgress.setObjectName(u"grpFittingProgress")
        sizePolicy1.setHeightForWidth(self.grpFittingProgress.sizePolicy().hasHeightForWidth())
        self.grpFittingProgress.setSizePolicy(sizePolicy1)
        self.grpFittingProgress.setMinimumSize(QSize(0, 221))
        self.grpFittingProgress.setMaximumSize(QSize(16777215, 221))
        self.verticalLayout_10 = QVBoxLayout(self.grpFittingProgress)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 0, 2, 2)
        self.textFitLog = QTextBrowser(self.grpFittingProgress)
        self.textFitLog.setObjectName(u"textFitLog")
        sizePolicy3.setHeightForWidth(self.textFitLog.sizePolicy().hasHeightForWidth())
        self.textFitLog.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        self.textFitLog.setFont(font1)

        self.verticalLayout_10.addWidget(self.textFitLog)


        self.hBoxLayoutFittingSettings.addWidget(self.grpFittingProgress)

        self.hBoxLayoutFittingSettings.setStretch(0, 1)
        self.hBoxLayoutFittingSettings.setStretch(1, 1)
        self.hBoxLayoutFittingSettings.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.hBoxLayoutFittingSettings)

        self.tabMain.addTab(self.pageFitting, "")

        self.horizontalLayout.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1276, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.dockExperiments = QDockWidget(MainWindow)
        self.dockExperiments.setObjectName(u"dockExperiments")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dockExperiments.sizePolicy().hasHeightForWidth())
        self.dockExperiments.setSizePolicy(sizePolicy6)
        self.dockExperiments.setMinimumSize(QSize(100, 100))
        self.dockExperiments.setBaseSize(QSize(300, 767))
        self.dockExperiments.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockExperiments.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockExperiments.setDockLocation(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.dockExperimentsContents = QWidget()
        self.dockExperimentsContents.setObjectName(u"dockExperimentsContents")
        sizePolicy6.setHeightForWidth(self.dockExperimentsContents.sizePolicy().hasHeightForWidth())
        self.dockExperimentsContents.setSizePolicy(sizePolicy6)
        self.dockExperimentsContents.setBaseSize(QSize(300, 742))
        self.verticalLayout = QVBoxLayout(self.dockExperimentsContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.treeExperiment = QTreeWidget(self.dockExperimentsContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeExperiment.setHeaderItem(__qtreewidgetitem)
        self.treeExperiment.setObjectName(u"treeExperiment")
        sizePolicy6.setHeightForWidth(self.treeExperiment.sizePolicy().hasHeightForWidth())
        self.treeExperiment.setSizePolicy(sizePolicy6)
        self.treeExperiment.setAlternatingRowColors(True)
        self.treeExperiment.setHeaderHidden(True)
        self.treeExperiment.setColumnCount(1)

        self.verticalLayout.addWidget(self.treeExperiment)

        self.dockExperiments.setWidget(self.dockExperimentsContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockExperiments)
        self.dockProperties = QDockWidget(MainWindow)
        self.dockProperties.setObjectName(u"dockProperties")
        sizePolicy6.setHeightForWidth(self.dockProperties.sizePolicy().hasHeightForWidth())
        self.dockProperties.setSizePolicy(sizePolicy6)
        self.dockProperties.setMinimumSize(QSize(200, 536))
        self.dockProperties.setBaseSize(QSize(300, 767))
        self.dockProperties.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockProperties.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockProperties.setDockLocation(Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockPropertiesContents = QWidget()
        self.dockPropertiesContents.setObjectName(u"dockPropertiesContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockPropertiesContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbxProperties = QToolBox(self.dockPropertiesContents)
        self.tbxProperties.setObjectName(u"tbxProperties")
        sizePolicy6.setHeightForWidth(self.tbxProperties.sizePolicy().hasHeightForWidth())
        self.tbxProperties.setSizePolicy(sizePolicy6)
        self.pageMetadata = QWidget()
        self.pageMetadata.setObjectName(u"pageMetadata")
        self.pageMetadata.setGeometry(QRect(0, 0, 200, 680))
        self.tbxProperties.addItem(self.pageMetadata, u"Metaadatok")

        self.verticalLayout_3.addWidget(self.tbxProperties)

        self.dockProperties.setWidget(self.dockPropertiesContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockProperties)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actImport)
        self.menuFile.addAction(self.actExport)

        self.retranslateUi(MainWindow)
        self.rbAutomaticSpectra.toggled.connect(self.sbNumberOfSpectra.setEnabled)
        self.rbAutomaticSpectra.toggled.connect(self.chkAtWavelengthSpectra.setEnabled)
        self.chkAtWavelengthSpectra.toggled.connect(self.dsbAtWavelengthSpectra.setEnabled)
        self.rbCustomSpectra.toggled.connect(self.leCustomTimesSpectral.setEnabled)
        self.chkTimeRangeSpectra.toggled.connect(self.dsbTimeRangeStartSpectra.setEnabled)
        self.chkTimeRangeSpectra.toggled.connect(self.dsbTimeRangeStopSpectra.setEnabled)
        self.chkMaskRangeSpectra.toggled.connect(self.dsbMaskRangeStartSpectra.setEnabled)
        self.chkMaskRangeSpectra.toggled.connect(self.dsbMaskRangeStopSpectra.setEnabled)
        self.rbCustomTrace.toggled.connect(self.leCustomWavelengthTrace.setEnabled)
        self.sldSvdShowComps.valueChanged.connect(self.sbSvdShowComps.setValue)
        self.sbSvdShowComps.valueChanged.connect(self.sldSvdShowComps.setValue)
        self.cbFittingType.currentIndexChanged.connect(self.stackedFitDataSelection.setCurrentIndex)
        self.leCustomWavelengthTrace.textChanged.connect(self.leGlobalFitTraces.setText)
        self.rbGlobalFitSvd.toggled.connect(self.sbGlobalFitSvdComps.setEnabled)
        self.rbGlobalFitRegion.toggled.connect(self.sbGlobalFitRegionMin.setEnabled)
        self.rbGlobalFitRegion.toggled.connect(self.sbGlobalFitRegionMax.setEnabled)
        self.rbGlobalFitTraces.toggled.connect(self.leGlobalFitTraces.setEnabled)
        self.rbGlobalFitTraces.toggled.connect(self.sbGlobalFitAverage.setEnabled)
        self.rbGlobalFitTraces.toggled.connect(self.leGlobalFitMasking.setEnabled)

        self.tabMain.setCurrentIndex(0)
        self.stackedViewModeOptions.setCurrentIndex(0)
        self.stackedFitDataSelection.setCurrentIndex(0)
        self.tbxProperties.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.grpViewAndExport.setTitle("")
        self.lblViewMode.setText(QCoreApplication.translate("MainWindow", u"N\u00e9zet:", None))
        self.cbViewMode.setItemText(0, QCoreApplication.translate("MainWindow", u"3D n\u00e9zet", None))
        self.cbViewMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Spektrum", None))
        self.cbViewMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Trace", None))

        self.btnExportPlot.setText(QCoreApplication.translate("MainWindow", u"Plot Export\u00e1l\u00e1sa", None))
        self.grp3DOptions.setTitle(QCoreApplication.translate("MainWindow", u"3D be\u00e1ll\u00edt\u00e1sok", None))
        self.lblColorMaps3D.setText(QCoreApplication.translate("MainWindow", u"Sz\u00ednpalett\u00e1k:", None))
        self.cbColormaps3D.setItemText(0, QCoreApplication.translate("MainWindow", u"Viridis", None))
        self.cbColormaps3D.setItemText(1, QCoreApplication.translate("MainWindow", u"Plasma", None))
        self.cbColormaps3D.setItemText(2, QCoreApplication.translate("MainWindow", u"Inferno", None))
        self.cbColormaps3D.setItemText(3, QCoreApplication.translate("MainWindow", u"Magma", None))
        self.cbColormaps3D.setItemText(4, QCoreApplication.translate("MainWindow", u"Cividis", None))

        self.lblViewStyle3D.setText(QCoreApplication.translate("MainWindow", u"N\u00e9zet st\u00edlus:", None))
        self.cbStyle3D.setItemText(0, QCoreApplication.translate("MainWindow", u"Fel\u00fclet", None))
        self.cbStyle3D.setItemText(1, QCoreApplication.translate("MainWindow", u"V\u00e1zlat", None))
        self.cbStyle3D.setItemText(2, QCoreApplication.translate("MainWindow", u"Kont\u00far", None))

        self.lblRenderQuality3D.setText(QCoreApplication.translate("MainWindow", u"Felbont\u00e1s:", None))
        self.lblResetView3D.setText(QCoreApplication.translate("MainWindow", u"Camera vissza\u00e1ll\u00edt\u00e1sa", None))
        self.btnResetView3D.setText("")
        self.grpTimeSelectionSpectra.setTitle(QCoreApplication.translate("MainWindow", u"Id\u0151 szelekci\u00f3", None))
        self.rbAllSpectra.setText(QCoreApplication.translate("MainWindow", u"\u00d6sszes Spektrum", None))
        self.rbAutomaticSpectra.setText(QCoreApplication.translate("MainWindow", u"Automatikus", None))
        self.lblNumberOfSpectra.setText(QCoreApplication.translate("MainWindow", u"Spektrumok sz\u00e1ma:", None))
        self.chkAtWavelengthSpectra.setText(QCoreApplication.translate("MainWindow", u"Specifikus hull\u00e1mhossz", None))
        self.rbCustomSpectra.setText(QCoreApplication.translate("MainWindow", u"Egy\u00e9ni", None))
        self.leCustomTimesSpectral.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1, 5, 10.5, 100", None))
        self.grpProcessingAndRangesSpectra.setTitle(QCoreApplication.translate("MainWindow", u"Feldolgoz\u00e1s \u00e9s tartom\u00e1nyok", None))
        self.chkTimeRangeSpectra.setText(QCoreApplication.translate("MainWindow", u"Id\u0151intervallum korl\u00e1toz\u00e1sa", None))
        self.lblTimeRangeStartSpectra.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.lblTimeRangeStopSpectra.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.chkFromMaxToMinSpectra.setText(QCoreApplication.translate("MainWindow", u"Id\u0151tartom\u00e1ny a maxim\u00e1lis amplit\u00fad\u00f3t\u00f3l", None))
        self.lblAverageSpectra.setText(QCoreApplication.translate("MainWindow", u"\u00c1tlagoland\u00f3 pontok sz\u00e1ma", None))
        self.chkMaskRangeSpectra.setText(QCoreApplication.translate("MainWindow", u"Maszkol\u00e1si tartom\u00e1ny", None))
        self.lblMaskRangeStartSpectra.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.lblMaskRangeStopSpectra.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.grpStyleSpectra.setTitle(QCoreApplication.translate("MainWindow", u"Kin\u00e9zet", None))
        self.lblColormapsSpectra.setText(QCoreApplication.translate("MainWindow", u"Sz\u00ednpalett\u00e1k", None))
        self.cbColormapsSpectra.setItemText(0, QCoreApplication.translate("MainWindow", u"Viridis", None))
        self.cbColormapsSpectra.setItemText(1, QCoreApplication.translate("MainWindow", u"Plasma", None))
        self.cbColormapsSpectra.setItemText(2, QCoreApplication.translate("MainWindow", u"Inferno", None))
        self.cbColormapsSpectra.setItemText(3, QCoreApplication.translate("MainWindow", u"Magma", None))
        self.cbColormapsSpectra.setItemText(4, QCoreApplication.translate("MainWindow", u"Cividis", None))

        self.lblLegendSpectra.setText(QCoreApplication.translate("MainWindow", u"Jelmagyar\u00e1zat", None))
        self.cbLegendSpectra.setItemText(0, QCoreApplication.translate("MainWindow", u"Sz\u00f6veges c\u00edmke", None))
        self.cbLegendSpectra.setItemText(1, QCoreApplication.translate("MainWindow", u"Id\u0151 sz\u00ednsk\u00e1la", None))
        self.cbLegendSpectra.setItemText(2, QCoreApplication.translate("MainWindow", u"Rejtett", None))

        self.lblStyleSpectra.setText(QCoreApplication.translate("MainWindow", u"Megjelen\u00edt\u00e9si st\u00edlus", None))
        self.cbStyleSpectra.setItemText(0, QCoreApplication.translate("MainWindow", u"Ultrapyfit vil\u00e1gos", None))
        self.cbStyleSpectra.setItemText(1, QCoreApplication.translate("MainWindow", u"Ultrapyfit s\u00f6t\u00e9t", None))
        self.cbStyleSpectra.setItemText(2, QCoreApplication.translate("MainWindow", u"Alap\u00e9rtelmezett", None))
        self.cbStyleSpectra.setItemText(3, QCoreApplication.translate("MainWindow", u"Seaborn vil\u00e1gos r\u00e1cs", None))
        self.cbStyleSpectra.setItemText(4, QCoreApplication.translate("MainWindow", u"Seaborn s\u00f6t\u00e9t r\u00e1cs", None))
        self.cbStyleSpectra.setItemText(5, QCoreApplication.translate("MainWindow", u"S\u00f6t\u00e9t h\u00e1tt\u00e9r", None))
        self.cbStyleSpectra.setItemText(6, QCoreApplication.translate("MainWindow", u"ggplot", None))

        self.grpWavelengthSelectionTrace.setTitle(QCoreApplication.translate("MainWindow", u"Hull\u00e1mhossz Szelekci\u00f3", None))
        self.rbAllTrace.setText(QCoreApplication.translate("MainWindow", u"\u00d6sszes hull\u00e1m", None))
        self.rbAutomaticTrace.setText(QCoreApplication.translate("MainWindow", u"Automatikus", None))
        self.rbCustomTrace.setText(QCoreApplication.translate("MainWindow", u"Egy\u00e9ni", None))
        self.leCustomWavelengthTrace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450, 500, 620", None))
        self.grpStyleTrace.setTitle(QCoreApplication.translate("MainWindow", u"Kin\u00e9zet", None))
        self.lblLegendTrace.setText(QCoreApplication.translate("MainWindow", u"Jelmagyar\u00e1zat", None))
        self.cbLegendTrace.setItemText(0, QCoreApplication.translate("MainWindow", u"Automatikus", None))
        self.cbLegendTrace.setItemText(1, QCoreApplication.translate("MainWindow", u"Mindig l\u00e1that\u00f3", None))
        self.cbLegendTrace.setItemText(2, QCoreApplication.translate("MainWindow", u"Elrejtve", None))

        self.lblStyleTrace.setText(QCoreApplication.translate("MainWindow", u"Megjelen\u00edt\u00e9si st\u00edlus", None))
        self.cbStyleTrace.setItemText(0, QCoreApplication.translate("MainWindow", u"Ultrapyfit vil\u00e1gos", None))
        self.cbStyleTrace.setItemText(1, QCoreApplication.translate("MainWindow", u"Ultrapyfit s\u00f6t\u00e9t", None))
        self.cbStyleTrace.setItemText(2, QCoreApplication.translate("MainWindow", u"Alap\u00e9rtelmezett", None))
        self.cbStyleTrace.setItemText(3, QCoreApplication.translate("MainWindow", u"Seaborn vil\u00e1gos r\u00e1cs", None))
        self.cbStyleTrace.setItemText(4, QCoreApplication.translate("MainWindow", u"Seaborn s\u00f6t\u00e9t r\u00e1cs", None))
        self.cbStyleTrace.setItemText(5, QCoreApplication.translate("MainWindow", u"S\u00f6t\u00e9t h\u00e1tt\u00e9r", None))
        self.cbStyleTrace.setItemText(6, QCoreApplication.translate("MainWindow", u"ggplot", None))

        self.tabMain.setTabText(self.tabMain.indexOf(self.pageDataExplorer), QCoreApplication.translate("MainWindow", u"Adatfelfedez\u0151", None))
        self.grpSvdSettings.setTitle(QCoreApplication.translate("MainWindow", u"SVD Be\u00e1ll\u00edt\u00e1sok", None))
        self.lblSvdCalcComps.setText(QCoreApplication.translate("MainWindow", u"Kisz\u00e1m\u00edtott komponensek:", None))
        self.lblSvdShowComps.setText(QCoreApplication.translate("MainWindow", u"Megjelen\u00edtett komponensek:", None))
        self.chkSvdLogScale.setText(QCoreApplication.translate("MainWindow", u"Logaritmikus sk\u00e1la", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pageSvd), QCoreApplication.translate("MainWindow", u"SVD", None))
        self.grpFittingType.setTitle("")
        self.lblFittingType.setText(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s t\u00edpusa:", None))
        self.cbFittingType.setItemText(0, QCoreApplication.translate("MainWindow", u"Glob\u00e1lis illeszt\u00e9s", None))
        self.cbFittingType.setItemText(1, QCoreApplication.translate("MainWindow", u"Egyetlen nyom illeszt\u00e9se", None))

#if QT_CONFIG(tooltip)
        self.cbFittingType.setToolTip(QCoreApplication.translate("MainWindow", u"V\u00e1lassza ki, hogy a teljes 2D adathalmazra (Glob\u00e1lis illeszt\u00e9s) vagy csak egyetlen kiv\u00e1lasztott kinetikai nyomra szeretne modellt illeszteni.", None))
#endif // QT_CONFIG(tooltip)
        self.grpFitDataSelection.setTitle(QCoreApplication.translate("MainWindow", u"Adatkiv\u00e1laszt\u00e1s", None))
#if QT_CONFIG(tooltip)
        self.rbGlobalFitSvd.setToolTip(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s a Szingul\u00e1ris \u00c9rt\u00e9k Felbont\u00e1s (SVD) kinetikai vektorai alapj\u00e1n. Ez a legink\u00e1bb aj\u00e1nlott m\u00f3dszer, mivel kiv\u00e1l\u00f3an sz\u0171ri a zajt.", None))
#endif // QT_CONFIG(tooltip)
        self.rbGlobalFitSvd.setText(QCoreApplication.translate("MainWindow", u"Svd Komponensek:", None))
#if QT_CONFIG(tooltip)
        self.sbGlobalFitSvdComps.setToolTip(QCoreApplication.translate("MainWindow", u"A glob\u00e1lis illeszt\u00e9shez haszn\u00e1lt SVD komponensek sz\u00e1ma (\u00e1ltal\u00e1ban 2-6 k\u00f6z\u00f6tti \u00e9rt\u00e9k).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rbGlobalFitRegion.setToolTip(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s egy megadott, egybef\u00fcgg\u0151 hull\u00e1mhossz-tartom\u00e1nyon bel\u00fcl.", None))
#endif // QT_CONFIG(tooltip)
        self.rbGlobalFitRegion.setText(QCoreApplication.translate("MainWindow", u"Tartom\u00e1ny (nm):", None))
#if QT_CONFIG(tooltip)
        self.sbGlobalFitRegionMin.setToolTip(QCoreApplication.translate("MainWindow", u"A vizsg\u00e1lni k\u00edv\u00e1nt tartom\u00e1ny kezd\u0151 \u00e9s v\u00e9gpontja (nm).", None))
#endif // QT_CONFIG(tooltip)
        self.lbldash.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.sbGlobalFitRegionMax.setToolTip(QCoreApplication.translate("MainWindow", u"A vizsg\u00e1lni k\u00edv\u00e1nt tartom\u00e1ny kezd\u0151 \u00e9s v\u00e9gpontja (nm).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rbGlobalFitTraces.setToolTip(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s specifikus, egyedi hull\u00e1mhosszak (nyomok) kiv\u00e1laszt\u00e1s\u00e1val.", None))
#endif // QT_CONFIG(tooltip)
        self.rbGlobalFitTraces.setText(QCoreApplication.translate("MainWindow", u"Nyomok (nm):", None))
#if QT_CONFIG(tooltip)
        self.leGlobalFitTraces.setToolTip(QCoreApplication.translate("MainWindow", u"Adja meg a vizsg\u00e1lni k\u00edv\u00e1nt hull\u00e1mhosszakat vessz\u0151vel elv\u00e1lasztva (pl. 450, 500, 550).", None))
#endif // QT_CONFIG(tooltip)
        self.leGlobalFitTraces.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450, 500, 550", None))
        self.lblGlobalFitAverage.setText(QCoreApplication.translate("MainWindow", u"\u00c1tlagol\u00e1s (pontok):", None))
#if QT_CONFIG(tooltip)
        self.sbGlobalFitAverage.setToolTip(QCoreApplication.translate("MainWindow", u"A kiv\u00e1lasztott hull\u00e1mhosszak k\u00f6r\u00fcli szomsz\u00e9dos pixelek \u00e1tlagol\u00e1sa a zaj cs\u00f6kkent\u00e9se \u00e9rdek\u00e9ben (1 = egy pixel balra \u00e9s jobbra).", None))
#endif // QT_CONFIG(tooltip)
        self.lblGlobalFitMasking.setText(QCoreApplication.translate("MainWindow", u"Kiz\u00e1rt Tartom\u00e1ny (nm):", None))
#if QT_CONFIG(tooltip)
        self.leGlobalFitMasking.setToolTip(QCoreApplication.translate("MainWindow", u"KIZ\u00c1RT TARTOM\u00c1NYOK: Adja meg az illeszt\u00e9sb\u0151l kihagyni k\u00edv\u00e1nt r\u00e9szeket k\u00f6t\u0151jellel \u00e9s vessz\u0151vel (pl. a l\u00e9zersz\u00f3r\u00e1s kisz\u0171r\u00e9s\u00e9re: 390-410, 790-810).", None))
#endif // QT_CONFIG(tooltip)
        self.leGlobalFitMasking.setPlaceholderText(QCoreApplication.translate("MainWindow", u"390-410, 790-810", None))
        self.lblSingleFitWave.setText(QCoreApplication.translate("MainWindow", u"Vizsg\u00e1lt hull\u00e1mhossz (nm):", None))
#if QT_CONFIG(tooltip)
        self.sbSingleFitWave.setToolTip(QCoreApplication.translate("MainWindow", u"Adja meg azt az egyetlen hull\u00e1mhosszt (nm), amelyre az exponenci\u00e1lis modellt illeszteni szeretn\u00e9.", None))
#endif // QT_CONFIG(tooltip)
        self.lblSingleFitAverage.setText(QCoreApplication.translate("MainWindow", u"\u00c1tlagol\u00e1s (pontok):", None))
        self.grpFitInitialParam.setTitle(QCoreApplication.translate("MainWindow", u"Be\u00e1ll\u00edt\u00e1sok \u00e9s Futtat\u00e1s", None))
        self.lblExpNo.setText(QCoreApplication.translate("MainWindow", u"Exponenci\u00e1lisok sz\u00e1ma:", None))
#if QT_CONFIG(tooltip)
        self.sbExpNo.setToolTip(QCoreApplication.translate("MainWindow", u"A modellben szerepl\u0151 exponenci\u00e1lis boml\u00e1sok (tau) sz\u00e1ma (\u00e1ltal\u00e1ban 1 \u00e9s 4 k\u00f6z\u00f6tt).", None))
#endif // QT_CONFIG(tooltip)
        self.lblIRFw.setText(QCoreApplication.translate("MainWindow", u"IRF sz\u00e9less\u00e9g (w):", None))
#if QT_CONFIG(tooltip)
        self.dsbIRFw.setToolTip(QCoreApplication.translate("MainWindow", u"A m\u0171szer v\u00e1laszf\u00fcggv\u00e9ny\u00e9nek (IRF) kezdeti sz\u00e9less\u00e9g-becsl\u00e9se (FWHM).", None))
#endif // QT_CONFIG(tooltip)
        self.lblIRFmu.setText(QCoreApplication.translate("MainWindow", u"Id\u0151 nulla (mu):", None))
#if QT_CONFIG(tooltip)
        self.dsbIRFmu.setToolTip(QCoreApplication.translate("MainWindow", u"A nulla id\u0151pont (t0) kezdeti becsl\u00e9se.", None))
#endif // QT_CONFIG(tooltip)
        self.lblInitialTau.setText(QCoreApplication.translate("MainWindow", u"Kezdeti tau (ps):", None))
#if QT_CONFIG(tooltip)
        self.leInitialTau.setToolTip(QCoreApplication.translate("MainWindow", u"OPCION\u00c1LIS: Adja meg a kezdeti \u00e9lettartam (tau) becsl\u00e9seket pikoszekundumban, vessz\u0151vel elv\u00e1lasztva (pl. 1.5, 10, 200). Ha \u00fcresen hagyja, a program automatikusan gener\u00e1l becsl\u00e9st.", None))
#endif // QT_CONFIG(tooltip)
        self.leInitialTau.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcion\u00e1lis (1.5, 15, 200)", None))
#if QT_CONFIG(tooltip)
        self.chkTauInf.setToolTip(QCoreApplication.translate("MainWindow", u"Adjon a modellhez egy v\u00e9gtelen \u00e9lettartam\u00fa (nem boml\u00f3) komponenst az id\u0151ablakot meghalad\u00f3, hossz\u00fa t\u00e1v\u00fa h\u00e1tt\u00e9rjelek le\u00edr\u00e1s\u00e1ra.", None))
#endif // QT_CONFIG(tooltip)
        self.chkTauInf.setText(QCoreApplication.translate("MainWindow", u"V\u00e9gtelen komponens", None))
#if QT_CONFIG(tooltip)
        self.btnRunFit.setToolTip(QCoreApplication.translate("MainWindow", u"Ind\u00edtsa el az illeszt\u00e9si algoritmust a megadott param\u00e9terekkel. A folyamat befejezt\u00e9vel az eredm\u00e9ny megjelenik a bal oldali f\u00e1ban.", None))
#endif // QT_CONFIG(tooltip)
        self.btnRunFit.setText(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s Futtat\u00e1sa", None))
        self.grpFittingProgress.setTitle(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s folyamata", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pageFitting), QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s be\u00e1ll\u00edt\u00e1sa", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"F\u00e1jlok", None))
        self.dockExperiments.setWindowTitle(QCoreApplication.translate("MainWindow", u"K\u00eds\u00e9rletek", None))
        self.dockProperties.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tuljadons\u00e1gok", None))
        self.tbxProperties.setItemText(self.tbxProperties.indexOf(self.pageMetadata), QCoreApplication.translate("MainWindow", u"Metaadatok", None))
    # retranslateUi

