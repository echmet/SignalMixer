# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(947, 803)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qpb_addSignal = QtWidgets.QPushButton(MainForm)
        self.qpb_addSignal.setObjectName("qpb_addSignal")
        self.horizontalLayout.addWidget(self.qpb_addSignal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.qhlay_mainPanel = QtWidgets.QHBoxLayout()
        self.qhlay_mainPanel.setObjectName("qhlay_mainPanel")
        self.qscrArea_addedSignals = QtWidgets.QScrollArea(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qscrArea_addedSignals.sizePolicy().hasHeightForWidth())
        self.qscrArea_addedSignals.setSizePolicy(sizePolicy)
        self.qscrArea_addedSignals.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.qscrArea_addedSignals.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.qscrArea_addedSignals.setWidgetResizable(False)
        self.qscrArea_addedSignals.setObjectName("qscrArea_addedSignals")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 460, 703))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.qscrArea_addedSignals.setWidget(self.scrollAreaWidgetContents)
        self.qhlay_mainPanel.addWidget(self.qscrArea_addedSignals)
        self.qtabw_signalsViews = QtWidgets.QTabWidget(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtabw_signalsViews.sizePolicy().hasHeightForWidth())
        self.qtabw_signalsViews.setSizePolicy(sizePolicy)
        self.qtabw_signalsViews.setObjectName("qtabw_signalsViews")
        self.singleSignal = QtWidgets.QWidget()
        self.singleSignal.setObjectName("singleSignal")
        self.qtabw_signalsViews.addTab(self.singleSignal, "")
        self.allSignals = QtWidgets.QWidget()
        self.allSignals.setObjectName("allSignals")
        self.qtabw_signalsViews.addTab(self.allSignals, "")
        self.qhlay_mainPanel.addWidget(self.qtabw_signalsViews)
        self.verticalLayout.addLayout(self.qhlay_mainPanel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.qpb_exportMixedSignals = QtWidgets.QPushButton(MainForm)
        self.qpb_exportMixedSignals.setObjectName("qpb_exportMixedSignals")
        self.horizontalLayout_2.addWidget(self.qpb_exportMixedSignals)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.qpb_quit = QtWidgets.QPushButton(MainForm)
        self.qpb_quit.setObjectName("qpb_quit")
        self.horizontalLayout_2.addWidget(self.qpb_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MainForm)
        self.qtabw_signalsViews.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.qpb_addSignal.setText(_translate("MainForm", "Add signal"))
        self.qtabw_signalsViews.setTabText(self.qtabw_signalsViews.indexOf(self.singleSignal), _translate("MainForm", "Single signal"))
        self.qtabw_signalsViews.setTabText(self.qtabw_signalsViews.indexOf(self.allSignals), _translate("MainForm", "All signals"))
        self.qpb_exportMixedSignals.setText(_translate("MainForm", "Export mixed signals"))
        self.qpb_quit.setText(_translate("MainForm", "Quit"))

