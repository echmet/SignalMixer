import simplemixer


class NoSuchMixerError(Exception):
    def __init__(self, mixer):
        super().__init__()
        self._mixer = mixer

    def __str__(self):
        return 'No mixer named {} is available'.format(self._mixer)


class SignalMixerFactory:
    @staticmethod
    def _makeAvailableMixers():
        mixers = {}

        def _add(m):
            mixers[m.shortName()] = m;

        _add(simplemixer.SimpleMixer())

        return mixers

    def __init__(self):
        self._availableMixers = self._makeAvailableMixers()

    def availableMixers(self):
        mixers = []
        for k,v in self._availableMixers.items():
            mixers.append((k, v.description()))

        return mixers

    def getMixer(self, shortName):
        if shortName not in self._availableMixers:
            raise NoSuchMixerError(shortName)

        return self._availableMixers[shortName]
