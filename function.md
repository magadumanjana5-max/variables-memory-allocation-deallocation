### 1. What is a variable in Python?

In Python, a variable is a name or reference bound to an object. An object has an identity, a type, and a value.

```python
x = 10
```

Conceptually, `x` refers to the integer object `10`. Python does not work like a simple box that contains a value.

### 2. Is everything in Python an object?

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

### 3. Python data types

Python's built-in data types include:
- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequence: `list`, `tuple`, `range`
- Set: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
- Special: `NoneType`

### 4. Numeric types

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

### 5. Boolean type

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

### 12. Mutable vs. immutable objects

**Immutable:** Objects cannot be changed after creation. Examples include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

**Mutable:** Objects can be changed after creation. Examples include `list`, `set`, `dict`, and `bytearray`.

### 13. Rebinding a variable

```python
x = 10
x = 20
```

It may look like `x` changed from `10` to `20`. Instead, `x` was rebound: first it referred to `10`, then it referred to `20`. The integer object `10` was not modified.

### 14. Names can refer to the same object

```python
a = 10
b = a
```

Conceptually, both names refer to the same integer object. If you then assign `a = 20`, `a` refers to `20`, while `b` still refers to `10`.

### 15. Mutable object example

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

### 17. Where is memory used?

At a conceptual level, a Python program uses memory for objects such as integers, strings, dictionaries, lists, and functions.

In CPython, objects are managed by Python's memory-management system. Memory is obtained from the process or operating system and allocated through Python's allocator mechanisms. Python names refer to objects, and exact implementation details can vary between Python implementations.

### 18. Reference counting in CPython

CPython primarily uses reference counting for object memory management.

```python
a = [1, 2, 3]
b = a
del b
```

Initially, both `a` and `b` refer to the same list. Deleting `b` removes that reference; `a` still refers to the list.

### 19. What is garbage collection?

Garbage collection identifies objects that are no longer needed or reachable and reclaims their memory. Python manages memory automatically, so normal Python code does not call `free()` to release objects manually.

### 20. Reference counting and the garbage collector

Reference counting tracks references to objects. Python's cyclic garbage collector can handle unreachable reference cycles that reference counting alone cannot reclaim.

```python
a = []
a.append(a)
```

The list refers to itself, creating a reference cycle. Python's cyclic garbage collector can detect and handle unreachable cycles like this.

### 21. `del` does not necessarily destroy an object

`del` removes a name or reference; it does not necessarily destroy the object immediately.

```python
numbers = [1, 2, 3]
b = numbers
del numbers
print(b)  # [1, 2, 3]
```

The list is still reachable through `b`.

### 22. When can an object become eligible for reclamation?

```python
numbers = [1, 2, 3]
b = numbers
del numbers
del b
```

After both names are deleted, there are no remaining references to the list from these names. The object becomes eligible for memory reclamation. The exact timing of reclamation, and when memory is returned or reused, depends on the implementation.

### 23. Summary: variable, object, and memory

```text
variable name -> object (identity, type, value) -> memory
                    no longer reachable -> eligible for reclamation
```

### 24. Question

If Python has garbage collection, why does `del numbers` not necessarily destroy the object immediately?
# hash it immediately
password = None
Example in Node.js:

let password = "secret123";
// hash it immediately
password = null;
This reduces the time sensitive data remains in memory.

10) Final comparison: Python vs Node.js
Python
variables store object references
memory is managed by reference counting + garbage collection
automatic cleanup happens when no references remain
Node.js
variables store values and object references in the V8 heap
memory is managed by the JavaScript engine’s garbage collector
cleanup happens when objects become unreachable
Both are automatic
Neither Python nor Node.js requires you to manually delete memory in normal programming.

Conclusion
Variables are used to hold data such as username, email, password, validation status, and form errors in a registration system. Their values are stored in memory and remain valid as long as they are referenced and in scope. Memory allocation happens when the variable is created, and memory deallocation happens automatically when the variable is no longer needed.

In Python, this is mainly done through reference counting and cyclic garbage collection. In Node.js, this is done through the V8 garbage collector.

