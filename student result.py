def get_result(marks):
	if marks >= 75:
		return "Distinction"
	if marks >= 35:
		return "Pass"
	return "Fail"


try:
	marks = float(input("Enter the student's marks: "))
	print(get_result(marks))
except ValueError:
	print("Please enter valid marks.")