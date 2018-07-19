import abc
from collections import namedtuple


class SignalTraceLoaderError(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return self._message


class NoDataError(Exception):
    def __init__(self):
        super()

    def __str__(self):
        return 'Loading service did not send any data'


LoadingOption = namedtuple('LoadingOption', ['index', 'name'])
SupportedFileFormat = namedtuple('SupportedFileFormat', ['tag', 'shortDescription', 'longDescription', 'loadingOptions'])


class SignalTraceLoader(metaclass=abc.ABCMeta):
    def __init__(self, loaderLauncher):
        self._loaderLauncher = loaderLauncher

    @abc.abstractmethod
    def loadSignal(self, tag, option, hintpath):
        pass

    @abc.abstractmethod
    def supportedFileFormats(self):
        pass

    @abc.abstractstaticmethod
    def serviceAvailable():
        pass

    def launchService(self):
        self._loaderLauncher.launch()

