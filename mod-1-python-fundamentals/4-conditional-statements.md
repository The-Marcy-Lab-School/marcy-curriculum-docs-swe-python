# 1.4 — Conditional Statements

**Table of Contents:**

- [Key Terms](#key-terms)
- [Conditional Statements](#conditional-statements)
  - [`if/elif/else` statements](#ifelifelse-statements)
  - [Order Matters](#order-matters)
  - [Only `if` statements](#only-if-statements)
  - [Guard Clauses](#guard-clauses)
  - [Truthy and Falsy Values](#truthy-and-falsy-values)
  - [Use Conditional Expressions To Simplify Conditionals](#use-conditional-expressions-to-simplify-conditionals)

## Key Terms

- **Control Flow** refers to the order in which statements of a program are executed, typically top-to-bottom.
- **Conditional statements** (`if`, `elif`, `else`) let you control the flow of your program based on data values. The order of conditions matters, and only the first true condition in a chain will execute.
- **Guard clauses** are single `if` statements that return early from a function, simplifying conditional logic.
- An `if` statement creates a **boolean context** where non-boolean values are converted to Booleans using the `bool()` function.
- Non-boolean values used in a boolean context are considered **truthy** if they evaluate to `True` or **falsy** if they evaluate to `False`. All values are truthy except for `None`, `False`, the numbers `0` and `0.0`, the empty string `""`, and empty collections such as `[]` and `{}`.
- **Conditional expressions** provide a concise way to choose between two values based on a condition.

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

### Truthy and Falsy Values

Python has a function called `bool()` that converts any value to `True` or `False`, and it is the one conditions use without being asked. Values that are "non-values" or "empty values" are considered **falsy**. All other values are **truthy**:

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

One caution. `if not value:` cannot tell `None` apart from `0` or `""`, because all three are falsy. When the question you are asking is specifically "is this `None`?", write `if value is None:`. That is what the `is` operator from chapter 1.2 is for.

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
