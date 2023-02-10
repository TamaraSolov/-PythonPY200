from typing import Union
from abc import ABC, abstractmethod

class GamesApplication:
    # прототип приложения игр/развлечений
    @abstractmethod
    def check_age(self):
        pass

class FinancesApplication:
    # прототип финансового приложения
    @abstractmethod
    def check_rating(self):
        pass

class BuysApplication:
    # прототип приложения онлайн магазина
    @abstractmethod
    def check_language(self):
        pass

class Application(ABC):
    # конструктор приложений
    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size

class GameApp(Application, GamesApplication):
    def __init__(self, name: str, size: float, age: int):
        super().__init__(name, size)
        self.age = age

    def check_age(self):
        if self.age < 18:
            print(f"Приложение {self.name} не доступно для скачивания по возрасту.")
        else:
            print(f"Приложение {self.name} доступно для скачивания.")


class FinanceApp(Application, FinancesApplication):
    def __init__(self, name: str, size: float, rating: float):
        super().__init__(name, size)
        self.rating = rating

    def check_rating(self):
        if self.rating < 3.8:
            print(f"Рейтинг приложение {self.name} низкий.")
        else:
            print(f"Рейтинг приложение {self.name} высокий.")


class BuyApp(Application, BuysApplication):
    def __init__(self, name: str, size: float, language: str):
        super().__init__(name, size)
        self.language = language

    def check_language(self):
        a = "english"
        b = "русский"
        if self.language == a:
            print(f"Приложение {self.name} на английском языке.")
        elif self.language == b:
            print(f"Приложение {self.name} на русском языке.")
        else:
            print(f"Приложение {self.name} не переведено на русский и английский языки.")


class AppStore:
    def __init__(self):
        self.applications = []

    def add_application(self, application: Union[GamesApplication, FinancesApplication, BuysApplication]):
        # добавляем приложения в стор
        self.applications.append(application)

    def check_age_app(self, age: int):
        for app in self.applications:
            if app.age == age and isinstance(app, GamesApplication):
                return app.check_age()
        print(f"Некорректно указан возраст {age}.")


    def check_rating_app(self, rating: float):
        for app in self.applications:
            if app.rating == rating and isinstance(app, FinancesApplication):
                return app.check_rating()
        print(f"Приложение с таким рейтингом {rating} не найдено.")


    def check_language_app(self, language: str):
        for app in self.applications:
            if app.language == language and isinstance(app, BuysApplication):
                return app.check_language()
        print(f"Приложение на таком языке {language} не найдено.")


if __name__ == "__main__":
    appstore = AppStore()
    app1 = GameApp("Jamp", 257.7, 19)
    app2 = FinanceApp("Bank", 199.1, 4.8)
    app3 = BuyApp("Ozon", 203.1, "русский")
    appstore.add_application(app1)
    appstore.add_application(app2)
    appstore.add_application(app3)

    appstore.check_age_app(19)
    # appstore.check_rating_app(4.8)
    # appstore.check_language_app("english")
