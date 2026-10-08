# Mod 1 Learning Objectives and Key Terms

One entry per lesson. Key terms are copied from each lesson's **Key Terms** section by `scripts/sync-key-terms.py`, so edit them in the lesson and rerun the script rather than editing them here. Learning objectives are written so that each one could be checked with a short task. Each list is split in two. _In the session_ names the three or four objectives the 90-minute lecture is responsible for: introduced, practiced, and checked before it ends. _By the end of the module_ names the rest, which the chapter's reading, the assignment, and the project carry, and which the Mod 1 assessment can draw on.

## 1.1 Intro to Programming

<!-- key-terms-from: 1-intro-to-programming.md -->

**Key terms**

- A **program** is a text file containing instructions that a computer executes to accomplish a task.
- **Comments** are used to document and explain code. They are ignored when a program is executed. A comment line begins with the `#` symbol and can be placed on its own line or following valid code.

  ```py
  # this is a comment that is ignored
  print("hello world") # this prints "hello world"
  ```

- **Expressions** are any piece of code that evaluates to a single value. They are often the result of using operators (`+`, `*`, `>`, `==` etc...) or invoking functions (`len("hi")`).
- **Statements** change the program.
  - Creating a variable increases the memory used by the program.
  - `if` statements change the "control flow" of a program by skipping lines of code.
- **State** refers to the data stored by a program at a point in time.
- The **Python interpreter** is the program that reads a `.py` file and executes it, one statement at a time. You start it with the `python3` command.
- The **`print()`** function is a built-in function that displays text to the Terminal output. It is used to view the result of code operations, primarily for debugging purposes.

  ```py
  print("hello world") # prints hello world
  ```

- An **f-string** is a string with an `f` before the opening quote. Any expression written inside `{}` is evaluated and its value is placed into the text.

  ```py
  x = 10
  print(f"x is {x}") # prints x is 10
  ```

- **Control Flow** refers to the order in which lines of code are executed. Control flow runs from the top of a file to the bottom.
- **Code Style** refers to the formatting of the code in a way that makes it easier to read and understand. Python's style conventions are written down in a document called [PEP 8](https://peps.python.org/pep-0008/).

**You will be able to…**

_In the session:_

- Explain what a program is and name the three kinds of lines it is made of: comments, expressions, and statements.
- Run a `.py` file from the Terminal with `python3` and explain what the interpreter does with it.
- Use `print()` to inspect a value, and use an f-string to place a value inside a message.
- Describe the default control flow of a program and name the two kinds of statement that change it.

_By the end of the module:_

- Tell an expression from a statement, and say what value a simple expression evaluates to.
- Read an `IndentationError` and explain why the interpreter refused the whole file.
- Rewrite a badly formatted function to follow PEP 8: four-space indentation, spaces around operators, `snake_case` names.

### Exit Ticket

**Learning Objective**: Fellows will be able to explain what the Python interpreter does with each line of a program when the file runs, and justify where a `print()` call must be placed to display a stored value.

**Question**

Maya's `main.py` contains these two lines:

```python
fahrenheit = 212
celsius = (fahrenheit - 32) * 5 / 9
```

Maya runs `python3 main.py`. The Terminal shows nothing, so Maya decides that the program did not run. Is Maya right? What line should Maya add to see the temperature in Celsius, where in the file should that line go, and why there?

**Level 2 Example**

Maya is wrong, the program did run. Maya needs to add `print(celsius)` at the bottom of the file.

**Level 3 Example**

Maya is wrong. When Maya runs `python3 main.py`, the Python interpreter executes the file one statement at a time, from top to bottom. The first line stores `212` in `fahrenheit`. The second line evaluates the expression `(fahrenheit - 32) * 5 / 9` and stores the result in `celsius`. Both lines change the program's state, but neither one displays anything, because only `print()` sends text to the Terminal. Maya should add `print(f"{fahrenheit}°F is {celsius}°C")` as a third line, which displays `212°F is 100.0°C`. The `print()` has to go after the line that calculates `celsius`, because control flow runs top to bottom, and `celsius` does not hold a value until that line has run.

## 1.2 Data Types, Variables, and Operators

<!-- key-terms-from: 2-data-types-variables.md -->

**Key terms**

- **State** refers to the data stored by a program at a point in time.
- **Data types** are categories of values in Python. There are 5 basic types (`str`, `int`, `float`, `bool`, `None`) and 3 types that hold other data or code (`list`, `dict`, and functions). Knowing the type of a value helps determine how you can use that value. Choosing the right type to represent your data is essential.
- **Variables** are named containers for data. You can **assign**, **reference** and **reassign** variables to store and update information in your program.
  - A variable is created the first time it is **assigned**. Names in `ALL_CAPS` are a signal to readers that a value is a constant and should not be reassigned.
- **`snake_case`** is the Python convention for naming variables and functions: lowercase words joined by underscores, like `days_in_each_month`.
- **Operators** are symbols (e.g. `+`, `>=`, `and`) that generate new data from existing values.
  - **Arithmetic operators** (`+`, `-`, `*`, `/`, `//`, `%`, `**`) calculate a new value from numbers.
  - **Comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) compare two values and produce a boolean.
  - **Logical operators** (`and`, `or`, `not`) combine or reverse conditions.
  - **Membership operators** (`in`, `not in`) check whether a value is inside a string, list, or dictionary.
  - **Identity operators** (`is`, `is not`) check whether two names refer to the very same object.
  - **Assignment operators** (`=`, `+=`, `-=`, and the rest) store a value in a variable.
- **Operator precedence** is the order in which Python evaluates the operators in an expression, such as multiplication before addition. Parentheses change that order: whatever is inside them is evaluated first.

**You will be able to…**

_In the session:_

- Identify the data type of any literal value and give a real-world example of data that each type represents.
- Predict the result of an expression that combines values with arithmetic, comparison, and logical operators, including the cases where the result is a `TypeError`.
- Apply operator precedence to predict the value of an expression, and add parentheses to change it.
- Assign, reassign, and reference a variable, and use augmented assignment (`+=`) to update one.
- Choose descriptive `snake_case` variable names, and recognize an `ALL_CAPS` name as a constant.

_By the end of the module:_

- Identify operators that produce unexpected output, such as `8 / 2`, `"3" * 5`, and `0.1 + 0.2 == 0.3`, and explain each result.
- Read and write a conditional expression that chooses between two values.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict the values produced by expressions and explain how operator precedence and the data types determine that result.

**Question**

Andre wants the average of two quiz scores and writes this program:

```python
quiz_1 = 80
quiz_2 = 90
average = quiz_1 + quiz_2 / 2
print(average)
```

