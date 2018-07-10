import abstractmixer
import simplemixercommon


class SimpleInterpolatingMixer(abstractmixer.AbstractMixer):
    def description(self):
        s = ('Simple mixing with interpolation of Y-axis values. Uneven X-axis sampling should be expected.\n\n'
             'All X-axis values of all loaded signals are retained and ordered in ascending order. '
             'Y axis values of signals with lower sampling rate are interpolated to eliminate "stair-shape" '
             'looking output.\n\n'
             'This is the recommended mixer to use to merge signals acquired with different sampling rates.')

        return s

    def mix(self, signalTraces):
        if len(signalTraces) < 1:
            return ([], [])

        xfrSigs = simplemixercommon.makeTransformedSignals(signalTraces)
        Xpts = simplemixercommon.makeFirst(xfrSigs[0].signal)
        simplemixercommon.flatten(Xpts, xfrSigs)

        cocktail = []
        for x in Xpts:
            yVals = []
            for pack in xfrSigs:
                def nextPt(idx):
                    if idx + 1 >= len(pack.signal):
                        return None
                    return pack.signal[idx + 1]

                ptLeft = simplemixercommon.findNearestLeft(pack, x)
                if ptLeft[0] is None:
                    yVals.append(None)
                    continue

                ptRight = nextPt(ptLeft[1])
                if ptRight is None:
                    yVals.append(None)
                    continue

                ptLeftV = ptLeft[0]

                k = (ptRight.y - ptLeftV.y) / (ptRight.x - ptLeftV.x)
                y = k * (x - ptLeftV.x) + ptLeftV.y
                yVals.append(y)

            cocktail.append(abstractmixer.MixedPoint(x, yVals))

        header = simplemixercommon.makeHeader(signalTraces)

        return (header, cocktail)

    def shortName(self):
        return 'Simple interpolating'
