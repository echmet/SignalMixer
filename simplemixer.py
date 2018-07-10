import abstractmixer
import simplemixercommon


class SimpleMixer(abstractmixer.AbstractMixer):
    def description(self):
        s = ('Simple mixing. Uneven X-axis sampling should be expected.\n\n'
             'All X values of all loaded signals are retained and ordered in '
             'ascending order in the output. Note that this is likely to produce '
             'an output with multiple X-axis datapoints with very similar values. '
             'This may happen either due to small differences of X axis datapoints\' '
             'values in input files or rounding errors.\n\n'
             'This mixer is recommended to use when traces aquired with the same sampling '
             'rates are merged together. Use of this mixed with signals acquired '
             'with a different sampling rate will lead to "stair-shaped" results.')

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
