# Python Fundamentals: Variables, Memory, and Functions

This guide introduces Python names and objects, memory management, and functions, with examples throughout.

## Variables, Objects, and Memory

### 1. What Is a Variable in Python?

In Python, a variable is a name or reference bound to an object. An object has an identity, a type, and a value.

```python
x = 10
```

Conceptually, `x` refers to the integer object `10`. Python does not work like a simple box that contains a value.

### 2. Is Everything in Python an Object?

This is an important Python concept. Values such as integers, strings, floats, and lists are objects:

```python
x = 10
name = "aishu"
marks = 85.5
numbers = [10, 20, 30]
```

Conceptually:
- `x` refers to an integer object.
- `name` refers to a string object.
- `marks` refers to a float object.
- `numbers` refers to a list object.

Objects have an identity, a type, and a value. You can inspect them with:

```python
x = 10
print(id(x))
print(type(x))
print(x)
```

Here, `id()` provides an object's identity, `type()` reports its type, and printing `x` displays its value.

### 3. Python Data Types

Python's built-in data types include:
- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequence: `list`, `tuple`, `range`
- Set: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
- Special: `NoneType`

### 4. Numeric Types

```python
# int
age = 25
count = -10

# float
price = 99.0
percentage = 88.75

# complex
z = 3 + 4j
```

### 5. Boolean Type

Python Boolean values are `True` and `False` (capitalized):

```python
is_active = True
is_logged_in = False

print(bool(0))
print(bool(""))
print(bool("hello"))
```

### 6. Strings

```python
name = "aishu"
```

A string is an immutable sequence of characters. Individual characters can be accessed by index:

```python
print(name[0])
print(name[1])
```

### 7. Lists

```python
numbers = [10, 20, 30]
data = [10, "python", 25.5, True]
```

Lists are:
- Ordered
- Mutable
- Able to contain duplicate values
- Able to contain values of different types

### 8. Tuples

```python
point = (10, 20)
```

Tuples are ordered and immutable, and they can contain duplicate values.

### 9. Sets

```python
numbers = {10, 10, 20, 30}
```

Sets are mutable collections of unique elements. They are not used for positional indexing like lists. Duplicate values are stored only once.

### 10. Dictionaries

```python
student = {
  "id": 101,
  "name": "aishu",
  "marks": 85.5,
}
```

A dictionary stores key-value pairs.

### 11. `None`

```python
name = None
```

`None` represents the absence of a value. Do not confuse it with `0`, `False`, `""`, or `[]`; they are different values with different meanings.

### 12. Mutable vs. Immutable Objects

**Immutable:** Objects cannot be changed after creation. Examples include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

**Mutable:** Objects can be changed after creation. Examples include `list`, `set`, `dict`, and `bytearray`.

### 13. Rebinding a Variable

```python
x = 10
x = 20
```

It may look like `x` changed from `10` to `20`. Instead, `x` was rebound: first it referred to `10`, then it referred to `20`. The integer object `10` was not modified.

### 14. Names Can Refer to the Same Object

```python
a = 10
b = a
```

Conceptually, both names refer to the same integer object. If you then assign `a = 20`, `a` refers to `20`, while `b` still refers to `10`.

### 15. Mutable Object Example

```python
a = [10, 20]
b = a
b.append(30)
print(a)
```

Output:

```text
[10, 20, 30]
```

Both names refer to the same list object. `append()` modifies that list, so the change is visible through either name.

### 16. `==` vs. `is`

