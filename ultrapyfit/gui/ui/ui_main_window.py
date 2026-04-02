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
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QSplitter, QStackedWidget, QStatusBar,
    QTabWidget, QTextBrowser, QToolButton, QTreeWidget,
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
        self.actSave = QAction(MainWindow)
        self.actSave.setObjectName(u"actSave")
        self.actLoad = QAction(MainWindow)
        self.actLoad.setObjectName(u"actLoad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_17 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.tabMain = QTabWidget(self.centralwidget)
        self.tabMain.setObjectName(u"tabMain")
        self.pagePreprocessing = QWidget()
        self.pagePreprocessing.setObjectName(u"pagePreprocessing")
        self.verticalLayout_21 = QVBoxLayout(self.pagePreprocessing)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.grpPreprocessingtool = QGroupBox(self.pagePreprocessing)
        self.grpPreprocessingtool.setObjectName(u"grpPreprocessingtool")
        self.horizontalLayout_17 = QHBoxLayout(self.grpPreprocessingtool)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lblPreprocessingTool = QLabel(self.grpPreprocessingtool)
        self.lblPreprocessingTool.setObjectName(u"lblPreprocessingTool")

        self.horizontalLayout_17.addWidget(self.lblPreprocessingTool)

        self.cbPreprocessingTool = QComboBox(self.grpPreprocessingtool)
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.addItem("")
        self.cbPreprocessingTool.setObjectName(u"cbPreprocessingTool")
        self.cbPreprocessingTool.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.cbPreprocessingTool)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)


        self.verticalLayout_21.addWidget(self.grpPreprocessingtool)

        self.preprocessingMplWidget = MplWidget(self.pagePreprocessing)
        self.preprocessingMplWidget.setObjectName(u"preprocessingMplWidget")
        sizePolicy.setHeightForWidth(self.preprocessingMplWidget.sizePolicy().hasHeightForWidth())
        self.preprocessingMplWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_21.addWidget(self.preprocessingMplWidget)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.grpPreprocessingSettings = QGroupBox(self.pagePreprocessing)
        self.grpPreprocessingSettings.setObjectName(u"grpPreprocessingSettings")
        self.verticalLayout_20 = QVBoxLayout(self.grpPreprocessingSettings)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.stackedPreprocessTools = QStackedWidget(self.grpPreprocessingSettings)
        self.stackedPreprocessTools.setObjectName(u"stackedPreprocessTools")
        self.pageCutTimeSettings = QWidget()
        self.pageCutTimeSettings.setObjectName(u"pageCutTimeSettings")
        self.formLayout_5 = QFormLayout(self.pageCutTimeSettings)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.lblCutTimeMin = QLabel(self.pageCutTimeSettings)
        self.lblCutTimeMin.setObjectName(u"lblCutTimeMin")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCutTimeMin)

        self.lblCutTimeMax = QLabel(self.pageCutTimeSettings)
        self.lblCutTimeMax.setObjectName(u"lblCutTimeMax")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCutTimeMax)

        self.leCutTimeMax = QLineEdit(self.pageCutTimeSettings)
        self.leCutTimeMax.setObjectName(u"leCutTimeMax")
        self.leCutTimeMax.setEnabled(False)

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leCutTimeMax)

        self.leCutTimeMin = QLineEdit(self.pageCutTimeSettings)
        self.leCutTimeMin.setObjectName(u"leCutTimeMin")
        self.leCutTimeMin.setEnabled(False)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leCutTimeMin)

        self.stackedPreprocessTools.addWidget(self.pageCutTimeSettings)
        self.pageCutWavelength = QWidget()
        self.pageCutWavelength.setObjectName(u"pageCutWavelength")
        self.formLayout_6 = QFormLayout(self.pageCutWavelength)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lblCutWaveMin = QLabel(self.pageCutWavelength)
        self.lblCutWaveMin.setObjectName(u"lblCutWaveMin")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCutWaveMin)

        self.lblCutWaveMax = QLabel(self.pageCutWavelength)
        self.lblCutWaveMax.setObjectName(u"lblCutWaveMax")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCutWaveMax)

        self.leCutWaveMin = QLineEdit(self.pageCutWavelength)
        self.leCutWaveMin.setObjectName(u"leCutWaveMin")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leCutWaveMin)

        self.leCutWaveMax = QLineEdit(self.pageCutWavelength)
        self.leCutWaveMax.setObjectName(u"leCutWaveMax")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leCutWaveMax)

        self.lblCutWaveInner = QLabel(self.pageCutWavelength)
        self.lblCutWaveInner.setObjectName(u"lblCutWaveInner")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCutWaveInner)

        self.cbCutWaveInner = QComboBox(self.pageCutWavelength)
        self.cbCutWaveInner.addItem("")
        self.cbCutWaveInner.addItem("")
        self.cbCutWaveInner.setObjectName(u"cbCutWaveInner")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cbCutWaveInner)

        self.stackedPreprocessTools.addWidget(self.pageCutWavelength)
        self.pageShiftTime = QWidget()
        self.pageShiftTime.setObjectName(u"pageShiftTime")
        self.horizontalLayout_21 = QHBoxLayout(self.pageShiftTime)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lblShiftTime = QLabel(self.pageShiftTime)
        self.lblShiftTime.setObjectName(u"lblShiftTime")

        self.horizontalLayout_21.addWidget(self.lblShiftTime)

        self.leShiftTime = QLineEdit(self.pageShiftTime)
        self.leShiftTime.setObjectName(u"leShiftTime")

        self.horizontalLayout_21.addWidget(self.leShiftTime)

        self.stackedPreprocessTools.addWidget(self.pageShiftTime)
        self.pageBaselineSubtraction = QWidget()
        self.pageBaselineSubtraction.setObjectName(u"pageBaselineSubtraction")
        self.formLayout_7 = QFormLayout(self.pageBaselineSubtraction)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.lblBaseSpec = QLabel(self.pageBaselineSubtraction)
        self.lblBaseSpec.setObjectName(u"lblBaseSpec")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblBaseSpec)

        self.chkBaseOnlyOne = QCheckBox(self.pageBaselineSubtraction)
        self.chkBaseOnlyOne.setObjectName(u"chkBaseOnlyOne")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.chkBaseOnlyOne)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_7.setItem(1, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer_12)

        self.leBaseSpec = QLineEdit(self.pageBaselineSubtraction)
        self.leBaseSpec.setObjectName(u"leBaseSpec")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leBaseSpec)

        self.stackedPreprocessTools.addWidget(self.pageBaselineSubtraction)
        self.pagePolynomialBaseline = QWidget()
        self.pagePolynomialBaseline.setObjectName(u"pagePolynomialBaseline")
        self.formLayout_8 = QFormLayout(self.pagePolynomialBaseline)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.lblPolyBasePoints = QLabel(self.pagePolynomialBaseline)
        self.lblPolyBasePoints.setObjectName(u"lblPolyBasePoints")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPolyBasePoints)

        self.lblPolyBaseOrder = QLabel(self.pagePolynomialBaseline)
        self.lblPolyBaseOrder.setObjectName(u"lblPolyBaseOrder")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPolyBaseOrder)

        self.lePolyBasePoints = QLineEdit(self.pagePolynomialBaseline)
        self.lePolyBasePoints.setObjectName(u"lePolyBasePoints")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lePolyBasePoints)

        self.sbPolyBaseOrder = QSpinBox(self.pagePolynomialBaseline)
        self.sbPolyBaseOrder.setObjectName(u"sbPolyBaseOrder")
        self.sbPolyBaseOrder.setValue(3)

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sbPolyBaseOrder)

        self.stackedPreprocessTools.addWidget(self.pagePolynomialBaseline)
        self.pageAverageTime = QWidget()
        self.pageAverageTime.setObjectName(u"pageAverageTime")
        self.gridLayout = QGridLayout(self.pageAverageTime)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblAvgTimeMethod = QLabel(self.pageAverageTime)
        self.lblAvgTimeMethod.setObjectName(u"lblAvgTimeMethod")

        self.gridLayout.addWidget(self.lblAvgTimeMethod, 1, 0, 1, 1)

        self.lblAvgTimeStart = QLabel(self.pageAverageTime)
        self.lblAvgTimeStart.setObjectName(u"lblAvgTimeStart")

        self.gridLayout.addWidget(self.lblAvgTimeStart, 0, 0, 1, 1)

        self.sbAvgTimeGrid = QSpinBox(self.pageAverageTime)
        self.sbAvgTimeGrid.setObjectName(u"sbAvgTimeGrid")
        self.sbAvgTimeGrid.setValue(5)

        self.gridLayout.addWidget(self.sbAvgTimeGrid, 1, 3, 1, 1)

        self.lblAvgTimeGrid = QLabel(self.pageAverageTime)
        self.lblAvgTimeGrid.setObjectName(u"lblAvgTimeGrid")

        self.gridLayout.addWidget(self.lblAvgTimeGrid, 1, 2, 1, 1)

        self.leAvgTimeStart = QLineEdit(self.pageAverageTime)
        self.leAvgTimeStart.setObjectName(u"leAvgTimeStart")

        self.gridLayout.addWidget(self.leAvgTimeStart, 0, 1, 1, 1)

        self.lblAvgTimeStep = QLabel(self.pageAverageTime)
        self.lblAvgTimeStep.setObjectName(u"lblAvgTimeStep")

        self.gridLayout.addWidget(self.lblAvgTimeStep, 0, 2, 1, 1)

        self.leAvgTimeStep = QLineEdit(self.pageAverageTime)
        self.leAvgTimeStep.setObjectName(u"leAvgTimeStep")

        self.gridLayout.addWidget(self.leAvgTimeStep, 0, 3, 1, 1)

        self.cbAvgTimeMethod = QComboBox(self.pageAverageTime)
        self.cbAvgTimeMethod.addItem("")
        self.cbAvgTimeMethod.addItem("")
        self.cbAvgTimeMethod.setObjectName(u"cbAvgTimeMethod")

        self.gridLayout.addWidget(self.cbAvgTimeMethod, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 4)

        self.stackedPreprocessTools.addWidget(self.pageAverageTime)
        self.pageDerivate = QWidget()
        self.pageDerivate.setObjectName(u"pageDerivate")
        self.formLayout_9 = QFormLayout(self.pageDerivate)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.lblDerivWindow = QLabel(self.pageDerivate)
        self.lblDerivWindow.setObjectName(u"lblDerivWindow")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblDerivWindow)

        self.sbDerivPoly = QSpinBox(self.pageDerivate)
        self.sbDerivPoly.setObjectName(u"sbDerivPoly")
        self.sbDerivPoly.setValue(3)

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sbDerivPoly)

        self.lblDerivPoly = QLabel(self.pageDerivate)
        self.lblDerivPoly.setObjectName(u"lblDerivPoly")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDerivPoly)

        self.sbDerivWindow = QSpinBox(self.pageDerivate)
        self.sbDerivWindow.setObjectName(u"sbDerivWindow")
        self.sbDerivWindow.setMaximum(9999)
        self.sbDerivWindow.setSingleStep(2)
        self.sbDerivWindow.setValue(25)

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sbDerivWindow)

        self.lblDerivOrder = QLabel(self.pageDerivate)
        self.lblDerivOrder.setObjectName(u"lblDerivOrder")

        self.formLayout_9.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDerivOrder)

        self.sbDerivOrder = QSpinBox(self.pageDerivate)
        self.sbDerivOrder.setObjectName(u"sbDerivOrder")
        self.sbDerivOrder.setValue(1)

        self.formLayout_9.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sbDerivOrder)

        self.stackedPreprocessTools.addWidget(self.pageDerivate)
        self.pageDeletePoints = QWidget()
        self.pageDeletePoints.setObjectName(u"pageDeletePoints")
        self.formLayout_10 = QFormLayout(self.pageDeletePoints)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.lblDeleteDim = QLabel(self.pageDeletePoints)
        self.lblDeleteDim.setObjectName(u"lblDeleteDim")

        self.formLayout_10.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDeleteDim)

        self.lblDeletePoints = QLabel(self.pageDeletePoints)
        self.lblDeletePoints.setObjectName(u"lblDeletePoints")

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblDeletePoints)

        self.leDeletePoints = QLineEdit(self.pageDeletePoints)
        self.leDeletePoints.setObjectName(u"leDeletePoints")

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leDeletePoints)

        self.cbDeleteDim = QComboBox(self.pageDeletePoints)
        self.cbDeleteDim.addItem("")
        self.cbDeleteDim.addItem("")
        self.cbDeleteDim.setObjectName(u"cbDeleteDim")

        self.formLayout_10.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cbDeleteDim)

        self.stackedPreprocessTools.addWidget(self.pageDeletePoints)
        self.pageCalibrateWavelength = QWidget()
        self.pageCalibrateWavelength.setObjectName(u"pageCalibrateWavelength")
        self.formLayout_11 = QFormLayout(self.pageCalibrateWavelength)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.lblCalibPixels = QLabel(self.pageCalibrateWavelength)
        self.lblCalibPixels.setObjectName(u"lblCalibPixels")

        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCalibPixels)

        self.lblCalibWaves = QLabel(self.pageCalibrateWavelength)
        self.lblCalibWaves.setObjectName(u"lblCalibWaves")

        self.formLayout_11.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCalibWaves)

        self.lblCalibOrder = QLabel(self.pageCalibrateWavelength)
        self.lblCalibOrder.setObjectName(u"lblCalibOrder")

        self.formLayout_11.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCalibOrder)

        self.leCalibPixels = QLineEdit(self.pageCalibrateWavelength)
        self.leCalibPixels.setObjectName(u"leCalibPixels")

        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leCalibPixels)

        self.leCalibWaves = QLineEdit(self.pageCalibrateWavelength)
        self.leCalibWaves.setObjectName(u"leCalibWaves")

        self.formLayout_11.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leCalibWaves)

        self.sbCalibOrder = QSpinBox(self.pageCalibrateWavelength)
        self.sbCalibOrder.setObjectName(u"sbCalibOrder")
        self.sbCalibOrder.setValue(2)

        self.formLayout_11.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sbCalibOrder)

        self.stackedPreprocessTools.addWidget(self.pageCalibrateWavelength)
        self.pageChirpPolynomial = QWidget()
        self.pageChirpPolynomial.setObjectName(u"pageChirpPolynomial")
        self.formLayout_12 = QFormLayout(self.pageChirpPolynomial)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.lblChirpPoints = QLabel(self.pageChirpPolynomial)
        self.lblChirpPoints.setObjectName(u"lblChirpPoints")

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblChirpPoints)

        self.leChirpPoints = QLineEdit(self.pageChirpPolynomial)
        self.leChirpPoints.setObjectName(u"leChirpPoints")
        self.leChirpPoints.setReadOnly(True)

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leChirpPoints)

        self.stackedPreprocessTools.addWidget(self.pageChirpPolynomial)
        self.pageChirpSellmeier = QWidget()
        self.pageChirpSellmeier.setObjectName(u"pageChirpSellmeier")
        self.gridLayout_2 = QGridLayout(self.pageChirpSellmeier)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblChirpExc = QLabel(self.pageChirpSellmeier)
        self.lblChirpExc.setObjectName(u"lblChirpExc")

        self.gridLayout_2.addWidget(self.lblChirpExc, 0, 0, 1, 1)

        self.dsbChirpExc = QDoubleSpinBox(self.pageChirpSellmeier)
        self.dsbChirpExc.setObjectName(u"dsbChirpExc")

        self.gridLayout_2.addWidget(self.dsbChirpExc, 0, 1, 1, 1)

        self.lblChirpBK7 = QLabel(self.pageChirpSellmeier)
        self.lblChirpBK7.setObjectName(u"lblChirpBK7")

        self.gridLayout_2.addWidget(self.lblChirpBK7, 0, 2, 1, 1)

        self.dsbChirpBK7 = QDoubleSpinBox(self.pageChirpSellmeier)
        self.dsbChirpBK7.setObjectName(u"dsbChirpBK7")

        self.gridLayout_2.addWidget(self.dsbChirpBK7, 0, 3, 1, 1)

        self.lblChirpCaF2 = QLabel(self.pageChirpSellmeier)
        self.lblChirpCaF2.setObjectName(u"lblChirpCaF2")

        self.gridLayout_2.addWidget(self.lblChirpCaF2, 1, 0, 1, 1)

        self.dsbChirpCaF2 = QDoubleSpinBox(self.pageChirpSellmeier)
        self.dsbChirpCaF2.setObjectName(u"dsbChirpCaF2")

        self.gridLayout_2.addWidget(self.dsbChirpCaF2, 1, 1, 1, 1)

        self.lblChirpSiO2 = QLabel(self.pageChirpSellmeier)
        self.lblChirpSiO2.setObjectName(u"lblChirpSiO2")

        self.gridLayout_2.addWidget(self.lblChirpSiO2, 1, 2, 1, 1)

        self.dsbChirpSiO2 = QDoubleSpinBox(self.pageChirpSellmeier)
        self.dsbChirpSiO2.setObjectName(u"dsbChirpSiO2")

        self.gridLayout_2.addWidget(self.dsbChirpSiO2, 1, 3, 1, 1)

        self.lblChirpOffset = QLabel(self.pageChirpSellmeier)
        self.lblChirpOffset.setObjectName(u"lblChirpOffset")

        self.gridLayout_2.addWidget(self.lblChirpOffset, 2, 0, 1, 1)

        self.dsbChirpOffset = QDoubleSpinBox(self.pageChirpSellmeier)
        self.dsbChirpOffset.setObjectName(u"dsbChirpOffset")

        self.gridLayout_2.addWidget(self.dsbChirpOffset, 2, 1, 1, 3)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.stackedPreprocessTools.addWidget(self.pageChirpSellmeier)
        self.pageOverlapCorrection = QWidget()
        self.pageOverlapCorrection.setObjectName(u"pageOverlapCorrection")
        self.horizontalLayout_19 = QHBoxLayout(self.pageOverlapCorrection)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lblStitchPoint = QLabel(self.pageOverlapCorrection)
        self.lblStitchPoint.setObjectName(u"lblStitchPoint")

        self.horizontalLayout_19.addWidget(self.lblStitchPoint)

        self.leStitchPoint = QLineEdit(self.pageOverlapCorrection)
        self.leStitchPoint.setObjectName(u"leStitchPoint")

        self.horizontalLayout_19.addWidget(self.leStitchPoint)

        self.stackedPreprocessTools.addWidget(self.pageOverlapCorrection)

        self.verticalLayout_20.addWidget(self.stackedPreprocessTools)

        self.btnApplyPreprocess = QPushButton(self.grpPreprocessingSettings)
        self.btnApplyPreprocess.setObjectName(u"btnApplyPreprocess")
        self.btnApplyPreprocess.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnApplyPreprocess.sizePolicy().hasHeightForWidth())
        self.btnApplyPreprocess.setSizePolicy(sizePolicy1)
        self.btnApplyPreprocess.setMinimumSize(QSize(0, 30))
        self.btnApplyPreprocess.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btnApplyPreprocess.setFont(font1)

        self.verticalLayout_20.addWidget(self.btnApplyPreprocess)


        self.horizontalLayout_18.addWidget(self.grpPreprocessingSettings)

        self.line_3 = QFrame(self.pagePreprocessing)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_18.addWidget(self.line_3)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lblPreprocessHistory = QLabel(self.pagePreprocessing)
        self.lblPreprocessHistory.setObjectName(u"lblPreprocessHistory")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblPreprocessHistory.sizePolicy().hasHeightForWidth())
        self.lblPreprocessHistory.setSizePolicy(sizePolicy2)
        self.lblPreprocessHistory.setFont(font1)

        self.verticalLayout_13.addWidget(self.lblPreprocessHistory)

        self.listPreprocessHistory = QListWidget(self.pagePreprocessing)
        self.listPreprocessHistory.setObjectName(u"listPreprocessHistory")
        self.listPreprocessHistory.setEnabled(False)
        sizePolicy.setHeightForWidth(self.listPreprocessHistory.sizePolicy().hasHeightForWidth())
        self.listPreprocessHistory.setSizePolicy(sizePolicy)
        self.listPreprocessHistory.setMinimumSize(QSize(0, 110))
        self.listPreprocessHistory.setMaximumSize(QSize(16777215, 110))

        self.verticalLayout_13.addWidget(self.listPreprocessHistory)

        self.btnUndoPreprocess = QPushButton(self.pagePreprocessing)
        self.btnUndoPreprocess.setObjectName(u"btnUndoPreprocess")
        self.btnUndoPreprocess.setEnabled(False)

        self.verticalLayout_13.addWidget(self.btnUndoPreprocess)


        self.horizontalLayout_18.addLayout(self.verticalLayout_13)

        self.horizontalLayout_18.setStretch(0, 2)
        self.horizontalLayout_18.setStretch(2, 1)

        self.verticalLayout_21.addLayout(self.horizontalLayout_18)

        self.verticalLayout_21.setStretch(1, 2)
        self.tabMain.addTab(self.pagePreprocessing, "")
        self.pageDataExplorer = QWidget()
        self.pageDataExplorer.setObjectName(u"pageDataExplorer")
        self.verticalLayout_11 = QVBoxLayout(self.pageDataExplorer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.grpViewAndExport = QGroupBox(self.pageDataExplorer)
        self.grpViewAndExport.setObjectName(u"grpViewAndExport")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.grpViewAndExport.sizePolicy().hasHeightForWidth())
        self.grpViewAndExport.setSizePolicy(sizePolicy3)
        self.horizontalLayout_12 = QHBoxLayout(self.grpViewAndExport)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 9, -1, -1)
        self.lblViewMode = QLabel(self.grpViewAndExport)
        self.lblViewMode.setObjectName(u"lblViewMode")
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedViewModeOptions.sizePolicy().hasHeightForWidth())
        self.stackedViewModeOptions.setSizePolicy(sizePolicy4)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.grpTimeSelectionSpectra.sizePolicy().hasHeightForWidth())
        self.grpTimeSelectionSpectra.setSizePolicy(sizePolicy5)
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
        sizePolicy5.setHeightForWidth(self.grpProcessingAndRangesSpectra.sizePolicy().hasHeightForWidth())
        self.grpProcessingAndRangesSpectra.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dsbTimeRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.dsbTimeRangeStartSpectra.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.dsbTimeRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.dsbTimeRangeStopSpectra.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.sbAverageSpectra.sizePolicy().hasHeightForWidth())
        self.sbAverageSpectra.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.dsbMaskRangeStartSpectra.sizePolicy().hasHeightForWidth())
        self.dsbMaskRangeStartSpectra.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.dsbMaskRangeStopSpectra.sizePolicy().hasHeightForWidth())
        self.dsbMaskRangeStopSpectra.setSizePolicy(sizePolicy6)
        self.dsbMaskRangeStopSpectra.setMinimumSize(QSize(0, 26))
        self.dsbMaskRangeStopSpectra.setMaximum(10000.000000000000000)

        self.horizontalLayout_6.addWidget(self.dsbMaskRangeStopSpectra)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.grpProcessingAndRangesSpectra)

        self.grpStyleSpectra = QGroupBox(self.pageSpectraOptions)
        self.grpStyleSpectra.setObjectName(u"grpStyleSpectra")
        sizePolicy5.setHeightForWidth(self.grpStyleSpectra.sizePolicy().hasHeightForWidth())
        self.grpStyleSpectra.setSizePolicy(sizePolicy5)
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
        sizePolicy6.setHeightForWidth(self.cbColormapsSpectra.sizePolicy().hasHeightForWidth())
        self.cbColormapsSpectra.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.cbLegendSpectra.sizePolicy().hasHeightForWidth())
        self.cbLegendSpectra.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.cbStyleSpectra.sizePolicy().hasHeightForWidth())
        self.cbStyleSpectra.setSizePolicy(sizePolicy6)
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
        self.rbAllTrace.setMinimumSize(QSize(121, 26))
        self.rbAllTrace.setMaximumSize(QSize(121, 26))
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
        sizePolicy6.setHeightForWidth(self.cbLegendTrace.sizePolicy().hasHeightForWidth())
        self.cbLegendTrace.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.cbStyleTrace.sizePolicy().hasHeightForWidth())
        self.cbStyleTrace.setSizePolicy(sizePolicy6)
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
        sizePolicy3.setHeightForWidth(self.grpSvdSettings.sizePolicy().hasHeightForWidth())
        self.grpSvdSettings.setSizePolicy(sizePolicy3)
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
        self.sldSvdShowComps.setMaximum(15)
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
        self.sbSvdShowComps.setMaximum(15)
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
        sizePolicy3.setHeightForWidth(self.grpFittingType.sizePolicy().hasHeightForWidth())
        self.grpFittingType.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.cbFittingType.sizePolicy().hasHeightForWidth())
        self.cbFittingType.setSizePolicy(sizePolicy3)
        self.cbFittingType.setMinimumSize(QSize(201, 26))
        self.cbFittingType.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_11.addWidget(self.cbFittingType)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)


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
        sizePolicy3.setHeightForWidth(self.grpFitDataSelection.sizePolicy().hasHeightForWidth())
        self.grpFitDataSelection.setSizePolicy(sizePolicy3)
        self.grpFitDataSelection.setMinimumSize(QSize(0, 221))
        self.grpFitDataSelection.setMaximumSize(QSize(16777215, 221))
        self.verticalLayout_8 = QVBoxLayout(self.grpFitDataSelection)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 9)
        self.stackedFitDataSelection = QStackedWidget(self.grpFitDataSelection)
        self.stackedFitDataSelection.setObjectName(u"stackedFitDataSelection")
        sizePolicy4.setHeightForWidth(self.stackedFitDataSelection.sizePolicy().hasHeightForWidth())
        self.stackedFitDataSelection.setSizePolicy(sizePolicy4)
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
        sizePolicy6.setHeightForWidth(self.sbGlobalFitRegionMin.sizePolicy().hasHeightForWidth())
        self.sbGlobalFitRegionMin.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.sbGlobalFitRegionMax.sizePolicy().hasHeightForWidth())
        self.sbGlobalFitRegionMax.setSizePolicy(sizePolicy6)
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
        sizePolicy3.setHeightForWidth(self.grpFitInitialParam.sizePolicy().hasHeightForWidth())
        self.grpFitInitialParam.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.grpFittingProgress.sizePolicy().hasHeightForWidth())
        self.grpFittingProgress.setSizePolicy(sizePolicy3)
        self.grpFittingProgress.setMinimumSize(QSize(0, 221))
        self.grpFittingProgress.setMaximumSize(QSize(16777215, 221))
        self.verticalLayout_10 = QVBoxLayout(self.grpFittingProgress)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 0, 2, 2)
        self.textFitLog = QTextBrowser(self.grpFittingProgress)
        self.textFitLog.setObjectName(u"textFitLog")
        sizePolicy4.setHeightForWidth(self.textFitLog.sizePolicy().hasHeightForWidth())
        self.textFitLog.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(10)
        self.textFitLog.setFont(font2)

        self.verticalLayout_10.addWidget(self.textFitLog)


        self.hBoxLayoutFittingSettings.addWidget(self.grpFittingProgress)

        self.hBoxLayoutFittingSettings.setStretch(0, 1)
        self.hBoxLayoutFittingSettings.setStretch(1, 1)
        self.hBoxLayoutFittingSettings.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.hBoxLayoutFittingSettings)

        self.tabMain.addTab(self.pageFitting, "")
        self.pageResults = QWidget()
        self.pageResults.setObjectName(u"pageResults")
        self.verticalLayout_12 = QVBoxLayout(self.pageResults)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedResultsMain = QStackedWidget(self.pageResults)
        self.stackedResultsMain.setObjectName(u"stackedResultsMain")
        self.pageGlobalFit = QWidget()
        self.pageGlobalFit.setObjectName(u"pageGlobalFit")
        self.verticalLayout_18 = QVBoxLayout(self.pageGlobalFit)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.grpGlobalViewMode = QGroupBox(self.pageGlobalFit)
        self.grpGlobalViewMode.setObjectName(u"grpGlobalViewMode")
        self.grpGlobalViewMode.setMinimumSize(QSize(0, 50))
        self.grpGlobalViewMode.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_14 = QHBoxLayout(self.grpGlobalViewMode)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lblGlobalViewMode = QLabel(self.grpGlobalViewMode)
        self.lblGlobalViewMode.setObjectName(u"lblGlobalViewMode")
        sizePolicy2.setHeightForWidth(self.lblGlobalViewMode.sizePolicy().hasHeightForWidth())
        self.lblGlobalViewMode.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.lblGlobalViewMode)

        self.cbGlobalViewMode = QComboBox(self.grpGlobalViewMode)
        self.cbGlobalViewMode.addItem("")
        self.cbGlobalViewMode.addItem("")
        self.cbGlobalViewMode.addItem("")
        self.cbGlobalViewMode.setObjectName(u"cbGlobalViewMode")

        self.horizontalLayout_14.addWidget(self.cbGlobalViewMode)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.verticalLayout_18.addWidget(self.grpGlobalViewMode)

        self.stackedGlobalSettings = QStackedWidget(self.pageGlobalFit)
        self.stackedGlobalSettings.setObjectName(u"stackedGlobalSettings")
        self.stackedGlobalSettings.setMinimumSize(QSize(0, 50))
        self.stackedGlobalSettings.setMaximumSize(QSize(16777215, 50))
        self.pageDasSettings = QWidget()
        self.pageDasSettings.setObjectName(u"pageDasSettings")
        self.verticalLayout_14 = QVBoxLayout(self.pageDasSettings)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.grpDasSettings = QGroupBox(self.pageDasSettings)
        self.grpDasSettings.setObjectName(u"grpDasSettings")
        self.horizontalLayout_15 = QHBoxLayout(self.grpDasSettings)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.chkConvertToEAS = QCheckBox(self.grpDasSettings)
        self.chkConvertToEAS.setObjectName(u"chkConvertToEAS")

        self.horizontalLayout_15.addWidget(self.chkConvertToEAS)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)


        self.verticalLayout_14.addWidget(self.grpDasSettings)

        self.stackedGlobalSettings.addWidget(self.pageDasSettings)
        self.pageGlobalFitPlotSettings = QWidget()
        self.pageGlobalFitPlotSettings.setObjectName(u"pageGlobalFitPlotSettings")
        self.verticalLayout_15 = QVBoxLayout(self.pageGlobalFitPlotSettings)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.grpGlobalFitPlotSettings = QGroupBox(self.pageGlobalFitPlotSettings)
        self.grpGlobalFitPlotSettings.setObjectName(u"grpGlobalFitPlotSettings")
        self.grpGlobalFitPlotSettings.setMinimumSize(QSize(0, 50))
        self.grpGlobalFitPlotSettings.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_16 = QHBoxLayout(self.grpGlobalFitPlotSettings)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lblGlobalKineticsSel = QLabel(self.grpGlobalFitPlotSettings)
        self.lblGlobalKineticsSel.setObjectName(u"lblGlobalKineticsSel")

        self.horizontalLayout_16.addWidget(self.lblGlobalKineticsSel)

        self.leGlobalKineticsSel = QLineEdit(self.grpGlobalFitPlotSettings)
        self.leGlobalKineticsSel.setObjectName(u"leGlobalKineticsSel")

        self.horizontalLayout_16.addWidget(self.leGlobalKineticsSel)

        self.horizontalSpacer_3 = QSpacerItem(346, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addWidget(self.grpGlobalFitPlotSettings)

        self.stackedGlobalSettings.addWidget(self.pageGlobalFitPlotSettings)

        self.verticalLayout_18.addWidget(self.stackedGlobalSettings)

        self.splitter = QSplitter(self.pageGlobalFit)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.globalMplWidget = MplWidget(self.splitter)
        self.globalMplWidget.setObjectName(u"globalMplWidget")
        sizePolicy.setHeightForWidth(self.globalMplWidget.sizePolicy().hasHeightForWidth())
        self.globalMplWidget.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.globalMplWidget)
        self.grpGlobalReport = QGroupBox(self.splitter)
        self.grpGlobalReport.setObjectName(u"grpGlobalReport")
        self.verticalLayout_16 = QVBoxLayout(self.grpGlobalReport)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 2, -1, -1)
        self.textGlobalReport = QTextBrowser(self.grpGlobalReport)
        self.textGlobalReport.setObjectName(u"textGlobalReport")

        self.verticalLayout_16.addWidget(self.textGlobalReport)

        self.splitter.addWidget(self.grpGlobalReport)

        self.verticalLayout_18.addWidget(self.splitter)

        self.stackedResultsMain.addWidget(self.pageGlobalFit)
        self.pageSingleFit = QWidget()
        self.pageSingleFit.setObjectName(u"pageSingleFit")
        self.verticalLayout_19 = QVBoxLayout(self.pageSingleFit)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.grpSingleFitSettings = QGroupBox(self.pageSingleFit)
        self.grpSingleFitSettings.setObjectName(u"grpSingleFitSettings")
        sizePolicy4.setHeightForWidth(self.grpSingleFitSettings.sizePolicy().hasHeightForWidth())
        self.grpSingleFitSettings.setSizePolicy(sizePolicy4)
        self.grpSingleFitSettings.setMinimumSize(QSize(0, 61))
        self.grpSingleFitSettings.setMaximumSize(QSize(16777215, 61))
        self.horizontalLayout = QHBoxLayout(self.grpSingleFitSettings)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 2, -1, -1)
        self.chkSingleDetails = QCheckBox(self.grpSingleFitSettings)
        self.chkSingleDetails.setObjectName(u"chkSingleDetails")

        self.horizontalLayout.addWidget(self.chkSingleDetails)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout_19.addWidget(self.grpSingleFitSettings)

        self.singleMplWidget = MplWidget(self.pageSingleFit)
        self.singleMplWidget.setObjectName(u"singleMplWidget")
        sizePolicy.setHeightForWidth(self.singleMplWidget.sizePolicy().hasHeightForWidth())
        self.singleMplWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_19.addWidget(self.singleMplWidget)

        self.stackedResultsMain.addWidget(self.pageSingleFit)

        self.verticalLayout_12.addWidget(self.stackedResultsMain)

        self.tabMain.addTab(self.pageResults, "")

        self.verticalLayout_17.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.dockExperiments = QDockWidget(MainWindow)
        self.dockExperiments.setObjectName(u"dockExperiments")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.dockExperiments.sizePolicy().hasHeightForWidth())
        self.dockExperiments.setSizePolicy(sizePolicy7)
        self.dockExperiments.setMinimumSize(QSize(100, 100))
        self.dockExperiments.setBaseSize(QSize(300, 767))
        self.dockExperiments.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockExperiments.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockExperiments.setDockLocation(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.dockExperimentsContents = QWidget()
        self.dockExperimentsContents.setObjectName(u"dockExperimentsContents")
        sizePolicy7.setHeightForWidth(self.dockExperimentsContents.sizePolicy().hasHeightForWidth())
        self.dockExperimentsContents.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.treeExperiment.sizePolicy().hasHeightForWidth())
        self.treeExperiment.setSizePolicy(sizePolicy7)
        self.treeExperiment.setAlternatingRowColors(True)
        self.treeExperiment.setHeaderHidden(True)
        self.treeExperiment.setColumnCount(1)

        self.verticalLayout.addWidget(self.treeExperiment)

        self.dockExperiments.setWidget(self.dockExperimentsContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockExperiments)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabMain, self.cbPreprocessingTool)
        QWidget.setTabOrder(self.cbPreprocessingTool, self.cbCutWaveInner)
        QWidget.setTabOrder(self.cbCutWaveInner, self.leCutTimeMin)
        QWidget.setTabOrder(self.leCutTimeMin, self.leCutTimeMax)
        QWidget.setTabOrder(self.leCutTimeMax, self.leCutWaveMax)
        QWidget.setTabOrder(self.leCutWaveMax, self.leShiftTime)
        QWidget.setTabOrder(self.leShiftTime, self.chkBaseOnlyOne)
        QWidget.setTabOrder(self.chkBaseOnlyOne, self.lePolyBasePoints)
        QWidget.setTabOrder(self.lePolyBasePoints, self.sbPolyBaseOrder)
        QWidget.setTabOrder(self.sbPolyBaseOrder, self.sbAvgTimeGrid)
        QWidget.setTabOrder(self.sbAvgTimeGrid, self.leAvgTimeStart)
        QWidget.setTabOrder(self.leAvgTimeStart, self.leAvgTimeStep)
        QWidget.setTabOrder(self.leAvgTimeStep, self.cbAvgTimeMethod)
        QWidget.setTabOrder(self.cbAvgTimeMethod, self.sbDerivPoly)
        QWidget.setTabOrder(self.sbDerivPoly, self.sbDerivWindow)
        QWidget.setTabOrder(self.sbDerivWindow, self.sbDerivOrder)
        QWidget.setTabOrder(self.sbDerivOrder, self.leDeletePoints)
        QWidget.setTabOrder(self.leDeletePoints, self.cbDeleteDim)
        QWidget.setTabOrder(self.cbDeleteDim, self.leCalibPixels)
        QWidget.setTabOrder(self.leCalibPixels, self.leCalibWaves)
        QWidget.setTabOrder(self.leCalibWaves, self.sbCalibOrder)
        QWidget.setTabOrder(self.sbCalibOrder, self.leChirpPoints)
        QWidget.setTabOrder(self.leChirpPoints, self.dsbChirpExc)
        QWidget.setTabOrder(self.dsbChirpExc, self.dsbChirpBK7)
        QWidget.setTabOrder(self.dsbChirpBK7, self.dsbChirpCaF2)
        QWidget.setTabOrder(self.dsbChirpCaF2, self.dsbChirpSiO2)
        QWidget.setTabOrder(self.dsbChirpSiO2, self.dsbChirpOffset)
        QWidget.setTabOrder(self.dsbChirpOffset, self.btnApplyPreprocess)
        QWidget.setTabOrder(self.btnApplyPreprocess, self.listPreprocessHistory)
        QWidget.setTabOrder(self.listPreprocessHistory, self.btnUndoPreprocess)
        QWidget.setTabOrder(self.btnUndoPreprocess, self.cbViewMode)
        QWidget.setTabOrder(self.cbViewMode, self.btnExportPlot)
        QWidget.setTabOrder(self.btnExportPlot, self.cbColormaps3D)
        QWidget.setTabOrder(self.cbColormaps3D, self.cbStyle3D)
        QWidget.setTabOrder(self.cbStyle3D, self.sbRenderQuality3D)
        QWidget.setTabOrder(self.sbRenderQuality3D, self.btnResetView3D)
        QWidget.setTabOrder(self.btnResetView3D, self.rbAllSpectra)
        QWidget.setTabOrder(self.rbAllSpectra, self.rbAutomaticSpectra)
        QWidget.setTabOrder(self.rbAutomaticSpectra, self.sbNumberOfSpectra)
        QWidget.setTabOrder(self.sbNumberOfSpectra, self.chkAtWavelengthSpectra)
        QWidget.setTabOrder(self.chkAtWavelengthSpectra, self.dsbAtWavelengthSpectra)
        QWidget.setTabOrder(self.dsbAtWavelengthSpectra, self.rbCustomSpectra)
        QWidget.setTabOrder(self.rbCustomSpectra, self.leCustomTimesSpectral)
        QWidget.setTabOrder(self.leCustomTimesSpectral, self.chkTimeRangeSpectra)
        QWidget.setTabOrder(self.chkTimeRangeSpectra, self.dsbTimeRangeStartSpectra)
        QWidget.setTabOrder(self.dsbTimeRangeStartSpectra, self.dsbTimeRangeStopSpectra)
        QWidget.setTabOrder(self.dsbTimeRangeStopSpectra, self.chkFromMaxToMinSpectra)
        QWidget.setTabOrder(self.chkFromMaxToMinSpectra, self.sbAverageSpectra)
        QWidget.setTabOrder(self.sbAverageSpectra, self.chkMaskRangeSpectra)
        QWidget.setTabOrder(self.chkMaskRangeSpectra, self.dsbMaskRangeStartSpectra)
        QWidget.setTabOrder(self.dsbMaskRangeStartSpectra, self.dsbMaskRangeStopSpectra)
        QWidget.setTabOrder(self.dsbMaskRangeStopSpectra, self.cbColormapsSpectra)
        QWidget.setTabOrder(self.cbColormapsSpectra, self.cbLegendSpectra)
        QWidget.setTabOrder(self.cbLegendSpectra, self.cbStyleSpectra)
        QWidget.setTabOrder(self.cbStyleSpectra, self.rbAllTrace)
        QWidget.setTabOrder(self.rbAllTrace, self.rbAutomaticTrace)
        QWidget.setTabOrder(self.rbAutomaticTrace, self.rbCustomTrace)
        QWidget.setTabOrder(self.rbCustomTrace, self.leCustomWavelengthTrace)
        QWidget.setTabOrder(self.leCustomWavelengthTrace, self.cbLegendTrace)
        QWidget.setTabOrder(self.cbLegendTrace, self.cbStyleTrace)
        QWidget.setTabOrder(self.cbStyleTrace, self.sbSvdCalcComps)
        QWidget.setTabOrder(self.sbSvdCalcComps, self.sldSvdShowComps)
        QWidget.setTabOrder(self.sldSvdShowComps, self.sbSvdShowComps)
        QWidget.setTabOrder(self.sbSvdShowComps, self.chkSvdLogScale)
        QWidget.setTabOrder(self.chkSvdLogScale, self.cbFittingType)
        QWidget.setTabOrder(self.cbFittingType, self.rbGlobalFitSvd)
        QWidget.setTabOrder(self.rbGlobalFitSvd, self.sbGlobalFitSvdComps)
        QWidget.setTabOrder(self.sbGlobalFitSvdComps, self.rbGlobalFitRegion)
        QWidget.setTabOrder(self.rbGlobalFitRegion, self.sbGlobalFitRegionMin)
        QWidget.setTabOrder(self.sbGlobalFitRegionMin, self.sbGlobalFitRegionMax)
        QWidget.setTabOrder(self.sbGlobalFitRegionMax, self.rbGlobalFitTraces)
        QWidget.setTabOrder(self.rbGlobalFitTraces, self.leGlobalFitTraces)
        QWidget.setTabOrder(self.leGlobalFitTraces, self.sbGlobalFitAverage)
        QWidget.setTabOrder(self.sbGlobalFitAverage, self.leGlobalFitMasking)
        QWidget.setTabOrder(self.leGlobalFitMasking, self.sbSingleFitWave)
        QWidget.setTabOrder(self.sbSingleFitWave, self.sbSingleFitAverage)
        QWidget.setTabOrder(self.sbSingleFitAverage, self.sbExpNo)
        QWidget.setTabOrder(self.sbExpNo, self.dsbIRFw)
        QWidget.setTabOrder(self.dsbIRFw, self.dsbIRFmu)
        QWidget.setTabOrder(self.dsbIRFmu, self.leInitialTau)
        QWidget.setTabOrder(self.leInitialTau, self.chkTauInf)
        QWidget.setTabOrder(self.chkTauInf, self.btnRunFit)
        QWidget.setTabOrder(self.btnRunFit, self.textFitLog)
        QWidget.setTabOrder(self.textFitLog, self.cbGlobalViewMode)
        QWidget.setTabOrder(self.cbGlobalViewMode, self.chkConvertToEAS)
        QWidget.setTabOrder(self.chkConvertToEAS, self.leGlobalKineticsSel)
        QWidget.setTabOrder(self.leGlobalKineticsSel, self.textGlobalReport)
        QWidget.setTabOrder(self.textGlobalReport, self.chkSingleDetails)
        QWidget.setTabOrder(self.chkSingleDetails, self.treeExperiment)
        QWidget.setTabOrder(self.treeExperiment, self.leCutWaveMin)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actImport)
        self.menuFile.addAction(self.actLoad)
        self.menuFile.addAction(self.actSave)

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
        self.stackedPreprocessTools.setCurrentIndex(0)
        self.stackedViewModeOptions.setCurrentIndex(0)
        self.stackedFitDataSelection.setCurrentIndex(0)
        self.stackedResultsMain.setCurrentIndex(0)
        self.stackedGlobalSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actSave.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.actLoad.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.grpPreprocessingtool.setTitle("")
        self.lblPreprocessingTool.setText(QCoreApplication.translate("MainWindow", u"Preprocessing Tool:", None))
        self.cbPreprocessingTool.setItemText(0, QCoreApplication.translate("MainWindow", u"Cut Time", None))
        self.cbPreprocessingTool.setItemText(1, QCoreApplication.translate("MainWindow", u"Cut Wavelength", None))
        self.cbPreprocessingTool.setItemText(2, QCoreApplication.translate("MainWindow", u"Shift Time", None))
        self.cbPreprocessingTool.setItemText(3, QCoreApplication.translate("MainWindow", u"Baseline Subtraction", None))
        self.cbPreprocessingTool.setItemText(4, QCoreApplication.translate("MainWindow", u"Polynomial Baseline", None))
        self.cbPreprocessingTool.setItemText(5, QCoreApplication.translate("MainWindow", u"Average Time", None))
        self.cbPreprocessingTool.setItemText(6, QCoreApplication.translate("MainWindow", u"Derivate", None))
        self.cbPreprocessingTool.setItemText(7, QCoreApplication.translate("MainWindow", u"Delete Points", None))
        self.cbPreprocessingTool.setItemText(8, QCoreApplication.translate("MainWindow", u"Calibrate Wavelength", None))
        self.cbPreprocessingTool.setItemText(9, QCoreApplication.translate("MainWindow", u"Chirp Correction (Polynomial)", None))
        self.cbPreprocessingTool.setItemText(10, QCoreApplication.translate("MainWindow", u"Chirp Correction (Sellmeier)", None))
        self.cbPreprocessingTool.setItemText(11, QCoreApplication.translate("MainWindow", u"Correct Overlap", None))

        self.grpPreprocessingSettings.setTitle(QCoreApplication.translate("MainWindow", u"Tool Inputs", None))
        self.lblCutTimeMin.setText(QCoreApplication.translate("MainWindow", u"Min Time:", None))
        self.lblCutTimeMax.setText(QCoreApplication.translate("MainWindow", u"Max Time:", None))
        self.lblCutWaveMin.setText(QCoreApplication.translate("MainWindow", u"Min Wave:", None))
        self.lblCutWaveMax.setText(QCoreApplication.translate("MainWindow", u"Max Wave:", None))
        self.lblCutWaveInner.setText(QCoreApplication.translate("MainWindow", u"Cutting Mode:", None))
        self.cbCutWaveInner.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.cbCutWaveInner.setItemText(1, QCoreApplication.translate("MainWindow", u"Cut", None))

        self.lblShiftTime.setText(QCoreApplication.translate("MainWindow", u"Shift Value:", None))
        self.lblBaseSpec.setText(QCoreApplication.translate("MainWindow", u"Spectra Index/Count:", None))
        self.chkBaseOnlyOne.setText(QCoreApplication.translate("MainWindow", u"Subtract only this index (Don't average)", None))
