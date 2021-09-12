from abc import ABCMeta, abstractmethod
from iterrator.sample.iterator import Iterator


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self) -> Iterator:
        pass
