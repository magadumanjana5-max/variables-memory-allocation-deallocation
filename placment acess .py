def assess_placement(age, marks, attendance, experience, has_backlog):
	if experience < 0:
		raise ValueError("Experience cannot be negative.")

	placement_eligible = marks >= 60 and attendance >= 75 and not has_backlog

	if experience == 0:
		category = "Fresher"
	elif experience <= 2:
		category = "Junior"
	else:
		category = "Experienced"

	return {
		"Placement eligible": "Yes" if placement_eligible else "No",
		"Candidate category": category,
	}


try:
	age = int(input("Enter the candidate's age: "))
	marks = float(input("Enter the candidate's marks: "))
	attendance = float(input("Enter the candidate's attendance percentage: "))
	experience = float(input("Enter the candidate's experience in years: "))
	backlog_answer = input("Does the candidate have a backlog? (yes/no): ").strip().lower()

	if backlog_answer not in ("yes", "no"):
		raise ValueError("Please answer yes or no for backlog status.")

	has_backlog = backlog_answer == "yes"
	for result, value in assess_placement(
		age, marks, attendance, experience, has_backlog
	).items():
		print(f"{result}: {value}")
except ValueError as error:
	print(error if str(error) else "Please enter valid numeric values.")