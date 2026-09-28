# 4. Strings and Conditional Statements

**Table of Contents:**

- [Key Terms](#key-terms)
- [Strings](#strings)
  - [String Interpolation with f-strings](#string-interpolation-with-f-strings)
  - [String Indexes and Bracket Notation](#string-indexes-and-bracket-notation)
  - [Strings are Immutable](#strings-are-immutable)
  - [String Length](#string-length)
  - [String Methods](#string-methods)
- [Conditional Statements](#conditional-statements)
  - [`if/elif/else` statements](#ifelifelse-statements)
  - [Order Matters](#order-matters)
  - [Only `if` statements](#only-if-statements)
  - [Guard Clauses](#guard-clauses)
  - [Type Conversion](#type-conversion)
  - [Truthy and Falsy Values](#truthy-and-falsy-values)
  - [Use Conditional Expressions To Simplify Conditionals](#use-conditional-expressions-to-simplify-conditionals)

![A string of characters is like a bracelet with beads on it](../.gitbook/assets/image.png)

## Key Terms

- **Strings** are sequences of characters enclosed in quotes (single or double). Strings are immutable, meaning their characters cannot be changed directly.
- You can _access_ individual characters of a string with **bracket notation**.
- You can check the length of a string with **`len(str)`** (and you can use this method on lists and dictionaries too!).
- **String methods** like `startswith`, `endswith`, `find`, `upper`, `replace`, `strip`, and `split` allow you to search, analyze, and manipulate string data.
- The **`in` operator** checks whether one string contains another.
- **Control Flow** refers to the order in which statements of a program are executed, typically top-to-bottom.
- **Conditional statements** (`if`, `elif`, `else`) let you control the flow of your program based on data values. The order of conditions matters, and only the first true condition in a chain will execute.
- **Guard clauses** are single `if` statements that return early from a function, simplifying conditional logic.
- Values can be **truthy** or **falsy** depending on their content. An `if` calls `bool()` on its condition for you, which is what makes `if not name:` work as a guard against empty input.
- **Conditional expressions** provide a concise way to choose between two values based on a condition.
- The **`input()`** function gets input from the user. It always returns a string, so converting it to another type is your job.
- **Type conversion** with `str()`, `int()`, `float()`, `bool()` turns a value of one type into another.

## Strings

A string is a sequence of characters between single or double quotations.

```python
print("This is a string!")
print('!@#$%^&*()1234556')  # <-- also a string
```

{% hint style="info" %}
**Escaping characters.** If you want a quotation mark inside your string, put a `\` in front of it: `"The robot said, \"beep boop bop\""`. The same backslash makes special characters: `\t` is a tab and `\n` is a new line, so `print("First line\nSecond line")` prints two lines.
{% endhint %}

### String Interpolation with f-strings

When a string is written with an `f` in front of the opening quote, an expression inside curly braces `{}` is **interpolated** into a string for easy formatting:

```python
print(f"The sum of 10 and 2 is {10 + 2}")
# Output: The sum of 10 and 2 is 12
```

These are called **f-strings**. Without the `f`, the curly braces are just characters:

```python
print("The sum of 10 and 2 is {10 + 2}")
# Output: The sum of 10 and 2 is {10 + 2}
```

### String Indexes and Bracket Notation

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
```

{% hint style="warning" %}
**Predict, then run.** There is no character at index 50.

```python
message = 'Hello there!'
print(message[50])
```

<details><summary>What actually happens</summary>

```
IndexError: string index out of range
```

The program stops. Later in this module you will learn how to catch errors like this one and decide what to do instead. For now, the lesson is that an index has to be inside the string.

</details>
{% endhint %}

### Strings are Immutable

Strings are "immutable" (unable to be mutated). In other words, you cannot use bracket notation to change characters of a string.

{% hint style="warning" %}
**Predict, then run.**

```python
message = 'Hello there!'

message[0] = "J"

print(message)
```

<details><summary>What actually happens</summary>

```
TypeError: 'str' object does not support item assignment
```

Python refuses. A string, once created, cannot be changed. If you want a different string, you make a new one, which is exactly what the string methods below do.

</details>
{% endhint %}

### String Length

The `len()` function tells us the number of characters in a string (including spaces).

```python
message = 'Hello there!'

print(len(message))
# Output: 12

print(message[len(message) - 1])
# Output: !  (the same character as message[-1])
```

### String Methods

A **method** is a function that is attached to a value. Often, methods are used to manipulate the value they are attached to.

- Methods are invoked using **dot notation**: `value.method()`

First, let's look at some "read only" checks that return a boolean. The `in` operator checks whether one string is inside another. `startswith` and `endswith` are methods:

```python
fruits = 'apples, bananas, cherries'

print('ana' in fruits)
# Output: True

print('ANA' in fruits)
# Output: False

print(fruits.startswith('apple'))
# Output: True

print(fruits.endswith('s'))
# Output: True
```

The methods `find` and `rfind` return a number representing the index of a particular character we're looking for. `rfind` searches from the right:

```python
fruits = 'apples, bananas, cherries'

print(fruits.find('p'))
# Output: 1

print(fruits.rfind('p'))
# Output: 2

print(fruits.find('z'))
# Output: -1 (not found)
```

The following return a copy of a string modified in some way. **Slicing** with `[start:end]` takes a piece of the string, from `start` up to but not including `end`. The `upper`, `lower`, and `replace` methods and the `*` operator do what their names suggest:

```python
fruits = 'apples, bananas, cherries'

apples = fruits[0:6]
print(apples)
# Output: apples

loud_fruits = fruits.upper()
print(loud_fruits)
# Output: APPLES, BANANAS, CHERRIES

print(apples * 3)
# Output: applesapplesapples

print(apples.replace('p', 'g'))
# Output: aggles

print(apples.replace('p', 'g', 1))
# Output: agples
```

Notice that `replace` replaces _every_ match unless you tell it how many to replace with a third argument.

Three more methods will do a lot of work for you once your programs start taking input from a user. `strip` removes whitespace from both ends, `split` breaks a string into a list of pieces, and `isdigit` tells you whether a string is made entirely of digits:

```python
answer = '  YES '

print(answer.strip())
# Output: YES

print(answer.strip().lower())
# Output: yes

print('apples, bananas, cherries'.split(', '))
# Output: ['apples', 'bananas', 'cherries']

print('42'.isdigit())
# Output: True

print('4.2'.isdigit())
# Output: False
```

`answer.strip().lower()` is two method calls in a row. `strip()` returns a new string, and `.lower()` is called on that new string. This is called **method chaining**, and it works because every one of these methods returns a string.

## Conditional Statements

Conditional statements allow us to change the behavior of our programs based on the current values of our data.

![In a decision tree, depending on the conditions, we can make different decisions.](../.gitbook/assets/decision-tree.png)

**<details><summary>Q: In the decision tree above, what are the variables that will impact the end result?</summary>**

The first variable is the `weather` and then, depending on the weather, the variable `time` or `hungry` is used to determine whether to walk or take the bus.

</details>

### `if/elif/else` statements

To define the possible decisions that our program can make, we use `if`, `elif`, and `else` statements:

```python
def is_it_hot(temp):
    if temp > 100:
        print("So Hot!")
    elif temp > 90:
        print("Yes!")
    elif temp > 75:
        print("Eh")
    else:
        print("Nah")

is_it_hot(80)
# Output: Eh

is_it_hot(95)
# Output: Yes!

is_it_hot(105)
# Output: So Hot!

is_it_hot(60)
# Output: Nah
```

- `if` and `elif` statements require a boolean condition to evaluate to `True` in order to run. `elif` is short for "else if".
- There can be many `elif` statements, or none at all.
- `else` statements do not require a condition and will run only when none of the other options do.

### Order Matters

Only the first condition that is `True` will be executed. This means we have to be careful with the order in which we write our conditional statements.

**Q: What happens if we rearrange the conditional statements like so?**

```python
def is_it_hot(temp):
    if temp > 75:
        print("Eh")
    elif temp > 90:
        print("Yes!")
    elif temp > 100:
        print("So Hot!")
    else:
        print("Nah")

is_it_hot(80)
# Output: ???

is_it_hot(95)
# Output: ???

is_it_hot(105)
# Output: ???

is_it_hot(60)
# Output: ???
```

### Only `if` statements

In an `if/elif/else` chain of conditional statements, only one statement will be executed. But what if we replace all of the `elif` and `else` statements with other `if` statements?

```python
def is_it_hot(temp):
    if temp > 75:
        print("Eh")
    if temp > 90:
        print("Yes!")
    if temp > 100:
        print("So Hot!")
    if temp <= 75:
        print("Nah")

is_it_hot(105)
# Output: ???
```

### Guard Clauses

When working with a function that changes the value returned based on a condition, we can avoid using conditional chains and only use `if` statements called "guard clauses".

A **guard clause** is an `if` statement that returns before subsequent return statements have a chance to be executed.

```python
def is_it_hot(temp):
    if temp > 75:
        return "Eh"
    if temp > 90:
        return "Yes!"
    if temp > 100:
        return "So Hot!"
    return "Nah"

print(is_it_hot(105))
# Output: ???
```

**<details><summary>Q: Why doesn't the last return statement need an `if` statement?</summary>**

If the program makes it to the last `return "Nah"` statement, we can assume that the temperature is less than or equal to 75 because none of the other conditions were `True`.

</details>

### Type Conversion

Conditions compare values, and a comparison only makes sense between values of the right type. Every string that comes out of `input()` is a string, even when the user typed a number, so before you can write `if age >= 18:` you will often need to convert.

We can convert a value of one data type into another data type using the type conversion functions `str()`, `int()`, and `float()`:

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

That last line is why the `.isdigit()` method from earlier in this chapter exists: check the string before you convert it, and you can give the user a message instead of a crash.

{% hint style="warning" %}
**Predict, then run.** What is the result of the expression below? What data type is produced? Do you think we should even be allowed to do something like this?

```python
print("1" + 1)
```

<details><summary>What actually happens</summary>

```
TypeError: can only concatenate str (not "int") to str
```

Python will not add a string and a number. It does not know whether you wanted the string `"11"` or the number `2`, and rather than pick one it stops and tells you. The error is your cue to say which conversion you meant:

```python
print("1" + str(1))   # -> "11"
print(int("1") + 1)   # -> 2
```

Between kinds of numbers, conversion happens on its own: `5 / 2` produces the float `2.5`, and `5 + True` produces `6` because `True` counts as `1` in arithmetic.

</details>
{% endhint %}

### Truthy and Falsy Values

The fourth conversion function is `bool()`, and it is the one conditions use without being asked. Values that are "non-values" or "empty values" are considered **falsy**. All other values are **truthy**:

```python
print(bool(0))         # -> False
print(bool(""))        # -> False
print(bool(None))      # -> False
print(bool([]))        # -> False (an empty list)
print(bool(100))       # -> True
print(bool("hello"))   # -> True
```

When an `if` is given something that is not already a boolean, it calls `bool()` on it for you. That makes a guard clause against empty input very short:

```python
def greet_friend(friend):
    if not friend:
        return "I can't say hi if I don't know your name!"
    return f"Hi, {friend}! Nice to meet you."

print(greet_friend(""))      # Output: I can't say hi if I don't know your name!
print(greet_friend("Jane"))  # Output: Hi, Jane! Nice to meet you.
```

`not friend` is `True` when `friend` is the empty string, because `""` is falsy. You will see this shape, `if not something:`, in nearly every program that takes input.

One caution. `if not value:` cannot tell `None` apart from `0` or `""`, because all three are falsy. When the question you are asking is specifically "is this `None`?", write `if value is None:`. That is what the `is` operator from chapter 2 is for.

{% hint style="warning" %}
**Predict, then run.**

```python
if "False":
    print("printed")
else:
    print("skipped")
```

<details><summary>What actually happens</summary>

It prints `printed`.

`"False"` is a string with five characters in it, and a non-empty string is truthy. What the characters spell has nothing to do with it. Only the boolean `False`, the number `0`, `None`, and empty things like `""` are falsy. If you ever compare user input to a boolean, remember that the user typed a string.

</details>
{% endhint %}

### Use Conditional Expressions To Simplify Conditionals

- `if` and `else` statements let you choose between one of two code blocks to execute.
- The conditional expression `val_a if condition else val_b` is used to choose between one of two values.

```python
# Okay - Use an if statement to choose which code block to execute
def is_this_even(num):
    if num % 2 == 0:
        message = 'it is even!'
    else:
        message = 'it is odd!'
    print(message)

# Better - Use a conditional expression to choose which value to assign to message
def is_this_even(num):
    message = "it is even!" if num % 2 == 0 else "it is odd!"
    print(message)
```
