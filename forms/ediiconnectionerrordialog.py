# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ediiconnectionerrordialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EDIIConnectionErrorDialog(object):
    def setupUi(self, EDIIConnectionErrorDialog):
        EDIIConnectionErrorDialog.setObjectName("EDIIConnectionErrorDialog")
        EDIIConnectionErrorDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(EDIIConnectionErrorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ql_icon = QtWidgets.QLabel(EDIIConnectionErrorDialog)
        self.ql_icon.setObjectName("ql_icon")
        self.horizontalLayout.addWidget(self.ql_icon)
        self.label = QtWidgets.QLabel(EDIIConnectionErrorDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ql_info = QtWidgets.QLabel(EDIIConnectionErrorDialog)
        self.ql_info.setObjectName("ql_info")
        self.verticalLayout.addWidget(self.ql_info)
        self.buttonBox = QtWidgets.QDialogButtonBox(EDIIConnectionErrorDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EDIIConnectionErrorDialog)
        QtCore.QMetaObject.connectSlotsByName(EDIIConnectionErrorDialog)

    def retranslateUi(self, EDIIConnectionErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        EDIIConnectionErrorDialog.setWindowTitle(_translate("EDIIConnectionErrorDialog", "EDII connection error"))
        self.ql_icon.setText(_translate("EDIIConnectionErrorDialog", "<ICON>"))
        self.label.setText(_translate("EDIIConnectionErrorDialog", "\"Is there anybody out there, anybody listening to me?\""))
        self.ql_info.setText(_translate("EDIIConnectionErrorDialog", "<PLACEHOLDER>"))

