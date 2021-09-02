class Calculator:
	@staticmethod
	def add(num1, num2):
		if (type(num1) == int or float) and (type(num2) == int or float):
			return (num1 + num2)
		else:
			return 'Invalid: Please enter a valid number'

	@staticmethod
	def subtract(num1, num2):
		if (type(num1) == int or float) and (type(num2) == int or float):
			return (num1 - num2)
		else:
			return 'Invalid: Please enter a valid number'
	
	@staticmethod
	def multiply(num1, num2):
		if (type(num1) == int or float) and (type(num2) == int or float):
			return (num1 * num2)
		else:
			return 'Invalid: Please enter a valid number'

	@staticmethod
	def divide(num1, num2):
		if (type(num1) == int or float) and (type(num2) == int or float):
			if num2==0:
				return "You can't divide by zero!"
			return (num1 / num2)
		else:
			return 'Invalid: Please enter a valid number'	