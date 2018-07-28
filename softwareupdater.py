from echmetupdatecheck import ECHMETUpdateCheck
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from softwareinfo import SoftwareInfo


class SoftwareUpdater(QObject):
    def __init__(parent=None):
        QObject.__init__(parent)

    update_check_complete = pyqtSignal(bool, bool, str, tuple, str)

    @pyqtSlot()
    def check_for_update(self):
        success, err, res = self._check_for_update(SoftwareInfo.VERSION_MAJ,
                                                   SoftwareInfo.VERSION_MIN,
                                                   SoftwareInfo.VERSION_REV)

        if not success:
            self.update_check_complete.emit(False, False, err, (), "")

        else:
            if res.status == ECHMETUpdateCheck.UpdateState.UP_TO_DATE:
                self.update_check_complete.emit(True, False, "", (), "")
            else:
                self.update_check_complete.emit(True, True, "",
                                                (res.version.major.value,
                                                 res.version.minor.value,
                                                 res.version.revision.decode('ASCII')),
                                                 res.link)

    def _check_for_update(self, ver_maj, ver_min, ver_rev):
        try:
            checker = ECHMETUpdateCheck('./libECHMETUpdateCheck.so')

            sw = ECHMETUpdateCheck.Software('SignalMixer',
                                            ECHMETUpdateCheck.Version(ver_maj,
                                                                      ver_min,
                                                                      ver_rev))

            success, err, res = checker.check('https://devoid-pointer.net/echmet/eupd_manifest.json',
                                              sw, False)
            return (success, checker.error_to_str(err), res)

        except AttributeError as ex:
            return (False, str(ex), None)
