# Python Fundamentals Cheat Sheet

Use this as a reference while working.

**Table of Contents:**

- [Data Types and Variables](#data-types-and-variables)
  - [Data Types](#data-types)
  - [Operators](#operators)
  - [Variables and Scope](#variables-and-scope)
- [Functions](#functions)
  - [Defining Functions](#defining-functions)
  - [Parameters, Arguments, and Return Values](#parameters-arguments-and-return-values)
- [Strings](#strings)
  - [String Basics](#string-basics)
  - [String Methods](#string-methods)
- [Conditional Statements](#conditional-statements)
- [Loops](#loops)
- [Modules and the Ecosystem](#modules-and-the-ecosystem)
  - [Modules](#modules)
  - [User Input](#user-input)
  - [Files and JSON](#files-and-json)
  - [venv, pip, and requirements.txt](#venv-pip-and-requirementstxt)
- [Lists](#lists)
  - [List Basics](#list-basics)
  - [Mutating Lists](#mutating-lists)
  - [References and Pure Functions](#references-and-pure-functions)
  - [Unpacking](#unpacking)
  - [Tuples](#tuples)
- [Dictionaries](#dictionaries)
  - [Dictionary Basics](#dictionary-basics)
  - [Modifying Dictionaries](#modifying-dictionaries)
  - [Iterating Over Dictionaries](#iterating-over-dictionaries)
- [Error Handling](#error-handling)
- [Higher-Order Functions and Callbacks](#higher-order-functions-and-callbacks)
- [Comprehensions and Built-in Iteration](#comprehensions-and-built-in-iteration)
  - [Comprehensions](#comprehensions)
  - [Combining](#combining)
  - [Sorting](#sorting)
  - [Other Built-ins](#other-built-ins)
- [Testing with pytest](#testing-with-pytest)
- [Regular Expressions (Optional)](#regular-expressions-optional)

## Data Types and Variables

### Data Types

**Basic Types** (immutable):

| Type      | Example                   | Description                        |
| --------- | ------------------------- | ---------------------------------- |
| `str`     | `"hello"`, `'world'`      | Sequence of characters             |
| `int`     | `42`, `-2`                | Whole numbers                      |
| `float`   | `10.5`, `0.99`            | Numbers with a decimal point       |
| `bool`    | `True`, `False`           | Truth values                       |
| `None`    | `None`                    | Intentional absence of value       |

**Collection Types** (mutable, held by reference):

| Type       | Example                            | Description                   |
| ---------- | ---------------------------------- | ----------------------------- |
| `dict`     | `{"name": "Alex", "age": 25}`      | Collection of key: value pairs |
| `list`     | `["apple", "banana", "cherry"]`    | Ordered list of values        |
| function   | `def double(x): return x * 2`      | Reusable block of code        |

**Type Conversion:**

```python
str(1)           # "1"
int("42")        # 42
int("hello")     # ValueError
float("0.5")     # 0.5
bool(0)          # False

# Falsy values: 0, 0.0, '', None, [], {}
# Everything else is truthy
```

Use `type()` to check a value's type:

```python
type("hello")   # <class 'str'>
type(42)        # <class 'int'>
type(4.0)       # <class 'float'>
type(True)      # <class 'bool'>
type(None)      # <class 'NoneType'>
type([1, 2])    # <class 'list'>
type({})        # <class 'dict'>
```

### Operators

| Category   | Operators                                                       | Notes                                        |
| ---------- | --------------------------------------------------------------- | -------------------------------------------- |
| Arithmetic | `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent) | `/` always gives a float           |
| Comparison | `>`, `<`, `>=`, `<=`, `==`, `!=`                                | `==` compares values                         |
| Logical    | `and`, `or`, `not`                                              |                                              |
| Membership | `in`, `not in`                                                  | Works on strings, lists, and dictionary keys |
| Identity   | `is`, `is not`                                                  | Same object? Used with `None`                |
| Conditional expression | `value_if_true if condition else value_if_false`    | Shorthand for if/else                        |

### Variables and Scope

**Three operations** you can perform with variables:
1. **Assign** — create a new variable by giving it a value
2. **Reassign** — give the variable a new value
3. **Reference** — use the variable to access its value

```python
count = 0          # assign (this creates the variable)
count = 1          # reassign
count += 1         # reassign using the current value; there is no ++
print(count)       # reference

MAX_GUESSES = 5    # ALL_CAPS: a constant by convention. Don't reassign it.
```

**Scope** determines where a variable can be accessed:
- **Local** — inside a function (including its parameters)
- **Global** — at the top level of a file
- **Built-in** — provided by Python (`print`, `len`, ...)
- Blocks (`if`, `for`, `while`) do NOT create a new scope

```python
a = 'global scope'

def my_func():
    b = 'local scope'
    if True:
        c = 'still local scope'
    print(a, b, c)  # all accessible
# b and c are NOT accessible here
```

## Functions

### Defining Functions

```python
def function_name(param1, param2):
    # body
    return value

# Default values and keyword arguments
def greet(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

greet("Ada")                     # "Hello, Ada!"
greet("Ada", "?")                # "Hello, Ada?"
greet(punctuation=".", name="Ada")  # "Hello, Ada."

# Anonymous one-expression function
square = lambda x: x * x
```

### Parameters, Arguments, and Return Values

- **Parameters** — placeholders in the function definition
- **Arguments** — actual values passed when calling
- **Return values** — the value sent back to the caller; terminates the function

```python
def greet(name):              # name is a parameter
    return f"Hello, {name}!"

greet('Ada')                  # 'Ada' is an argument
# returns "Hello, Ada!"

# Functions without a return statement return None
```

**Function calls resolve from the inside out:**

```python
add(add(1, 2), add(3, 4))
# add(3, 7)
# 10
```

## Strings

### String Basics

- Each character has an **index** starting at `0`; negative indexes count from the end
- Strings are **immutable** — string methods return new strings

```python
message = 'Hello there!'
message[0]         # 'H'
message[-1]        # '!'
len(message)       # 12
message[0:5]       # 'Hello'  (slice: start up to but not including end)
message[6:]        # 'there!'
```

**f-strings** (string interpolation):

```python
name = 'Ada'
greeting = f"Hello, {name}! 2 + 2 = {2 + 2}"
# "Hello, Ada! 2 + 2 = 4"
```

**Escape Characters:** `\"` (quote), `\n` (newline), `\t` (tab)

### String Methods

**Read-only checks** (return booleans or numbers):

| Method / Operator     | Returns   | Description                              |
| --------------------- | --------- | ---------------------------------------- |
| `sub in string`       | `bool`    | Does the string contain `sub`?           |
| `.startswith(sub)`    | `bool`    | Does the string start with `sub`?        |
| `.endswith(sub)`      | `bool`    | Does the string end with `sub`?          |
| `.find(sub)`          | `int`     | Index of first match (`-1` if not found) |
| `.rfind(sub)`         | `int`     | Index of last match (`-1` if not found)  |
| `.isdigit()`          | `bool`    | Made entirely of digits?                 |

**Methods that return a modified copy:**

| Method                          | Description                                  |
| ------------------------------- | -------------------------------------------- |
| `.upper()` / `.lower()`         | Change case                                  |
| `.strip()`                      | Remove whitespace from both ends             |
| `.replace(old, new)`            | Replace all occurrences (`count=1` for first) |
| `.split(sep)`                   | Break into a list of strings                 |
| `sep.join(list)`                | Glue a list of strings together with `sep`   |
| `.capitalize()`                 | Uppercase the first character                |
| `string * n`                    | Repeat string `n` times                      |

```python
s = 'Hello World'
'World' in s                  # True
s[0:5]                        # 'Hello'
s.lower()                     # 'hello world'
s.replace('World', 'Ada')     # 'Hello Ada'
'  yes '.strip().lower()      # 'yes'
'a,b,c'.split(',')            # ['a', 'b', 'c']
'-'.join(['a', 'b'])          # 'a-b'
```

## Conditional Statements

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition2 is True
else:
    # runs if all conditions are False
```

**Order matters!** Only the first `True` condition executes.

**Guard Clauses** — return early to simplify logic:

```python
def can_vote(age):
    if age < 18:
        return False
    return True
```

**Conditional Expression** — shorthand for simple if/else:

```python
message = 'even' if num % 2 == 0 else 'odd'
```

## Loops

**For Loop with `range()`** — use when you know how many iterations:

```python
for i in range(10):          # 0 through 9
    print(i)

range(1, 11)                 # 1 through 10
range(0, 20, 5)              # 0, 5, 10, 15
```

**For Loop over a list:**

```python
for friend in friends:
    print(friend)

for index, friend in enumerate(friends):
    print(index, friend)
```

**While Loop** — use when the number of iterations is unknown:

```python
while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input == 'q':
        break                    # exit the loop
    if not user_input.isdigit():
        continue                 # skip to next iteration
    print(f"You entered: {user_input}")
```

**`break` vs `return`:**
- `break` — exits the current loop, continues after the loop
- `return` — exits the loop AND the current function

**Nested Loops:**

```python
for i in range(3):
    for j in range(5):
        print(f"{i} - {j}")
# Outer runs 3 times × inner runs 5 times = 15 total iterations
```

## Modules and the Ecosystem

### Modules

Every top-level name in a file can be imported. There is no export statement.

```python
# Import the whole module; use dot notation
import circle_helpers
circle_helpers.get_area(5)

# Import specific names
from circle_helpers import get_area, get_diameter

# From the standard library
import random
import math

# Only run when this file is the one being executed
if __name__ == "__main__":
    main()
```

Importing a file runs it. `__name__` is `"__main__"` in the file you ran and the module name everywhere else.

### User Input

```python
name = input("What's your name? ")   # always returns a string
age = int(input("How old? "))         # convert when you need a number
```

### Files and JSON

```python
import json

with open("tasks.json", "w") as file:   # write
    json.dump(tasks, file)

with open("tasks.json") as file:        # read
    tasks = json.load(file)
```

### venv, pip, and requirements.txt

```sh
python3 -m venv .venv               # create a virtual environment (once)
source .venv/bin/activate           # activate it (every new Terminal)
deactivate                          # turn it off
pip install rich                    # install a package into it
pip list                            # see what is installed
pip freeze > requirements.txt       # record installed packages
pip install -r requirements.txt     # install everything a project needs
```

- `.venv/` and `__pycache__/` go in `.gitignore` — never commit them
- `ModuleNotFoundError` usually means the environment is not activated

## Lists

### List Basics

```python
fruits = ['apple', 'banana', 'cherry']
fruits[0]                  # 'apple'
fruits[-1]                 # 'cherry'
len(fruits)                # 3
'banana' in fruits         # True
fruits.index('cherry')     # 2
fruits[0:2]                # ['apple', 'banana'] (non-mutating)
```

### Mutating Lists

Unlike strings, lists **are mutable**:

```python
arr = ['a', 'b', 'c']

arr[1] = 'B'                  # change element at index
arr.append('d')               # add to end
arr.insert(0, 'z')            # add at index
arr.pop()                     # remove and return last
arr.pop(0)                    # remove and return at index
arr.remove('B')               # remove first matching value
del arr[0]                    # remove at index
arr[1:3] = ['x', 'y', 'z']    # replace a slice
arr.clear()                   # empty the list
```

Mutating methods (`.append`, `.sort`, `.reverse`, ...) return `None`.

### References and Pure Functions

Variables holding lists store a **reference** to data in memory, not the data itself:

```python
original = [1, 2, 3]
copy = original            # both point to the SAME list
copy.append(4)
print(original)            # [1, 2, 3, 4] — original is affected!
copy is original           # True
```

**Pure functions** avoid mutating input values. Copy first:

```python
def extend(items, value):
    return [*items, value]   # creates a new list

nums = [1, 2, 3]
result = extend(nums, 4)     # [1, 2, 3, 4]
print(nums)                  # [1, 2, 3] — unchanged

list(items)   # also a copy
items[:]      # also a copy
```

### Unpacking

```python
first, second, *rest = [1, 2, 3, 4, 5]
first   # 1
second  # 2
rest    # [3, 4, 5]
```

### Tuples

```python
point = (30, 90)        # a list that cannot change
point[0]                # 30
lat, long = point       # unpacks like a list
```

## Dictionaries

### Dictionary Basics

```python
user = {
    "name": "Alex",
    "age": 25,
    "friends": ["Sam", "Jo"],
}

user["name"]             # 'Alex'
user["missing"]          # KeyError
user.get("missing")      # None
user.get("missing", 0)   # 0
"age" in user            # True (checks keys)
len(user)                # 3
```

### Modifying Dictionaries

```python
user["age"] = 26            # update existing key
user["is_admin"] = False    # add new key
del user["friends"]         # remove key
user.pop("is_admin")        # remove key and return its value

# Dynamic keys: the key can be any expression
key = "age"
user[key]                   # 26

# Copy before changing in a pure function
clone = dict(user)
```

### Iterating Over Dictionaries

```python
for key in user:                    # keys
    print(key, user[key])

for key, value in user.items():     # keys and values together
    print(key, value)

user.keys()      # all keys
user.values()    # all values
```

## Error Handling

**Read a traceback from the bottom up:** error type and message last, the line that raised it just above.

Common errors:

| Error               | Cause                                             |
| ------------------- | ------------------------------------------------- |
| `SyntaxError`       | Invalid Python; found before anything runs        |
| `IndentationError`  | Wrong indentation                                 |
| `NameError`         | Variable not defined (typo, scope, or order)      |
| `TypeError`         | Wrong type for an operation or call               |
| `ValueError`        | Right type, unacceptable value (`int("abc")`)     |
| `IndexError`        | List/string index out of range                    |
| `KeyError`          | Dictionary key not found                          |
| `AttributeError`    | Value has no such method or attribute             |
| `ZeroDivisionError` | Division by zero                                  |

```python
try:
    number = int(user_input)      # might raise ValueError
except ValueError as err:
    print(f"Oops! {err}")

# Raise your own
if amount > balance:
    raise ValueError("Insufficient funds")
```

## Higher-Order Functions and Callbacks

- **Higher-order function (HOF)** — a function that accepts another function as an argument or returns a function
- **Callback** — a function passed as an argument to a HOF

**Important:** Pass the function itself, don't invoke it:

```python
# Wrong — invokes immediately, passes None
repeat(print_message(), 3)

# Right — passes the function
repeat(print_message, 3)

# Inline callback
repeat(lambda: print('tick'), 3)
```

**Functions in dictionaries** (a dispatch table):

```python
actions = {"1": add_task, "2": view_tasks}
actions[choice]()
```

**Built-in HOFs:**

```python
sorted(animals, key=len)                       # sort by a callback's result
max(users, key=lambda user: user['age'])       # largest by a callback's result
```

## Comprehensions and Built-in Iteration

| You want to...                  | Use                                   | Returns                |
| ------------------------------- | ------------------------------------- | ---------------------- |
| Do a side effect per element    | `for item in items:`                  | nothing                |
| Transform each element          | `[f(x) for x in items]`               | new list (same length) |
| Keep elements that pass         | `[x for x in items if test]`          | new list (subset)      |
| Get first match                 | `for` loop with `return`, or `next()` | first matching element |
| Combine into one value          | `sum()`, `min()`, `max()`, `len()`    | single value           |
| Sort                            | `sorted(items)` / `items.sort()`      | new list / in place    |

### Comprehensions

```python
nums = [1, 2, 3, 4, 5]

doubled = [num * 2 for num in nums]            # [2, 4, 6, 8, 10]
evens = [num for num in nums if num % 2 == 0]  # [2, 4]
by_id = {user['id']: user for user in users}   # dict comprehension
```

### Combining

```python
sum(nums)          # 15
min(nums)          # 1
max(nums)          # 5
len(nums)          # 5

# Accumulator pattern: start, update, return
total = 0
for num in nums:
    total += num

# Frequency counter
freqs = {}
for letter in ['a', 'b', 'a']:
    freqs[letter] = freqs.get(letter, 0) + 1
# {'a': 2, 'b': 1}
```

### Sorting

```python
nums = [4, 2, 5, 1, 3]

sorted(nums)                     # [1, 2, 3, 4, 5]  new list
sorted(nums, reverse=True)       # [5, 4, 3, 2, 1]
sorted(words, key=len)           # by a callback's result
nums.sort()                      # in place, returns None!
```

### Other Built-ins

```python
for index, value in enumerate(items):    # index and value
for a, b in zip(list_a, list_b):         # two lists in step
any(x > 10 for x in nums)                # at least one?
all(x > 0 for x in nums)                 # every one?
```

## Testing with pytest

```sh
pip install pytest
python3 -m pytest              # run all tests
python3 -m pytest -v           # show each test by name
python3 -m pytest tests/test_calc.py   # one file
```

```python
# tests/test_calc.py — files and functions start with test_
from src.calc import add

def test_adds_two_numbers():
    assert add(1, 2) == 3               # == compares contents

def test_returns_a_new_list():
    assert double([1, 2]) == [2, 4]
    assert double(nums) is not nums     # is / is not compares identity

def test_raises():
    with pytest.raises(ValueError):
        int("abc")
```

## Regular Expressions (Optional)

Regular expressions are patterns for searching, matching, and manipulating text. Write them as raw strings: `r"pattern"`.

**Common patterns:**

| Pattern    | Meaning              |
| ---------- | -------------------- |
| `^`        | Start of string      |
| `$`        | End of string        |
| `\w`       | Word character       |
| `\d`       | Digit (0-9)          |
| `\s`       | Whitespace           |
| `.`        | Any character        |
| `+`        | One or more          |
| `*`        | Zero or more         |
| `?`        | Zero or one          |
| `[abc]`    | Character class      |
| `[^abc]`   | Negated class        |
| `{n}`      | Exactly n times      |
| `{n,m}`    | Between n and m      |

**Flags:** `re.IGNORECASE`

**Functions:**

```python
import re

re.fullmatch(r"\w+", "hello_1")            # match object or None — whole string
re.search(r"cat", "the Cat", re.IGNORECASE)  # first match or None
re.findall(r"cat", "cat catnip")           # ['cat', 'cat']
re.sub(r"world", "Python", "hello world")  # 'hello Python'
```
