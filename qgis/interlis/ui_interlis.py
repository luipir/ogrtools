# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interlis.ui'
#
# Created: Wed Feb 19 14:20:22 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Interlis(object):
    def setupUi(self, Interlis):
        Interlis.setObjectName(_fromUtf8("Interlis"))
        Interlis.resize(406, 345)
        self.gridLayout_2 = QtGui.QGridLayout(Interlis)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Interlis)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.transfertab = QtGui.QWidget()
        self.transfertab.setObjectName(_fromUtf8("transfertab"))
        self.gridLayout = QtGui.QGridLayout(self.transfertab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mDataLineEdit = QtGui.QLineEdit(self.transfertab)
        self.mDataLineEdit.setObjectName(_fromUtf8("mDataLineEdit"))
        self.gridLayout.addWidget(self.mDataLineEdit, 0, 1, 1, 1)
        self.mConfigButton = QtGui.QPushButton(self.transfertab)
        self.mConfigButton.setEnabled(True)
        self.mConfigButton.setObjectName(_fromUtf8("mConfigButton"))
        self.gridLayout.addWidget(self.mConfigButton, 4, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.transfertab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.mModelLineEdit = QtGui.QLineEdit(self.transfertab)
        self.mModelLineEdit.setObjectName(_fromUtf8("mModelLineEdit"))
        self.gridLayout.addWidget(self.mModelLineEdit, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.transfertab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.cbDbConnections = QtGui.QComboBox(self.transfertab)
        self.cbDbConnections.setObjectName(_fromUtf8("cbDbConnections"))
        self.cbDbConnections.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbDbConnections, 3, 1, 1, 1)
        self.mDataFileLabel = QtGui.QLabel(self.transfertab)
        self.mDataFileLabel.setObjectName(_fromUtf8("mDataFileLabel"))
        self.gridLayout.addWidget(self.mDataFileLabel, 0, 0, 1, 1)
        self.mModelFileButton = QtGui.QPushButton(self.transfertab)
        self.mModelFileButton.setObjectName(_fromUtf8("mModelFileButton"))
        self.gridLayout.addWidget(self.mModelFileButton, 2, 2, 1, 1)
        self.mDataFileButton = QtGui.QPushButton(self.transfertab)
        self.mDataFileButton.setObjectName(_fromUtf8("mDataFileButton"))
        self.gridLayout.addWidget(self.mDataFileButton, 0, 2, 1, 1)
        self.mConfigLineEdit = QtGui.QLineEdit(self.transfertab)
        self.mConfigLineEdit.setObjectName(_fromUtf8("mConfigLineEdit"))
        self.gridLayout.addWidget(self.mConfigLineEdit, 4, 1, 1, 1)
        self.mModelFileLabel = QtGui.QLabel(self.transfertab)
        self.mModelFileLabel.setObjectName(_fromUtf8("mModelFileLabel"))
        self.gridLayout.addWidget(self.mModelFileLabel, 2, 0, 1, 1)
        self.frame = QtGui.QFrame(self.transfertab)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 3, 2, 1, 1)
        self.mImportButton = QtGui.QPushButton(self.frame)
        self.mImportButton.setEnabled(False)
        self.mImportButton.setObjectName(_fromUtf8("mImportButton"))
        self.gridLayout_3.addWidget(self.mImportButton, 2, 0, 2, 1)
        self.cbResetData = QtGui.QCheckBox(self.frame)
        self.cbResetData.setChecked(True)
        self.cbResetData.setObjectName(_fromUtf8("cbResetData"))
        self.gridLayout_3.addWidget(self.cbResetData, 1, 0, 1, 1)
        self.cbImportEnums = QtGui.QCheckBox(self.frame)
        self.cbImportEnums.setChecked(True)
        self.cbImportEnums.setObjectName(_fromUtf8("cbImportEnums"))
        self.gridLayout_3.addWidget(self.cbImportEnums, 0, 0, 1, 1)
        self.mExportButton = QtGui.QPushButton(self.frame)
        self.mExportButton.setEnabled(False)
        self.mExportButton.setObjectName(_fromUtf8("mExportButton"))
        self.gridLayout_3.addWidget(self.mExportButton, 2, 1, 2, 1)
        self.gridLayout.addWidget(self.frame, 6, 0, 1, 3)
        self.mModelLookupButton = QtGui.QPushButton(self.transfertab)
        self.mModelLookupButton.setObjectName(_fromUtf8("mModelLookupButton"))
        self.gridLayout.addWidget(self.mModelLookupButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.transfertab, _fromUtf8(""))
        self.settingstab = QtGui.QWidget()
        self.settingstab.setObjectName(_fromUtf8("settingstab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.settingstab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_2 = QtGui.QFrame(self.settingstab)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout = QtGui.QFormLayout(self.frame_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.cbSkipFailures = QtGui.QCheckBox(self.frame_2)
        self.cbSkipFailures.setChecked(True)
        self.cbSkipFailures.setObjectName(_fromUtf8("cbSkipFailures"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbSkipFailures)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.settingstab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label_5.setBuddy(self.mConfigLineEdit)
        self.label.setBuddy(self.cbDbConnections)
        self.mDataFileLabel.setBuddy(self.mDataLineEdit)
        self.mModelFileLabel.setBuddy(self.mModelLineEdit)
        self.label_3.setBuddy(self.lineEdit)
        self.label_4.setBuddy(self.lineEdit_2)

        self.retranslateUi(Interlis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Interlis.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Interlis.reject)
        QtCore.QMetaObject.connectSlotsByName(Interlis)
        Interlis.setTabOrder(self.tabWidget, self.mDataFileButton)
        Interlis.setTabOrder(self.mDataFileButton, self.mModelFileButton)
        Interlis.setTabOrder(self.mModelFileButton, self.mImportButton)
        Interlis.setTabOrder(self.mImportButton, self.mExportButton)
        Interlis.setTabOrder(self.mExportButton, self.buttonBox)
        Interlis.setTabOrder(self.buttonBox, self.mConfigButton)
        Interlis.setTabOrder(self.mConfigButton, self.mConfigLineEdit)
        Interlis.setTabOrder(self.mConfigLineEdit, self.lineEdit)
        Interlis.setTabOrder(self.lineEdit, self.lineEdit_2)
        Interlis.setTabOrder(self.lineEdit_2, self.cbDbConnections)
        Interlis.setTabOrder(self.cbDbConnections, self.mDataLineEdit)
        Interlis.setTabOrder(self.mDataLineEdit, self.mModelLineEdit)

    def retranslateUi(self, Interlis):
        Interlis.setWindowTitle(QtGui.QApplication.translate("Interlis", "Interlis", None, QtGui.QApplication.UnicodeUTF8))
        self.mConfigButton.setText(QtGui.QApplication.translate("Interlis", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Interlis", "OGR Config.:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Interlis", "Speicherort:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDbConnections.setItemText(0, QtGui.QApplication.translate("Interlis", "QGIS Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.mDataFileLabel.setText(QtGui.QApplication.translate("Interlis", "Transferfile:", None, QtGui.QApplication.UnicodeUTF8))
        self.mModelFileButton.setText(QtGui.QApplication.translate("Interlis", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mDataFileButton.setText(QtGui.QApplication.translate("Interlis", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mModelFileLabel.setText(QtGui.QApplication.translate("Interlis", "IlisMeta Modell:", None, QtGui.QApplication.UnicodeUTF8))
        self.mImportButton.setText(QtGui.QApplication.translate("Interlis", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.cbResetData.setText(QtGui.QApplication.translate("Interlis", "Daten ersetzen", None, QtGui.QApplication.UnicodeUTF8))
        self.cbImportEnums.setText(QtGui.QApplication.translate("Interlis", "Import Enums", None, QtGui.QApplication.UnicodeUTF8))
        self.mExportButton.setText(QtGui.QApplication.translate("Interlis", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.mModelLookupButton.setText(QtGui.QApplication.translate("Interlis", "Modell Lookup", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transfertab), QtGui.QApplication.translate("Interlis", "Import/Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Interlis", "Model Repositories:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Interlis", "http://models.interlis.ch/", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Interlis", "IlisMeta Lookup:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("Interlis", "http://interlis.sourcepole.ch/ilismeta", None, QtGui.QApplication.UnicodeUTF8))
        self.cbSkipFailures.setText(QtGui.QApplication.translate("Interlis", "Fehler überspringen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingstab), QtGui.QApplication.translate("Interlis", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))