Andre expected `85`. What does the program print, and why? What would Andre change to get the average? Then suppose `quiz_2` held the string `"90"` instead of the number `90`. What would happen, and why?

**Level 2 Example**

The program prints `125.0` because the division happens first. Andre needs parentheses: `(quiz_1 + quiz_2) / 2`. With `"90"` the program would crash, because you can't divide a string.

**Level 3 Example**

The program prints `125.0`. Python evaluates `/` before `+` because of operator precedence, so it first calculates `quiz_2 / 2`, which is `45.0`, and then adds `80`. To get the average, Andre should use parentheses to add first and then divide: `(quiz_1 + quiz_2) / 2`. Whatever is inside parentheses is evaluated first, so the program adds the scores to get `170` and then divides by `2` to get `85.0`.

If `quiz_2` held the string `"90"`, the program would crash with a `TypeError` on the `average` line. A value's data type decides which operators work on it, and `/` works only on numbers, so Python cannot divide the string `"90"` by `2`, even though the string's characters look like a number.

## 1.3 Functions

<!-- key-terms-from: 3-functions.md -->

**Key terms**

- **Don't Repeat Yourself (DRY)** is a principle of software engineering aimed at making it easier to maintain, update, and debug code.
- **Functions** are named containers for statements that can be invoked to execute code, improving readability and reducing repetition.
- **Built-in functions** like `print()`, `len()`, and `type()` come with Python, so they can be called without being defined first.
- A **docstring** is a string written on the first line of a function's body that describes what the function does. VS Code and the built-in `help()` function show it to whoever is about to call the function.
- **Parameters** are placeholders for inputs given to the function. Parameters can be used by their function to change the function's behavior.
- **Arguments** are the actual values given when invoking a function.
- **Return statements** allow functions to produce values that can be used elsewhere in your program and terminate function execution. A function with no `return` statement returns `None`.
- Parameters can have **default values**, and arguments can be passed by **keyword** as well as by position.
- A **`NameError`** is raised when a line uses a name that does not exist at the moment that line runs: the name is misspelled, it belongs to a different function's scope, or it is assigned (or its function is defined) further down the file than the line that uses it.
- A **`TypeError`** is raised when a value is the wrong type for what the code asks of it, such as adding a string to a number, or when a function is called with the wrong number of arguments.
- **Scope** determines where variables can be accessed.
  - **Global scope** is the file, outside of any function. A variable assigned there is reachable anywhere in that file.
  - **Local scope** is the inside of a function. A variable or parameter assigned there exists only while that function is running and is reachable only within it.

**You will be able to…**

_In the session:_

- Define a function with `def`, call it, and trace the control flow of a program that defines and calls functions
- Recognize repeated code and refactor it into a function with well-named parameters.
- Distinguish parameters from arguments and predict the `TypeError` that results from calling a function with the wrong number of them.
- Explain the two jobs of `return`, and explain why a function without `return` produces `None`.
- Predict whether a variable is reachable from a given line, using the rules for local and global scope, and explain the `NameError` when it is not.

_By the end of the module:_

- Resolve nested function calls from the inside out.
- Write a function with default parameter values and call it with positional and keyword arguments.
- Explain why a function must be defined before the line that calls it runs, and why two functions can each have a variable with the same name.
- Explain why assigning to a global variable inside a function raises `UnboundLocalError`, and say why passing values in and returning them out is preferred to `global`.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict the value a function call produces and explain how `return` and local scope determine which values can leave a function.

**Question**

Priya writes a function to calculate a 20% tip:

```python
def calculate_tip(bill):
    tip = bill * 0.2
    print(tip)

dinner_tip = calculate_tip(50)
print(f"Leave ${dinner_tip}")
```

Priya expected the last line to print `Leave $10.0`. What does the program actually print, and why? Priya then tries replacing the last line with `print(f"Leave ${tip}")`. What happens, and why? What change would make the original last line print `Leave $10.0`?

**Level 2 Example**

The program prints `10.0` and then `Leave $None` because the function prints the tip instead of returning it. Using `tip` outside the function gives a `NameError`. Priya should change `print(tip)` to `return tip`.

**Level 3 Example**

The program prints `10.0` and then `Leave $None`. Calling `calculate_tip(50)` runs the function body, so `tip` becomes `10.0` and `print(tip)` shows it in the Terminal. But `print` only shows a value to the person at the Terminal. The function has no `return` statement, so the call produces `None`, and `None` is what gets stored in `dinner_tip`. Writing `print(f"Leave ${tip}")` instead raises `NameError: name 'tip' is not defined`, because `tip` is a local variable. It exists only while `calculate_tip` is running, and it cannot be reached from the global scope. Since the rest of the program cannot reach a function's local variables, the only way to get a value out of a function is to return it. Changing `print(tip)` to `return tip` makes the call `calculate_tip(50)` resolve to `10.0`, so `dinner_tip` holds `10.0` and the last line prints `Leave $10.0`.

## 1.4 Conditional Statements

<!-- key-terms-from: 4-conditional-statements.md -->

**Key terms**

- **Control Flow** refers to the order in which statements of a program are executed, typically top-to-bottom.
- **Conditional statements** (`if`, `elif`, `else`) let you control the flow of your program based on data values. The order of conditions matters, and only the first true condition in a chain will execute.
- **Guard clauses** are single `if` statements that return early from a function, simplifying conditional logic.
- An `if` statement creates a **boolean context** where non-boolean values are converted to Booleans using the `bool()` function.
- Non-boolean values used in a boolean context are considered **truthy** if they evaluate to `True` or **falsy** if they evaluate to `False`. All values are truthy except for `None`, `False`, the numbers `0` and `0.0`, the empty string `""`, and empty collections such as `[]` and `{}`.
- **Conditional expressions** provide a concise way to choose between two values based on a condition.

**You will be able to…**

_In the session:_

- Write an `if`/`elif`/`else` chain and predict which branch runs, including when the branches are in the wrong order or are separate `if` statements.
- Rewrite a conditional chain as guard clauses and explain why the last `return` needs no condition.
- List the falsy values, predict what `if "False":` does, and use `if not value:` as a guard against an empty value.

_By the end of the module:_

- Say when `if value is None:` is the right test instead of `if not value:`.
- Replace an `if`/`else` that assigns one of two values with a conditional expression.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict which branch of a conditional chain or a set of guard clauses runs and explain how the order of the conditions and an early `return` determine it.

**Question**

Jordan writes a function that turns a test score into a letter grade:

