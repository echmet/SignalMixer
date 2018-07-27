# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkforupdatedialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CheckForUpdateDialog(object):
    def setupUi(self, CheckForUpdateDialog):
        CheckForUpdateDialog.setObjectName("CheckForUpdateDialog")
        CheckForUpdateDialog.resize(518, 420)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CheckForUpdateDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.qvlay_mainWidget = QtWidgets.QVBoxLayout()
        self.qvlay_mainWidget.setObjectName("qvlay_mainWidget")
        self.verticalLayout_2.addLayout(self.qvlay_mainWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.qpb_checkForUpdate = QtWidgets.QPushButton(CheckForUpdateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qpb_checkForUpdate.sizePolicy().hasHeightForWidth())
        self.qpb_checkForUpdate.setSizePolicy(sizePolicy)
        self.qpb_checkForUpdate.setObjectName("qpb_checkForUpdate")
        self.gridLayout.addWidget(self.qpb_checkForUpdate, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CheckForUpdateDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(CheckForUpdateDialog)
        QtCore.QMetaObject.connectSlotsByName(CheckForUpdateDialog)

    def retranslateUi(self, CheckForUpdateDialog):
        _translate = QtCore.QCoreApplication.translate
        CheckForUpdateDialog.setWindowTitle(_translate("CheckForUpdateDialog", "Check for update"))
        self.qpb_checkForUpdate.setText(_translate("CheckForUpdateDialog", "Check for update"))

