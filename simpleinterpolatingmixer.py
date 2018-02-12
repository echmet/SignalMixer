import abstractmixer
import simplemixercommon


class SimpleInterpolatingMixer(abstractmixer.AbstractMixer):
    def description(self):
        return 'Simple mixing with interpolation of Y values. Uneven X-axis sampling should be expected.'

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
