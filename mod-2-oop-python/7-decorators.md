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
  - A **wrapper** is the inner function a decorator returns. The wrapper is what gets called in place of the original function.
  - The **`@` syntax** applies a decorator: writing `@requires_paid` above a method is the same as reassigning the method to the decorator's result.
- A **decorator factory** is a function that takes an argument and builds a decorator from that argument. `@requires_status("paid")` first calls `requires_status("paid")`, which returns a decorator, and then applies that decorator to the method. `@app.route("/")` in Flask works the same way.

## The Same Check in Every Method

A reservation at the venue moves through a fixed series of statuses. It starts out reserved, becomes paid, and then is either checked in at the door or refunded. Each step is only allowed from one status:

- A reservation can be `"paid"` only after it is `"reserved"`
- A reservation can be `"checked_in"` or `"refunded"` only after it is `"paid"`

Here is a `Reservation` class that enforces those rules, using only what you have learned so far:

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
            print('Reservation must be reserved in order to use pay.')
            return
        self._status = 'paid'

    def check_in(self):
        if self._status != 'paid':
            print('Reservation must be paid in order to use check_in.')
            return
        self._status = 'checked_in'

    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.check_in()          # Reservation must be paid in order to use check_in.
maya.refund()
print(maya.status)       # refunded
```

`status` is a property with no setter, so no code outside the class can assign it, and every change has to go through `pay()`, `check_in()`, or `refund()`. Each of those methods is a refusal: it turns down a change from the wrong status, says why, and changes nothing.

**<details><summary>Q: What is expected about this behavior? What is unexpected?</summary>**

Maya has a reservation but hasn't paid yet so it is expected that she is unable to check in.

However, since Maya hasn't paid, it is unexpected that she is able to get refunded.

</details>

**<details><summary>Q: Which lines are the same in `pay()` and `check_in()`, and which are different?</summary>**

The same in both:

- The shape of the check: an `if` statement that compares `self._status` with one required status, a `print()` that says why the call was refused, and a `return` that stops the method before it changes anything.

Different:

- The status each method requires: `'reserved'` for `pay()` and `'paid'` for `check_in()`.
- The method name inside the message.
- The one line at the end that changes the status.

</details>

The check is written out in full in every method that needs it, and that repetition has already caused a bug. `refund()` was written without its guard clause, so the program just refunded a ticket that Maya never paid for, and nothing printed an error.

Every new method that depends on a status needs another copy of the same three lines, and nothing warns you when a copy is missing. The only defense is every programmer remembering to paste the guard clause.

What the class needs is a way to write each check once, and then attach it to any method by naming the rule, so that a reader can see at a glance that `check_in()` requires a paid reservation. Python's tool for this is a **decorator**: a function that takes a method and hands back a new version of it with the check in front. A decorator is a function that returns another function, and that returned function is a closure that remembers the method the decorator was given. The rest of this chapter builds the decorator from those two pieces.

## Wrapping a Function

**The Problem:** Some code needs to run around another function, before it or after it, without editing that function (e.g. every status change needs to check for a required status before changing the status).

**Code:**

```python
def announce(func):                 # takes a function as its parameter
    def wrapper(name):              # the wrapper, defined inside announce()
        print('--- starting ---')   # runs before func
        func(name)                  # wrapper closes over func, so it can call func later
        print('--- finished ---')   # runs after func
    return wrapper                  # returns the wrapper without calling it


def greet(name):
    print(f'Hi, {name}!')


greet('Maya')
# Hi, Maya!

