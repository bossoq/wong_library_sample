from datetime import datetime

from model import Book


class BookRepository:
    books: list[Book]

    def __init__(self, books: list[Book]) -> None:
        self.books = books

    def find_by_author(self, name: str) -> list[Book]:
        return [book for book in self.books if name.lower() in book['author'].lower()]

    def find_by_hardest(self, length: int) -> list[Book]:
        return [book for book in self.books if book['length'] >= length]

    def find_by_recent(self, year: int) -> list[Book]:
        return [book for book in self.books if datetime.now().year - book['publication_date'].year <= year]
