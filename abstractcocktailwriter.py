import abc


class CocktailWriterError(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self):
        return self._message


class AbstractCocktailWriter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, header, cocktail, target):
        pass
