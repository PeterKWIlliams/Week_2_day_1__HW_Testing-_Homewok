import unittest 

from src.calculator import add, divide, multiply, subtract 


class TestCalculator(unittest.TestCase):
      

    def test_add(self):
      self.assertEqual(10,add(5,5))
    #   expected = 5 
    #   actual = add(5,5)
    #   self.assertEqual(expected,actual)

    def test_subtract(self):
        self.assertEqual(10,subtract(20,10))

    def test_divide(self):
        self.assertEqual(2,divide(20,10))

    def test_multiply(self):
        self.assertEqual(10,multiply(2,5))    