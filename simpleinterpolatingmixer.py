import abstractmixer


class SimpleInterpolatingMixer(abstractmixer.AbstractMixer):
    def description(self):
        return 'Simple mixing with interpolation of Y values. Uneven X-axis sampling should be expected.'

    def mix(self, signalTraces):
        return []

    def shortName(self):
        return 'Simple interpolating'
