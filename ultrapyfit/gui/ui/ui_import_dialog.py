# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ImportDialog(object):
    def setupUi(self, ImportDialog):
        if not ImportDialog.objectName():
            ImportDialog.setObjectName(u"ImportDialog")
        ImportDialog.resize(761, 651)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportDialog.sizePolicy().hasHeightForWidth())
        ImportDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        ImportDialog.setFont(font)
        ImportDialog.setLocale(QLocale(QLocale.Hungarian, QLocale.Hungary))
        self.verticalLayout_2 = QVBoxLayout(ImportDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FilePathLabel = QLabel(ImportDialog)
        self.FilePathLabel.setObjectName(u"FilePathLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.FilePathLabel.setFont(font1)

        self.horizontalLayout_2.addWidget(self.FilePathLabel)

        self.FilePathLineEdit = QLineEdit(ImportDialog)
        self.FilePathLineEdit.setObjectName(u"FilePathLineEdit")
        self.FilePathLineEdit.setFont(font1)
        self.FilePathLineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.FilePathLineEdit)

        self.BrowseButton = QPushButton(ImportDialog)
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.BrowseButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FormatOptionsGroupBox = QGroupBox(ImportDialog)
        self.FormatOptionsGroupBox.setObjectName(u"FormatOptionsGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FormatOptionsGroupBox.sizePolicy().hasHeightForWidth())
        self.FormatOptionsGroupBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.FormatOptionsGroupBox.setFont(font2)
        self.FormatOptionsGroupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.FormatOptionsGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.SepLabel = QLabel(self.FormatOptionsGroupBox)
        self.SepLabel.setObjectName(u"SepLabel")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.SepLabel.setFont(font3)

        self.verticalLayout.addWidget(self.SepLabel)

        self.SepComboBox = QComboBox(self.FormatOptionsGroupBox)
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.setObjectName(u"SepComboBox")
        self.SepComboBox.setFont(font3)

        self.verticalLayout.addWidget(self.SepComboBox)

        self.OtherSepLabel = QLabel(self.FormatOptionsGroupBox)
        self.OtherSepLabel.setObjectName(u"OtherSepLabel")
        self.OtherSepLabel.setFont(font3)

        self.verticalLayout.addWidget(self.OtherSepLabel)

        self.OtherSepLineEdit = QLineEdit(self.FormatOptionsGroupBox)
        self.OtherSepLineEdit.setObjectName(u"OtherSepLineEdit")
        self.OtherSepLineEdit.setFont(font3)
        self.OtherSepLineEdit.setMaxLength(32767)

        self.verticalLayout.addWidget(self.OtherSepLineEdit)

        self.DecLabel = QLabel(self.FormatOptionsGroupBox)
        self.DecLabel.setObjectName(u"DecLabel")
        self.DecLabel.setFont(font3)

        self.verticalLayout.addWidget(self.DecLabel)

        self.DecComboBox = QComboBox(self.FormatOptionsGroupBox)
        self.DecComboBox.addItem("")
        self.DecComboBox.addItem("")
        self.DecComboBox.setObjectName(u"DecComboBox")
        self.DecComboBox.setFont(font3)

        self.verticalLayout.addWidget(self.DecComboBox)

        self.WaveIsRowCheckBox = QCheckBox(self.FormatOptionsGroupBox)
        self.WaveIsRowCheckBox.setObjectName(u"WaveIsRowCheckBox")
        self.WaveIsRowCheckBox.setFont(font3)

        self.verticalLayout.addWidget(self.WaveIsRowCheckBox)

        self.TimeColumnLabel = QLabel(self.FormatOptionsGroupBox)
        self.TimeColumnLabel.setObjectName(u"TimeColumnLabel")
        self.TimeColumnLabel.setFont(font3)

        self.verticalLayout.addWidget(self.TimeColumnLabel)

        self.TimeColumnSpinBox = QSpinBox(self.FormatOptionsGroupBox)
        self.TimeColumnSpinBox.setObjectName(u"TimeColumnSpinBox")
        self.TimeColumnSpinBox.setFont(font3)
        self.TimeColumnSpinBox.setMinimum(1)
        self.TimeColumnSpinBox.setMaximum(999)
        self.TimeColumnSpinBox.setValue(1)

        self.verticalLayout.addWidget(self.TimeColumnSpinBox)

        self.WavelengthRowLabel = QLabel(self.FormatOptionsGroupBox)
        self.WavelengthRowLabel.setObjectName(u"WavelengthRowLabel")
        self.WavelengthRowLabel.setFont(font3)

        self.verticalLayout.addWidget(self.WavelengthRowLabel)

        self.WavelengthRowSpinBox = QSpinBox(self.FormatOptionsGroupBox)
        self.WavelengthRowSpinBox.setObjectName(u"WavelengthRowSpinBox")
        self.WavelengthRowSpinBox.setFont(font3)
        self.WavelengthRowSpinBox.setMinimum(1)
        self.WavelengthRowSpinBox.setMaximum(999)
        self.WavelengthRowSpinBox.setValue(1)

        self.verticalLayout.addWidget(self.WavelengthRowSpinBox)

        self.TimeMetricLabel = QLabel(self.FormatOptionsGroupBox)
        self.TimeMetricLabel.setObjectName(u"TimeMetricLabel")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setKerning(True)
        self.TimeMetricLabel.setFont(font4)

        self.verticalLayout.addWidget(self.TimeMetricLabel)

        self.TimeMetricComboBox = QComboBox(self.FormatOptionsGroupBox)
        self.TimeMetricComboBox.addItem("")
        self.TimeMetricComboBox.addItem("")
        self.TimeMetricComboBox.addItem("")
        self.TimeMetricComboBox.addItem("")
        self.TimeMetricComboBox.addItem("")
        self.TimeMetricComboBox.setObjectName(u"TimeMetricComboBox")
        self.TimeMetricComboBox.setFont(font3)

        self.verticalLayout.addWidget(self.TimeMetricComboBox)

        self.WavelengthMetricLabel = QLabel(self.FormatOptionsGroupBox)
        self.WavelengthMetricLabel.setObjectName(u"WavelengthMetricLabel")
        self.WavelengthMetricLabel.setFont(font3)

        self.verticalLayout.addWidget(self.WavelengthMetricLabel)

        self.WavelengthMetricComboBox = QComboBox(self.FormatOptionsGroupBox)
        self.WavelengthMetricComboBox.addItem("")
        self.WavelengthMetricComboBox.addItem("")
        self.WavelengthMetricComboBox.addItem("")
        self.WavelengthMetricComboBox.setObjectName(u"WavelengthMetricComboBox")
        self.WavelengthMetricComboBox.setFont(font3)

        self.verticalLayout.addWidget(self.WavelengthMetricComboBox)

        self.lblMetaShapeDescription = QLabel(self.FormatOptionsGroupBox)
        self.lblMetaShapeDescription.setObjectName(u"lblMetaShapeDescription")
        self.lblMetaShapeDescription.setFont(font3)

        self.verticalLayout.addWidget(self.lblMetaShapeDescription)

        self.lblMetaShape = QLabel(self.FormatOptionsGroupBox)
        self.lblMetaShape.setObjectName(u"lblMetaShape")
        self.lblMetaShape.setFont(font3)

        self.verticalLayout.addWidget(self.lblMetaShape)


        self.horizontalLayout.addWidget(self.FormatOptionsGroupBox)

        self.tableWidget = QTableWidget(ImportDialog)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setPointSize(9)
        self.tableWidget.setFont(font5)

        self.horizontalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ImportButton = QPushButton(ImportDialog)
        self.ImportButton.setObjectName(u"ImportButton")
        self.ImportButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.ImportButton)


        self.retranslateUi(ImportDialog)

        QMetaObject.connectSlotsByName(ImportDialog)
    # setupUi

    def retranslateUi(self, ImportDialog):
        ImportDialog.setWindowTitle(QCoreApplication.translate("ImportDialog", u"Import Dialog", None))
        self.FilePathLabel.setText(QCoreApplication.translate("ImportDialog", u"File Path:", None))
        self.BrowseButton.setText(QCoreApplication.translate("ImportDialog", u"Browse", None))
        self.FormatOptionsGroupBox.setTitle(QCoreApplication.translate("ImportDialog", u"Import Settings", None))
        self.SepLabel.setText(QCoreApplication.translate("ImportDialog", u"Separator character (guessed):", None))
        self.SepComboBox.setItemText(0, QCoreApplication.translate("ImportDialog", u"Semicolon (;)", None))
        self.SepComboBox.setItemText(1, QCoreApplication.translate("ImportDialog", u"Colon (:)", None))
        self.SepComboBox.setItemText(2, QCoreApplication.translate("ImportDialog", u"Comma (,)", None))
        self.SepComboBox.setItemText(3, QCoreApplication.translate("ImportDialog", u"Tab key (\\t)", None))
        self.SepComboBox.setItemText(4, QCoreApplication.translate("ImportDialog", u"Hyphen (-)", None))
        self.SepComboBox.setItemText(5, QCoreApplication.translate("ImportDialog", u"Underscore (_)", None))
        self.SepComboBox.setItemText(6, QCoreApplication.translate("ImportDialog", u"Space ( )", None))
        self.SepComboBox.setItemText(7, QCoreApplication.translate("ImportDialog", u"Vertical line (|)", None))
        self.SepComboBox.setItemText(8, QCoreApplication.translate("ImportDialog", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.SepComboBox.setToolTip(QCoreApplication.translate("ImportDialog", u"Ignor\u00e1lt, ha van valami bele\u00edrva az egy\u00e9b szepar\u00e1tor men\u00fcbe.", None))
#endif // QT_CONFIG(tooltip)
        self.OtherSepLabel.setText(QCoreApplication.translate("ImportDialog", u"Custom Separator:", None))
#if QT_CONFIG(tooltip)
        self.OtherSepLineEdit.setToolTip(QCoreApplication.translate("ImportDialog", u"A list\u00e1ban nem tal\u00e1lhat\u00f3 szepar\u00e1tor eset\u00e9n kell kit\u00f6lteni.", None))
#endif // QT_CONFIG(tooltip)
        self.DecLabel.setText(QCoreApplication.translate("ImportDialog", u"Decimal point:", None))
        self.DecComboBox.setItemText(0, QCoreApplication.translate("ImportDialog", u"Pont (.)", None))
        self.DecComboBox.setItemText(1, QCoreApplication.translate("ImportDialog", u"Vessz\u0151 (,)", None))

#if QT_CONFIG(tooltip)
        self.DecComboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.WaveIsRowCheckBox.setText(QCoreApplication.translate("ImportDialog", u"Wave is row?", None))
        self.TimeColumnLabel.setText(QCoreApplication.translate("ImportDialog", u"Column containing timestamp:", None))
#if QT_CONFIG(tooltip)
        self.TimeColumnSpinBox.setToolTip(QCoreApplication.translate("ImportDialog", u"H\u00e1nyadik sor/oszlop tartalmazza az id\u0151 b\u00e9lyeget.", None))
#endif // QT_CONFIG(tooltip)
        self.WavelengthRowLabel.setText(QCoreApplication.translate("ImportDialog", u"Row containing wavelengths:", None))
#if QT_CONFIG(tooltip)
        self.WavelengthRowSpinBox.setToolTip(QCoreApplication.translate("ImportDialog", u"H\u00e1nyadik sor/oszlop tartalmazza a hull\u00e1mhosszat.", None))
#endif // QT_CONFIG(tooltip)
        self.TimeMetricLabel.setText(QCoreApplication.translate("ImportDialog", u"Unit of time:", None))
        self.TimeMetricComboBox.setItemText(0, QCoreApplication.translate("ImportDialog", u"Nanosecond (ns)", None))
        self.TimeMetricComboBox.setItemText(1, QCoreApplication.translate("ImportDialog", u"Microsecond (\u03bcs)", None))
        self.TimeMetricComboBox.setItemText(2, QCoreApplication.translate("ImportDialog", u"Picosecond (ps)", None))
        self.TimeMetricComboBox.setItemText(3, QCoreApplication.translate("ImportDialog", u"Femtosecond (fs)", None))
        self.TimeMetricComboBox.setItemText(4, QCoreApplication.translate("ImportDialog", u"Attosecond (as)", None))

        self.WavelengthMetricLabel.setText(QCoreApplication.translate("ImportDialog", u"Unit of wavelength:", None))
        self.WavelengthMetricComboBox.setItemText(0, QCoreApplication.translate("ImportDialog", u"Nanometer (nm)", None))
        self.WavelengthMetricComboBox.setItemText(1, QCoreApplication.translate("ImportDialog", u"Micrometer (\u00b5m)", None))
        self.WavelengthMetricComboBox.setItemText(2, QCoreApplication.translate("ImportDialog", u"Picometer (pm)", None))

        self.lblMetaShapeDescription.setText(QCoreApplication.translate("ImportDialog", u"Datapoints (Time x Trace)", None))
        self.lblMetaShape.setText(QCoreApplication.translate("ImportDialog", u"-", None))
        self.ImportButton.setText(QCoreApplication.translate("ImportDialog", u"Import", None))
    # retranslateUi

