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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTabWidget, QToolBox,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

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
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.DataExplorerTab = QWidget()
        self.DataExplorerTab.setObjectName(u"DataExplorerTab")
        self.gridLayout = QGridLayout(self.DataExplorerTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ViewModeLabel = QLabel(self.DataExplorerTab)
        self.ViewModeLabel.setObjectName(u"ViewModeLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ViewModeLabel.sizePolicy().hasHeightForWidth())
        self.ViewModeLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.ViewModeLabel, 1, 0, 1, 1)

        self.ViewModeOptionsStackedWidget = QStackedWidget(self.DataExplorerTab)
        self.ViewModeOptionsStackedWidget.setObjectName(u"ViewModeOptionsStackedWidget")
        self.ViewModeOptionsStackedWidget.setMaximumSize(QSize(16777215, 120))
        self.View3DOptions = QWidget()
        self.View3DOptions.setObjectName(u"View3DOptions")
        self.RenderQuality3DLabel = QLabel(self.View3DOptions)
        self.RenderQuality3DLabel.setObjectName(u"RenderQuality3DLabel")
        self.RenderQuality3DLabel.setGeometry(QRect(10, 30, 59, 26))
        sizePolicy1.setHeightForWidth(self.RenderQuality3DLabel.sizePolicy().hasHeightForWidth())
        self.RenderQuality3DLabel.setSizePolicy(sizePolicy1)
        self.RenderQuality3DSpinBox = QSpinBox(self.View3DOptions)
        self.RenderQuality3DSpinBox.setObjectName(u"RenderQuality3DSpinBox")
        self.RenderQuality3DSpinBox.setGeometry(QRect(140, 30, 100, 26))
        self.RenderQuality3DSpinBox.setMaximumSize(QSize(100, 16777215))
        self.RenderQuality3DSpinBox.setMinimum(1)
        self.RenderQuality3DSpinBox.setMaximum(10)
        self.ViewStyle3DLabel = QLabel(self.View3DOptions)
        self.ViewStyle3DLabel.setObjectName(u"ViewStyle3DLabel")
        self.ViewStyle3DLabel.setGeometry(QRect(10, 60, 71, 26))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ViewStyle3DLabel.sizePolicy().hasHeightForWidth())
        self.ViewStyle3DLabel.setSizePolicy(sizePolicy2)
        self.ViewStyle3DComboBox = QComboBox(self.View3DOptions)
        self.ViewStyle3DComboBox.addItem("")
        self.ViewStyle3DComboBox.addItem("")
        self.ViewStyle3DComboBox.addItem("")
        self.ViewStyle3DComboBox.setObjectName(u"ViewStyle3DComboBox")
        self.ViewStyle3DComboBox.setGeometry(QRect(140, 60, 100, 26))
        self.ResetView3DLabel = QLabel(self.View3DOptions)
        self.ResetView3DLabel.setObjectName(u"ResetView3DLabel")
        self.ResetView3DLabel.setGeometry(QRect(10, 90, 121, 26))
        self.ResetView3DButton = QPushButton(self.View3DOptions)
        self.ResetView3DButton.setObjectName(u"ResetView3DButton")
        self.ResetView3DButton.setGeometry(QRect(140, 90, 101, 26))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRestore))
        self.ResetView3DButton.setIcon(icon)
        self.ResetView3DButton.setIconSize(QSize(16, 16))
        self.ColorMaps3DComboBox = QComboBox(self.View3DOptions)
        self.ColorMaps3DComboBox.addItem("")
        self.ColorMaps3DComboBox.addItem("")
        self.ColorMaps3DComboBox.addItem("")
        self.ColorMaps3DComboBox.addItem("")
        self.ColorMaps3DComboBox.addItem("")
        self.ColorMaps3DComboBox.setObjectName(u"ColorMaps3DComboBox")
        self.ColorMaps3DComboBox.setGeometry(QRect(140, 0, 101, 26))
        self.ColorMaps3DLabel = QLabel(self.View3DOptions)
        self.ColorMaps3DLabel.setObjectName(u"ColorMaps3DLabel")
        self.ColorMaps3DLabel.setGeometry(QRect(10, 0, 71, 26))
        self.ViewModeOptionsStackedWidget.addWidget(self.View3DOptions)
        self.ViewSpectraOptions = QWidget()
        self.ViewSpectraOptions.setObjectName(u"ViewSpectraOptions")
        self.ViewModeOptionsStackedWidget.addWidget(self.ViewSpectraOptions)
        self.ViewTracesOptions = QWidget()
        self.ViewTracesOptions.setObjectName(u"ViewTracesOptions")
        self.ViewModeOptionsStackedWidget.addWidget(self.ViewTracesOptions)

        self.gridLayout.addWidget(self.ViewModeOptionsStackedWidget, 3, 0, 1, 3)

        self.PlotWidget = MplWidget(self.DataExplorerTab)
        self.PlotWidget.setObjectName(u"PlotWidget")
        sizePolicy.setHeightForWidth(self.PlotWidget.sizePolicy().hasHeightForWidth())
        self.PlotWidget.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.PlotWidget, 2, 0, 1, 3)

        self.ViewModeComboBox = QComboBox(self.DataExplorerTab)
        self.ViewModeComboBox.addItem("")
        self.ViewModeComboBox.addItem("")
        self.ViewModeComboBox.addItem("")
        self.ViewModeComboBox.setObjectName(u"ViewModeComboBox")
        self.ViewModeComboBox.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.ViewModeComboBox, 1, 1, 1, 1)

        self.tabWidget.addTab(self.DataExplorerTab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        self.menuF_jlok = QMenu(self.menubar)
        self.menuF_jlok.setObjectName(u"menuF_jlok")
        MainWindow.setMenuBar(self.menubar)
        self.ExperimentsDockWidget = QDockWidget(MainWindow)
        self.ExperimentsDockWidget.setObjectName(u"ExperimentsDockWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ExperimentsDockWidget.sizePolicy().hasHeightForWidth())
        self.ExperimentsDockWidget.setSizePolicy(sizePolicy3)
        self.ExperimentsDockWidget.setMinimumSize(QSize(100, 100))
        self.ExperimentsDockWidget.setBaseSize(QSize(300, 767))
        self.ExperimentsDockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.ExperimentsDockWidget.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.ExperimentsDockWidget.setDockLocation(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.dockWidgetContents1 = QWidget()
        self.dockWidgetContents1.setObjectName(u"dockWidgetContents1")
        sizePolicy3.setHeightForWidth(self.dockWidgetContents1.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents1.setSizePolicy(sizePolicy3)
        self.dockWidgetContents1.setBaseSize(QSize(300, 742))
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ExperimentTreeWidget = QTreeWidget(self.dockWidgetContents1)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.ExperimentTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.ExperimentTreeWidget.setObjectName(u"ExperimentTreeWidget")
        sizePolicy3.setHeightForWidth(self.ExperimentTreeWidget.sizePolicy().hasHeightForWidth())
        self.ExperimentTreeWidget.setSizePolicy(sizePolicy3)
        self.ExperimentTreeWidget.setAlternatingRowColors(True)
        self.ExperimentTreeWidget.setHeaderHidden(True)
        self.ExperimentTreeWidget.setColumnCount(1)

        self.verticalLayout.addWidget(self.ExperimentTreeWidget)

        self.ExperimentsDockWidget.setWidget(self.dockWidgetContents1)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.ExperimentsDockWidget)
        self.PropertiesDockWidget = QDockWidget(MainWindow)
        self.PropertiesDockWidget.setObjectName(u"PropertiesDockWidget")
        sizePolicy3.setHeightForWidth(self.PropertiesDockWidget.sizePolicy().hasHeightForWidth())
        self.PropertiesDockWidget.setSizePolicy(sizePolicy3)
        self.PropertiesDockWidget.setMinimumSize(QSize(200, 100))
        self.PropertiesDockWidget.setBaseSize(QSize(300, 767))
        self.PropertiesDockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.PropertiesDockWidget.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.PropertiesDockWidget.setDockLocation(Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy3.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy3)
        self.Metadata = QWidget()
        self.Metadata.setObjectName(u"Metadata")
        self.Metadata.setGeometry(QRect(0, 0, 200, 710))
        self.toolBox.addItem(self.Metadata, u"Metaadatok")

        self.verticalLayout_3.addWidget(self.toolBox)

        self.PropertiesDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.PropertiesDockWidget)

        self.menubar.addAction(self.menuF_jlok.menuAction())
        self.menuF_jlok.addAction(self.actionImport)
        self.menuF_jlok.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.ViewModeOptionsStackedWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.ViewModeLabel.setText(QCoreApplication.translate("MainWindow", u"N\u00e9zet:", None))
        self.RenderQuality3DLabel.setText(QCoreApplication.translate("MainWindow", u"Felbont\u00e1s:", None))
        self.ViewStyle3DLabel.setText(QCoreApplication.translate("MainWindow", u"N\u00e9zet st\u00edlus:", None))
        self.ViewStyle3DComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Fel\u00fclet", None))
        self.ViewStyle3DComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"V\u00e1zlat", None))
        self.ViewStyle3DComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kont\u00far", None))

        self.ResetView3DLabel.setText(QCoreApplication.translate("MainWindow", u"Camera vissza\u00e1ll\u00edt\u00e1sa", None))
        self.ResetView3DButton.setText("")
        self.ColorMaps3DComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Viridis", None))
        self.ColorMaps3DComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Plasma", None))
        self.ColorMaps3DComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Inferno", None))
        self.ColorMaps3DComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Magma", None))
        self.ColorMaps3DComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Cividis", None))

        self.ColorMaps3DLabel.setText(QCoreApplication.translate("MainWindow", u"Sz\u00ednpalett\u00e1k:", None))
        self.ViewModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"3D n\u00e9zet", None))
        self.ViewModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Spektrum", None))
        self.ViewModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Trace", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataExplorerTab), QCoreApplication.translate("MainWindow", u"Adatfelfedez\u0151", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuF_jlok.setTitle(QCoreApplication.translate("MainWindow", u"F\u00e1jlok", None))
        self.ExperimentsDockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"K\u00eds\u00e9rletek", None))
        self.PropertiesDockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tuljadons\u00e1gok", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Metadata), QCoreApplication.translate("MainWindow", u"Metaadatok", None))
    # retranslateUi

