# 1.9 Modules, Virtual Environments, and pytest

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/09-modules-environments-pytest/)
{% endhint %}

In this lesson we'll learn how Python programs are split across multiple files and how those files share code with each other. Then we'll learn where Python code comes from when you didn't write it: the standard library that ships with Python, the packages other people publish, and the virtual environments that keep each project's packages separate. The package we will install is `pytest`, and we will finish by using it to test our own code.

**Table of Contents:**

- [Key Terms](#key-terms)
- [Modules](#modules)
  - [Every Top-Level Name Can Be Imported](#every-top-level-name-can-be-imported)
  - [Importing with `import` and `from ... import`](#importing-with-import-and-from--import)
- [What Happens When You Import a File?](#what-happens-when-you-import-a-file)
  - [`__name__`](#__name__)
  - [The `if __name__ == "__main__":` Guard](#the-if-__name__--__main__-guard)
  - [Madlib Challenge, Part 2](#madlib-challenge-part-2)
- [The Standard Library](#the-standard-library)
- [Third-Party Packages and PyPI](#third-party-packages-and-pypi)
- [Virtual Environments with `venv`](#virtual-environments-with-venv)
- [Installing Packages with `pip`](#installing-packages-with-pip)
- [Dependencies and Sub-Dependencies](#dependencies-and-sub-dependencies)
- [`requirements.txt`](#requirementstxt)
  - [Keep `.venv` Out of Git](#keep-venv-out-of-git)
- [Developer Dependencies](#developer-dependencies)
- [Testing Your Code with pytest](#testing-your-code-with-pytest)
  - [Project Layout](#project-layout)
  - [First Test](#first-test)
  - [Practice: Add A Test](#practice-add-a-test)
  - [Reading a Failure](#reading-a-failure)
  - [Checking `True`, `False`, and Decimals](#checking-true-false-and-decimals)
- [The Commands, All Together](#the-commands-all-together)

## Key Terms

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

## Modules

Consider the simple Python program below. It defines a few functions for calculating data about a circle with a given radius and then prints them out. Notice that the `main` function is where the functions are all being executed in a logical order:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
# functions for circle stuff
LAZY_PI = 3.14

def get_area(radius):
    return LAZY_PI * radius * radius

def get_diameter(radius):
    return radius * 2

def get_circumference(radius):
    return LAZY_PI * radius * 2

# Helper function for printing stuff.
# It is a "wrapper" for the print function
def display(message):
    print(message)

# The main function just runs all of the other functions
def main():
    radius = 5
    area = get_area(radius)
    display(f"the area of a circle with radius {radius} is {area}")

    diameter = get_diameter(radius)
    display(f"the diameter of a circle with radius {radius} is {diameter}")

    circumference = get_circumference(radius)
    display(f"the circumference of a circle with radius {radius} is {circumference}")

main()
```

{% endcode %}

This file is short enough to read in one go. Now imagine it with fifty circle functions, a dozen display helpers, and the code that ties them together. To fix a wrong area, you would scroll past all of the display code to find `get_area`. Two teammates fixing different things would be editing the same file at the same time. As a project grows, **separation of concerns** is what keeps it manageable.

{% hint style="info" %}
Separation of Concerns is a fundamental principle of software engineering. It emphasizes the importance of organizing our code into distinct functions and modules that each serve a singular and specific purpose. However, when put together, those individual pieces work in harmony.
{% endhint %}

To achieve separation of concerns, Python projects are typically separated into multiple files called **modules** that share code with each other.

A **module** is a file containing code, which can then be **imported** and utilized in other parts of a larger program or system.

### Every Top-Level Name Can Be Imported

Every name assigned at the top level of a file, meaning every function and every variable that is not indented inside something else, can be imported by another file. That means a function can leave `main.py` and `main.py` can still call it, by importing it back.

So we can move the `display` function into its own file:

{% code title="display.py" overflow="wrap" lineNumbers="true" %}

```python
def display(message):
    print(message)
```

{% endcode %}

And the circle functions into theirs:

{% code title="circle_helpers.py" overflow="wrap" lineNumbers="true" %}

```python
LAZY_PI = 3.14

def get_area(radius):
    return LAZY_PI * radius * radius

def get_diameter(radius):
    return radius * 2

def get_circumference(radius):
    return LAZY_PI * radius * 2
```

{% endcode %}

That is the whole file. `LAZY_PI`, `get_area`, `get_diameter`, and `get_circumference` are all available to any file that imports `circle_helpers`.

### Importing with `import` and `from ... import`

To use a module's names, use the `import` statement. A module's name is its filename without the `.py`. When you run `python3 main.py`, Python looks for `circle_helpers.py` and `display.py` in the same folder as `main.py`, so keep the three files side by side. Move `display.py` into a different folder and `from display import display` stops with `ModuleNotFoundError: No module named 'display'`.

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
# Import the whole module. Its names are reached with dot notation.
import circle_helpers

# Import one specific name from a module. It can then be used directly.
from display import display

def main():
    radius = 5

    # the get_area function is INSIDE of the circle_helpers module so we use dot notation
    area = circle_helpers.get_area(radius)

    # display was imported by name so we can just invoke it.
    display(f"the area of a circle with radius {radius} is {area}")

    # ... the rest of the code ...

main()
```

{% endcode %}

**<details><summary>Q: How does this file structure demonstrate separation of concerns? What is the concern of each file?</summary>**

Each file is concerned with only one aspect of the functionality of the entire program.

- `display.py` is concerned with output logic.
- `circle_helpers.py` is concerned with logic related to circle calculations.
- `main.py` is concerned with combining the functions and executing them in a logical manner.

</details>

If you will use several names from a module, you can list them all in one `from` statement, and then none of them need the module name in front:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
from circle_helpers import get_area, get_diameter, get_circumference
```

{% endcode %}

You can also give a module a shorter name as you import it with `as`:

```python
import circle_helpers as ch

area = ch.get_area(5)
```

You will see this constantly in other people's code, where long library names get two-letter aliases.

There is also `from circle_helpers import *`, which imports every name in the module at once.

**<details><summary>Q: Why write `import circle_helpers` and then `circle_helpers.get_area(...)`, or list the names you want, when `from circle_helpers import *` would let you write `get_area(...)` with less typing?</summary>**

Two reasons, and the second is the important one.

First, readability. When a reader sees `circle_helpers.get_area(radius)` in `main.py`, they know exactly which file to open to find out what `get_area` does. With `import *`, `get_area` appears from nowhere.

Second, safety. `import *` brings in _every_ top-level name in the module, including ones you did not know were there. Suppose someone adds a variable called `len` to `circle_helpers.py`. After `from circle_helpers import *`, the built-in `len` function in `main.py` is silently replaced by their variable, and every `len(...)` call in your file breaks. Importing by name means nothing arrives that you did not ask for.

</details>

## What Happens When You Import a File?

Here is something that surprises almost everyone. Importing a file **runs it**, top to bottom, the first time it is imported, almost exactly as if you had typed `python3 circle_helpers.py`. The one difference is a variable called `__name__`, which is coming up shortly.

{% hint style="warning" %}
**Predict, then run.** Add one line to the very bottom of `circle_helpers.py`:

```python
print("circle_helpers was loaded")
```

Then run `python3 main.py` (not `circle_helpers.py`). Write down everything you expect to see printed, in order.

<details><summary>What actually happens</summary>

```
circle_helpers was loaded
the area of a circle with radius 5 is 78.5
the diameter of a circle with radius 5 is 10
the circumference of a circle with radius 5 is 31.400000000000002
```

The message from `circle_helpers.py` prints _first_, before anything from `main.py`. When the interpreter reaches `import circle_helpers` on line 2 of `main.py`, it goes and runs all of `circle_helpers.py`. The `def` statements create the functions, and the `print` at the bottom prints. Only then does it return to `main.py` and continue.

(That `31.400000000000002` is the slightly inexact decimal arithmetic from chapter 1.6, and `{circumference:.2f}` in the f-string would display it as `31.40`.)

</details>
{% endhint %}

{% hint style="info" %}
**What is that `__pycache__` folder?** The first time you import a module, a folder called `__pycache__` appears next to it, holding a file like `circle_helpers.cpython-312.pyc`. That is a pre-processed copy of the module that Python saves so the next import is faster. It is rebuilt automatically whenever the module changes, you never edit it, and it never belongs in Git. The `.gitignore` section later in this lesson shows how to keep it out.
{% endhint %}

Running a file when it is imported is usually fine, because most of what is in a module is `def` statements, and a `def` statement only creates a function without running the code inside it. But what if a file is _both_ a program you sometimes run directly _and_ a module other files import? `main.py` ends with a call to `main()`. If another file imported `main.py` to reuse one function, `main()` would run during the import. The circle results would print in the middle of the other program's output. Worse, if that file were the madlib `main.py`, the person using the other program would suddenly be asked to `Choose a name:`.

### `__name__`

Every module has a variable called `__name__` that Python sets for it automatically. Replace the `print` at the bottom of `circle_helpers.py` with this, and add the same line to the bottom of `main.py`:

```python
print(f"my __name__ is {__name__}")
```

Now run `python3 main.py`:

```
my __name__ is circle_helpers
my __name__ is __main__
```

When a file is imported, its `__name__` is its module name. When a file is the one you ran with `python3`, its `__name__` is the special string `"__main__"`. So a file can tell which situation it is in.

### The `if __name__ == "__main__":` Guard

That gives us the standard way to finish a Python program:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
from circle_helpers import get_area, get_diameter, get_circumference
from display import display

def main():
    # ...

if __name__ == "__main__":
    main()
```

{% endcode %}

Read it as: "if this file is the one being run, call `main()`." When `main.py` is run with `python3 main.py`, the condition is true and the program starts. If any other file ever does `import main`, the condition is false and nothing runs except the `def` statements.

You will see this guard at the bottom of nearly every Python program you read, and you should put it at the bottom of every one you write. The two underscores on each side of `name` and `main` are part of the spelling; Python uses that pattern for names it manages itself.

### Madlib Challenge, Part 2

Open the `madlib-challenge` folder from chapter 1.6. Right now, the `madlib` function and the `main` function that asks the user for input share one file.

1. Re-organize the code such that the `madlib` function is in its own file called `madlib.py`, and `main.py` imports it.
2. Replace the `main()` call at the bottom of `main.py` with the `if __name__ == "__main__":` guard.

**<details><summary>Q: Solution</summary>**

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
from madlib import madlib

def main():
    name = input('Choose a name: ')
    verb = input('Choose a verb: ')
    quantity = input('Choose a quantity: ')
    item = input('Choose an item: ')
    new_item = input('Choose a new item: ')
    is_happy_response = input('Choose whether the story is happy. Y or N: ')
    is_happy = is_happy_response.strip().upper() == "Y"

    madlib(name, verb, quantity, item, new_item, is_happy)

if __name__ == "__main__":
    main()
```

{% endcode %}

{% code title="madlib.py" overflow="wrap" lineNumbers="true" %}

```python
def madlib(name, verb, quantity, item, new_item, is_happy):
    print(f"There once was a man named {name}.")
    print(f"Every day he would {verb} with his {quantity} {item}s")

    if is_happy:
        print(f"But then, he found a {new_item} and everything changed!")
    else:
        print(f"But then, a {new_item} took over his life and he couldn't {verb} again!")

    print("The end.")
```

{% endcode %}

`madlib.py` is concerned with telling the story. `main.py` is concerned with collecting the user's choices. Neither file needs to know how the other does its job.

</details>

## The Standard Library

Python is described as coming with "batteries included". A large collection of modules, the **standard library**, is installed alongside the interpreter itself. You have already used one:

```python
import random

print(random.random())              # a float ≥ 0 and < 1
print(random.randint(1, 10))        # a whole number from 1 to 10, inclusive
print(random.choice(["heads", "tails"]))  # one item from a list, chosen at random
```

These modules are imported exactly the same way as your own `circle_helpers.py`, and the interpreter finds them for you. Here is `math`:

```python
import math

print(math.pi)         # 3.141592653589793
print(math.ceil(4.2))  # 5
print(math.floor(4.8)) # 4
```

Remember `LAZY_PI = 3.14` from the start of this lesson? `math.pi` is the version that isn't lazy.

One more you will want soon is `json`, which turns lists and dictionaries into text that can be saved in a file, and back again. That text format is called **JSON**:

```python
import json

tasks = [{"description": "walk the dog", "is_complete": False}]

# Write the list to a file as JSON text
with open("tasks.json", "w") as file:
    json.dump(tasks, file)

# Read it back into a list
with open("tasks.json") as file:
    saved_tasks = json.load(file)

print(saved_tasks)  # [{'description': 'walk the dog', 'is_complete': False}]
```

`open()` is a built-in function that opens a file. The `"w"` means "open it for writing": it creates `tasks.json` if the file does not exist and replaces whatever was in it if it does. The second `open()` has no `"w"`, so it opens the file for reading, which is what `open()` does by default. The `with` statement closes the file again when the indented block ends. This is how the task manager case study can be extended to remember its tasks between runs.

Nobody memorizes the standard library. The habit to build is to ask "does Python already have this?" before writing it yourself, and to check the [standard library documentation](https://docs.python.org/3/library/index.html) when you suspect it does.

## Third-Party Packages and PyPI

Suppose you wanted a tool that checks every function in your project and tells you which ones return the wrong answer, all with a single command. Do you have the tools to implement that feature on your own?

While you could figure this out, there is no need to reinvent the wheel! Instead, just download an existing package from the **Python Package Index (PyPI)**.

A **package** is a folder of modules that someone has published so that other people can install it and import it into their own programs. Packages, and the standard library, are also called **libraries**: code written for other programs to use, rather than a program you run on its own.

Visit https://pypi.org/ to explore available packages. Start by searching for the "pytest" package. Its page shows a description, usage examples, and the command to install it.

But before installing anything, we need somewhere to put it.

## Virtual Environments with `venv`

Every Python project you build will need its own set of packages, often in different versions. If every project installed its packages into the one Python on your computer, they would collide: project A needs version 2 of something, project B needs version 3, and one of them stops working.

A **virtual environment** solves this. It is a folder inside your project that holds its own packages, along with a `python3` that is a link to the Python interpreter already installed on your computer. Whatever you install while it is turned on goes there and nowhere else.

Create one in your project folder with the `venv` module, which is part of the standard library:

```sh
python3 -m venv .venv
```

`python3 -m venv` means "run the `venv` module as a program". The `.venv` at the end is the name of the folder to create. It starts with a dot so that it is hidden from `ls` and does not clutter your view of the project. The name `.venv` is a convention that editors like VS Code recognize.

Then turn it on. This is called **activating** the environment:

```sh
source .venv/bin/activate
```

Your Terminal prompt changes to show `(.venv)` at the front. That is how you know it is on. From now on, in this Terminal window, `python3` and `pip` refer to the ones inside `.venv`:

```sh
which python3
# /Users/you/mod-1/9-testing/.venv/bin/python3
```

Because of that, a package you install with the environment on lives only inside `.venv`. If you ever get a `ModuleNotFoundError` for a package you are sure you installed, look at the prompt before you do anything else. Nine times out of ten, `(.venv)` is missing, which means `python3` is your computer's own Python, and that Python has never had the package installed.

To turn it off, type `deactivate`. You will need to activate it again in every new Terminal window you open for this project.

{% hint style="info" %}
On Windows under WSL, these are the same commands. You are running Ubuntu, and Ubuntu is what these instructions were written for.

If VS Code asks you to select a Python interpreter, choose the one inside `.venv`.
{% endhint %}

## Installing Packages with `pip`

With the environment activated, install a package with `pip install`:

```sh
pip install pytest
```

`pip` downloads the package from PyPI and prints what it did (version numbers may vary):

```
Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest
Successfully installed iniconfig-2.3.0 packaging-26.3 pluggy-1.6.0 pygments-2.21.0 pytest-9.1.1
```

You may also see a `[notice]` that a newer version of `pip` is available. That is a suggestion, not an error, and you can ignore it.

`pip list` shows everything installed in the active environment:

```
Package   Version
--------- -------
iniconfig 2.3.0
packaging 26.3
pip       24.0
pluggy    1.6.0
Pygments  2.21.0
pytest    9.1.1
```

## Dependencies and Sub-Dependencies

When you install a package for your project, it is called a **dependency**: your project depends on it.

Notice that `pip install pytest` installed five packages, not one. `pytest` itself needs `iniconfig`, `packaging`, `pluggy`, and `pygments` to work, so `pip` installed those as well. They are **sub-dependencies**. You can see what a package requires with `pip show`:

```sh
pip show pytest
```

```
Name: pytest
Version: 9.1.1
Summary: pytest: simple powerful testing with Python
...
Requires: iniconfig, packaging, pluggy, pygments
```

Sub-dependencies can have dependencies of their own, and `pip` follows the whole chain.

**<details><summary>Q: You only asked for `pytest`. What would happen if `pip` installed `pytest` and nothing else?</summary>**

The first time `pytest` tried to `import pluggy`, it would crash with `ModuleNotFoundError: No module named 'pluggy'`. A package is written by importing other packages, exactly the way your `main.py` imports `circle_helpers.py`, so every package it imports has to be installed too.

</details>

## `requirements.txt`

The `.venv` folder can be big, and it is specific to your computer. So it is **never** committed to Git. Instead, you commit a small text file that says what to install, and anyone (including future you, on a new laptop) rebuilds the environment from it.

That file is `requirements.txt`, and `pip` writes it for you:

```sh
pip freeze > requirements.txt
```

`pip freeze` prints every installed package with its exact version, and `>` sends that output into the file instead of the screen (you met `>>` in Mod 0; `>` is the same idea but replaces the file rather than adding to it). Open it up:

```
iniconfig==2.3.0
packaging==26.3
pluggy==1.6.0
Pygments==2.21.0
pytest==9.1.1
```

The `==` records the exact version, so that everyone who installs from this file gets the same packages you tested with.

To install everything a `requirements.txt` lists, in a fresh environment:

```sh
pip install -r requirements.txt
```

This is the command you will run every time you clone a project. The pattern is always the same:

```sh
git clone [repo_url]
cd [repo_name]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Keep `.venv` Out of Git

Create a file called `.gitignore` in the project folder, if there isn't one already, and add two lines:

```
.venv/
__pycache__/
```

Git will then pretend those folders do not exist. The second line covers the `__pycache__` folders that Python creates whenever it imports a module, which Python rebuilds on its own and which never belong in Git.

**<details><summary>Q: Why not just commit `.venv` so that nobody has to run `pip install`?</summary>**

Three reasons. It is large: with only `pytest` installed, `.venv` already holds about 30 megabytes in roughly 2,000 files, and it grows with every package you add. Git is built for the files you write, not for installed programs. It is also specific to your machine. `.venv/bin/python3` is a link, a tiny file that points to the place Python is installed on your computer, and the other programs in `.venv/bin` record the full path of the folder `.venv` was created in. On a teammate's computer those paths may lead nowhere, so the environment would not work there anyway. And it is completely reproducible from `requirements.txt` in a few seconds, so there is nothing to gain.

The general rule: commit the recipe, not the meal.

</details>

## Developer Dependencies

Some packages are used by the developer(s) who are building a project but aren't needed by the people who run it. These are called **developer dependencies**. `pytest` is one of them.

**<details><summary>Q: Why is `pytest` a developer dependency and not a required dependency of the project?</summary>**

Only the files in `tests/` import `pytest`. The files in `src/` that make up the program never do, so someone who just wants to _run_ your program can do it without `pytest` installed. `pytest` serves the people building the program.

</details>

Many projects keep a second file, `requirements-dev.txt`, for developer dependencies. For this module, one `requirements.txt` with everything in it is fine.

## Testing Your Code with pytest

Up to now, you have checked your functions by calling them and reading what `print()` shows.

> "Now that we've tested the application, what should we do with the tests? Do we delete them? Do we comment them out? If we keep them, where can they live?"

With manual testing, your tests are the `print()` calls you added to check each function, and you're always left with this question. You've spent time and effort writing them, so deleting them is wasteful. But if you leave them in, they run every time the program runs, and, as you saw earlier in this lesson, every time another file imports that file. Whoever runs the program sees your check results mixed in with its real output and has no idea what they mean.

Rather than testing functions directly in the files where they live, it is better to create separate **test files** that import functions and test them against sample inputs. Test files provide a number of benefits:

- **Separation of concerns**: our source code can focus on functionality while test files focus on testing.
- **Automation**: test files can be executed with a single command or can be configured to run automatically whenever a commit is made, ensuring all new code is functional.
- **Documentation**: test files serve as living documentation, showing how functions are expected to behave.
- **Confidence**: having a comprehensive test suite gives developers confidence when making changes.

The assignments in this program come with test files already written. Running them tells you which of your functions work and which do not.

### Project Layout

Organize the project so that source code and tests live in separate folders:

```
9-testing/
├── .venv/
├── requirements.txt
├── src/
│   └── calc.py
└── tests/
    └── test_calc.py
```

`pytest` finds tests by name. It looks for files whose names start with `test_`, and inside them, for functions whose names start with `test_`. There is nothing to configure.

### First Test

In the file called `src/calc.py`, define a simple `add` function.

```python
# calc.py
def add(a, b):
    return a + b
```

In the `tests` directory, create a file called `test_calc.py` (the test file name should always match the name of the file being tested, with `test_` in front).

Then, add the following code:

```python
# test_calc.py
from src.calc import add


def test_add():
    """add - adds two positive numbers"""
    assert add(1, 2) == 3
    assert add(10, 5) == 15
```

The first line imports `add` from `src/calc.py`. When a module sits inside a folder, you write the folder name, a dot, and then the module name, so `src.calc` means "the `calc` module inside the `src` folder". Python starts looking from the folder you run the tests in, which is why the hint below says to run them from the project's root folder.

Each function whose name starts with `test_` is one test. Name it after the function it tests. The string on the first line is a docstring, the function description you met in chapter 1.3. In a test, the docstring says what the test checks. Inside, the `assert` statement is the whole mechanism:

- `assert expression` checks that the `expression` is truthy. If it is, nothing happens and the test continues.
- If it is falsy, `assert` raises an `AssertionError`, the test stops, and pytest reports it as a failure.
- `add(1, 2) == 3` is an ordinary comparison, the same `==` from chapter 1.2. There is no special testing vocabulary to learn.

A test can hold as many `assert` statements as you like. The test passes only if every one of them passes.

Run the tests with:

```sh
python3 -m pytest
```

And you should see something like this (the Python and pytest version numbers will be whatever is on your machine):

```
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/ben/mod-1/9-testing
collected 1 item

tests/test_calc.py .                                                     [100%]

============================== 1 passed in 0.00s ===============================
```

Each dot after a filename is one passing test. We see a passing test because every `assert` expression was `True`.

{% hint style="info" %}
**Why `python3 -m pytest` and not just `pytest`?** Installing pytest gives you a `pytest` command as well, and you will see it in other people's instructions. But `pytest` on its own does not put your project folder on the list of places Python looks for modules, so `from src.calc import add` fails with `ModuleNotFoundError: No module named 'src'`. Running it through `python3 -m` adds the folder you are in to that list. The project's root folder, `9-testing/`, contains `src/`, so from there `from src.calc import add` works. If you `cd tests` first, Python adds `tests/` instead, finds no `src` there, and you are back to `ModuleNotFoundError`. So run `python3 -m pytest` from the project's root folder every time.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Deactivate the environment with `deactivate`, then run `python3 -m pytest` again. What happens?

<details><summary>What actually happens</summary>

```
/usr/local/bin/python3: No module named pytest
```

(The path at the front is wherever Python lives on your computer, so yours may differ.) `pytest` was installed into `.venv`, and with `.venv` turned off, `python3` is the copy of Python that came with your computer, which has never heard of it.

This is the error you will see most often for the rest of the year, and it almost always means one of two things: you forgot to activate the environment, or you forgot to install the package into it. Check the `(.venv)` at the front of your prompt first.

Activate the environment again with `source .venv/bin/activate` before moving on.

</details>
{% endhint %}

### Practice: Add A Test

In the `tests/test_calc.py` file, add a new test called `test_add_negatives` that confirms that the `add` function will work properly for inputs like `-3` and `-2`.

**<details><summary>Solution</summary>**

```python
def test_add_negatives():
    """add - adds two negative numbers"""
    assert add(-3, -2) == -5
```

</details>

Run `python3 -m pytest` again and you should now see two dots. To see every test by name, add `-v` (for "verbose"):

```sh
python3 -m pytest -v
```

```
tests/test_calc.py::test_add PASSED                                      [ 50%]
tests/test_calc.py::test_add_negatives PASSED                            [100%]
```

### Reading a Failure

Change the expected value in your new test to `-6`, run the tests again, and look at what pytest tells you:

```
tests/test_calc.py .F                                                    [100%]

=================================== FAILURES ===================================
______________________________ test_add_negatives ______________________________

    def test_add_negatives():
        """add - adds two negative numbers"""
>       assert add(-3, -2) == -6
E       assert -5 == -6
E        +  where -5 = add(-3, -2)

tests/test_calc.py:12: AssertionError
=========================== short test summary info ============================
FAILED tests/test_calc.py::test_add_negatives - assert -5 == -6
========================= 1 failed, 1 passed in 0.01s ==========================
```

The test output provides some really useful information.

- We can see which tests failed: the `F` in the dots, and the name under `FAILURES`
- For each failing test, we can see which `assert` statement failed, marked with `>`
- We can see what the function actually returned (`-5`) and what we said it should be (`-6`), and pytest even shows you the call that produced the `-5`.

Armed with this information, we can more confidently build our functions knowing that we have a specific set of targets to aim for. Automated tests allow us to repeatedly run our code against the same set of tests until all expectations are met.

Change the `-6` back to `-5` before moving on.

### Checking `True`, `False`, and Decimals

Two more kinds of assertion appear all over the test files in your assignments.

When a function should return `True`, `False`, or `None`, the test uses `is` rather than `==`:

```python
def test_is_even():
    """is_even - returns True for even numbers, False for odd"""
    assert is_even(2) is True
    assert is_even(3) is False
```

`is` is the identity operator from chapter 1.2. There is only one `True` and one `False` in a Python program, so `is True` asks "did the function return the boolean `True` itself?"

**<details><summary>Q: Suppose `is_even` were written as `return 1 - num % 2`, which returns `1` for even numbers and `0` for odd ones. Would `assert is_even(2) == True` pass? Would `assert is_even(2) is True`?</summary>**

The `==` version passes, because `True` counts as `1` in arithmetic, so `1 == True` is `True`. The `is` version fails:

```
E       assert 1 is True
E        +  where 1 = is_even(2)
```

`1` is truthy, but it is not the boolean `True`. That difference shows up as soon as someone uses the function: `print(f"Is 4 even? {is_even(4)}")` prints `Is 4 even? 1`, and whoever reads that has to guess what `1` means. A function named `is_even` promises a boolean. The `==` version lets the broken function pass, and the `is True` version catches it.

</details>

When a function returns a decimal number, the test compares with `pytest.approx()`:

```python
import pytest
from src.calc import add


def test_add_decimals():
    """add - adds decimal numbers"""
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

Remember from chapter 1.2 that `0.1 + 0.2 == 0.3` is `False`, because decimals are stored very slightly inexactly. `pytest.approx(0.3)` means "a number close enough to `0.3` that the difference is only that inexactness." Using it requires `import pytest` at the top of the test file.

## The Commands, All Together

```sh
# Create a virtual environment (once per project)
python3 -m venv .venv

# Activate it (once per Terminal window)
source .venv/bin/activate

# Turn it off
deactivate

# Install a package into the active environment
pip install [package]

# See what is installed
pip list

# See what a package requires
pip show [package]

# Record what is installed
pip freeze > requirements.txt

# Install everything a project needs
pip install -r requirements.txt

# Run every test in the project
python3 -m pytest
```
