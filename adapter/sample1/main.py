from adapter.sample1.print_banner import Print, PrintBanner


def main():
    p: Print = PrintBanner(string="Hello")
    p.print_weak()
    p.print_strong()


if __name__ == '__main__':
    main()
