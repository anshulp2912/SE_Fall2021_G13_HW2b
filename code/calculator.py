class calculator:
	@staticmethod
	def add(num1, num2):
		return (num1 + num2)

	@staticmethod
	def subtract(num1, num2):
		return (num1 - num2)
	
	@staticmethod
	def multiply(num1, num2):
		return (num1 * num2)

	@staticmethod
	def divide(num1, num2):
		if num2==0:
			return "You can't divide by zero!"
		return (num1 / num2)
	
	