# 1.4 Conditional Statements

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/04-conditional-statements/)
{% endhint %}

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

To define the possible decisions that our program can make, we use `if`, `elif`, and `else` statements.

For example, this function uses these statements to print a message

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

- The condition after `if` or `elif` is usually a comparison like `temp > 100`. The code block under it runs only when the condition is `True`.
- `elif` is short for "else if" and only runs if the previous conditions were `False` _and_ its own condition is `True`
- There can be many `elif` statements, or none at all.
- `else` statements do not require a condition and will run only when none of the other options do.

### Order Matters

Python checks the conditions from top to bottom and runs the code block under the first condition that is `True`. As soon as one block runs, Python skips every remaining `elif` and `else` without checking them. So if a broad condition like `temp > 75` comes first, it catches 95 and 105 too, and the narrower conditions below it never get a turn.

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

When a function returns a different value depending on a condition, you can replace the `elif`/`else` chain with plain `if` statements. This works because a `return` statement ends the function the moment it runs. Once one `if` returns, none of the lines below it get a chance to run. An `if` statement used this way is called a **guard clause**.

Return the statements to the original order and replace each `print()` call with a `return` statement:

```python
def is_it_hot(temp):
    if temp > 100:
        return "So Hot!"
    if temp > 90:
        return "Yes!"
    if temp > 75:
        return "Eh"
    return "Nah"

print(is_it_hot(105))
# Output: ???
```

**<details><summary>Answer</summary>**

It prints `So Hot!`. `105 > 100` is `True`, so the first guard clause returns `"So Hot!"` before `temp > 90` and `temp > 75` are ever checked.

Order matters for guard clauses just as it does for an `elif` chain. Start with the narrowest condition first, then move on to less restrictive conditions.
</details>

**<details><summary>Q: Why doesn't the last return statement need an `if` statement?</summary>**

A `return` statement ends the function the moment it runs, so the program only reaches the last line when every `if` above it was `False`. If `temp > 75` was `False`, the temperature must be 75 or less. An `if temp <= 75:` on that line would check a condition that can only ever be `True`, so you can leave it off and just `return "Nah"`.

</details>

### Truthy and Falsy Values

Python has a function called `bool()` that converts any value to `True` or `False`. An `if` statement calls `bool()` on its condition for you whenever the condition is not already a boolean. Values that are "non-values" or "empty values" are considered **falsy**. All other values are **truthy**:

```python
print(bool(0))         # -> False
print(bool(""))        # -> False
print(bool(None))      # -> False
print(bool([]))        # -> False (an empty list)
print(bool(100))       # -> True
print(bool("hello"))   # -> True
```

Because an `if` calls `bool()` for you, `if not friend:` does the same job as `if friend == "":`, in fewer characters:

```python
def greet_friend(friend):
    if not friend:
        return "I can't say hi if I don't know your name!"
    return f"Hi, {friend}! Nice to meet you."

print(greet_friend(""))      # Output: I can't say hi if I don't know your name!
print(greet_friend("Jane"))  # Output: Hi, Jane! Nice to meet you.
```

When `friend` is the empty string, `bool("")` is `False`, and `not` flips `False` to `True`. So `not friend` is `True`, and the guard clause returns the message. You will see this pattern, `if not my_variable:`, in nearly every program that takes input.

One caution. `if not value:` cannot tell `None` apart from `0` or `""`, because all three are falsy. Suppose `score` is `None` until a player finishes a game. A player who finishes with a score of `0` also makes `not score` evaluate to `True`, and your program would treat that player as if they had never played. When the question you are asking is specifically "is this `None`?", write `if score is None:`. That is what the `is` operator from chapter 1.2 is for.

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

`"False"` is a string with five characters in it, and a non-empty string is truthy. What the characters spell has nothing to do with it. Only the boolean `False`, the number `0`, `None`, and empty things like `""` are falsy.

</details>

{% endhint %}

This mistake often occurs when using user input (e.g. from the `input()` function) in a condition. You must remember that the user typed a string. A user who types `no` or `False` still gives you a non-empty string, so `if answer:` runs the `True` branch for them.

```py
answer = input("Yes or No?")
if answer:
    print("they said yes!")
else:
    print(":(")
```

Compare the string itself instead: `if answer == "Yes":`.

```py
answer = input("Yes or No?")
if answer == "Yes":
    print("they said yes!")
else:
    print(":(")
```

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

Both versions print the same message. The conditional expression is easier to read because `message` is assigned on one line, with both possible values side by side. A reader does not have to scan two branches to find out what `message` can hold.
