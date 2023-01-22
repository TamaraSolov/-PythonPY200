from typing import Any, Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    """ Класс, который который описывает книгу """
    def __init__(self, id_: int, name: str, pages: int):
        """"
        Создаем новую книгу через конструктор
                :param id_: идентификатор книги
                :param name: Название книги
                :param pages: Количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'
        # return str(self.name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        """
        Записываем конструктор для класса Library
        :param books: список книг
        """
        self.books = books

    def get_next_book_id(self):
        """
        Метод для добавления новой книги в библиотеку
        """
        if self.books is None:
            return 1
        else:
            return len(self.books) + 1


    def get_index_by_book_id(self, book_id):
        """
               Метод, который определяет индекс книги
               :param book_id: id книги
               :return: индекс книги в списке книг
               """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError ("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
