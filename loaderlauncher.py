import time
import platform
import os
from PyQt5.QtCore import QProcess
import signaltraceloaderfactory
import signaltraceloader


class LoaderLauncherError(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return self._message


class LoaderLauncher:
    BIN_PREFIX = '/bin/'
    EXE_NAME = 'EDIICore'

    @staticmethod
    def check_edii_path(path):
        return os.path.isfile(LoaderLauncher.make_path(path))

    @staticmethod
    def default_path():
        return os.getcwd() + '/EDII'

    @staticmethod
    def exe_suffix():
        ostype = platform.system()
        if ostype == 'Windows':
            return '.exe'
        else:
            return ''

    @staticmethod
    def make_path(path):
        return (path + LoaderLauncher.BIN_PREFIX + LoaderLauncher.EXE_NAME
                     + LoaderLauncher.exe_suffix())

    def __init__(self):
        self._ldrProcess = QProcess()

    def launch(self, loaderpath):
        self._setup_path(loaderpath)

        try:
            if signaltraceloaderfactory.serviceAvailable():
                return
        except signaltraceloader.SignalTraceLoaderError as ex:
            raise LoaderLauncherError(str(ex))

        self._ldrProcess.start()
        if not self._ldrProcess.waitForStarted(2000):
            raise LoaderLauncherError('Cannot launch loader service: ' + self._ldrProcess.errorString())
        time.sleep(0.25)

    def _setup_path(self, loaderpath):
        if isinstance(loaderpath, str) is False:
            raise LoaderLauncherError('Invalid path to EDII service')

        path = ''
        if not os.path.isabs(loaderpath):
            path = os.path.abspath(loaderpath)
        else:
            path = loaderpath

        exe_path = LoaderLauncher.make_path(path)

        self._ldrProcess.setProgram(exe_path)
        self._ldrProcess.setWorkingDirectory(path + LoaderLauncher.BIN_PREFIX)

    def terminate(self):
        self._ldrProcess.terminate()
        self._ldrProcess.waitForFinished(3000)
