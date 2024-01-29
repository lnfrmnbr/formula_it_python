class Book:
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("название книги должно быть str")
        if not isinstance(author, str):
            raise TypeError("название книги должно быть str")
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self) -> str:
        return f'Книга "{self._name}"'

    def __repr__(self):
        return f'Book(name=\'{self._name}\', author=\'{self._author}\')'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"PaperBook({self.name}, {self.author}, {self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("продолжительность должна быть int")
        if duration <= 0:
            raise ValueError("продолжительность должна быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, {self.duration} hours"

    def __repr__(self):
        return f"AudioBook({self.name}, {self.author}, {self.duration})"
