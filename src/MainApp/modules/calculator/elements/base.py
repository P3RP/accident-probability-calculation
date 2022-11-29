from abc import *


class BaseCalc(metaclass=ABCMeta):
    @abstractmethod
    def calc(self, **kwargs):
        pass
