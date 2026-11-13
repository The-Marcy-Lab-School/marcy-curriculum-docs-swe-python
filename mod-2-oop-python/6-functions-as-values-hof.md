# 2.6 Functions as Values: Callbacks, Higher-Order Functions, and Closures

**Table of Contents**

- [Key Terms](#key-terms)
- [Two Searches, Written Twice](#two-searches-written-twice)
- [Functions Are Values](#functions-are-values)
- [Passing a Function to a Function](#passing-a-function-to-a-function)
  - [Challenge: Finding Attendees](#challenge-finding-attendees)
- [Passing the Function, Not Its Result](#passing-the-function-not-its-result)
- [Writing a Function Inline with `lambda`](#writing-a-function-inline-with-lambda)
- [Sorting and Choosing with `key=`](#sorting-and-choosing-with-key)
  - [Challenge: The Event Listings](#challenge-the-event-listings)
- [Functions That Return Functions](#functions-that-return-functions)
  - [Closures](#closures)
- [Advanced Topics](#advanced-topics)
  - [`map()` and `filter()`](#map-and-filter)
  - [Sorting by More Than One Value](#sorting-by-more-than-one-value)
  - [A Dictionary of Functions in Place of an `if`/`elif` Chain](#a-dictionary-of-functions-in-place-of-an-ifelif-chain)
  - [Changing a Closed-Over Variable with `nonlocal`](#changing-a-closed-over-variable-with-nonlocal)
- [Summary](#summary)

## Key Terms

- A function treated as a value is considered "**first-class**": Python functions are first class because they can be assigned to a variable, stored in a list, passed as an argument, or returned from another function.
- A **higher-order function** is a function that takes a function as an argument, returns a function, or both. `sorted(events, key=...)` is one: it takes a function in its `key` parameter that tells it how to sort the values in the given list.
- A function passed into another function so that it can be called later, at the moment the receiving function decides, is called a **callback**.
  - A function that takes one value and returns `True` or `False`, such as a function that tells `find_events()` whether one event matches, is called a **predicate**.
- A **`lambda`** is a function written in one expression without a name, such as `lambda event: event.date`. It is most often written directly where a callback is expected.
- A **closure** is formed when an inner function refers to a variable from the function that enclosed it. The inner function keeps access to that variable after the outer function has returned.

## Two Searches, Written Twice

The venue's staff keep asking the program questions about its events. Which events are in December? Which events cost less than $10? Here is a `Venue` with one method for each question:

```python
from datetime import date

class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def events_in_month(self, month):
        return [event for event in self.events if event.date.month == month]

    def events_under(self, price):
        return [event for event in self.events if event.ticket_price() < price]


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15))
hall.add_event(Event('Movie Night: Coco', date(2026, 11, 28), capacity=30, base_price=8))
hall.add_event(Event('Board Game Night', date(2027, 1, 8), capacity=25, base_price=0))

print(hall.events_in_month(12))   # [Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09)]
print(hall.events_under(10))      # [Event('Movie Night: Coco', 2026-11-28), Event('Board Game Night', 2027-01-08)]
```

**<details><summary>Q: Which parts of the two search methods are the same, and which part is different?</summary>**

The same in both:

- The list comprehension that walks through `self.events` and builds a new list.
- The `if` that keeps an event only when a test is `True`.

Different:

- The test itself: `event.date.month == month` in one, and `event.ticket_price() < price` in the other.

</details>

Only one part of each method is about its question, and it is the test inside the `if`. Everything else is the same search, written twice. The repetition has a cost beyond typing. Every new question means a new method on `Venue`, so the venue's author has to foresee every question the staff will ever ask. A staff member who wants the free events, or the events with "Night" in their name, cannot ask until someone edits the `Venue` class to add `free_events()` or `events_named()`, each one another copy of the same loop.

What changes from one question to the next is the test, and the test is a piece of code. If the program could hand that piece of code to the venue as a value, the way it hands over a month or a price, then one search method could answer every question, including questions nobody has thought of yet. Python can do exactly that, because a function is a value like any other. This chapter shows how to treat functions as values, how to pass one into another function, how Python's own `sorted()`, `min()`, and `max()` use the same idea, and how a function can build a new function and hand it back, such as a test for whichever month the staff ask about.

## Functions Are Values

**The Problem:** To hand a test to the venue, the test has to be something a program can store in a variable and pass as an argument, the way it stores and passes a string or a number.

**New Concepts:**

- `def is_free(event):` creates a function and assigns it to the name `is_free`, the same way `price = 0` assigns a number to `price`.
- The name on its own, with no parentheses, is the function itself. `type(is_free)` reports `<class 'function'>`.
- The name followed by parentheses, `is_free(event)`, calls the function, and the call produces whatever the function returns.
- Because a function is a value, it can be given a second name, stored in a list or a dictionary, and passed as an argument. A function that can be used in every way a value can is called a **first-class function**.

**Code:**

```python
def is_free(event):
    return event.ticket_price() == 0


board_games = hall.events[3]

print(type(is_free))         # <class 'function'>
print(is_free)               # <function is_free at 0x104fccd60>: the function itself
print(is_free(board_games))  # True: the value the call returned

check = is_free              # a second name for the same function; nothing is called
print(check(board_games))    # True
```

**<details><summary>Q: Pop quiz! Name the data type stored in each variable below.</summary>**

```python
a = 'Friday Night Jazz'
b = 40
c = True
d = ['A1', 'A2']
e = {'Main Hall': 150}

def f(event):
    return event.ticket_price() == 0
```

1. `a` holds a `str`.
2. `b` holds an `int`.
3. `c` holds a `bool`.
4. `d` holds a `list`.
5. `e` holds a `dict`.
6. `f` holds a function. `print(type(f))` prints `<class 'function'>`.

`def` is an assignment, just like the five lines above it: it creates a function and stores it in the variable `f`.

</details>

{% hint style="warning" %}
**Predict, then run.** The venue's announcements can be printed in two styles, and each style is a function stored in a dictionary. What do the two `print()` calls show?

```python
def shout(message):
    return message.upper()

def whisper(message):
    return message.lower()

styles = {'shout': shout, 'whisper': whisper}

print(styles['shout']('Doors open at 7'))
print(styles['whisper'])
```

<details><summary>What actually happens</summary>

```
DOORS OPEN AT 7
<function whisper at 0x1047a4a40>
```

- `styles['shout']` looks up the function stored under `'shout'`, and the `('Doors open at 7')` after it calls that function, so the line prints what `shout` returned.
- `styles['whisper']` looks up the `whisper` function but never calls it, because no parentheses follow it. Printing a function shows the function itself, with its address in memory.

</details>
{% endhint %}

## Passing a Function to a Function

**The Problem:** `events_in_month()` and `events_under()` differ only in their test. One method that receives the test as a parameter could replace both of them, and every search the staff have not thought of yet.

**New Concepts:**

- A function passed into another function is called a **callback**. The function that receives it is a **higher-order function**.
- Inside the higher-order function, the callback is an ordinary parameter. `find_events()` calls `matches(event)` once for each event, at the moment it decides, and keeps the event when the call returns `True`.
- The higher-order function never names the test. The caller decides what the test is, so the same method answers any question about the events.
- A function that tests something and returns `True` or `False` is often called a predicate. `matches` is a predicate.
- A higher-order function can also return a function. The end of this chapter builds one.

**Code:**

```python
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def find_events(self, matches):
        return [event for event in self.events if matches(event)]


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15))
hall.add_event(Event('Movie Night: Coco', date(2026, 11, 28), capacity=30, base_price=8))
hall.add_event(Event('Board Game Night', date(2027, 1, 8), capacity=25, base_price=0))


def is_in_december(event):
    return event.date.month == 12

def is_free(event):
    return event.ticket_price() == 0


print(hall.find_events(is_in_december))   # [Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09)]
print(hall.find_events(is_free))          # [Event('Board Game Night', 2027-01-08)]
```

{% hint style="warning" %}
**Predict, then run.** This version of the test prints a line every time it runs. What does the program print, and in what order?

```python
def is_cheap(event):
    print(f'Checking {event.name}')
    return event.ticket_price() < 10


cheap = hall.find_events(is_cheap)
print([event.name for event in cheap])
```

<details><summary>What actually happens</summary>

```
Checking Friday Night Jazz
Checking Intro to Pottery
Checking Movie Night: Coco
Checking Board Game Night
['Movie Night: Coco', 'Board Game Night']
```

- `hall.find_events(is_cheap)` hands the `is_cheap` function to `find_events()` without calling it.
- `find_events()` calls `matches(event)` once for each of the four events, in the order they were added, so `is_cheap` prints four lines.
- Only Coco and Board Game Night cost less than $10, so only those two are in the list that `find_events()` returns.

The caller wrote the test, but `find_events()` decided when to run it and how many times.

</details>
{% endhint %}

{% hint style="warning" %}
**Check for understanding.** A higher-order function takes a function as an argument, returns a function, or both. For each call or function below, say whether it is a higher-order function, and if it is, which of the two conditions it meets.

1. `hall.find_events(is_free)`
2. `len(hall.events)`
3. `is_free(board_games)`

<details><summary>Answers</summary>

1. **Higher-order: it takes a function.** `find_events()` receives `is_free` as an argument and calls it on each event.
2. **Not higher-order.** `len()` receives a list, not a function.
3. **Not higher-order.** `is_free()` receives an event and returns `True` or `False`. It is the callback in the first call, not the function receiving one.

</details>
{% endhint %}

### Challenge: Finding Attendees

The venue also keeps a list of attendees. Add a list of attendees to `Venue`, an `add_attendee(attendee)` method, and a higher-order method `find_attendees(matches)` that returns a new list of the attendees for whom `matches` returns `True`. Then call it twice, with two different named functions: once for the attendees whose email address ends with `@example.com`, and once for the attendees whose name starts with `S`.

```python
from dataclasses import dataclass

@dataclass
class Attendee:
    name: str
    email: str


hall.add_attendee(Attendee('Maya Rodriguez', 'maya@example.com'))
hall.add_attendee(Attendee('Sam Lee', 'sam@school.edu'))
hall.add_attendee(Attendee('Mona Patel', 'mona@example.com'))

print(hall.find_attendees(uses_example_email))
# [Attendee(name='Maya Rodriguez', email='maya@example.com'), Attendee(name='Mona Patel', email='mona@example.com')]
print(hall.find_attendees(name_starts_with_s))
# [Attendee(name='Sam Lee', email='sam@school.edu')]
```

**<details><summary>Solution</summary>**

```python
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []
        self.attendees = []

    def add_event(self, event):
        self.events.append(event)

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def find_events(self, matches):
        return [event for event in self.events if matches(event)]

    def find_attendees(self, matches):
        return [attendee for attendee in self.attendees if matches(attendee)]


def uses_example_email(attendee):
    return attendee.email.endswith('@example.com')

def name_starts_with_s(attendee):
    return attendee.name.startswith('S')
```

- `find_attendees()` has the same shape as `find_events()`: it walks through a list and keeps each element for which the callback returns `True`.
- Each callback receives one attendee and returns `True` or `False`, so `find_attendees()` can call it on every attendee without knowing what it tests.
- `uses_example_email` and `name_starts_with_s` are passed without parentheses, because `find_attendees()` calls them itself.

</details>

## Passing the Function, Not Its Result

**The Problem:** Writing `hall.find_events(is_free())` looks almost the same as `hall.find_events(is_free)`, but the parentheses call `is_free` too early, before `find_events()` has an event to give it, and the program stops with an error that seems to have nothing to do with searching.

**New Concepts:**

- Python works out every argument before it calls a function. In `hall.find_events(is_free())`, it runs `is_free()` first, and `find_events()` never starts.
- `is_free()` with nothing in the parentheses is a call that is missing its `event` argument, so Python raises a `TypeError` that names the missing parameter.
- Passing a callback means writing its name with no parentheses. The higher-order function adds the parentheses, and the argument, when it calls the callback.

**Code:**

```python
print(hall.find_events(is_free))     # [Event('Board Game Night', 2027-01-08)]

hall.find_events(is_free())
# TypeError: is_free() missing 1 required positional argument: 'event'
```

**<details><summary>Q: Why does the error mention `is_free()` instead of `find_events()`?</summary>**

The error happens before `find_events()` runs:

- Python works out the argument first, so it runs `is_free()`.
- `is_free` has one parameter, `event`, and the call passes nothing, so the call fails with a `TypeError`.
- The `TypeError` stops the line, so `find_events()` is never called.

The message names `is_free()` because that is the call that broke. The fix is to remove the parentheses, so that `find_events()` receives the function and calls it on each event.

</details>

{% hint style="warning" %}
**Predict, then run.** This time the callback is called with an argument, so no argument is missing. What happens?

```python
board_games = hall.events[3]
hall.find_events(is_free(board_games))
```

<details><summary>What actually happens</summary>

```
TypeError: 'bool' object is not callable
```

- Python works out the argument first: `is_free(board_games)` runs and returns `True`.
- `find_events()` receives `True` as `matches`, not a function.
- Inside `find_events()`, the comprehension tries `matches(event)`, which means `True(event)`, and a `bool` cannot be called, so Python raises a `TypeError`.

This time the error comes from inside `find_events()`, one step away from the line that made the mistake. In both versions the cure is the same: pass `is_free`, the function, not the value a call to it returns.

</details>
{% endhint %}

## Writing a Function Inline with `lambda`

**The Problem:** A test that is one line long and used once still needs a `def`, a name, and a place in the file above the call. A reader of `hall.find_events(is_cheap)` has to look somewhere else to find out what "cheap" means.

**New Concepts:**

- A **`lambda`** writes a function in one expression, right where it is used: `lambda event: event.ticket_price() < 10`.
- The parameters come before the colon, and the expression after the colon is what the function returns. A `lambda` has no `return` keyword, and it can hold only one expression.
- `lambda event: event.ticket_price() < 10` and a `def is_cheap(event):` that returns the same expression are the same function, except that the `lambda` has no name.
- Use a `lambda` for a callback that fits comfortably on one line and is used in one place. Once a test needs a second line or a name to explain it, use `def`. PEP 8 also says not to assign a `lambda` to a name, as in `is_cheap = lambda event: ...`, because `def` does the same job and gives the function a name that shows up in error messages.

**Code:**

```python
print(hall.find_events(lambda event: event.ticket_price() < 10))
# [Event('Movie Night: Coco', 2026-11-28), Event('Board Game Night', 2027-01-08)]

print(hall.find_events(lambda event: 'Night' in event.name))
# [Event('Friday Night Jazz', 2026-12-05), Event('Movie Night: Coco', 2026-11-28), Event('Board Game Night', 2027-01-08)]
```

{% hint style="warning" %}
**Check for understanding.** Rewrite each search as a single call to `hall.find_events()` with a `lambda`, and say what each search returns.

1. The events with a capacity of 30 or more.
2. The events that take place in 2027.

<details><summary>Answers</summary>

```python
print(hall.find_events(lambda event: event.capacity >= 30))
# [Event('Friday Night Jazz', 2026-12-05), Event('Movie Night: Coco', 2026-11-28)]

print(hall.find_events(lambda event: event.date.year == 2027))
# [Event('Board Game Night', 2027-01-08)]
```

- Each `lambda` receives one event, named `event` before the colon, and returns `True` or `False` from the expression after the colon.
- Friday Night Jazz holds 40 and Coco holds 30, so they are the only events with a capacity of 30 or more.
- Board Game Night is the only event dated in 2027.

</details>
{% endhint %}

## Sorting and Choosing with `key=`

**The Problem:** `sorted()` can put numbers or strings in order, but it cannot put events in order, because Python does not know whether one event is less than another. Sorting a list of prices first loses track of which event each price belongs to, and the staff need the events themselves in order, by date or by price.

**New Concepts:**

- `sorted()` is a built-in higher-order function. Its `key` parameter takes a callback, and `sorted()` calls it once on each element to get the value to compare.
- `key` decides the order, but it never changes the elements: `sorted(hall.events, key=...)` still returns the events, not their dates or prices.
- `key` takes a named function or a `lambda`, written without parentheses, because `sorted()` calls it itself. `reverse=True` still reverses the order.
- `min()` and `max()` take `key` the same way, and return the element whose key is smallest or largest.

**Code:**

```python
def event_date(event):
    return event.date


by_date = sorted(hall.events, key=event_date)                          # a named function
by_date = sorted(hall.events, key=lambda event: event.date)            # the same order, with a lambda
print([event.name for event in by_date])
# ['Movie Night: Coco', 'Friday Night Jazz', 'Intro to Pottery', 'Board Game Night']

by_price = sorted(hall.events, key=lambda event: event.ticket_price(), reverse=True)
print([event.name for event in by_price])
# ['Friday Night Jazz', 'Intro to Pottery', 'Movie Night: Coco', 'Board Game Night']

print(min(hall.events, key=lambda event: event.ticket_price()))   # Event('Board Game Night', 2027-01-08)
print(max(hall.events, key=lambda event: event.capacity))         # Event('Friday Night Jazz', 2026-12-05)
```

{% hint style="warning" %}
**Predict, then run.** What happens when `sorted()` is given the events with no `key`?

```python
print(sorted(hall.events))
```

<details><summary>What actually happens</summary>

```
TypeError: '<' not supported between instances of 'Event' and 'Event'
```

- `sorted()` puts elements in order by asking whether one is less than another, which is the `<` operator.
- `Event` defines no way to compare two events with `<`, so the first comparison fails with a `TypeError`.
- With `key=lambda event: event.date`, `sorted()` compares dates instead, and Python already knows how to compare two dates.

</details>
{% endhint %}

### Challenge: The Event Listings

The venue's website shows its events three ways. Using `sorted()`, `min()`, and `max()` with `key`, print:

1. The names of the events, from the latest date to the earliest.
2. The name of the event with the fewest seats.
3. The names of the events in alphabetical order by name.

```python
# 1. ['Board Game Night', 'Intro to Pottery', 'Friday Night Jazz', 'Movie Night: Coco']
# 2. Intro to Pottery
# 3. ['Board Game Night', 'Friday Night Jazz', 'Intro to Pottery', 'Movie Night: Coco']
```

**<details><summary>Solution</summary>**

```python
latest_first = sorted(hall.events, key=lambda event: event.date, reverse=True)
print([event.name for event in latest_first])

smallest = min(hall.events, key=lambda event: event.capacity)
print(smallest.name)

by_name = sorted(hall.events, key=lambda event: event.name)
print([event.name for event in by_name])
```

- Each `key` receives one event and returns the value to compare: a date, a capacity, or a name.
- `reverse=True` turns earliest-first into latest-first.
- `min()` returns the event itself, so `.name` reads its name. Intro to Pottery has 12 seats, the fewest.

</details>

## Functions That Return Functions

**The Problem:** A staff member types in a month, and the program has to find that month's events. `find_events()` calls its callback with one argument, the event, so the callback has no way to receive the month as a second argument. Writing one test per month, `is_in_december()`, `is_in_january()`, and ten more like them, brings back the repetition `find_events()` was meant to remove.

**New Concepts:**

- A function can be defined inside another function. The **inner function** is created each time the outer function runs.
- `return matches`, with no parentheses, hands back the inner function itself. The caller can store it in a variable or pass it straight to `find_events()`.
- Calling the outer function and calling the function it returns are two separate steps, and they happen at different times: `matches_month(12)` builds the test, and `find_events()` calls the test later, once for each event.
- `matches_month` is a higher-order function by the second condition: it returns a function.

**Code:**

```python
def matches_month(month):
    def matches(event):
        return event.date.month == month
    return matches


in_december = matches_month(12)
print(in_december)                          # <function matches_month.<locals>.matches at 0x1004831c0>
print(hall.find_events(in_december))        # [Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09)]
print(hall.find_events(matches_month(1)))   # [Event('Board Game Night', 2027-01-08)]
```

{% hint style="warning" %}
**Predict, then run.** Someone changes the last line of `matches_month()` from `return matches` to `return matches()`. What happens when the program calls `matches_month(12)`?

```python
def matches_month(month):
    def matches(event):
        return event.date.month == month
    return matches()


in_december = matches_month(12)
```

<details><summary>What actually happens</summary>

```
TypeError: matches_month.<locals>.matches() missing 1 required positional argument: 'event'
```

- `matches()` with parentheses calls the inner function immediately, inside `matches_month()`, instead of handing it back.
- `matches` requires an `event`, and the call passes none, so Python raises a `TypeError` before `matches_month()` can return anything.

Read the message in two parts: `matches_month.<locals>.matches()` names the function that was called, the `matches` defined inside `matches_month`, and `missing 1 required positional argument: 'event'` says what the call left out.

</details>
{% endhint %}

{% hint style="warning" %}
**Check for understanding.** A higher-order function takes a function as an argument, returns a function, or both. For each function below, say whether it is a higher-order function, and if it is, which of the two conditions it meets.

1. `sorted()`, called as `sorted(hall.events, key=event_date)`
2. `matches_month`
3. `in_december`, the function that `matches_month(12)` returned

<details><summary>Answers</summary>

1. **Higher-order: it takes a function.** `sorted()` receives `event_date` in its `key` parameter and calls it on each event.
2. **Higher-order: it returns a function.** `matches_month(12)` hands back the inner `matches` function without calling it.
3. **Not higher-order.** `in_december` receives one event and returns `True` or `False`. It is a predicate that `find_events()` calls, not a function that takes or returns one.

</details>
{% endhint %}

### Closures

**The Problem:** `find_events()` calls `in_december` long after `matches_month(12)` has returned, and `in_december` still compares each event's month with `12`. A function's parameters normally disappear when the function returns, so it is not obvious how `matches` can still use `month`.

**New Concepts:**

- An inner function that refers to a variable of the function around it keeps access to that variable after the outer function returns. The inner function together with the variables it keeps is called a **closure**, and the inner function is said to close over those variables. `matches` closes over `month`.
- Each call to the outer function creates new variables and a new inner function, so each function it returns has its own copy of what it closed over. `matches_month(12)` and `matches_month(1)` return two closures, one holding `12` and one holding `1`.
- Code outside the closure has no name for the variable it holds: `month` exists only inside the closure, so `print(month)` at the top level raises `NameError: name 'month' is not defined`.

**Code:**

```python
def make_announcer(venue_name):
    def announce(message):
        print(f'{venue_name}: {message}')
    return announce


main_hall = make_announcer('Riverside Community Hall')
main_hall('Doors open at 7.')     # Riverside Community Hall: Doors open at 7.
```

**<details><summary>Q: In the function below, which function is the outer function, which is the inner function, and which variable from the outer function does the inner function refer to?</summary>**

```python
def sort_by_distance_from(prices, target):
    return sorted(prices, key=lambda price: abs(price - target))


print(sort_by_distance_from([8, 30, 25, 15], 20))   # [25, 15, 30, 8]
```

- The outer function is `sort_by_distance_from`.
- The inner function is the `lambda`, which `sorted()` calls once for each price.
- The `lambda` refers to `target`, a parameter of the outer function, so the `lambda` closes over `target`.

Every `lambda` that uses a variable from the function around it is a closure, so you have been writing closures whenever a `key` function used one of the outer function's parameters.

</details>

{% hint style="warning" %}
**Predict, then run.** The venue also announces events in its annex. What do the three calls print?

```python
main_hall = make_announcer('Riverside Community Hall')
annex = make_announcer('Riverside Annex')

main_hall('Doors open at 7.')
annex('Doors open at 8.')
main_hall('Last call.')
```

<details><summary>What actually happens</summary>

```
Riverside Community Hall: Doors open at 7.
Riverside Annex: Doors open at 8.
Riverside Community Hall: Last call.
```

- Each call to `make_announcer()` created a new `venue_name` and a new `announce` function that closes over it.
- `main_hall` closes over `'Riverside Community Hall'`, and `annex` closes over `'Riverside Annex'`.
- Making `annex` did not change `main_hall`, so the third call still announces the main hall.

</details>
{% endhint %}

{% hint style="warning" %}
**Check for understanding.** Open `src/venue.py` in the case study and find `upcoming_events()`:

```python
def upcoming_events(self, today):
    upcoming = self.find_events(lambda event: event.date >= today)
    return sorted(upcoming, key=lambda event: event.date)
```

The method holds two `lambda` functions. For each one, say which function calls it, what it receives, and what it returns. Then say which variable the first `lambda` closes over, and why it can still use that variable when `find_events()` calls it.

<details><summary>Answer</summary>

- The first `lambda` is the callback for `find_events()`. `find_events()` calls it once for each of the venue's events, and it returns `True` when the event's date is today or later.
- The second `lambda` is the `key` for `sorted()`. `sorted()` calls it once for each upcoming event, and it returns that event's date, which is the value `sorted()` compares.
- The first `lambda` closes over `today`, the parameter of `upcoming_events()`. `find_events()` is the function that calls it, and `find_events()` has no variable called `today`, but the `lambda` is a closure, so it keeps access to `today` from the method where it was written.

`upcoming_events()` returns a new list of the events dated today or later, ordered from the earliest date to the latest.

</details>
{% endhint %}

## Advanced Topics

### `map()` and `filter()`

**The Problem:** Code written by other programmers sometimes uses `map()` and `filter()`, two built-in higher-order functions, for jobs that a list comprehension also does.

**New Concepts:**

- `filter(callback, items)` keeps the items for which the callback returns `True`. `map(callback, items)` calls the callback on every item and collects the results.
- Both return an object that produces values one at a time, so `list()` turns the result into a list.
- Python programmers prefer comprehensions for these jobs, because the expression sits in the line instead of inside a callback. Recognize `map()` and `filter()`, and write comprehensions.

**Code:**

```python
cheap = list(filter(lambda event: event.ticket_price() < 10, hall.events))
names = list(map(lambda event: event.name, cheap))
print(names)   # ['Movie Night: Coco', 'Board Game Night']

names = [event.name for event in hall.events if event.ticket_price() < 10]
print(names)   # ['Movie Night: Coco', 'Board Game Night']
```

### Sorting by More Than One Value

**The Problem:** Two events on the same date tie when sorting by date, and their order is left as it was in the list. A listing that should show them alphabetically within each day needs a second value to compare.

**New Concepts:**

- A `key` can return a tuple, such as `(event.date, event.name)`.
- Python compares tuples one position at a time: by the first value, and by the second only when the first values are equal.

**Code:**

```python
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), capacity=15, base_price=10))

by_day_then_name = sorted(hall.events, key=lambda event: (event.date, event.name))
print([event.name for event in by_day_then_name])
# ['Movie Night: Coco', 'Friday Night Jazz', 'Holiday Crafts', 'Intro to Pottery', 'Board Game Night']
```

### A Dictionary of Functions in Place of an `if`/`elif` Chain

**The Problem:** A menu that runs a different function for each choice is often written as a long `if`/`elif` chain, such as the eight branches of `show_menu()` in the case study's `src/menu.py`. Adding a choice means adding another branch.

**New Concepts:**

- A dictionary can map each choice to the function that handles it. Looking up the choice and calling what comes back replaces the whole chain. This pattern is called a **dispatch table**.
- It only works when every function takes the same arguments. In `show_menu()`, `register(venue)` takes one argument and `book_ticket(venue, today)` takes two, which is one reason the case study keeps its `if`/`elif` chain.

**Code:**

```python
def list_events(venue):
    print([event.name for event in venue.events])

def count_events(venue):
    print(len(venue.events))

actions = {'1': list_events, '2': count_events}

choice = '2'
actions[choice](hall)   # 5
```

### Changing a Closed-Over Variable with `nonlocal`

**The Problem:** A closure can read the variables it closes over, but assigning to one, such as adding one to a count, raises an error.

**New Concepts:**

- An assignment such as `count += 1` inside the inner function makes `count` a new variable belonging to the inner function, so Python reads it before it has a value and raises `UnboundLocalError`.
- `nonlocal count` tells Python that `count` belongs to the enclosing function, so the assignment changes the closed-over variable.
- Each counter made by `make_counter()` has its own `count`.

**Code:**

```python
def make_counter():
    count = 0
    def counter():
        count += 1
        return count
    return counter


door = make_counter()
door()
# UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


door = make_counter()
box_office = make_counter()
print(door(), door(), box_office(), door())   # 1 2 1 3
```

## Summary

- **Stub:** one paragraph, as in earlier chapters. It covers six things:
  - a function is a value: its name without parentheses is the function, and with parentheses it is a call;
  - a callback is a function passed into another function, and the higher-order function that receives it decides when to call it;
  - one higher-order method, such as `find_events(matches)`, replaces a separate method for every question;
  - pass the function, not its result, because Python works out arguments before it calls the function;
  - a `lambda` writes a one-line callback where it is used, and `sorted()`, `min()`, and `max()` take one as their `key`;
  - a function can build and return another function, and an inner function that uses a variable of the function around it is a closure, which keeps that variable after the outer function returns.
