# 7. The Python Ecosystem: pip, venv, and requirements.txt

In this lesson we'll learn where Python code comes from when you didn't write it: the standard library that ships with Python, the packages other people publish, and the tools that keep each project's packages separate from every other project's.

**Table of Contents:**

- [Key Terms](#key-terms)
- [The Standard Library](#the-standard-library)
- [Third-Party Packages and PyPI](#third-party-packages-and-pypi)
- [Virtual Environments with `venv`](#virtual-environments-with-venv)
- [Installing Packages with `pip`](#installing-packages-with-pip)
- [Dependencies and Sub-Dependencies](#dependencies-and-sub-dependencies)
- [`requirements.txt`](#requirementstxt)
  - [Keep `.venv` Out of Git](#keep-venv-out-of-git)
- [Developer Dependencies](#developer-dependencies)
- [The Commands, All Together](#the-commands-all-together)

## Key Terms

- The **standard library** is the collection of modules that come with Python. `random`, `math`, `time`, and `json` are examples. They need `import` but no installation.
- Third-party packages are published on the **Python Package Index (PyPI)** and installed with **`pip`**, Python's package installer.
- A **virtual environment** is a private copy of Python and its packages for one project. You create one with `python3 -m venv .venv` and turn it on with `source .venv/bin/activate`.
  - Installing a package inside an activated virtual environment installs it only there.
  - A package can have **sub-dependencies**, other packages it needs, and `pip` installs those too.
- **`requirements.txt`** is a file listing the packages a project needs. `pip freeze > requirements.txt` writes it; `pip install -r requirements.txt` reads it.
- The `.venv` folder is never committed to Git. It goes in `.gitignore` and is rebuilt from `requirements.txt` instead.
- **Developer dependencies** like `pytest` are packages used by the developer(s) of a project but not needed by the people who run it.

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

Remember `LAZY_PI = 3.14` from the last chapter? `math.pi` is the version that isn't lazy.

One more you will want soon is `json`, which turns lists and dictionaries into text that can be saved in a file, and back again:

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

`open()` is a built-in that opens a file, and the `with` statement closes it again when the indented block ends. This is how the task manager case study can be extended to remember its tasks between runs.

Nobody memorizes the standard library. The habit to build is to ask "does Python already have this?" before writing it yourself, and to check the [standard library documentation](https://docs.python.org/3/library/index.html) when you suspect it does.

## Third-Party Packages and PyPI

Suppose you wanted to print text to the Terminal in color, with bold and italics and a table with borders. Do you have the tools to implement that feature on your own?

While you could figure this out, there is no need to reinvent the wheel! Instead, just download an existing package from the **Python Package Index (PyPI)**.

Visit https://pypi.org/ to explore available packages. Start by searching for the "rich" package. Its page shows a description, usage examples, and the command to install it.

But before installing anything, we need somewhere to put it.

## Virtual Environments with `venv`

Every Python project you build will need its own set of packages, often in different versions. If every project installed its packages into the one Python on your computer, they would collide: project A needs version 2 of something, project B needs version 3, and one of them stops working.

A **virtual environment** solves this. It is a folder inside your project that holds a private copy of the interpreter and its own packages. Whatever you install while it is turned on goes there and nowhere else.

Create one in your project folder with the `venv` module, which is part of the standard library:

```sh
python3 -m venv .venv
```

`python3 -m venv` means "run the `venv` module as a program". The `.venv` at the end is the name of the folder to create. It starts with a dot so that it is hidden from `ls` and does not clutter your view of the project. The name `.venv` is a convention that editors like VS Code recognize.

Then turn it on. This is called **activating** the environment:

```sh
source .venv/bin/activate
```

Your Terminal prompt changes to show `(.venv)` at the front. That is how you know it is on. If you ever get a `ModuleNotFoundError` for a package you are sure you installed, look at the prompt before you do anything else. Nine times out of ten, `(.venv)` is missing. From now on, in this Terminal window, `python3` and `pip` refer to the copies inside `.venv`:

```sh
which python3
# /Users/you/mod-1/6-ecosystem/.venv/bin/python3
```

To turn it off, type `deactivate`. You will need to activate it again in every new Terminal window you open for this project.

{% hint style="info" %}
On Windows under WSL, these are the same commands. You are running Ubuntu, and Ubuntu is what these instructions were written for.

If VS Code asks you to select a Python interpreter, choose the one inside `.venv`.
{% endhint %}

## Installing Packages with `pip`

With the environment activated, install a package with `pip install`:

```sh
pip install rich
```

`pip` downloads the package from PyPI and prints what it did (version numbers may vary):

```
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-4.2.0 mdurl-0.1.2 pygments-2.21.0 rich-15.0.0
```

You may also see a `[notice]` that a newer version of `pip` is available. That is a suggestion, not an error, and you can ignore it.

`pip list` shows everything installed in the active environment:

```
Package        Version
-------------- -------
markdown-it-py 4.2.0
mdurl          0.1.2
pip            24.0
Pygments       2.21.0
rich           15.0.0
```

Now the package can be imported like any module:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
from rich.console import Console

console = Console()
console.print("Hello, [bold magenta]World[/bold magenta]!")
console.print("[green]This text is green[/green] and [red]this is red[/red]")
```

{% endcode %}

`rich.console` is a module inside the `rich` package (a package is a folder of modules), and `Console` is a name inside it. Run the file and you should see colored text.

{% hint style="warning" %}
**Predict, then run.** Deactivate the environment with `deactivate`, then run the same file again with `python3 main.py`. What happens?

<details><summary>What actually happens</summary>

```
ModuleNotFoundError: No module named 'rich'
```

`rich` was installed into `.venv`, and with `.venv` turned off, `python3` is the copy of Python that came with your computer, which has never heard of it.

This is the error you will see most often for the rest of the year, and it almost always means one of two things: you forgot to activate the environment, or you forgot to install the package into it. Check the `(.venv)` at the front of your prompt first.

</details>
{% endhint %}

## Dependencies and Sub-Dependencies

When you install a package for your project, it is called a **dependency**: your project depends on it.

Notice that `pip install rich` installed four packages, not one. `rich` itself needs `markdown-it-py` and `pygments` to work, so `pip` installed those as well. They are **sub-dependencies**. You can see what a package requires with `pip show`:

```sh
pip show rich
```

```
Name: rich
Version: 15.0.0
Key Terms: Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
...
Requires: markdown-it-py, pygments
```

**<details><summary>Q: `rich` requires `markdown-it-py` and `pygments`. Where did `mdurl` come from?</summary>**

Run `pip show markdown-it-py` and look at its `Requires:` line. `markdown-it-py` needs `mdurl`. Dependencies have dependencies, and `pip` follows the whole chain.

</details>

## `requirements.txt`

The `.venv` folder can be big, it contains a copy of Python, and it is specific to your computer. So it is **never** committed to Git. Instead, you commit a small text file that says what to install, and anyone (including future you, on a new laptop) rebuilds the environment from it.

That file is `requirements.txt`, and `pip` writes it for you:

```sh
pip freeze > requirements.txt
```

`pip freeze` prints every installed package with its exact version, and `>` sends that output into the file instead of the screen (you met `>>` in Mod 0; `>` is the same idea but replaces the file rather than adding to it). Open it up:

```
markdown-it-py==4.2.0
mdurl==0.1.2
Pygments==2.21.0
rich==15.0.0
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

Git will then pretend those folders do not exist. The second line covers the `__pycache__` folders you met in chapter 6, which Python rebuilds on its own and which never belong in Git.

**<details><summary>Q: Why not just commit `.venv` so that nobody has to run `pip install`?</summary>**

Three reasons. It is large, often hundreds of megabytes, and Git is built for text files, not for copies of programs. It contains paths and a copy of Python specific to your machine and operating system, so it would not work on a teammate's computer anyway. And it is completely reproducible from `requirements.txt` in a few seconds, so there is nothing to gain.

The general rule: commit the recipe, not the meal.

</details>

## Developer Dependencies

Some packages are used by the developer(s) who are building a project but aren't needed by the people who run it. These are called **developer dependencies**.

The one you will meet soonest is `pytest`, a package for running automated tests, which we'll use at the end of this module:

```sh
pip install pytest
```

**<details><summary>Q: Why is `pytest` a developer dependency and not a required dependency of the project?</summary>**

`pytest` makes it easier to check that your code works, but the functionality of the program is not changed by it. Someone who just wants to _run_ your program never needs it. It is a convenience for developers.

</details>

Many projects keep a second file, `requirements-dev.txt`, for developer dependencies. For this module, one `requirements.txt` with everything in it is fine.

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
```
