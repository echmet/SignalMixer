from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject
import signaltrace
import hashlib
from cropscalepack import CropScalePack


class SignalTraceModelError(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return self._message

class SignalTraceModel(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._storedSignals = {}

    def adjustSignal(self, identifier, pack):
        if identifier not in self._storedSignals:
            raise SignalTraceModelError('No such signal')

        sig = self._storedSignals[identifier]
        sig.removeCrop(not pack.cropFromEnabled, not pack.cropToEnabled)
        if pack.cropFromEnabled:
            sig.setCropFrom(pack.cropFrom)
        if pack.cropToEnabled:
            sig.setCropTo(pack.cropTo)

        sig.setPrependAppend(pack.prepend, pack.append)
        if not pack.scalingEnabled:
            sig.removeScaling()
        else:
            sig.setScaling(pack.scaleFrom, pack.scaleTo)

    def allSignals(self):
        ret = dict(self._storedSignals)
        return ret

    def getSignal(self, identifier):
        if identifier not in self._storedSignals:
            raise SignalTraceModelError('No such signal')

        return self._storedSignals[identifier]

    def removeSignal(self, identifier):
        if identifier in self._storedSignals:
            del self._storedSignals[identifier]

    def setCustomSignalID(self, identifier, customID):
        if identifier in self._storedSignals:
            self._storedSignals[identifier].customID = customID

    @pyqtSlot(signaltrace.SignalTrace)
    def onSignalLoaded(self, sig):
        m = hashlib.sha256()
        m.update(sig.srcFile.encode('UTF-8'))
        m.update(sig.dataID.encode('UTF-8'))
        identifier = m.hexdigest()

        if identifier in self._storedSignals:
            self.signalLoaded.emit(sig, '')
            return

        sig.customID = sig.srcFile
        if len(sig.dataID) > 0:
            sig.customID += '_' + sig.dataID

        self._storedSignals[identifier] = sig
        self.signalLoaded.emit(sig, identifier)
 
    signalLoaded = pyqtSignal(signaltrace.SignalTrace, str)