```python
def letter_grade(score):
    if score >= 70:
        return "C"
    if score >= 80:
        return "B"
    if score >= 90:
        return "A"
    return "F"

print(letter_grade(95))
```

Jordan expected `A`. What does the program print, and why? How should Jordan fix the function? Why does the last line, `return "F"`, not need an `if`?

**Level 2 Example**

The program prints `C` because `score >= 70` is checked first. Jordan should put `score >= 90` first and `score >= 70` last. The last line doesn't need an `if` because it runs when none of the others do.

**Level 3 Example**

The program prints `C`. Each `if` is a guard clause, and a `return` statement ends the function the moment it runs. So the first condition that is `True` decides the answer, and the conditions below it are never checked. `95 >= 70` is `True`, so the function returns `"C"` before it ever checks `score >= 80` or `score >= 90`. Jordan should put the narrowest condition first: `score >= 90`, then `score >= 80`, then `score >= 70`. Then a score of 95 meets `score >= 90` first and gets `"A"`, while a score of 75 fails the first two checks and still gets `"C"`. The last line needs no condition because the function only reaches it when every guard clause above it was `False`, which means the score must be below 70.

## 1.5 Loops

<!-- key-terms-from: 5-loops.md -->

**Key terms**

- **Loops** allow you to repeat code multiple times, making it easy to automate repetitive tasks and process collections of data.
- The **`for` loop** with **`range()`** is best for repeating a process a known number of times, such as counting.
- An **iterable** is any value a `for` loop can walk through one element at a time. A `range()` and a string are both iterables.
- The **`while` loop** is useful for repeating a process an unknown number of times, continuing until a condition is no longer true.
- **Infinite loops** occur when the loop's condition never becomes false; use `break` to exit early and `continue` to skip to the next iteration.
- **Nested loops** let you loop inside another loop, useful for working with multi-dimensional data or complex processes.
- Loop challenges help you practice using loops to solve real problems, such as counting results or repeating until something happens.

**You will be able to…**

_In the session:_

- Rewrite repeated statements as a `for` loop over `range()`, and predict the first and last values `range()` produces.
- Choose between a `for` loop and a `while` loop from whether the number of repetitions is known in advance.
- Write a `while True` loop that repeats until a random event happens, using `break` to leave and `continue` to skip, and explain how `break` differs from `return`.
- Keep a running count across iterations of a loop and report it afterward.

_By the end of the module:_

- Loop over the characters of a string.
- Predict the output and the number of iterations of a nested loop.
- Stop an infinite loop from the Terminal.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict the result a loop produces, explain how placing a variable inside or outside the loop determines that result, and justify the choice between a `for` loop and a `while` loop.

**Question**

Kiara writes a function that rolls a die many times and counts the sixes:

```python
import random

def count_sixes(rolls):
    for i in range(rolls):
        sixes = 0
        if random.randint(1, 6) == 6:
            sixes += 1
    print(f"{sixes} sixes in {rolls} rolls")

count_sixes(100)
```

Kiara runs the program several times. The message always reports either 0 or 1 sixes, never anything close to the 16 or 17 sixes that 100 rolls usually produce. Why? How should Kiara fix the function? Next, Kiara wants a program that rolls until the first 6 and then reports how many rolls it took. Should Kiara use a `for` loop or a `while` loop, and why?

**Level 2 Example**

The count is reset to 0 every time the loop runs. Kiara should move `sixes = 0` above the `for` line. For rolling until a 6, Kiara should use a `while` loop.

**Level 3 Example**

A `for` loop runs its whole body once for every number in `range(100)`. `sixes = 0` is inside the body, so it runs at the start of every roll and throws away the count from all the rolls before. By the time the loop ends, `sixes` holds only the result of the last roll: `1` if the last roll was a 6 and `0` if it was not. Kiara should move `sixes = 0` above the `for` line. Then `sixes = 0` runs once, and `sixes += 1` adds to a running count that lasts across all 100 iterations. For rolling until the first 6, Kiara should use a `while` loop, because nobody knows in advance how many rolls it will take, and a `for` loop with `range()` needs the number of repetitions before the loop starts. Kiara could set a `rolls` counter to `0` before a `while True:` loop, add 1 to it on every roll, `break` when the roll is a 6, and print `rolls` after the loop.

## 1.6 Inputs and Outputs

<!-- key-terms-from: 6-inputs-outputs.md -->

**Key terms**

- **Strings** are sequences of characters enclosed in quotes (single or double). Strings are immutable, meaning their characters cannot be changed directly.
- You can _access_ individual characters of a string with **bracket notation**.
- You can check the length of a string with **`len(str)`** (and you can use this method on lists and dictionaries too!).
- A **method** is a function that is attached to a value. Methods are invoked using **dot notation**: `value.method()`.
- **String methods** like `startswith`, `endswith`, `find`, `upper`, `replace`, `strip`, and `split` allow you to search, analyze, and manipulate string data.
- The **`in` operator** checks whether one string contains another.
- **`print()`** takes any number of values. It puts `sep` between them, a space unless you say otherwise, and `end` after them, a new line unless you say otherwise.
- **f-strings** interpolate the value of any expression written inside `{}` into a string. A **format specifier** after a colon, like `{price:.2f}`, controls how the value is displayed.
- The **`input()`** function gets input from the user. It always returns a string, so converting it to another type is your job.
- **Type conversion** with `str()`, `int()`, `float()`, `bool()` turns a value of one type into another.
- A program is **hard-coded** if the program code must be modified in order to produce a new result.

**You will be able to…**

_In the session:_

- Access a character of a string by positive or negative index, take a slice, and predict the `IndexError` for a position that does not exist.
- Print several values in one `print()` call, control what goes between and after them with `sep` and `end`, and build a message with an f-string that formats a decimal with `:.2f`.
- Read a line of input with `input()`, clean it up with `strip()` and `lower()`, explain why it is always a string, and convert it with `int()` or `float()` after checking it with `isdigit()`.
- Convert a hard-coded program into one that takes its values from `input()`, turning a `Y`/`N` answer into a boolean.

_By the end of the module:_

- Explain what it means that strings are immutable and predict the `TypeError` from trying to change one in place.
- Search and change strings with `in`, `find()`, `startswith()`, `endswith()`, `replace()`, and `split()`, and chain two methods in one expression.
- Predict the `TypeError` from `"1" + 1` and fix it by converting one side.
- Explain the difference between displaying a number with `:.2f` and changing it with `round()`.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict how a program handles the value returned by `input()` and explain why that value must be cleaned, checked, and converted before it is used as a number.

**Question**

Luis writes this program:

