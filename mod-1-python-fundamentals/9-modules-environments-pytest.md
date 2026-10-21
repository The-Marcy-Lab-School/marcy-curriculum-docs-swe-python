# 1.9 Modules, Virtual Environments, and pytest

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/09-modules-environments-pytest/)
{% endhint %}

In this lesson we'll learn how a program is split into pieces that each do one job: first into functions, and then into separate files that share code with each other. Then we'll learn where Python code comes from when you didn't write it: the standard library that ships with Python, the packages other people publish, and the virtual environments that keep each project's packages separate. The package we will install is `pytest`, the tool that has been running the tests in your assignments.

**Table of Contents:**

- [Key Terms](#key-terms)
- [Modularity](#modularity)
  - [One Long Block of Code](#one-long-block-of-code)
  - [Helper Functions and a `main()` Function](#helper-functions-and-a-main-function)
- [Modules](#modules)
  - [One Kind of Function per Module](#one-kind-of-function-per-module)
  - [Every Top-Level Name Can Be Imported](#every-top-level-name-can-be-imported)
  - [Importing with `import` and `from ... import`](#importing-with-import-and-from--import)
- [What Happens When You Import a File?](#what-happens-when-you-import-a-file)
  - [`__name__`](#__name__)
  - [The `if __name__ == "__main__":` Guard](#the-if-__name__--__main__-guard)
  - [A Traceback Across Two Files](#a-traceback-across-two-files)
  - [Challenge: Split the Madlib](#challenge-split-the-madlib)
- [The Standard Library](#the-standard-library)
- [Third-Party Packages and PyPI](#third-party-packages-and-pypi)
- [Virtual Environments with `venv`](#virtual-environments-with-venv)
- [Installing Packages with `pip`](#installing-packages-with-pip)
- [Dependencies and Sub-Dependencies](#dependencies-and-sub-dependencies)
- [`requirements.txt`](#requirementstxt)
  - [Keep `.venv` Out of Git](#keep-venv-out-of-git)
- [pytest: A Package You Already Use](#pytest-a-package-you-already-use)
- [The Commands, All Together](#the-commands-all-together)
- [Summary](#summary)

## Key Terms

- **Modularity** means building a program from small pieces that each do one job, so that each piece can be read, changed, and checked on its own.
  - A **helper function** does one piece of a bigger job. A **`main()` function** calls the helper functions in a logical order, so reading `main()` tells you what the program does.
- A **module** is a file containing code, which can then be imported and utilized in other parts of a larger program or system.
  - Every function and variable defined at the top level of a file can be imported by another file.
  - A module is imported with `import module_name`, or specific names are imported with `from module_name import name`.
- Importing a file **runs** it, top to bottom. The variable `__name__` tells a file whether it is being run directly (`"__main__"`) or imported by another file.
- The `if __name__ == "__main__":` guard is how a file says "only run this part when I am the program being run".
- The **standard library** is the collection of modules that come with Python. `random` and `math` are examples. They need `import` but no installation.
- A **package** is a folder of modules that someone has published so that other people can install it and import it. `pytest` is a package.
- A **library** is a collection of code written for other programs to use rather than to be run on its own. The standard library is Python's own library, and many packages, like `pytest`, are libraries too.
- Third-party packages are published on the **Python Package Index (PyPI)** and installed with **`pip`**, Python's package installer.
- A **virtual environment** is a folder that holds one project's private set of packages, together with a link to the Python installed on your computer. You create one with `python3 -m venv .venv` and turn it on with `source .venv/bin/activate`.
  - Installing a package inside an activated virtual environment installs it only there.
  - A package can have **sub-dependencies**, other packages it needs, and `pip` installs those too.
- **`requirements.txt`** is a file listing the packages a project needs. `pip freeze > requirements.txt` writes it; `pip install -r requirements.txt` reads it.
- A **`.gitignore`** file lists the files and folders in a project that Git should not track. The `.venv/` and `__pycache__/` folders go in it. The `.venv` folder is never committed; it is rebuilt from `requirements.txt` instead.
- **`pytest`** is the third-party package that runs the tests in your assignments. It finds files whose names start with `test_` and runs them with `python3 -m pytest`. It is a **developer dependency**: a package used by the developers of a project but not needed by the people who run it.

## Modularity

### One Long Block of Code

Consider the café program below. It is the ordering program from chapter 1.8, with one addition: it asks how many of each item the customer wants.

{% code title="cafe/main.py" overflow="wrap" lineNumbers="true" %}

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}
purchases = []

while True:
    item = input("Item (or done to finish): ").strip().lower()
    if item == "done":
        break
    if item not in menu:
        print(f"Sorry, {item} is not on the menu")
        continue

    while True:
        answer = input(f"How many {item}s? ").strip()
        try:
            quantity = int(answer)
            break
        except ValueError:
            print(f"Sorry, {answer} is not a whole number")

    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})

total = 0
print("Receipt")
print("-" * 20)
for purchase in purchases:
    cost = purchase["quantity"] * purchase["price"]
    print(f"{purchase['quantity']} {purchase['item']}: ${cost:.2f}")
    total += cost
print("-" * 20)
print(f"Total: ${total:.2f}")
```

{% endcode %}

The program works, but every job it does is tangled together in one block: asking for an item, checking it against the menu, parsing the quantity, recording the purchase, adding up the total, and printing the receipt.

Suppose the café asks for the total to include sales tax. The line that adds up the total, `total += cost`, sits inside the loop that prints the receipt, so the change has to be made in the middle of the printing code. And the only way to check that the new total is right is to run the whole program and type an order, every time you make a change.

**Modularity** solves this problem by building a program from small pieces that each do one job. The first tool for modularity is one you already have: functions.

### Helper Functions and a `main()` Function

Here is the same program, with each job moved into a function of its own. A function that does one piece of a bigger job is called a **helper function**:

{% code title="cafe/main.py" overflow="wrap" lineNumbers="true" %}

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}
purchases = []

def add_purchase(item, quantity):
    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})

def get_total():
    total = 0
    for purchase in purchases:
        total += purchase["quantity"] * purchase["price"]
    return total

def ask_for_item():
    while True:
        item = input("Item (or done to finish): ").strip().lower()
        if item == "done" or item in menu:
            return item
        print(f"Sorry, {item} is not on the menu")

def ask_for_quantity(item):
    while True:
        answer = input(f"How many {item}s? ").strip()
        try:
            return int(answer)
        except ValueError:
            print(f"Sorry, {answer} is not a whole number")

def print_receipt():
    print("Receipt")
    print("-" * 20)
    for purchase in purchases:
        cost = purchase["quantity"] * purchase["price"]
        print(f"{purchase['quantity']} {purchase['item']}: ${cost:.2f}")
    print("-" * 20)
    print(f"Total: ${get_total():.2f}")

# The main function just runs all of the other functions
def main():
    while True:
        item = ask_for_item()
        if item == "done":
            break
        quantity = ask_for_quantity(item)
        add_purchase(item, quantity)

    print_receipt()

main()
```

{% endcode %}

Each function's name says what its one job is. The `main` function does none of the jobs itself. It calls the other functions in a logical order, so reading `main()` tells you what the program does without the details of how each step is done.

The sales tax change now has one home: `get_total`. The tax can also be checked without typing an order, by calling `add_purchase("coffee", 2)` and then printing `get_total()`.

**<details><summary>Q: Which of these functions talk to the user, and which ones only work with the data?</summary>**

- `ask_for_item`, `ask_for_quantity`, and `print_receipt` talk to the user. They call `input()` or `print()`.
- `add_purchase` and `get_total` only work with `menu` and `purchases`. Neither one asks the user anything or prints anything.
- `main` does neither job itself. It combines the other functions and runs them in a logical order.

</details>

## Modules

This file is now organized, but it is still one file. Now imagine it with fifty menu functions, a dozen functions for talking to the user, and the code that ties them together. To fix a wrong total, you would scroll past all of the input code to find `get_total`. Two teammates fixing different things would be editing the same file at the same time. As a project grows, **separation of concerns** is what keeps it manageable.

{% hint style="info" %}
Separation of Concerns is a fundamental principle of software engineering. It emphasizes the importance of organizing our code into distinct functions and modules that each serve a singular and specific purpose. However, when put together, those individual pieces work in harmony.
{% endhint %}

To achieve separation of concerns, Python projects are typically separated into multiple files called **modules** that share code with each other.

A **module** is a file containing code, which can then be **imported** and utilized in other parts of a larger program or system.

### One Kind of Function per Module

The question above sorted the functions into two kinds, plus `main`. Each kind gets its own module:

- **`orders.py`** holds the data, `menu` and `purchases`, and the functions that work with it.
- **`interface.py`** holds the functions that talk to the user: the ones that clean, validate, and parse what the user types, and the one that prints the receipt.
- **`main.py`** is the entry point, the file you run. It combines the functions from the other two modules.

You will see the same split in the case study at the end of this module.

{% code title="cafe/orders.py" overflow="wrap" lineNumbers="true" %}

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}
purchases = []

def is_on_menu(item):
    return item in menu

def add_purchase(item, quantity):
    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})

def get_total():
    total = 0
    for purchase in purchases:
        total += purchase["quantity"] * purchase["price"]
    return total
```

{% endcode %}

{% code title="cafe/interface.py" overflow="wrap" lineNumbers="true" %}

```python
from orders import is_on_menu

def ask_for_item():
    while True:
        item = input("Item (or done to finish): ").strip().lower()
        if item == "done" or is_on_menu(item):
            return item
        print(f"Sorry, {item} is not on the menu")

def ask_for_quantity(item):
    while True:
        answer = input(f"How many {item}s? ").strip()
        try:
            return int(answer)
        except ValueError:
            print(f"Sorry, {answer} is not a whole number")

def print_receipt(purchases, total):
    print("Receipt")
    print("-" * 20)
    for purchase in purchases:
        cost = purchase["quantity"] * purchase["price"]
        print(f"{purchase['quantity']} {purchase['item']}: ${cost:.2f}")
    print("-" * 20)
    print(f"Total: ${total:.2f}")
```

{% endcode %}

Two functions changed on the way into their modules, and both changes keep `interface.py` away from the data:

- `ask_for_item` used to check `item in menu` itself. Now it calls `is_on_menu`, a new function in `orders.py`, so `interface.py` never touches `menu`. If the menu ever changes how it is stored, only `orders.py` has to change.
- `print_receipt` used to read `purchases` and call `get_total()` itself. Now it receives the purchases and the total as arguments, so it only prints what it is given.

### Every Top-Level Name Can Be Imported

Every name assigned at the top level of a file, meaning every function and every variable that is not indented inside something else, can be imported by another file. That means a function can leave `main.py` and `main.py` can still call it, by importing it back.

`menu`, `purchases`, `is_on_menu`, `add_purchase`, and `get_total` are all available to any file that imports `orders`. `interface.py` imports one of them, `is_on_menu`, on its first line.

### Importing with `import` and `from ... import`

To use a module's names, use the `import` statement. A module's name is its filename without the `.py`. When you run `python3 main.py`, Python looks for `orders.py` and `interface.py` in the same folder as `main.py`, so keep the three files side by side. Move `interface.py` into a different folder and `from interface import ask_for_item, ask_for_quantity, print_receipt` stops with `ModuleNotFoundError: No module named 'interface'`.

{% code title="cafe/main.py" overflow="wrap" lineNumbers="true" %}

```python
# Import the whole module. Its names are reached with dot notation.
import orders

# Import specific names from a module. They can then be used directly.
from interface import ask_for_item, ask_for_quantity, print_receipt

def main():
    while True:
        # ask_for_item was imported by name so we can just invoke it.
        item = ask_for_item()
        if item == "done":
            break
        quantity = ask_for_quantity(item)

        # add_purchase is INSIDE of the orders module so we use dot notation
        orders.add_purchase(item, quantity)

    print_receipt(orders.purchases, orders.get_total())

main()
```

{% endcode %}

**<details><summary>Q: How does this file structure demonstrate separation of concerns? What is the concern of each file?</summary>**

Each file is concerned with only one aspect of the functionality of the entire program.

- `orders.py` is concerned with the café's data: what is on the menu, what the customer bought, and what it all costs.
- `interface.py` is concerned with talking to the user: asking for an order and printing the receipt.
- `main.py` is concerned with combining the functions and executing them in a logical manner.

</details>

You can also give a module a shorter name as you import it with `as`:

```python
import orders as o

o.add_purchase("coffee", 2)
```

You will see this constantly in other people's code, where long library names get two-letter aliases.

There is also `from orders import *`, which imports every name in the module at once.

**<details><summary>Q: Why write `import orders` and then `orders.add_purchase(...)`, or list the names you want, when `from orders import *` would let you write `add_purchase(...)` with less typing?</summary>**

Two reasons, and the second is the important one.

First, readability. When a reader sees `orders.add_purchase(item, quantity)` in `main.py`, they know exactly which file to open to find out what `add_purchase` does. With `import *`, `add_purchase` appears from nowhere.

Second, safety. `import *` brings in _every_ top-level name in the module, including ones you did not know were there. Suppose someone adds a variable called `len` to `orders.py`. After `from orders import *`, the built-in `len` function in `main.py` is silently replaced by their variable, and every `len(...)` call in your file breaks. Importing by name means nothing arrives that you did not ask for.

</details>

## What Happens When You Import a File?

Here is something that surprises almost everyone. Importing a file **runs it**, top to bottom, the first time it is imported, almost exactly as if you had typed `python3 orders.py`. The one difference is a variable called `__name__`, which is coming up shortly.

{% hint style="warning" %}
**Predict, then run.** Add one line to the very bottom of `orders.py`:

```python
print("orders was loaded")
```

Then run `python3 main.py` (not `orders.py`) and type `done` at the first question. Write down everything you expect to see printed, in order.

<details><summary>What actually happens</summary>

```
orders was loaded
Item (or done to finish): done
Receipt
--------------------
--------------------
Total: $0.00
```

The message from `orders.py` prints _first_, before anything from `main.py`. When the interpreter reaches `import orders` on line 2 of `main.py`, it goes and runs all of `orders.py`. The assignments create `menu` and `purchases`, the `def` statements create the functions, and the `print` at the bottom prints. Only then does it return to `main.py` and continue.

`interface.py` imports from `orders` too, on its first line, but the message prints only once. Python runs a module the first time it is imported, and every later import reuses the module it already ran.

</details>
{% endhint %}

{% hint style="info" %}
**What is that `__pycache__` folder?** The first time you import a module, a folder called `__pycache__` appears next to it, holding a file like `orders.cpython-312.pyc`. That is a pre-processed copy of the module that Python saves so the next import is faster. It is rebuilt automatically whenever the module changes, you never edit it, and it never belongs in Git. The `.gitignore` section later in this lesson shows how to keep it out.
{% endhint %}

Running a file when it is imported is usually fine, because most of what is in a module is `def` statements, and a `def` statement only creates a function without running the code inside it. But what if a file is _both_ a program you sometimes run directly _and_ a module other files import? `main.py` ends with a call to `main()`. If another file imported `main.py` to reuse something from it, `main()` would run during the import, and the person using the other program would suddenly be asked `Item (or done to finish):`.

### `__name__`

Every module has a variable called `__name__` that Python sets for it automatically. Replace the `print` at the bottom of `orders.py` with this, and add the same line to `main.py`, just below its `import` lines:

```python
print(f"my __name__ is {__name__}")
```

Now run `python3 main.py`:

```
my __name__ is orders
my __name__ is __main__
Item (or done to finish):
```

When a file is imported, its `__name__` is its module name. When a file is the one you ran with `python3`, its `__name__` is the special string `"__main__"`. So a file can tell which situation it is in.

### The `if __name__ == "__main__":` Guard

That gives us the standard way to finish a Python program:

{% code title="cafe/main.py" overflow="wrap" lineNumbers="true" %}

```python
import orders
from interface import ask_for_item, ask_for_quantity, print_receipt

def main():
    while True:
        item = ask_for_item()
        if item == "done":
            break
        quantity = ask_for_quantity(item)
        orders.add_purchase(item, quantity)

    print_receipt(orders.purchases, orders.get_total())

if __name__ == "__main__":
    main()
```

{% endcode %}

Read it as: "if this file is the one being run, call `main()`." When `main.py` is run with `python3 main.py`, the condition is true and the program starts. If any other file ever does `import main`, the condition is false and nothing runs except the `def` statements.

You will see this guard at the bottom of nearly every Python program you read, and you should put it at the bottom of every one you write. The two underscores on each side of `name` and `main` are part of the spelling; Python uses that pattern for names it manages itself. `orders.py` and `interface.py` do not need the guard, because they are never the file you run.

### A Traceback Across Two Files

Once a program is split into modules, the traceback crosses files, and the `File` line changes as it goes. Suppose a teammate changes the check in `ask_for_item` to `if len(item) > 0:`, so that it accepts any answer that is not empty, and a customer orders a pizza:

```
Item (or done to finish): pizza
How many pizzas? 1
Traceback (most recent call last):
  File "/Users/ben/cafe/main.py", line 15, in <module>
    main()
  File "/Users/ben/cafe/main.py", line 10, in main
    orders.add_purchase(item, quantity)
  File "/Users/ben/cafe/orders.py", line 13, in add_purchase
    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})
                                                                   ~~~~^^^^^^
KeyError: 'pizza'
```

The rule does not change. Read from the bottom: the error is a `KeyError` on line 13 of `orders.py`, because `menu` has no `"pizza"` key. That function was called from line 10 of `main.py`, and that call came from line 15.

The bad value itself came from `ask_for_item` in `interface.py`, which had already returned by the time the error was raised, so `interface.py` does not appear in the traceback at all. The traceback still points the way: line 10 passed `item` to `add_purchase`, and line 6 of `main.py`, `item = ask_for_item()`, is where `item` got its value. That is the next place to look.

### Challenge: Split the Madlib

Here is a solution to the madlib challenge from chapter 1.5. The `madlib` function and the `main` function that asks the user for input share one file.

{% code title="madlib-challenge/main.py" overflow="wrap" lineNumbers="true" %}

```python
def madlib(name, verb, quantity, item, new_item, is_happy):
    name = name[0].upper() + name[1:].lower()

    if new_item[0].lower() in "aeiou":
        article = "an"
    else:
        article = "a"

    if quantity == "1":
        items = item
    else:
        items = item + "s"

    title = f"The Story of {name}"
    print(title)
    print("=" * len(title))

    print(f"There once was a man named {name}.")
    print(f"Every day he would {verb} with his {quantity} {items}")

    if is_happy:
        print(f"But then, he found {article} {new_item} and everything changed!")
    else:
        print(f"But then, {article} {new_item} took over his life and he couldn't {verb} again!")

    print("The end.")

def main():
    name = input('Choose a name: ').strip()
    verb = input('Choose a verb: ').strip()
    quantity = input('Choose a quantity: ').strip()
    item = input('Choose an item: ').strip()
    new_item = input('Choose a new item: ').strip()
    is_happy_response = input('Choose whether the story is happy. Y or N: ')
    is_happy = is_happy_response.strip().upper() == "Y"

    madlib(name, verb, quantity, item, new_item, is_happy)

main()
```

{% endcode %}

1. Re-organize the code such that the `madlib` function is in its own file called `madlib.py`, and `main.py` imports it.
2. Replace the `main()` call at the bottom of `main.py` with the `if __name__ == "__main__":` guard.

**<details><summary>Q: Solution</summary>**

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
from madlib import madlib

def main():
    name = input('Choose a name: ').strip()
    verb = input('Choose a verb: ').strip()
    quantity = input('Choose a quantity: ').strip()
    item = input('Choose an item: ').strip()
    new_item = input('Choose a new item: ').strip()
    is_happy_response = input('Choose whether the story is happy. Y or N: ')
    is_happy = is_happy_response.strip().upper() == "Y"

    madlib(name, verb, quantity, item, new_item, is_happy)

if __name__ == "__main__":
    main()
```

{% endcode %}

`madlib.py` holds the `madlib` function exactly as it was, with nothing else in the file.

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

These modules are imported exactly the same way as your own `orders.py`, and the interpreter finds them for you. Here is `math`:

```python
import math

print(math.pi)         # 3.141592653589793
print(math.ceil(4.2))  # 5
print(math.floor(4.8)) # 4
```

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
# /Users/you/cafe/.venv/bin/python3
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

The first time `pytest` tried to `import pluggy`, it would crash with `ModuleNotFoundError: No module named 'pluggy'`. A package is written by importing other packages, exactly the way your `main.py` imports `orders.py`, so every package it imports has to be installed too.

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

## pytest: A Package You Already Use

Every assignment in this program comes with a `tests/` folder and a `requirements.txt` that lists `pytest`. `pytest` is the third-party package that has been checking your work.

When you run `python3 -m pytest`, Python runs the `pytest` module from the active virtual environment. `pytest` then:

- finds every file in the project whose name starts with `test_`, such as `tests/test_debug.py`;
- runs every function in those files whose name starts with `test_`. Each one imports a function from your code, calls it with an input whose answer is already known, and checks that your function returned that answer;
- prints a `.` for every test that passed and an `F` for every test that failed, and then explains each failure.

`pytest` is a **developer dependency**. Only the files in `tests/` import it, and the files that make up the program never do, so someone who just wants to _run_ your program can do it without `pytest` installed. `pytest` serves the people building the program. Many projects keep a second file, `requirements-dev.txt`, for developer dependencies. For this module, one `requirements.txt` with everything in it is fine.

The lesson on test-driven development, later in this module, teaches you to write tests of your own.

{% hint style="warning" %}
**Predict, then run.** In an assignment folder with its environment activated, deactivate the environment with `deactivate`, then run `python3 -m pytest`. What happens?

<details><summary>What actually happens</summary>

```
/usr/local/bin/python3: No module named pytest
```

(The path at the front is wherever Python lives on your computer, so yours may differ.) `pytest` was installed into `.venv`, and with `.venv` turned off, `python3` is the copy of Python that came with your computer, which has never heard of it.

This is the error you will see most often for the rest of the year, and it almost always means one of two things: you forgot to activate the environment, or you forgot to install the package into it. Check the `(.venv)` at the front of your prompt first.

Activate the environment again with `source .venv/bin/activate` before moving on.

</details>
{% endhint %}

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

## Summary

A program is easier to read, change, and check when it is built from small pieces that each do one job. This idea, **modularity**, starts with helper functions and a `main()` function that calls them in a logical order, and it continues with **modules**: files that each hold one kind of function and share code by importing each other's top-level names. Importing a file runs it, so a file that is also a program puts its startup code under `if __name__ == "__main__":`. Code you didn't write arrives the same way. The **standard library** comes with Python. **Third-party packages**, such as `pytest`, are installed from PyPI with `pip` into a **virtual environment**, which keeps each project's packages separate, and `requirements.txt` records what to install again.
