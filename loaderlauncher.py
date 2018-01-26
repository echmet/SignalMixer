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
    def __init__(self, loaderpath=''):
        self._ldrProcess = QProcess()

        ostype = platform.system()
        if len(loaderpath) < 1:
            if ostype == 'Linux':
                prefix = os.path.realpath(os.getcwd())

                self._ldrProcess.setProgram(prefix + '/loader/CEvalEFGLoader')
                self._ldrProcess.setWorkingDirectory(prefix + '/loader')

                print(self._ldrProcess.program())
            elif ostype == 'Windows':
                self._ldrProcess.setProgram('loader/CEvalEFGLoader.exe')
                self._ldrProcess.setWorkingDirectory('loader/')
            else:
                raise LoaderLauncherError('Unsupported platform')
        else:
            path = ''
            if not os.path.isabs(loaderpath):
                path = os.path.abspath(loaderpath)
            else:
                path = loaderpath

            self._ldrProcess.setProgram(path)
            self._ldrProcess.setWorkingDirectory(os.path.dirname(path))

    def launch(self):
        try:
            if signaltraceloaderfactory.serviceAvailable():
                return
        except signaltraceloader.SignalTraceLoaderError as ex:
            raise LoaderLauncherError(str(ex))

        self._ldrProcess.start()
        if not self._ldrProcess.waitForStarted(2000):
            raise LoaderLauncherError('Cannot launch loader service')
        time.sleep(0.25)

    def terminate(self):
        self._ldrProcess.terminate()
        self._ldrProcess.waitForFinished(3000)
