# Variables, Memory Allocation, and Deallocation in Node.js and Python

Variables give values names so a program can read data, update its state, pass values to functions, and make decisions. In both Node.js and Python, the runtime manages memory automatically, but the details differ between V8 and Python implementations.

## A Checkout Example

An online shop needs to keep track of a cart, its items, a running total, and a discount. Variables make these values accessible by name.

### Node.js

```js
function checkout() {
	const cart = [
		{ name: "notebook", price: 5 },
		{ name: "pen", price: 2 },
	];
	let total = 0;

	for (const item of cart) {
		total += item.price;
	}

	const discount = 1;
	return total - discount;
}

const amountCharged = checkout();
```

### Python

```python
def checkout():
	cart = [
		{"name": "notebook", "price": 5},
		{"name": "pen", "price": 2},
	]
	total = 0

	for item in cart:
		total += item["price"]

	discount = 1
	return total - discount


amount_charged = checkout()
```

In each version, the function uses its local names to work with the cart and calculate the amount to charge. The returned number is bound to a name outside the function. Variables also make a program easier to organize, understand, and change.

## Names and Values

A variable is best understood as a name bound to a value, not as a box that always contains an entire object. In the checkout example, `cart` refers to an array or list. That container refers to the item objects inside it. Multiple names can refer to the same object:

```js
const first = { color: "blue" };
const second = first;
second.color = "green";
console.log(first.color); // "green": both names refer to the same object
```

```python
first = {"color": "blue"}
second = first
second["color"] = "green"
print(first["color"])  # "green": both names refer to the same object
```

Changing a mutable object through one name is visible through the other. Rebinding a name to another value does not, by itself, change the original object or remove other references to it.

The exact memory representation of a value is an implementation detail. A variable in source code does not necessarily correspond to one fixed stack slot or one heap allocation; runtimes can represent and optimize values in different ways.

## Scope and Lifetime

Scope determines where a name can be used. It does not set a fixed timer for when the underlying value's memory is reclaimed.

In the checkout functions, `cart`, `total`, and `discount` are local names. They can be used while the function executes. When it returns, those local bindings are no longer available in that scope. The returned total remains available through `amountCharged` or `amount_charged`.

An object can outlive a local name if another reference remains. A closure, for example, can keep access to a local value after the function that created it has returned:

```js
function makeCounter() {
	let count = 0;
	return () => ++count;
}

const next = makeCounter();
console.log(next()); // 1; the closure still refers to count
```

```python
def make_counter():
	count = 0

	def next_value():
		nonlocal count
		count += 1
		return count

	return next_value


next_value = make_counter()
print(next_value())  # 1; the closure still refers to count
```

## Memory Allocation in Node.js

Node.js runs JavaScript using the V8 engine. As the program creates and uses values, V8 arranges the storage needed for them. Objects and dynamically sized data are generally managed in the garbage-collected heap, but the engine may optimize or represent values in other ways. Declaring a variable creates a binding according to JavaScript's scope rules; it does not guarantee a particular physical memory location.

`let` and `const` are block-scoped, while `var` is function-scoped (or module/global scoped, depending on context). `const` prevents rebinding the name, but it does not make the referenced object immutable:

```js
const item = { count: 1 };
item.count = 2; // allowed: the object is mutable
// item = {};   // TypeError: the const binding cannot be reassigned
```

## Memory Allocation in Python

Python assignment binds a name to an object. Creating a list, dictionary, or other object causes the Python implementation to obtain the memory it needs. In the commonly used CPython implementation, Python's memory manager handles object allocations and may use pools and arenas for small objects. Other Python implementations can manage memory differently.

```python
items = [1, 2, 3]
alias = items
alias.append(4)
print(items)  # [1, 2, 3, 4]
```

There is one list object here, referred to by both `items` and `alias`. Reassigning or deleting one name does not remove the other name's reference.

## Memory Deallocation in Node.js

V8 uses garbage collection to identify objects that can no longer be reached from live program references, such as active variables and runtime-held state. When an object becomes unreachable, it is eligible for collection. V8 chooses when collection happens; JavaScript does not provide a standard command to immediately free an individual object's memory.

```js
let data = { values: [1, 2, 3] };
let alias = data;

data = null; // alias still refers to the object
console.log(alias.values); // [1, 2, 3]

alias = null; // the object is now eligible for garbage collection
```

Setting a name to `null` removes that reference, but does not force collection. Other references, including retained event listeners or caches, can keep objects alive and contribute to memory growth.

## Memory Deallocation in Python

When a name is rebound, deleted, or leaves its scope, that particular reference is removed. An object can be reclaimed when it is no longer reachable or otherwise in use.

In CPython, reference counting usually reclaims an object when its reference count reaches zero. A cyclic garbage collector also finds certain unreachable groups of objects that refer to one another. Python as a language does not require CPython's specific strategy, and code should not depend on an exact collection time.

