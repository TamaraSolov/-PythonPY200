import random
from typing import Union

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
        self._model = model
        self._color = color

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        if not isinstance(new_model, str):
            raise TypeError("Название авто должно быть str")
        else:
            self._model = new_model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: int) -> None:
        if not isinstance(new_color, int):
            raise TypeError("Скорость должна быть типа int")
        if new_color <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self._color = new_color

    def __str__(self):
        return f"Машина {self.model}. Цвет {self.color}"

    def __repr__(self):
        """
             Метод, которыq представляет класс Car в читаемом виде
        """
        return f"{self.__class__.__name__}(Model={self.model!r}, Color={self.color!r})"

class ElectroCar(Car):
    MODELS = ["Kia", "Lada", "BMW", "Infinity", "Lexus", "Audi", "Volvo"]

    def __init__(self, model: str, color: Union[str, int], speed: int):
        super().__init__(model, color)

        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: int) -> None:
        if not isinstance(new_speed, int):
            raise TypeError("Скорость должна быть типа int")
        if new_speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self._speed = new_speed

    # @classmethod
    # def doublespeed(cls, plusspeed):
    #     """ Изменяем атрибут speed класса Electrocar"""
    #         return cls.speed + plusspeed

    @classmethod
    def doublespeed(cls, *dbspeed):
        """ Изменяем атрибут speed класса Electrocar"""
        if len(dbspeed) >= 0:
            return cls.acceleration(*dbspeed)

    @staticmethod
    def acceleration(speed: int, time:int):
        """ Формула расчета ускорения через скорость и время"""
        return speed/time

    def randommodel(self):
        return random.choice(self.MODELS)

    def __str__(self):
        return f"Электрокар, модель {self.model}. цвет {self.color}. скорость {self.speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Model={self.model!r}, Color={self.color!r}, Speed={self.speed!r} )"

if __name__ == '__main__':
    car = Car("Lada", 3)
    car1 = ElectroCar("Kia", "Black", 120)
    print(car)
    print(car1)
    print(ElectroCar.doublespeed(300, 25))