That is why variables in both languages are safe and easy to use, even without manual memory deletion.

---------------------2nd partision---------------------------

what is a variable in python ?(type,identity,value)
ans:In python , a VARIBLE is essentially a name or reference bound to an object.
example:x=10
x->10(10 is object)
python does not work like a simple variable box containing 10 model.

2.everything in python is an object ?
ans:This an important interview concept.
x= 10
name="aishu"
marks=85.5
numbers=[10,20,30]

x->intiger object
name->string object
marks->float object
numbers->list object
objects have : identity, type and value.
you can demonstrate:
     x=10
     print(ID(X))
     print(type(x))
     print(x)
think like ID() is an identity ,type () is a type, value is an actual data.  

3.python datatypes?
ans: usefull classification  
python built-in data types
* numeric(int,float,complex)
* Boolean(bool)
* text(str)
* sequence(list, tuple ,range)
* set(set,frozenset)
* mapping (dict)
* binary(bytes,bytearrays, memory view)
* special(none type)

4.numeric types?
ans: * int
    age=25
    count=-10

   * float
    price=99.0
    percentage=88.75
  
    * complex
    z=3+4j
    
5.boolean types?
ans:is_active=true
    is_looged_in=false

example: 
    bool(0)
    bool" "
    bool("hello")

6.string
name="aishu"
string is an immutable sequence of characters.
name=[0]
name=[1]

7.list
  numbers=[10,20,30]
  properties:
   *ordered
   *mutable
   * allows duplicate
   *can contain different types
ex:data=[10, "python",25.5,TRUE]

8.TUPLE
point=(10,20)
properties:
  * ordered
  * immutable
  * allows duplicates 
9.set
example:number{10,10,20,30}
properties:
*unique elements
*mutable
*not used for positional indexing like list

10.dictionary
 ex:student={
       "id":101,
       "name":"aishu",
       "marks":"85.5"
}
it stores in key value pairs

11>none
none=name
none represents the absence of a value
do not confuse none,0,false,"",[].
they are different values or objects have different meanings.

12.mutable vs immutable
ans: immutable:
          objects cannot be changed after creation.
           ex:int,float,bool,str,tuple,frozenset.
     mutable:
          objects can be changed after creation.
           ex: list,set,dict,bytearray.
13.the object referenced by the variable is mutable or immutable
ex:x=10
    x=20
it looks like x changed from 10 tp 20
actually before x-> 10,after x->20
the integer 10 was not modify.
x was rebound to another object

14.memory example
 a=10
 b=a
conceptually  a->10,b->
both names refer to the same object conceptually.
now a=20 becomes
    10<-b
    20<-a
    b remains 10
15.mutable object example
  a=[10,20]
b=a
b.append(30)
print(a)
o/p:[10,20,30]

why??
because a ->[10,20]
b->[10,20]
both names reference the name list object
append()modifies that list



both name reference the name list objects.
append () modifies that list

16.== vs is(imp)
== checkes whether valuess are equal 
ex:a==b
is checkes whether two refernces point to the same object
a is b
ex:a[1,2]
   b=[1,2]
print(a==b) #true

print(a is b) # false

17.where is memory used ?
at a conceptual level ,python program use memory for :
     program
     	objects
	int
	string
	dict
	list
	functions
in C PYTHON ,objects are managed in python managed memory system,with memory obtained from the underlying process or OS And allocated through pythons allocator mechanisems 
"python names reference objectes and  C Python and C Python manages object memory dynamically.
the exact implementation details depend on the python implementation"

18.reference counting in CPython:CPthon primarly uses reference counting.
ex: a=[1,2,3]
    b=a
conceptually 
a -> [1,2,3]
b-> [1,2,3]
references =2
now del b
conceptually a->[1,2,3]
reference count decrease.

19.what is garbage collection?
ans: identifying objects that are no longer needed or reachable and reclaiming their memory.
python has automatic memory management.
you do not normally write free() ,
delet memory.
like in languages where manually memory managent is common.

20.reference counting +garbage collector
reference counting:
immideatly tracks references to objects CPthon 

