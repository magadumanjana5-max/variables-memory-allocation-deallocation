def calculator(first_number, second_number):
	results = {
		"Addition": first_number + second_number,
		"Subtraction": first_number - second_number,
		"Multiplication": first_number * second_number,
	}

	if second_number == 0:
		results["Division"] = "undefined (cannot divide by zero)"
		results["Floor division"] = "undefined (cannot divide by zero)"
		results["Remainder"] = "undefined (cannot divide by zero)"
	else:
		results["Division"] = first_number / second_number
		results["Floor division"] = first_number // second_number
		results["Remainder"] = first_number % second_number

	return results


try:
	first_number = float(input("Enter the first number: "))
	second_number = float(input("Enter the second number: "))

	for operation, result in calculator(first_number, second_number).items():
		print(f"{operation}: {result}")
except ValueError:
	print("Please enter valid numbers.")
