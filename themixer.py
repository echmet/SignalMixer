#! /usr/bin/python3
import sys
from signaltraceloader import SignalTraceLoaderError
import signaltraceloaderfactory
from PyQt5.QtWidgets import QApplication, QMessageBox
from ui.mainwindow import MainWindow
from signaltracemodel import SignalTraceModel
import loaderlauncher


def main(argv):
    qApp = QApplication(argv)
    sigLoader = None
    supportedFileFormats = None
    sigModel = SignalTraceModel()

    ldrPath = argv[1] if len(argv) > 1 else ''

    ldrLauncher = loaderlauncher.LoaderLauncher(ldrPath)

    try:
        ldrLauncher.launch()
    except loaderlauncher.LoaderLauncherError as ex:
        mbox = QMessageBox(QMessageBox.Critical, 'Loader service error', str(ex))
        mbox.exec_()
        sys.exit(1)

    try:
        sigLoader = signaltraceloaderfactory.makeSignalLoaderDelegate(ldrLauncher)
        supportedFileFormats = sigLoader.supportedFileFormats()
        mWin = MainWindow(supportedFileFormats, sigModel)

        sigLoader.signalLoaded.connect(sigModel.onSignalLoaded)
    except SignalTraceLoaderError as ex:
        mbox = QMessageBox(QMessageBox.Critical, 'Cannot initialize signal loader', str(ex))
        mbox.exec_()
        ldrLauncher.terminate()
        sys.exit(1)

    mWin.loadSignal.connect(sigLoader.onLoadSignal)
    mWin.show()

    ret = qApp.exec_()
    ldrLauncher.terminate()

    return ret


if __name__ == "__main__":
    main(sys.argv)
