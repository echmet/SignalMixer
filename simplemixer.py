import abstractmixer
import bisect


class XFRSignalPack:
    def __init__(self, signal, lastIdx):
        self.signal = signal
        self.lastIdx = lastIdx


class SimpleMixer(abstractmixer.AbstractMixer):
    @staticmethod
    def _findNearestLeft(pack, x):
        for idx in range(pack.lastIdx, len(pack.signal)):
            if pack.signal[idx].x > x:
                if idx == 0:
                    return None
                pack.lastIdx = idx - 1
                return pack.signal[idx - 1].y

        pack.lastIdx = len(pack.signal) - 1
        return pack.signal[-1].y

    @staticmethod
    def _makeFirst(sig):
        srt = sorted(sig, key=lambda pt: pt.x)
        Xfirst = []
        for pt in srt:
            Xfirst.append(pt.x)

        return Xfirst

    @staticmethod
    def _makeTransformedSignals(signalTraces):
        xfrSigs = []
        for sig in signalTraces.values():
            xfrSigs.append(XFRSignalPack(sig.transformedSignal(), 0))

        return xfrSigs

    def description(self):
        return 'Simple mixing. Uneven X-axis sampling should be expected.'

    def mix(self, signalTraces):
        if len(signalTraces) < 1:
            return []

        xfrSigs = self._makeTransformedSignals(signalTraces)
        Xpts = self._makeFirst(xfrSigs[0].signal)

        for idx in range(1, len(xfrSigs)):
                sig = xfrSigs[idx].signal
                for pt in sig:
                    pos = bisect.bisect_left(Xpts, pt.x)
                    if pos < len(Xpts):
                        if Xpts[pos] != pt.x:
                            Xpts.insert(pos, pt.x)

        cocktail = []
        for x in Xpts:
            yVals = []
            for pack in xfrSigs:
                y = self._findNearestLeft(pack, x)
                yVals.append(y)

            cocktail.append(abstractmixer.MixedPoint(x, yVals))

        header = ['x']
        for sig in signalTraces.values():
            header.append(sig.customID)

        return (header, cocktail)

    def shortName(self):
        return 'Simple'
