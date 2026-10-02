def check_number(number):
	return {
		"even or odd": "Even" if number % 2 == 0 else "Odd",
		"Divisible by 3": number % 3 == 0,
		"Divisible by 5": number % 5 == 0,
	}


try:
	number = int(input("Enter an integer: "))
	for check, result in check_number(number).items():
		print(f"{check}: {result}")
except ValueError:
	print("Please enter a valid integer.")