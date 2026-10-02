def check_access(age, has_id, is_employee):
	if (age >= 18 and has_id) or is_employee:
		return "Access granted"
	return "Access denied"


try:
	age = int(input("Enter your age: "))
	has_id_answer = input("Do you have an ID? (yes/no): ").strip().lower()
	employee_answer = input("Are you an employee? (yes/no): ").strip().lower()

	if has_id_answer not in ("yes", "no") or employee_answer not in ("yes", "no"):
		raise ValueError

	has_id = has_id_answer == "yes"
	is_employee = employee_answer == "yes"
	print(check_access(age, has_id, is_employee))
except ValueError:
	print("Please enter a valid age and answer yes or no.")