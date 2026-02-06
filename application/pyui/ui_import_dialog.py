# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_import_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_ImportOptionsDialog(object):
    def setupUi(self, ImportOptionsDialog):
        if not ImportOptionsDialog.objectName():
            ImportOptionsDialog.setObjectName(u"ImportOptionsDialog")
        ImportOptionsDialog.resize(520, 250)
        font = QFont()
        font.setPointSize(14)
        ImportOptionsDialog.setFont(font)
        ImportOptionsDialog.setLocale(QLocale(QLocale.Hungarian, QLocale.Hungary))
        self.SepComboBox = QComboBox(ImportOptionsDialog)
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.addItem("")
        self.SepComboBox.setObjectName(u"SepComboBox")
        self.SepComboBox.setGeometry(QRect(10, 40, 211, 34))
        self.Seplabel = QLabel(ImportOptionsDialog)
        self.Seplabel.setObjectName(u"Seplabel")
        self.Seplabel.setGeometry(QRect(10, 10, 182, 26))
        self.OtherSepLineEdit = QLineEdit(ImportOptionsDialog)
        self.OtherSepLineEdit.setObjectName(u"OtherSepLineEdit")
        self.OtherSepLineEdit.setGeometry(QRect(230, 40, 161, 34))
        self.OtherSeplabel = QLabel(ImportOptionsDialog)
        self.OtherSeplabel.setObjectName(u"OtherSeplabel")
        self.OtherSeplabel.setGeometry(QRect(230, 10, 161, 26))
        self.Declabel = QLabel(ImportOptionsDialog)
        self.Declabel.setObjectName(u"Declabel")
        self.Declabel.setGeometry(QRect(400, 10, 93, 26))
        self.DecComboBox = QComboBox(ImportOptionsDialog)
        self.DecComboBox.addItem("")
        self.DecComboBox.addItem("")
        self.DecComboBox.setObjectName(u"DecComboBox")
        self.DecComboBox.setGeometry(QRect(400, 40, 112, 34))
        self.WaveIsRowCheckBox = QCheckBox(ImportOptionsDialog)
        self.WaveIsRowCheckBox.setObjectName(u"WaveIsRowCheckBox")
        self.WaveIsRowCheckBox.setGeometry(QRect(10, 80, 203, 31))
        self.TimeSpinBox = QSpinBox(ImportOptionsDialog)
        self.TimeSpinBox.setObjectName(u"TimeSpinBox")
        self.TimeSpinBox.setGeometry(QRect(350, 116, 62, 35))
        self.TimeSpinBox.setMinimum(1)
        self.TimeSpinBox.setMaximum(999)
        self.TimeSpinBox.setValue(1)
        self.WavelengthSpinBox = QSpinBox(ImportOptionsDialog)
        self.WavelengthSpinBox.setObjectName(u"WavelengthSpinBox")
        self.WavelengthSpinBox.setGeometry(QRect(350, 156, 62, 35))
        self.WavelengthSpinBox.setMinimum(1)
        self.WavelengthSpinBox.setMaximum(999)
        self.WavelengthSpinBox.setValue(1)
        self.TimeLabel = QLabel(ImportOptionsDialog)
        self.TimeLabel.setObjectName(u"TimeLabel")
        self.TimeLabel.setGeometry(QRect(10, 120, 311, 26))
        self.WavelengthLabel = QLabel(ImportOptionsDialog)
        self.WavelengthLabel.setObjectName(u"WavelengthLabel")
        self.WavelengthLabel.setGeometry(QRect(10, 160, 337, 26))
        self.ContinueButton = QPushButton(ImportOptionsDialog)
        self.ContinueButton.setObjectName(u"ContinueButton")
        self.ContinueButton.setGeometry(QRect(220, 210, 80, 34))

        self.retranslateUi(ImportOptionsDialog)

        QMetaObject.connectSlotsByName(ImportOptionsDialog)
    # setupUi

    def retranslateUi(self, ImportOptionsDialog):
        ImportOptionsDialog.setWindowTitle(QCoreApplication.translate("ImportOptionsDialog", u"Dialog", None))
        self.SepComboBox.setItemText(0, QCoreApplication.translate("ImportOptionsDialog", u"Pontos vessz\u0151 (;)", None))
        self.SepComboBox.setItemText(1, QCoreApplication.translate("ImportOptionsDialog", u"Kett\u0151spont (:)", None))
        self.SepComboBox.setItemText(2, QCoreApplication.translate("ImportOptionsDialog", u"Vessz\u0151 (,)", None))
        self.SepComboBox.setItemText(3, QCoreApplication.translate("ImportOptionsDialog", u"Tabul\u00e1tor (\\t)", None))
        self.SepComboBox.setItemText(4, QCoreApplication.translate("ImportOptionsDialog", u"K\u00f6t\u0151jel (-)", None))
        self.SepComboBox.setItemText(5, QCoreApplication.translate("ImportOptionsDialog", u"Al\u00e1h\u00faz\u00e1s (_)", None))
        self.SepComboBox.setItemText(6, QCoreApplication.translate("ImportOptionsDialog", u"Sz\u00f3k\u00f6z ( )", None))
        self.SepComboBox.setItemText(7, QCoreApplication.translate("ImportOptionsDialog", u"F\u00fcgg\u0151leges vonal (|)", None))

