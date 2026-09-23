# 1. Intro to Programming

There are so many terms and concepts to learn about programming. In this lesson, we will learn the fundamental vocabulary and concepts that are shared by practically every programming language. You may see code with syntax that you don't understand and that is fine, you will dig deeper into that code's syntax in later lessons. For now, just focus on learning the vocabulary in the **Key Terms** section.

**Table of Contents**

- [Setup](#setup)
- [Key Terms](#key-terms)
- [What is a program?](#what-is-a-program)
- [Running a file with the Python interpreter](#running-a-file-with-the-python-interpreter)
- [Printing to the Terminal with `print()`](#printing-to-the-terminal-with-print)
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

- **Control Flow** refers to the order in which lines of code are executed. Control flow runs from the top of a file to the bottom.
- **Code Style** refers to the formatting of the code in a way that makes it easier to read and understand. Python's style conventions are written down in a document called [PEP 8](https://peps.python.org/pep-0008/).

## What is a program?

A program is a text file with instructions that a computer executes to accomplish some task. It will be made up of comments, expressions, and statements:

**Comments** are ignored and help to explain the code.

```python
# this is a comment
```

**Expressions** are any piece of code that evaluates to a single value. the results of evaluating an operation (e.g. `5 + 5`) or a function call (e.g. `len("hi")`). A standalone values (e.g. the string literal `"hello world"`) is also considered an expression because it evaluates to itself.

```python
5 + 5       # Evaluates to 10
len("hi")   # Evaluates to 2
"hello"     # Evaluates to "hello"
5           # Evaluates to 5
```

Expressions on their own do nothing. Expressions become useful when used within statements.

**Statements** are instructions that perform an action. They change the program in some way, often using expressions. For example, variable assignments alter the program's **state** (the data stored by a program at a point in time) and `if`/`else` statements change the control flow of the program:

{% code title="main.py" lineNumbers="true" %}

```python
# assigning a variable stores a value in the program's memory to be used later
instructor = "ben"
mood = None

# if statements change the control flow of a program (which line of code is executed next)
if instructor != "ben":
    mood = "sad"
else:
    mood = "happy"

print(mood)
```

{% endcode %}

**<details><summary>Q: In the statements above, what expressions can you see?</summary>**

The `instructor` and `"ben"` expressions are combined using the `!=` operator to create an expression that returns the value `False`

</details>

## Running a file with the Python interpreter

When we want to run the code in a file, we use a piece of software called the **Python interpreter**.

> The Python interpreter is a program that reads a `.py` file and executes it, one statement at a time.

The interpreter is installed on your computers and can be activated in the Terminal using the `python3 [filename]` command:

```sh
# main.py is the name of the file we want to run
python3 main.py
```

**Question:** Why are we not seeing anything when we run this file?

## Printing to the Terminal with `print()`

`print()` is a built-in function that prints text to "standard output", which is a more formal way of describing the Terminal.

```python
print("hello world!")
```

The `print()` function is used primarily to verify the output of a program for debugging purposes. For example, this code converts 212° Fahrenheit to Celsius which should produce the result 100°C. Do you expect it to work?

```python
fahrenheit = 100
celsius = fahrenheit - 32 * 5 / 9
```

With `print(celsius)` we can verify whether or not we performed the calculation properly.

### Debunking The `print()` Myth

{% hint style="danger" %}
Myth: "If our program doesn't print anything to the screen, then it isn't working or it isn't doing anything!"
{% endhint %}

It is common to think that without `print()`, the program isn't doing anything. This is not the case!

This program below runs a loop one hundred million times! Even if you don't see any output, notice that it takes a moment for it to finish running:

```python
x = 0

# A loop with 100 million iterations will take a few seconds to run! Increase that number to a billion and it could take a minute or more.
for i in range(100_000_000):
    x += 1
```

Your computer IS executing the instructions you give it, but you just can't see the results because there is no `print()` statement. You can prove it by asking the Terminal to time the program for you:

```sh
time python3 main.py
```

```
python3 main.py  3.82s user 0.02s system 99% cpu 3.840 total
```

Nothing was printed by the program, but the Terminal reports that it spent almost four seconds running it. (Your numbers will differ.)

`print()` itself also has more to it than a single message. It can take several values at once, and you can control what goes between them and what comes after them:

```python
x = 10

print("start")
print("the value of x is", x)
print("a", "b", "c", sep="-")
print("no new line after this one", end="")
print(" <- see?")
```

## Control Flow

Computers can only execute one statement at a time and **Control Flow** refers to the order in which a program's statements are executed.

The default control flow is top to bottom, with statement being executed in order.

```python
print("1")
print("2")
print("3")
```

There exist tools in most programming languages like `if` statements, functions, and loops that let the programmer alter the program's control flow. For example, `if` statements can cause certain statements to be skipped.

```python
instructor = "ben"
mood = None

# if statements change the "control flow" of a program (which line of code comes next)
if instructor != "ben":
    mood = "sad"  # this is skipped
else:
    mood = "happy"  # this line of code is executed next
```

A `for` loop can cause a statement (or multiple) to be executed more than once

```py
# A loop with 100 million iterations will take a few seconds to run! Increase that number to a billion and it could take a minute or more.
for i in range(100_000_000):
    x += 1
```

We'll dive deeper into `if` statements and `for` loops later on but for now, the important things to remember about control flow are:

- Only one statement is executed at a time
- You can alter the program's control flow with special statements like `if` statements and loops

## Code Style and Readability

**Readability** is how easy it is for another engineer to read and understand your code (including future you).

Indentation shows the scope of each line of code. In Python it does more than that: indentation is how the interpreter knows which lines belong to which block. Whenever a line ends with a colon `:`, the lines that belong to it must be indented underneath it. The convention, written down in PEP 8, is four spaces per level.

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

Nothing runs. The interpreter cannot tell what belongs to `can_vote`, so it refuses the whole file before executing a single line. In Python, indentation is not a style choice you make for your readers. It is part of the language, and getting it wrong is a syntax error.

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

Four spaces per level, all the way down. Spaces around `<=`. No spaces inside the parentheses. No extra blank lines. And the function is renamed from `saythetime` to `say_the_time`, because that is how Python names things.

</details>
