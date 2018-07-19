from PyQt5.QtWidgets import QDialog, QStyle
from PyQt5.QtGui import QIcon
import forms.ediiconnectionerrordialog
import platform


class EDIIConnectionErrorDialog(QDialog, forms.ediiconnectionerrordialog.Ui_EDIIConnectionErrorDialog):
    def __init__(self, error, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        if platform.system() == 'Linux':
            pix = QIcon.fromTheme("dialog-error").pixmap(64, 64)
            self.ql_icon.setPixmap(pix)
        else:
            pix = self.style().standardIcon(QStyle.SP_MessageBoxCritical).pixmap(64, 64)
            self.ql_icon.setPixmap(pix)

        self.ql_info.setText(('Failed to connect to EDII service.\n'
                              'Error reported: {}').format(error))

        self.buttonBox.accepted.connect(self.accept)
