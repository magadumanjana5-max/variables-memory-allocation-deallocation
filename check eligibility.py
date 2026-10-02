def check_eligibility(marks, attendance, has_backlog):
	if marks >= 60 and attendance >= 75 and not has_backlog:
		return "Eligible"
	return "Not eligible"


try:
	marks = float(input("Enter the student's marks: "))
	attendance = float(input("Enter the student's attendance percentage: "))
	backlog_answer = input("Does the student have any backlogs? (yes/no): ").strip().lower()

	if backlog_answer not in ("yes", "no"):
		raise ValueError

	has_backlog = backlog_answer == "yes"
	print(check_eligibility(marks, attendance, has_backlog))
except ValueError:
	print("Please enter valid numbers and answer yes or no for backlogs.")