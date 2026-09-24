# 2. Data Types and Variables

**Table of Contents:**

- [Key Terms](#key-terms)
- [Computation is All About Data](#computation-is-all-about-data)
- [Data Types](#data-types)
- [Operators](#operators)
  - [Resolution Order of Operations](#resolution-order-of-operations)
- [Variables](#variables)
  - [Using Variables: Assign, Reassign, Reference](#using-variables-assign-reassign-reference)
  - [Naming Conventions](#naming-conventions)
- [Operators in Depth](#operators-in-depth)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Comparison (Relational) Operators](#comparison-relational-operators)
  - [Logical Operators](#logical-operators)
  - [Membership and Identity Operators](#membership-and-identity-operators)
  - [Assignment Operators](#assignment-operators)
  - [The Conditional Expression](#the-conditional-expression)

## Key Terms

- **State** refers to the data stored by a program at a point in time.
- **Data types** are categories of values in Python. There are 5 basic types (`str`, `int`, `float`, `bool`, `None`) and 3 types that hold other data or code (`list`, `dict`, and functions). Knowing the type of a value helps determines how you can use that value. Choosing the right type to represent your data is essential.
- **Operators** are symbols (e.g. `+`, `>=`, `and`) that generate new data from existing values. Arithmetic, comparison, logical, membership, identity, and assignment operators allow you to perform calculations and make decisions.
- **Variables** are named containers for data. You can reference and reassign variables to store and update information in your program.
  - A variable is created the first time it is assigned. Names in `ALL_CAPS` are a signal to readers that a value is a constant and should not be reassigned.

## Computation is All About Data

Starting from the very first computational device, the abacus, computers were designed to make it easier for humans to manipulate, generate, and visualize data.

![The abacus is the earliest known computational device](../.gitbook/assets/abacus.png)

What has changed and evolved over time is how quickly our devices can perform those calculations and how sophisticated our ability to generate and visualize data has become. Here are some modern ways that computers make use of data:

- **Rendering images & video**: Calculating pixel positions, color values, and frame rates turns raw math into Netflix streams and 3D games.
- **Navigation systems**: Continuous GPS data (latitude/longitude as numbers) is transformed into live maps, directions, and traffic updates.
- **Social media**: Posts are stored as text data, likes as counts, and relationships as graph data — powering your feed and recommendations.
- **Online shopping**: Prices (numbers), product info (strings), and cart contents (lists of dictionaries) are combined to let you browse, compare, and buy.
- **Music & audio**: Sound waves are stored as numerical data, then processed and streamed as songs, podcasts, and phone calls.
- **Healthcare & fitness apps**: Heart rate, steps, and sleep cycles (all data points) are tracked and analyzed to monitor your health.
- **Artificial intelligence**: Images, text, or speech are converted into numbers (vectors, matrices) that models process to recognize faces, generate text, or translate languages.

In this lesson, we'll learn about the different types of data, how our computers store data in variables, and then the many ways that we can compute new data.

## Data Types

All values have a **data type** that determines what you can do with that value.

For example, you can use numbers to perform mathematical calculations and can use strings to construct messages. Knowing the different data types allows you to choose the best data type for your particular use case.

In Python, there are five basic **data types** to start with: `str`, `int`, `float`, `bool`, and `None`

| Data Type   | Syntax Example           | What It Represents                | Common Use Cases                                                        |
| ----------- | ------------------------ | --------------------------------- | ----------------------------------------------------------------------- |
| **`str`**   | `"hello"` or `'@abc123'` | Text (any sequence of characters) | Usernames, chat messages, product descriptions, search queries          |
| **`int`**   | `50` or `-2`             | Whole numbers                     | Scores in a game, count of likes on a post, a task's position in a list |
| **`float`** | `10.5` or `0.99`         | Numbers with a decimal point      | Prices, averages, percentages, timers                                   |
| **`bool`**  | `True` or `False`        | Truth value                       | Login status, feature toggles (dark mode on/off), win/lose conditions   |
| **`None`**  | `None`                   | Intentional absence of a value    | Representing "no result" or "not yet set"                               |

There are also three types that hold other data or hold code: lists, dictionaries, and functions.

| Type         | Syntax Example                  | What It Represents                           | Common Use Cases                                                                         |
| ------------ | ------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **`list`**   | `["apple", "banana", "cherry"]` | An ordered list of similar values            | Storing lists (shopping cart items, game high scores, chat messages)                     |
| **`dict`**   | `{"name": "Alex", "age": 25}`   | A collection of data relating to one "thing" | Storing user profile data, storing data about product (name, description, price, etc...) |
| **function** | `def greet(): print("Hi!")`     | A reusable block of code                     | Performing actions, handling events, calculations                                        |

**Challenge:** Identify the data types of the values below:

```py
[5]
"5"
5
5.0
{ "value": 5 }
def five():
    return 5
```

**<details><summary>Q: Open up YouTube.com. What examples can you come up with for each of the data types listed above?</summary>**

Here are some examples of each of the basic data types:

- `str`: The title of a video
- `int`: The number of views on a video
- `float`: The average rating of a video, or how many seconds into it you are
- `bool`: Indicator for whether or not you have liked (or disliked) a video
- `None`: The current user (when you are logged out)

Here are some examples of each of the other three:

- `dict`: A single video with all of the related data (view count, likes, comments, etc...)
- `list`: All of the comments for a single video
- function: Clicking on the "Subscribe" button triggers some sort of "subscribe" functionality

</details>

## Operators

Each data types is a different option that a programmer has to represent information. For example, you could choose to represent the state of a light switch with the strings `"on"` and `"off"` or you could use booleans `True` and `False`.

How you make that decision almost entirely depends on the kinds of **operators** that you can use with each data type. Operators are used to create expressions that generate new data. However, you must learn how each data type interacts with each operator to avoid `TypeError`s

```python
5 + 2               # the value 7 is created
"hello" + " world"  # the value "hello world" is created

5 * 2               # the value 10 is created
"hello" * "world"   # TypeError: can't multiply sequence by non-int of type 'str'
```

In most cases, Python uses operators in ways that are predictable. Sometimes however, Python will do something unexpected. For now, you don't need to memorize all of these rules but be aware that there is a concrete and reproduce-able explanation for every unexpected behavior.

**Challenge:** Can you predict what each expression will produce? Some of these get a bit weird.

```python
# What you would expect to happen usually happens
10 + 5 * 2
"B" > "A"
2 > 1 and "B" > "A"

# Slightly unexpected results
8 / 2
"3" * 5
"5" + 5
True + True + False
[1, 2] * 2

# Huh?
0 or "Python"
0.1 + 0.2 == 0.3
[1, 2] == [1, 2]
[1, 2] is [1, 2]
```

{% hint style="info" %}
The fastest way to check a prediction like these is the **Python REPL**. Run `python3` in the Terminal with no file after it, and you get a prompt that evaluates one expression at a time and prints the result. Type `exit()` to leave.

![The Python REPL is useful for testing out expressions.](../.gitbook/assets/1-python-repl-expressions.png)
{% endhint %}

**<details><summary>Answers</summary>**

```python
10 + 5 * 2
# Result: 20
# Why: Multiplication comes first, then addition -> 10 + (5 * 2)

"B" > "A"
# Result: True
# Why: Alphabetically, B comes after A

2 > 1 and "B" > "A"
# Result: True
# Why: Both expressions `2 > 1` and `"B" > "A"` are True

8 / 2
# Result: 4.0 (not 4)
# Why: `/` always returns a float. Use `//` if you want an integer

"3" * 5
# Result: "33333"
# Why: Multiplying a string by an integer repeats the string

"5" + 5
# Result: TypeError
# Why: Some operations you simply can't perform. In this case, you can't add different types.

True + True + False
# Result: 2
# Why: In Python, True evaluates to 1 and False evaluates to 0 in arithmetic contexts

[1, 2] * 2
# Result: [1, 2, 1, 2]
# Why: Like the "3" * 5 example, a list is repeated when multiplied by an integer

0 or "Python"
# Result: "Python"
# Why: `or` treats 0 as False and hands back the other value. Chapter 4 explains which values count as false.

0.1 + 0.2 == 0.3
# Result: False
# Why: A classic computer science trap. Due to how floating-point numbers are represented in binary (base-2), 0.1 + 0.2 actually evaluates to 0.30000000000000004, making the equality check fail.

[1, 2] == [1, 2]
# Result: True
# Why: Both lists hold equal values

[1, 2] is [1, 2]
# Result: False
# Why: `is` checks for identity equality, not value equality. While they both contain the same values, Python creates two distinct list objects in memory.
```

</details>

### Resolution Order of Operations

Operators can be combined to form complex expressions. In these cases, understanding the order in which operators are evaluated — also called **operator precedence** — is crucial.

Chapter 1 had an example of getting it wrong. This code is meant to convert 212°F to 100°C:

```python
fahrenheit = 212
celsius = fahrenheit - 32 * 5 / 9
print(celsius)  # 194.22222222222223
```

Below is the order of precedence:

1. Anything inside parentheses `()` is evaluated first, then function calls
2. Then arithmetic operators. `**` is evaluated before `*`, `/`, `//`, `%`, which are evaluated before `+` and `-`. Operators at the same level are evaluated left to right.
3. Followed by comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`).
4. Then logical operators. `not` is evaluated first, then `and`, then `or`.
5. The conditional expression (`x if condition else y`) and assignment happen last (`=`)

Parentheses `()` can always be used to override the default order and make the evaluation order explicit:

```python
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)  # 100.0
```

**<details><summary>Q: Walk through both versions one operator at a time. At which operation do they differ?</summary>**

Without parentheses:

1. `32 * 5` resolves to `160`, because `*` comes before `-`.
2. `160 / 9` resolves to `17.777...`, because `/` is at the same level as `*` and comes next, left to right.
3. `212 - 17.777...` resolves to `194.222...`.
4. `celsius = 194.222...` assigns the result.

With parentheses:

1. `(212 - 32)` resolves to `180`, because parentheses go first.
2. `180 * 5` resolves to `900`.
3. `900 / 9` resolves to `100.0`.
4. `celsius = 100.0` assigns the result.

They differ right at step 1. Everything after that is downstream of which operator got to go first.

</details>

The same rules decide how a comparison and a conditional expression fit together. What is the value of `report`?

```python
temperature = 85
report = "hot" if temperature - 10 > 70 else "mild"
```

**<details><summary>Q: So, what is the order of operations? What is the value stored in report?</summary>**

1. `temperature - 10` resolves to `75`, because arithmetic comes before comparison.
2. `75 > 70` resolves to `True`.
3. `"hot" if True else "mild"` resolves to `"hot"`.
4. `report = "hot"` assigns the result.

If arithmetic did _not_ come before comparison, Python would have read it as `temperature - (10 > 70)`, which is `85 - False`, which is `85`, and then `"hot" if 85 else "mild"`. That gives the same answer here by luck, and a different one for other temperatures. Knowing the order is what lets you predict the result instead of hoping.

</details>

**Challenge**: what values are produced by the code snippet below?

```python
# Arithmetic
print(5 + 2 * 3)
print((5 + 2) * 3)
print(2 ** 3 * 2)
print(10 - 2 - 3)

# Comparison
print(5 + 2 > 6)
print(5 + (2 > 6))

# Logical
print(True or False and False)
print((True or False) and False)

# Combined
print(5 > 3 and 2 + 2 == 4)
print((5 > 3 and 2 + 2) == 4)
print("even" if 7 % 2 == 0 else "odd")
```

**<details><summary>Answers</summary>**

```python
# Arithmetic
print(5 + 2 * 3)       # 11 -> Multiplication before addition
print((5 + 2) * 3)     # 21 -> Parentheses override precedence
print(2 ** 3 * 2)      # 16 -> Exponentiation before multiplication: (2 ** 3) * 2
print(10 - 2 - 3)      # 5 -> Same level, left to right: (10 - 2) - 3

# Comparison
print(5 + 2 > 6)       # True -> Addition happens before comparison
print(5 + (2 > 6))     # 5 -> Comparison happens first due to parentheses. False counts as 0 in arithmetic.

# Logical
print(True or False and False)     # True -> and has higher precedence than or
print((True or False) and False)   # False -> Parentheses change the evaluation order

# Combined
print(5 > 3 and 2 + 2 == 4)        # True -> Arithmetic and comparison combined with logical
print((5 > 3 and 2 + 2) == 4)      # True -> `True and 4` produces 4, and 4 == 4
print("even" if 7 % 2 == 0 else "odd")  # odd -> % first, then ==, then the conditional expression chooses
```

</details>

## Variables

A **Variable** is a named container for data. By labeling our data, variables enable us to perform a series of computations in a program and "save" our progress along the way. Descriptive variable names dramatically improve the readability of our code.

Consider the two approaches below to produce the same result. The first does not use variables while the second does. What are the tradeoffs of each approach?

**Approach 1: No Variables**

```python
print(f"The sum of 4 + 3 + 2 + 1 is {4 + 3 + 2 + 1} and the average is {(4 + 3 + 2 + 1) / 4}")
# Output: The sum of 4 + 3 + 2 + 1 is 10 and the average is 2.5
```

**Approach 2: Variables**

```python
sum = 4 + 3 + 2 + 1
average = sum / 4
message = f"The sum of 4 + 3 + 2 + 1 is {sum} and the average is {average}"
print(message)
# Output: The sum of 4 + 3 + 2 + 1 is 10 and the average is 2.5
```

**<details><summary>Tradeoffs of each approach</summary>**

The first approach can be written in one line, however, it is very long. This makes it more difficult to read and predict the output. Additionally the `4 + 3 + 2 + 1` expression must be calculated twice since that calculation is not saved anywhere.

With variables, each expression is nicely labeled for readability and comprehension. Additionally, the calculation for the sum is stored in the `sum` variable allowing us to use it to calculate the `average` and to help construct the `message`. However, more lines of code are used.

In most cases, the benefits of readability, comprehension, and minimizing repetition outweigh the extra space taken up in a file.

</details>

### Using Variables: Assign, Reassign, Reference

There are three things we can do with variables, each with "technical" language that we use to talk about them:

1. Create a new variable by giving it a value ("**assign** the variable a value").
2. Give the variable a new value to hold ("**reassign** the variable")
3. Use the value held by the variable ("**reference** the variable")

```python
# Create the variable count and assign it the value 0
count = 0

# Reference the count variable to access its current value, 0
print(f"count starts at {count}")

# Reassign the variable to hold a new value: 1
count = 1

# Reference the count variable again to access its current value, 1
print(f"count is now {count}")
```

We can even reference the _current_ value of a variable to _reassign_ it a new value:

```python
# The right side (count + 1) resolves before the assignment. count becomes 2
count = count + 1

# += is an "augmented assignment" operator. It is the same as `count = count + 1`. count becomes 3
count += 1

# It works with any amount. count becomes 6
count += 3

# You can use every other arithmetic operator with =. count becomes 12
count *= 2

print(f"count is now {count}")  # Output: count is now 12
```

**Predict, then Run**: What is the output of the code below?

```py
msg = 'hello'
msg += 'world' + '!' * 3
print(msg)
```

**<details><summary>Answer</summary>**

```
helloworld!!!
```

Be careful about adding strings together. If you don't put a space in between the words, then the words will be combined directly!

The entire statement gets evaluated in this order:

1. `'!' * 3` evaluates to `'!!!'`
2. `'world' + '!!!'` evaluates to `'world!!!'`
3. `msg += 'world!!!'` reassigns `msg` to `'helloworld!!!'`

</details>

### Naming Conventions

Variables should be named using `lower_underscore_case` and describe the data they hold for the best readability

```py
# Bad: Unclear what the data is
numbers = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Good: easy to understand the data in the variable
days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Bad: descriptive but difficult to read
daysineachmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Not Pythonic: readable but not conventional in Python
daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

A global variable whose value should never change is written in `ALL_CAPS`, and every Python programmer reads that as "do not reassign me". It is just a convention, so it is still possible to reassign them.

```python
# Good: a constant. The name tells the reader it will never change.
MAX_GUESSES = 5

# This is still possible though so always be careful!
MAX_GUESSES = 10
```

## Operators in Depth

### Arithmetic Operators

**Arithmetic Operators**: Perform standard mathematical calculations (such as addition, subtraction, division, and exponentiation) or sequence manipulation like string concatenation and list repetition.

| Operator | Name                        | Compatible Data Types                                         | Behavior & Notes                                                                                                          |
| -------- | --------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `+`      | Addition / Concatenation    | `int`, `float`, `str`, `list`                                 | Numerics: Adds values.<br> <br>Sequences: Concatenates two sequence instances of the **same type**.                       |
| `-`      | Subtraction / Difference    | `int`, `float`                                                | Numerics: Subtracts right operand from left.                                                                              |
| `*`      | Multiplication / Repetition | Numerics: (`int`, `float`)<br> <br>Sequences: (`str`, `list`) | Numerics: Multiplies values.<br><br>Sequences: Multiplies sequence by an `int` to repeat it.                              |
| `/`      | Division                    | `int`, `float`                                                | Always returns a `float`, even if dividing two integers.                                                                  |
| `//`     | Floor Division              | `int`, `float`                                                | Divides and rounds down to nearest integer. Returns `int` if both inputs are `int`; returns `float` if either is `float`. |
| `%`      | Modulus                     | `int`, `float`                                                | Returns the remainder of division.                                                                                        |
| `**`     | Exponentiation              | `int`, `float`                                                | Raises left operand to the power of the right operand.                                                                    |

**Examples**:

```py
5 + 3           # 8
"a" + "b"       # "ab"
10 - 4          # 6
4 * 2.5         # 10.0
"hi" * 3        # "hihihi"
7 / 2           # 3.5
4 / 2           # 2.0
7 // 2          # 3
7.0 // 2        # 3.0
7 % 2           # 1
2 ** 3          # 8
```

---

### Comparison (Relational) Operators

**Comparison (Relational) Operators**: Compare two values—checking for equality, inequality, or relative order—and return a Boolean value (`True` or `False`).

| Operator | Description              | Compatible Data Types         | Behavior & Notes                                                                                                  |
| -------- | ------------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `==`     | Equal to                 | All data types                | Evaluates whether value contents are equal.                                                                       |
| `!=`     | Not equal to             | All data types                | Evaluates whether value contents are not equal.                                                                   |
| `<`      | Less than                | `int`, `float`, `str`, `list` | Numerics: Value comparison.<br> <br>Strings: Lexicographical order.<br> <br>Lists: Element-by-element comparison. |
| `>`      | Greater than             | `int`, `float`, `str`, `list` | Numerics/Strings/Sequences: Ordering test.                                                                        |
| `<=`     | Less than or equal to    | `int`, `float`, `str`, `list` | Numerics/Strings/Sequences: Ordering test.                                                                        |
| `>=`     | Greater than or equal to | `int`, `float`, `str`, `list` | Numerics/Strings/Sequences: Ordering test.                                                                        |

_Note: Comparing incompatible types (e.g., `5 < "hello"`) raises a `TypeError` in Python 3._

**Examples**:

```py
5 == 5              # True
"a" != "b"          # True
3 < 5               # True
10 > 2              # True
[1, 2] <= [1, 2]    # True
5.0 >= 5            # True
5 < "hello"         # TypeError
```

---

### Logical Operators

**Logical Operators**: Combine boolean values (`and`, `or`, `not`) into a single `True` or `False`.

| Operator | Description | Compatible Data Types | Behavior & Return Value                        |
| -------- | ----------- | --------------------- | ---------------------------------------------- |
| `and`    | Logical AND | `bool`                | `True` only if both sides are `True`.          |
| `or`     | Logical OR  | `bool`                | `True` if either side is `True`.               |
| `not`    | Logical NOT | `bool`                | Flips `True` to `False` and `False` to `True`. |

**Examples**:

```py
True and False      # False
True or False       # True
not True            # False
5 > 3 and 2 > 1     # True
```

In chapter 4 you will learn that `and` and `or` also accept values that are not booleans, using a rule called truthiness. That is what the `[] or "Python"` line in the challenge above was doing.

---

### Membership and Identity Operators

**Membership and Identity Operators**: Membership operators (`in`, `not in`) test whether a value exists inside a sequence or container; identity operators (`is`, `is not`) test whether two names refer to the very same object.

| Operator | Name               | Compatible Data Types                 | Behavior & Notes                                                                                                                   |
| -------- | ------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `in`     | Membership Test    | Any iterable (`str`, `list`, `dict`,) | Checks if value exists in sequence/container. For `dict`, checks **keys**.                                                         |
| `not in` | Negated Membership | Any iterable                          | Checks if value does not exist in sequence/container.                                                                              |
| `is`     | Identity Test      | All data types                        | `True` if both sides are the very same object, not just equal ones. Used mostly as `x is None`. Chapter 8 explains the difference. |
| `is not` | Negated Identity   | All data types                        | The opposite of `is`.                                                                                                              |

**Examples**:

```py
'a' in 'apple'    # True
'x' in {'x': 1}   # True
3 not in [1, 2]   # True
x is None         # True
a is not b        # True
```

---

### Assignment Operators

**Assignment Operators**: Assign values to variables (`=`) or update a variable's existing value by combining an operation with assignment (such as `+=` or `-=`).

| Operator                                   | Name                 | Compatible Data Types         | Behavior & Notes                                                    |
| ------------------------------------------ | -------------------- | ----------------------------- | ------------------------------------------------------------------- |
| `=`                                        | Simple Assignment    | All data types                | Binds a value to a variable name.                                   |
| `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` | Augmented Assignment | `int`, `float`, `str`, `list` | Evaluates the operation and stores the result back in the variable. |

**Examples:**

```py
x = 10                      # Simple assignment
x += 5                      # Augmented assignment (add 5 to x and re-bind)
```

### The Conditional Expression

The **conditional expression** is best seen and then explained:

```python
print("it is even!" if 5 % 2 == 0 else "it is odd!") # prints "it is odd" because 5 % 2 has a remainder of 1, not 0
```

`val_a if bool_expression else val_b` produces one of two values based on the `bool_expression` value:

- `val_a` is produced if the `bool_expression` evaluates to `True`
- `val_b` is produced if the `bool_expression` evaluates to `False`
