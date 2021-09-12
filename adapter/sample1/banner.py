class Banner:
    def __init__(self, string: str):
        self.string = string

    def show_with_paren(self) -> None:
        print("(" + self.string + ")")

    def show_with_aster(self) -> None:
        print("*" + self.string + "*")
