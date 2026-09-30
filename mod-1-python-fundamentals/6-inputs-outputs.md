# 6. Inputs and Outputs

A program takes data in, does something with it, and puts data out. In this lesson we'll learn the tools a command-line program uses for both ends of that: strings, which are what the user types and what the program prints; `print()` and f-strings, which put data out; and `input()` and type conversion, which bring data in.

**Table of Contents:**

- [Key Terms](#key-terms)
- [Strings](#strings)
  - [String Indexes and Bracket Notation](#string-indexes-and-bracket-notation)
  - [Strings are Immutable](#strings-are-immutable)
  - [String Length](#string-length)
  - [String Methods](#string-methods)
- [Output with `print()`](#output-with-print)
  - [Printing Several Values](#printing-several-values)
  - [String Interpolation with f-strings](#string-interpolation-with-f-strings)
  - [Formatting Numbers](#formatting-numbers)
- [Input with `input()`](#input-with-input)
- [Type Conversion](#type-conversion)
- [Madlib Challenge](#madlib-challenge)

![A string of characters is like a bracelet with beads on it](../.gitbook/assets/image.png)

## Key Terms

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

## Strings

A string is a sequence of characters between single or double quotations.

```python
print("This is a string!")
print('!@#$%^&*()1234556')  # <-- also a string
```

{% hint style="info" %}
**Escaping characters.** If you want a quotation mark inside your string, put a `\` in front of it: `"The robot said, \"beep boop bop\""`. The same backslash makes special characters: `\t` is a tab and `\n` is a new line, so `print("First line\nSecond line")` prints two lines.
{% endhint %}

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

Three more methods will do a lot of work for you once your programs start taking input from a user, which they will by the end of this chapter. `strip` removes whitespace from both ends, `split` breaks a string into a list of pieces, and `isdigit` tells you whether a string is made entirely of digits:

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

## Output with `print()`

You have been calling `print()` since chapter 1 with one value at a time. It can do more than that.

### Printing Several Values

Give `print()` several values separated by commas and it prints all of them on one line, with a space between each:

```python
name = "Ada"
age = 36

print("name:", name, "age:", age)
# Output: name: Ada age: 36
```

Two keyword arguments control the spacing. `sep` (separator) is what goes _between_ the values, and its default is a space. `end` is what goes _after_ the last value, and its default is `"\n"`, the new line character from the escaping hint above. That default is why every `print()` starts on a new line.

```python
print("a", "b", "c", sep="-")
# Output: a-b-c

print("loading", end="")
print("...", end="")
print("done")
# Output: loading...done
```

{% hint style="warning" %}
**Predict, then run.**

```python
print("1", "2", "3", sep="")
print(1, 2, 3, sep=" + ", end=" = 6\n")
```

<details><summary>What actually happens</summary>

```
123
1 + 2 + 3 = 6
```

The first line has nothing between the values, so they run together. The second line puts `" + "` between the numbers and `" = 6\n"` after them. Notice that `print()` accepted the numbers `1`, `2`, and `3` without complaint. It turns every value into text before printing it.

</details>
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

Anything that produces a value can go inside the braces: a variable, arithmetic, a function call, or a method call.

```python
name = "ada"

print(f"Hello, {name.upper()}! Your name has {len(name)} letters.")
# Output: Hello, ADA! Your name has 3 letters.
```

Like `print()` with commas, an f-string turns each value into text for you. That is why f-strings are the way most Python programmers build a message: the words and the values sit in the order they will be printed, and you never have to convert anything yourself.

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
**Predict, then run.** The coin-flip challenge in chapter 5 printed a percentage. Suppose 7 of 12 flips came up heads.

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

`.1f` keeps one digit after the decimal point. The same calculation, displayed for a human instead of for the computer.

</details>
{% endhint %}

## Input with `input()`

Every program you have written so far has had its data typed directly into the code. The built-in `input()` function lets the person running the program provide it instead, through the Terminal.

`input(prompt)` prints the `prompt`, waits for the user to type a line and press Enter, and returns what they typed:

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

```python
name = input("Hello there! What's your name? ")
print(f"hi {name}. My name is HAL")
```

{% endcode %}

The space at the end of the prompt is there so that what the user types does not run into the question.

Users type messily. They add spaces, they use capitals when you expected lowercase. The string methods from earlier in this chapter clean that up, and method chaining lets you do it on the same line as the `input()`:

```python
answer = input("Do you want to continue? (yes/no) ").strip().lower()

if answer == "yes":
    print("Let's keep going!")
else:
    print("Okay, see you later.")
```

Whether the user types `yes`, `YES`, or `  Yes `, `answer` holds `"yes"`.

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

`input()` **always returns a string**, no matter what the user typed. The user typed `20`, but `age` holds `"20"`, and a string multiplied by `2` is repeated, just like `"3" * 5` in chapter 2.

Every time you take input from a user and want a number, the conversion is your job. Nothing does it for you. That conversion is the next section.

</details>
{% endhint %}

## Type Conversion

Arithmetic and comparisons only make sense between values of the right type. Every value that comes out of `input()` is a string, even when the user typed a number, so before you can write `age + 1` or `if age >= 18:` you will need to convert.

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

```python
age = input("How old are you? ")

if not age.isdigit():
    print(f"Sorry, {age} is not a number")
else:
    age = int(age)
    print(f"Next year you will be {age + 1}")
```

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

The fourth conversion function, `bool()`, is the one you met with truthy and falsy values in chapter 4. It is the one conditions use without being asked.

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

main()
```

{% endcode %}

Your goal is to do the following in the `madlib-challenge` folder:

1. Replace the hard-coded variables defined in the `main` function with values retrieved from the user via the `input()` function.
2. `is_happy` has to be a boolean, but the user can only type a string. Ask them to type `Y` or `N`, and turn their answer into `True` or `False`. `y`, `Y`, and ` Y ` should all count as yes.

If you get stuck, you can view the solution below:

**<details><summary>Q: Solution</summary>**

{% code title="main.py" overflow="wrap" lineNumbers="true" %}

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
    name = input('Choose a name: ')
    verb = input('Choose a verb: ')
    quantity = input('Choose a quantity: ')
    item = input('Choose an item: ')
    new_item = input('Choose a new item: ')
    is_happy_response = input('Choose whether the story is happy. Y or N: ')
    is_happy = is_happy_response.strip().upper() == "Y"

    madlib(name, verb, quantity, item, new_item, is_happy)

main()
```

{% endcode %}

Notice that `quantity` is left as a string. It only ever gets printed, so there is no reason to convert it.

</details>

**Bonus:** Go back to the While Loop Challenge in chapter 5. In that version, the computer guesses its own number. Change it so that the user types each guess instead, and check each guess with `.isdigit()` before you convert it.