garbage collector:
the gc module handles cyclic garbage that reference counting alone cannot reclaim.
ex:a=[]
   a.append(a)
now the list refers to itself.
this is a reference cycle.
pythons cyclic garbage collector can detect and handles such cycles.

21.del doesnot neceserly delete the objetes.
ex:a=[1,2,3]
   del a
del numbers removes the name or referance numbers.
"it dose not mean immediately destroy this object"
if another reference objects exists
numbers=[1,2,3]
b= numbers
del numbers
print(b)#[1,2,3]
the object is still reachable through b.

22.when can an object become object ?
ans: numbers=[1,2,3]
     b=a
     del numbers
     del b 
now there are no remaining references to that list from these names.
it becomes eligible memory reclamation.
the exact timing of memory being return or reused is implemention dependent.

23.variable ->object->memory->garbage collector.
ans: "variable" -> OBJECT(IDENTITY,TYPE,VALUE,)->MEMORY-> NO LONGER REACHBLE->GARBAGE COLLECTION.

24.IF python has garbage collection ,why dose not del numbers neceserly destroy the object immediately?

---

# Python Functions

## 1. Why Use Functions?

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

## 2. What Is a Function?

A function is a named, reusable block of code that performs a task. It can accept inputs, perform work, and optionally return a result.

```python
def add(a, b):
  return a + b


result = add(2, 3)
print(result)  # 5
```

## 3. Defining and Calling a Function

The `def` statement defines a function. Its body does not run just because the function was defined. Calling the function by its name followed by parentheses runs its body.

```python
def greet():
  print("Hello")


greet()  # function call; prints Hello
```

## 4. Functions Without Parameters

A function does not need parameters if it can do its task without input:

```python
def welcome():
  print("Welcome to Nighan2 Labs!")


welcome()
```

## 5. Parameters and Arguments

A parameter is a name in the function definition. An argument is the value supplied when the function is called.

```python
def welcome(name):  # name is a parameter
  print("Welcome,", name)


welcome("Sanika")  # "Sanika" is an argument
```

## 6. Multiple Parameters

A function can accept more than one parameter. Arguments are matched to parameters by position unless you use keyword arguments.

```python
def add(a, b):
  return a + b


print(add(10, 20))  # 30
```

## 7. `print()` and `return`

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

## 8. What Happens After `return`?

`return` immediately ends the current function call. Statements after it in that call are not executed. Code after the function call continues normally.

```python
def test():
  return 10
  print("This line does not run")


result = test()
print(result)       # 10
print("Hello")      # this line does run
```

## 9. Returning Multiple Values

Python can return multiple values, which are packed into a tuple. The caller can unpack that tuple into multiple names.

```python
def calculate(a, b):
  return a + b, a - b, a * b


total, difference, product = calculate(10, 5)
print(total)       # 15
print(difference)  # 5
print(product)     # 50
```

## 10. Default Parameters

A default parameter value is used when the caller leaves that argument out. Defaults are useful when one value is common but callers may provide another.

```python
def greet(name="Sanika"):
  print("Hello,", name)


greet()          # Hello, Sanika
greet("Aisha")   # Hello, Aisha
```

## 11. Positional Arguments

Positional arguments are matched to parameters by their order:

```python
def student(name, age):
  print(name, age)


student("Sanika", 21)
```

## 12. Keyword Arguments

Keyword arguments identify parameters by name, so their order does not matter:

```python
student(age=21, name="Sanika")
```

## 13. Combining Positional and Keyword Arguments

You may provide positional arguments first, followed by keyword arguments:

```python
def student(name, age, course):
  print(name, age, course)


student("Sanika", 21, course="BCA")
student(name="Sanika", age=21, course="BCA")
```

A positional argument cannot follow a keyword argument in the same call. For example, `student(name="Sanika", 21, course="BCA")` is invalid because `21` is positional and comes after a keyword argument.

## 14. `*args`: A Variable Number of Positional Arguments

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

## 15. `**kwargs`: A Variable Number of Keyword Arguments

`**kwargs` collects extra keyword arguments into a dictionary. The name `kwargs` is a convention; the `**` is what performs the collection.

