import abstractmixer
import simplemixercommon


class SimpleMixer(abstractmixer.AbstractMixer):
    def description(self):
        return 'Simple mixing. Uneven X-axis sampling should be expected.'

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
                pt = simplemixercommon.findNearestLeft(pack, x)[0]
                if pt is None:
                    yVals.append(None)
                else:
                    yVals.append(pt.y)

            cocktail.append(abstractmixer.MixedPoint(x, yVals))

        header = simplemixercommon.makeHeader(signalTraces)

        return (header, cocktail)

    def shortName(self):
        return 'Simple'
