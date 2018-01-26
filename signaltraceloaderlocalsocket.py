from signaltraceloader import SignalTraceLoader, SignalTraceLoaderError, SupportedFileFormat, LoadingOption
from PyQt5.QtNetwork import QLocalSocket
import time
import platform
import struct
import signaltrace
import datapoint
from loaderlauncher import LoaderLauncherError


class LocalSocketError(SignalTraceLoaderError):
    def __init__(self, message):
        super().__init__(message)


class CannotConnectError(LocalSocketError):
    def __init__(self):
        super().__init__('Cannot connect to loader service')


class CommunicationError(LocalSocketError):
    def __init__(self, message='Unspecified error'):
        super().__init__('Socket communication error: {}'.format(message))


class DataLengthError(LocalSocketError):
    def __init__(self, expected, got):
        super().__init__('Data of unexpected size received, expected:{}, got: {}'.format(expected, got))


class LoadingServiceError(LocalSocketError):
    def __init__(self, message):
        super().__init__('Loading service error: {}'.format(message))


class Packet:
    def __init__(self, payload, size):
        self.payload = payload
        self.size = size

def makePacket(packing, *args):
    sz = struct.calcsize(packing)
    data = struct.pack(packing, *args)
    return Packet(data, sz)

class SignalTraceLoaderLocalSocket(SignalTraceLoader):
    RQTYPE_SUPPORTED_FORMATS = 1
    RQTYPE_LOAD_DATA = 2
    RQTYPE_LOAD_DATA_DESCRIPTOR = 3

    RES_SUCCESS = 1
    RES_FAILURE = 2

    RESP_SUPPORTED_FORMAT_HEADER = 1
    RESP_LOAD_DATA_HEADER = 2
    RESP_SUPPORTED_FORMAT_DESCRIPTOR = 3
    RESP_LOAD_DATA_DESCRIPTOR = 4
    RESP_LOAD_OPTION_DESCRIPTOR = 5

    LDMODE_LOAD_INTERACTIVE = 1
    LDMODE_LOAD_HINT = 2
    LDMODE_LOAD_FILE = 3
       
    PACKET_MAGIC = 0x091E
    SOCKET_NAME = 'cevalefgloader'

    def _checkResponse(self, response):
        if response[2] == self.RES_SUCCESS:
            return

        if response[4] > 0:
            err = self._readStringBlock(response[4])
            raise LoadingServiceError(err)

    def _connectSocket(self):
        if not SignalTraceLoaderLocalSocket.serviceAvailable():
            try:
                self._loaderLauncher.launch()
            except LoaderLauncherError:
                return False

        MAX = 24
        ctr = 0

        while (self._socket.state() != QLocalSocket.ConnectedState) and (ctr < MAX):
            self._socket.connectToServer(self.SOCKET_NAME)
            if self._socket.waitForConnected(1000):
                return True
            if self._isWindows:
                time.sleep(1)
            else:
                time.sleep(0.1)
            ctr += 1

        return False

    def _fail(self):
        self._socket.close()
        raise CommunicationError

    def _makeRequest(self, reqType):
        return makePacket('=HB', self.PACKET_MAGIC, reqType)

    def _readPacket(self, packing):
        _packing = '=HBB' + packing
        pkt = self._readBlock(_packing)

        if pkt[0] != self.PACKET_MAGIC:
            raise CommunicationError('Invalid packet header')

        return pkt

    def _readBlock(self, packing):
        expectedSize = struct.calcsize(packing)
        if not self._waitForData(expectedSize):
            raise CommunicationError('Timeout while waiting for data')

        data = self._socket.readData(expectedSize)
        if len(data) != expectedSize:
            raise DataLengthError(expectedSize, len(data))

        return struct.unpack(packing, data)

    def _readRaw(self, size):
        if not self._waitForData(size):
            raise CommunicationError('Timeout while waiting for data')

        data = self._socket.readData(size)
        if len(data) != size:
            raise DataLengthError(size, len(data))

        return data

    def _readStringBlock(self, length):
        if length < 1:
            return ''

        packing = '={}b'.format(length)
        data = self._readBlock(packing)

        byteSeq = bytearray()
        for b in data:
            byteSeq.append(b)

        return byteSeq.decode('UTF-8')

    def _readSupportedFileFormats(self):
        if not self._reconnectIfNeeded():
            raise CannotConnectError

        reqHdr = self._makeRequest(self.RQTYPE_SUPPORTED_FORMATS)
        self._sendPacket(reqHdr)

        respHdr = self._readPacket('iI')
        self._checkResponse(respHdr)

        sffs = []
        for item in range(0, respHdr[3]):
            sfHdr = self._readPacket('4I')
            self._checkResponse(sfHdr)

            longDesc = self._readStringBlock(sfHdr[3])
            shortDesc = self._readStringBlock(sfHdr[4])
            tag = self._readStringBlock(sfHdr[5])
            numOpts = sfHdr[6]
            opts = []

            if numOpts > 0:
                for idx in range(0, numOpts):
                    optHdr = self._readPacket('I')
                    self._checkResponse(optHdr)

                    optDesc = self._readStringBlock(optHdr[3])
                    opts.append(LoadingOption(idx, optDesc))

            sffs.append(SupportedFileFormat(tag, shortDesc, longDesc, opts))

        return sffs

    def _reconnectIfNeeded(self):
        if self._socket.state() != QLocalSocket.ConnectedState:
            return self._connectSocket()

    def _sendPacket(self, packet):
        if self._socket.write(packet.payload) < packet.size:
            raise CommunicationError

        if not self._socket.waitForBytesWritten():
            raise CommunicationError

    def _sendStringBlock(self, block):
        length = len(block)
        if self._socket.write(block) < length:
            raise CommunicationError('Failed to send string block')

        if not self._socket.waitForBytesWritten():
            raise CommunicationError('Failed to wait for written string block')

    @staticmethod
    def _strToBytes(s):
        return s.encode('UTF-8')

    def _waitForData(self, size):
        avail = self._socket.bytesAvailable()
        while avail < size:
            state = self._socket.state()
            if state != QLocalSocket.ConnectedState:
                return False

            self._socket.waitForReadyRead(100)
            avail = self._socket.bytesAvailable()

        return True

    def __init__(self, loaderLauncher):
        super().__init__(loaderLauncher)
        self._isWindows = platform.system() == 'Windows'

        self._socket = QLocalSocket()

        try:
            self._supportedFileFormats = self._readSupportedFileFormats()
        except LocalSocketError:
            self._socket.close()
            raise

    def loadSignal(self, tag, option, hintpath):
        try:
            if not self._reconnectIfNeeded():
                raise CommunicationError

            reqHdr = self._makeRequest(self.RQTYPE_LOAD_DATA)
            self._sendPacket(reqHdr)

            hintpathBA = self._strToBytes(hintpath)
            loadMode = self.LDMODE_LOAD_INTERACTIVE if len(hintpathBA) < 1 else self.LDMODE_LOAD_HINT
            tagBA = self._strToBytes(tag)
            reqLdrHdr = makePacket('=HBBiII', self.PACKET_MAGIC, self.RQTYPE_LOAD_DATA_DESCRIPTOR, loadMode, option, len(tagBA), len(hintpathBA))

            self._sendPacket(reqLdrHdr)
            self._sendStringBlock(tagBA)
            if len(hintpathBA) > 0:
                self._sendStringBlock(hintpathBA)

            respLdrHdr = self._readPacket('iI')
            self._checkResponse(respLdrHdr)

            signals = []
            for item in range(0, respLdrHdr[3]):
                ldrDesc = self._readPacket('8I')
                if ldrDesc[1] != self.RESP_LOAD_DATA_DESCRIPTOR or ldrDesc[2] != self.RES_SUCCESS:
                    raise CommunicationError('Invalid load data descriptor response received')

                # Discard the "name" block
                self._readStringBlock(ldrDesc[3])
                dataID = self._readStringBlock(ldrDesc[4])
                path = self._readStringBlock(ldrDesc[5])
                xDesc = self._readStringBlock(ldrDesc[6])
                yDesc = self._readStringBlock(ldrDesc[7])
                xUnit = self._readStringBlock(ldrDesc[8])
                yUnit = self._readStringBlock(ldrDesc[9])

                datapoints = []
                dpPacking = '2d'
                dpSize = struct.calcsize(dpPacking)
                for dpIdx in range(0, ldrDesc[10]):
                    dpRaw = self._readRaw(dpSize)
                    dp = struct.unpack(dpPacking, dpRaw)
                    datapoints.append(datapoint.Datapoint(x=dp[0], y=dp[1]))

                signals.append(signaltrace.SignalTrace(datapoints, path, dataID, xDesc, xUnit, yDesc, yUnit))

            return signals
        except LocalSocketError:
            self._socket.close()
            raise

    def serviceAvailable():
        socket = QLocalSocket()
        socket.connectToServer(SignalTraceLoaderLocalSocket.SOCKET_NAME)
        return socket.waitForConnected(500)

    def supportedFileFormats(self):
        return self._supportedFileFormats
