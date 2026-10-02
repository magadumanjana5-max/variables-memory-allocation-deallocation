# Python Operators and Function Logic

Python operators are symbols used to perform operations on values and variables. They help in calculations, comparisons, conditions, and decision-making.

## 1. Types of operators in Python

### Arithmetic operators
These operators are used for mathematical calculations.

- `+` : addition
- `-` : subtraction
- `*` : multiplication
- `/` : division
- `//` : floor division
- `%` : modulus (remainder)
- `**` : exponentiation

Example:

- `10 + 5` gives `15`
- `10 - 5` gives `5`
- `10 * 5` gives `50`
- `10 / 5` gives `2.0`
- `10 // 3` gives `3`
- `10 % 3` gives `1`
- `2 ** 3` gives `8`

### Assignment operators
These operators assign values to variables.

- `=` assigns a value
- `+=` adds and then assigns
- `-=` subtracts and then assigns
- `*=` multiplies and then assigns
- `/=` divides and then assigns

Example:

- `x = 10`
- `x += 5` means `x = x + 5`

### Comparison operators
These operators compare two values and return either `True` or `False`.

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

Example:

- `5 == 5` is `True`
- `4 > 7` is `False`

### Logical operators
These are used to combine conditional statements.

- `and` : both conditions must be `True`
- `or` : at least one condition must be `True`
- `not` : reverses a condition

Example:

- `age >= 18 and has_id == True`
- `marks >= 60 or attendance >= 75`

### Identity operators
These compare object identity.

- `is` checks if both values are the same object
- `is not` checks if they are not the same object

### Membership operators
These check whether a value exists in a sequence.

- `in`
- `not in`

Example:

- `"a" in "admin"` is `True`

### Bitwise operators
These work on binary digits.

- `&` AND
- `|` OR
- `^` XOR
- `~` NOT
- `<<` left shift
- `>>` right shift

### Ternary operator
This is a short form of an `if-else` statement.

Syntax:

`value_if_true if condition else value_if_false`

Example:

`result = "Pass" if marks >= 35 else "Fail"`

---

## 2. Function logic explained

### Task 1: Calculator function
Purpose:
A calculator function performs arithmetic operations on two numbers and returns the result.

Logic:
- Add two numbers using `+`
- Subtract using `-`
- Multiply using `*`
- Divide using `/`
- Floor division using `//`
- Find remainder using `%`
- If the second number is `0`, then division is invalid, so the program handles it safely

Example logic:

- `Addition = a + b`
- `Subtraction = a - b`
- `Multiplication = a * b`
- `Division = a / b` if `b != 0`
- `Floor division = a // b` if `b != 0`
- `Remainder = a % b` if `b != 0`

This is why the program checks `if second_number == 0` before division operations.

### Task 2: Even/odd and divisibility check
Purpose:
A function accepts an integer and checks:
- whether it is even or odd
- whether it is divisible by 3
- whether it is divisible by 5

Logic:
- If `number % 2 == 0`, it is even
- Otherwise it is odd
- If `number % 3 == 0`, it is divisible by 3
- If `number % 5 == 0`, it is divisible by 5

This function uses the modulus operator `%`, which gives the remainder after division. If the remainder is `0`, the number is divisible by that value.

### Task 3: Student pass/fail and distinction logic
Purpose:
A function takes student marks and decides the result.

Logic:
- If `marks >= 75`, result is `Distinction`
- Else if `marks >= 35`, result is `Pass`
- Else result is `Fail`

This is a typical decision tree using `if` and `elif` conditions.

### Task 4: Student eligibility check
Purpose:
The function checks if a student is eligible based on marks, attendance, and backlog status.

Logic:
- Student is eligible only if:
  - `marks >= 60`
  - `attendance >= 75`
  - `backlogs == False`

Condition:

`marks >= 60 and attendance >= 75 and backlogs == False`

If all three are true, return `Eligible`; otherwise return `Not Eligible`.

### Task 5: Username and password validation
Purpose:
This function validates login credentials.

Logic:
- Username must be exactly `"admin"`
- Password must be exactly `"python 123"`

Condition:

`username == "admin" and password == "python 123"`

If both are true, the user is valid; otherwise, the user is invalid.

### Task 6: Discount calculation
Purpose:
A function accepts the purchase amount and calculates the discount based on the total price.

Logic:
- If purchase amount is `>= 5000`, discount is `20%`
- If amount is between `3000` and `4999`, discount is `10%`
- If amount is below `3000`, discount is `5%`

Formula:

- `discount_amount = purchase_amount * discount_rate`
- `final_payable = purchase_amount - discount_amount`

This function uses conditional checks to choose the right discount percentage.

### Task 7: Access control logic
Purpose:
The function decides whether a person is allowed access.

Logic:
- Access is granted if:
  - `age >= 18 and has_id == True`
  - OR `is_employee == True`

Condition:

`(age >= 18 and has_id == True) or is_employee == True`

This means a person may enter either by being an adult with an ID or by being an employee.

### Task 8: Calculator with variable operator
Purpose:
This function accepts `a`, an operator, and `b`, then performs the required operation.

Supported operators:
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division
- `%` modulus
- `**` exponentiation

Logic:
- Check the operator value
- Perform the matching operation
- If the operator is invalid, print a message like `Invalid operator`
- If `b == 0` and division-based operators are used, handle it safely to avoid runtime errors

This is a smart function because it works with different operators using a single condition-based structure.

### Task 9: Placement eligibility and category prediction
Purpose:
This function checks whether a candidate is eligible for placement and then determines their experience category.

Eligibility condition:
- `marks >= 60`
- `attendance >= 75`
- `has_backlog == False`

If all conditions are true, the candidate is placement eligible.

Then the function classifies the candidate:
- `experience == 0` → `Fresher`
- `1 <= experience <= 2` → `Junior`
- `experience > 2` → `Experienced`

Final output:
- `Placement Eligible: Yes/No`
- `Candidate Category: Fresher/Junior/Experienced`

This function combines both condition checking and category selection.

---

## 3. Summary
Python functions depend on operators and conditions to make decisions. Arithmetic operators perform calculations, comparison operators test values, and logical operators combine conditions. By combining these tools with `if`, `elif`, and `else`, we can build real-world decision-making programs such as calculators, school result systems, login checks, discount logic, access control, and placement eligibility systems.

In simple words:
- operators help us compute and compare values
- functions organize these steps into reusable blocks
- conditions decide the flow of the program

This is the core logic behind almost every real-world Python program.