- `==` checks whether two values are equal.
- `is` checks whether two names refer to the same object.

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: the values are equal
print(a is b)  # False: these are different list objects
```

### 17. Where Is Memory Used?

At a conceptual level, a Python program uses memory for objects such as integers, strings, dictionaries, lists, and functions.

In CPython, objects are managed by Python's memory-management system. Memory is obtained from the process or operating system and allocated through Python's allocator mechanisms. Python names refer to objects, and exact implementation details can vary between Python implementations.

### 18. Reference Counting in CPython

CPython primarily uses reference counting for object memory management.

```python
a = [1, 2, 3]
b = a
del b
```

Initially, both `a` and `b` refer to the same list. Deleting `b` removes that reference; `a` still refers to the list.

### 19. What Is Garbage Collection?

Garbage collection identifies objects that are no longer needed or reachable and reclaims their memory. Python manages memory automatically, so normal Python code does not call `free()` to release objects manually.

### 20. Reference Counting and the Garbage Collector

Reference counting tracks references to objects. Python's cyclic garbage collector can handle unreachable reference cycles that reference counting alone cannot reclaim.

```python
a = []
a.append(a)
```

The list refers to itself, creating a reference cycle. Python's cyclic garbage collector can detect and handle unreachable cycles like this.

### 21. `del` Does Not Necessarily Destroy an Object

`del` removes a name or reference; it does not necessarily destroy the object immediately.

```python
numbers = [1, 2, 3]
b = numbers
del numbers
print(b)  # [1, 2, 3]
```

The list is still reachable through `b`.

### 22. When Can an Object Become Eligible for Reclamation?

```python
numbers = [1, 2, 3]
b = numbers
del numbers
del b
```

After both names are deleted, there are no remaining references to the list from these names. The object becomes eligible for memory reclamation. The exact timing of reclamation, and when memory is returned or reused, depends on the implementation.

### 23. Summary: Variable, Object, and Memory

```text
variable name -> object (identity, type, value) -> memory
                    no longer reachable -> eligible for reclamation
```

### 24. Why Does `del` Not Necessarily Destroy an Object Immediately?

`del` removes a name or reference. The object can remain alive if another reference still reaches it. Once an object is no longer reachable, it may become eligible for reclamation, but the exact timing and whether memory is returned to the operating system depend on the Python implementation and allocator.

In CPython, reference counting commonly reclaims objects promptly when their reference count reaches zero. Its cyclic garbage collector handles some unreachable cycles. JavaScript in Node.js uses V8's garbage collector instead. Neither language promises that setting a name to `None` or `null` securely erases sensitive data from memory.

---

## Python Functions

### 1. Why Use Functions?

If the same steps are needed several times, writing them repeatedly makes code harder to update. A function lets you give those steps a name and reuse them.

Without a function:

```python
print("Welcome, Sanika!")
print("Welcome, S_K!")
print("Welcome, S_K_K!")
```

With a function:

```python
def welcome(name):
  print("Welcome,", name)


welcome("Sanika")
welcome("S_K")
welcome("S_K_K")
```

Functions help with code reuse, reducing repetition, organizing code, maintenance, and testing.

### 2. What Is a Function?

A function is a named, reusable block of code that performs a task. It can accept inputs, perform work, and optionally return a result.

```python
def add(a, b):
  return a + b


result = add(2, 3)
print(result)  # 5
```

### 3. Defining and Calling a Function

The `def` statement defines a function. Its body does not run just because the function was defined. Calling the function by its name followed by parentheses runs its body.

```python
def greet():
  print("Hello")


greet()  # function call; prints Hello
```

### 4. Functions Without Parameters

A function does not need parameters if it can do its task without input:

```python
def welcome():
  print("Welcome to Nighan2 Labs!")


welcome()
```

### 5. Parameters and Arguments

A parameter is a name in the function definition. An argument is the value supplied when the function is called.

```python
def welcome(name):  # name is a parameter
  print("Welcome,", name)


welcome("Sanika")  # "Sanika" is an argument
```

### 6. Multiple Parameters

A function can accept more than one parameter. Arguments are matched to parameters by position unless you use keyword arguments.

```python
def add(a, b):
  return a + b


print(add(10, 20))  # 30
```

### 7. `print()` and `return`

`print()` displays information. `return` sends a value back to the caller so the program can store it, use it in another calculation, or display it later.

```python
def add_and_print(a, b):
  print(a + b)


def add_and_return(a, b):
  return a + b