```python
age = input("How old are you? ")
if age >= 18:
    print("You can vote!")
else:
    print("Not yet!")
```

Luis runs the program and types `21`. What happens, and why? How should Luis change the program so that typing `21` prints `You can vote!`, and typing `twenty` prints a message instead of crashing?

**Level 2 Example**

The program crashes with a `TypeError` because `age` is a string. Luis needs to convert it with `int()`, and check it with `isdigit()` first so that `twenty` doesn't crash.

**Level 3 Example**

The program crashes with `TypeError: '>=' not supported between instances of 'str' and 'int'`. `input()` always returns a string, so even though Luis typed `21`, `age` holds `"21"`. Python will not compare a string with a number, because it does not know whether Luis meant the text or the number. To fix the program, Luis has to convert `age` with `int()` before the comparison. But `int("twenty")` raises a `ValueError`, so Luis should check the string before converting it. I would write `age = input("How old are you? ").strip()` to remove stray spaces, then `if not age.isdigit():` print a message like `twenty is not a number`, and otherwise run `age = int(age)` before the `>= 18` comparison. Then `21` passes `isdigit()`, becomes the integer `21`, and prints `You can vote!`, while `twenty` fails `isdigit()` and gets a message instead of a crash.

## 1.7 Lists

<!-- key-terms-from: 7-lists.md -->

**Key terms**

- **Lists** are ordered collections of values. Like strings, they have indexes starting at `0`, support bracket notation and slicing, and work with `len()` and the `in` operator.
- Unlike strings, lists are **mutable**. Methods like `append`, `insert`, `pop`, and `remove` change a list in place.
- A variable does not hold a list. It holds a **reference** to the list. Two variables can reference the same list, and a function receiving a list receives a reference to the caller's list.
- A **pure function** returns the same output for the same input and has no side effects. Functions that mutate the list they are given are impure. To keep a function pure, make a copy first with `list(arr)`, `arr[:]`, or `[*arr]`.
- Lists can contain other lists (**2D lists**), and a list can be **unpacked** into several variables at once. A **tuple** is a list that cannot change, written with parentheses.

**You will be able to…**

_In the session:_

- Create a list, access elements by index, slice it, test membership with `in`, and loop over it with `for` and `enumerate()`.
- Add, replace, and remove elements with the list methods and `del`, and predict the list's contents after each operation.
- Predict what happens to `nums` after `clone = nums; clone[1] = 20`, and explain it in terms of references.
- Explain why a function can change a list it was given, and classify a function as pure or impure.

_By the end of the module:_

- Explain why the same bracket assignment that fails on a string works on a list.
- Make a pure version of an impure list function by copying the list first.
- Access rows and columns of a 2D list and report its size with `len()`.
- Explain when to use a tuple instead of a list, and predict the `TypeError` from changing one.
- Unpack a list into several variables, including with `*rest`.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict how a function that receives a list affects the caller's list, explain the result in terms of references, and classify the function as pure or impure.

**Question**

Amara writes a function that adds a bonus score to a list of scores:

```python
def add_bonus(scores):
    scores.append(100)
    return scores

original = [70, 85]
with_bonus = add_bonus(original)
print(original)
print(with_bonus)
```

Amara expected `original` to still be `[70, 85]`. What do the two `print()` lines show, and why? Is `add_bonus` a pure function? How could Amara change `add_bonus` so that `original` stays `[70, 85]`?

**Level 2 Example**

Both lines print `[70, 85, 100]` because the function changed the original list. `add_bonus` is impure. Amara should make a copy of the list before appending.

**Level 3 Example**

Both lines print `[70, 85, 100]`. A variable does not hold a list, it holds a reference to the list. When Amara calls `add_bonus(original)`, the parameter `scores` receives a reference to the same list that `original` references. `scores.append(100)` mutates that one list in place, and `return scores` hands back the same reference, so `original`, `scores`, and `with_bonus` are three names for one list. `add_bonus` is impure because it has a side effect: it mutates the list it was given. To make it pure, Amara should copy the list and add to the copy, for example by writing `return [*scores, 100]`. Then `with_bonus` references a new list, `[70, 85, 100]`, and `original` still references the unchanged `[70, 85]`.

## 1.8 Dictionaries

<!-- key-terms-from: 8-dictionaries.md -->

**Key terms**

- **Dictionaries** are data structures that store multiple pieces of data as key-value pairs, useful for representing real-world entities like users or products.
  - A **key** is the name a value is stored under and looked up by. Each key appears only once in a dictionary.
  - A **value** is the data stored under a key. It can be any type, including a list or another dictionary.
- Dictionary values are accessed using **bracket notation** (`my_dict["key"]`), which raises a `KeyError` for a missing key, or with the **`.get()`** method, which returns `None` (or a default you choose) instead.
- Dictionaries are **mutable**, meaning you can add, modify, or delete key-value pairs after creation using assignment, `del`, or `.pop()`.
- Dictionaries can contain **nested data** including lists and other dictionaries, allowing for complex data structures.
- Like lists, dictionaries are held by **reference**. Copy one with `dict(my_dict)` before changing it inside a pure function.
- **`.keys()`**, **`.values()`**, and **`.items()`** let you loop over a dictionary. `.items()` hands you each key and value together.

**You will be able to…**

_In the session:_

- Create a dictionary, read a value by key, and choose between bracket notation and `.get()` based on whether the key is guaranteed to exist.
- Add, update, and delete key-value pairs, including with a key held in a variable.
- Loop over a dictionary's keys, values, and key-value pairs with `.items()` and unpacking, and explain what `.keys()` returns.
- Model "many of the same kind of thing" as a list of dictionaries, loop over it, and add to it.

_By the end of the module:_

- Explain which values can be keys and why a list cannot.
- Predict the effect of mutating a dictionary through a second variable, and copy a dictionary before changing it in a pure function.
- Write a function that takes a dictionary and uses only the keys it needs.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict the result of looking up a key in a dictionary and justify when to use bracket notation and when to use `.get()`, based on whether the key is guaranteed to exist.

**Question**

Tomas keeps track of how many copies of each book a small library has:

```python
library = {"Kindred": 2, "Beloved": 0}

def copies_available(title):
    return library[title]

print(copies_available("Kindred"))
print(copies_available("Sula"))
```

What does the program print, and why? How should Tomas change `copies_available` so that a book the library does not own is reported as having `0` copies? Tomas also has this loop elsewhere in the program. Should Tomas change `library[title]` to use `.get()` here as well? Why or why not?

```python
for title in library:
    print(f"{title}: {library[title]} copies")
```

**Level 2 Example**

