from typing import Union
import doctest

class Human:
    """ Класс, который задает параметры человека. """

    def __init__(self, age: int, weight: int, height: int):
        """
        Задаем параметры человека
        :param age: возраст
        :param weight: вес
        :param height: рост
        """
        self.height = None
        self.init_height(height)

        if not isinstance(age, int):
            raise TypeError("Укажите возраст в виде целого числа")
        if not age > 0:
            raise ValueError("Число должно быть положительным")
        if not isinstance(weight, int):
            raise TypeError("Укажите вес в виде целого числа")
        if not weight > 0:
            raise ValueError("Число должно быть положительным")
        self.age = age
        self.weight = weight

    def init_height(self, height: int):
        """"
        Метод, который инициализирует атрибут height
        Примеры:
        >>> human = Human(32, 74, 175)
        >>> human.init_height(180)
        """
        if not isinstance(height, int):
            raise TypeError("Укажите рост в виде целого числа")
        if not height > 0:
            raise ValueError("Число должно быть положительным")
        self.height = height


    def __str__(self) -> str:
        """"
        Метод, которыq представляет класс Human в удобном для пользователя виде
        """
        return f'Количество лет = {self.age}. Вес этого человека = {self.weight}. И его рост = {self.height}'


if __name__ == '__main__':
    human = Human(34, 54, 168)
    print(human)
    doctest.testmod() # тестирование примеров в документации