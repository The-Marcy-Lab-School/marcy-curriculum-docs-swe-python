# 1.13 — Comprehensions and Built-in Iteration

**Table of Contents**

- [Key Terms](#key-terms)
- [Imperative vs. Declarative Code: Why We Use Built-in Iteration](#imperative-vs-declarative-code-why-we-use-built-in-iteration)
- [The Toolkit](#the-toolkit)
  - [Transforming with List Comprehensions](#transforming-with-list-comprehensions)
  - [Filtering with an `if`](#filtering-with-an-if)
  - [Finding the First Match](#finding-the-first-match)
  - [Combining Into One Value](#combining-into-one-value)
  - [Sorting with `sorted()` and `.sort()`](#sorting-with-sorted-and-sort)
- [Tips and Tricks](#tips-and-tricks)
  - [Combining Steps](#combining-steps)
  - [Generating a Frequency Counter](#generating-a-frequency-counter)
  - [Nested Lists](#nested-lists)
  - [`zip()`, `any()`, and `all()`](#zip-any-and-all)
- [Refactoring with Tests](#refactoring-with-tests)
  - [A Pure Function and Its Tests](#a-pure-function-and-its-tests)
  - [Refactor with Confidence](#refactor-with-confidence)
- [Test-Driven Development](#test-driven-development)
  - [Step 1: Define New Requirements](#step-1-define-new-requirements)
  - [Step 2: Write Tests Before Code (They Will Fail)](#step-2-write-tests-before-code-they-will-fail)
  - [Step 3: Implement Just Enough Code to Pass](#step-3-implement-just-enough-code-to-pass)
  - [Reflection](#reflection)
- [Banking System Challenge](#banking-system-challenge)
- [Extension / Practice](#extension--practice)

## Key Terms

- **List comprehensions** provide declarative ways to build new lists from existing ones, making code more readable and reducing the need for explicit loops.
- `[expression for item in items]` **transforms** each element and returns a new list with the transformed values, useful for converting data formats or applying calculations.
- `[item for item in items if test]` **filters**, creating a new list containing only elements that pass a test condition.
- A **dictionary comprehension**, `{key: value for item in items}`, builds a new dictionary the same way a list comprehension builds a new list.
- Finding the **first** element that passes a test is a `for` loop with an early `return` or `break`.
- **`sum()`**, **`min()`**, **`max()`**, and **`len()`** combine a whole list into a single value. When none of them fits, the **accumulator pattern** does: start a variable, update it in a loop, return it.
- **`sorted()`** returns a new sorted list and **`.sort()`** sorts a list in place. Both take a `key` callback that says what to compare and `reverse=True` for descending order.
- **`enumerate()`**, **`zip()`**, **`any()`**, and **`all()`** cover the other everyday loop shapes without an index in sight.
- **`==`** compares the contents of two values. **`is`** and **`is not`** compare identity: whether two names refer to the very same object. A test for a **pure function** uses `==` to check the returned contents and `is not` to check that a new list came back rather than the original.
- To **refactor** is to change how code works without changing what it does. Passing tests are what let you refactor with confidence, for example from a `for` loop to a list comprehension.
- **Test-driven development (TDD)** is a workflow that writes the test first, watches it fail (**red**), writes just enough code to pass (**green**), and then refactors while the tests stay green.
- **`isinstance(value, type)`** asks whether a value is of a given type, and accepts a tuple of types.

## Imperative vs. Declarative Code: Why We Use Built-in Iteration

What is the value of these tools? They allow us to write our code in a more _declarative_ manner rather than in an _imperative_ manner.

**Imperative code** provides explicit instructions for every step to complete a task. This gives us a lot of control over every step, but it takes more effort.

**Declarative code** just describes the desired solution and uses existing tools to handle the steps. While we give up control to the existing tool, we save time and effort.

For example, suppose we want to double every value in a list. We can either write out every single step imperatively, or we can declaratively describe the desired outcome using a list comprehension

```python
# Imperative: High Control & High Effort:
nums = [1, 5, 10, 20]

def double_all_nums(items):
    new_items = []
    for num in items:
        result = num * 2
        new_items.append(result)
    return new_items

doubled_imperatively = double_all_nums(nums)
print(doubled_imperatively)

# Declarative: Low Control & Low Effort:
doubled_declaratively = [num * 2 for num in nums]
print(doubled_declaratively)
```

Let's look at how we can use Python's built-in iteration tools to write more declarative code.

## The Toolkit

Here are the most common things you want to do with a list, and the Python tool for each:

| You want to...                                              | Use                                                        | Example                                       |
| ----------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------- |
| Perform a task that produces a side effect for every value  | a `for` loop                                               | Print each value, or mutate each dictionary   |
| Transform every value and collect the results in a new list | a list comprehension                                       | Double every number in the source list        |
| Test every value and keep the ones that pass                | a list comprehension with `if`                             | Keep only the even numbers in the source list |
| Test every value and get the first one that passes          | a `for` loop with `return`/`break`                         | Find the first number greater than 10         |
| Combine every value into one                                | `sum()`, `min()`, `max()`, `len()`, or an accumulator loop | Calculate the sum of all numbers              |
| Compare values to put them in order                         | `sorted()` or `.sort()`                                    | Sort a list of numbers in descending order    |

### Transforming with List Comprehensions

A list comprehension builds a new list by evaluating an expression once for every element of a source list. The value of the expression is added to the new list.

```python
[expression for item in source_list]
```

Use it when you want a copy of the source list with each value converted to a new value.

**Example:** In this example, we have a list `inches_list` containing values each representing a number of inches. Using a comprehension, we transform each `inches` value into a string in the format `x inches => y feet z inches`. Each of these new strings is added to the list stored in `feet_and_inches`:

{% code title="transform.py" %}

```python
inches_list = [70, 55, 62, 12, 36]

# This example converts inches to feet and inches strings
def get_feet_and_inches_str(inches):
    feet = inches // 12
    remaining_inches = inches % 12
    return f"{inches} inches => {feet} feet {remaining_inches} inches"

feet_and_inches = [get_feet_and_inches_str(inches) for inches in inches_list]
print(feet_and_inches)
```

{% endcode %}

Read a comprehension from the `for` outward: "for each `inches` in `inches_list`, compute `get_feet_and_inches_str(inches)` and collect it." The new list always has exactly as many elements as the source.

**Challenge:** In this example, we have a `users` list full of user dictionaries. Write a comprehension that extracts all of the usernames into a new list:

{% code title="transform.py" %}

```python
users = [
    {'id': 1, 'username': 'ben', 'is_admin': False},
    {'id': 2, 'username': 'maya', 'is_admin': True},
    {'id': 3, 'username': 'reuben', 'is_admin': True},
    {'id': 4, 'username': 'gonzalo', 'is_admin': False},
]
usernames = [??? for user in users]
```

{% endcode %}

**<details><summary>Solution</summary>**

```python
usernames = [user['username'] for user in users]
```

</details>

### Filtering with an `if`

Adding an `if` to the end of a comprehension keeps only the elements for which the test is `True`.

```python
[item for item in source_list if test]
```

Use it when you want a copy of the source list with unwanted values removed.

**Example:** In this example, we want to know how many scores in a list of numbers are greater than or equal to 75. Using a comprehension with an `if`, we can get a copy of the list containing only those passing scores and then read its length.

{% code title="filter.py" %}

```python
scores = [100, 85, 90, 70, 74]

# This is a copy of scores that has been filtered.
passing_scores = [score for score in scores if score >= 75]

# Using its length, we can get the number of passing scores
print(f"There were {len(passing_scores)} passing scores")
```

{% endcode %}

Notice that the expression before the `for` is just `score`. Filtering keeps values as they are. You can transform _and_ filter in one comprehension by changing that expression, and the result can be shorter than the source.

**Challenge:** In this example, we have a list of user dictionaries. We want to get a copy of the list that only contains admins.

Use a comprehension with an `if` to check each dictionary and keep only those with `'is_admin': True`.

{% code title="filter.py" %}

```python
users = [
    {'id': 1, 'username': 'ben', 'is_admin': False},
    {'id': 2, 'username': 'maya', 'is_admin': True},
    {'id': 3, 'username': 'reuben', 'is_admin': True},
    {'id': 4, 'username': 'gonzalo', 'is_admin': False},
]

admins = [??? for user in users if ???]

print(admins)
# [
#   {'id': 2, 'username': 'maya', 'is_admin': True},
#   {'id': 3, 'username': 'reuben', 'is_admin': True},
# ]
```

{% endcode %}

**<details><summary>Solution</summary>**

```python
admins = [user for user in users if user['is_admin']]
```

`user['is_admin'] == True` works too, but a boolean is already a boolean, so the comparison adds nothing.

</details>

### Finding the First Match

While a filtering comprehension is used to get ALL values that pass a test, sometimes you only want the first one. The plain way is a `for` loop that leaves as soon as it finds it:

```python
def find_first_odd(nums):
    for num in nums:
        if num % 2 == 1:
            return num
    return None  # nothing passed the test

def find_first_odd_index(nums):
    for index, num in enumerate(nums):
        if num % 2 == 1:
            return index
    return -1
```

`return` inside the loop is what makes this "first": the loop stops at the first success and never looks at the rest. The line after the loop handles the case where nothing matched. Decide what that case should return before you write the function, because callers will need to check for it.

### Combining Into One Value

Python has built-in functions for the most common ways to boil a list down to a single value:

```python
lunch_costs = [5, 10, 7, 9, 15, 8, 12]

print(sum(lunch_costs))   # 66
print(min(lunch_costs))   # 5
print(max(lunch_costs))   # 15
print(len(lunch_costs))   # 7
print(sum(lunch_costs) / len(lunch_costs))  # 9.428571428571429, the average
```

When none of them does what you want, the general shape is the **accumulator pattern**: create a variable holding a starting value, update it once per element, and return it when the loop ends.

```python
def total(costs):
    running_total = 0          # the starting value
    for cost in costs:
        running_total += cost  # combine the current value into the total so far
    return running_total       # the final accumulated value

print(total(lunch_costs))  # 66
```

`sum()` is exactly this loop with `0` as the starting value and `+` as the combining step. The pattern matters because the starting value and the combining step can be anything, which is what the frequency counter below does with a dictionary.

### Sorting with `sorted()` and `.sort()`

Given a list of numbers, `sorted()` returns a new list with them in ascending order, from smallest to largest. The source list is untouched:

```python
nums = [4, 2, 3, 5, 1]
ordered = sorted(nums)
print(ordered)  # [1, 2, 3, 4, 5]
print(nums)     # [4, 2, 3, 5, 1]
```

The list method `.sort()` does the same thing **in place** which means that the source list is modified and nothing is returned:

```python
nums = [4, 2, 3, 5, 1]
nums.sort()      # sorts nums "in place"
print(nums)      # [1, 2, 3, 4, 5]
```

{% hint style="warning" %}
**Predict, then run.**

```python
nums = [4, 2, 3, 5, 1]
result = nums.sort()
print(result)
```

<details><summary>What actually happens</summary>

It prints `None`.

`.sort()` changes `nums` and returns nothing, so `result` gets `None`. This is one of the most common mistakes in Python: writing `x = my_list.sort()` and then wondering where the list went. If you want the sorted list as a value, use `sorted(nums)`. If you want to reorder `nums` itself, call `nums.sort()` on its own line and don't assign it to anything.

The same rule applies to `.append()`, `.reverse()`, and every other method that mutates a list in place: they return `None`.

</details>
{% endhint %}

Both take the same two optional keyword arguments. `reverse=True` gives descending order, and `key` takes a callback, as you saw in the last chapter, that says what to compare:

```python
nums = [4, 2, 3, 5, 1]
print(sorted(nums, reverse=True))   # [5, 4, 3, 2, 1]

animals = ['aardvark', 'bear', 'cheetah', 'deer']
print(sorted(animals, key=len))     # ['bear', 'deer', 'cheetah', 'aardvark']
```

`key` is called once per element, and the elements are ordered by what it returns. It never changes the elements themselves; `sorted(animals, key=len)` still returns the animal names, not their lengths.

**Challenge**

Sort this list of user dictionaries by age, youngest first, and then by username alphabetically.

```python
users = [
    {'username': 'ben', 'age': 30},
    {'username': 'maya', 'age': 25},
    {'username': 'reuben', 'age': 41},
    {'username': 'gonzalo', 'age': 25},
]
```

**<details><summary>Solution</summary>**

```python
by_age = sorted(users, key=lambda user: user['age'])

by_name = sorted(users, key=lambda user: user['username'])
```

The `key` callback receives one dictionary at a time and returns the value to sort by. Dictionaries have no natural order, so `sorted(users)` with no `key` would raise a `TypeError`.

</details>

## Tips and Tricks

### Combining Steps

Because each of these tools takes a list and gives back a list (or a value), the output of one can feed straight into the next. Name the intermediate steps when it helps the reader:

```python
my_nums = [1, 2, 3, 4, 5]

tripled = [num * 3 for num in my_nums]                  # multiply by 3
big_ones = [num for num in tripled if num > 12]          # keep the numbers bigger than 12
number_of_values_bigger_than_12_when_tripled = len(big_ones)  # count how many there are

print(number_of_values_bigger_than_12_when_tripled)
# 1
```

Or fold the transform and the filter into one comprehension, which is fine while it stays readable:

```python
print(len([num * 3 for num in my_nums if num * 3 > 12]))
# 1
```

### Generating a Frequency Counter

Counting how many times each value appears is the accumulator pattern with a dictionary as the accumulator. The `.get(key, 0)` from chapter 1.8 is what makes it short:

```python
repeaters = [1, 2, 4, 2, 3, 1, 4, 6, 2]

# The starting value here is an empty {}
frequencies = {}
for num in repeaters:
    frequencies[num] = frequencies.get(num, 0) + 1

print('frequencies', frequencies)
# frequencies {1: 2, 2: 3, 4: 2, 3: 1, 6: 1}
```

{% hint style="info" %}
This is so common that the standard library has it built in: `from collections import Counter` and then `Counter(repeaters)` gives you a dictionary-like object with the same counts. Knowing the loop is what lets you recognize what `Counter` is doing.
{% endhint %}

### Nested Lists

```python
# Nested list
smiley_face = [
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '*', '-', '*', '-', '-'],
    ['-', '-', '-', '*', '-', '-', '-'],
    ['-', '*', '-', '-', '-', '*', '-'],
    ['-', '-', '*', '*', '*', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
]

# We can nest the loops
for row_number, row in enumerate(smiley_face):
    line = f"{row_number}: "
    for cell in row:
        line += cell
    print(line)

# Or join each row's cells into one string
for row_number, row in enumerate(smiley_face):
    print(f"{row_number}: {''.join(row)}")
```

### `zip()`, `any()`, and `all()`

Three more built-ins that replace common loops:

```python
names = ['ben', 'maya', 'reuben']
ages = [30, 25, 41]

# zip walks two lists in step, pairing up elements by position
for name, age in zip(names, ages):
    print(f"{name} is {age}")

scores = [100, 85, 90, 70, 74]

# any: did at least one pass?  all: did every one pass?
print(any([score >= 90 for score in scores]))  # True
print(all([score >= 75 for score in scores]))  # False
```

{% hint style="info" %}
The same syntax with curly braces and a `key: value` expression builds a dictionary: `{user['id']: user['username'] for user in users}` produces `{1: 'ben', 2: 'maya'}`. You will not need it often in this module, but you will recognize it when you see it.
{% endhint %}

{% hint style="info" %}
Python also has built-in functions called `map()` and `filter()` that take a callback and a list, exactly like the higher-order functions in the last chapter. They work, and you will see them, but Python programmers overwhelmingly prefer comprehensions for the same jobs because the expression is right there instead of hidden inside a callback. Recognize `map` and `filter`; write comprehensions.
{% endhint %}

## Refactoring with Tests

Every comprehension in this chapter replaced a loop that already worked. How do you know the comprehension does _exactly_ what the loop did? You could run both and compare the output by eye, but you already have a better tool: the `pytest` tests from chapter 1.9.

### A Pure Function and Its Tests

Consider this pure function that takes in a list of numbers and returns a copy of that list where each value is doubled:

```python
def double_all_purely(items):
    doubled = list(items)
    for i in range(len(doubled)):
        doubled[i] *= 2
    return doubled
```

**<details><summary>Q: Imagine you were given this function and asked to verify that it works. How would you test it? What do you expect to happen when testing?</summary>**

To test this manually, you could invoke the function with some sample data and see if the _output_ matches what you _expect_.

```python
nums = [1, 2, 3, 4]

copy_of_nums = double_all_purely(nums)

print(nums)
print(copy_of_nums)
```

`nums` should not be mutated and `copy_of_nums` should contain all of the values doubled. We would expect to see:

```
[1, 2, 3, 4]
[2, 4, 6, 8]
```

</details>

In the `9-testing` project from chapter 1.9, put this function in a new file, `src/double_all.py`, and create `tests/test_double_all.py`.

Since we are now working with a mutable type (a list), we need to test two different things: that the _contents_ are right, and that the function gave us a _new_ list rather than the one we passed in.

```python
from src.double_all import double_all_purely


def test_double_all_purely():
    """double_all_purely - doubles each value in the list"""
    # == compares the contents of lists and dictionaries
    assert double_all_purely([1, 2, 3, 4]) == [2, 4, 6, 8]


def test_double_all_purely_does_not_mutate():
    """double_all_purely - returns a new list and leaves the original alone"""
    original = [1, 2, 3, 4]
    copy = double_all_purely(original)

    # A new list should be returned, not the original
    assert copy is not original

    # The copy should be doubled
    assert copy == [2, 4, 6, 8]

    # The original should not be mutated
    assert original == [1, 2, 3, 4]
```

This example demonstrates a few new details about `assert` statements.

- `==` compares the contents of lists and dictionaries, element by element. Two different lists with the same values are `==`.
- `is` compares identity: whether two variables reference the very same object, as you saw with `id()` in chapter 1.7. `is not` is its opposite.
- `assert` accepts any expression that produces a boolean, so `not`, `in`, `<`, and every other operator you know work inside it.

### Refactor with Confidence

Now that we have passing tests, we can change _how_ the code works — as long as it keeps passing the same tests.

**<details><summary>Challenge: Refactor `double_all_purely` to use a list comprehension</summary>**

```python
def double_all_purely(items):
    return [num * 2 for num in items]
```

</details>

Run `python3 -m pytest tests/test_double_all.py` again: the tests should still pass. (Giving pytest a file path runs only that file.)

## Test-Driven Development

So far we've been looking at tests _after_ we have already written the code. The tests just tell us whether the code we've already written works as expected.

**Test-driven development** is a workflow for creating software that starts with tests and then uses those tests as a guide for what code to write. Test driven development has a number of benefits:

- **Clear Requirements** - Writing tests first forces you to clearly define what your code should do before writing it
- **Better Design** - Starting with tests helps you design cleaner, more modular code that's easier to test
- **Fewer Bugs** - Having comprehensive tests from the start helps catch bugs early in development
- **Faster Development** - While it may seem slower at first, TDD often leads to faster development by catching issues early

Let's try it out. We'll follow 4 steps:

1. Define new requirements
2. Write tests before code (they will fail)
3. Implement just enough code to pass
4. Refactor if necessary while keeping the tests passing

### Step 1: Define New Requirements

**New Feature:** The `double_all_purely` function should be able to handle lists containing numbers mixed with strings and other values.

**Requirements:**

- If a given value in the list is a number, multiply the number by 2
- If a given value in the list is a string, concatenate the value to itself: (`"abc"` > `"abcabc"`)
- If a given value is neither, do nothing to it, just add it to the list.

### Step 2: Write Tests Before Code (They Will Fail)

**<details><summary>Solution</summary>**

```python
def test_double_all_purely_strings():
    """double_all_purely - doubles numbers and repeats strings"""
    assert double_all_purely([1, 2, 'a', None]) == [2, 4, 'aa', None]
```

Run it. It fails with `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`. The numbers and the string were never the problem, because `'a' * 2` is already `'aa'`. `None` is: it cannot be multiplied, and the comprehension has no way to know it should be left alone. A failing test is the point of this step: it proves the test is actually checking something.

</details>

### Step 3: Implement Just Enough Code to Pass

**<details><summary>Solution</summary>**

```python
def double_all_purely(items):
    return [double(value) for value in items]


def double(value):
    if isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, str):
        return value + value
    else:
        return value
```

`isinstance(value, some_type)` asks whether `value` is of that type, and it accepts several types at once when you give it a tuple like `(int, float)`. It is the tool for "what kind of thing is this?" checks, and it reads better inside a comprehension when the branching lives in its own small function.

</details>

### Reflection

- How did writing tests _before_ code clarify what the function should do?

## Banking System Challenge

The assignment for this session applies the same cycle to a list of bank account dictionaries: a pure `deposit` function with tests already written, a refactor to a comprehension while the tests stay green, and a `withdraw` function built test-first with an overdraft rule. It is the same three steps you just did, on the data shape your project will use.

## Extension / Practice

Once the banking assignment is done:

- Add a `get_empty_accounts(bank_accounts)` feature using TDD.
- Add an `add_100_to_all_accounts(bank_accounts)` feature using TDD.
- Add a `transfer(bank_accounts, transaction)` feature using TDD, where the transaction has `from_owner`, `to_owner`, and `amount` keys.
- Refactor repetitive lookup logic into a helper function `get_account_by_owner()`.
- Write new tests to confirm helper behavior.
- Make `withdraw` raise a `ValueError` on overdraft instead of silently doing nothing, and test it with `pytest.raises` the way chapter 1.11 did.
