import math
from signaltracescaler import SignalTraceScaler
from datapoint import Datapoint
import xunitguesser
import sys


class SignalTraceError(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return self._message


class InvalidSignalTraceCropError(SignalTraceError):
    def __init__(self):
        super().__init__('Invalid signal trace crop')


class InvalidSignalTraceScalingError(SignalTraceError):
    def __init__(self):
        super().__init__('Invalid signal trace scaling')


class InvalidSignalError(SignalTraceError):
    def __init__(self, message):
        super().__init__('Invalid signal trace: {}'.format(message))


def calcYRange(datapoints):
    yMax = -sys.float_info.max
    yMin = sys.float_info.max

    for dp in datapoints:
        if dp.y > yMax:
            yMax = dp.y
        if dp.y < yMin:
            yMin = dp.y


def convertToCommonX(datapoints, xUnit):
    scaleMultiplier = xunitguesser.guessRatio(xUnit)

    if scaleMultiplier <= 0.0:
        raise SignalTraceError('Nonsensical X axis unit multiplier')

    converted = []
    for pt in datapoints:
        converted.append(Datapoint(pt.x * scaleMultiplier, pt.y))

    return converted


def checkSignalValid(datapoints):
    if len(datapoints) < 2:
        raise InvalidSignalError('Not enough datapoints')

    for idx in range(1, len(datapoints) - 1):
        p = datapoints[idx - 1]
        q = datapoints[idx]

        if q.x <= p.x:
            raise InvalidSignalError('X axis is not monotonic')


class SignalTrace:
    def __init__(self, srcDatapoints, srcFile, dataID, xTitle, xUnit, yTitle, yUnit):
        checkSignalValid(srcDatapoints)

        self._srcDatapoints = convertToCommonX(srcDatapoints, xUnit)
        self.srcFile = srcFile
        self.dataID = dataID
        self.xTitle = xTitle
        self.xUnit = 'sec'
        self.yTitle = yTitle
        self.yUnit = yUnit
        self.customID = ''

        self._avgSR = len(self._srcDatapoints) / (self._srcDatapoints[-1].x - self._srcDatapoints[0].x)
        self._YRange = calcYRange(self._srcDatapoints)
        print(self._avgSR)

        self._cropFrom = self._srcDatapoints[0].x
        self._cropTo = self._srcDatapoints[-1].x
        self._prepend = self._srcDatapoints[0].y
        self._append = self._srcDatapoints[-1].y

        self._scaleFrom = self._srcDatapoints[0].x
        self._scaleTo = self._srcDatapoints[-1].x
        self._scalingEnabled = False

    def _applyCropping(self):
        datapoints = []
        x = self._cropFrom
        xStep = 1.0 / self._avgSR

        while x < self._srcDatapoints[0].x:
            datapoints.append(Datapoint(x, self._prepend))
            x += xStep

        for pt in self._srcDatapoints:
            if pt.x > self._cropTo:
                break
            if pt.x >= self._cropFrom:
                datapoints.append(pt)

        x = self._srcDatapoints[-1].x
        while x <= self._cropTo:
            datapoints.append(Datapoint(x, self._append))
            x += xStep

        return datapoints

    def averageXStep(self):
        return float(1.0 / self._avgSR)

    def removeCrop(self, front, tail):
        if front:
            self._cropFrom = self._srcDatapoints[0].x
        if tail:
            self._cropTo = self._srcDatapoints[-1].x

    def removeScaling(self):
        self._scalingEnabled = False

    def samplingRate(self):
        return self._samplingRate

    def setCropFrom(self, xFrom):
        if xFrom >= self._cropTo:
            raise InvalidSignalTraceCropError

        self._cropFrom = xFrom

    def setCropTo(self, xTo):
        if xTo <= self._cropFrom:
            raise InvalidSignalTraceCropError

        self._cropTo = xTo

    def setPrependAppend(self, prepend, append):
        self._prepend = prepend
        self._append = append

    def setScaling(self, scaleFrom, scaleTo):
        if scaleFrom >= scaleTo:
            raise InvalidSignalTraceScalingError

        if self._scaleFrom < self._scaleTo and scaleFrom >= scaleTo:
            raise InvalidSignalTraceScalingError
        elif self._scaleFrom > self._scaleTo and scaleFrom <= scaleTo:
            raise InvalidSignalTraceScalingError

        self._scaleFrom = scaleFrom
        self._scaleTo = scaleTo
        self._scalingEnabled = True

    def sourceSignal(self):
        return self._srcDatapoints

    def transformedSignal(self):
        cropped = self._applyCropping()

        if self._scalingEnabled:
            return SignalTraceScaler.scale(cropped, self._scaleFrom, self._scaleTo)
        else:
            return cropped

    def YRange(self):
        return int(self._YRange)