announced_greet = announce(greet)   # announced_greet now refers to wrapper
announced_greet('Maya')
# --- starting ---
# Hi, Maya!
# --- finished ---
```

**New Concepts:**

- A function can take another function as a parameter, here `func`, define a **wrapper** that calls `func` with extra code around the call, and return the wrapper.
- Here, the `wrapper` forms a closure around `func`. Whenever `wrapper` is called, `func` is called as well, with print statements before and after.
- The original function (`func`) is never edited, and the wrapping function (`wrapper`) doesn't need to know anything about what the original does. Each does one job: `wrapper` adds the print statements and `func` does still does its own job.

{% hint style="warning" %}
**Predict, then run.** In what order do these four lines print?

```python
announced_greet = announce(greet)
print('ready')
announced_greet('Maya')
```

<details><summary>What actually happens</summary>

```
ready
--- starting ---
Hi, Maya!
--- finished ---
```

- `announce(greet)` defines `wrapper` and returns `wrapper` without calling it, and defining a function prints nothing.
- `print('ready')` runs next.
- `announced_greet('Maya')` calls `wrapper`, which prints the first line, calls `func('Maya')`, and prints the last line. `func` is `greet`, so `Hi, Maya!` appears between the two.

</details>
{% endhint %}

### Challenge: Keep the Return Value

`announce()` throws away whatever the wrapped function returns, so `announce()` breaks any function that has a `return` statement:

```python
# unchanged from the previous example
def announce(func):
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


def shout(name):
    return f'HI, {name.upper()}!'


announced_shout = announce(shout)
print(announced_shout('Maya'))
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
- `return result` hands the value back. Without that line, `wrapper` reaches its end and returns `None`, the value every function returns when it has no `return` statement.

</details>

### Decorators and the `@` Syntax

**The Problem:** `announced_greet = announce(greet)` creates a second name, and the original `greet` still exists unwrapped. Any code that calls `greet` instead of `announced_greet` skips the wrapper.

**Code:**

```python
# unchanged from the first announce() example
def announce(func):
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


@announce          # the decorator: the same as greet = announce(greet) after the definition
def greet(name):
    print(f'Hi, {name}!')


greet('Maya')      # greet now refers to the wrapper
# --- starting ---
# Hi, Maya!
# --- finished ---
```

**New Concepts:**

- Writing `@announce` on the line above `def greet` "decorates" the `greet` function. Specifically it means `greet = announce(greet)` (reassigns `greet` to the "decorated" version).
  - The name `greet` now refers to the wrapper, so every call to `greet` goes through the wrapper, and the unwrapped version has no name left.
- A function like `announce` used this way is called a **decorator**.
  - The decorator runs once, when Python reaches the definition, not each time the function is called.
- `@property` and `@dataclass` are decorators that Python provides, which is why they are written the same way.

{% hint style="warning" %}

`func.__name__` is a function's name as a string. A decorator can use `func.__name__` to say which function the decorator is wrapping.

**Predict, then run.** This version of `announce()` prints a line as soon as `announce()` is called, before building the wrapper. In what order do the lines print?

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
- `greet('Maya')` calls the wrapper, because the name `greet` now refers to the wrapper.

</details>
{% endhint %}

## A Decorator That Refuses

**The Problem:** The `Reservation` class still copies most of the status guard clause between its methods, and `refund()` was written without any guard clause at all, so an unpaid ticket was refunded.

**Code:**

```python
def requires_paid(method):
    def wrapper(self):                      # receives the instance as self, as the method would
        if self.status != 'paid':
            # method.__name__ is the name of the method being refused, such as 'refund'
            print(f'Reservation must be paid in order to use {method.__name__}.')
            return                          # refuses: the method's body never runs
        return method(self)                 # allowed: runs the original method
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
            print('Reservation must be reserved in order to use pay.')
            return
        self._status = 'paid'

    @requires_paid      # check_in() runs only when the reservation is paid
    def check_in(self):
        self._status = 'checked_in'

    @requires_paid      # one decorator guards a second method
    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.refund()            # Reservation must be paid in order to use refund.
print(maya.status)       # reserved

maya.pay()
maya.refund()
print(maya.status)       # refunded
```

**New Concepts:**

- A decorator can wrap a method as well as a function. The class stores the wrapper under the method's name, so Python passes the instance into the wrapper as the wrapper's first argument, `self`, exactly as Python would pass the instance into the method.
- The wrapper checks the status before calling the method. When the status is wrong, the wrapper prints why and returns without calling the method, so the method's body never runs. The decorator is a **reusable refusal**.
- Each decorator is named for the rule it enforces, so `@requires_paid` above `check_in()` states the rule where the method is defined.
- `method.__name__` lets one decorator name whichever method it refused, so `@requires_paid` can guard both `check_in()` and `refund()`.

