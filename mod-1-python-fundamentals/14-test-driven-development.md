# 1.14 Test-Driven Development

**Table of Contents**

- [Key Terms](#key-terms)
- [Refactoring with Tests](#refactoring-with-tests)
  - [A Pure Function and Its Tests](#a-pure-function-and-its-tests)
  - [Refactor with Confidence](#refactor-with-confidence)
- [Test-Driven Development](#test-driven-development)
  - [Step 1: Define New Requirements](#step-1-define-new-requirements)
  - [Step 2: Write Tests Before Code (They Will Fail)](#step-2-write-tests-before-code-they-will-fail)
  - [Step 3: Implement Just Enough Code to Pass](#step-3-implement-just-enough-code-to-pass)
  - [Step 4: Refactor If Necessary While Keeping the Tests Passing](#step-4-refactor-if-necessary-while-keeping-the-tests-passing)
  - [Reflection](#reflection)
- [Banking System Challenge](#banking-system-challenge)
- [Extension / Practice](#extension--practice)

## Key Terms

- A **pure function** returns the same output every time it gets the same input, and has no **side effects**: it changes nothing outside itself, such as a list it was given. A function that breaks either rule is **impure**. Pure functions are the easiest functions to test.
- **`==`** compares the contents of two values. **`is`** and **`is not`** compare identity: whether two names refer to the very same object. A test for a **pure function** uses `==` to check the returned contents and `is not` to check that a new list came back rather than the original.
- To **refactor** is to change how code works without changing what it does. Passing tests are what let you refactor with confidence, for example from a `for` loop to a list comprehension.
- **Test-driven development (TDD)** is a workflow that writes the test first, watches it fail (**red**), writes just enough code to pass (**green**), and then refactors while the tests stay green.
- **`isinstance(value, type)`** asks whether a value is of a given type, and accepts a tuple of types.

## Refactoring with Tests

Every comprehension in chapter 1.13 replaced a loop that already worked. How do you know the comprehension does _exactly_ what the loop did? You could run both and compare the output by eye, but you already have a better tool: the `pytest` tests from chapter 1.9.

### A Pure Function and Its Tests

A test calls a function with an input you chose and checks the result against the answer you expect. That check only means something when two things are true of the function:

1. **It returns the same output every time it gets the same input.** A function like `roll_die()`, which returns `random.randint(1, 6)`, cannot be checked with `==`, because no single expected value is right.
2. **It has no side effects.** A **side effect** is a change a function makes outside itself, such as changing a list it was given. A test of a function that changes its input has to check the input as well as the output, and the next test that uses the same list starts from different data.

A function that meets both rules is called a **pure function**, and a function that breaks either one is **impure**. Chapter 1.7 showed how to keep a function from changing a list it was given: copy the list first and change only the copy. That is what makes this function pure. It takes in a list of numbers and returns a copy of that list where each value is doubled:

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

### Step 4: Refactor If Necessary While Keeping the Tests Passing

The `double` function from Step 3 follows the requirements line by line, so it has one branch for numbers and another for strings. But the two branches do the same job: `value + value` and `value * 2` produce the same string, because `'a' * 2` is already `'aa'`.

**<details><summary>Challenge: Combine the number branch and the string branch into one, then run the tests again</summary>**

```python
def double(value):
    if isinstance(value, (int, float, str)):
        return value * 2
    else:
        return value
```

Run `python3 -m pytest tests/test_double_all.py`. All three tests still pass, so the refactor changed how `double` works without changing what it does. If a refactor ever makes a test fail, the test has caught the change in behavior right away, and you can undo the refactor before you build anything on top of it.

</details>

### Reflection

- How did writing tests _before_ code clarify what the function should do?

## Banking System Challenge

The assignment for this session applies the same cycle to a list of bank account dictionaries: a pure `deposit` function with tests already written, a refactor to a comprehension while the tests stay green, and a `withdraw` function built test-first with an overdraft rule. Those three tasks repeat the three parts of this chapter (testing a pure function, refactoring with tests, and test-driven development), on the data shape your project will use.

## Extension / Practice

Once the banking assignment is done:

- Add a `get_empty_accounts(bank_accounts)` feature using TDD.
- Add an `add_100_to_all_accounts(bank_accounts)` feature using TDD.
- Add a `transfer(bank_accounts, transaction)` feature using TDD, where the transaction has `from_owner`, `to_owner`, and `amount` keys.
- Refactor repetitive lookup logic into a helper function `get_account_by_owner()`.
- Write new tests to confirm helper behavior.
- Make `withdraw` raise a `ValueError` on overdraft instead of silently doing nothing, and test it with `pytest.raises` the way chapter 1.11 did.
