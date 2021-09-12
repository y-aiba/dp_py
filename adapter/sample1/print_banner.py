from adapter.sample1.banner import Banner
from adapter.sample1.print import Print


class PrintBanner(Banner, Print):
    def __init__(self, string: str):
        Banner.__init__(self, string=string)

    def print_weak(self) -> None:
        self.show_with_paren()

    def print_strong(self) -> None:
        self.show_with_aster()
