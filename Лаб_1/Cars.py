from typing import Union
import doctest

class Car:
    """ Класс, который создает прототип машины. """

    def __init__(self, model: str, color: Union[str, int]):
        """
        Создаем новую машину и задаем параметры
        :param model: Марка авто, записывается как строка
        :param color: Цвет авто, записывается как строка
        """
        if not isinstance(model, str):
            raise TypeError("Укажите название модели авто в виде строки")
        if not isinstance(color, (str, int)):
            raise TypeError("Укажите цвет авто цифрой или в виде строки")
        self.model = model
        self.color = color

    def get_model(self) -> str:
        """"
        Метод, который возвращает значение атрибута model
        Примеры:
        >>> car = Car("Infinity", "black")
        >>> car.get_model("BMW")
        """
        return self.model

    def get_color(self) -> str:
        """"
        Метод, который возвращает значение атрибута color
        Примеры:
        >>> car = Car("Infinity", "black")
        >>> car.get_color("red")
        """
        return self.color

    def __repr__(self) -> str:
        """"
        Метод, которыq представляет класс Car в читаемом виде
        """
        return f'Car({self.model}, {self.color})'


if __name__ == '__main__':
    car = Car("Lada", 3)
    print(car)
    doctest.testmod() # тестирование примеров в документации