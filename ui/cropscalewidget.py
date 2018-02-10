import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from forms.cropscalewidget import Ui_CropScaleWidget
from cropscalepack import CropScalePack


class CropScaleWidget(QWidget, Ui_CropScaleWidget):
    @pyqtSlot()
    def _onCropFromCheckboxToggled(self):
        sender = self.sender()
        self.qdspbox_cropFrom.setEnabled(sender.checkState() == Qt.Checked)
        self._sendCropScalePack()

    @pyqtSlot()
    def _onCropToCheckboxToggled(self):
        sender = self.sender()
        self.qdspbox_cropTo.setEnabled(sender.checkState() == Qt.Checked)

    @pyqtSlot(bool)
    def _onEnableScalingToggled(self, checked):
        self.qdspbox_scaleFrom.setEnabled(checked)
        self.qdspbox_scaleTo.setEnabled(checked)
        self._sendCropScalePack()

    @pyqtSlot()
    def _onScaleFromReset(self):
        self.qdspbox_scaleFrom.setValue(self._defaultXFirst)
        self._sendCropScalePack()

    @pyqtSlot()
    def _onScaleToReset(self):
        self.qdspbox_scaleTo.setValue(self._defaultXLast)
        self._sendCropScalePack()

    @pyqtSlot(float)
    def _onSpinboxValueChanged(self, value):
        self._sendCropScalePack()

    def _sendCropScalePack(self):
        cropFromEnabled = self.qcb_cropFrom.checkState() == Qt.Checked
        cropToEnabled = self.qcb_cropTo.checkState() == Qt.Checked
        cropFrom = self.qdspbox_cropFrom.value()
        cropTo = self.qdspbox_cropTo.value()
        prepend = self.qdspbox_prepend.value()
        append = self.qdspbox_append.value()
        scalingEnabled = self.qcb_enableScaling.checkState() == Qt.Checked
        scaleFrom = self.qdspbox_scaleFrom.value()
        scaleTo = self.qdspbox_scaleTo.value()

        pack = CropScalePack(cropFromEnabled=cropFromEnabled,
                             cropFrom=cropFrom,
                             cropToEnabled=cropToEnabled,
                             cropTo=cropTo,
                             prepend=prepend,
                             append=append,
                             scalingEnabled=scalingEnabled,
                             scaleFrom=scaleFrom,
                             scaleTo=scaleTo)

        self.cropScaleParamsChanged.emit(pack)

    def __init__(self, xFirst, xLast, yZero, xStep, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.isCollapsed = False

        self._defaultXFirst = xFirst
        self._defaultXLast = xLast
        self._fodder = yZero

        self.qdspbox_cropFrom.setMaximum(sys.float_info.max - 1)
        self.qdspbox_cropFrom.setMinimum(-sys.float_info.max + 1)
        self.qdspbox_cropTo.setMaximum(sys.float_info.max - 1)
        self.qdspbox_cropTo.setMinimum(-sys.float_info.max + 1)
        self.qdspbox_cropFrom.setSingleStep(xStep * 10.0)
        self.qdspbox_cropTo.setSingleStep(xStep * 10.0)

        self.qdspbox_prepend.setMaximum(sys.float_info.max - 1)
        self.qdspbox_prepend.setMinimum(-sys.float_info.max + 1)
        self.qdspbox_append.setMaximum(sys.float_info.max - 1)
        self.qdspbox_append.setMinimum(-sys.float_info.max + 1)
        self.qdspbox_prepend.setSingleStep(xStep * 10.0)
        self.qdspbox_append.setSingleStep(xStep * 10.0)

        self.qdspbox_scaleFrom.setMaximum(sys.float_info.max - 1)
        self.qdspbox_scaleFrom.setMinimum(-sys.float_info.max + 1)
        self.qdspbox_scaleTo.setMaximum(sys.float_info.max - 1)
        self.qdspbox_scaleTo.setMinimum(-sys.float_info.max + 1)
        self.qdspbox_scaleFrom.setSingleStep(xStep * 10.0)
        self.qdspbox_scaleTo.setSingleStep(xStep * 10.0)

        self.qcb_cropFrom.setCheckState(Qt.Unchecked)
        self.qcb_cropTo.setCheckState(Qt.Unchecked)
        self.qdspbox_cropFrom.setEnabled(False)
        self.qdspbox_cropTo.setEnabled(False)

        self.qcb_enableScaling.setCheckState(Qt.Unchecked)
        self.qdspbox_scaleFrom.setEnabled(False)
        self.qdspbox_scaleTo.setEnabled(False)

        self.qdspbox_cropFrom.setValue(self._defaultXFirst)
        self.qdspbox_cropTo.setValue(self._defaultXLast)
        self.qdspbox_prepend.setValue(self._fodder)
        self.qdspbox_append.setValue(self._fodder)
        self.qdspbox_scaleFrom.setValue(self._defaultXFirst)
        self.qdspbox_scaleTo.setValue(self._defaultXLast)

        self.qcb_cropFrom.clicked.connect(self._onCropFromCheckboxToggled)
        self.qcb_cropTo.clicked.connect(self._onCropToCheckboxToggled)
        self.qpb_resetScaleFrom.clicked.connect(self._onScaleFromReset)
        self.qpb_resetScaleTo.clicked.connect(self._onScaleToReset)
        self.qcb_enableScaling.clicked.connect(self._onEnableScalingToggled)

        self.qdspbox_cropFrom.valueChanged.connect(self._onSpinboxValueChanged)
        self.qdspbox_cropTo.valueChanged.connect(self._onSpinboxValueChanged)
        self.qdspbox_prepend.valueChanged.connect(self._onSpinboxValueChanged)
        self.qdspbox_append.valueChanged.connect(self._onSpinboxValueChanged)
        self.qdspbox_scaleFrom.valueChanged.connect(self._onSpinboxValueChanged)
        self.qdspbox_scaleTo.valueChanged.connect(self._onSpinboxValueChanged)

    cropScaleParamsChanged = pyqtSignal(CropScalePack)

    def collapse(self):
        self.qgbox_crop.setVisible(False)
        self.qgbox_scale.setVisible(False)
        self.isCollapsed = True

    def expand(self):
        self.qgbox_crop.setVisible(True)
        self.qgbox_scale.setVisible(True)
        self.isCollapsed = False