add_and_print(10, 20)  # displays 30; returns None
result = add_and_return(10, 20)
print(result)  # displays 30
```

Use `return` when the caller needs the result. A function that only prints a result is less reusable in other calculations.

### 8. What Happens After `return`?

`return` immediately ends the current function call. Statements after it in that call are not executed. Code after the function call continues normally.

```python
def test():
  return 10
  print("This line does not run")


result = test()
print(result)       # 10
print("Hello")      # this line does run
```

### 9. Returning Multiple Values

Python can return multiple values, which are packed into a tuple. The caller can unpack that tuple into multiple names.

```python
def calculate(a, b):
  return a + b, a - b, a * b


total, difference, product = calculate(10, 5)
print(total)       # 15
print(difference)  # 5
print(product)     # 50
```

### 10. Default Parameters

A default parameter value is used when the caller leaves that argument out. Defaults are useful when one value is common but callers may provide another.

```python
def greet(name="Sanika"):
  print("Hello,", name)


greet()          # Hello, Sanika
greet("Aisha")   # Hello, Aisha
```

### 11. Positional Arguments

Positional arguments are matched to parameters by their order:

```python
def student(name, age):
  print(name, age)


student("Sanika", 21)
```

### 12. Keyword Arguments

Keyword arguments identify parameters by name, so their order does not matter:

```python
student(age=21, name="Sanika")
```

### 13. Combining Positional and Keyword Arguments

You may provide positional arguments first, followed by keyword arguments:

```python
def student(name, age, course):
  print(name, age, course)