The program prints `2` and then crashes with a `KeyError` because `"Sula"` isn't in the dictionary. Tomas should use `library.get(title, 0)`. The loop doesn't need `.get()` because the keys are already in the dictionary.

**Level 3 Example**

The program prints `2` and then crashes with `KeyError: 'Sula'`. Bracket notation requires the key to exist, and `"Sula"` is not one of the keys in `library`. Tomas should write `return library.get(title, 0)`. `.get()` returns the default value `0` when the key is missing, and `0` is also the right answer, because a book the library does not own has zero copies. The loop does not need `.get()`. A `for` loop over a dictionary visits only the keys that are in it, so every `title` the loop hands to `library[title]` is guaranteed to exist. Bracket notation is the right choice whenever the key is guaranteed to exist, and `.get()` is the right choice when the key might be missing.

## 1.9 Modules, Virtual Environments, and pytest

<!-- key-terms-from: 9-modules-environments-pytest.md -->

**Key terms**

- A **module** is a file containing code, which can then be imported and utilized in other parts of a larger program or system.
  - Every function and variable defined at the top level of a file can be imported by another file.
  - A module is imported with `import module_name`, or specific names are imported with `from module_name import name`.
- Importing a file **runs** it, top to bottom. The variable `__name__` tells a file whether it is being run directly (`"__main__"`) or imported by another file.
- The `if __name__ == "__main__":` guard is how a file says "only run this part when I am the program being run".
- The **standard library** is the collection of modules that come with Python. `random`, `math`, `time`, and `json` are examples. They need `import` but no installation.
- A **package** is a folder of modules that someone has published so that other people can install it and import it. `pytest` is a package.
- A **library** is a collection of code written for other programs to use rather than to be run on its own. The standard library is Python's own library, and many packages, like `pytest`, are libraries too.
- Third-party packages are published on the **Python Package Index (PyPI)** and installed with **`pip`**, Python's package installer.
- A **virtual environment** is a folder that holds one project's private set of packages, together with a link to the Python installed on your computer. You create one with `python3 -m venv .venv` and turn it on with `source .venv/bin/activate`.
  - Installing a package inside an activated virtual environment installs it only there.
  - A package can have **sub-dependencies**, other packages it needs, and `pip` installs those too.
- **`requirements.txt`** is a file listing the packages a project needs. `pip freeze > requirements.txt` writes it; `pip install -r requirements.txt` reads it.
- A **`.gitignore`** file lists the files and folders in a project that Git should not track. The `.venv/` and `__pycache__/` folders go in it. The `.venv` folder is never committed; it is rebuilt from `requirements.txt` instead.
- **JSON** is a text format for storing lists and dictionaries in a file. The standard library's `json` module writes them with `json.dump()` and reads them back with `json.load()`.
- **Developer dependencies** like `pytest` are packages used by the developer(s) of a project but not needed by the people who run it.
- A **unit test** is a small program that calls one function with a known input and checks that the output is what you expected. A collection of them is a **test suite**.
- A **test file** is a file whose name starts with `test_` that imports functions from your source code and tests them. Keeping tests in their own files, in a `tests/` folder beside `src/`, is separation of concerns applied to testing.
- **`pytest`** is the third-party package that finds and runs test files. It is installed into the project's virtual environment and run with `python3 -m pytest`.
- A **test function** is any function in a test file whose name starts with `test_`. It is named after the function it tests, and the docstring on its first line describes what the test checks.
- The **`assert`** statement checks that an expression is truthy. If it is not, it raises an `AssertionError` and `pytest` reports the test as failed. The expression is an ordinary comparison: `==` for most values, `is` for `True`, `False`, and `None`, and `pytest.approx()` for decimal numbers.

**You will be able to…**

_In the session:_

- Split a single-file program into modules so that each file has one concern, import a whole module or specific names, and explain why `from module import *` is avoided.
- Predict what prints when a module with top-level code is imported, explain what `__name__` holds, and use the `__main__` guard to keep a module's code from running on import.
- Create and activate a virtual environment, install `pytest` into it with `pip`, and record it in `requirements.txt` with `pip freeze`.
- Write a test function with `assert` and a docstring, run the tests with `python3 -m pytest`, and read a failure report to find which assertion failed and what the function actually returned.

_By the end of the module:_

- Explain what the `__pycache__` folder is, keep it and `.venv/` out of Git, and explain why the recipe is committed rather than the meal.
- Distinguish a standard library module from a third-party package and say which needs installing.
- Save a list or dictionary to a JSON file and read it back with `json.dump()` and `json.load()`.
- Use `pip list` and `pip show` to see what is installed and what a package requires, and rebuild an environment with `pip install -r requirements.txt`.
- Explain the `ModuleNotFoundError` that appears when the environment is not activated, and check for that first.
- Explain why `pytest` is a developer dependency and why the tests are run with `python3 -m pytest` rather than `pytest`.
- Assert a boolean result with `is True` or `is False` and a decimal result with `pytest.approx()`, and say what each catches that `==` would miss.
- Split the madlib program into a module for the story and a `main.py` for the input.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict what runs when one module imports another and explain how importing a file runs it and how the `if __name__ == "__main__":` guard controls what runs.

**Question**

Sofia has two files in the same folder:

```python
# greetings.py
def greet(name):
    return f"Hello, {name}!"

print(greet("test"))
```

```python
# main.py
from greetings import greet

print(greet("Ada"))
```

Sofia runs `python3 main.py`. What prints, and why? Sofia wants the line `print(greet("test"))` to run only when `greetings.py` is the file being run with `python3`, and not when another file imports it. How should Sofia change `greetings.py`, and why does that change work?

**Level 2 Example**

The program prints `Hello, test!` and then `Hello, Ada!` because importing `greetings` runs it. Sofia should put the test `print` inside `if __name__ == "__main__":`.

**Level 3 Example**

The program prints `Hello, test!` and then `Hello, Ada!`. Importing a file runs it from top to bottom, so when the interpreter reaches `from greetings import greet` on the first line of `main.py`, it runs all of `greetings.py`. The `def` creates the `greet` function, and the `print` at the bottom prints `Hello, test!`. Only then does Python return to `main.py` and print `Hello, Ada!`. To fix it, Sofia should move the test line inside `if __name__ == "__main__":`. Python sets `__name__` for every file automatically: when `greetings.py` is imported, its `__name__` is `"greetings"`, and when it is the file run with `python3`, its `__name__` is `"__main__"`. So the condition is `True` only when `greetings.py` is the program being run, and `python3 main.py` prints only `Hello, Ada!`.

## 1.10 Reading Unfamiliar Code

