# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shiftaxiswidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShiftAxisWidget(object):
    def setupUi(self, ShiftAxisWidget):
        ShiftAxisWidget.setObjectName("ShiftAxisWidget")
        ShiftAxisWidget.resize(320, 121)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShiftAxisWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ql_referenceValue = QtWidgets.QLabel(ShiftAxisWidget)
        self.ql_referenceValue.setObjectName("ql_referenceValue")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ql_referenceValue)
        self.qle_referenceValue = QtWidgets.QLineEdit(ShiftAxisWidget)
        self.qle_referenceValue.setObjectName("qle_referenceValue")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.qle_referenceValue)
        self.ql_newValue = QtWidgets.QLabel(ShiftAxisWidget)
        self.ql_newValue.setObjectName("ql_newValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ql_newValue)
        self.qle_newValue = QtWidgets.QLineEdit(ShiftAxisWidget)
        self.qle_newValue.setObjectName("qle_newValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qle_newValue)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShiftAxisWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ShiftAxisWidget)
        QtCore.QMetaObject.connectSlotsByName(ShiftAxisWidget)

    def retranslateUi(self, ShiftAxisWidget):
        _translate = QtCore.QCoreApplication.translate
        ShiftAxisWidget.setWindowTitle(_translate("ShiftAxisWidget", "Shift axis"))
        self.ql_referenceValue.setText(_translate("ShiftAxisWidget", "Reference value"))
        self.ql_newValue.setText(_translate("ShiftAxisWidget", "New value"))