#if QT_CONFIG(tooltip)
        self.SepComboBox.setToolTip(QCoreApplication.translate("ImportOptionsDialog", u"Ignor\u00e1lt, ha van valami bele\u00edrva az egy\u00e9b szepar\u00e1tor men\u00fcbe.", None))
#endif // QT_CONFIG(tooltip)
        self.Seplabel.setText(QCoreApplication.translate("ImportOptionsDialog", u"Szepar\u00e1tor karakter:", None))
#if QT_CONFIG(tooltip)
        self.OtherSepLineEdit.setToolTip(QCoreApplication.translate("ImportOptionsDialog", u"A list\u00e1ban nem tal\u00e1lhat\u00f3 szepar\u00e1tor eset\u00e9n kell kit\u00f6lteni.", None))
#endif // QT_CONFIG(tooltip)
        self.OtherSeplabel.setText(QCoreApplication.translate("ImportOptionsDialog", u"Egy\u00e9b Szepar\u00e1tor:", None))
        self.Declabel.setText(QCoreApplication.translate("ImportOptionsDialog", u"Tizedesjel:", None))
        self.DecComboBox.setItemText(0, QCoreApplication.translate("ImportOptionsDialog", u"Pont (.)", None))
        self.DecComboBox.setItemText(1, QCoreApplication.translate("ImportOptionsDialog", u"Vessz\u0151 (,)", None))

#if QT_CONFIG(tooltip)
        self.DecComboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.WaveIsRowCheckBox.setText(QCoreApplication.translate("ImportOptionsDialog", u"A sorok a hull\u00e1mok?", None))
#if QT_CONFIG(tooltip)
        self.TimeSpinBox.setToolTip(QCoreApplication.translate("ImportOptionsDialog", u"H\u00e1nyadik sor/oszlop tartalmazza az id\u0151 b\u00e9lyeget.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.WavelengthSpinBox.setToolTip(QCoreApplication.translate("ImportOptionsDialog", u"H\u00e1nyadik sor/oszlop tartalmazza a hull\u00e1mhosszat.", None))
#endif // QT_CONFIG(tooltip)
        self.TimeLabel.setText(QCoreApplication.translate("ImportOptionsDialog", u"Id\u0151b\u00e9lyeget tartalmaz\u00f3 sor/oszlop:", None))
        self.WavelengthLabel.setText(QCoreApplication.translate("ImportOptionsDialog", u"Hull\u00e1mhosszat tartalmaz\u00f3 sor/oszlop:", None))
        self.ContinueButton.setText(QCoreApplication.translate("ImportOptionsDialog", u"Tov\u00e1bb", None))
    # retranslateUi