<!-- key-terms-from: 10-reading-unfamiliar-code.md -->

**Key terms**

- Reading code means **building a model of someone else's intent** from the artifacts they left behind: files, names, and behavior. You are not trying to memorize the code. You are trying to be able to predict it.
- The **orientation questions** give you a place to stand before you dive in: what is this supposed to do, where does the behavior show up, which files matter, what do I know versus what am I guessing.
- The method has six steps: **run it, find the entry point, find the data, trace one action, predict then run, and write down what you know and what you are guessing**.
- Names are the author's notes to you. A function's name and its parameters tell you its intent; the body tells you whether it lives up to it.
- Reading code a model wrote is the same activity with more suspicion. Generated code is confident and plausible, and plausible is not the same as correct.

**You will be able to…**

_In the session:_

- Run an unfamiliar program with good and bad input and describe what it does in one sentence, before reading it.
- Map a multi-file program by its `import` and `def` lines and identify the entry point and the one piece of data everything revolves around.
- Trace a single user action from input to output through every function it touches.
- Predict what a function returns for a specific input, check the prediction, and treat a wrong prediction as a finding.

_By the end of the module:_

- Answer the six orientation questions about a program before changing anything in it.
- Keep separate lists of what is known and what is guessed, and move an item across only after running code.
- Find a defect in a plausible, model-written function and describe it as a bug report: concrete input, actual output, expected output, and where.
- Ask a model about code in tutor mode, using the AI policy's standing instruction.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict what an unfamiliar function returns for a specific input, justify why a function's name and docstring are not evidence that it works, and describe a defect as a bug report that names the input, the actual output, the expected output, and the line at fault.

**Question**

Malik asked a model for a function that counts vowels, and the model produced this:

```python
def count_vowels(word):
    """Count the vowels in a word."""
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count
```

Malik reads it and decides, "The name and the docstring say it counts vowels, so it works." Predict what `count_vowels("Apple")` returns. Is Malik right? Explain why or why not, and write a bug report for the function.

**Level 2 Example**

`count_vowels("Apple")` returns `1` instead of `2` because it doesn't count the capital `A`, so Malik is wrong. Bug report: `count_vowels("Apple")` returns `1`, expected `2`.

**Level 3 Example**

`count_vowels("Apple")` returns `1`. The loop checks each letter with `letter in "aeiou"`, and that string contains only lowercase vowels, so the capital `A` fails the check and only the `e` gets counted. Malik is wrong. The name and the docstring tell me what the author intended, but only the body tells me what the function actually does, and a model writes a name and a docstring with the same confidence whether the body is right or wrong. The way to check is to predict the output for one specific input and then run the function. My bug report: "`count_vowels("Apple")` returns `1`. Expected `2`. The check on line 5, `if letter in "aeiou"`, skips uppercase vowels." Changing that check to `letter.lower() in "aeiou"` would fix the function.

## 1.11 Errors and Tracebacks

<!-- key-terms-from: 11-errors-tracebacks.md -->

**Key terms**

- **Errors** are code that prevents a program from running successfully and are "raised" when something goes wrong, providing valuable debugging information.
- **Syntax errors** occur when code is invalid and can't be executed (e.g., missing quotes, wrong indentation), while **runtime errors** occur when code executes but encounters faulty logic or improper data type usage. Python calls runtime errors **exceptions**.
- Common error types include **`SyntaxError`** (invalid Python), **`NameError`** (undefined variables), **`TypeError`** (wrong data types), **`ValueError`** (right type, wrong value), **`IndexError`** and **`KeyError`** (missing positions and keys), and **`FileNotFoundError`** (operating system constraints).
- A **traceback** is the report Python prints when an error is raised. Reading it from the bottom up tells you the error type, the message, and the chain of function calls that led there.
- Errors can be manually raised using the `raise` keyword, and uncaught errors will cause programs to crash. `try` and `except` let a program catch an error and decide what to do instead.
- **`pytest.raises(ErrorType)`** is how a test checks that a function raises the error it should.

**You will be able to…**

_In the session:_

- Distinguish a syntax error from a runtime error by whether any of the program ran before it appeared.
- Read a traceback from the bottom up: the error type and message, the line where it occurred, and the chain of calls that led there, including across two files.
- Catch a specific error type with `try`/`except`, use the error object's message, and explain why a bare `except:` is avoided.
- Write a loop that keeps asking for input until `int()` succeeds, catching `ValueError`.

_By the end of the module:_

- Name the error type that a given mistake produces, and read an error message to say what went wrong.
- Point at the line where an error occurred and the line where the bad value came from, and say which one the fix belongs on.
- Raise a `ValueError` or `TypeError` from a function that is handed a value it cannot work with.
- Test that a function raises an error with `pytest.raises`, and read the `DID NOT RAISE` failure when it does not.

### Exit Ticket

**Learning Objective**: Fellows will be able to read a traceback from the bottom up and explain which line raised the error, which line supplied the value that caused it, and why output printed before the crash still appeared.

**Question**

Nia's program has two files:

```python
# stats.py
def average(scores):
    return sum(scores) / len(scores)
```

```python
# main.py
from stats import average

def report(name, scores):
    print(f"{name}: {average(scores)}")

def main():
    report("Jamal", [90, 80])
    report("Omar", [])

main()
```

Running `python3 main.py` prints this:

