from templete.sample.abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):
    def __init__(self, string: str):
        self.string = string
        self.width = len(string)

    def open(self) -> None:
        self.print_line()

    def print(self) -> None:
        print("|" + self.string + "|")

    def close(self) -> None:
        self.print_line()

    def print_line(self):
        print("+" + "-" * self.width + "+")
