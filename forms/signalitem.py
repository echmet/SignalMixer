# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signalitem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignalItem(object):
    def setupUi(self, SignalItem):
        SignalItem.setObjectName("SignalItem")
        SignalItem.resize(545, 298)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignalItem.sizePolicy().hasHeightForWidth())
        SignalItem.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignalItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ql_dataSource = QtWidgets.QLabel(SignalItem)
        self.ql_dataSource.setObjectName("ql_dataSource")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ql_dataSource)
        self.qle_dataSource = QtWidgets.QLineEdit(SignalItem)
        self.qle_dataSource.setEnabled(True)
        self.qle_dataSource.setReadOnly(True)
        self.qle_dataSource.setObjectName("qle_dataSource")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.qle_dataSource)
        self.ql_dataID = QtWidgets.QLabel(SignalItem)
        self.ql_dataID.setObjectName("ql_dataID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ql_dataID)
        self.qle_dataID = QtWidgets.QLineEdit(SignalItem)
        self.qle_dataID.setReadOnly(True)
        self.qle_dataID.setObjectName("qle_dataID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qle_dataID)
        self.ql_customID = QtWidgets.QLabel(SignalItem)
        self.ql_customID.setObjectName("ql_customID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ql_customID)
        self.qle_customID = QtWidgets.QLineEdit(SignalItem)
        self.qle_customID.setObjectName("qle_customID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.qle_customID)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(SignalItem)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.qpb_collapseExpandButton = CollapseExpandButton(SignalItem)
        self.qpb_collapseExpandButton.setText("")
        self.qpb_collapseExpandButton.setObjectName("qpb_collapseExpandButton")
        self.horizontalLayout_2.addWidget(self.qpb_collapseExpandButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.qpb_show = QtWidgets.QPushButton(SignalItem)
        self.qpb_show.setObjectName("qpb_show")
        self.horizontalLayout_2.addWidget(self.qpb_show)
        self.qpb_remove = QtWidgets.QPushButton(SignalItem)
        self.qpb_remove.setObjectName("qpb_remove")
        self.horizontalLayout_2.addWidget(self.qpb_remove)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SignalItem)
        QtCore.QMetaObject.connectSlotsByName(SignalItem)

    def retranslateUi(self, SignalItem):
        _translate = QtCore.QCoreApplication.translate
        SignalItem.setWindowTitle(_translate("SignalItem", "Form"))
        self.ql_dataSource.setText(_translate("SignalItem", "Data source"))
        self.ql_dataID.setText(_translate("SignalItem", "Data ID"))
        self.ql_customID.setText(_translate("SignalItem", "Custom ID"))
        self.label.setText(_translate("SignalItem", "Transformations:"))
        self.qpb_show.setText(_translate("SignalItem", "Show"))
        self.qpb_remove.setText(_translate("SignalItem", "Remove"))

from ui.collapseexpandbutton import CollapseExpandButton
