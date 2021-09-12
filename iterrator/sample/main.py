from iterrator.sample.book import Book
from iterrator.sample.book_shelf import BookShelf
from iterrator.sample.iterator import Iterator


class Main:
    @staticmethod
    def main():
        book_shelf: BookShelf = BookShelf(maxsize=4)
        book_shelf.append_book(Book(name="Around the world in 80 days"))
        book_shelf.append_book(Book(name="Bible"))
        book_shelf.append_book(Book(name="Cinderella"))
        book_shelf.append_book(Book(name="Daddy-Long-Legs"))
        it: Iterator = book_shelf.iterator()
        while it.has_next():
            book: Book = it.next()
            print(book.get_name())


if __name__ == '__main__':
    cls = Main()
    cls.main()
