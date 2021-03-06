from signaltraceloader import SignalTraceLoader, SignalTraceLoaderError, SupportedFileFormat, LoadingOption, NoDataError
from PyQt5.QtDBus import QDBusConnection, QDBusInterface, QDBusMessage
from signaltrace import SignalTrace
from datapoint import Datapoint
from loaderlauncher import EDIIConnectionError, EDIIStartError


class DBusInterfaceError(SignalTraceLoaderError):
    def __init__(self, message):
        super().__init__(message)


class DBusReplyError(SignalTraceLoaderError):
    def __init__(self, message):
        super().__init__(message)


class SignalTraceLoaderDBus(SignalTraceLoader):
    DBUS_SERVICE_NAME = 'cz.cuni.natur.echmet.edii'
    DBUS_OBJECT_PATH = '/EDII'

    ABI_VERSION_MAJOR = 0
    ABI_VERSION_MINOR = 1

    def _fetchABIVersion(self):
        msg = self._dbusIface.call('abiVersion')
        if msg.type() != QDBusMessage.ReplyMessage:
            raise DBusReplyError('Invalid reply to abiVersion request')

        if len(msg.arguments()) != 1:
            raise DBusReplyError('Invalid reply length to abiVersion request')

        return msg.arguments()[0]

    def _fetchSupportedFormats(self):
        msg = self._dbusIface.call('supportedFileFormats')
        if msg.type() != QDBusMessage.ReplyMessage:
            raise DBusReplyError('Invalid reply to supportedFileFormats request')

        if len(msg.arguments()) < 1:
            raise DBusReplyError('Invalid reply length to supportedFileFormats request')

        sffs = []
        for sff in msg.arguments()[0]:
            loadingOptions = []
            for idx in range(0, len(sff[3])):
                opt = sff[3][idx]
                loadingOptions.append(LoadingOption(idx, opt))

            sffs.append(SupportedFileFormat(sff[2], sff[1], sff[0], loadingOptions))

        return sffs

    @staticmethod
    def _payloadToSignal(block):
        path = block[0]
        dataID = block[1]
        xTitle = block[3]
        xUnit = block[5]
        yTitle = block[4]
        yUnit = block[6]
        datapoints = []

        for pt in block[7]:
            datapoints.append(Datapoint(x=pt[0], y=pt[1]))

        return SignalTrace(datapoints, path, dataID, xTitle, xUnit, yTitle, yUnit)

    def loadSignal(self, tag, option, hintpath):
        if not SignalTraceLoaderDBus.serviceAvailable():
            try:
                self._loaderLauncher.launchIfNeeded()
            except EDIIConnectionError:
                return []
            except EDIIStartError:
                return []

        msg = None
        if len(hintpath) > 0:
            msg = self._dbusIface.call('loadDataHint', tag, hintpath, option)
        else:
            msg = self._dbusIface.call('loadData', tag, option)
        if msg.type() != QDBusMessage.ReplyMessage:
            raise DBusReplyError('Invalid reply to loadData request')

        if len(msg.arguments()) < 1:
            raise DBusReplyError('Invalid reply length to loadData request')

        payload = msg.arguments()[0]

        if payload[0] is False:
            raise NoDataError()

        signals = []
        for block in payload[2]:
            signals.append(self._payloadToSignal(block))

        return signals

    def __init__(self, loaderLauncher):
        super().__init__(loaderLauncher)

        if not QDBusConnection.sessionBus().interface().isServiceRegistered(SignalTraceLoaderDBus.DBUS_SERVICE_NAME):
            raise DBusInterfaceError('Service {} is not registered'.format(SignalTraceLoaderDBus.DBUS_SERVICE_NAME))

        self._dbusIface = QDBusInterface(SignalTraceLoaderDBus.DBUS_SERVICE_NAME, SignalTraceLoaderDBus.DBUS_OBJECT_PATH, '')
        if not self._dbusIface.isValid():
            raise DBusInterfaceError('DBus interface is invalid')

        abiVersion = self._fetchABIVersion()

        if abiVersion[0] != self.ABI_VERSION_MAJOR or abiVersion[1] != self.ABI_VERSION_MINOR:
            raise DBusInterfaceError('Incompatible version od DBus interface ABI {}.{}'.format(abiVersion[0], abiVersion[1]))

        self._supportedFileFormats = self._fetchSupportedFormats()
        self._dbusIface.setTimeout(600000)

    def serviceAvailable():
        if not QDBusConnection.sessionBus().interface().isServiceRegistered(SignalTraceLoaderDBus.DBUS_SERVICE_NAME):
            return False

        dbusIface = QDBusInterface(SignalTraceLoaderDBus.DBUS_SERVICE_NAME, SignalTraceLoaderDBus.DBUS_OBJECT_PATH, '')
        return dbusIface.isValid()

    def supportedFileFormats(self):
        return self._supportedFileFormats