#if QT_CONFIG(tooltip)
        self.leBaseSpec.setToolTip(QCoreApplication.translate("MainWindow", u"(e.g., \"5\" or \"2, 5\")", None))
#endif // QT_CONFIG(tooltip)
        self.leBaseSpec.setPlaceholderText("")
        self.lblPolyBasePoints.setText(QCoreApplication.translate("MainWindow", u"Zero Points:", None))
        self.lblPolyBaseOrder.setText(QCoreApplication.translate("MainWindow", u"Order:", None))
        self.lePolyBasePoints.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. 400, 500", None))
        self.lblAvgTimeMethod.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.lblAvgTimeStart.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.lblAvgTimeGrid.setText(QCoreApplication.translate("MainWindow", u"Grid Dense:", None))
        self.lblAvgTimeStep.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.cbAvgTimeMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Log", None))
        self.cbAvgTimeMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"Constant", None))

        self.lblDerivWindow.setText(QCoreApplication.translate("MainWindow", u"Window Length (Odd):", None))
        self.lblDerivPoly.setText(QCoreApplication.translate("MainWindow", u"Poly Order:", None))
        self.lblDerivOrder.setText(QCoreApplication.translate("MainWindow", u"Derivative:", None))
        self.lblDeleteDim.setText(QCoreApplication.translate("MainWindow", u"Dimension:", None))
        self.lblDeletePoints.setText(QCoreApplication.translate("MainWindow", u"Points:", None))
        self.leDeletePoints.setPlaceholderText(QCoreApplication.translate("MainWindow", u"451, 500, 537", None))
        self.cbDeleteDim.setItemText(0, QCoreApplication.translate("MainWindow", u"Time", None))
        self.cbDeleteDim.setItemText(1, QCoreApplication.translate("MainWindow", u"Wavelength", None))

        self.lblCalibPixels.setText(QCoreApplication.translate("MainWindow", u"Pixels:", None))
        self.lblCalibWaves.setText(QCoreApplication.translate("MainWindow", u"True Waves:", None))
        self.lblCalibOrder.setText(QCoreApplication.translate("MainWindow", u"Order:", None))
        self.leCalibPixels.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10, 50, 100 or 1-500", None))
        self.leCalibWaves.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200, 250, 300 or 300-800", None))
        self.lblChirpPoints.setText(QCoreApplication.translate("MainWindow", u"Click graph to pick points", None))
        self.lblChirpExc.setText(QCoreApplication.translate("MainWindow", u"Excitation:", None))
        self.lblChirpBK7.setText(QCoreApplication.translate("MainWindow", u"BK7:", None))
        self.lblChirpCaF2.setText(QCoreApplication.translate("MainWindow", u"CaF2:", None))
        self.lblChirpSiO2.setText(QCoreApplication.translate("MainWindow", u"SiO2:", None))
        self.lblChirpOffset.setText(QCoreApplication.translate("MainWindow", u"Offset:", None))
        self.lblStitchPoint.setText(QCoreApplication.translate("MainWindow", u"Stitch Wavelength", None))
        self.btnApplyPreprocess.setText(QCoreApplication.translate("MainWindow", u"Apply Tool", None))
        self.lblPreprocessHistory.setText(QCoreApplication.translate("MainWindow", u"Action History:", None))
        self.btnUndoPreprocess.setText(QCoreApplication.translate("MainWindow", u"Undo Last Action", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pagePreprocessing), QCoreApplication.translate("MainWindow", u"Preprocessing", None))
        self.grpViewAndExport.setTitle("")
        self.lblViewMode.setText(QCoreApplication.translate("MainWindow", u"View:", None))
        self.cbViewMode.setItemText(0, QCoreApplication.translate("MainWindow", u"3D View", None))
        self.cbViewMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Spectra", None))
        self.cbViewMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Trace", None))

        self.btnExportPlot.setText(QCoreApplication.translate("MainWindow", u"Export Plot", None))
        self.grp3DOptions.setTitle(QCoreApplication.translate("MainWindow", u"3D Settings", None))
        self.lblColorMaps3D.setText(QCoreApplication.translate("MainWindow", u"Colormaps:", None))
        self.cbColormaps3D.setItemText(0, QCoreApplication.translate("MainWindow", u"Viridis", None))
        self.cbColormaps3D.setItemText(1, QCoreApplication.translate("MainWindow", u"Plasma", None))
        self.cbColormaps3D.setItemText(2, QCoreApplication.translate("MainWindow", u"Inferno", None))
        self.cbColormaps3D.setItemText(3, QCoreApplication.translate("MainWindow", u"Magma", None))
        self.cbColormaps3D.setItemText(4, QCoreApplication.translate("MainWindow", u"Cividis", None))

        self.lblViewStyle3D.setText(QCoreApplication.translate("MainWindow", u"View style:", None))
        self.cbStyle3D.setItemText(0, QCoreApplication.translate("MainWindow", u"Surface", None))
        self.cbStyle3D.setItemText(1, QCoreApplication.translate("MainWindow", u"Wireframe", None))
        self.cbStyle3D.setItemText(2, QCoreApplication.translate("MainWindow", u"Contour", None))

        self.lblRenderQuality3D.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.lblResetView3D.setText(QCoreApplication.translate("MainWindow", u"Reset camera", None))
        self.btnResetView3D.setText("")
        self.grpTimeSelectionSpectra.setTitle(QCoreApplication.translate("MainWindow", u"Time Selection", None))
        self.rbAllSpectra.setText(QCoreApplication.translate("MainWindow", u"All Spectra", None))
        self.rbAutomaticSpectra.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.lblNumberOfSpectra.setText(QCoreApplication.translate("MainWindow", u"Number of spectra", None))
        self.chkAtWavelengthSpectra.setText(QCoreApplication.translate("MainWindow", u"Specific Wavelength:", None))
        self.rbCustomSpectra.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.leCustomTimesSpectral.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1, 5, 10.5, 100", None))
        self.grpProcessingAndRangesSpectra.setTitle(QCoreApplication.translate("MainWindow", u"Processing and Region", None))
        self.chkTimeRangeSpectra.setText(QCoreApplication.translate("MainWindow", u"Time interval range", None))
        self.lblTimeRangeStartSpectra.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.lblTimeRangeStopSpectra.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.chkFromMaxToMinSpectra.setText(QCoreApplication.translate("MainWindow", u"Time interval from maximum amplitude", None))
        self.lblAverageSpectra.setText(QCoreApplication.translate("MainWindow", u"Average points:", None))
        self.chkMaskRangeSpectra.setText(QCoreApplication.translate("MainWindow", u"Mask region", None))
        self.lblMaskRangeStartSpectra.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.lblMaskRangeStopSpectra.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.grpStyleSpectra.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.lblColormapsSpectra.setText(QCoreApplication.translate("MainWindow", u"Colormaps", None))
        self.cbColormapsSpectra.setItemText(0, QCoreApplication.translate("MainWindow", u"Viridis", None))
        self.cbColormapsSpectra.setItemText(1, QCoreApplication.translate("MainWindow", u"Plasma", None))
        self.cbColormapsSpectra.setItemText(2, QCoreApplication.translate("MainWindow", u"Inferno", None))
        self.cbColormapsSpectra.setItemText(3, QCoreApplication.translate("MainWindow", u"Magma", None))
        self.cbColormapsSpectra.setItemText(4, QCoreApplication.translate("MainWindow", u"Cividis", None))

        self.lblLegendSpectra.setText(QCoreApplication.translate("MainWindow", u"Legend", None))
        self.cbLegendSpectra.setItemText(0, QCoreApplication.translate("MainWindow", u"Text labels", None))
        self.cbLegendSpectra.setItemText(1, QCoreApplication.translate("MainWindow", u"Time colorbar", None))
        self.cbLegendSpectra.setItemText(2, QCoreApplication.translate("MainWindow", u"Hidden", None))

        self.lblStyleSpectra.setText(QCoreApplication.translate("MainWindow", u"View style", None))
        self.cbStyleSpectra.setItemText(0, QCoreApplication.translate("MainWindow", u"Ultrapyfit bright", None))
        self.cbStyleSpectra.setItemText(1, QCoreApplication.translate("MainWindow", u"Ultrapyfit dark", None))
        self.cbStyleSpectra.setItemText(2, QCoreApplication.translate("MainWindow", u"Default", None))
        self.cbStyleSpectra.setItemText(3, QCoreApplication.translate("MainWindow", u"Seaborn white grid", None))
        self.cbStyleSpectra.setItemText(4, QCoreApplication.translate("MainWindow", u"Seaborn dark grid", None))
        self.cbStyleSpectra.setItemText(5, QCoreApplication.translate("MainWindow", u"Dark background", None))
        self.cbStyleSpectra.setItemText(6, QCoreApplication.translate("MainWindow", u"ggplot", None))

        self.grpWavelengthSelectionTrace.setTitle(QCoreApplication.translate("MainWindow", u"Wavelength selection", None))
        self.rbAllTrace.setText(QCoreApplication.translate("MainWindow", u"All wavelengths", None))
        self.rbAutomaticTrace.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.rbCustomTrace.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.leCustomWavelengthTrace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450, 500, 620", None))
        self.grpStyleTrace.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.lblLegendTrace.setText(QCoreApplication.translate("MainWindow", u"Legend", None))
        self.cbLegendTrace.setItemText(0, QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.cbLegendTrace.setItemText(1, QCoreApplication.translate("MainWindow", u"Always shown", None))
        self.cbLegendTrace.setItemText(2, QCoreApplication.translate("MainWindow", u"Hidden", None))

        self.lblStyleTrace.setText(QCoreApplication.translate("MainWindow", u"View style", None))
        self.cbStyleTrace.setItemText(0, QCoreApplication.translate("MainWindow", u"Ultrapyfit bright", None))
        self.cbStyleTrace.setItemText(1, QCoreApplication.translate("MainWindow", u"Ultrapyfit dark", None))
        self.cbStyleTrace.setItemText(2, QCoreApplication.translate("MainWindow", u"Default", None))
        self.cbStyleTrace.setItemText(3, QCoreApplication.translate("MainWindow", u"Seaborn white grid", None))
        self.cbStyleTrace.setItemText(4, QCoreApplication.translate("MainWindow", u"Seaborn dark grid", None))
        self.cbStyleTrace.setItemText(5, QCoreApplication.translate("MainWindow", u"Dark background", None))
        self.cbStyleTrace.setItemText(6, QCoreApplication.translate("MainWindow", u"ggplot", None))

        self.tabMain.setTabText(self.tabMain.indexOf(self.pageDataExplorer), QCoreApplication.translate("MainWindow", u"Data Explorer", None))
        self.grpSvdSettings.setTitle(QCoreApplication.translate("MainWindow", u"SVD Settings", None))
        self.lblSvdCalcComps.setText(QCoreApplication.translate("MainWindow", u"Calculated components:", None))
        self.lblSvdShowComps.setText(QCoreApplication.translate("MainWindow", u"Rendered components:", None))
        self.chkSvdLogScale.setText(QCoreApplication.translate("MainWindow", u"Logaritmic scale", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pageSvd), QCoreApplication.translate("MainWindow", u"SVD", None))
        self.grpFittingType.setTitle("")
        self.lblFittingType.setText(QCoreApplication.translate("MainWindow", u"Fit type:", None))
        self.cbFittingType.setItemText(0, QCoreApplication.translate("MainWindow", u"Global fit", None))
        self.cbFittingType.setItemText(1, QCoreApplication.translate("MainWindow", u"Single trace fit", None))

#if QT_CONFIG(tooltip)
        self.cbFittingType.setToolTip(QCoreApplication.translate("MainWindow", u"V\u00e1lassza ki, hogy a teljes 2D adathalmazra (Glob\u00e1lis illeszt\u00e9s) vagy csak egyetlen kiv\u00e1lasztott kinetikai nyomra szeretne modellt illeszteni.", None))
#endif // QT_CONFIG(tooltip)
        self.grpFitDataSelection.setTitle(QCoreApplication.translate("MainWindow", u"Data Selection", None))
#if QT_CONFIG(tooltip)
        self.rbGlobalFitSvd.setToolTip(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s a Szingul\u00e1ris \u00c9rt\u00e9k Felbont\u00e1s (SVD) kinetikai vektorai alapj\u00e1n. Ez a legink\u00e1bb aj\u00e1nlott m\u00f3dszer, mivel kiv\u00e1l\u00f3an sz\u0171ri a zajt.", None))
#endif // QT_CONFIG(tooltip)
        self.rbGlobalFitSvd.setText(QCoreApplication.translate("MainWindow", u"Svd components:", None))
#if QT_CONFIG(tooltip)
        self.sbGlobalFitSvdComps.setToolTip(QCoreApplication.translate("MainWindow", u"A glob\u00e1lis illeszt\u00e9shez haszn\u00e1lt SVD komponensek sz\u00e1ma (\u00e1ltal\u00e1ban 2-6 k\u00f6z\u00f6tti \u00e9rt\u00e9k).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rbGlobalFitRegion.setToolTip(QCoreApplication.translate("MainWindow", u"Illeszt\u00e9s egy megadott, egybef\u00fcgg\u0151 hull\u00e1mhossz-tartom\u00e1nyon bel\u00fcl.", None))
#endif // QT_CONFIG(tooltip)
        self.rbGlobalFitRegion.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
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
        self.rbGlobalFitTraces.setText(QCoreApplication.translate("MainWindow", u"Traces:", None))
#if QT_CONFIG(tooltip)
        self.leGlobalFitTraces.setToolTip(QCoreApplication.translate("MainWindow", u"Adja meg a vizsg\u00e1lni k\u00edv\u00e1nt hull\u00e1mhosszakat vessz\u0151vel elv\u00e1lasztva (pl. 450, 500, 550).", None))
#endif // QT_CONFIG(tooltip)
        self.leGlobalFitTraces.setPlaceholderText(QCoreApplication.translate("MainWindow", u"450, 500, 550", None))
        self.lblGlobalFitAverage.setText(QCoreApplication.translate("MainWindow", u"Average points:", None))
#if QT_CONFIG(tooltip)
        self.sbGlobalFitAverage.setToolTip(QCoreApplication.translate("MainWindow", u"A kiv\u00e1lasztott hull\u00e1mhosszak k\u00f6r\u00fcli szomsz\u00e9dos pixelek \u00e1tlagol\u00e1sa a zaj cs\u00f6kkent\u00e9se \u00e9rdek\u00e9ben (1 = egy pixel balra \u00e9s jobbra).", None))
#endif // QT_CONFIG(tooltip)
        self.lblGlobalFitMasking.setText(QCoreApplication.translate("MainWindow", u"Excluded regions:", None))
#if QT_CONFIG(tooltip)
        self.leGlobalFitMasking.setToolTip(QCoreApplication.translate("MainWindow", u"KIZ\u00c1RT TARTOM\u00c1NYOK: Adja meg az illeszt\u00e9sb\u0151l kihagyni k\u00edv\u00e1nt r\u00e9szeket k\u00f6t\u0151jellel \u00e9s vessz\u0151vel (pl. a l\u00e9zersz\u00f3r\u00e1s kisz\u0171r\u00e9s\u00e9re: 390-410, 790-810).", None))
#endif // QT_CONFIG(tooltip)
        self.leGlobalFitMasking.setPlaceholderText(QCoreApplication.translate("MainWindow", u"390-410, 790-810", None))
        self.lblSingleFitWave.setText(QCoreApplication.translate("MainWindow", u"Wavelength analyzed  (nm):", None))
#if QT_CONFIG(tooltip)
        self.sbSingleFitWave.setToolTip(QCoreApplication.translate("MainWindow", u"Adja meg azt az egyetlen hull\u00e1mhosszt (nm), amelyre az exponenci\u00e1lis modellt illeszteni szeretn\u00e9.", None))
#endif // QT_CONFIG(tooltip)
        self.lblSingleFitAverage.setText(QCoreApplication.translate("MainWindow", u"Average (points):", None))
        self.grpFitInitialParam.setTitle(QCoreApplication.translate("MainWindow", u"Settings and Execution", None))
        self.lblExpNo.setText(QCoreApplication.translate("MainWindow", u"Number of Exponential", None))
#if QT_CONFIG(tooltip)
        self.sbExpNo.setToolTip(QCoreApplication.translate("MainWindow", u"A modellben szerepl\u0151 exponenci\u00e1lis boml\u00e1sok (tau) sz\u00e1ma (\u00e1ltal\u00e1ban 1 \u00e9s 4 k\u00f6z\u00f6tt).", None))
#endif // QT_CONFIG(tooltip)
        self.lblIRFw.setText(QCoreApplication.translate("MainWindow", u"IRF width:", None))
#if QT_CONFIG(tooltip)
        self.dsbIRFw.setToolTip(QCoreApplication.translate("MainWindow", u"A m\u0171szer v\u00e1laszf\u00fcggv\u00e9ny\u00e9nek (IRF) kezdeti sz\u00e9less\u00e9g-becsl\u00e9se (FWHM).", None))
#endif // QT_CONFIG(tooltip)
        self.lblIRFmu.setText(QCoreApplication.translate("MainWindow", u"Time zero:", None))
#if QT_CONFIG(tooltip)
        self.dsbIRFmu.setToolTip(QCoreApplication.translate("MainWindow", u"A nulla id\u0151pont (t0) kezdeti becsl\u00e9se.", None))
#endif // QT_CONFIG(tooltip)
        self.lblInitialTau.setText(QCoreApplication.translate("MainWindow", u"Starter tau(s)", None))
#if QT_CONFIG(tooltip)
        self.leInitialTau.setToolTip(QCoreApplication.translate("MainWindow", u"OPCION\u00c1LIS: Adja meg a kezdeti \u00e9lettartam (tau) becsl\u00e9seket pikoszekundumban, vessz\u0151vel elv\u00e1lasztva (pl. 1.5, 10, 200). Ha \u00fcresen hagyja, a program automatikusan gener\u00e1l becsl\u00e9st.", None))
#endif // QT_CONFIG(tooltip)
        self.leInitialTau.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optional (1.5, 15, 200)", None))
#if QT_CONFIG(tooltip)
        self.chkTauInf.setToolTip(QCoreApplication.translate("MainWindow", u"Adjon a modellhez egy v\u00e9gtelen \u00e9lettartam\u00fa (nem boml\u00f3) komponenst az id\u0151ablakot meghalad\u00f3, hossz\u00fa t\u00e1v\u00fa h\u00e1tt\u00e9rjelek le\u00edr\u00e1s\u00e1ra.", None))
#endif // QT_CONFIG(tooltip)
        self.chkTauInf.setText(QCoreApplication.translate("MainWindow", u"Infinite Component", None))
#if QT_CONFIG(tooltip)
        self.btnRunFit.setToolTip(QCoreApplication.translate("MainWindow", u"Ind\u00edtsa el az illeszt\u00e9si algoritmust a megadott param\u00e9terekkel. A folyamat befejezt\u00e9vel az eredm\u00e9ny megjelenik a bal oldali f\u00e1ban.", None))
#endif // QT_CONFIG(tooltip)
        self.btnRunFit.setText(QCoreApplication.translate("MainWindow", u"Start Fit", None))
        self.grpFittingProgress.setTitle(QCoreApplication.translate("MainWindow", u"Fitting Progress", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pageFitting), QCoreApplication.translate("MainWindow", u"Fitting Settings", None))
        self.grpGlobalViewMode.setTitle("")
        self.lblGlobalViewMode.setText(QCoreApplication.translate("MainWindow", u"View:", None))
        self.cbGlobalViewMode.setItemText(0, QCoreApplication.translate("MainWindow", u"DAS / SAS Spectra", None))
        self.cbGlobalViewMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Kinetics (Fitted Traces)", None))
        self.cbGlobalViewMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Kinetics + Residuals", None))

        self.grpDasSettings.setTitle("")
        self.chkConvertToEAS.setText(QCoreApplication.translate("MainWindow", u"EAS (Szekvenci\u00e1lis) Spektrumok", None))
        self.grpGlobalFitPlotSettings.setTitle("")
        self.lblGlobalKineticsSel.setText(QCoreApplication.translate("MainWindow", u"Hull\u00e1mhosszak (nm):", None))
        self.grpGlobalReport.setTitle(QCoreApplication.translate("MainWindow", u"Glob\u00e1lis Illeszt\u00e9s Eredm\u00e9nyei:", None))
        self.grpSingleFitSettings.setTitle(QCoreApplication.translate("MainWindow", u"Egyedi Kinetikai Illeszt\u00e9s", None))
        self.chkSingleDetails.setText(QCoreApplication.translate("MainWindow", u"Tau \u00e9rt\u00e9kek mutat\u00e1sa a grafikonon", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.pageResults), QCoreApplication.translate("MainWindow", u"Result", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.dockExperiments.setWindowTitle(QCoreApplication.translate("MainWindow", u"Experiments", None))
    # retranslateUi

