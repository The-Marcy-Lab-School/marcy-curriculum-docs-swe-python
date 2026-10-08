# 1.1 Intro to Programming

There are so many terms and concepts to learn about programming. In this lesson, we will learn the fundamental vocabulary and concepts that are shared by practically every programming language. You may see code with syntax that you don't understand and that is fine, you will dig deeper into that code's syntax in later lessons. For now, just focus on learning the vocabulary in the **Key Terms** section.

**Table of Contents**

- [Setup](#setup)
- [Key Terms](#key-terms)
- [What is a program?](#what-is-a-program)
- [Running a file with the Python interpreter](#running-a-file-with-the-python-interpreter)
- [Printing to the Terminal with `print()`](#printing-to-the-terminal-with-print)
  - [Printing Values Inside Text with f-strings](#printing-values-inside-text-with-f-strings)
  - [Debunking The `print()` Myth](#debunking-the-print-myth)
- [Control Flow](#control-flow)
- [Code Style and Readability](#code-style-and-readability)

## Setup

- In your `mod-1` folder, create a new folder called `1-intro-to-programming`
- `cd 1-intro-to-programming`
- `touch main.py`
- Open the `main.py` file

## Key Terms

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

## What is a program?

A program is a text file with instructions that a computer executes to accomplish some task. It will be made up of comments, expressions, and statements:

**Comments** are ignored and help to explain the code.

```python
# this is a comment
```

{% hint style="info" %}
💡 You can quickly turn any line into a comment by highlighting the line (or any range of lines) and pressing <kbd>Command+/</kbd> (Mac) or <kbd>Control+/</kbd>
{% endhint %}

**Expressions** are any piece of code that evaluates to a single value, such as an operation (`5 + 5`) or a function call (`len("hi")`). A value on its own, such as the string `"hello world"`, is also an expression, because a value evaluates to itself.

```python
5 + 5       # Evaluates to 10
len("hi")   # Evaluates to 2
"hello"     # Evaluates to "hello"
5           # Evaluates to 5
```

Python evaluates an expression on a line by itself, like `5 + 5`, and then throws the value away, so the program is no different afterward. To keep a value or act on it, you use the expression inside a statement, for example by storing the value in a variable.

**Statements** are instructions that perform an action. They change the program in some way, often using expressions. For example, variable assignments alter the program's **state** (the data stored by a program at a point in time) and `if`/`else` statements change the control flow of the program:

{% code title="main.py" lineNumbers="true" %}

```python
# assigning a variable stores a value in the program's memory to be used later
instructor = "ben"
mood = None

# if statements change the control flow of a program (which line of code is executed next)
if instructor == "ben":
    mood = "happy"
else:
    mood = "sad"

print(mood)
```

{% endcode %}

**<details><summary>Q: In the statements above, what expressions can you see?</summary>**

- Every value is an expression: `"ben"` and `None` on lines 2 and 3, and `"happy"` and `"sad"` inside the `if`/`else`.
- Every variable name that the program reads is an expression too, like `mood` in `print(mood)`.
- The biggest expression is the condition `instructor == "ben"`, which combines the `instructor` and `"ben"` expressions with the `==` operator.
- `instructor` holds `"ben"`, so asking whether the two values are equal evaluates to `True`.

</details>

## Running a file with the Python interpreter

When we want to run the code in a file, we use a piece of software called the **Python interpreter**.

> The Python interpreter is a program that reads a `.py` file and executes it, one statement at a time.

The interpreter is installed on your computers and can be activated in the Terminal using the `python3 [filename]` command:

```sh
# main.py is the name of the file we want to run
python3 main.py
```

**Question:** Run `python3 main.py`. Only one word, `happy`, appears in the Terminal, even though the file contains several statements. Why?

**<details><summary>Answer</summary>**

Only the `print()` function sends anything to the Terminal. The other statements still ran, but they changed the program's state: they stored values in `instructor` and `mood`, and the `if`/`else` chose which of the two assignments to run. The state of a program stays hidden unless you print it.

</details>

## Printing to the Terminal with `print()`

`print()` is a built-in function that prints text to "standard output", which is a more formal way of describing the Terminal.

```python
print("hello world!")
```

The `print()` function is used primarily to verify the output of a program for debugging purposes. For example, this code converts 212° Fahrenheit to Celsius which should produce the result 100°C. Do you expect it to work?

```python
fahrenheit = 212
celsius = fahrenheit - 32 * 5 / 9
```

With `print(celsius)` we can verify whether or not we performed the calculation properly.

**<details><summary>Q: So, does it work?</summary>**

No. The formula says to subtract 32 first and then multiply by 5/9, but Python does multiplication and division before subtraction. So Python computed `32 * 5 / 9` first and subtracted that result from 212, and `print(celsius)` shows `194.22222222222223` instead of `100.0`.

Parentheses are always evaluated first, so `(fahrenheit - 32) * 5 / 9` makes the subtraction happen first.

Notice that Python never complained. A wrong formula is still valid code, so the program runs happily and stores the wrong number. The only way you'd find out is by looking at the value, and that is exactly what `print()` is for.

</details>

`print()` can also take several values at once, separated by commas. By default, `print()` puts a space between the values and starts a new line after the last one. Writing `sep=` inside the parentheses changes what goes between the values, and writing `end=` changes what goes after the last value:

```python
x = 10

print("start")
print("the value of x is", x)
print("a", "b", "c", sep="-")
print("no new line after this one", end="")
print(" <- see?")
```

```
start
the value of x is 10
a-b-c
no new line after this one <- see?
```

### Printing Values Inside Text with f-strings

Most of the time you want to print a value with some words around it, not on its own. Put an `f` in front of the opening quote, and Python fills in any expression you write inside curly braces `{}`:

```python
fahrenheit = 212
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is {celsius}°C")
# Output: 212°F is 100.0°C
```

This is called an **f-string**. Without the `f`, the braces are just characters and print exactly as written. You will use f-strings in nearly every program from here on, so get used to reading them now. Chapter 1.6 covers strings and f-strings in full.

### Debunking The `print()` Myth

{% hint style="danger" %}
Myth: "If our program doesn't print anything to the screen, then it isn't working or it isn't doing anything!"
{% endhint %}

It is common to think that without `print()`, the program isn't doing anything. This is not the case!

This program below runs a loop one hundred million times! Run it and watch the Terminal:

```python
x = 0

# A loop with 100 million iterations will take a few seconds to run! Increase that number to a billion and it could take a minute or more.
for i in range(100_000_000):
    x += 1
```

You won't see any output, but the prompt takes a few seconds to come back. A program that did nothing would finish instantly, so those seconds are your computer adding 1 to `x`, one hundred million times. Your computer IS executing the instructions you give it, but you just can't see the results because there is no `print()` statement. You can prove it by asking the Terminal to time the program for you:

```sh
time python3 main.py
```

```
python3 main.py  3.82s user 0.02s system 99% cpu 3.840 total
```

Nothing was printed, but the Terminal reports that the program ran for almost four seconds, and every one of those seconds went to the loop. (Your numbers will differ.)

## Control Flow

Computers can only execute one statement at a time and **Control Flow** refers to the order in which a program's statements are executed.

The default control flow is top to bottom, with statement being executed in order.

```python
print("1")
print("2")
print("3")
```

Most programming languages have tools like `if` statements, functions, and loops that let the programmer alter the program's control flow. For example, `if` statements can cause certain statements to be skipped.

Below, `instructor` holds `"ben"`, so `instructor == "ben"` is `True`. The interpreter runs the indented line under `if` and skips the line under `else`.

```python
instructor = "ben"
mood = None

# if statements change the "control flow" of a program (which line of code comes next)
if instructor == "ben":
    mood = "happy"  # this line of code is executed next
else:
    mood = "sad"  # this is skipped
```

A `for` loop can cause a statement (or multiple) to be executed more than once

```py
# A loop with 100 million iterations will take a few seconds to run! Increase that number to a billion and it could take a minute or more.
x = 0
for i in range(100_000_000):
    x += 1
```

We'll dive deeper into `if` statements and `for` loops later on but for now, the important things to remember about control flow are:

- Only one statement is executed at a time
- You can alter the program's control flow with special statements like `if` statements and loops

## Code Style and Readability

**Readability** is how easy it is for another engineer to read and understand your code (including future you).

Indentation is how the interpreter knows which lines belong to which block. A block is the group of lines that sit under a line ending in a colon `:`, like the body of a function or of an `if` statement. Whenever a line ends with a colon `:`, the lines that belong to it must be indented underneath it. The convention, written down in PEP 8, is four spaces per level.

```python
def can_vote(age):
    if age >= 18:
        return True
    else:
        return False
```

{% hint style="warning" %}
**Predict, then run.** Delete the indentation from the second line so the file looks like this, then predict what `python3 main.py` does.

```python
def can_vote(age):
if age >= 18:
    return True
```

<details><summary>What actually happens</summary>

```
  File "main.py", line 2
    if age >= 18:
    ^
IndentationError: expected an indented block after function definition on line 1
```

- Line 1 ends with a colon, so the interpreter expects the next line to be indented as the body of `can_vote`.
- Line 2 isn't indented, so `can_vote` has no body at all.
- Before running anything, the interpreter reads the whole file to check that its structure makes sense. Because the structure is broken, the interpreter stops right there and runs nothing, not even the lines above the mistake. (Put `print("start")` at the top of the file and run it again: `start` never appears, and the error message now names line 3, because every line moved down by one.)

So indentation is part of the language itself, and getting it wrong is a syntax error.

</details>
{% endhint %}

Because the interpreter enforces indentation for you, the remaining style choices are the ones it does not care about but your readers do: how many spaces you indent by, spaces around operators, blank lines between functions, and the names you choose. Python names use `snake_case`, lowercase words joined by underscores.

**Question:** This function runs without errors. How would you fix its code style?

```python
def saythetime(time):
 if time<=12:
            print("Good morning")
 elif time<=18:
  print( "Good afternoon" )

 else:
    print("Good evening")

saythetime(5)
```

**<details><summary>Answer</summary>**

```python
def say_the_time(time):
    if time <= 12:
        print("Good morning")
    elif time <= 18:
        print("Good afternoon")
    else:
        print("Good evening")

say_the_time(5)
```

The original indents each block by a different amount (1, 12, 2 and 4 spaces). Python accepts that, but a reader can't tell at a glance which `print` belongs to which branch. So use four spaces per level, all the way down. Add spaces around `<=` so the comparison stands out from the names on either side. Remove the spaces inside the parentheses and the stray blank line. Rename `saythetime` to `say_the_time`, because Python names use `snake_case` and the underscores let a reader see the three words.

</details>
