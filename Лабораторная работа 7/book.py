class Book:
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("название книги должно быть str")
        if not isinstance(author, str):
            raise TypeError("имя автора должно быть str")
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("название книги должно быть str")
        else:
            self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError("имя автора должно быть str")
        else:
            self._author = new_author

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
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("количество страниц должно быть int")
        elif new_pages <= 0:
            raise ValueError("количество страниц должно быть положительным числом")
        else:
            self._pages = new_pages

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"PaperBook({self.name}, {self.author}, {self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("продолжительность должна быть float")
        if duration <= 0:
            raise ValueError("продолжительность должна быть положительным числом")
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("продолжительность должна быть float")
        elif new_duration <= 0:
            raise ValueError("продолжительность должна быть положительным числом")
        else:
            self._duration = new_duration

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, {self.duration} hours"

    def __repr__(self):
        return f"AudioBook({self.name}, {self.author}, {self.duration})"
