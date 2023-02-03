import unittest
import random
from main import ElectroCar # импортируем то, что будем тестировать


class MyTestElectroCar(unittest.TestCase):

    def setUp(self):
        self.model = ["Kia", "Lada", "BMW", "Infinity", "Lexus", "Audi", "Volvo"]

    def test_doublespeed(self):
        self.assertEqual(ElectroCar.doublespeed(300, 25), 12)

    def test_acceleration(self):
        self.assertEqual(ElectroCar.acceleration(100, 20), 5)

    def test_randommodel(self):
        element = random.choice(self.model)
        self.assertTrue(element in self.model)
        self.assertFalse(element not in self.model)

    def test_errore_model(self):
        car = ElectroCar("Lada", "Black", 120)
        with self.assertRaises(TypeError):
            car.model = 1222

    def test_errore_speed(self):
        car = ElectroCar("Lada", "Black", 120)
        with self.assertRaises(TypeError):
            car.speed = "sfsfs"

    def test_errore_color(self):
        car = ElectroCar("Lada", "Black", 120)
        with self.assertRaises(TypeError):
            car.color = [1,2]

if __name__ == '__main__':
    unittest.main()

