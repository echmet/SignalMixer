# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cropscalewidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CropScaleWidget(object):
    def setupUi(self, CropScaleWidget):
        CropScaleWidget.setObjectName("CropScaleWidget")
        CropScaleWidget.resize(433, 366)
        self.verticalLayout = QtWidgets.QVBoxLayout(CropScaleWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.qgbox_crop = QtWidgets.QGroupBox(CropScaleWidget)
        self.qgbox_crop.setObjectName("qgbox_crop")
        self.gridLayout = QtWidgets.QGridLayout(self.qgbox_crop)
        self.gridLayout.setObjectName("gridLayout")
        self.qdspbox_cropFrom = QtWidgets.QDoubleSpinBox(self.qgbox_crop)
        self.qdspbox_cropFrom.setDecimals(4)
        self.qdspbox_cropFrom.setObjectName("qdspbox_cropFrom")
        self.gridLayout.addWidget(self.qdspbox_cropFrom, 2, 1, 1, 1)
        self.ql_cropEnabled = QtWidgets.QLabel(self.qgbox_crop)
        self.ql_cropEnabled.setObjectName("ql_cropEnabled")
        self.gridLayout.addWidget(self.ql_cropEnabled, 0, 2, 1, 1)
        self.qdspbox_cropTo = QtWidgets.QDoubleSpinBox(self.qgbox_crop)
        self.qdspbox_cropTo.setObjectName("qdspbox_cropTo")
        self.gridLayout.addWidget(self.qdspbox_cropTo, 3, 1, 1, 1)
        self.ql_prepend = QtWidgets.QLabel(self.qgbox_crop)
        self.ql_prepend.setObjectName("ql_prepend")
        self.gridLayout.addWidget(self.ql_prepend, 4, 0, 1, 1)
        self.ql_append = QtWidgets.QLabel(self.qgbox_crop)
        self.ql_append.setObjectName("ql_append")
        self.gridLayout.addWidget(self.ql_append, 5, 0, 1, 1)
        self.qdspbox_prepend = QtWidgets.QDoubleSpinBox(self.qgbox_crop)
        self.qdspbox_prepend.setObjectName("qdspbox_prepend")
        self.gridLayout.addWidget(self.qdspbox_prepend, 4, 1, 1, 1)
        self.ql_cropFrom = QtWidgets.QLabel(self.qgbox_crop)
        self.ql_cropFrom.setObjectName("ql_cropFrom")
        self.gridLayout.addWidget(self.ql_cropFrom, 2, 0, 1, 1)
        self.qcb_cropTo = QtWidgets.QCheckBox(self.qgbox_crop)
        self.qcb_cropTo.setText("")
        self.qcb_cropTo.setObjectName("qcb_cropTo")
        self.gridLayout.addWidget(self.qcb_cropTo, 3, 2, 1, 1)
        self.qcb_cropFrom = QtWidgets.QCheckBox(self.qgbox_crop)
        self.qcb_cropFrom.setText("")
        self.qcb_cropFrom.setObjectName("qcb_cropFrom")
        self.gridLayout.addWidget(self.qcb_cropFrom, 2, 2, 1, 1)
        self.ql_cropTo = QtWidgets.QLabel(self.qgbox_crop)
        self.ql_cropTo.setObjectName("ql_cropTo")
        self.gridLayout.addWidget(self.ql_cropTo, 3, 0, 1, 1)
        self.qdspbox_append = QtWidgets.QDoubleSpinBox(self.qgbox_crop)
        self.qdspbox_append.setObjectName("qdspbox_append")
        self.gridLayout.addWidget(self.qdspbox_append, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.qgbox_crop)
        self.qgbox_scale = QtWidgets.QGroupBox(CropScaleWidget)
        self.qgbox_scale.setObjectName("qgbox_scale")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.qgbox_scale)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qcb_enableScaling = QtWidgets.QCheckBox(self.qgbox_scale)
        self.qcb_enableScaling.setObjectName("qcb_enableScaling")
        self.gridLayout_2.addWidget(self.qcb_enableScaling, 0, 0, 1, 3)
        self.qdspbox_scaleFrom = QtWidgets.QDoubleSpinBox(self.qgbox_scale)
        self.qdspbox_scaleFrom.setObjectName("qdspbox_scaleFrom")
        self.gridLayout_2.addWidget(self.qdspbox_scaleFrom, 2, 1, 1, 1)
        self.qpb_resetScaleFrom = QtWidgets.QPushButton(self.qgbox_scale)
        self.qpb_resetScaleFrom.setObjectName("qpb_resetScaleFrom")
        self.gridLayout_2.addWidget(self.qpb_resetScaleFrom, 2, 2, 1, 1)
        self.qdspbox_scaleTo = QtWidgets.QDoubleSpinBox(self.qgbox_scale)
        self.qdspbox_scaleTo.setObjectName("qdspbox_scaleTo")
        self.gridLayout_2.addWidget(self.qdspbox_scaleTo, 3, 1, 1, 1)
        self.qpb_resetScaleTo = QtWidgets.QPushButton(self.qgbox_scale)
        self.qpb_resetScaleTo.setObjectName("qpb_resetScaleTo")
        self.gridLayout_2.addWidget(self.qpb_resetScaleTo, 3, 2, 1, 1)
        self.ql_scaleTo = QtWidgets.QLabel(self.qgbox_scale)
        self.ql_scaleTo.setObjectName("ql_scaleTo")
        self.gridLayout_2.addWidget(self.ql_scaleTo, 3, 0, 1, 1)
        self.ql_scaleFrom = QtWidgets.QLabel(self.qgbox_scale)
        self.ql_scaleFrom.setObjectName("ql_scaleFrom")
        self.gridLayout_2.addWidget(self.ql_scaleFrom, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.qgbox_scale)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(CropScaleWidget)
        QtCore.QMetaObject.connectSlotsByName(CropScaleWidget)

    def retranslateUi(self, CropScaleWidget):
        _translate = QtCore.QCoreApplication.translate
        CropScaleWidget.setWindowTitle(_translate("CropScaleWidget", "Form"))
        self.qgbox_crop.setTitle(_translate("CropScaleWidget", "Crop"))
        self.ql_cropEnabled.setText(_translate("CropScaleWidget", "Enabled"))
        self.ql_prepend.setText(_translate("CropScaleWidget", "Prepend"))
        self.ql_append.setText(_translate("CropScaleWidget", "Append"))
        self.ql_cropFrom.setText(_translate("CropScaleWidget", "From"))
        self.ql_cropTo.setText(_translate("CropScaleWidget", "To"))
        self.qgbox_scale.setTitle(_translate("CropScaleWidget", "Scale"))
        self.qcb_enableScaling.setText(_translate("CropScaleWidget", "Enable scaling"))
        self.qpb_resetScaleFrom.setText(_translate("CropScaleWidget", "Reset"))
        self.qpb_resetScaleTo.setText(_translate("CropScaleWidget", "Reset"))
        self.ql_scaleTo.setText(_translate("CropScaleWidget", "To"))
        self.ql_scaleFrom.setText(_translate("CropScaleWidget", "From"))
