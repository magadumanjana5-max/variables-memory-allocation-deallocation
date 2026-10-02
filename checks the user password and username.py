def validate_user(username, password):
	if username == "admin" and password == "python 123":
		return "Valid user"
	return "Invalid user"


username = input("Enter username: ")
password = input("Enter password: ")
print(validate_user(username, password))