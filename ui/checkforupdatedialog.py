from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
import forms.checkforupdatedialog
from ui.softwareupdatewidget import SoftwareUpdateWidget
from softwareinfo import SoftwareInfo
from softwareupdateresult import SoftwareUpdateResult


class CheckForUpdateDialog(QDialog,
                           forms.checkforupdatedialog.Ui_CheckForUpdateDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.swuw = SoftwareUpdateWidget()
        self.qvlay_mainWidget.addWidget(self.swuw)

        self.buttonBox.rejected.connect(self.close)
        self.qpb_checkForUpdate.clicked.connect(self.on_check_for_update)

    check_for_update = pyqtSignal(bool)

    @pyqtSlot()
    def on_check_for_update(self):
        self.swuw.updateInProgress()
        self.check_for_update.emit(False)

    @pyqtSlot(SoftwareUpdateResult)
    def on_update_check_complete(self, result):
        if result.state != SoftwareUpdateResult.State.NO_ERROR:
            main_text = ''
            if result.state == SoftwareUpdateResult.State.NETWORK_ERROR:
                main_text = 'Network error occured during update check'
            elif result.state == SoftwareUpdateResult.State.DATA_ERROR:
                main_text = 'List of updates contains invalid data'
            else:
                main_text = 'Error occured during update check'
            self.swuw.setDisplay(main_text,
                                 result.extra_info,
                                 '(N/A)', '')
        else:
            if not result.update_available:
                self.swuw.setDisplay('{} is up to date'.format(SoftwareInfo.softwareName()),
                                     '', '(none available)', '')
            else:
                self.swuw.setDisplay('Update for {} is available'.format(SoftwareInfo.softwareName()),
                                     '',
                                     '{0}.{1}{2}'.format(result.new_ver_maj,
                                                         result.new_ver_min,
                                                         result.new_ver_rev),
                                     result.link)
