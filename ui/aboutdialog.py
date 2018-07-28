from PyQt5.QtWidgets import QDialog
import forms.aboutdialog
from softwareinfo import SoftwareInfo

ECHMET_LINK = 'http://echmet.natur.cuni.cz'

class AboutDialog(QDialog, forms.aboutdialog.Ui_AboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ql_swName.setText(SoftwareInfo.softwareName())
        self.ql_versionTag.setText(SoftwareInfo.versionString())
        self.ql_echmetLogo.setText('')
        self.ql_echmetLogo.setPixmap(SoftwareInfo.echmetLogo().scaledToWidth(100))

        self.ql_echmetLink.setText('<a href="{0}">{0}</a>'.format(ECHMET_LINK))
        self.ql_echmetLink.setOpenExternalLinks(True)

        self.buttonBox.accepted.connect(self.accept)
