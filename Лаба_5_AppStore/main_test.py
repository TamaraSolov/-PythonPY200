import unittest

from main import GameApp # импортируем то, что будем тестировать
from main import FinanceApp
from main import BuyApp


class MyTestBuyApp(unittest.TestCase):

    def test_errore_language(self):
        byeapp = BuyApp("BSPB", 257.7, "русский")
        with self.assertRaises(TypeError):
            byeapp.language = [1,2]

    # def test_check_language(self):
    #     self.assertEqual(BuyApp.check_language("english"), "english")

    def test_check_1(self):
        obj = BuyApp("BSPB", 257.7, "русский")
        mes = "обект не принадлежит к этому классу"
        self.assertIsInstance(obj, BuyApp, mes)

class MyTestFinanceApp(unittest.TestCase):

    def test_errore_rating(self):
        financapp = FinanceApp("BSPB", 257.7, 4.1)
        with self.assertRaises(TypeError):
            financapp.rating = "wrfef"

    # def test_check_rating(self):
    #     self.assertEqual(FinanceApp.check_rating(4.2), 4.2)

    def test_check_2(self):
        obj = FinanceApp("BSPB", 257.7, 4.1)
        mes = "обект не принадлежит к этому классу"
        self.assertIsInstance(obj, FinanceApp, mes)

class MyTestGameApp(unittest.TestCase):

    def test_errore_age(self):
        gameapp = GameApp("Jamp", 257.7, 19)
        with self.assertRaises(TypeError):
            gameapp.age = "sfsfs"

    # def test_check_age(self):
    #     self.assertEqual(GameApp.check_age(19), 19)

    def test_check_3(self):
        obj = GameApp("Jamp", 257.7, 19)
        mes = "обект не принадлежит к этому классу"
        self.assertIsInstance(obj, GameApp, mes)

if __name__ == '__main__':
    unittest.main()

