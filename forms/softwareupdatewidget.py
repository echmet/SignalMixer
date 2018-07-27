# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'softwareupdatewidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SoftwareUpdateWidget(object):
    def setupUi(self, SoftwareUpdateWidget):
        SoftwareUpdateWidget.setObjectName("SoftwareUpdateWidget")
        SoftwareUpdateWidget.resize(331, 229)
        self.verticalLayout = QtWidgets.QVBoxLayout(SoftwareUpdateWidget)
        self.verticalLayout.setContentsMargins(-1, 14, 6, -1)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ql_result = QtWidgets.QLabel(SoftwareUpdateWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ql_result.setFont(font)
        self.ql_result.setAlignment(QtCore.Qt.AlignCenter)
        self.ql_result.setObjectName("ql_result")
        self.verticalLayout.addWidget(self.ql_result)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ql_newVersionCap = QtWidgets.QLabel(SoftwareUpdateWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ql_newVersionCap.setFont(font)
        self.ql_newVersionCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ql_newVersionCap.setObjectName("ql_newVersionCap")
        self.gridLayout.addWidget(self.ql_newVersionCap, 0, 0, 1, 1)
        self.ql_newVersion = QtWidgets.QLabel(SoftwareUpdateWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ql_newVersion.setFont(font)
        self.ql_newVersion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ql_newVersion.setObjectName("ql_newVersion")
        self.gridLayout.addWidget(self.ql_newVersion, 0, 1, 1, 1)
        self.ql_currentVersionCap = QtWidgets.QLabel(SoftwareUpdateWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ql_currentVersionCap.setFont(font)
        self.ql_currentVersionCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ql_currentVersionCap.setObjectName("ql_currentVersionCap")
        self.gridLayout.addWidget(self.ql_currentVersionCap, 1, 0, 1, 1)
        self.ql_currentVersion = QtWidgets.QLabel(SoftwareUpdateWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ql_currentVersion.setFont(font)
        self.ql_currentVersion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ql_currentVersion.setObjectName("ql_currentVersion")
        self.gridLayout.addWidget(self.ql_currentVersion, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.ql_extraInfo = QtWidgets.QLabel(SoftwareUpdateWidget)
        self.ql_extraInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ql_extraInfo.setWordWrap(True)
        self.ql_extraInfo.setObjectName("ql_extraInfo")
        self.verticalLayout.addWidget(self.ql_extraInfo)
        self.ql_link = QtWidgets.QLabel(SoftwareUpdateWidget)
        self.ql_link.setAlignment(QtCore.Qt.AlignCenter)
        self.ql_link.setObjectName("ql_link")
        self.verticalLayout.addWidget(self.ql_link)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(SoftwareUpdateWidget)
        QtCore.QMetaObject.connectSlotsByName(SoftwareUpdateWidget)

    def retranslateUi(self, SoftwareUpdateWidget):
        _translate = QtCore.QCoreApplication.translate
        SoftwareUpdateWidget.setWindowTitle(_translate("SoftwareUpdateWidget", "Form"))
        self.ql_result.setText(_translate("SoftwareUpdateWidget", "<Update check result>"))
        self.ql_newVersionCap.setText(_translate("SoftwareUpdateWidget", "New version"))
        self.ql_newVersion.setText(_translate("SoftwareUpdateWidget", "<Version tag>"))
        self.ql_currentVersionCap.setText(_translate("SoftwareUpdateWidget", "Current version"))
        self.ql_currentVersion.setText(_translate("SoftwareUpdateWidget", "<Version tag>"))
        self.ql_extraInfo.setText(_translate("SoftwareUpdateWidget", "<EXTRA_INFO>"))
        self.ql_link.setText(_translate("SoftwareUpdateWidget", "<Donwload link>"))

