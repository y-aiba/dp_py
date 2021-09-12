from templete.sample.abstract_display import AbstractDisplay
from templete.sample.char_display import CharDisplay
from templete.sample.string_display import StringDisplay


class Main:
    def main(self) -> None:
        d1: AbstractDisplay = CharDisplay(ch='H')
        d2: AbstractDisplay = StringDisplay(string='Hello, world.')
        d3: AbstractDisplay = StringDisplay(string='こんにちは')
        d1.display()
        d2.display()
        d3.display()


if __name__ == '__main__':
    m = Main()
    m.main()
