from PyQt5.QtWidgets import QDialog
import forms.aboutdialog
import softwareinfo


class AboutDialog(QDialog, forms.aboutdialog.Ui_AboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ql_versionTag.setText(softwareinfo.SoftwareInfo.versionString())
        self.ql_echmetLogo.setText('')
        self.ql_echmetLogo.setPixmap(softwareinfo.SoftwareInfo.echmetLogo().scaledToWidth(100))

        self.buttonBox.accepted.connect(self.accept)
