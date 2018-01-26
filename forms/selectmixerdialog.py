# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectmixerdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectMixerDialog(object):
    def setupUi(self, SelectMixerDialog):
        SelectMixerDialog.setObjectName("SelectMixerDialog")
        SelectMixerDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectMixerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ql_mixerType = QtWidgets.QLabel(SelectMixerDialog)
        self.ql_mixerType.setObjectName("ql_mixerType")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ql_mixerType)
        self.qcbox_mixerType = QtWidgets.QComboBox(SelectMixerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qcbox_mixerType.sizePolicy().hasHeightForWidth())
        self.qcbox_mixerType.setSizePolicy(sizePolicy)
        self.qcbox_mixerType.setObjectName("qcbox_mixerType")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.qcbox_mixerType)
        self.qplainTE_mixerDesc = QtWidgets.QPlainTextEdit(SelectMixerDialog)
        self.qplainTE_mixerDesc.setReadOnly(True)
        self.qplainTE_mixerDesc.setObjectName("qplainTE_mixerDesc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.qplainTE_mixerDesc)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SelectMixerDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectMixerDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectMixerDialog)

    def retranslateUi(self, SelectMixerDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectMixerDialog.setWindowTitle(_translate("SelectMixerDialog", "Select mixer"))
        self.ql_mixerType.setText(_translate("SelectMixerDialog", "Mixer type"))