{% hint style="warning" %}
**Check for understanding.** In `requires_paid`, which variable does `wrapper` close over? `requires_paid` returned long before `maya.check_in()` is called, so how can `wrapper` still call the original `check_in`?

<details><summary>Answer</summary>

`wrapper` closes over `method`, the parameter of `requires_paid`.

- When Python reaches `@requires_paid` above `def check_in`, it calls `requires_paid(check_in)`, so `method` refers to the original `check_in` function.
- `requires_paid` defines `wrapper`, returns it, and finishes. The class stores `wrapper` under the name `check_in`.
- `wrapper` refers to `method`, so `wrapper` is a closure and keeps `method` after `requires_paid` has returned.
- When `maya.check_in()` runs, Python calls `wrapper(maya)`. If the status is `'paid'`, `wrapper` calls `method(self)`, which is the original `check_in`.

</details>
{% endhint %}

### Challenge: `@requires_reserved`

`pay()` still writes its check out by hand. Write a decorator called `requires_reserved` that refuses a call unless the reservation is reserved, and use it on `pay()` so that `pay()` contains only the line that changes the status.

```python
sam = Reservation(1002, 'Sam Lee')
sam.pay()
sam.pay()                # Reservation must be reserved in order to use pay.
print(sam.status)        # paid
```

**<details><summary>Solution</summary>**

```python
def requires_reserved(method):
    def wrapper(self):
        if self.status != 'reserved':
            print(f'Reservation must be reserved in order to use {method.__name__}.')
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
- The program prints `Reservation must be paid in order to use refund.` and the status stays `'reserved'`. The wrapper returns before it calls the original `refund()`, so the line `self._status = 'refunded'` never runs.
- `requires_paid` guards two methods. `method.__name__` is `'check_in'` in one wrapper and `'refund'` in the other, so one decorator prints the right name for whichever method was refused.

</details>
{% endhint %}

## Testing a Status Guard

**The Problem:** A guard that stops working crashes nothing. If `@requires_paid` were deleted from `check_in()`, an unpaid reservation would be checked in at the door, and the first person to notice would be the venue counting its money at the end of the night.

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

    maya.check_in()                         # called from the wrong status

    assert maya.status == 'reserved'        # the refusal changed nothing


def test_checking_in_after_paying_is_allowed():
    maya = Reservation(1001, 'Maya Rodriguez')
    maya.pay()

    maya.check_in()                         # called from the right status

    assert maya.status == 'checked_in'      # the guard let the call through
```

With the virtual environment turned on and pytest installed, run `pytest` from the `guard-practice` folder. Both tests pass.

**New Concepts:**

- A test calls the guarded method from the wrong status and asserts that the status did not change.
- A second test calls the method from the right status and asserts that the status did change, so the tests also catch a guard that refuses too much.

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
- The case study's version also asserts that `Reservation must be reserved in order to use pay.` was printed. Only the guard prints that message, so the extra check fails as soon as the guard is gone.

When a refused call would leave the same status as an allowed one, a test has to check something that only the refusal produces.

</details>
{% endhint %}

## Reading a Decorator Factory

**The Problem:** `requires_reserved` and `requires_paid` are identical except for one string, the status each one requires. A third status would need a third copy of the same decorator.

**Code:**

```python
def requires_status(status):        # the factory: takes the required status
    def decorator(method):          # the decorator the factory builds and returns
        def wrapper(self):          # closes over both status and method
            if self.status != status:
                print(f'Reservation must be {status} in order to use {method.__name__}.')
                return
            return method(self)
        return wrapper
    return decorator


class Reservation:
    # ... __init__ and the status property from above ...

    @requires_status('reserved')    # calls the factory, then applies the decorator it returns
    def pay(self):
        self._status = 'paid'

    @requires_status('paid')
    def check_in(self):
        self._status = 'checked_in'
```

**New Concepts:**

- A **decorator factory** is a function that takes an argument and returns a decorator built from that argument.
- `@requires_status('paid')` is applied in two steps. First, Python calls `requires_status('paid')`, which returns a decorator. Second, Python calls that decorator with the method below it, and the method's name now refers to the wrapper.
- The innermost wrapper closes over two variables: `status` from the factory and `method` from the decorator.
- You will read decorator factories more often than you write them. Flask, which you use in Mod 3, defines every page of a website with one: `@app.route("/")`.

