# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 212)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ql_swName = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.ql_swName.setFont(font)
        self.ql_swName.setAlignment(QtCore.Qt.AlignCenter)
        self.ql_swName.setObjectName("ql_swName")
        self.verticalLayout.addWidget(self.ql_swName)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ql_versionCaption = QtWidgets.QLabel(AboutDialog)
        self.ql_versionCaption.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ql_versionCaption.setObjectName("ql_versionCaption")
        self.horizontalLayout.addWidget(self.ql_versionCaption)
        self.ql_versionTag = QtWidgets.QLabel(AboutDialog)
        self.ql_versionTag.setObjectName("ql_versionTag")
        self.horizontalLayout.addWidget(self.ql_versionTag)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ql_echmetLogo = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.ql_echmetLogo.sizePolicy().hasHeightForWidth())
        self.ql_echmetLogo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ql_echmetLogo.setFont(font)
        self.ql_echmetLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.ql_echmetLogo.setObjectName("ql_echmetLogo")
        self.verticalLayout.addWidget(self.ql_echmetLogo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.ql_swName.setText(_translate("AboutDialog", "Signal mixer"))
        self.ql_versionCaption.setText(_translate("AboutDialog", "Version: "))
        self.ql_versionTag.setText(_translate("AboutDialog", "<PLACEHOLDER>"))
        self.ql_echmetLogo.setText(_translate("AboutDialog", "<ECHMET_LOGO>"))

