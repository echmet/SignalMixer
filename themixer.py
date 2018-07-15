#! /usr/bin/python3

import sys
from signaltraceloader import SignalTraceLoaderError
import signaltraceloaderfactory
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog
from ui.mainwindow import MainWindow
from signaltracemodel import SignalTraceModel
from configuration import Configuration
from loaderlauncher import LoaderLauncher, LoaderLauncherError


def check_edii_valid(config):
    path = config.get_value('edii_path')

    if path is None:
        return False

    return LoaderLauncher.check_edii_path(path)


def set_edii_path(config):
    dlg = QFileDialog(None, 'Set path to EDII service',
                      config.get_value('edii_path'))
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
    ldrLauncher = LoaderLauncher()

    config = Configuration()

    if check_edii_valid(config) is False:
        mbox = QMessageBox(QMessageBox.Information,
                           'Incomplete configuration',
                           ('Path to ECHMET Data Import Infrastructure (EDII) '
                            'service has not been set. '
                            'This service is necessary for SigMix to load '
                            'experimental data and SigMix cannot function '
                            'without it.\n\n'
                            'Unless you have a reason to set the path '
                            'manually default path should be safe to use.'))
        mbox.addButton('Use default path', QMessageBox.YesRole)
        mbox.addButton('Set path manually', QMessageBox.NoRole)
        if mbox.exec_() == QDialog.Accepted:
            set_edii_path(config)
        else:
            config.set_value('edii_path', LoaderLauncher.default_path())

    while True:
        try:
            ldrLauncher.launch(config.get_value('edii_path'))
            break
        except LoaderLauncherError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'EDII service error',
                               str(ex))
            mbox.exec_()

            mbox = QMessageBox(QMessageBox.Question,
                               'Invalid configuration',
                               ('SigMix was unable to start EDII service. '
                                'Would you like to set a different path to '
                                'the EDII service and try again?'),
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
