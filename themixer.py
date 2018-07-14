#! /usr/bin/python3

import sys
from signaltraceloader import SignalTraceLoaderError
import signaltraceloaderfactory
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog
from ui.mainwindow import MainWindow
from signaltracemodel import SignalTraceModel
from configuration import Configuration
import loaderlauncher
import os.path


def check_edii_valid(config):
    path = config.get_value('edii_path')

    if path is None or os.path.isfile(path + '/bin/EDIICore') is False:
        return False

    return True


def set_edii_path(config):
    dlg = QFileDialog(None, 'Set path to EDII service', config.get_value('edii_path'))
    dlg.setAcceptMode(QFileDialog.AcceptOpen)
    dlg.setOptions(QFileDialog.ShowDirsOnly | QFileDialog.ReadOnly)

    ret = dlg.exec_()
    if ret != QDialog.Accepted:
        return

    config.set_value('edii_path', dlg.selectedFiles()[0])


def main(argv):
    qApp = QApplication(argv)
    sigLoader = None
    supportedFileFormats = None
    sigModel = SignalTraceModel()
    ldrLauncher = loaderlauncher.LoaderLauncher()

    config = Configuration()

    if check_edii_valid(config) is False:
        mbox = QMessageBox(QMessageBox.Information,
                           'Incomplete configuration',
                           ('Path to EDII (ECHMET Data Import Infrastructure) is not set. '
                            'Please set the path now.'))
        mbox.exec_()
        set_edii_path(config)
        print(config.get_value('edii_path'))

    while True:
        try:
            ldrLauncher.launch(config.get_value('edii_path'))
            break
        except loaderlauncher.LoaderLauncherError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'EDII service error', str(ex))
            mbox.exec_()

            mbox = QMessageBox(QMessageBox.Question,
                               'Update configuration',
                               ('Would you like to set a different path to EDII service '
                                'directory and try again?'),
                               QMessageBox.Yes | QMessageBox.No)
            ret = mbox.exec_()

            if ret == QMessageBox.Yes:
                set_edii_path(config)
                continue

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
    config.save()

    return ret


if __name__ == "__main__":
    main(sys.argv)
