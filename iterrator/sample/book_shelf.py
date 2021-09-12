from iterrator.sample.aggregate import Aggregate
from iterrator.sample.book import Book
from iterrator.sample.iterator import Iterator
from typing import List


class BookShelf(Aggregate):
    def __init__(self, maxsize: int):
        self.books: List[Book] = [Book(name='init') for i in range(maxsize)]
        self.last: int = 0

    def get_book_at(self, index: int) -> Book:
        return self.books[index]

    def append_book(self, book: Book) -> None:
        self.books[self.last] = book
        self.last += 1

    def get_length(self) -> int:
        return self.last

    def iterator(self) -> Iterator:
        return BookSelfIterator(self)


class BookSelfIterator(Iterator):
    def __init__(self, book_shelf: BookShelf):
        self.book_shelf: BookShelf = book_shelf
        self.index: int = 0

    def has_next(self) -> bool:
        if self.index < self.book_shelf.get_length():
            return True
        else:
            return False

    def next(self) -> object:
        book: Book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book
