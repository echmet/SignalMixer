# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xunitinputdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XUnitInputDialog(object):
    def setupUi(self, XUnitInputDialog):
        XUnitInputDialog.setObjectName("XUnitInputDialog")
        XUnitInputDialog.resize(411, 179)
        self.verticalLayout = QtWidgets.QVBoxLayout(XUnitInputDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ql_message = QtWidgets.QLabel(XUnitInputDialog)
        self.ql_message.setWordWrap(True)
        self.ql_message.setObjectName("ql_message")
        self.verticalLayout.addWidget(self.ql_message)
        self.ql_messagePartTwo = QtWidgets.QLabel(XUnitInputDialog)
        self.ql_messagePartTwo.setWordWrap(True)
        self.ql_messagePartTwo.setObjectName("ql_messagePartTwo")
        self.verticalLayout.addWidget(self.ql_messagePartTwo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ql_second = QtWidgets.QLabel(XUnitInputDialog)
        self.ql_second.setObjectName("ql_second")
        self.horizontalLayout.addWidget(self.ql_second)
        self.qle_multiplier = QtWidgets.QLineEdit(XUnitInputDialog)
        self.qle_multiplier.setObjectName("qle_multiplier")
        self.horizontalLayout.addWidget(self.qle_multiplier)
        self.ql_multiply = QtWidgets.QLabel(XUnitInputDialog)
        self.ql_multiply.setObjectName("ql_multiply")
        self.horizontalLayout.addWidget(self.ql_multiply)
        self.ql_unit = QtWidgets.QLabel(XUnitInputDialog)
        self.ql_unit.setObjectName("ql_unit")
        self.horizontalLayout.addWidget(self.ql_unit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(XUnitInputDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(XUnitInputDialog)
        QtCore.QMetaObject.connectSlotsByName(XUnitInputDialog)

    def retranslateUi(self, XUnitInputDialog):
        _translate = QtCore.QCoreApplication.translate
        XUnitInputDialog.setWindowTitle(_translate("XUnitInputDialog", "Set X axis unit ratio"))
        self.ql_message.setText(_translate("XUnitInputDialog", "<PLACEHOLDER>"))
        self.ql_messagePartTwo.setText(_translate("XUnitInputDialog", "Please provide the conversion ratio of the X axis unit to seconds manually."))
        self.ql_second.setText(_translate("XUnitInputDialog", "[second] = "))
        self.ql_multiply.setText(_translate("XUnitInputDialog", "*"))
        self.ql_unit.setText(_translate("XUnitInputDialog", "<UNIT>"))

