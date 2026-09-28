# 6. Modules and `if __name__ == "__main__"`

In this lesson we'll learn how Python programs are split across multiple files, how those files share code with each other, and how a program gets input from the person running it.

**Table of Contents:**

- [Key Terms](#key-terms)
- [Modules](#modules)
  - [Every Top-Level Name Can Be Imported](#every-top-level-name-can-be-imported)
  - [Importing with `import` and `from ... import`](#importing-with-import-and-from--import)
- [What Happens When You Import a File?](#what-happens-when-you-import-a-file)
  - [`__name__`](#__name__)
  - [The `if __name__ == "__main__":` Guard](#the-if-__name__--__main__-guard)
- [Getting Input from the User with `input()`](#getting-input-from-the-user-with-input)
- [Madlib Challenge](#madlib-challenge)

## Key Terms

- A **module** is a file containing code, which can then be imported and utilized in other parts of a larger program or system.
  - Every function and variable defined at the top level of a file can be imported by another file.
  - A module is imported with `import module_name`, or specific names are imported with `from module_name import name`.
- Importing a file **runs** it, top to bottom. The variable `__name__` tells a file whether it is being run directly (`"__main__"`) or imported by another file.
- The `if __name__ == "__main__":` guard is how a file says "only run this part when I am the program being run".
- `input()` pauses the program, waits for the user to type a line, and returns what they typed as a **string**.

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

As a project grows in scale and complexity, **separation of concerns** becomes increasingly important.

{% hint style="info" %}
Separation of Concerns is a fundamental principle of software engineering. It emphasizes the importance of organizing our code into distinct functions and modules that each serve a singular and specific purpose. However, when put together, those individual pieces work in harmony.
{% endhint %}

To achieve separation of concerns, Python projects are typically separated into multiple files called **modules** that share code with each other.

A **module** is a file containing code, which can then be **imported** and utilized in other parts of a larger program or system.

### Every Top-Level Name Can Be Imported

Every name assigned at the top level of a file, meaning every function and every variable that is not indented inside something else, can be imported by another file.

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

To use a module's names, use the `import` statement. A module's name is its filename without the `.py`.

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

Here is something that surprises almost everyone. Importing a file **runs it**, top to bottom, exactly as if you had typed `python3 circle_helpers.py`.

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

The message from `circle_helpers.py` prints _first_, before anything from `main.py`. When the interpreter reaches `import circle_helpers` on line 1 of `main.py`, it goes and runs all of `circle_helpers.py`. The `def` statements create the functions, and the `print` at the bottom prints. Only then does it return to `main.py` and continue.

(That `31.400000000000002` is not a mistake in your code. Computers store decimal numbers in a way that is very slightly inexact, and sometimes the inexactness shows. You will learn how to round it away.)

</details>
{% endhint %}

{% hint style="info" %}
**What is that `__pycache__` folder?** The first time you import a module, a folder called `__pycache__` appears next to it, holding a file like `circle_helpers.cpython-314.pyc`. That is a pre-processed copy of the module that Python saves so the next import is faster. It is rebuilt automatically whenever the module changes, you never edit it, and it never belongs in Git. Chapter 7 shows how to keep it out.
{% endhint %}

This is usually fine, because most of what is in a module is `def` statements and defining a function is harmless. But it raises a question: what if a file is _both_ a program you sometimes run directly _and_ a module other files import? `main()` gets called at the bottom of `main.py`. If another file ever imported `main.py`, `main()` would run during the import, which is almost never what anyone wants.

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

## Getting Input from the User with `input()`

Suppose you wanted to add functionality that allows you to get command-line input from the user of your program via the terminal. The built-in `input()` function does this.

`input(prompt)` prints the `prompt`, waits for the user to type a line and press Enter, and returns what they typed:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
name = input("Hello there! What's your name? ")
print(f"hi {name}. My name is HAL")
```

{% endcode %}

We can now replace the hard-coded radius in our circle program and ask the user to provide one instead!

{% hint style="warning" %}
**Predict, then run.**

```python
radius = input("Choose a radius for your circle! ")
print(get_area(radius))
```

Type `5` when asked. What prints?

<details><summary>What actually happens</summary>

```
TypeError: can't multiply sequence by non-int of type 'float'
```

`input()` **always returns a string**, no matter what the user typed. The user typed `5`, but `radius` holds `"5"`, and `3.14 * "5" * "5"` makes no sense to Python.

The fix is the `int()` conversion function from chapter 4:

```python
radius = int(input("Choose a radius for your circle! "))
```

Every time you take input from a user and want a number, this conversion is your job. Nothing does it for you.

</details>
{% endhint %}

## Madlib Challenge

A program is considered **hard-coded** if the program code must be modified in order to produce a new result.

The `input()` function is really useful for creating programs that will produce new results depending on the user's input.

In a new `madlib-challenge` folder, create a `main.py` file with the following hard-coded program:

{% code title="madlib-challenge/main.py" overflow="wrap" lineNumbers="true" %}

```python
def madlib(name, verb, quantity, item, new_item, is_happy):
    print(f"There once was a man named {name}.")
    print(f"Every day he would {verb} with his {quantity} {item}s")

    if is_happy:
        print(f"But then, he found a {new_item} and everything changed!")
    else:
        print(f"But then, a {new_item} took over his life and he couldn't {verb} again!")

    print("The end.")

def main():
    name = 'Ben'
    verb = 'run'
    quantity = 50
    item = 'dog'
    new_item = 'new car'
    is_happy = False

    madlib(name, verb, quantity, item, new_item, is_happy)

if __name__ == "__main__":
    main()
```

{% endcode %}

Your goal is to do the following in the `madlib-challenge` folder:

1. Replace the hard-coded variables defined in the `main` function with values retrieved from the user via the `input()` function.
2. Re-organize the code such that the `madlib` function is in its own file called `madlib.py`, and `main.py` imports it.

If you get stuck, you can view the solution below:

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

Notice that `quantity` is left as a string. It only ever gets printed, so there is no reason to convert it.

</details>
