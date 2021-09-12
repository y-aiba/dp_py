from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    def display(self) -> None:
        self.open()
        for i in range(5):
            self.print()
        self.close()
