from PyQt5.QtWidgets import QDialog
import forms.aboutdialog
import softwareinfo

ECHMET_LINK = 'http://echmet.natur.cuni.cz'

class AboutDialog(QDialog, forms.aboutdialog.Ui_AboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ql_versionTag.setText(softwareinfo.SoftwareInfo.versionString())
        self.ql_echmetLogo.setText('')
        self.ql_echmetLogo.setPixmap(softwareinfo.SoftwareInfo.echmetLogo().scaledToWidth(100))

        self.ql_echmetLink.setText('<a href="{0}">{0}</a>'.format(ECHMET_LINK))
        self.ql_echmetLink.setOpenExternalLinks(True)

        self.buttonBox.accepted.connect(self.accept)
