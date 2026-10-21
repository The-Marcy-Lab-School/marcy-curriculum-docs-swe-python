# 1.5 Strings, Inputs and Outputs

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/05-strings-inputs-and-outputs/)
{% endhint %}

**Table of Contents:**

- [Key Terms](#key-terms)
- [Strings](#strings)
- [Input](#input)
  - [Getting Input with `input()`](#getting-input-with-input)
  - [Cleaning Input](#cleaning-input)
    - [Challenge: Find the Method](#challenge-find-the-method)
    - [Type Casting](#type-casting)
  - [Validating Input](#validating-input)
    - [The `len()` builtin](#the-len-builtin)
    - [The `in` operator](#the-in-operator)
    - [Challenge: Find String Methods for Validation](#challenge-find-string-methods-for-validation)
    - [Validating Numbers with `try` and `except`](#validating-numbers-with-try-and-except)
  - [Parsing Input](#parsing-input)
    - [Bracket Notation](#bracket-notation)
    - [Slicing](#slicing)
    - [Slicing with `find()`](#slicing-with-find)
- [Output](#output)
  - [Repeating Characters with `*`](#repeating-characters-with-)
  - [String Tools Inside f-strings](#string-tools-inside-f-strings)
  - [Formatting Numbers](#formatting-numbers)
  - [Lining Up Columns](#lining-up-columns)
- [Madlib Challenge](#madlib-challenge)

![A string of characters is like a bracelet with beads on it](../.gitbook/assets/image.png)

## Key Terms

- A program is **hard-coded** if the program code must be modified in order to produce a new result.
- The **`input()`** function gets input from the user. It always returns a string, so casting it to another type is your job.
  - **Type casting** with `str()`, `int()`, `float()`, `bool()` turns a value of one type into another.
- A program that uses user input to influence the program's behavior involves three steps:
  - **Cleaning** input means putting what the user typed into the format that the rest of the program expects (e.g. removing whitespace or converting a string to lowercase).
  - **Validating** input means checking that it is acceptable before the program uses it (e.g. checking that a name is not empty or that an email address contains an `@`).
  - **Parsing** input means taking it apart to get the pieces the program needs (e.g. getting the first letter of a name or the part of an email address before the `@`).
- A **method** is a function that is attached to a value. Methods are invoked using **dot notation**: `value.method()`.
- Strings have many tools for cleaning, validating, and parsing input:
  - **String methods** like `startswith`, `endswith`, `find`, `upper`, `replace`, `strip`, and `split` allow you to search, analyze, and manipulate string data. Strings are immutable, meaning all operations are "read-only".
  - **Bracket notation** returns individual characters within a string: `str[index]`
  - The built-in **`len()`** function returns the number of characters in a string (and you can use this function on lists and dictionaries too!).
- A **`try`/`except` statement** runs the code in its `try` block, and if a line there raises the error named after `except`, runs the `except` block instead of crashing. It is how a program validates input that only a cast like `int()` can judge.
- A **format specifier** after a colon inside an f-string's braces controls how the value is displayed. `{price:.2f}` shows two digits after the decimal point, and `{item:<12}` and `{price:>8}` set a width and line the value up on the left or the right.

## Strings

A string is a sequence of characters between single or double quotations.

```python
print("This is a string!")
print('1234556')     # <-- also a string
print('True')        # <-- also a string
print('!@#$%^&*()')  # <-- also a string
```

{% hint style="info" %}
**Escaping characters.** If you want a quotation mark inside your string, put a `\` in front of it:

```py
print("The robot said, \"beep boop bop\"")
```

The same backslash makes special characters: `\t` is a tab and `\n` is a new line:

```py
print("First line\nSecond line") # prints two lines
```
{% endhint %}

## Input

A program is considered **hard-coded** if the program code must be modified in order to produce a new result. The built-in `input()` function lets the person running the program provide the data instead, through the Terminal.

Handing that job to the user means giving up some control. When you wrote the data yourself, you knew exactly what each value held. A user can type anything: extra spaces, unexpected capitals, nothing at all, or an email address with no `@` in it.

A program that uses those values exactly as they arrive will print strange output or crash. What you still control is what the program does with each value next. A program typically does a few things with user input:

1. cleaning
2. validating
3. parsing

Whatever the user types arrives as a string, so the more you know about strings, the more kinds of input your program can handle. The rest of this section teaches the string tools for each job.

### Getting Input with `input()`

`input(prompt)` prints the `prompt`, waits for the user to type a line and press Enter, and returns what they typed:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
name = input("Hello there! What's your name? ")
print(f"hi {name}. My name is HAL")
```

{% endcode %}

The space at the end of the prompt is there so that what the user types does not run into the question.

### Cleaning Input

**Cleaning** input means putting what the user typed into the format that the rest of the program expects. Users type messily. They add spaces, and they use capitals when you expected lowercase. Python compares strings character by character, so `"YES" == "yes"` is `False`. Without any cleanup, a check like `answer == "yes"` would tell a user who typed `YES` "Okay, see you later."

Strings come with tools for cleaning up text like this, called methods. A **method** is a special kind of function that is attached to a value. Methods are invoked using **dot notation**: `value.method()`:

```py
answer = '  YES '

# str.strip() returns `str` without the whitespace at either end
print(answer.strip())
# Output: YES

# str.lower() returns `str` with every character in lowercase
print('YES'.lower())
# Output: yes

# str.upper() returns `str` with every character capitalized
print('yes'.upper())
# Output: YES

# Other data types have methods too, such as float.is_integer()
print(5.0.is_integer()) # True
print(5.1.is_integer()) # False
```

{% hint style="info" %}

🤔 **How does the method access the value?** Because methods are attached to a value, they can access the value without it being passed in as an argument (this is possible with the `class` syntax in Python, covered in the next module).

{% endhint %}

Strings are **immutable** (read-only), so a string method never changes the string it is called on. Methods like `strip()` and `lower()` first copy the string they are operating on and return a new string instead. So, after `answer.strip()` runs, `answer` still holds `'  YES '`.

```python
answer = '  YES '
answer.strip()
answer.lower()
print(answer)
# Output:   YES   (the spaces and the capitals are still there)
```

As a result, we need to store the new string in a variable. However, to avoid storing each method result in a new variable and working through them one at a time, we can use **method chaining** to combine multiple method calls into one line:

```py
answer = '  YES '
cleaned = answer.strip().lower()
print(cleaned)
# Output: yes
```

This works because `strip()` returns a new string, and `.lower()` is called on that new string.

Method chaining lets you clean input on the same line as the `input()`:

```python
answer = input("Do you want to continue? (yes/no) ").strip().lower()

if answer == "yes":
    print("Let's keep going!")
else:
    print("Okay, see you later.")
```

Whether the user types `yes`, `YES`, or ` Yes`, `answer` holds `"yes"`.

#### Challenge: Find the Method

Sometimes cleaning means removing characters from the middle of a string, not only from its ends. Head over to [w3schools](https://www.w3schools.com/python/python_strings_methods.asp) and **find the method that can be used to convert a phone number like `'555-123-4567'` into `'5551234567'` (remove the `-` between the numbers).**

**<details><summary>Answer</summary>**

`replace(old, new)` replaces every appearance of `old` with `new`, so replacing a character with an empty string removes it:

```python
phone = '555-123-4567'

print(phone.replace('-', ''))
# Output: 5551234567

print('apples'.replace('p', 'g'))
# Output: aggles

print('apples'.replace('p', 'g', 1))
# Output: agples
```

Notice that `replace` replaces _every_ match unless you tell it how many to replace with a third argument.

</details>

#### Type Casting

Cleaning input also means giving it the data type the program needs.

{% hint style="warning" %}
**Predict, then run.**

```python
age = input("How old are you? ")
print(age * 2)
```

Type `20` when asked. What prints?

<details><summary>What actually happens</summary>

```
2020
```

`input()` **always returns a string**, no matter what the user typed. The user typed `20`, but `age` holds `"20"`, and a string multiplied by `2` is repeated, just like `"3" * 5` in chapter 1.2.

Every time you take input from a user and want a number, casting it is your job. Nothing does it for you.

</details>
{% endhint %}

Every value that comes out of `input()` is a string, even when the user typed a number. If `age` holds the string `"20"`, both `age + 1` and `age >= 18` crash with a `TypeError`, because Python will not do arithmetic or a `>=` comparison between a string and a number. Before you can write either one, you need to cast `age` to a number.

Converting a value from one data type to another is called **type casting**. We can cast a value using the type casting functions `str()`, `int()`, and `float()`:

```python
# Everything can easily be turned into a string
print(str(1))          # -> "1"
print(str(True))       # -> "True"

# Not everything becomes a number in a nice way
print(int(False))      # -> 0
print(int("42"))       # -> 42
print(float("0.50"))   # -> 0.5
print(int("hello"))    # -> crashes with ValueError: invalid literal for int() with base 10: 'hello'
```

Casting input works the same way. `strip()` and `int()` can both clean the input on the same line as the `input()`:

```python
age = int(input("How old are you? ").strip())
print(f"Next year you will be {age + 1}")
```

If the user types `twenty` instead of `20`, `int()` crashes with the same `ValueError` as `int("hello")`. A program that casts input without validating it crashes as soon as a user types something unexpected. Handling that problem is the job of [Validating Input](#validating-input), which comes next.

{% hint style="warning" %}
**Predict, then run.** What is the result of the expression below? What data type is produced? Do you think we should even be allowed to do something like this?

```python
print("1" + 1)
```

<details><summary>What actually happens</summary>

```
TypeError: can only concatenate str (not "int") to str
```

Python will not add a string and a number. It does not know whether you wanted the string `"11"` or the number `2`, and rather than pick one it stops and tells you. The error is your cue to say which cast you meant:

```python
print("1" + str(1))   # -> "11"
print(int("1") + 1)   # -> 2
```

Between kinds of numbers, conversion happens on its own: `5 + 2.5` turns the integer `5` into a float and produces `7.5`, and `5 + True` produces `6` because `True` counts as `1` in arithmetic. Division with `/` is a separate rule: `/` always produces a float, even between two integers, so `4 / 2` produces `2.0`.

</details>
{% endhint %}

The fourth type casting function, `bool()`, is the one you met with truthy and falsy values in chapter 1.4. An `if` statement calls `bool()` on its condition for you whenever the condition is not already a boolean.

### Validating Input

**Validating** input means checking that it is acceptable before the program uses it. Clean input can still be the wrong input. The user may have pressed Enter without typing anything, or typed an email address with no `@` in it. Each tool in this section answers a question about a string, and the answer is a value that an `if` statement can use to decide what the program does next. The last tool, `try` and `except`, answers the one question that no string method answers exactly: whether a cast will work.

#### The `len()` builtin

The `len()` function returns the number of characters in a string (including spaces). `len()` is a function rather than a method, so the string goes inside the parentheses: `len(name)`.

```python
message = 'Hello there!'

print(len(message))
# Output: 12

print(len(''))
# Output: 0
```

A string with no characters at all, `''`, is called an **empty string**, and its length is `0`. Pressing Enter without typing anything makes `input()` return an empty string. Typing only spaces does too, once `strip()` has removed them.

Without a check, this program would greet the user with `Hello, !`, and the user could reasonably believe the program is broken. Checking the length first lets the program say what went wrong instead:

```python
name = input("What's your name? ").strip()

if len(name) == 0:
    print("You didn't type a name.")
else:
    print(f"Hello, {name}!")
```

#### The `in` operator

The `in` operator checks whether one string is inside another.

```py
print('ana' in 'banana')
# Output: True

print('ANA' in 'banana')
# Output: False
```

**<details><summary>Q: Is this operation case-sensitive?</summary>**

Yes! In the example above, `'ANA' in 'banana'` resolved to `False`. This is one reason to clean input with `lower()` before validating it.

</details>

**Question: How would you use `in` to complete this `is_marcy_email` function below?**

```py
def is_marcy_email(email):
    return ???

print(is_marcy_email('reuben@marcylabschool.org')) # True
print(is_marcy_email('reuben@marcylabschool.com')) # False
print(is_marcy_email('reuben@marcy.org'))          # False
```

**<details><summary>Answer</summary>**

```py
def is_marcy_email(email):
    return '@marcylabschool.org' in email
```

</details>

#### Challenge: Find String Methods for Validation

Head over to [w3schools](https://www.w3schools.com/python/python_strings_methods.asp) and look at the string methods. There are a number of useful methods for validating inputs. See if you can find the right method for the following scenarios:

1. The user enters a phone number but it must use the `"718"` area code
2. The user enters a password but it can only contain alphanumeric characters (letters and numbers, no symbols)
3. The user enters a username but it must be written in lowercase
4. The user enters a ZIP code but it must contain only digits

**<details><summary>Answers</summary>**

1. You can use `phone_number.startswith("718")`
2. You can use `password.isalnum()`
3. You can use `username.islower()`
4. You can use `zip_code.isdigit()`

Note that most string methods don't use snake_case and instead use all lowercase letters.

</details>

#### Validating Numbers with `try` and `except`

When a program needs a number, `isdigit()` looks like the check to run before the cast. But `isdigit()` answers "is every character a digit?", and the program needs to know "can `int()` convert this?". For some strings, those two questions have different answers:

```python
print('-5'.isdigit())
# Output: False, but int('-5') returns -5

print('²'.isdigit())
# Output: True, but int('²') crashes with a ValueError
```

A program that checks `isdigit()` before calling `int()` would tell a user who typed `-5` that it is not a number, and it would still crash for a user who typed `²`. The only reliable judge of what `int()` can convert is `int()` itself. A **`try`/`except` statement** lets the program attempt the cast and decide what to do when it fails:

```python
age = input("How old are you? ").strip()

try:
    age = int(age)
    print(f"Next year you will be {age + 1}")
except ValueError:
    print(f"Sorry, {age} is not a whole number")
```

Python runs the lines in the `try` block in order. If one of them raises the error named after `except`, Python stops the `try` block at that line and runs the `except` block instead of crashing. If no line raises that error, Python skips the `except` block. Here is what happens when the user types `twenty`:

- `int("twenty")` raises a `ValueError`.
- Python stops the `try` block on that line. The assignment never happens, so `age` still holds the string `"twenty"`, and the `print()` beneath it never runs.
- The error is a `ValueError`, which is the type named after `except`, so Python runs the `except` block, and the user reads `Sorry, twenty is not a whole number` instead of a crash.

`except ValueError` catches only a `ValueError`. Any other error, such as a `NameError` from a misspelled variable, still crashes the program and shows its message, so a mistake in your own code is not hidden behind the message meant for the user.

{% hint style="warning" %}
**Predict, then run.** Run the program above three times, typing `-3`, then `4.2`, then `42` with spaces around it. What prints each time?

<details><summary>What actually happens</summary>

```
Next year you will be -2
Sorry, 4.2 is not a whole number
Next year you will be 43
```

`int()` accepts a minus sign, so `-3` is converted. `int()` rejects a decimal point, so `4.2` reaches the `except` block. If the program should accept decimals, cast with `float()` instead. `strip()` removed the spaces around `42` before `int()` saw it.

</details>
{% endhint %}

Use an `if` check when a simple check answers the question exactly, such as `len(name) == 0` for an empty answer. Use `try` and `except` when only the operation itself can tell whether it will work, such as casting with `int()` or `float()`.

### Parsing Input

**Parsing** input means taking it apart to get the pieces the program needs, such as the first letter of a name or the part of an email address before the `@`. Taking a piece out of a string starts with knowing where each character is.

#### Bracket Notation

Each character in a string, including spaces, has an **index** — a numbered position starting at `0`.

We can get a single character from a string using **Bracket Notation** and the index: `string[index]`

```python
print("abc"[0])    # Output: a
print("abc"[1])    # Output: b
print("abc"[2])    # Output: c
```

It works on variables too!

```python
message = 'Hello there!'

print(message[0])   # Output: H
print(message[4])   # Output: o
print(message[5])   # Output: ???
print(message[11])  # Output: ???
```

Python also lets you count backwards from the end of a string with a negative index. `-1` is the last character, `-2` is the one before it, and so on:

```python
print(message[-1])  # Output: !
print(message[-2])  # Output: ???

print(message[len(message) - 1])
# Output: !  (the same character as message[-1])
```

{% hint style="warning" %}
**Predict, then run.** Run this program and press Enter without typing a name.

```python
name = input("What's your name? ").strip()
print(f"Your name starts with {name[0].upper()}")
```

<details><summary>What actually happens</summary>

```
IndexError: string index out of range
```

- Pressing Enter without typing anything makes `input()` return an empty string, `""`.
- An empty string has no characters, so it has no index `0`.
- `name[0]` asks for a character that does not exist, so Python stops with an `IndexError`.

The program stops, because an index has to be inside the string.

The `len()` check from [Validating Input](#validating-input) prevents this crash too, because index `0` exists only when the string has at least one character:

```python
name = input("What's your name? ").strip()

if len(name) == 0:
    print("You didn't type a name.")
else:
    print(f"Your name starts with {name[0].upper()}")
```

</details>
{% endhint %}

**Question: What would you return to complete this `starts_and_ends_with_a` function below?**

```py
def starts_and_ends_with_a(text):
    return ???

print(starts_and_ends_with_a('apple'))          # False
print(starts_and_ends_with_a('banana'))         # False
print(starts_and_ends_with_a('abracadabra'))    # True
```

**<details><summary>Answer</summary>**

```py
def starts_and_ends_with_a(text):
    return text[0] == 'a' and text[-1] == 'a'
```

</details>

#### Slicing

An index takes out one character. **Slicing** with `[start:end]` takes out a piece of the string, from `start` up to but not including `end`:

```python
fruits = 'apples, bananas, cherries'

print(fruits[0:6])
# Output: apples
```

Either number in a slice can be left out. Leaving out `start` begins the slice at the first character, and leaving out `end` continues the slice to the last character. A negative number counts from the end of the string, just as it does with a single index:

```python
print(fruits[:6])
# Output: apples

print(fruits[8:])
# Output: bananas, cherries

print(fruits[-8:])
# Output: cherries
```

#### Slicing with `find()`

A slice needs index numbers, but with input, the user decides where the interesting part of the string is. The methods `find` and `rfind` return the index of a character, or a longer piece of text, that you are looking for.

- `find` returns the index of the first match
- `rfind` returns the index of the last match.
- Both methods count the index from the left, the normal way. When there is no match, both methods return `-1`:

**Predict, then run**: What will be the output of each print statement below?

```python
fruit = 'bananas'

print(fruit.find('a'))
# Output: ???

print(fruit.rfind('a'))
# Output: ???

print(fruit.find('z'))
# Output: ???
```

**<details><summary>Answer</summary>**

```python
fruit = 'bananas'

print(fruit.find('a'))
# Output: 1

print(fruit.rfind('a'))
# Output: 5

print(fruit.find('z'))
# Output: -1 (not found)
```

</details>

Together, `find()` and a slice take out a piece of the input whose position you could not know in advance. This program asks for an email address, validates it with the `in` operator, and takes everything before the `@` as a username:

```python
email = input("What's your email? ").strip().lower()

if "@" in email:
    username = email[:email.find("@")]
    print(f"Welcome, {username}!")
else:
    print(f"Sorry, {email} is not an email address.")
```

`email.find("@")` returns the index of the `@`, and a slice stops just before its `end`, so `email[:email.find("@")]` is every character before the `@`. If the user types `Reuben@MarcyLabSchool.org`, `lower()` turns it into `reuben@marcylabschool.org`, `find("@")` returns `6`, and `username` holds `"reuben"`. The `is_marcy_email` function from [Validating Input](#validating-input) could check the same `email` to decide whether the user belongs to Marcy.

When the input holds several pieces separated by the same characters, the `split` method breaks it into a list of pieces. Lists are the subject of chapter 1.7.

```python
print('apples, bananas, cherries'.split(', '))
# Output: ['apples', 'bananas', 'cherries']
```

Be careful when chaining after `split()`. Not every method returns a string: `split()` returns a list and `isdigit()` returns a boolean, so something like `'a, b'.split(', ').lower()` crashes with an `AttributeError`.

## Output

Everything a command-line program shows its user comes out of `print()`. Chapter 1.1 showed how to print several values at once and how to place values inside text with f-strings. `print()` turns every value into a string before showing it, so the output of your program is a string that you build, and the string tools you used on input work just as well on output. This section adds a few tools for making that output easy to read.

### Repeating Characters with `*`

The `*` operator repeats a string, as you saw with `"3" * 5` in chapter 1.2. A repeated character makes a separator line. For example, this program prints a heading in capitals with a line of `=` beneath it:

```python
title = "Shopping List"

print(title.upper())
print("=" * len(title))
# Output:
# SHOPPING LIST
# =============
```

`title.upper()` returns a capitalized copy of the title, and `"=" * len(title)` repeats `=` once for every character in the title. Because the length of the line comes from `len()` instead of from counting characters by hand, the line stays exactly as long as the heading when `title` changes to `"Groceries"` or to anything else.

{% hint style="warning" %}
**Predict, then run.** Many receipts hide every digit of the card number except the last four.

```python
card = "4111222233334444"
print("*" * (len(card) - 4) + card[-4:])
```

<details><summary>What actually happens</summary>

```
************4444
```

- `len(card)` is `16`, so `len(card) - 4` is `12`.
- `"*" * 12` repeats the star twelve times.
- `card[-4:]` takes the last four characters, `"4444"`.
- `+` joins the two strings. Both sides are already strings, so nothing needs casting.

The number of stars comes from the card number itself, so a 15-digit card gets 11 stars and still shows only its last four digits. The program never needs to know in advance how long the card number is.

</details>
{% endhint %}

### String Tools Inside f-strings

Anything that produces a value can go inside an f-string's braces, including a method call, an index, or a slice. Each string tool from the Input section can shape a value right where it appears in the message:

```python
first = "ada"
last = "lovelace"
card = "4111222233334444"

print(f"Welcome, {first[0].upper()}{first[1:]}!")
# Output: Welcome, Ada!

print(f"Your initials are {first[0].upper()}.{last[0].upper()}.")
# Output: Your initials are A.L.

print(f"Paid with the card ending in {card[-4:]}")
# Output: Paid with the card ending in 4444
```

Each pair of braces holds its own expression. In the first message, `first[0].upper()` takes the first character of the name and capitalizes it, and `first[1:]` takes every character after the first, so together they print the name with a capital letter even though `first` is stored in lowercase.

### Formatting Numbers

Put a colon after the expression inside the braces and you can say _how_ the value should be displayed. This is called a **format specifier**. The one you will use most is `.2f`, which means "as a decimal number with exactly two digits after the decimal point":

```python
price = 5
print(f"${price:.2f}")
# Output: $5.00

total = 31.400000000000002
print(f"{total:.2f}")
# Output: 31.40
```

That `31.400000000000002` is the kind of number you get from arithmetic with decimals, because computers store decimal numbers in a way that is very slightly inexact. The format specifier changes only how the number is _displayed_. The value in `total` is untouched. If you want to change the number itself, `round(total, 2)` returns `31.4`.

{% hint style="warning" %}
**Predict, then run.** Suppose you flip a coin 12 times and 7 of the flips come up heads.

```python
heads = 7
flips = 12

print(f"That is {heads / flips * 100}%!")
print(f"That is {heads / flips * 100:.1f}%!")
```

<details><summary>What actually happens</summary>

```
That is 58.333333333333336%!
That is 58.3%!
```

`.1f` rounds the number to one digit after the decimal point. Both lines print the same calculation. The second line shows only as many digits as a person reading a percentage needs.

</details>
{% endhint %}

### Lining Up Columns

A receipt is hard to read when each price starts wherever its item's name happens to end. A number after the colon in a format specifier sets a **width**, the fewest characters the value takes up, and Python fills the rest of that space with spaces. `<` lines the value up on the left of that space and `>` lines it up on the right. Together with `*`, a width prints a table whose columns line up, however long each item's name is:

```python
print(f"{'Item':<12}{'Price':>8}")
print("-" * 20)
print(f"{'Coffee':<12}{3.5:>8.2f}")
print(f"{'Bagel':<12}{2.25:>8.2f}")
print("-" * 20)
print(f"{'Total':<12}{3.5 + 2.25:>8.2f}")
```

```
Item           Price
--------------------
Coffee          3.50
Bagel           2.25
--------------------
Total           5.75
```

Every row is 12 characters of name plus 8 characters of price, so the separator line is `"-" * 20`. `>8.2f` combines a width with two digits after the decimal point, and lining the prices up on the right puts every decimal point in the same column. The width is the _fewest_ characters, so a name longer than 12 characters pushes its price out of line. Choose a width wider than the longest value the column will hold.

## Madlib Challenge

The program below is **hard-coded**: the only way to get a different story is to open `main.py` and edit the variables, which a friend playing your madlib cannot do. The `input()` function fixes that problem: the person running the program supplies the words, and every run can tell a new story.

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

main()
```

{% endcode %}

Your goal is to do the following in the `madlib-challenge` folder:

1. Replace the hard-coded variables defined in the `main` function with values retrieved from the user via the `input()` function, and remove any spaces the user types around their answers.
2. `is_happy` has to be a boolean. The user can only type a string, and every non-empty string is truthy (chapter 1.4). If you passed their answer straight to `madlib`, typing `N` would still give the story a happy ending. Ask them to type `Y` or `N`, and turn their answer into `True` or `False`. `y`, `Y`, and `Y` (with spaces around it) should all count as yes.

Now run your program a few times with different words. The hard-coded story read correctly only because its words happened to fit the sentences around them. Once a friend chooses the words, the story starts to break: the name `ben` prints as "a man named ben", the item `apple` prints as "he found a apple", and the quantity `1` prints as "his 1 dogs". The `madlib` function produces the program's output, so fix each of these problems inside `madlib`, using the string tools from this chapter:

3. Print the name with a capital first letter and the rest in lowercase, however the user typed it. `ben`, `BEN`, and `bEN` should all print as `Ben`.
4. Put "an" before `new_item` when it starts with a vowel, and "a" otherwise: "an apple" but "a new car".
5. When the quantity is `1`, leave the `s` off the item: "his 1 dog", but "his 50 dogs".
6. Start the story with a title, such as `The Story of Ben`, and print a line of `=` beneath it that is exactly as long as the title. The user chooses the name, so you cannot count the characters ahead of time.

If you get stuck, you can view the solution below:

**<details><summary>Q: Solution</summary>**

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

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

Notice that `quantity` is left as a string. It is printed and compared with `"1"`, and neither of those needs a number, so there is no reason to cast it.

This solution assumes that the user types at least one character for every answer. A user who presses Enter without typing a name still crashes `name[0]` with the `IndexError` from [Parsing Input](#parsing-input). Adding a `len()` check for that case is a good next step.

</details>
