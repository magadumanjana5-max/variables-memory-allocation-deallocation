def calculate(a, operator, b):
	if operator not in ("+", "-", "*", "/", "//", "%", "**"):
		return "Invalid operator"

	try:
		if operator == "+":
			return a + b
		if operator == "-":
			return a - b
		if operator == "*":
			return a * b
		if operator == "/":
			return a / b
		if operator == "//":
			return a // b
		if operator == "%":
			return a % b
		return a ** b
	except ZeroDivisionError:
		return "Cannot divide by zero"


try:
	a = float(input("Enter the first number: "))
	operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
	b = float(input("Enter the second number: "))
	print(calculate(a, operator, b))
except ValueError:
	print("Please enter valid numbers.")