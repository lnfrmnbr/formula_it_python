from typing import List


class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError("идентификатор книги должен быть типа int")
        if not isinstance(name, str):
            raise TypeError("название книги должно быть str")
        if not isinstance(id, int):
            raise TypeError("количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("количество страниц должно быть положительным числом")
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id={self.id}, name=\'{self.name}\', pages={self.pages})'


class Library:
    def __init__(self, books: List = []):
        self.books = books

    def get_next_book_id(self) -> int:
        ls = self.books
        if len(ls) == 0:
            return 1
        else:
            return ls[len(ls)-1].id + 1

    def get_index_by_book_id(self, b: Book) -> int:
        ls = self.books
        for item in enumerate(ls):
            if item[1].id == b.id:
                return item[0]
        else:
            raise ValueError("книги с запрашиваемым id не существует")


c = Book(1, 'колобок', 100)
print(str(c))
print(repr(c))

books = [
    {
        "id": 1,
        "name": "колобок",
        "pages": 100,
    },
    {
        "id": 2,
        "name": "мертвые души",
        "pages": 200,
    },
    {
        "id": 3,
        "name": "старик и море",
        "pages": 150,
    }
]

list_books = [Book(id=book["id"], name=book["name"], pages=book["pages"]) for book in books]
library = Library(list_books)
print(library.get_next_book_id())
print(library.get_index_by_book_id(c))