student("Sanika", 21, course="BCA")
student(name="Sanika", age=21, course="BCA")
```

A positional argument cannot follow a keyword argument in the same call. For example, `student(name="Sanika", 21, course="BCA")` is invalid because `21` is positional and comes after a keyword argument.

### 14. `*args`: A Variable Number of Positional Arguments

`*args` collects extra positional arguments into a tuple. The name `args` is a convention; the `*` is what performs the collection.

```python
def add(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total


print(add(10, 20))          # 30
print(add(10, 20, 30))      # 60
print(add(1, 2, 3, 4, 5))   # 15
```

### 15. `**kwargs`: A Variable Number of Keyword Arguments

`**kwargs` collects extra keyword arguments into a dictionary. The name `kwargs` is a convention; the `**` is what performs the collection.

```python
def show_student(**details):
  print(details)


show_student(name="Sanika", age=21, course="BCA")
# {'name': 'Sanika', 'age': 21, 'course': 'BCA'}
```

### 16. Combining Parameters, `*args`, and `**kwargs`

A function can combine required parameters, default parameters, extra positional arguments, and extra keyword arguments in this order:

```python
def example(a, b=10, *args, **kwargs):
  print("a:", a)
  print("b:", b)
  print("extra positional:", args)
  print("extra keyword:", kwargs)


example(1, 2, 3, 4, city="London")
```

Here, `a` is `1`, `b` is `2`, `args` is `(3, 4)`, and `kwargs` is `{"city": "London"}`.

### 17. Local and Global Scope

A variable assigned inside a function is local to that function unless declared otherwise. A function can read a global variable, but relying on mutable global state can make programs harder to understand and test.

```python
def show_local():
  message = "I am local"
  print(message)


show_local()
```

This function can read a global name:

```python
message = "I am global"


def show_global():
  print(message)


show_global()
```

### 18. The `global` Keyword

Use `global` to assign to a module-level name from inside a function. Prefer parameters and return values for reusable functions when practical.

```python
count = 0


def increment():
  global count
  count += 1


increment()
print(count)  # 1
```

### 19. A Local Name Is Not Available Outside Its Function

The following raises `NameError` because `value` is local to `test()` and is not defined in the surrounding scope:

```python
def test():
  value = 10


test()
print(value)  # NameError
```

To use a function's result outside it, return the value:

```python
def test():
  value = 10
  return value


result = test()
print(result)  # 10
```

### 20. Functions Can Call Other Functions

Functions can divide a larger task into smaller steps. One function can call another and use its return value:

```python
def calculate_total(price, tax):
  return price + tax


def display_total(total):
  print("Total:", total)


def main():
  total = calculate_total(20, 2)
  display_total(total)


main()
```

A larger program might follow a flow such as:

```text
main() -> validate() -> calculate() -> save() -> display()
```

Each function handles one clear responsibility, making the program easier to read, test, and maintain.

## Function Review Questions and Answers

1. **What happens when a function is called?**  
   Python matches arguments to parameters, executes the function body, and gives the returned value back to the caller.

   ```python
   def multiply(a, b):
       return a * b


   result = multiply(5, 4)
   print(result)  # 20
   ```

2. **Can a function be assigned to another variable?**  
   Yes. Functions are objects in Python. Assigning one to another name does not call it; use parentheses to call it.

   ```python
   def greet():
       print("Hello")


   say_hello = greet
   say_hello()
   ```

3. **What is a higher-order function?**  
   It is a function that accepts another function as an argument or returns a function.

   ```python
   def square(value):
       return value * value


   def process(function, value):
       return function(value)


   print(process(square, 5))  # 25
   ```

4. **What is a lambda expression?**  
   A `lambda` creates a small anonymous function with one expression. Use a named `def` function when the logic needs more than a simple expression.

   ```python
   square = lambda value: value * value
   print(square(5))  # 25

   numbers = [1, 2, 3, 4]
   doubled = list(map(lambda number: number * 2, numbers))
   print(doubled)  # [2, 4, 6, 8]
   ```

5. **What is recursion, and what does a recursive function need?**  
   Recursion is when a function calls itself. It needs a base case to stop and a recursive step that moves toward that case.

   ```python
   def countdown(number):
       if number <= 0:  # base case
           return

       print(number)
       countdown(number - 1)


   countdown(5)  # prints 5 through 1
   ```

6. **What is a docstring?**  
   A docstring is a string at the start of a function body that documents the function. It can be accessed through `__doc__` or shown with `help()`.

   ```python
   def add(a, b):
       """Return the sum of two numbers."""
       return a + b


   print(add.__doc__)
   ```

7. **What do type hints do?**  
   Type hints document intended parameter and return types. Editors and type checkers can use them, but Python does not generally enforce them at runtime.

   ```python
   def add(a: int, b: int) -> int:
       return a + b
   ```

8. **How can a function make an electricity-bill calculation reusable?**  
   Put the calculation in a function that accepts units and returns the bill. These sample rates charge 2 per unit for the first 100 units, 4 for the next 100, 6 for additional units, plus a fixed charge of 100. Actual rates vary by provider.

   ```python
   def calculate_bill(units):
       if units < 0:
           raise ValueError("Units cannot be negative")

       if units <= 100:
           energy_charge = units * 2
       elif units <= 200:
           energy_charge = 100 * 2 + (units - 100) * 4
       else:
           energy_charge = 100 * 2 + 100 * 4 + (units - 200) * 6

       return energy_charge + 100


   print(calculate_bill(150))  # 500
   ```

9. **What makes a function well designed?**  
   It has a clear purpose, well-defined inputs, and an understandable return value or side effect. Focused functions are easier to read, test, and maintain.

10. **Why should a program avoid one giant function?**  
    A function that handles input, validation, calculations, storage, and display is difficult to test and change. Divide the work into focused helpers.

    ```python
    def validate_student(student):
        return bool(student.get("name")) and bool(student.get("marks"))


    def calculate_average(marks):
        return sum(marks) / len(marks)


    def display_student(student, average):
        print("Student:", student["name"])
        print("Average:", average)


    def student_system(student):
        if not validate_student(student):
            print("Student data is incomplete")
            return

        average = calculate_average(student["marks"])
        display_student(student, average)


    student_system({"name": "Sanika", "marks": [85, 90, 95]})
    ```

    Each helper handles one responsibility. A larger program can add separate functions for collecting input and saving data.