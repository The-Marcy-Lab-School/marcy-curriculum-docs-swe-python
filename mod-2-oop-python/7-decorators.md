# 2.7 Decorators

**Table of Contents**

- [Key Terms](#key-terms)
- [The Same Check in Every Method](#the-same-check-in-every-method)
- [Wrapping a Function](#wrapping-a-function)
  - [Challenge: Keep the Return Value](#challenge-keep-the-return-value)
  - [Decorators and the `@` Syntax](#decorators-and-the--syntax)
- [A Decorator That Refuses](#a-decorator-that-refuses)
  - [Challenge: `@requires_reserved`](#challenge-requires_reserved)
- [Testing a Status Guard](#testing-a-status-guard)
- [Reading a Decorator Factory](#reading-a-decorator-factory)
- [Advanced Topics](#advanced-topics)
  - [Wrapping a Function That Takes Any Arguments](#wrapping-a-function-that-takes-any-arguments)
  - [Keeping a Method's Name with `functools.wraps`](#keeping-a-methods-name-with-functoolswraps)
- [Summary](#summary)

## Key Terms

- A **decorator** is a higher-order function that takes a function, wraps it in another function, and returns the wrapper. The wrapper can run code before and after the original.
  - A **wrapper** is the inner function a decorator returns. It is what gets called in place of the original function.
  - The **`@` syntax** applies a decorator: writing `@requires_paid` above a method is the same as reassigning the method to the decorator's result.
- A **decorator factory** is a function that takes an argument and builds a decorator from it. `@requires_status("paid")` first calls `requires_status("paid")`, which returns a decorator, and then applies that decorator to the method. `@app.route("/")` in Flask works the same way.

## The Same Check in Every Method

A reservation at the venue moves through a fixed series of statuses. It starts out reserved, becomes paid, and then is either checked in at the door or refunded. Each step is only allowed from one status: a reservation can be paid only while it is reserved, and it can be checked in or refunded only once it is paid. Here is a `Reservation` class that enforces those rules, using only what you have learned so far:

```python
class Reservation:
    def __init__(self, number, attendee_name):
        self.number = number
        self.attendee_name = attendee_name
        self._status = 'reserved'

    @property
    def status(self):
        return self._status

    def pay(self):
        if self._status != 'reserved':
            print(f'Cannot pay: reservation #{self.number} is {self._status}.')
            return
        self._status = 'paid'

    def check_in(self):
        if self._status != 'paid':
            print(f'Cannot check_in: reservation #{self.number} is {self._status}.')
            return
        self._status = 'checked_in'

    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.check_in()          # Cannot check_in: reservation #1001 is reserved.
maya.refund()
print(maya.status)       # refunded
```

`status` is a property with no setter, so no code outside the class can assign it, and every change has to go through `pay()`, `check_in()`, or `refund()`. Each of those methods is a refusal: it turns down a change from the wrong status, says why, and changes nothing.

**<details><summary>Q: Which lines are the same in `pay()` and `check_in()`, and which are different?</summary>**

The same in both:

- The shape of the check: an `if` statement that compares `self._status` with one required status, a `print()` that says why the call was refused, and a `return` that stops the method before it changes anything.

Different:

- The status each method requires: `'reserved'` for `pay()` and `'paid'` for `check_in()`.
- The method name inside the message.
- The one line at the end that changes the status.

</details>

The check is written out in full in every method that needs it, and that repetition has already caused a bug. `refund()` was written without its check, so the program just refunded a ticket that Maya never paid for, and nothing printed an error. Every new method that depends on a status needs another copy of the same three lines, and nothing warns you when a copy is missing. The only defence is every programmer remembering to paste the check in.

What the class needs is a way to write each check once, and then attach it to any method by naming the rule, so that a reader can see at a glance that `check_in()` requires a paid reservation. Python's tool for this is a **decorator**: a function that takes a method and hands back a new version of it with the check in front. A decorator is a function that returns another function, and the function it returns is a closure that remembers the method it was given. The rest of this chapter builds the decorator from those two pieces.

## Wrapping a Function

**The Problem:** Some code needs to run around another function, before it or after it, without editing that function. Adding the extra lines to every function that needs them repeats the same code in each one and mixes it in with the function's own job, so it has to be picked back out of every function when it is no longer wanted.

**New Concepts:**

- A function can take a function as its parameter, define a **wrapper** that calls it with extra code around the call, and return the wrapper.
- The wrapper closes over the function it was given, here `func`, so it can call it whenever the wrapper itself is called.
- The original function is never edited, and the wrapping function never mentions what the original does. Each does one job.

**Code:**

```python
def announce(func):
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


def greet(name):
    print(f'Hi, {name}!')


loud_greet = announce(greet)
loud_greet('Maya')
# --- starting ---
# Hi, Maya!
# --- finished ---
```

{% hint style="warning" %}
**Predict, then run.** In what order do these four lines print?

```python
loud_greet = announce(greet)
print('ready')
loud_greet('Maya')
```

<details><summary>What actually happens</summary>

```
ready
--- starting ---
Hi, Maya!
--- finished ---
```

- `announce(greet)` defines `wrapper` and returns it without calling it, and defining a function prints nothing.
- `print('ready')` runs next.
- `loud_greet('Maya')` calls `wrapper`, which prints the first line, calls `func('Maya')`, and prints the last line. `func` is `greet`, so `Hi, Maya!` appears between the two.

</details>
{% endhint %}

### Challenge: Keep the Return Value

`announce()` throws away whatever the wrapped function returns, so it breaks any function that has a `return` statement:

```python
def shout(name):
    return f'HI, {name.upper()}!'


loud_shout = announce(shout)
print(loud_shout('Maya'))
# --- starting ---
# --- finished ---
# None
```

Fix `wrapper` so that it hands back the wrapped function's return value. After your change, the last line should print `HI, MAYA!` instead of `None`.

**<details><summary>Solution</summary>**

```python
def announce(func):
    def wrapper(name):
        print('--- starting ---')
        result = func(name)
        print('--- finished ---')
        return result
    return wrapper
```

- `result = func(name)` stores what the wrapped function returned.
- The closing line is printed after the call, so the result has to be stored rather than returned straight away.
- `return result` hands the value back. Without it, `wrapper` reaches its end and returns `None`, the value every function returns when it has no `return` statement.

</details>

### Decorators and the `@` Syntax

**The Problem:** `loud_greet = announce(greet)` creates a second name, and the original `greet` still exists unwrapped. Any code that calls `greet` instead of `loud_greet` skips the wrapper.

**New Concepts:**

- Writing `@announce` on the line above `def greet` means exactly `greet = announce(greet)`, run straight after the function is defined. A function used this way is called a **decorator**.
- The name `greet` now refers to the wrapper, so every call to `greet` goes through it, and the unwrapped version has no name left.
- The decorator runs once, when Python reaches the definition, not each time the function is called.
- `func.__name__` is a function's name as a string. A decorator can use it to say which function it is wrapping.
- `@property` and `@dataclass` are decorators that Python provides, which is why they are written the same way.

**Code:**

```python
@announce
def greet(name):
    print(f'Hi, {name}!')


greet('Maya')
# --- starting ---
# Hi, Maya!
# --- finished ---
```

{% hint style="warning" %}
**Predict, then run.** This version of `announce()` prints a line when it is called, before it builds the wrapper. In what order do the lines print?

```python
def announce(func):
    print(f'decorating {func.__name__}')
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


@announce
def greet(name):
    print(f'Hi, {name}!')


print('ready')
greet('Maya')
```

<details><summary>What actually happens</summary>

```
decorating greet
ready
--- starting ---
Hi, Maya!
--- finished ---
```

- `@announce` calls `announce(greet)` as soon as Python reaches the definition, so `decorating greet` prints first, before any line below the function runs.
- `print('ready')` runs next.
- `greet('Maya')` calls the wrapper, because the name `greet` now refers to it.

</details>
{% endhint %}

## A Decorator That Refuses

**The Problem:** Back at the reservation, the status check is copied into every method that needs it, and `refund()` was written without its copy, so an unpaid ticket was refunded.

**New Concepts:**

- A decorator can wrap a method as well as a function. The class stores the wrapper under the method's name, so Python passes the instance into the wrapper as its first argument, `self`, exactly as it would into the method.
- The wrapper checks the status before calling the method. When the status is wrong, it prints why and returns without calling the method, so the method's body never runs. The decorator is a **reusable refusal**.
- Each decorator is named for the rule it enforces, so `@requires_paid` above `check_in()` states the rule where the method is defined.
- `method.__name__` lets one decorator name whichever method it refused, so `@requires_paid` can guard both `check_in()` and `refund()`.

**Code:**

```python
def requires_paid(method):
    def wrapper(self):
        if self.status != 'paid':
            print(f'Cannot {method.__name__}: reservation #{self.number} is {self.status}.')
            return
        return method(self)
    return wrapper


class Reservation:
    def __init__(self, number, attendee_name):
        self.number = number
        self.attendee_name = attendee_name
        self._status = 'reserved'

    @property
    def status(self):
        return self._status

    def pay(self):
        if self._status != 'reserved':
            print(f'Cannot pay: reservation #{self.number} is {self._status}.')
            return
        self._status = 'paid'

    @requires_paid
    def check_in(self):
        self._status = 'checked_in'

    @requires_paid
    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.refund()            # Cannot refund: reservation #1001 is reserved.
print(maya.status)       # reserved

maya.pay()
maya.refund()
print(maya.status)       # refunded
```

{% hint style="warning" %}
**Check for understanding.** In `requires_paid`, which variable does `wrapper` close over? `requires_paid` returned long before `maya.check_in()` is called, so how can `wrapper` still call the original `check_in`?

<details><summary>Answer</summary>

`wrapper` closes over `method`, the parameter of `requires_paid`.

- When Python reaches `@requires_paid` above `def check_in`, it calls `requires_paid(check_in)`, so `method` refers to the original `check_in` function.
- `requires_paid` defines `wrapper`, returns it, and finishes. The class stores `wrapper` under the name `check_in`.
- `wrapper` refers to `method`, so it is a closure and keeps `method` after `requires_paid` has returned.
- When `maya.check_in()` runs, Python calls `wrapper(maya)`. If the status is `'paid'`, `wrapper` calls `method(self)`, which is the original `check_in`.

</details>
{% endhint %}

### Challenge: `@requires_reserved`

`pay()` still writes its check out by hand. Write a decorator called `requires_reserved` that refuses a call unless the reservation is reserved, and use it on `pay()` so that `pay()` contains only the line that changes the status.

```python
sam = Reservation(1002, 'Sam Lee')
sam.pay()
sam.pay()                # Cannot pay: reservation #1002 is paid.
print(sam.status)        # paid
```

**<details><summary>Solution</summary>**

```python
def requires_reserved(method):
    def wrapper(self):
        if self.status != 'reserved':
            print(f'Cannot {method.__name__}: reservation #{self.number} is {self.status}.')
            return
        return method(self)
    return wrapper


class Reservation:
    # ... __init__, the status property, check_in(), and refund() from above ...

    @requires_reserved
    def pay(self):
        self._status = 'paid'
```

- `requires_reserved` is `requires_paid` with the required status changed to `'reserved'`.
- `method.__name__` is `'pay'`, so the message names the refused method without the decorator mentioning paying.
- `pay()` now holds only its own job, and the rule appears on the line above it.

</details>

{% hint style="warning" %}
**Check for understanding.** Open `src/reservation.py` in the case study. Which methods does each decorator guard? Then suppose reservation #1005 is reserved and the program calls its `refund()` method. What does the program print, what happens to the status, and why does the message use `method.__name__` instead of the word `refund`?

<details><summary>Answer</summary>

- `@requires_reserved` guards `pay()`. `@requires_paid` guards `check_in()` and `refund()`.
- The program prints `Cannot refund: reservation #1005 is reserved.` and the status stays `'reserved'`. The wrapper returns before it calls the original `refund()`, so the line `self._status = 'refunded'` never runs.
- `requires_paid` guards two methods. `method.__name__` is `'check_in'` in one wrapper and `'refund'` in the other, so one decorator prints the right name for whichever method was refused.

</details>
{% endhint %}

## Testing a Status Guard

**The Problem:** A guard that stops working crashes nothing. If `@requires_paid` were deleted from `check_in()`, an unpaid reservation would be checked in at the door, and the first person to notice would be the venue counting its money at the end of the night.

**New Concepts:**

- A test calls the guarded method from the wrong status and asserts that the status did not change.
- A second test calls it from the right status and asserts that it did change, so the tests also catch a guard that refuses too much.

**Code:**

Set up a project with the decorators and `Reservation` in `src/reservation.py`, and the tests in `tests/test_reservation.py`:

```
guard-practice/
├── .venv/
├── pytest.ini
├── src/
│   └── reservation.py
└── tests/
    └── test_reservation.py
```

`pytest.ini` holds the same two settings as every Mod 2 repository: `pythonpath = src` lets the test file import from the `src` folder, and `testpaths = tests` tells pytest where the tests are:

```
[pytest]
pythonpath = src
testpaths = tests
```

`src/reservation.py` holds `requires_reserved`, `requires_paid`, and the `Reservation` class with all three methods decorated. Then write one test for each side of the rule:

```python
from reservation import Reservation


def test_checking_in_before_paying_is_refused():
    maya = Reservation(1001, 'Maya Rodriguez')

    maya.check_in()

    assert maya.status == 'reserved'


def test_checking_in_after_paying_is_allowed():
    maya = Reservation(1001, 'Maya Rodriguez')
    maya.pay()

    maya.check_in()

    assert maya.status == 'checked_in'
```

With the virtual environment turned on and pytest installed, run `pytest` from the `guard-practice` folder. Both tests pass.

{% hint style="warning" %}
**Predict, then run.** In `src/reservation.py`, delete the `@requires_paid` line above `check_in()`, and run `pytest` again. Which test fails, and what does pytest report?

<details><summary>What actually happens</summary>

Only the first test fails:

```
>       assert maya.status == 'reserved'
E       AssertionError: assert 'checked_in' == 'reserved'
E
E         - reserved
E         + checked_in
```

- Without the decorator, nothing wraps `check_in()`, so its body runs from any status and sets the status to `'checked_in'`.
- The second test still passes, because checking in after paying was always allowed.
- The two lines starting with `-` and `+` are pytest comparing the two strings: `-` marks what the test expected, and `+` marks what the code produced.

Put the `@requires_paid` line back before moving on.

</details>
{% endhint %}

{% hint style="warning" %}
**Check for understanding.** This test is based on one in the case study's `tests/test_reservation.py`, with its objects built inside the test. (In the case study's file, the objects come from shared setup in `tests/conftest.py`, which the case study session explains.)

```python
from datetime import date

from attendee import Attendee
from events import Concert
from reservation import Reservation


def test_paying_twice_is_refused():
    jordan = Attendee('Jordan Lee', 'jordan@example.com')
    jazz = Concert('Friday Night Jazz', date(2026, 12, 13), capacity=40, base_price=25, performer='The Blue Notes')
    reservation = Reservation(1005, jordan, jazz)
    reservation.pay()

    reservation.pay()

    assert reservation.status == 'paid'
```

Name the rule this test protects. Then suppose someone deleted `@requires_reserved` from `pay()`. Would this test fail? The case study's version of the test also checks the message the refusal prints. What does that extra check catch?

<details><summary>Answer</summary>

- The test protects the rule that a reservation can be paid only once, while it is still reserved.
- Without `@requires_reserved`, the second `pay()` runs its body and sets the status to `'paid'` again. The status is `'paid'` either way, so the `assert` passes and the test does not notice the missing guard.
- The case study's version also asserts that `Cannot pay: reservation #... is paid.` was printed. Only the guard prints that message, so the extra check fails as soon as the guard is gone.

When a refused call would leave the same status as an allowed one, a test has to check something that only the refusal produces.

</details>
{% endhint %}

## Reading a Decorator Factory

**The Problem:** `requires_reserved` and `requires_paid` are identical except for one string, the status each one requires. A third status would need a third copy of the same decorator.

**New Concepts:**

- A **decorator factory** is a function that takes an argument and returns a decorator built from it.
- `@requires_status('paid')` is applied in two steps. First, Python calls `requires_status('paid')`, which returns a decorator. Second, Python calls that decorator with the method below it, and the method's name now refers to the wrapper.
- The innermost wrapper closes over two variables: `status` from the factory and `method` from the decorator.
- You will read decorator factories more often than you write them. Flask, which you use in Mod 3, defines every page of a website with one: `@app.route("/")`.

**Code:**

```python
def requires_status(status):
    def decorator(method):
        def wrapper(self):
            if self.status != status:
                print(f'Cannot {method.__name__}: reservation #{self.number} is {self.status}.')
                return
            return method(self)
        return wrapper
    return decorator


class Reservation:
    # ... __init__ and the status property from above ...

    @requires_status('reserved')
    def pay(self):
        self._status = 'paid'

    @requires_status('paid')
    def check_in(self):
        self._status = 'checked_in'
```

{% hint style="warning" %}
**Check for understanding.** When Python reaches `@requires_status('paid')` above `def check_in`, what are the two steps it performs? Name the call that builds the decorator and the function that the decorator then wraps. What does `print(requires_status('paid'))` show, and why?

<details><summary>Answer</summary>

- **Step 1:** Python calls `requires_status('paid')`. That call defines `decorator`, which closes over `status`, and returns it.
- **Step 2:** Python calls the returned decorator with the original `check_in` function. The decorator defines `wrapper`, which closes over `method`, and returns it, and the class stores `wrapper` under the name `check_in`.

`print(requires_status('paid'))` shows a function, `<function requires_status.<locals>.decorator at 0x...>`, because calling the factory returns the decorator rather than wrapping anything. Nothing is wrapped until that decorator is called with a method.

</details>
{% endhint %}

## Advanced Topics

### Wrapping a Function That Takes Any Arguments

**The Problem:** A wrapper written as `def wrapper(name):` can only wrap functions that take exactly one argument. Wrapping a function with two parameters raises an error when it is called.

**New Concepts:**

- `*args` collects every positional argument into a tuple, and `**kwargs` collects every keyword argument into a dictionary.
- `func(*args, **kwargs)` passes them all on unchanged, so one wrapper works for a function with any parameters.

**Code:**

```python
@announce
def seat_label(row, number):
    return f'{row}{number}'


seat_label('B', 12)
# TypeError: announce.<locals>.wrapper() takes 1 positional argument but 2 were given
```

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print('--- starting ---')
        result = func(*args, **kwargs)
        print('--- finished ---')
        return result
    return wrapper


@announce
def seat_label(row, number):
    return f'{row}{number}'


print(seat_label('B', 12))                 # B12, after the two announcements
print(seat_label(row='C', number=3))       # C3, after the two announcements
```

### Keeping a Method's Name with `functools.wraps`

**The Problem:** After decorating, the method's name refers to the wrapper, so anything that asks for the method's name gets `'wrapper'`. Error messages and tools that list methods then show the wrong name.

**New Concepts:**

- `@wraps(method)` from the `functools` module, placed above `def wrapper`, copies the original method's name and description onto the wrapper.
- It changes only how the wrapper describes itself. The wrapper still runs in place of the method.

**Code:**

```python
print(Reservation.check_in.__name__)   # wrapper
```

```python
from functools import wraps


def requires_paid(method):
    @wraps(method)
    def wrapper(self):
        if self.status != 'paid':
            print(f'Cannot {method.__name__}: reservation #{self.number} is {self.status}.')
            return
        return method(self)
    return wrapper

# ... the Reservation class from above, with @requires_paid above check_in() ...

print(Reservation.check_in.__name__)   # check_in
```

## Summary

- **Stub:** one paragraph, as in earlier chapters. It covers four things:
  - a status check copied into every method is repeated code, and forgetting one copy lets an invalid change through;
  - a decorator's wrapper is a closure: it keeps the function or method it was given, and calls it after the decorator has returned;
  - a decorator takes a function, wraps it, and returns the wrapper, and `@decorator` above a definition is the same as reassigning the name to the decorator's result;
  - a decorator such as `@requires_paid` is a reusable refusal: its wrapper checks the status and returns before the method runs, and a test proves it by calling the method from the wrong status and asserting that the status did not change.
