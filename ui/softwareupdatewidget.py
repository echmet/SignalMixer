from PyQt5.QtWidgets import QWidget
import forms.softwareupdatewidget
from softwareinfo import SoftwareInfo


class SoftwareUpdateWidget(QWidget, forms.softwareupdatewidget.Ui_SoftwareUpdateWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ql_result.setText("Update check has not been done yet")
        self.ql_extraInfo.setText("")
        self.ql_link.setText("")
        self.ql_newVersion.setText("(N/A)")
        self.ql_currentVersion.setText(SoftwareInfo.versionString())

    def setDisplay(self, result, extra_info, ver_str, link):
        self.ql_result.setText(result)
        self.ql_extraInfo.setText(extra_info)
        self.ql_newVersion.setText(ver_str)
        self.ql_link.setText(link)

    def updateInProgress(self):
        self.ql_extraInfo.setText("Checking for update...")
        self.ql_newVersion.setText("")
        self.ql_link.setText("")
