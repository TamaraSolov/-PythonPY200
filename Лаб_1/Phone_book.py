from typing import Union
import doctest

class PhoneBook:
    """ Класс, который ищет человека в телефонном справочнике. """

    def __init__(self, number_of_pages: int, name: str, phone_number: int):
        """
        Ищем номер человека из справочника по заданным параметрам
        :param number_of_pages: номер страницы в справочнике
        :param name: имя человека, которого ищем
        :param phone_number: номер телефона
        """
        self.number_of_pages = None
        self.init_number_of_pages(number_of_pages)

        if not isinstance(phone_number, int):
            raise TypeError("Укажите номер телефона в виде целого числа")
        if not phone_number > 0:
            raise ValueError("Число должно быть положительным")
        if not isinstance(name, str):
            raise TypeError("Укажите имя в виде строки")
        self.name = name
        self.phone_number = phone_number

    def init_number_of_pages(self, number_of_pages: int):
        """"
        Метод, который инициализирует атрибут number_of_pages
        Примеры:
        >>> pb = PhoneBook(321, "Tomas", 89119515000)
        >>> pb.init_number_of_pages(212)
        """
        if not isinstance(number_of_pages, int):
            raise TypeError("Укажите номер страницы в виде целого числа")
        if not number_of_pages > 0:
            raise ValueError("Число должно быть положительным")
        self.number_of_pages = number_of_pages


    def __str__(self) -> str:
        """"
        Метод, которыq представляет класс PhoneBook в удобном для пользователя виде
        """
        return f'Cтраница в справочнике {self.number_of_pages}. Имя человека, которого вы ищите = {self.name}. Телефон этого человека {self.phone_number}'


if __name__ == '__main__':
    phone_b = PhoneBook(34, "Даша", 89110282865)
    print(phone_b)
    doctest.testmod() # тестирование примеров в документации