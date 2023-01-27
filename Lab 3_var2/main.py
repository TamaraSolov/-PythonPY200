class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError("Название автора должно быть str")
        self._author = new_author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Название книги должно быть str")
        self._name = new_name

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страницы {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r} )"


class AudioBook(PaperBook):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.duration = new_duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration!r} )"

