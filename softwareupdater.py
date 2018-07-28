from echmetupdatecheck import ECHMETUpdateCheck
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from softwareinfo import SoftwareInfo
from softwareupdateresult import SoftwareUpdateResult


class SoftwareUpdater(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checker = ECHMETUpdateCheck('./libECHMETUpdateCheck.so')


    update_check_complete = pyqtSignal(SoftwareUpdateResult)

    @pyqtSlot()
    def check_for_update(self):
        success, err, res = self._check_for_update(SoftwareInfo.VERSION_MAJ,
                                                   SoftwareInfo.VERSION_MIN,
                                                   SoftwareInfo.VERSION_REV)

        if not success:
            st = None
            if ECHMETUpdateCheck.error_type(err) == ECHMETUpdateCheck.ErrorType.NETWORK_ERROR:
                st = SoftwareUpdateResult.State.NETWORK_ERROR
            elif ECHMETUpdateCheck.error_type(err) == ECHMETUpdateCheck.ErrorType.PROCESSING_ERROR:
                st = SoftwareUpdateResult.State.PROCESSING_ERROR
            else:
                st = SoftwareUpdateResult.State.NO_ERROR

            self.update_check_complete.emit(SoftwareUpdateResult(st, False,
                                                                 self.checker.error_to_str(err),
                                                                 0, 0, '', ''))

        else:
            if res.status == ECHMETUpdateCheck.UpdateState.UP_TO_DATE:
                self.update_check_complete.emit(SoftwareUpdateResult(SoftwareUpdateResult.State.NO_ERROR,
                                                                     False,
                                                                     '',
                                                                     0, 0, '', ''))
            elif res.status == ECHMETUpdateCheck.UpdateState.UNKNOWN:
                self.update_check_complete.emit(SoftwareUpdateResult(SoftwareUpdateResult.State.DATA_ERROR,
                                                                     False,
                                                                     self.checker.error_to_str(err),
                                                                     0, 0, '', ''))
            else:
                self.update_check_complete.emit(SoftwareUpdateResult(SoftwareUpdateResult.State.NO_ERROR,
                                                                     True,
                                                                     '',
                                                                     res.version.major.value,
                                                                     res.version.minor.value,
                                                                     res.version.revision.decode('ASCII'),
                                                                     res.link))

    def _check_for_update(self, ver_maj, ver_min, ver_rev):
        sw = ECHMETUpdateCheck.Software('SignalMixer',
                                         ECHMETUpdateCheck.Version(ver_maj,
                                                                   ver_min,
                                                                   ver_rev))
        return self.checker.check('https://devoid-pointer.net/echmet/eupd_manifest.json',
                                  sw, False)
