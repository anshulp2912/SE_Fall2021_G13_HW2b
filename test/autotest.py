import unittest
from code import calculator

class TestCalculator(unittest.TestCase):
	def setUp(self):
		self.calc=calculator()
	
	def test_add(self):
		self.assertEqual(self.calc.add(4,7), 11)
	
	def test_subtract(self):
		self.assertEqual(self.calc.subtract(10,5), 5)
	
	def test_multiply(self):
		self.assertEqual(self.calc.multiply(3,7), 21)
	
	def test_divide(self):
		self.assertEqual(self.calc.divide(10,2), 5)   
    
if __name__ == "__main__":
  unittest.main()
