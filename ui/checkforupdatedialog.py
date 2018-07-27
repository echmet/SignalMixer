from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
import forms.checkforupdatedialog
from ui.softwareupdatewidget import SoftwareUpdateWidget
from softwareinfo import SoftwareInfo


class CheckForUpdateDialog(QDialog,
                           forms.checkforupdatedialog.Ui_CheckForUpdateDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.swuw = SoftwareUpdateWidget()
        self.qvlay_mainWidget.addWidget(self.swuw)

        self.buttonBox.rejected.connect(self.close)
        self.qpb_checkForUpdate.clicked.connect(self.on_check_for_update)

    check_for_update = pyqtSignal()

    @pyqtSlot()
    def on_check_for_update(self):
        self.swuw.updateInProgress()
        self.check_for_update.emit()

    @pyqtSlot(bool, bool, str, tuple, str)
    def on_update_check_complete(self, check_ok, update_avail, info, version,
                                 link):
        if not check_ok:
            self.swuw.setDisplay("Error occured during update check",
                                 info,
                                 "(N/A)", "")
        else:
            if not update_avail:
                self.swuw.setDisplay("{} is up to date".format(SoftwareInfo.softwareName()),
                                     "", "(none available)", "")
            else:
                self.swuw.setDisplay("Update for {} is available".format(SoftwareInfo.softwareName()),
                                     "",
                                     "{0}.{1}{2}".format(version[0],
                                                         version[1],
                                                         version[2]),
                                     link)
