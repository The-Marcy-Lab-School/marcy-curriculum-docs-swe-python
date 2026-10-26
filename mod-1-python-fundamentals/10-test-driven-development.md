# 1.10 Test-Driven Development

**Table of Contents**

- [Key Terms](#key-terms)
- [Testing Your Code with pytest](#testing-your-code-with-pytest)
  - [Project Layout](#project-layout)
  - [First Test](#first-test)
  - [Practice: Add A Test](#practice-add-a-test)
  - [Reading a Failure](#reading-a-failure)
  - [Checking `True`, `False`, and Decimals](#checking-true-false-and-decimals)
- [Refactoring with Tests](#refactoring-with-tests)
  - [A Pure Function and Its Tests](#a-pure-function-and-its-tests)
  - [Refactor with Confidence](#refactor-with-confidence)
- [Test-Driven Development](#test-driven-development)
  - [Step 1: Define New Requirements](#step-1-define-new-requirements)
  - [Step 2: Write Tests Before Code (They Will Fail)](#step-2-write-tests-before-code-they-will-fail)
  - [Step 3: Implement Just Enough Code to Pass](#step-3-implement-just-enough-code-to-pass)
  - [Step 4: Refactor If Necessary While Keeping the Tests Passing](#step-4-refactor-if-necessary-while-keeping-the-tests-passing)
  - [Reflection](#reflection)
- [Testing Errors](#testing-errors)
  - [Raising Your Own Errors](#raising-your-own-errors)
  - [Testing That a Function Raises](#testing-that-a-function-raises)
  - [One Failing Test Does Not Stop the Others](#one-failing-test-does-not-stop-the-others)
- [Challenge: Bank Accounts](#challenge-bank-accounts)

## Key Terms

- A **unit test** is a small program that calls one function with a known input and checks that the output is what you expected. A collection of them is a **test suite**.
- A **test file** is a file whose name starts with `test_` that imports functions from your source code and tests them. Keeping tests in their own files, in a `tests/` folder beside `src/`, is separation of concerns applied to testing.
- A **test function** is any function in a test file whose name starts with `test_`. It is named after the function it tests, and the docstring on its first line describes what the test checks.
- The **`assert`** statement checks that an expression is truthy. If it is not, it raises an `AssertionError` and `pytest` reports the test as failed. The expression is an ordinary comparison: `==` for most values, `is` for `True`, `False`, and `None`, and `pytest.approx()` for decimal numbers.
- A **pure function** returns the same output every time it gets the same input, and has no **side effects**: it changes nothing outside itself, such as a list it was given. A function that breaks either rule is **impure**. Pure functions are the easiest functions to test.
- **`==`** compares the contents of two values. **`is`** and **`is not`** compare identity: whether two names refer to the very same object. A test for a **pure function** uses `==` to check the returned contents and `is not` to check that a new list came back rather than the original.
- To **refactor** is to change how code works without changing what it does. Passing tests are what let you refactor with confidence, for example from a loop that changes a copy by index to a loop that appends to a new list.
- **Test-driven development (TDD)** is a workflow that writes the test first, watches it fail (**red**), writes just enough code to pass (**green**), and then refactors while the tests stay green.
- **`isinstance(value, type)`** asks whether a value is of a given type, and accepts a tuple of types.
- The **`raise`** statement lets a function report a problem itself, such as `raise ValueError("message")`. **`pytest.raises(ErrorType)`** is how a test checks that a function raises the error it should.
- pytest catches an error raised inside a test, reports that test as failed, and keeps running the others. A test file that cannot be imported stops the whole run.

## Testing Your Code with pytest

Up to now, you have checked your functions by calling them and reading what `print()` shows.

> "Now that we've tested the application, what should we do with the tests? Do we delete them? Do we comment them out? If we keep them, where can they live?"

With manual testing, your tests are the `print()` calls you added to check each function, and you're always left with this question. You've spent time and effort writing them, so deleting them is wasteful. But if you leave them in, they run every time the program runs, and, as you saw in the Modules lesson, every time another file imports that file. Whoever runs the program sees your check results mixed in with its real output and has no idea what they mean.

Rather than testing functions directly in the files where they live, it is better to create separate **test files** that import functions and test them against sample inputs. Test files provide a number of benefits:

- **Separation of concerns**: our source code can focus on functionality while test files focus on testing.
- **Automation**: test files can be executed with a single command or can be configured to run automatically whenever a commit is made, ensuring all new code is functional.
- **Documentation**: test files serve as living documentation, showing how functions are expected to behave.
- **Confidence**: having a comprehensive test suite gives developers confidence when making changes.

The assignments in this program come with test files already written. Running them tells you which of your functions work and which do not.

### Project Layout

Create a folder called `testing-practice`. In it, create and activate a virtual environment and install `pytest`, as you did in the Modules lesson.

```sh
cd [repo_name]
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

Then organize the project so that source code and tests live in separate folders:

```
testing-practice/
├── .venv/
├── requirements.txt
├── src/
│   └── calc.py
└── tests/
    └── test_calc.py
```

`pytest` finds tests by name. It looks for files whose names start with `test_`, and inside them, for functions whose names start with `test_`. There is nothing to configure.

### First Test

In the file called `src/calc.py`, define a simple `add` function.

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


def test_add():
    """add - adds two positive numbers"""
    assert add(1, 2) == 3
    assert add(10, 5) == 15
```

The first line imports `add` from `src/calc.py`. When a module sits inside a folder, you write the folder name, a dot, and then the module name, so `src.calc` means "the `calc` module inside the `src` folder". Python starts looking from the folder you run the tests in, which is why the hint below says to run them from the project's root folder.

Each function whose name starts with `test_` is one test. Name it after the function it tests. The string on the first line is a docstring, the function description you met in chapter 1.3. In a test, the docstring says what the test checks. Inside, the `assert` statement is the whole mechanism:

- `assert expression` checks that the `expression` is truthy. If it is, nothing happens and the test continues.
- If it is falsy, `assert` raises an `AssertionError`, the test stops, and pytest reports it as a failure. Outside of a test, a failing `assert` crashes the program like any other error: `assert 1 == 2, "one is not two"` raises `AssertionError: one is not two`.
- `add(1, 2) == 3` is an ordinary comparison, the same `==` from chapter 1.2. There is no special testing vocabulary to learn.

A test can hold as many `assert` statements as you like. The test passes only if every one of them passes.

Run the tests with:

```sh
python3 -m pytest
```

And you should see something like this (the Python and pytest version numbers will be whatever is on your machine):

```
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/ben/mod-1/testing-practice
collected 1 item

tests/test_calc.py .                                                     [100%]

============================== 1 passed in 0.00s ===============================
```

Each dot after a filename is one passing test. We see a passing test because every `assert` expression was `True`.

{% hint style="info" %}
**Why `python3 -m pytest` and not just `pytest`?** Installing pytest gives you a `pytest` command as well, and you will see it in other people's instructions. But `pytest` on its own does not put your project folder on the list of places Python looks for modules, so `from src.calc import add` fails with `ModuleNotFoundError: No module named 'src'`. Running it through `python3 -m` adds the folder you are in to that list. The project's root folder, `testing-practice/`, contains `src/`, so from there `from src.calc import add` works. If you `cd tests` first, Python adds `tests/` instead, finds no `src` there, and you are back to `ModuleNotFoundError`. So run `python3 -m pytest` from the project's root folder every time.
{% endhint %}

### Practice: Add A Test

In the `tests/test_calc.py` file, add a new test called `test_add_negatives` that confirms that the `add` function will work properly for inputs like `-3` and `-2`.

**<details><summary>Solution</summary>**

```python
def test_add_negatives():
    """add - adds two negative numbers"""
    assert add(-3, -2) == -5
```

</details>

Run `python3 -m pytest` again and you should now see two dots. To see every test by name, add `-v` (for "verbose"):

```sh
python3 -m pytest -v
```

```
tests/test_calc.py::test_add PASSED                                      [ 50%]
tests/test_calc.py::test_add_negatives PASSED                            [100%]
```

### Reading a Failure

Change the expected value in your new test to `-6`, run the tests again, and look at what pytest tells you:

```
tests/test_calc.py .F                                                    [100%]

=================================== FAILURES ===================================
______________________________ test_add_negatives ______________________________

    def test_add_negatives():
        """add - adds two negative numbers"""
>       assert add(-3, -2) == -6
E       assert -5 == -6
E        +  where -5 = add(-3, -2)

tests/test_calc.py:12: AssertionError
=========================== short test summary info ============================
FAILED tests/test_calc.py::test_add_negatives - assert -5 == -6
========================= 1 failed, 1 passed in 0.01s ==========================
```

The test output provides some really useful information.

- We can see which tests failed: the `F` in the dots, and the name under `FAILURES`
- For each failing test, we can see which `assert` statement failed, marked with `>`
- We can see what the function actually returned (`-5`) and what we said it should be (`-6`), and pytest even shows you the call that produced the `-5`.

Armed with this information, we can more confidently build our functions knowing that we have a specific set of targets to aim for. Automated tests allow us to repeatedly run our code against the same set of tests until all expectations are met.

Change the `-6` back to `-5` before moving on.

### Checking `True`, `False`, and Decimals

Two more kinds of assertion appear all over the test files in your assignments.

When a function should return `True`, `False`, or `None`, the test uses `is` rather than `==`:

```python
def test_is_even():
    """is_even - returns True for even numbers, False for odd"""
    assert is_even(2) is True
    assert is_even(3) is False
```

`is` is the identity operator from chapter 1.2. There is only one `True` and one `False` in a Python program, so `is True` asks "did the function return the boolean `True` itself?"

**<details><summary>Q: Suppose `is_even` were written as `return 1 - num % 2`, which returns `1` for even numbers and `0` for odd ones. Would `assert is_even(2) == True` pass? Would `assert is_even(2) is True`?</summary>**

The `==` version passes, because `True` counts as `1` in arithmetic, so `1 == True` is `True`. The `is` version fails:

```
E       assert 1 is True
E        +  where 1 = is_even(2)
```

`1` is truthy, but it is not the boolean `True`. That difference shows up as soon as someone uses the function: `print(f"Is 4 even? {is_even(4)}")` prints `Is 4 even? 1`, and whoever reads that has to guess what `1` means. A function named `is_even` promises a boolean. The `==` version lets the broken function pass, and the `is True` version catches it.

</details>

When a function returns a decimal number, the test compares with `pytest.approx()`:

```python
import pytest
from src.calc import add


def test_add_decimals():
    """add - adds decimal numbers"""
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

Remember from chapter 1.2 that `0.1 + 0.2 == 0.3` is `False`, because decimals are stored very slightly inexactly. `pytest.approx(0.3)` means "a number close enough to `0.3` that the difference is only that inexactness." Using it requires `import pytest` at the top of the test file.

## Refactoring with Tests

Once a function works, you will often want to rewrite it: to make it shorter, to make it clearer, or to make room for a new feature. How do you know the new version does _exactly_ what the old one did? You could run both and compare the output by eye, but you already have a better tool: the `pytest` tests from the last section.

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

In your `testing-practice` project, put this function in a new file, `src/double_all.py`, and create `tests/test_double_all.py`.

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

`double_all_purely` copies the list and then changes every position of the copy by its index. Chapter 1.7 showed a more direct way to build a new list: start with an empty list and append each new value to it.

**<details><summary>Challenge: Refactor `double_all_purely` to append each doubled value to a new, empty list</summary>**

```python
def double_all_purely(items):
    doubled = []
    for num in items:
        doubled.append(num * 2)
    return doubled
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

Run it. It fails with `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`. The numbers and the string were never the problem, because `'a' * 2` is already `'aa'`. `None` is: it cannot be multiplied, and the loop has no way to know it should be left alone. A failing test is the point of this step: it proves the test is actually checking something.

</details>

### Step 3: Implement Just Enough Code to Pass

**<details><summary>Solution</summary>**

```python
def double_all_purely(items):
    doubled = []
    for value in items:
        doubled.append(double(value))
    return doubled


def double(value):
    if isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, str):
        return value + value
    else:
        return value
```

`isinstance(value, some_type)` asks whether `value` is of that type, and it accepts several types at once when you give it a tuple like `(int, float)`. It is the tool for "what kind of thing is this?" checks, and the loop stays easy to read when the branching lives in its own small function.

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

## Testing Errors

### Raising Your Own Errors

Sometimes your code is the one that discovers the problem. A function that is handed a value it cannot work with should say so loudly rather than carry on and produce nonsense:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Cannot withdraw {amount} from a balance of {balance}")
    return balance - amount
```

The caller can then choose to catch it with `try` and `except`, or let it crash:

```python
balance = 100

try:
    balance = withdraw(balance, 500)
except ValueError:
    print("You don't have enough money for that withdrawal.")
```

Either way, the failure happens where the mistake is, with a message that says what went wrong, instead of three functions later with a confusing one. Pick the built-in error type whose meaning is closest: `ValueError` for a bad value, `TypeError` for a bad type.

### Testing That a Function Raises

An error that a function raises on purpose is part of what the function does, so it deserves a test like any other behavior. In your `testing-practice` project, put `withdraw` in `src/bank.py` and write `tests/test_bank.py`:

```python
import pytest
from src.bank import withdraw


def test_withdraw():
    """withdraw - subtracts the amount from the balance"""
    assert withdraw(100, 30) == 70


def test_withdraw_overdraft():
    """withdraw - raises a ValueError when the amount is more than the balance"""
    with pytest.raises(ValueError):
        withdraw(100, 500)
```

`with pytest.raises(ValueError):` means "the indented code below must raise a `ValueError`." If it does, pytest catches the error and the test passes. If it does not, the test fails. The `with` statement starts a block that `pytest.raises` watches: pytest runs the indented code and then checks what happened.

{% hint style="warning" %}
**Predict, then run.** Delete the whole `if` statement from `withdraw` (both the `if` line and the `raise` line beneath it) so that it quietly allows the overdraft, and run the tests again. What does pytest report?

<details><summary>What actually happens</summary>

```
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE ValueError
```

pytest reports `test_withdraw_overdraft` as failed. `test_withdraw` still passes, because `withdraw(100, 30)` never reached the `raise` anyway: 30 is not more than 100. `test_withdraw_overdraft` fails, because `withdraw(100, 500)` now returns `-400` instead of raising a `ValueError`. The function no longer does what the test says it should, and pytest tells you exactly which promise it broke. Put the `if` statement back before moving on.

</details>
{% endhint %}

### One Failing Test Does Not Stop the Others

Every failure so far happened at an `assert`. A test can also fail because the function it calls crashes. Suppose a bug made `withdraw` raise a `TypeError` on every call. pytest would report both `withdraw` tests as failed, show the `TypeError` and its traceback, and still run every other test in the project.

pytest runs each test function the way a `try`/`except` would. When a test raises an error, pytest catches it, records that test as failed, and moves on to the next test. That is why one broken function never hides the results of the rest of your tests. `pytest.raises` is the reverse case: inside a `with pytest.raises(ValueError):` block, the error is the result the test expects, so the test fails when the error does _not_ happen.

The one failure that stops everything is a test file that cannot be imported, for example because it imports a function that does not exist yet. pytest cannot even find the tests in that file, so it stops with `Interrupted: 1 error during collection` and runs none of the tests in the project. Read the `ImportError` it prints and fix the import before anything else.

## Challenge: Bank Accounts

Practice the whole cycle on a list of bank account dictionaries, the data shape your project will use. Add the functions below to `src/bank.py`, beside `withdraw`, and test them in a new file, `tests/test_bank_accounts.py`. Build each one test-first: write a test, watch it fail, write just enough code to pass, and then refactor while the tests stay green.

Start the test file with a function that returns the sample accounts. Each test calls `make_accounts()` to get its own fresh list, so a test that changes the accounts cannot change the data another test starts from:

```python
def make_accounts():
    return [
        {"owner": "Ada", "balance": 250},
        {"owner": "Zo", "balance": 0},
        {"owner": "Maya", "balance": 40},
    ]
```

1. `get_empty_accounts(bank_accounts)` returns a new list of the accounts whose balance is `0`.
2. `add_100_to_all_accounts(bank_accounts)` returns a new list of new account dictionaries, each with `100` more in its balance. The original accounts must not change, so test it the way you tested `double_all_purely`.
3. `transfer(bank_accounts, transaction)` moves money from one account to another. The transaction is a dictionary with `from_owner`, `to_owner`, and `amount` keys. Use `withdraw` to take the money out, so that a transfer the sender cannot afford raises a `ValueError`, and test that with `pytest.raises`.
4. `transfer` has to find two accounts by their owner. Refactor that lookup into a helper function, `get_account_by_owner(bank_accounts, owner)`, that returns the matching account, or `None` when no account matches. Write tests for the helper, and run every test to confirm that the refactor changed nothing.

**<details><summary>Solution</summary>**

{% code title="tests/test_bank_accounts.py" overflow="wrap" %}

```python
import pytest
from src.bank import get_empty_accounts, add_100_to_all_accounts, get_account_by_owner, transfer


def make_accounts():
    return [
        {"owner": "Ada", "balance": 250},
        {"owner": "Zo", "balance": 0},
        {"owner": "Maya", "balance": 40},
    ]


def test_get_empty_accounts():
    """get_empty_accounts - keeps only the accounts with a balance of 0"""
    assert get_empty_accounts(make_accounts()) == [{"owner": "Zo", "balance": 0}]


def test_add_100_to_all_accounts():
    """add_100_to_all_accounts - returns new accounts with 100 more in each"""
    accounts = make_accounts()
    updated = add_100_to_all_accounts(accounts)
    assert updated == [
        {"owner": "Ada", "balance": 350},
        {"owner": "Zo", "balance": 100},
        {"owner": "Maya", "balance": 140},
    ]
    assert updated is not accounts
    assert accounts == make_accounts()


def test_get_account_by_owner():
    """get_account_by_owner - finds the account, or returns None"""
    accounts = make_accounts()
    assert get_account_by_owner(accounts, "Maya") is accounts[2]
    assert get_account_by_owner(accounts, "Bo") is None


def test_transfer():
    """transfer - moves the amount from one account to another"""
    accounts = make_accounts()
    transfer(accounts, {"from_owner": "Ada", "to_owner": "Zo", "amount": 50})
    assert accounts[0]["balance"] == 200
    assert accounts[1]["balance"] == 50


def test_transfer_overdraft():
    """transfer - raises a ValueError when the sender does not have enough"""
    accounts = make_accounts()
    with pytest.raises(ValueError):
        transfer(accounts, {"from_owner": "Maya", "to_owner": "Ada", "amount": 100})
```

{% endcode %}

{% code title="src/bank.py (below withdraw)" overflow="wrap" %}

```python
def get_empty_accounts(bank_accounts):
    empty = []
    for account in bank_accounts:
        if account["balance"] == 0:
            empty.append(account)
    return empty


def add_100_to_all_accounts(bank_accounts):
    updated = []
    for account in bank_accounts:
        new_account = dict(account)
        new_account["balance"] += 100
        updated.append(new_account)
    return updated


def get_account_by_owner(bank_accounts, owner):
    for account in bank_accounts:
        if account["owner"] == owner:
            return account
    return None


def transfer(bank_accounts, transaction):
    from_account = get_account_by_owner(bank_accounts, transaction["from_owner"])
    to_account = get_account_by_owner(bank_accounts, transaction["to_owner"])
    from_account["balance"] = withdraw(from_account["balance"], transaction["amount"])
    to_account["balance"] += transaction["amount"]
```

{% endcode %}

`add_100_to_all_accounts` copies each dictionary with `dict(account)` before changing its balance, as chapter 1.8 showed, so the original accounts keep their balances. `transfer` changes the accounts it was given, so its tests check the accounts afterward instead of a returned value.

</details>
