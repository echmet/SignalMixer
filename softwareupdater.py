from echmetupdatecheck import ECHMETUpdateCheck
from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
from softwareinfo import SoftwareInfo
from softwareupdateresult import SoftwareUpdateResult


class UpdateWorker(QObject):
    def __init__(self, checker, automatic, parent=None):
        super().__init__(parent)
        self.checker = checker
        self.automatic = automatic

        self.links_to_try = ['https://echmet.natur.cuni.cz/echmet/download/public/eupd_manifest.json',
                             'https://devoid-pointer.net/echmet/eupd_manifest.json'
                             ]

    update_check_complete = pyqtSignal(tuple, bool)

    @pyqtSlot()
    def on_check_for_update(self):
        ret = self._check_for_update()
        self.update_check_complete.emit(ret, self.automatic)

    def _keep_trying(self, data):
        if data[0]:
            return data[2].status == ECHMETUpdateCheck.UpdateState.UNKNOWN
        return True

    def _check_for_update(self):
        sw = ECHMETUpdateCheck.Software('SignalMixer',
                                         ECHMETUpdateCheck.Version(SoftwareInfo.VERSION_MAJ,
                                                                   SoftwareInfo.VERSION_MIN,
                                                                   SoftwareInfo.VERSION_REV))

        ret = None
        for link in self.links_to_try:
            ret = self.checker.check(link, sw, False)
            if not self._keep_trying(ret):
                return ret

        return ret

class SoftwareUpdater(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checker = ECHMETUpdateCheck('./libECHMETUpdateCheck.so')
        self.thr = None
        self.worker = None

    update_check_complete = pyqtSignal(SoftwareUpdateResult)
    automatic_check_complete = pyqtSignal()

    @pyqtSlot(bool)
    def check_for_update(self, automatic):
        if self.thr is not None and self.thr.isRunning():
            return

        self.thr = QThread()
        self.worker = UpdateWorker(self.checker, automatic)

        self.worker.moveToThread(self.thr)
        self.thr.started.connect(self.worker.on_check_for_update)
        self.worker.update_check_complete.connect(self._on_update_check_complete)
        self.worker.update_check_complete.connect(self.thr.quit)

        self.thr.start()

    @pyqtSlot(tuple, bool)
    def _on_update_check_complete(self, result, automatic):
        success, err, res = result

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
            return

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
            if automatic:
                self.automatic_check_complete.emit()
