# 14. pytest and Test-Driven Development

**Table of Contents**

- [Key Terms](#key-terms)
- [Learning Objectives](#learning-objectives)
- [A Basic Example](#a-basic-example)
  - [Test Files](#test-files)
- [pytest](#pytest)
  - [Installation and Setup](#installation-and-setup)
  - [First Test](#first-test)
  - [Practice: Add A Test](#practice-add-a-test)
  - [Reading a Failure](#reading-a-failure)
  - [`==` vs. `is`](#-vs-is)
  - [Refactor with Confidence](#refactor-with-confidence)
- [Test-Driven Development](#test-driven-development)
  - [Step 1: Define New Requirements](#step-1-define-new-requirements)
  - [Step 2: Write Tests Before Code (They Will Fail)](#step-2-write-tests-before-code-they-will-fail)
  - [Step 3: Implement Just Enough Code to Pass](#step-3-implement-just-enough-code-to-pass)
  - [Reflection](#reflection)
- [Banking System Challenge](#banking-system-challenge)
- [Extension / Practice](#extension--practice)

## Key Terms

- A **unit test** is a small program that calls one function with a known input and checks that the output is what you expected. A collection of them is a **test suite**.
- A **test file** is a file whose name starts with `test_` that imports functions from your source code and tests them. Keeping tests in their own files, in a `tests/` folder beside `src/`, is separation of concerns applied to testing.
- **`pytest`** is the third-party package that finds and runs test files. It is installed into the project's virtual environment and run with `python3 -m pytest`.
- A **test function** is any function in a test file whose name starts with `test_`. Its name is the description of the test, so write it as a sentence.
- The **`assert`** statement checks that an expression is truthy. If it is not, it raises an `AssertionError` and `pytest` reports the test as failed. There is no other testing vocabulary; the expression is an ordinary comparison.
- **`==`** compares the contents of two values. **`is`** and **`is not`** compare identity: whether two names refer to the very same object. A test for a **pure function** uses `==` to check the returned contents and `is not` to check that a new list came back rather than the original.
- To **refactor** is to change how code works without changing what it does. Passing tests are what let you refactor with confidence, for example from a `for` loop to a list comprehension.
- **Test-driven development (TDD)** is a workflow that writes the test first, watches it fail (**red**), writes just enough code to pass (**green**), and then refactors while the tests stay green.
- **`isinstance(value, type)`** asks whether a value is of a given type, and accepts a tuple of types.
- **`pytest.raises(ErrorType)`** is how a test checks that a function raises the error it should.

## Learning Objectives

By the end of this lesson, you should be able to:

- Explain what unit tests are and why they matter.
- Write tests with pytest using `test_` functions and `assert`.
- Use unit tests to safely **refactor** code that uses loops into **comprehensions**.
- Apply **test-driven development (TDD)** to add new functionality by writing tests before implementation.
- Choose the right comparison in an assertion.
  - `==` for "has the same contents"
  - `is` and `is not` for "is (or is not) the very same object"

## A Basic Example

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

### Test Files

> "Now that we've tested the application, what should we do with the tests? Do we delete them? Do we comment them out? If we keep them, where can they live?"

With manual testing, you're always left with this question. You've spent time and effort to create the tests so deleting them is wasteful, but we can't just leave them in our code because they add clutter.

Rather than testing functions directly in the files where they live, it is better to create separate **test files** that import functions and test them against sample inputs. Test files provide a number of benefits:

- **Separation of concerns**: our source code can focus on functionality while test files focus on testing.
- **Automation**: test files can be executed with a single command or can be configured to run automatically whenever a commit is made, ensuring all new code is functional.
- **Documentation**: test files serve as living documentation, showing how functions are expected to behave.
- **Confidence**: having a comprehensive test suite gives developers confidence when making changes.

## pytest

Let's learn [pytest](https://docs.pytest.org/en/stable/getting-started.html), the most popular framework for creating test files in Python.

### Installation and Setup

`pytest` is a third-party package, so it goes in a virtual environment, exactly as in chapter 7:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pip freeze > requirements.txt
```

Then organize the project so that source code and tests live in separate folders:

```
14-testing/
├── .venv/
├── requirements.txt
├── src/
│   ├── calc.py
│   └── double_all.py
└── tests/
    ├── test_calc.py
    └── test_double_all.py
```

`pytest` finds tests by name. It looks for files whose names start with `test_`, and inside them, for functions whose names start with `test_`. There is nothing to configure.

### First Test

We've created a simple example to demonstrate how to create a test file.

In the file called `src/calc.py`, we've defined a simple `add` function.

```python
# calc.py
def add(a, b):
    return a + b
```

In the `tests` directory, create a file called `test_calc.py` (the test file name should always match the name of the file being tested, with `test_` in front).

Then, add the following code:

```python
# test_calc.py
from src.calc import add


def test_adds_two_numbers():
    assert add(1, 2) == 3
```

Each function whose name starts with `test_` is one test. The name is the description of the test, so make it a sentence. Inside, the `assert` statement is the whole mechanism:

- `assert expression` checks that the `expression` is truthy. If it is, nothing happens and the test continues.
- If it is falsy, `assert` raises an `AssertionError`, the test stops, and pytest reports it as a failure.
- `add(1, 2) == 3` is an ordinary comparison, the same `==` from chapter 2. There is no special testing vocabulary to learn.

Run the tests with:

```sh
python3 -m pytest
```

And you should see something like this (the Python and pytest version numbers will be whatever is on your machine):

```
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/ben/mod-1/14-testing
collected 1 item

tests/test_calc.py .                                                     [100%]

============================== 1 passed in 0.00s ===============================
```

Each dot after a filename is one passing test. We see a passing test because the `assert` expression was `True`.

{% hint style="info" %}
**Why `python3 -m pytest` and not just `pytest`?** Installing pytest gives you a `pytest` command as well, and you will see it in other people's instructions. But `pytest` on its own does not put your project folder on the list of places Python looks for modules, so `from src.calc import add` fails with `ModuleNotFoundError: No module named 'src'`. Running it through `python3 -m` adds the current folder to that list, and the import works. Use `python3 -m pytest`, from the project's root folder, every time.
{% endhint %}

### Practice: Add A Test

In the `tests/test_calc.py` file, add a new test called `test_adds_negatives` that confirms that the `add` function will work properly for inputs like `-3` and `-2`.

**<details><summary>Solution</summary>**

```python
def test_adds_negatives():
    assert add(-3, -2) == -5
```

</details>

Run `python3 -m pytest` again and you should now see two dots. To see every test by name, add `-v` (for "verbose"):

```sh
python3 -m pytest -v
```

```
tests/test_calc.py::test_adds_two_numbers PASSED                         [ 50%]
tests/test_calc.py::test_adds_negatives PASSED                           [100%]
```

### Reading a Failure

Change the expected value in your new test to `-6`, run the tests again, and look at what pytest tells you:

```
tests/test_calc.py .F                                                    [100%]

=================================== FAILURES ===================================
_____________________________ test_adds_negatives ______________________________

    def test_adds_negatives():
>       assert add(-3, -2) == -6
E       assert -5 == -6
E        +  where -5 = add(-3, -2)

tests/test_calc.py:9: AssertionError
=========================== short test summary info ============================
FAILED tests/test_calc.py::test_adds_negatives - assert -5 == -6
========================= 1 failed, 1 passed in 0.01s ==========================
```

The test output provides some really useful information.

- We can see which tests failed: the `F` in the dots, and the name under `FAILURES`
- For each failing test, we can see which `assert` statement failed, marked with `>`
- We can see what the function actually returned (`-5`) and what we said it should be (`-6`), and pytest even shows you the call that produced the `-5`.

Armed with this information, we can more confidently build our functions knowing that we have a specific set of targets to aim for. Automated tests allow us to repeatedly run our code against the same set of tests until all expectations are met.

Change the `-6` back to `-5` before moving on.

### `==` vs. `is`

Take a look at the `src/double_all.py` file, and put the loop version of `double_all_purely` from the top of this chapter in it.

We've already created a test for you in the accompanying `tests/test_double_all.py` file.

Since we are now working with a mutable type (a list), we need to test two different things: that the _contents_ are right, and that the function gave us a _new_ list rather than the one we passed in.

```python
from src.double_all import double_all_purely


def test_doubles_each_value_in_the_list():
    # == compares the contents of lists and dictionaries
    assert double_all_purely([1, 2, 3, 4]) == [2, 4, 6, 8]


def test_does_not_mutate_the_original_list():
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
- `is` compares identity: whether two variables reference the very same object, as you saw with `id()` in chapter 8. `is not` is its opposite.
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
def test_can_double_strings_and_numbers():
    assert double_all_purely([1, 2, 'a', 'b']) == [2, 4, 'aa', 'bb']
```

Run it. It fails with a `TypeError`, because `'a' * 2` is fine but the comprehension has no way to know a string should be handled differently. A failing test is the point of this step: it proves the test is actually checking something.

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
- Make `withdraw` raise a `ValueError` on overdraft instead of silently doing nothing, and test it with `pytest.raises`:

  ```python
  import pytest

  def test_withdraw_raises_on_overdraft():
      with pytest.raises(ValueError):
          withdraw(bank_accounts, {"owner": "Alice", "amount": 500})
  ```
