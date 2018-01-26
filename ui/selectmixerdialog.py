from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
import forms.selectmixerdialog


class SelectMixerDialog(QDialog, forms.selectmixerdialog.Ui_SelectMixerDialog):
    @pyqtSlot()
    def _onAccept(self):
        self.selectedMixer = self.qcbox_mixerType.currentData()
        self.accept()

    @pyqtSlot(int)
    def _onMixerSelected(self, idx):
        self.qplainTE_mixerDesc.clear()
        if idx < 0:
            return

        data = self.qcbox_mixerType.currentData()
        if data in self._mixerDescriptions:
            self.qplainTE_mixerDesc.appendPlainText(self._mixerDescriptions[data])

    @pyqtSlot()
    def _onReject(self):
        self.selectedMixer = None
        self.reject()
    def _initMixerSelection(self, mixers):
        for m in mixers:
            self.qcbox_mixerType.addItem(m[0], m[0])
            self._mixerDescriptions[m[0]] = m[1]

    def __init__(self, mixers, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._mixerDescriptions = {}
        self._initMixerSelection(mixers)
        self._selectedMixer = None

        self._onMixerSelected(self.qcbox_mixerType.currentIndex())

        self.buttonBox.accepted.connect(self._onAccept)
        self.buttonBox.rejected.connect(self._onReject)
        self.qcbox_mixerType.currentIndexChanged.connect(self._onMixerSelected)