```python
data = [1, 2, 3]
alias = data
del data  # removes the name data; alias still refers to the list
print(alias)  # [1, 2, 3]

del alias  # neither of these names now refers to the list
```

`del` removes a binding; it is not a command to return a particular block of memory to the operating system immediately.

## Reclaimed Memory and Process Memory

When an object is reclaimed, its storage can become available for reuse by the runtime. The process's memory usage reported by the operating system does not have to decrease immediately: the runtime may keep allocated regions for future objects. Garbage collection can also happen later, when the runtime determines it is useful.

| Question | Practical answer |
|---|---|
| Does a variable have a fixed expiration time? | No. Scope controls where a name is usable; references and runtime behavior affect an object's lifetime. |
| Does leaving a function always destroy its values? | No. A return value, closure, or other reference can keep a value alive. |
| Does `del` or assigning `null` immediately free memory? | No. These remove references; the runtime manages reclamation. |
| Can ordinary code choose exactly when memory returns to the OS? | Generally no. Do not rely on immediate collection or a drop in process memory. |

## Review Questions and Answers

1. **What is a variable, and what is it used for?**  
   A variable is a name bound to a value. It lets a program access, update, and pass data.

2. **How does a variable name relate to the value it refers to?**  
   The name is a binding or reference that lets the program access the value; it is not necessarily a box containing the entire object.

3. **What happens when two variables refer to the same mutable object?**  
   A change made to that object through either name is visible through the other name.

4. **How does reassigning a variable differ from changing a mutable object?**  
   Reassigning changes which value a name refers to. Mutating changes the object itself, which can be observed through every reference to it.

5. **What is scope?**  
   Scope is the part of a program where a particular name can be used.

6. **When do local variable names in a function stop being usable?**  
   Ordinarily, they stop being usable from outside their local scope when the function returns.

7. **Can an object remain alive after the function that created it returns? How?**  
   Yes. A returned reference, closure, or another reachable object can continue referring to it.

8. **What is a closure, and how can it keep a local value accessible?**  
   A closure is a function that retains access to variables from its surrounding scope, even after that scope's function has returned.

9. **What does `const` prevent in JavaScript?**  
   It prevents reassignment of the `const` binding after initialization.

10. **Does `const` make an object immutable?**  
	No. The binding cannot be reassigned, but the referenced object's properties can still be changed if the object is mutable.

11. **What is the difference between `let` and `var` in JavaScript scope?**  
	`let` is block-scoped; `var` is function-scoped, or module/global scoped depending on context.

12. **Which JavaScript engine does Node.js use?**  
	Node.js uses the V8 JavaScript engine.

13. **How does V8 generally manage objects and dynamically sized data?**  
	They are generally managed in a garbage-collected heap, though V8 may optimize or represent values differently.

14. **Why should you not assume each variable maps to a specific stack slot or heap allocation?**  
	Memory representation is an implementation detail, and the runtime may optimize how values are stored.

15. **How does Python assignment associate a name with an object?**  
	Assignment binds the name to the object; it does not necessarily copy the object.

16. **What happens when two Python names refer to the same list?**  
	Both names refer to that one list, so modifying it through either name is visible through the other.

17. **How does CPython commonly manage object memory?**  
	CPython uses its memory manager, which may use pools and arenas for small allocations.

18. **What role does reference counting play in CPython?**  
	It tracks references to objects and usually reclaims an object when its reference count reaches zero.

19. **What problem does CPython's cyclic garbage collector address?**  
	It finds certain unreachable groups of objects that refer to one another in cycles.

20. **What does Python's `del` statement do to a name?**  
	It removes that name's binding. It does not necessarily destroy the object if other references remain.

21. **Does assigning `null` in JavaScript immediately free an object's memory?**  
	No. It removes that reference; the object may be collected only when it is unreachable, and collection timing is controlled by the runtime.

22. **How does garbage collection determine whether an object can be reclaimed?**  
	It identifies objects that can no longer be reached from live program references and runtime-held state.

23. **Why might reported process memory not decrease after an object is reclaimed?**  
	The runtime may retain the freed memory for reuse instead of returning it to the operating system immediately.

24. **Why should programs avoid relying on an exact garbage-collection time?**  
	The runtime chooses when to collect; the language does not generally guarantee immediate reclamation or a specific memory decrease.

## Summary

Variables are names bound to values or objects. Scope determines how long a name can be used; whether an object can be reclaimed depends on whether it remains reachable and on the runtime's memory manager. Node.js relies on V8 garbage collection. CPython primarily uses reference counting plus cyclic garbage collection, while other Python implementations may differ. In either language, do not rely on an exact memory cleanup time. Release external resources such as files and network connections explicitly with the appropriate resource-management tools.
 