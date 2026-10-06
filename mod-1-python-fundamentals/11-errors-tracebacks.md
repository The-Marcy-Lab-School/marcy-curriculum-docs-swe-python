# 1.11 Errors and Tracebacks

Writing code with errors is a natural part of programming. But rather than avoiding them at all costs, we should learn to understand them! Errors provide us valuable information about how we can improve our programs.

**Table of Contents:**

- [Key Terms](#key-terms)
- [What is an error? Why are they "raised"?](#what-is-an-error-why-are-they-raised)
- [What causes an error? Syntax and Runtime Errors](#what-causes-an-error-syntax-and-runtime-errors)
- [Types of Errors](#types-of-errors)
  - [Syntax Errors:](#syntax-errors)
    - [`SyntaxError`:](#syntaxerror)
    - [`IndentationError`:](#indentationerror)
  - [Runtime Errors:](#runtime-errors)
    - [`NameError`](#nameerror)
    - [`TypeError`](#typeerror)
    - [`ValueError`](#valueerror)
    - [`IndexError` and `KeyError`](#indexerror-and-keyerror)
    - [`AttributeError`](#attributeerror)
    - [`ZeroDivisionError`](#zerodivisionerror)
    - [`FileNotFoundError` and the `OSError` family](#filenotfounderror-and-the-oserror-family)
    - [`AssertionError`](#assertionerror)
- [How to Read a Traceback](#how-to-read-a-traceback)
  - [A Traceback Across Two Files](#a-traceback-across-two-files)
- [Handling Errors](#handling-errors)
  - [The Error You Will Catch Most: `ValueError` from `input()`](#the-error-you-will-catch-most-valueerror-from-input)
- [Raising Your Own Errors](#raising-your-own-errors)
  - [Testing That a Function Raises](#testing-that-a-function-raises)

## Key Terms

- **Errors** are code that prevents a program from running successfully and are "raised" when something goes wrong, providing valuable debugging information.
- **Syntax errors** occur when code is invalid and can't be executed (e.g., missing quotes, wrong indentation), while **runtime errors** occur when code executes but encounters faulty logic or improper data type usage. Python calls runtime errors **exceptions**.
- Common error types include **`SyntaxError`** (invalid Python), **`NameError`** (undefined variables), **`TypeError`** (wrong data types), **`ValueError`** (right type, wrong value), **`IndexError`** and **`KeyError`** (missing positions and keys), and **`FileNotFoundError`** (operating system constraints).
- A **traceback** is the report Python prints when an error is raised. Reading it from the bottom up tells you the error type, the message, and the chain of function calls that led there.
- Errors can be manually raised using the `raise` keyword, and uncaught errors will cause programs to crash. `try` and `except` let a program catch an error and decide what to do instead.
- **`pytest.raises(ErrorType)`** is how a test checks that a function raises the error it should.

## What is an error? Why are they "raised"?

- An error is any code that prevents a program from running successfully.
- In the world of programming, we say that **"an error is raised"**. You will also hear "thrown", which means the same thing.
- An error that is not handled is considered **"uncaught"** until we fix it (or catch it). Uncaught errors will cause the program to crash.

```python
message = 'hello world'
message.append('!!!')
# AttributeError: 'str' object has no attribute 'append'
```

You can manually raise an error in Python like this:

```python
raise ValueError('an error occurred')
```

## What causes an error? Syntax and Runtime Errors

There are many causes of errors but in general there are two categories:

- **Syntax Errors:** The code you've written is invalid and can't be executed
  - e.g. you're missing a closing `"` or you've forgotten to indent

  ```python
  print("foo)

  #     print("foo)
  #           ^
  # SyntaxError: unterminated string literal (detected at line 1)
  ```

- **Runtime Errors:** The code you've written can be executed but an error has occurred as a result of faulty logic or improper use of data types. Python calls these **exceptions**.
  - e.g. you've attempted to invoke the `.append` method on a variable holding a string which doesn't have that method

  ```python
  "hello".append('hi')
  # AttributeError: 'str' object has no attribute 'append'
  ```

{% hint style="warning" %}
**Predict, then run.** This file has a syntax error on line 3 and a perfectly good `print` on line 1. What prints?

```python
print("this line is fine")

print("this one is not)
```

<details><summary>What actually happens</summary>

Nothing prints except the error. Not even `this line is fine`.

You saw this in Mod 0 and it is worth seeing again now that you know the name for it. Python reads and checks the _whole file_ before it runs any of it. A syntax error means the file is rejected before line 1 ever executes. A runtime error, by contrast, only happens when the program reaches the broken line, so everything before it runs first. That difference is the fastest way to tell which kind of error you are looking at.

</details>
{% endhint %}

## Types of Errors

### Syntax Errors:

#### `SyntaxError`:

_Very common_. Indicates that a program is not valid Python. The interpreter finds these while reading the file, before running anything. These errors are almost always indicative of a broken program.

```python
print("hello);
# SyntaxError: unterminated string literal (detected at line 1)
```

#### `IndentationError`:

_Very common when you are new._ A kind of `SyntaxError` specific to Python: a line is indented where it should not be, or not indented where it must be.

```python
def can_vote(age):
if age >= 18:
    return True
# IndentationError: expected an indented block after function definition on line 1
```

### Runtime Errors:

#### `NameError`

_Very common_. Indicates that an attempt is being made to access a variable that is not defined. Such errors commonly indicate typos in code, a variable used before the line that assigns it, or a variable used outside its scope.

```python
does_not_exist
# NameError: name 'does_not_exist' is not defined
```

#### `TypeError`

_Very common_. Indicates that an operation or function was given a value of a type it cannot handle. For example, adding a string to a number, calling a function with the wrong number of arguments, or calling something that is not a function.

```python
"1" + 1
# TypeError: can only concatenate str (not "int") to str

print_sum()
# TypeError: print_sum() missing 2 required positional arguments: 'x' and 'y'
```

#### `ValueError`

_Very common, especially with user input._ The type is right, but the value is not acceptable. The classic case is converting a string that does not look like a number.

```python
int("hello")
# ValueError: invalid literal for int() with base 10: 'hello'
```

#### `IndexError` and `KeyError`

_Very common._ You asked a list for a position it does not have, or a dictionary for a key it does not have.

```python
[1, 2, 3][5]
# IndexError: list index out of range

{"a": 1}["b"]
# KeyError: 'b'
```

#### `AttributeError`

_Common._ You used dot notation to ask a value for a method or attribute it does not have. Very often this means the value is not the type you thought it was.

```python
"hello".append('hi')
# AttributeError: 'str' object has no attribute 'append'
```

#### `ZeroDivisionError`

_Common._ Exactly what it says. It usually means a count somewhere was zero when you assumed it would not be.

```python
total / 0
# ZeroDivisionError: division by zero
```

#### `FileNotFoundError` and the `OSError` family

_Common once your programs touch files._ Python raises these when an application violates an operating system constraint. For example, this error will occur if an application attempts to read a file that does not exist.

```python
open("nope.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'nope.txt'
```

**<details><summary>This is a list of operating-system errors commonly encountered when writing a Python program.</summary>**

They are all kinds of `OSError`. For a comprehensive list, see the [built-in exceptions documentation](https://docs.python.org/3/library/exceptions.html#os-exceptions).

- `FileNotFoundError` (No such file or directory): the path you gave does not exist.
- `PermissionError` (Permission denied): an attempt was made to access a file in a way forbidden by its file access permissions.
- `ConnectionRefusedError` (Connection refused): no connection could be made because the target machine actively refused it. This usually results from trying to connect to a service that is not running. You will meet this one in Mod 5.

</details>

#### `AssertionError`

_Less common in programs, very common in tests._ Indicates the failure of an `assert` statement. In chapter 1.9, every `pytest` test that failed at an `assert` line failed with one of these.

```python
assert 1 == 2, "one is not two"
# AssertionError: one is not two
```

## How to Read a Traceback

Errors provide us valuable information about how we can improve our programs so let's learn how to read error messages! Python's error report is called a **traceback**.

Consider the code below which will raise an error.

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
def cause_trouble(items):
    items.append('!!!')

def play_nice():
    print('yipeeee')

def main():
    cause_trouble('hello world')
    play_nice()

main()

# Order of Operations:
# 1. Run the main function on line 11
# 2. Run cause_trouble on line 8
# 3. Run the code inside cause_trouble which will raise the AttributeError on line 2
# 4. When cause_trouble raises the error, the program will crash and play_nice will not be executed
#
# The following traceback will be printed to the console:
#
# Traceback (most recent call last):
#   File "/Users/ben/mod-1/main.py", line 11, in <module>
#     main()
#   File "/Users/ben/mod-1/main.py", line 8, in main
#     cause_trouble('hello world')
#   File "/Users/ben/mod-1/main.py", line 2, in cause_trouble
#     items.append('!!!')
#     ^^^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'append'
```

{% endcode %}

The first line says it: `most recent call last`. A traceback is printed in the order the calls happened, so the place where the error actually occurred is at the **bottom**. Read it from the bottom up:

- The **error type** (`SyntaxError`, `NameError`, `TypeError`, etc…) is the last line
  - In this case, we have an `AttributeError`
- The **error message** describing the problem is on that same line.
  - `'str' object has no attribute 'append'`
- The **call stack** is everything above it.
  - we see the file names, line numbers, and function names tracing how we got to the error, with the most recently called function at the bottom.
    - `items.append('!!!')` in `cause_trouble` on line `2` was reached because…
    - `cause_trouble('hello world')` in `main` on line `8` was called, which happened because…
    - `main()` on line `11` in `<module>` (which means the top level of the file, outside any function) was executed by the interpreter
  - The `^^^^` carets under `items.append` point at the exact part of the line that failed.

### A Traceback Across Two Files

Once a program is split into modules, the traceback crosses files, and the `File` line changes as it goes. Here `cause_trouble` lives in `helpers.py` and `main.py` imports it:

```
Traceback (most recent call last):
  File "/Users/ben/unit-1/main.py", line 10, in <module>
    main()
  File "/Users/ben/unit-1/main.py", line 7, in main
    cause_trouble('hello world')
  File "/Users/ben/unit-1/helpers.py", line 2, in cause_trouble
    items.append('!!!')
    ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'append'
```

The rule does not change. Read from the bottom: the error is on line 2 of `helpers.py`, that function was called from line 7 of `main.py`, and that call came from line 10. Where the error _occurred_ and where the bad value _came from_ are now in different files, and both lines are in front of you.

{% hint style="info" %}
The **call stack** is a data structure that the interpreter uses to keep track of the functions that are called while the program is running. It saves function calls in a last-in-first-out (LIFO) order which means that the most recent function call is always on top, followed by the function that called it, and so on. A traceback is a printout of the call stack at the moment the error was raised, printed with the most recent call last. So the top of the stack, the call that was running when the error happened, appears at the bottom of the traceback.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Before running this, say which line number the traceback will name at the bottom, and which error type.

```python
def average(scores):
    return sum(scores) / len(scores)

def main():
    print(average([90, 80]))
    print(average([]))

main()
```

<details><summary>What actually happens</summary>

`85.0` prints first, because the first call works. Then the traceback names line 2, `ZeroDivisionError: division by zero`. `len([])` is `0`.

If you said line 6, you pointed at the call that _caused_ the problem rather than the line where the error _occurred_. Both appear in the traceback. The bottom one is where Python was standing when it gave up, and it is usually where the fix goes, or where you learn that the caller sent something the function never expected.

</details>
{% endhint %}

## Handling Errors

- Uncaught errors will crash the program. For most errors, we can just edit our program and fix them.
- Some errors we can't fix though. For example, if our program requests data from another program via the internet but the internet is down, then there is nothing we can do (other than fix the internet). What we _can_ do is prevent our program from crashing in these cases.
- We can plan ahead and add code to our program that **"catches a raised error"** using `try` and `except` blocks. This prevents the program from crashing and allows us to decide what to do next.

```python
def cause_trouble(items):
    try:
        # attempt to run the code that might raise an error
        items.append('!!!')
    except AttributeError as err:
        # Handle the error here.
        print(f"Oops! {err}")
        print('not to worry. carry on...')

def play_nice():
    print('yipeeee')

def main():
    cause_trouble('hello world')
    play_nice()

main()

# Prints to the console:
#
# Oops! 'str' object has no attribute 'append'
# not to worry. carry on...
# yipeeee
```

Explanation:

- The `try:` code block attempts to do something that we suspect might raise an error. In this case, it attempts to use the `.append` method on the given `items` value (which it assumes is a list). Since `cause_trouble` was invoked with a string `'hello world'` and NOT a list, an `AttributeError` will be raised.
- The `except AttributeError as err:` code block is executed if an `AttributeError` is raised and is given the error object which we can reference with the parameter-like variable `err`. Printing `err` shows the error message before continuing on.
- Since the error in `cause_trouble` was caught, the program doesn't crash and `play_nice` can be executed.

Naming the error type after `except` matters. It means "catch _this_ kind of error and let every other kind crash as usual." A bare `except:` with no type catches everything, including mistakes you would rather know about, so name the type.

### The Error You Will Catch Most: `ValueError` from `input()`

Every program in this module that asks the user for a number has the same weak spot, and you found it in the last chapter: `int("twenty")` crashes. Now you can do something about it.

```python
def ask_for_number(prompt):
    while True:
        answer = input(prompt)
        try:
            return int(answer)
        except ValueError:
            print(f"Sorry, {answer} is not a whole number. Try again.")

people = ask_for_number("How many people? ")
```

The `return` inside the `try` ends the loop and the function the moment the conversion succeeds. If it fails, the `except` prints a message and the `while True` asks again. This function will appear, in some form, in your project.

**<details><summary>Q: Chapter 1.6 checked input with `.isdigit()` instead. Why might `try`/`except` be the better tool here?</summary>**

`.isdigit()` only accepts strings made entirely of digits, so it rejects `-5` and `" 5"` (a 5 with a space in front) even though `int()` would happily convert both. The `try`/`except` version lets `int()` be the judge of what it can convert, which is exactly the right judge. Use `.isdigit()` when you specifically want strings made only of digits, with no minus sign or spaces; use `try`/`except` when you want "whatever `int()` accepts."

</details>

## Raising Your Own Errors

Sometimes your code is the one that discovers the problem. A function that is handed a value it cannot work with should say so loudly rather than carry on and produce nonsense:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Cannot withdraw {amount} from a balance of {balance}")
    return balance - amount
```

The caller can then choose to catch it or let it crash. Either way, the failure happens where the mistake is, with a message that says what went wrong, instead of three functions later with a confusing one. Pick the built-in error type whose meaning is closest: `ValueError` for a bad value, `TypeError` for a bad type.

### Testing That a Function Raises

An error that a function raises on purpose is part of what the function does, so it deserves a test like any other behavior. In the `9-testing` project from chapter 1.9, put `withdraw` in `src/bank.py` and write `tests/test_bank.py`:

```python
import pytest
from src.bank import withdraw


def test_withdraw():
    """withdraw - subtracts the amount from the balance"""
    assert withdraw(100, 30) == 70


def test_withdraw_overdraft():
    """withdraw - raises a ValueError when the amount is more than the balance"""
    with pytest.raises(ValueError):
        withdraw(100, 500)
```

`with pytest.raises(ValueError):` means "the indented code below must raise a `ValueError`." If it does, pytest catches the error and the test passes. If it does not, the test fails. It is the same `with` statement that opened files in chapter 1.9: it sets something up, runs the indented block, and then checks what happened.

{% hint style="warning" %}
**Predict, then run.** Delete the whole `if` statement from `withdraw` (both the `if` line and the `raise` line beneath it) so that it quietly allows the overdraft, and run the tests again. What does pytest report?

<details><summary>What actually happens</summary>

```
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE ValueError
```

pytest reports `1 failed, 1 passed`. `test_withdraw` still passes, because `withdraw(100, 30)` never reached the `raise` anyway: 30 is not more than 100. `test_withdraw_overdraft` fails, because `withdraw(100, 500)` now returns `-400` instead of raising a `ValueError`. The function no longer does what the test says it should, and pytest tells you exactly which promise it broke. Put the `if` statement back before moving on.

</details>
{% endhint %}
