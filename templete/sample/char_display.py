from templete.sample.abstract_display import AbstractDisplay


class CharDisplay(AbstractDisplay):
    def __init__(self, ch: str):
        self.ch = ch

    def open(self) -> None:
        print("<<", end='')

    def print(self) -> None:
        print(self.ch, end='')

    def close(self) -> None:
        print(">>")