```python
def show_student(**details):
  print(details)


show_student(name="Sanika", age=21, course="BCA")
# {'name': 'Sanika', 'age': 21, 'course': 'BCA'}
```

## 16. Combining Parameters, `*args`, and `**kwargs`

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

## 17. Local and Global Scope

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

## 18. The `global` Keyword

Use `global` to assign to a module-level name from inside a function. Prefer parameters and return values for reusable functions when practical.

```python
count = 0


def increment():
  global count
  count += 1


increment()
print(count)  # 1
```

## 19. A Local Name Is Not Available Outside Its Function

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

## 20. Functions Can Call Other Functions

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

## 21. Function Call Flow

When a function is called, Python passes its arguments to the parameters, runs the function body, and sends the returned value back to the caller.

```python
def multiply(a, b):
  return a * b


result = multiply(5, 4)
print(result)  # 20
```

The call `multiply(5, 4)` binds `a` to `5` and `b` to `4`. The function calculates `a * b`, returns `20`, and the assignment stores that result in `result`.

## 22. Functions Are Objects

In Python, functions are objects. Assigning a function to another name does not call it; parentheses are needed to call it.

```python
def greet():
  print("Hello")


say_hello = greet  # both names refer to the same function object
say_hello()        # calls the function and prints Hello
```

## 23. Passing a Function to Another Function

A function can be passed as an argument to another function. A function that accepts or returns another function is called a higher-order function.

```python
def square(value):
  return value * value


def process(function, value):
  return function(value)


print(process(square, 5))  # 25
```

Here, `square` is passed without parentheses, so the function itself is passed rather than its result.

## 24. Lambda Expressions

A `lambda` expression creates a small anonymous function containing one expression. It is often useful for a short operation passed to another function.

```python
square = lambda value: value * value
print(square(5))  # 25

numbers = [1, 2, 3, 4]
doubled = list(map(lambda number: number * 2, numbers))
print(doubled)  # [2, 4, 6, 8]
```

For more involved logic, use a regular `def` function with a descriptive name.

## 25. Recursion

Recursion occurs when a function calls itself. A recursive function needs a base case that stops the calls, and a recursive step that makes progress toward that case.

```python
def countdown(number):
  if number <= 0:  # base case
    return

  print(number)
  countdown(number - 1)  # recursive step


countdown(5)
```

This prints `5` through `1`. Without a reachable base case, recursion continues until Python raises `RecursionError`.

## 26. Function Documentation

A docstring is a string at the beginning of a function body that describes the function. Tools such as `help()` can display it.

```python
def add(a, b):
  """Return the sum of two numbers."""
  return a + b


print(add.__doc__)
help(add)
```

Clear docstrings are especially useful when a function's purpose or expected inputs are not obvious from its name and parameters.

## 27. Type Hints

Type hints document the kinds of values a function expects and returns. Editors and static type-checking tools can use them, but Python generally does not enforce them automatically at runtime.

```python
def add(a: int, b: int) -> int:
  return a + b


print(add(2, 3))  # 5
```

## 28. Practical Example: Electricity Bill

This example uses sample rates: the first 100 units cost 2 per unit, the next 100 cost 4 per unit, units above 200 cost 6 per unit, and a fixed charge of 100 is added. Real tariffs vary by location and provider.

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

  fixed_charge = 100
  return energy_charge + fixed_charge


units = int(input("Enter units used: "))
bill = calculate_bill(units)
print("Bill:", bill)
```

Putting the calculation in `calculate_bill()` separates it from input and output. It also makes the calculation easy to reuse and test with different unit values.

## 29. Function Design

A well-designed function usually has a clear purpose, well-defined inputs, and an understandable result or side effect. Keeping each function focused makes it easier to read, test, and maintain.

## 30. Avoid One Giant Function

A function that handles input, validation, calculations, database work, and printing is difficult to test and change. Split the work into smaller functions with clear responsibilities.

```python
def validate_student(student):
  return bool(student["name"]) and bool(student["marks"])


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

Each helper handles one part of the task. A larger application could add separate functions for collecting input and saving data, keeping those responsibilities out of the calculation and display functions.