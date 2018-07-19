import platform
from signaltrace import SignalTrace, InvalidSignalError
from signaltraceloader import SignalTraceLoaderError, NoDataError
from signaltraceloaderdbus import SignalTraceLoaderDBus
from signaltraceloaderlocalsocket import SignalTraceLoaderLocalSocket
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox


class UnsupportedPlatformError(SignalTraceLoaderError):
    def __init__(self):
        super().__init__('Unsupported platform')


class SignalTraceLoaderDelegate(QObject):
    def __init__(self, loader, parent=None):
        super().__init__(parent)
        self._loader = loader

    def supportedFileFormats(self):
        try:
            return self._loader.supportedFileFormats()
        except SignalTraceLoaderError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'Failed to get supported file types', str(ex))
            mbox.exec_()
            return []

    @pyqtSlot(str, int, str)
    def onLoadSignal(self, tag, option, hintpath):
        try:
            siglist = self._loader.loadSignal(tag, option, hintpath)
            if siglist is not False:
                for sig in siglist:
                    self.signalLoaded.emit(sig)
        except NoDataError:
            return
        except SignalTraceLoaderError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'Failed to load signal', str(ex))
            mbox.exec_()
        except InvalidSignalError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'Loaded signal is invalid', str(ex))
            mbox.exec_()

    signalLoaded = pyqtSignal(SignalTrace)


def makeSignalLoaderDelegate(loaderLauncher):
    os = platform.system()

    if os == 'Linux':
        if SignalTraceLoaderDBus.serviceAvailable() is True:
            return SignalTraceLoaderDelegate(SignalTraceLoaderDBus(loaderLauncher))
        return SignalTraceLoaderDelegate(SignalTraceLoaderLocalSocket(loaderLauncher))
    elif os == 'Windows':
        return SignalTraceLoaderDelegate(SignalTraceLoaderLocalSocket(loaderLauncher))
    else:
        raise UnsupportedPlatformError


def serviceAvailable():
    os = platform.system()

    if os == 'Linux':
        if SignalTraceLoaderDBus.serviceAvailable() is True:
            return True
        return SignalTraceLoaderLocalSocket.serviceAvailable()
    elif os == 'Windows':
        return SignalTraceLoaderLocalSocket.serviceAvailable()
    else:
        raise UnsupportedPlatformError
