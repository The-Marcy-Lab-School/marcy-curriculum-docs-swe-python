# Mod 1 Learning Objectives and Key Terms

One entry per lesson. Key terms are copied from each lesson's **Key Terms** section by `scripts/sync-key-terms.py`, so edit them in the lesson and rerun the script rather than editing them here. Learning objectives are written so that each one could be checked with a short task. Each list is split in two. _In the session_ names the three or four objectives the 90-minute lecture is responsible for: introduced, practiced, and checked before it ends. _By the end of the module_ names the rest, which the chapter's reading, the assignment, and the project carry, and which the Mod 1 assessment can draw on.

## 1.1 — Intro to Programming

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

## 1.2 — Data Types, Variables, and Operators

<!-- key-terms-from: 2-data-types-variables.md -->

**Key terms**

- **State** refers to the data stored by a program at a point in time.
- **Data types** are categories of values in Python. There are 5 basic types (`str`, `int`, `float`, `bool`, `None`) and 3 types that hold other data or code (`list`, `dict`, and functions). Knowing the type of a value helps determines how you can use that value. Choosing the right type to represent your data is essential.
- **Operators** are symbols (e.g. `+`, `>=`, `and`) that generate new data from existing values.
  - **Arithmetic operators** (`+`, `-`, `*`, `/`, `//`, `%`, `**`) calculate a new value from numbers.
  - **Comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) compare two values and produce a boolean.
  - **Logical operators** (`and`, `or`, `not`) combine or reverse conditions.
  - **Membership operators** (`in`, `not in`) check whether a value is inside a string, list, or dictionary.
  - **Identity operators** (`is`, `is not`) check whether two names refer to the very same object.
  - **Assignment operators** (`=`, `+=`, `-=`, and the rest) store a value in a variable.
- **Operator precedence** is the order in which Python evaluates the operators in an expression, such as multiplication before addition. Parentheses change that order: whatever is inside them is evaluated first.
- **Variables** are named containers for data. You can reference and reassign variables to store and update information in your program.
  - A variable is created the first time it is assigned. Names in `ALL_CAPS` are a signal to readers that a value is a constant and should not be reassigned.
- **`snake_case`** is the Python convention for naming variables and functions: lowercase words joined by underscores, like `days_in_each_month`.

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

## 1.3 — Functions

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

## 1.4 — Conditional Statements

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

## 1.5 — Loops

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

## 1.6 — Inputs and Outputs

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

## 1.7 — Lists

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

## 1.8 — Dictionaries

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

## 1.9 — Modules, Virtual Environments, and pytest

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
- A **virtual environment** is a private copy of Python and its packages for one project. You create one with `python3 -m venv .venv` and turn it on with `source .venv/bin/activate`.
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

## 1.10 — Reading Unfamiliar Code

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

## 1.11 — Errors and Tracebacks

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

## 1.12 — First-Class Functions and Higher-Order Functions

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

## 1.13 — Comprehensions and Built-in Iteration

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
