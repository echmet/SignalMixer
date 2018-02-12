import bisect


class XFRSignalPack:
    def __init__(self, signal, lastIdx):
        self.signal = signal
        self.lastIdx = lastIdx


def findNearestLeft(pack, x):
    for idx in range(pack.lastIdx, len(pack.signal)):
        if pack.signal[idx].x > x:
            if idx == 0:
                return (None, None)
            pack.lastIdx = idx - 1
            return (pack.signal[idx - 1], idx)

    pack.lastIdx = len(pack.signal) - 1
    return (None, len(pack.signal) - 1)


def flatten(Xpts, xfrSigs):
    for idx in range(1, len(xfrSigs)):
        sig = xfrSigs[idx].signal
        for pt in sig:
            pos = bisect.bisect_left(Xpts, pt.x)
            if pos < len(Xpts):
                if Xpts[pos] != pt.x:
                    Xpts.insert(pos, pt.x)
            else:
                Xpts.append(pt.x)


def makeFirst(sig):
    srt = sorted(sig, key=lambda pt: pt.x)
    Xfirst = []
    for pt in srt:
        Xfirst.append(pt.x)

    return Xfirst


def makeHeader(signalTraces):
    header = ['x']
    for sig in signalTraces.values():
        header.append(sig.customID)

    return header


def makeTransformedSignals(signalTraces):
    xfrSigs = []
    for sig in signalTraces.values():
        xfrSigs.append(XFRSignalPack(sig.transformedSignal(), 0))

    return xfrSigs
