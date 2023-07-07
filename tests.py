import unittest
from car import Car

class TestCarClass(unittest.TestCase):
    def test_constructor(self):
        car = Car("blue",200)
        assert car.color == "blue"
        assert car.cost == 200
    
    def test_change_color(self):
        car = Car("blue",200)
        car.change_color("green")
        self.assertEqual(car.color,"green")

if __name__ == "__main__":
    unittest.main()