import abc
from collections import namedtuple


MixedPoint=namedtuple('MixedPoint', ['x', 'yValues'])


class AbstractMixer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def mix(self, signalTraces):
        pass

    @abc.abstractmethod
    def shortName(self):
        pass
