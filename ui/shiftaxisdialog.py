from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QLocale
from forms.shiftaxiswidget import Ui_ShiftAxisWidget

class ShiftInfo:
    def __init__(self, ref, new):
        self.reference = ref
        self.new = new


class ShiftAxisDialog(QDialog, Ui_ShiftAxisWidget):
    @pyqtSlot()
    def _onRejectClicked(self):
        self.reject()

    @pyqtSlot()
    def _onAcceptClicked(self):
        loc = QLocale()

        refTup = loc.toDouble(self.qle_referenceValue.text())
        if refTup[1] is not True:
            mbox = QMessageBox(QMessageBox.Warning, 'Invalid input',
                               '"reference" value is not a number')
            mbox.exec_()
            return

        newTup = loc.toDouble(self.qle_newValue.text())
        if (newTup[1] is not True):
            mbox = QMessageBox(QMessageBox.Warning, 'Invalid input',
                               '"new" value is not a number')

            mbox.exec_()
            return

        self.shift = ShiftInfo(refTup[0], newTup[0])
        self.accept()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.shift = None

        self.buttonBox.rejected.connect(self._onRejectClicked)
        self.buttonBox.accepted.connect(self._onAcceptClicked)