```
Jamal: 85.0
Traceback (most recent call last):
  File "/Users/nia/mod-1/main.py", line 10, in <module>
    main()
  File "/Users/nia/mod-1/main.py", line 8, in main
    report("Omar", [])
  File "/Users/nia/mod-1/main.py", line 4, in report
    print(f"{name}: {average(scores)}")
                     ^^^^^^^^^^^^^^^
  File "/Users/nia/mod-1/stats.py", line 2, in average
    return sum(scores) / len(scores)
           ~~~~~~~~~~~~^~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

Which line raised the error, and which line supplied the value that caused it? Why did `Jamal: 85.0` print even though the program crashed?

**Level 2 Example**

The error is on line 2 of `stats.py`, because `len([])` is `0`. The empty list came from line 8 of `main.py`. `Jamal: 85.0` printed because the first call worked.

**Level 3 Example**

I read the traceback from the bottom up. The last line gives the error type and message, `ZeroDivisionError: division by zero`, and the entry just above it says that the error occurred on line 2 of `stats.py`, inside `average`. `scores` was an empty list, so `len(scores)` was `0`, and dividing by zero raises the error. The entries above that one show how the program got there: `average` was called from `report` on line 4 of `main.py`, and `report` was called on line 8 of `main.py` with `report("Omar", [])`. Line 8 is where the bad value came from, because that call handed an empty list to a function that divides by the list's length. `Jamal: 85.0` printed first because a runtime error happens only when the program reaches the broken line, and the call to `report` on line 7 ran and finished before line 8 was reached.

## 1.12 First-Class Functions and Higher-Order Functions

<!-- key-terms-from: 12-first-class-functions-hof.md -->

**Key terms**

- **Functions are "first-class" values** meaning they can be stored in variables and data structures (lists/dictionaries), passed to functions as arguments, and returned from functions.
- A **method** is a function attached to a value, like `"abc".upper()`. In Mod 2 you will write your own.
- **Higher-order functions (HOFs)** are functions that accept other functions as input and/or return functions, enabling powerful programming patterns and code reuse.
- **Callback functions** are functions passed as arguments to higher-order functions, allowing you to customize behavior without modifying the HOF itself.
- When passing callbacks to HOFs, avoid invoking them (don't use parentheses) - the HOF will handle the invocation with the correct parameters.
- **`lambda`** creates a small anonymous function in one expression, a concise way to define callbacks when they won't be reused elsewhere.
- `sorted()`, `min()`, and `max()` are built-in higher-order functions. Their `key` parameter takes a callback that says what to compare.
- A **wrapper** is a function returned by another function that calls the original and adds behavior around it. Written with an `@` above a definition, it is called a **decorator**.

**You will be able to…**

_In the session:_

- Show that a function is a value: store it in a variable, in a dictionary, and pass it to another function.
- Write a higher-order function that accepts a callback and calls it, and explain what makes it reusable.
- Predict the `TypeError` from passing `say_hello()` instead of `say_hello` as a callback, and explain the `None` that causes it.
- Sort a list of strings by length and find the largest dictionary in a list by one of its values, using `key=`.
- Write a function that returns a wrapper around another function, and predict when each line of it prints.

_By the end of the module:_

- Replace an `if`/`elif` chain of menu options with a dictionary of functions.
- Write a short callback as a `lambda` and say when a `def` is the better choice.
- Explain what `@announce` above a definition does, in terms of `greet = announce(greet)`.
- Change a wrapper so that it returns the wrapped function's return value, and so that it guards the call with a condition.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict what a higher-order function does with a callback and explain the difference between passing a function and passing the value that a call to the function returns.

**Question**

Dev writes a higher-order function and a callback:

```python
def repeat(callback, times):
    for i in range(times):
        callback()

def cheer():
    print("Go team!")

repeat(cheer, 3)
repeat(cheer(), 3)
```

What does each of the last two lines print, and why? The second call raises an error, but `Go team!` still appears once before the error. Why?

**Level 2 Example**

The first call prints `Go team!` three times. The second call prints it once and then raises `TypeError: 'NoneType' object is not callable`, because you shouldn't put parentheses on a callback.

**Level 3 Example**

`repeat(cheer, 3)` prints `Go team!` three times. Writing `cheer` without parentheses passes the function itself, because a function is a value like any other. Inside `repeat`, the parameter `callback` refers to `cheer`, and `callback()` calls it once on each pass through the loop. `repeat(cheer(), 3)` behaves differently because Python resolves the arguments before it calls `repeat`. `cheer()` runs first and prints `Go team!` once, and since `cheer` has no `return` statement, the call produces `None`. So `repeat` receives `None` as its callback, and the first `callback()` inside the loop tries to call `None`, which raises `TypeError: 'NoneType' object is not callable`. The single `Go team!` shows that the callback ran too early, before `repeat` ever received it. A higher-order function calls its callback itself, so the callback should be passed without parentheses.

## 1.13 Comprehensions and Built-in Iteration

<!-- key-terms-from: 13-comprehensions-builtin-iteration.md -->

**Key terms**

- **List comprehensions** provide declarative ways to build new lists from existing ones, making code more readable and reducing the need for explicit loops.
- `[expression for item in items]` **transforms** each element and returns a new list with the transformed values, useful for converting data formats or applying calculations.
- `[item for item in items if test]` **filters**, creating a new list containing only elements that pass a test condition.
- A **dictionary comprehension**, `{key: value for item in items}`, builds a new dictionary the same way a list comprehension builds a new list.
- Finding the **first** element that passes a test is a `for` loop with an early `return` or `break`.
- **`sum()`**, **`min()`**, **`max()`**, and **`len()`** combine a whole list into a single value. When none of them fits, the **accumulator pattern** does: start a variable, update it in a loop, return it.
- **`sorted()`** returns a new sorted list and **`.sort()`** sorts a list in place. Both take a `key` callback that says what to compare and `reverse=True` for descending order.
- **`enumerate()`**, **`zip()`**, **`any()`**, and **`all()`** cover the other everyday loop shapes without an index in sight.
- **`==`** compares the contents of two values. **`is`** and **`is not`** compare identity: whether two names refer to the very same object. A test for a **pure function** uses `==` to check the returned contents and `is not` to check that a new list came back rather than the original.
- To **refactor** is to change how code works without changing what it does. Passing tests are what let you refactor with confidence, for example from a `for` loop to a list comprehension.
- **Test-driven development (TDD)** is a workflow that writes the test first, watches it fail (**red**), writes just enough code to pass (**green**), and then refactors while the tests stay green.
- **`isinstance(value, type)`** asks whether a value is of a given type, and accepts a tuple of types.

**You will be able to…**

_In the session:_

- Rewrite an imperative loop that builds a new list as a list comprehension, and read a comprehension aloud from the `for` outward.
- Filter a list of dictionaries by one of their values.
- Combine a list into one value with `sum()`, `min()`, `max()`, or `len()`, and write the accumulator loop when none of them fits.
- Explain the difference between `sorted()` and `.sort()`, predict the `None` from `result = nums.sort()`, and sort with `key=` and `reverse=True`.

_By the end of the module:_

- Choose the right tool for a loop shape: a `for` loop for side effects, a comprehension to transform, a comprehension with `if` to filter, an early `return` to find the first match, a built-in or accumulator to combine, `sorted()` to order.
- Write a function that returns the first element passing a test, and decide what it returns when nothing passes.
- Build a frequency counter with a dictionary and `.get(key, 0)`.
- Use `enumerate()`, `zip()`, `any()`, and `all()` in place of index-based loops.
- Test a pure function with `==` for its contents and `is not` for a new list, then refactor it from a loop to a comprehension while its tests stay green.
- Apply the TDD cycle to a new requirement: write a failing test, implement just enough to pass, refactor.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict the results of `.sort()`, `sorted()`, and list comprehensions, explain the difference between a tool that changes a list in place and a tool that returns a new list, and rewrite a loop that builds a list as a comprehension.

**Question**

Imani has a list of prices and wants a new list with $2 taken off each price, ordered from cheapest to most expensive:

```python
prices = [12, 3, 8]