{% hint style="warning" %}
**Check for understanding.** When Python reaches `@requires_status('paid')` above `def check_in`, what are the two steps it performs? Name the call that builds the decorator and the function that the decorator then wraps. What does `print(requires_status('paid'))` show, and why?

<details><summary>Answer</summary>

- **Step 1:** Python calls `requires_status('paid')`. That call defines `decorator`, which closes over `status`, and returns `decorator`.
- **Step 2:** Python calls the returned decorator with the original `check_in` function. The decorator defines `wrapper`, which closes over `method`, and returns `wrapper`, and the class stores `wrapper` under the name `check_in`.

`print(requires_status('paid'))` shows a function, `<function requires_status.<locals>.decorator at 0x...>`, because calling the factory returns the decorator rather than wrapping anything. Nothing is wrapped until that decorator is called with a method.

</details>
{% endhint %}

## Advanced Topics

### Wrapping a Function That Takes Any Arguments

**The Problem:** A wrapper written as `def wrapper(name):` can only wrap functions that take exactly one argument. Calling a wrapped function that has two parameters raises an error.

**Code:**

```python
# unchanged from the first announce() example
def announce(func):
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


@announce
def seat_label(row, number):
    return f'{row}{number}'


seat_label('B', 12)
# TypeError: announce.<locals>.wrapper() takes 1 positional argument but 2 were given
```

```python
def announce(func):
    def wrapper(*args, **kwargs):           # collects any positional and keyword arguments
        print('--- starting ---')
        result = func(*args, **kwargs)      # passes them all on to func unchanged
        print('--- finished ---')
        return result
    return wrapper


@announce
def seat_label(row, number):
    return f'{row}{number}'


print(seat_label('B', 12))                 # B12, after the two announcements
print(seat_label(row='C', number=3))       # C3, after the two announcements
```

**New Concepts:**

- `*args` collects every positional argument into a tuple, and `**kwargs` collects every keyword argument into a dictionary.
- `func(*args, **kwargs)` passes them all on unchanged, so one wrapper works for a function with any parameters.

### Keeping a Method's Name with `functools.wraps`

**The Problem:** After decorating, the method's name refers to the wrapper, so anything that asks for the method's name gets `'wrapper'`. Error messages and tools that list methods then show the wrong name.

**Code:**

```python
# unchanged from A Decorator That Refuses
def requires_paid(method):
    def wrapper(self):
        if self.status != 'paid':
            print(f'Reservation must be paid in order to use {method.__name__}.')
            return
        return method(self)
    return wrapper


# only check_in() is needed for this example
class Reservation:
    @requires_paid
    def check_in(self):
        self._status = 'checked_in'


print(Reservation.check_in.__name__)   # wrapper
```

```python
from functools import wraps


def requires_paid(method):
    @wraps(method)                          # copies method's name onto wrapper
    def wrapper(self):
        if self.status != 'paid':
            print(f'Reservation must be paid in order to use {method.__name__}.')
            return
        return method(self)
    return wrapper


# unchanged from the previous example
class Reservation:
    @requires_paid
    def check_in(self):
        self._status = 'checked_in'


print(Reservation.check_in.__name__)   # check_in
```

**New Concepts:**

- `@wraps(method)` from the `functools` module, placed above `def wrapper`, copies the original method's name and description onto the wrapper.
- `@wraps` changes only how the wrapper describes itself. The wrapper still runs in place of the method.

## Summary

- **Stub:** one paragraph, as in earlier chapters. It covers four things:
  - a status check copied into every method is repeated code, and forgetting one copy lets an invalid change through;
  - a decorator's wrapper is a closure: the wrapper keeps the function or method the decorator was given, and calls that function after the decorator has returned;
  - a decorator takes a function, wraps it, and returns the wrapper, and `@decorator` above a definition is the same as reassigning the name to the decorator's result;
  - a decorator such as `@requires_paid` is a reusable refusal: its wrapper checks the status and returns before the method runs, and a test proves that the guard works by calling the method from the wrong status and asserting that the status did not change.
