from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QLocale
from forms.xunitinputdialog import Ui_XUnitInputDialog


class XUnitInputDialog(QDialog, Ui_XUnitInputDialog):
    def _onAccepted(self):
        loc = QLocale()
        ret = loc.toDouble(self.qle_multiplier.text())

        if not ret[1]:
            mbox = QMessageBox(QMessageBox.Warning, 'Invalid input', 'Entered data cannot be converted to number')
            mbox.exec_()
            return

        if ret[0] <= 0.0:
            mbox = QMessageBox(QMessageBox.Warning, 'Invalid input', 'Convertion ratio must be positive')
            mbox.exec_()
            return

        self._multiplier = ret[0]
        self.accept()

    def __init__(self, xUnit, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._multiplier = -1

        self.ql_message.setText('X axis unit "{}" was not recognized'.format(xUnit))
        self.ql_unit.setText(xUnit)
        self.buttonBox.accepted.connect(self._onAccepted)

    def multiplier(self):
        return self._multiplier