discounted = []
for price in prices:
    discounted.append(price - 2)

ordered = discounted.sort()
print(ordered)
```

Imani expected `[1, 6, 10]`. What does the program print, and why? How should Imani fix it? Then rewrite the `for` loop as a list comprehension, and explain why a comprehension can do the loop's job.

**Level 2 Example**

The program prints `None` because `.sort()` doesn't return anything. Imani should use `sorted(discounted)` instead. The loop can be `discounted = [price - 2 for price in prices]`.

**Level 3 Example**

The program prints `None`. `.sort()` sorts a list in place, which means it changes `discounted` itself and returns nothing, so `ordered` gets `None`. The list in `discounted` is now `[1, 6, 10]`, but Imani never prints it. Imani should write `ordered = sorted(discounted)`, because `sorted()` returns a new sorted list and leaves `discounted` unchanged. Calling `discounted.sort()` on its own line and then printing `discounted` would also work. The loop can become `discounted = [price - 2 for price in prices]`. The loop transforms every value and collects the results in a new list, and that is exactly what a list comprehension does: for each `price` in `prices`, it computes `price - 2` and adds the result to a new list that has as many elements as the source. Combining the two steps, `ordered = sorted([price - 2 for price in prices])` does the whole job in one line.

## Case Study: CLI Task Manager

**Key terms:** none new. The case study exercises the terms from lessons 1 to 13.

**You will be able to…**

_In the session:_

- Set up and run a multi-file Python project from a repository using a virtual environment.
- Trace a menu choice from `main.py` through `menu.py` to the function in `tasks.py` that handles it.
- Identify every guard clause in the application and predict what would happen without each one.
- Predict how the program responds to invalid input, and identify the `try`/`except` and the two-condition check that handle it.

_By the end of the module:_

- Explain how the task manager's data is represented and justify the choice of a boolean over a number or a string.
- Explain why `tasks` lives in `tasks.py` and is not imported into `menu.py`, and why only `main.py` has the `__main__` guard.
- Explain why the menu uses a `while` loop, what `is_running` does, and how the same loop could be written with `break`.
- Debug a model-written `delete_task()` and write a bug report that names the input, the actual output, the expected output, and the line at fault.
- Plan a dispatch table for the menu and explain which option cannot go into it.
- Write a list comprehension that selects the completed tasks, and use `all()` to check whether every task is complete.
- Extend the application with a new feature that respects the existing separation of concerns.

### Exit Ticket

**Learning Objective**: Fellows will be able to predict the effect of a change to the task manager and justify the application's separation of concerns by explaining what the change would bypass.

**Question**

In the task manager, `menu.py` imports `add_task` from `tasks.py` but does not import the `tasks` list. Carlos suggests a shortcut: add `from tasks import tasks` to `menu.py`, and replace the call to `add_task(description)` in the menu's option `1` branch with this line:

```python
tasks.append({"description": description, "is_complete": False})
```

Would Add Task still add tasks? What would happen if the user pressed Enter without typing a description, and why? Why did the author keep the `tasks` list out of `menu.py`?

**Level 2 Example**

Add Task would still work, because `menu.py` would have the same list. But a task with an empty description could be added, because the guard clause in `add_task()` would be skipped. Keeping `tasks` in `tasks.py` is separation of concerns.

**Level 3 Example**

Add Task would still add tasks, because `from tasks import tasks` gives `menu.py` a reference to the same list that `tasks.py` holds, and `.append()` mutates that one list. But Carlos's line skips everything inside `add_task()`. `add_task()` starts with the guard clause `if not description:`, and an empty string is falsy, so the guard clause refuses an empty description and prints `Task description cannot be empty.` Without that guard clause, pressing Enter without typing anything would add a task with a blank description to the list, and the user would no longer see the `Task "..." added!` confirmation either, because `add_task()` prints it. The author kept `tasks` out of `menu.py` so that only the functions in `tasks.py` can change the list. Each module has one concern: `menu.py` talks to the user, and `tasks.py` owns the data and the rules about it. A rule like "no empty descriptions" then lives in exactly one place, no other file can go around it, and anyone looking for the cause of a bad task only has to search `tasks.py`.

## Project: CLI Application

**Key terms:** none new. The project applies the terms from lessons 1 to 13.

**You will be able to…**

_In the session:_

- Build an interactive command-line application from a written specification, one feature at a time, committing after each.
- Organize the code into an entry point, a menu module, and a data module, with an `if __name__ == "__main__":` guard and a virtual environment kept out of Git.
- Represent the application's data as a dictionary or a list of dictionaries and choose the shape deliberately.

_By the end of the module:_

- Validate every piece of user input so that the program never ends with a traceback.
- Write a `README.md` that lets someone else set up and run the program, and a reflection that explains one concept in plain terms.
- Describe the program well enough to critique generated additions to it in December.

### Exit Ticket

**Learning Objective**: Fellows will be able to compare ways of building an application and justify building, running, and committing one feature at a time, in terms of how quickly each way finds a bug and recovers from one.

**Question**

Zoe and Kwame each build the Shopping List app. Zoe writes all four features (add, remove, view, and total) in one evening and runs the program for the first time at the end. Choosing View crashes with `KeyError: 'qty'`. Kwame builds Add Item first, runs it with good and bad input, and commits it, then does the same for View, then Remove, then Total. Suppose Kwame made the same mistake while writing View. Which of the two would find the cause of the `KeyError` faster, and why? What can Kwame do if adding Total later breaks something that used to work?

**Level 2 Example**

Kwame would find it faster, because Kwame had only written one new feature since the program last worked. If Total breaks something, Kwame can go back to the last commit.

**Level 3 Example**

Kwame would find the cause faster. `KeyError: 'qty'` means some line reads the key `"qty"` from an item dictionary that does not have that key, probably because a different line stored the quantity under `"quantity"`. Kwame ran the program right after writing View, and Add Item had already been run and committed, so the mistake has to be in the few lines of View, or in how View reads the dictionaries that Add Item builds. Zoe ran the program for the first time after writing every feature, so the wrong key could be in any line of any feature that builds or reads an item, and Zoe has to search all of them. If Total breaks something that used to work, Kwame can compare the code with the last commit, or go back to it, because each of Kwame's commits records a version of the program that was known to work. Zoe has never had a version that was known to work, so Zoe has no such version to go back to.
