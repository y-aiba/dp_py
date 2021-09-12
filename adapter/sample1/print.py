from abc import ABCMeta, abstractmethod


class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self) -> None:
        pass

    @abstractmethod
    def print_strong(self) -> None:
        pass
