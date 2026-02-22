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
    QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QToolBox, QToolButton, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from ultrapyfit.gui.widgets.mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
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
        self.gridLayout = QGridLayout(self.pageDataExplorer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbViewMode = QComboBox(self.pageDataExplorer)
        self.cbViewMode.addItem("")
        self.cbViewMode.addItem("")
        self.cbViewMode.addItem("")
        self.cbViewMode.setObjectName(u"cbViewMode")
        self.cbViewMode.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.cbViewMode, 1, 1, 1, 1)

        self.lblViewMode = QLabel(self.pageDataExplorer)
        self.lblViewMode.setObjectName(u"lblViewMode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblViewMode.sizePolicy().hasHeightForWidth())
        self.lblViewMode.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lblViewMode, 1, 0, 1, 1)

        self.mplWidget = MplWidget(self.pageDataExplorer)
        self.mplWidget.setObjectName(u"mplWidget")
        sizePolicy.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mplWidget, 2, 0, 1, 3)

        self.stackedViewModeOptions = QStackedWidget(self.pageDataExplorer)
        self.stackedViewModeOptions.setObjectName(u"stackedViewModeOptions")
        self.stackedViewModeOptions.setMaximumSize(QSize(16777215, 51))
        self.page3DOptions = QWidget()
        self.page3DOptions.setObjectName(u"page3DOptions")
        self.horizontalLayout_2 = QHBoxLayout(self.page3DOptions)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblColorMaps3D = QLabel(self.page3DOptions)
        self.lblColorMaps3D.setObjectName(u"lblColorMaps3D")
        sizePolicy1.setHeightForWidth(self.lblColorMaps3D.sizePolicy().hasHeightForWidth())
        self.lblColorMaps3D.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lblColorMaps3D)

        self.cbColormaps3D = QComboBox(self.page3DOptions)
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.addItem("")
        self.cbColormaps3D.setObjectName(u"cbColormaps3D")
        sizePolicy1.setHeightForWidth(self.cbColormaps3D.sizePolicy().hasHeightForWidth())
        self.cbColormaps3D.setSizePolicy(sizePolicy1)
        self.cbColormaps3D.setMinimumSize(QSize(121, 28))
        self.cbColormaps3D.setMaximumSize(QSize(121, 28))

        self.horizontalLayout_2.addWidget(self.cbColormaps3D)

        self.lblViewStyle3D = QLabel(self.page3DOptions)
        self.lblViewStyle3D.setObjectName(u"lblViewStyle3D")
        sizePolicy1.setHeightForWidth(self.lblViewStyle3D.sizePolicy().hasHeightForWidth())
        self.lblViewStyle3D.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lblViewStyle3D)

        self.cbStyle3D = QComboBox(self.page3DOptions)
        self.cbStyle3D.addItem("")
        self.cbStyle3D.addItem("")
        self.cbStyle3D.addItem("")
        self.cbStyle3D.setObjectName(u"cbStyle3D")
        sizePolicy1.setHeightForWidth(self.cbStyle3D.sizePolicy().hasHeightForWidth())
        self.cbStyle3D.setSizePolicy(sizePolicy1)
        self.cbStyle3D.setMinimumSize(QSize(121, 28))
        self.cbStyle3D.setMaximumSize(QSize(121, 28))

        self.horizontalLayout_2.addWidget(self.cbStyle3D)

        self.lblRenderQuality3D = QLabel(self.page3DOptions)
        self.lblRenderQuality3D.setObjectName(u"lblRenderQuality3D")
        sizePolicy1.setHeightForWidth(self.lblRenderQuality3D.sizePolicy().hasHeightForWidth())
        self.lblRenderQuality3D.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lblRenderQuality3D)

        self.sbRenderQuality3D = QSpinBox(self.page3DOptions)
        self.sbRenderQuality3D.setObjectName(u"sbRenderQuality3D")
        sizePolicy1.setHeightForWidth(self.sbRenderQuality3D.sizePolicy().hasHeightForWidth())
        self.sbRenderQuality3D.setSizePolicy(sizePolicy1)
        self.sbRenderQuality3D.setMinimumSize(QSize(91, 28))
        self.sbRenderQuality3D.setMaximumSize(QSize(121, 28))
        self.sbRenderQuality3D.setMinimum(1)
        self.sbRenderQuality3D.setMaximum(10)

        self.horizontalLayout_2.addWidget(self.sbRenderQuality3D)

        self.lblResetView3D = QLabel(self.page3DOptions)
        self.lblResetView3D.setObjectName(u"lblResetView3D")
        sizePolicy1.setHeightForWidth(self.lblResetView3D.sizePolicy().hasHeightForWidth())
        self.lblResetView3D.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lblResetView3D)

        self.btnResetView3D = QToolButton(self.page3DOptions)
        self.btnResetView3D.setObjectName(u"btnResetView3D")
        self.btnResetView3D.setMinimumSize(QSize(28, 28))
        self.btnResetView3D.setMaximumSize(QSize(28, 28))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRestore))
        self.btnResetView3D.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btnResetView3D)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.grpTimeSelectionSpectra.sizePolicy().hasHeightForWidth())
        self.grpTimeSelectionSpectra.setSizePolicy(sizePolicy2)
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
        sizePolicy1.setHeightForWidth(self.lblNumberOfSpectra.sizePolicy().hasHeightForWidth())
        self.lblNumberOfSpectra.setSizePolicy(sizePolicy1)
        self.lblNumberOfSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.lblNumberOfSpectra, 2, 0, 1, 1)

        self.sbNumberOfSpectra = QSpinBox(self.grpTimeSelectionSpectra)
        self.sbNumberOfSpectra.setObjectName(u"sbNumberOfSpectra")
        self.sbNumberOfSpectra.setMinimumSize(QSize(0, 26))
        self.sbNumberOfSpectra.setMaximum(1024)
        self.sbNumberOfSpectra.setValue(8)

        self.gridLayout_4.addWidget(self.sbNumberOfSpectra, 2, 1, 1, 1)

        self.chkAtWavelengthSpectra = QCheckBox(self.grpTimeSelectionSpectra)
        self.chkAtWavelengthSpectra.setObjectName(u"chkAtWavelengthSpectra")
        sizePolicy1.setHeightForWidth(self.chkAtWavelengthSpectra.sizePolicy().hasHeightForWidth())
        self.chkAtWavelengthSpectra.setSizePolicy(sizePolicy1)
        self.chkAtWavelengthSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.chkAtWavelengthSpectra, 3, 0, 1, 1)

        self.dsbAtWavelengthSpectra = QDoubleSpinBox(self.grpTimeSelectionSpectra)
        self.dsbAtWavelengthSpectra.setObjectName(u"dsbAtWavelengthSpectra")
        self.dsbAtWavelengthSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.dsbAtWavelengthSpectra, 3, 1, 1, 1)

        self.rbCustomSpectra = QRadioButton(self.grpTimeSelectionSpectra)
        self.rbCustomSpectra.setObjectName(u"rbCustomSpectra")
        self.rbCustomSpectra.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.rbCustomSpectra, 4, 0, 1, 1)

        self.leCustomTimes = QLineEdit(self.grpTimeSelectionSpectra)
        self.leCustomTimes.setObjectName(u"leCustomTimes")
        self.leCustomTimes.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.leCustomTimes, 5, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.grpTimeSelectionSpectra)

        self.grpProcessingAndRangesSpectra = QGroupBox(self.pageSpectraOptions)
        self.grpProcessingAndRangesSpectra.setObjectName(u"grpProcessingAndRangesSpectra")
        sizePolicy2.setHeightForWidth(self.grpProcessingAndRangesSpectra.sizePolicy().hasHeightForWidth())
        self.grpProcessingAndRangesSpectra.setSizePolicy(sizePolicy2)
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
        self.lblTimeRangeStartSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.lblTimeRangeStartSpectra)

        self.dsbTimeRangeStartSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbTimeRangeStartSpectra.setObjectName(u"dsbTimeRangeStartSpectra")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dsbTimeRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.dsbTimeRangeStartSpectra.setSizePolicy(sizePolicy3)
        self.dsbTimeRangeStartSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.dsbTimeRangeStartSpectra)

        self.lblTimeRangeStopSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblTimeRangeStopSpectra.setObjectName(u"lblTimeRangeStopSpectra")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lblTimeRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.lblTimeRangeStopSpectra.setSizePolicy(sizePolicy4)
        self.lblTimeRangeStopSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_5.addWidget(self.lblTimeRangeStopSpectra)

        self.dsbTimeRangeStopSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbTimeRangeStopSpectra.setObjectName(u"dsbTimeRangeStopSpectra")
        sizePolicy3.setHeightForWidth(self.dsbTimeRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.dsbTimeRangeStopSpectra.setSizePolicy(sizePolicy3)
        self.dsbTimeRangeStopSpectra.setMinimumSize(QSize(0, 26))

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lblAverageSpectra.sizePolicy().hasHeightForWidth())
        self.lblAverageSpectra.setSizePolicy(sizePolicy5)
        self.lblAverageSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_7.addWidget(self.lblAverageSpectra)

        self.sbAverageSpectra = QSpinBox(self.grpProcessingAndRangesSpectra)
        self.sbAverageSpectra.setObjectName(u"sbAverageSpectra")
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
        self.lblMaskRangeStartSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.lblMaskRangeStartSpectra)

        self.dsbMaskRangeStartSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbMaskRangeStartSpectra.setObjectName(u"dsbMaskRangeStartSpectra")
        sizePolicy3.setHeightForWidth(self.dsbMaskRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.dsbMaskRangeStartSpectra.setSizePolicy(sizePolicy3)
        self.dsbMaskRangeStartSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.dsbMaskRangeStartSpectra)

        self.lblMaskRangeStopSpectra = QLabel(self.grpProcessingAndRangesSpectra)
        self.lblMaskRangeStopSpectra.setObjectName(u"lblMaskRangeStopSpectra")
        sizePolicy4.setHeightForWidth(self.lblMaskRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.lblMaskRangeStopSpectra.setSizePolicy(sizePolicy4)
        self.lblMaskRangeStopSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.lblMaskRangeStopSpectra)

        self.dsbMaskRangeStopSpectra = QDoubleSpinBox(self.grpProcessingAndRangesSpectra)
        self.dsbMaskRangeStopSpectra.setObjectName(u"dsbMaskRangeStopSpectra")
        sizePolicy3.setHeightForWidth(self.dsbMaskRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.dsbMaskRangeStopSpectra.setSizePolicy(sizePolicy3)
        self.dsbMaskRangeStopSpectra.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.dsbMaskRangeStopSpectra)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.grpProcessingAndRangesSpectra)

        self.grpStyleSpectra = QGroupBox(self.pageSpectraOptions)
        self.grpStyleSpectra.setObjectName(u"grpStyleSpectra")
        sizePolicy2.setHeightForWidth(self.grpStyleSpectra.sizePolicy().hasHeightForWidth())
        self.grpStyleSpectra.setSizePolicy(sizePolicy2)
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
        sizePolicy3.setHeightForWidth(self.cbColormapsSpectra.sizePolicy().hasHeightForWidth())
        self.cbColormapsSpectra.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.cbLegendSpectra.sizePolicy().hasHeightForWidth())
        self.cbLegendSpectra.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.cbStyleSpectra.sizePolicy().hasHeightForWidth())
        self.cbStyleSpectra.setSizePolicy(sizePolicy3)
        self.cbStyleSpectra.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.cbStyleSpectra)


        self.horizontalLayout_3.addWidget(self.grpStyleSpectra)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedViewModeOptions.addWidget(self.pageSpectraOptions)
        self.pageTracesOptions = QWidget()
        self.pageTracesOptions.setObjectName(u"pageTracesOptions")
        self.stackedViewModeOptions.addWidget(self.pageTracesOptions)

        self.gridLayout.addWidget(self.stackedViewModeOptions, 3, 0, 1, 3)

        self.tabMain.addTab(self.pageDataExplorer, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabMain.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
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
        self.dockProperties.setMinimumSize(QSize(200, 111))
        self.dockProperties.setBaseSize(QSize(300, 767))
        self.dockProperties.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockProperties.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockProperties.setDockLocation(Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockPropertiesContents = QWidget()
        self.dockPropertiesContents.setObjectName(u"dockPropertiesContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockPropertiesContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbxProperties = QToolBox(self.dockPropertiesContents)
        self.tbxProperties.setObjectName(u"tbxProperties")
        sizePolicy6.setHeightForWidth(self.tbxProperties.sizePolicy().hasHeightForWidth())
        self.tbxProperties.setSizePolicy(sizePolicy6)
        self.pageMetadata = QWidget()
        self.pageMetadata.setObjectName(u"pageMetadata")
        self.pageMetadata.setGeometry(QRect(0, 0, 200, 710))
        self.tbxProperties.addItem(self.pageMetadata, u"Metaadatok")

        self.verticalLayout_3.addWidget(self.tbxProperties)

        self.dockProperties.setWidget(self.dockPropertiesContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockProperties)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actImport)
        self.menuFile.addAction(self.actExport)

        self.retranslateUi(MainWindow)

        self.tabMain.setCurrentIndex(0)
        self.stackedViewModeOptions.setCurrentIndex(0)
        self.tbxProperties.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.cbViewMode.setItemText(0, QCoreApplication.translate("MainWindow", u"3D n\u00e9zet", None))
        self.cbViewMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Spektrum", None))
        self.cbViewMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Trace", None))

        self.lblViewMode.setText(QCoreApplication.translate("MainWindow", u"N\u00e9zet:", None))
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
        self.btnResetView3D.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.grpTimeSelectionSpectra.setTitle(QCoreApplication.translate("MainWindow", u"Id\u0151 szelekci\u00f3", None))
        self.rbAllSpectra.setText(QCoreApplication.translate("MainWindow", u"\u00d6sszes Spektrum", None))
        self.rbAutomaticSpectra.setText(QCoreApplication.translate("MainWindow", u"Automatikus", None))
        self.lblNumberOfSpectra.setText(QCoreApplication.translate("MainWindow", u"Spektrumok sz\u00e1ma:", None))
        self.chkAtWavelengthSpectra.setText(QCoreApplication.translate("MainWindow", u"Hull\u00e1mhossz t\u00e1vols\u00e1g", None))
        self.rbCustomSpectra.setText(QCoreApplication.translate("MainWindow", u"Egy\u00e9ni", None))
        self.leCustomTimes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1, 5, 10.5, 100", None))
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
        self.cbStyleSpectra.setItemText(5, QCoreApplication.translate("MainWindow", u"Seaborn vil\u00e1gos", None))
        self.cbStyleSpectra.setItemText(6, QCoreApplication.translate("MainWindow", u"ggplot", None))

        self.tabMain.setTabText(self.tabMain.indexOf(self.pageDataExplorer), QCoreApplication.translate("MainWindow", u"Adatfelfedez\u0151", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"F\u00e1jlok", None))
        self.dockExperiments.setWindowTitle(QCoreApplication.translate("MainWindow", u"K\u00eds\u00e9rletek", None))
        self.dockProperties.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tuljadons\u00e1gok", None))
        self.tbxProperties.setItemText(self.tbxProperties.indexOf(self.pageMetadata), QCoreApplication.translate("MainWindow", u"Metaadatok", None))
    # retranslateUi

