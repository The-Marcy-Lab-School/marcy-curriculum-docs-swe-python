# 2.2 Composition, `__repr__`, `__eq__`, and `@dataclass`

**Table of Contents**

- [Key Terms](#key-terms)
- [Objects That Hold Other Objects](#objects-that-hold-other-objects)
  - [Reaching Through One Object to Another](#reaching-through-one-object-to-another)
  - [A Method That Searches the List](#a-method-that-searches-the-list)
  - [Challenge: Events by Month](#challenge-events-by-month)
- [Printing an Instance with `__repr__`](#printing-an-instance-with-__repr__)
  - [`__repr__`](#__repr__)
  - [Challenge: A Readable Performer](#challenge-a-readable-performer)
- [Comparing Instances with `__eq__`](#comparing-instances-with-__eq__)
  - [Designing Refusals](#designing-refusals)
  - [Challenge: Equal Performers](#challenge-equal-performers)
- [Writing Less with `@dataclass`](#writing-less-with-dataclass)
  - [Challenge: Refactor Performer with `@dataclass`](#challenge-refactor-performer-with-dataclass)
- [Putting It Together: Reservations](#putting-it-together-reservations)
  - [Challenge: One Ticket per Attendee](#challenge-one-ticket-per-attendee)
- [Testing That a Venue Refuses a Duplicate](#testing-that-a-venue-refuses-a-duplicate)
- [Advanced Topics](#advanced-topics)
  - [Comparing with an Object of Another Type](#comparing-with-an-object-of-another-type)
  - [Objects with `__eq__` Cannot Be Dictionary Keys](#objects-with-__eq__-cannot-be-dictionary-keys)
  - [`__str__` and `__repr__`](#__str__-and-__repr__)
- [Summary](#summary)

## Key Terms

- **Composition** is one object holding another object, or a list of objects, as an attribute. A `Venue` that stores a list of `Event` objects is composed of them, and `venue.events[0].name` reaches through the venue and its list to the data in one event.
- **`__repr__`** is the method Python calls to turn an object into a string for a programmer to read. Without it, printing an object shows its class name and a memory address, which tells you nothing about which object you are holding.
  ```python
  def __repr__(self):
      return f'Event({self.name!r}, {self.date})'
  ```
- **Identity** is whether two names refer to the same object, which `is` checks. **Equality** is whether two objects hold equal data, which `==` checks.
  - **`__eq__`** is the method Python calls for `==`. Without one, `==` checks identity, so two events holding identical data are not equal.
    ```python
    def __eq__(self, other):
        return self.name == other.name and self.date == other.date
    ```
- A **refusal** is a method turning down an action that would break its object's data, saying why, and changing nothing.
- A **`@dataclass`** is a decorator that writes `__init__`, `__repr__`, and `__eq__` for you, from the attribute names you list. It suits a class that mostly carries data.
  - A **value object** is an object defined entirely by the data it holds, with little or no behavior of its own. Two value objects with equal data are interchangeable.

## Objects That Hold Other Objects

A venue hosts many events, and a program for the venue has to keep track of all of them. Here is a small `Event` class, and a `Venue` class that holds a list of events:

```python
from datetime import date

class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

hall = Venue('Riverside Community Hall')
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
pottery = Event('Intro to Pottery', date(2026, 12, 9), 12)
hall.add_event(jazz)
hall.add_event(pottery)

# You will often see classes instantiated directly in a method call like this
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))
```

- `hall` is an instance of `Venue`, and `hall.events` is a list of `Event` instances.
- `self.events = []` runs once for every venue that is created, so every venue starts with its own empty list.
- `add_event()` puts an event in that list. The rest of the program adds events by asking the venue, so the venue is the one place that decides what goes into its list.

One object holding another object as an attribute is called **composition**. The venue is composed of its events. You have been using composition already: every `Event` holds a `date` object, which the `date` class from the `datetime` module made.

### Reaching Through One Object to Another

To read data inside an object that another object holds, write one step for each object you pass through:

```python
print(hall.events[0].name)         # Friday Night Jazz
print(hall.events[1].date.month)   # 12
```

Read `hall.events[0].name` from left to right, one step at a time:

- `hall.events` is the list stored on the venue.
- `[0]` is the first `Event` in that list.
- `.name` reads that event's name.

`hall.events[1].date.month` takes one more step: from the second event to its `date` object, and from the date to its month.

`self.events.append(event)` stores a reference to the event, not a copy of it. A variable holding a list works the same way: it refers to the list rather than holding a separate copy.

{% hint style="warning" %}
**Predict, then run.** The jazz concert moves to a bigger room. What do the two `print()` calls show?

```python
jazz.capacity = 60

print(hall.events[0].capacity)
print(jazz is hall.events[0])
```

<details><summary>What actually happens</summary>

```
60
True
```

- `hall.add_event(jazz)` stored a reference to the `jazz` event in the venue's list, not a copy, so `jazz` and `hall.events[0]` are two names for one event.
- `jazz.capacity = 60` changes that one event, so reading the capacity through the venue shows the new value.
- `is` checks whether two names refer to the same object, and `jazz` and `hall.events[0]` do.

</details>
{% endhint %}

### A Method That Searches the List

Suppose the application needed a way to know which events occur on a given date.

The venue holds the list of events, so the venue is the natural place for code that searches it. `events_on()` returns the events on one day:

```python
from datetime import date

class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def events_on(self, day):
        return [event for event in self.events if event.date == day]

hall = Venue('Riverside Community Hall')
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
pottery = Event('Intro to Pottery', date(2026, 12, 9), 12)
hall.add_event(jazz)
hall.add_event(pottery)
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))

for event in hall.events_on(date(2026, 12, 5)):
    print(event.name)
# Friday Night Jazz
# Holiday Crafts

print(len(hall.events_on(date(2026, 12, 25)))) # 0
```

- `events_on()` asks each event for its date and returns a **new** list of the events whose date matches. A caller who changes the returned list cannot change the venue's own list.
- A list comprehension is allowed to find no matches, so a day with no events returns `[]` with no special case.

The rest of the program asks the venue for the events on a day instead of looping over `hall.events` itself, so that loop is written in one place.

### Challenge: Events by Month

Add a method `events_in_month(month)` to `Venue` that returns a new list of the venue's events whose date falls in that month, where `month` is a number from 1 to 12.

```python
hall.add_event(Event('New Year Concert', date(2027, 1, 2), 60))

for event in hall.events_in_month(12):
    print(event.name)
# Friday Night Jazz
# Intro to Pottery
# Holiday Crafts

for event in hall.events_in_month(1):
    print(event.name)
# New Year Concert

print(len(hall.events_in_month(7))) # 0
```

**<details><summary>Solution</summary>**

```python
def events_in_month(self, month):
    return [event for event in self.events if event.date.month == month]
```

`event.date.month` reaches through two objects: from the event to its date, and from the date to its month.

</details>

{% hint style="warning" %}
**Check for understanding.** The case study's `src/menu.py` describes a reservation with this function:

```python
def describe(reservation):
    return (f'#{reservation.number}: {reservation.attendee.name}, {reservation.event.name}, '
            f'${reservation.price}, {reservation.status}')
```

Trace `reservation.attendee.name`. What object does `reservation.attendee` give you, and which object is `.name` read from? Why doesn't `Reservation` store the attendee's name as its own attribute?

<details><summary>Answer</summary>

- `reservation.attendee` gives you the `Attendee` object stored on the reservation.
- `.name` reads the name from that `Attendee` object, so the name is the attendee's data, not the reservation's.

The reservation holds a reference to the attendee, so the attendee's details are stored in one place. If the reservation copied the name into its own attribute, a later correction to the attendee's name would leave every reservation showing the old spelling.

</details>
{% endhint %}

## Printing an Instance with `__repr__`

The examples above used a `for` loop to show what `events_on()` returned, because printing the list it returns directly gives you this.

```python
print(hall.events_on(date(2026, 12, 5)))
# [<__main__.Event object at 0x1027ddfd0>, <__main__.Event object at 0x1027bc410>]
```

Each part of `<__main__.Event object at 0x1027ddfd0>` says something, but not much:

- `__main__.Event` is the class, the same name `type()` reports.
- `object at 0x1027ddfd0` is the memory address where this object lives, written in hexadecimal.

The output says what _kind_ of object each one is, but not _which_ event. If a bug left the wrong event in the list, you could not tell by reading the output.

### `__repr__`

Python's built-in operations work on your objects through dunder methods. This section and the next write two of them:

- `print()` calls `__repr__`
- `==` calls `__eq__`

`__repr__` is a dunder method, so you never call it yourself: Python calls it whenever it needs to show an object to a programmer, including when you `print()` one. Whatever string `__repr__` returns is what appears. Here is `Event` with a `__repr__` added, and the venue built again from it:

```python
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'

hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))

print(hall.events[0])     # Python calls __repr__ and prints what it returns -> Event('Friday Night Jazz', 2026-12-05)
print(hall.events)        # [Event('Friday Night Jazz', 2026-12-05), Event('Holiday Crafts', 2026-12-05)]
```

Now each event says which event it is. A list prints each of its elements with that element's `__repr__`, so the venue's whole list becomes readable too.

{% hint style="info" %}
💡 The `!r` inside `{self.name!r}` tells the f-string to show the value the way it would be written in code. For a string, that means with quotes around it: `f'{jazz.name}'` gives `Friday Night Jazz`, while `f'{jazz.name!r}'` gives `'Friday Night Jazz'`. The quotes tell a programmer reading the output that the name is a string, so `Event('7', ...)` and `Event(7, ...)` look different.

The convention is to make `__repr__` look like the code that would create the object: the class name, then the values in parentheses. A programmer can read it and know exactly what they are holding.
{% endhint %}

`__repr__` must **return** its string, because Python uses whatever comes back as the text to show. A `__repr__` that prints its string instead hands back `None`, the value every function returns when it reaches its end without a `return` statement:

```python
def __repr__(self):
    print(f'Event({self.name!r}, {self.date})')    # prints instead of returning

print(hall.events)
# Event('Friday Night Jazz', 2026-12-05)
# TypeError: __repr__ returned non-string (type NoneType)
```

The text appears first, because `__repr__` printed it. Then Python checks what `__repr__` handed back and stops. Read the message in two parts: `__repr__ returned non-string` says what rule was broken, and `(type NoneType)` names what came back instead.

### Challenge: A Readable Performer

The venue books performers for its concerts. Write a class `Performer` whose `__init__` takes a name and a genre and stores both. Give it a `__repr__` so that this code:

```python
blue_notes = Performer('The Blue Notes', 'jazz')
print(blue_notes)
print([blue_notes, Performer('Lena Ortiz', 'folk')])
```

prints:

```
Performer('The Blue Notes', genre='jazz')
[Performer('The Blue Notes', genre='jazz'), Performer('Lena Ortiz', genre='folk')]
```

**<details><summary>Solution</summary>**

```python
class Performer:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f'Performer({self.name!r}, genre={self.genre!r})'
```

- `!r` puts quotes around both strings.
- `genre=` is plain text inside the f-string. It labels the second value, so a reader does not have to remember which argument comes second.

</details>

{% hint style="warning" %}
**Check for understanding.** Here is the `__repr__` of the case study's `Event` class, from `src/events.py`, with its comment removed. `type(self).__name__` is the name of the object's class as a string, such as `'Event'`:

```python
def __repr__(self):
    return f'{type(self).__name__}({self.name!r}, {self.date})'
```

The case study's `Event` takes a name, a date, a capacity, and a base price. What does `print(board_games)` show for `board_games = Event('Board Game Night', date(2026, 12, 18), 25, 5)`? Which parts of the f-string produce quotes in the output, and which do not?

<details><summary>Answer</summary>

```
Event('Board Game Night', 2026-12-18)
```

- `type(self).__name__` gives the class name, `Event`, with no quotes, because it has no `!r`.
- `{self.name!r}` shows the name the way it would be written in code, so it appears in quotes.
- `{self.date}` has no `!r`, so the date appears as `2026-12-18` with no quotes.
- The capacity and the base price are not in the f-string, so they do not appear.

</details>
{% endhint %}

## Comparing Instances with `__eq__`

The venue's staff add events by typing them into a form. If someone types in Friday Night Jazz a second time, the venue should turn it down instead of listing the concert twice. Here is a first attempt: `add_event()` checks whether the event is already in the list before adding it.

```python
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)

hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

print(hall.events)
# [Event('Friday Night Jazz', 2026-12-05), Event('Friday Night Jazz', 2026-12-05)]
```

The check never printed its message, and the concert is now listed twice. Anyone reading the calendar would believe the venue hosts two jazz concerts that night.

The rule behind this: `in` checks each element of the list with `==`, and without an `__eq__` method, `==` on your objects checks **identity**. It asks whether the two names refer to the same object, which is the same question `is` asks. Each call to `Event(...)` creates a new object, so the event the staff typed in a second time is a different object from the one in the list, even though it holds the same data:

```python
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
jazz_again = Event('Friday Night Jazz', date(2026, 12, 5), 40)

print(jazz == jazz_again)   # False
print(jazz is jazz_again)   # False
```

To make `==` compare the data instead, which is **equality**, write `__eq__`. When Python evaluates `jazz == jazz_again`, it calls `jazz.__eq__(jazz_again)`: the object on the left of `==` arrives as `self`, and the object on the right arrives as the parameter, named `other` by convention. Whatever `__eq__` returns is the result of the `==`. Below we decide that if two events share a name and a date, they are equal:

```python
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date

jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
jazz_again = Event('Friday Night Jazz', date(2026, 12, 5), 40)

print(jazz == jazz_again)   # Python calls jazz.__eq__(jazz_again) -> True: same name, same date
print(jazz is jazz_again)   # False: still two separate objects
```

Defining `__eq__` changes what `==` means for events. It does not change what `is` means: `jazz` and `jazz_again` are still two objects, so `is` still says `False`. Identity and equality are two different questions, and now they can have two different answers.

`in` uses `==`, so the venue's check now finds the concert. Built again from this `Event` class, the venue turns the second concert down:

```python
hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
# Friday Night Jazz on 2026-12-05 is already on the calendar.

print(hall.events)
# [Event('Friday Night Jazz', 2026-12-05)]
```

{% hint style="warning" %}
**Predict, then run.** The venue holds one Friday Night Jazz, on December 5. A staff member types in the concert again with a capacity of 60, and then a second concert a week later. What does each call print, and how many events does the venue hold at the end?

```python
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 60))
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 12), 40))
print(len(hall.events))
```

<details><summary>What actually happens</summary>

```
Friday Night Jazz on 2026-12-05 is already on the calendar.
2
```

- The first new event has the same name and date as the stored concert. `__eq__` leaves out the capacity, so `in` finds a match and `add_event()` refuses it.
- The second new event has a different date, so `__eq__` returns `False` for it, `in` finds no match, and `add_event()` adds it.
- The venue ends with the original concert and the one on December 12.

</details>
{% endhint %}

### Designing Refusals

`add_event()` just made a **refusal**. It turned down an action that would have left the venue's list wrong, it printed a message that says why, and it left the list as it was. You have seen a class refuse before, whenever an event turns down a ticket sale because it is sold out. Refusing is how a class keeps its data correct when other code asks it to do something that would break it, and the rest of this module adds more ways for a class to refuse.

Deciding which attributes go into `__eq__` is a design decision. This `__eq__` compares the name and the date and leaves out the capacity, because an event moved to a bigger room is still the same event. If two events with the same name on the same day could be genuinely different events at your venue, the `__eq__` would need another attribute, such as the room.

### Challenge: Equal Performers

Add an `__eq__` method to your `Performer` class so that two performers are equal when they have the same name and the same genre:

```python
print(Performer('The Blue Notes', 'jazz') == Performer('The Blue Notes', 'jazz'))  # True
print(Performer('The Blue Notes', 'jazz') == Performer('The Blue Notes', 'blues')) # False
```

**<details><summary>Solution</summary>**

```python
class Performer:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f'Performer({self.name!r}, genre={self.genre!r})'

    def __eq__(self, other):
        return self.name == other.name and self.genre == other.genre
```

Both comparisons have to be `True` for `and` to return `True`, so a performer with the same name but a different genre is not equal.

</details>

{% hint style="warning" %}
**Check for understanding.** Open `src/venue.py` in the case study and find `add_event()`. Then open `src/events.py` and find the `__eq__` method of the `Event` class.

A staff member types in an event with the same name and date as one already on the calendar, but with a different capacity, and the program calls `venue.add_event(event)`. Which line of `add_event()` finds the match, which method does that line cause Python to call, and what does `add_event()` print and return?

<details><summary>Answer</summary>

- `if event in self._events:` finds the match. `in` compares the new event with each stored event using `==`.
- `==` causes Python to call `Event.__eq__`, which compares only the name and the date, so the different capacity does not matter and the stored event matches.
- `add_event()` prints `<name> on <date> is already on the calendar.` and returns `None`, without adding the event.

</details>
{% endhint %}

## Writing Less with `@dataclass`

`Performer` now has three methods, and every attribute name appears in all three: once as a parameter and an assignment in `__init__`, once in `__repr__`, and once in `__eq__`. Here is the same pattern for a seat in the venue's balcony:

```python
class Seat:
    def __init__(self, section, row, number):
        self.section = section
        self.row = row
        self.number = number

    def __repr__(self):
        return f'Seat(section={self.section!r}, row={self.row!r}, number={self.number!r})'

    def __eq__(self, other):
        return (self.section == other.section
                and self.row == other.row
                and self.number == other.number)
```

That is eleven lines to say "a seat has a section, a row, and a number". Adding a fourth attribute means editing three methods, and forgetting the edit to `__eq__` leaves seats that compare as equal while holding different data, with no error to point at the mistake.

A class like `Seat` mostly carries data, and for that kind of class Python can write the three methods for you. The `@dataclass` line placed above the class does it:

```python
from dataclasses import dataclass

@dataclass
class Seat:
    section: str
    row: str
    number: int

front_row = Seat('Balcony', 'B', 12)
same_seat = Seat('Balcony', 'B', 12)

print(front_row)               # Seat(section='Balcony', row='B', number=12)
print(front_row == same_seat)  # True
print(front_row is same_seat)  # False
```

Here's how it works:

- `from dataclasses import dataclass` imports it from the standard library.
- A line that starts with `@` and sits directly above a class changes the class it sits above. `@dataclass` reads the class body and writes `__init__`, `__repr__`, and `__eq__` for the class.
- Each attribute is listed once, in the class body, in the order `__init__` will take its arguments. `Seat('Balcony', 'B', 12)` stores `'Balcony'` as `section`, `'B'` as `row`, and `12` as `number`.
- `: str` and `: int` are **type annotations**: notes saying what type of value each attribute is meant to hold. `@dataclass` requires one for every attribute, because the annotation is how it finds the attribute names. Python does not check them, so `Seat('Floor', 'A', '3')` is created without complaint, with the string `'3'` as its number.
- The generated `__eq__` compares every listed attribute, in order. Add an attribute to the list and it is included in `__init__`, `__repr__`, and `__eq__` automatically.

A seat is a **value object**: it is defined entirely by its data. Two `Seat` objects for balcony row B, seat 12, describe the same seat, and it doesn't matter which one your program holds. Value objects are what `@dataclass` suits best.

A class whose `__init__` has to do more than store its arguments is better written by hand. The case study's `Reservation` is a plain class for this reason: its `__init__` calls `event.ticket_price()` to work out the price and sets the status to `'reserved'`, and the `__init__` that `@dataclass` writes only stores the arguments it is given. Its `Attendee` class, which holds just a name and an email address, is a dataclass.

### Challenge: Refactor Performer with `@dataclass`

Rewrite your `Performer` class with `@dataclass`, so that it defines no methods by hand. Then confirm that it behaves the same as before: run the `print()` calls from Challenge: A Readable Performer and the `==` comparisons from Challenge: Equal Performers, and compare the output.

**<details><summary>Solution</summary>**

```python
from dataclasses import dataclass

@dataclass
class Performer:
    name: str
    genre: str

blue_notes = Performer('The Blue Notes', 'jazz')
print(blue_notes)
# Performer(name='The Blue Notes', genre='jazz')
print(Performer('The Blue Notes', 'jazz') == Performer('The Blue Notes', 'jazz'))   # True
print(Performer('The Blue Notes', 'jazz') == Performer('The Blue Notes', 'blues'))  # False
```

The comparisons give the same results. The printed form is slightly different: the generated `__repr__` labels every value, so it shows `name='The Blue Notes'` where the hand-written one showed only `'The Blue Notes'`. It still identifies the performer, and it still looks like the code that would create one.

</details>

{% hint style="warning" %}
**Check for understanding.** The case study's `Attendee` class, in `src/attendee.py`, is a dataclass. Its `Event` class, in `src/events.py`, is a plain class whose hand-written `__eq__` compares the name and the date:

```python
@dataclass
class Attendee:
    name: str
    email: str
```

What do the two `print()` calls show, and why do they give different answers?

```python
board_games = Event('Board Game Night', date(2026, 12, 18), 25, 5)
board_games_bigger = Event('Board Game Night', date(2026, 12, 18), 40, 8)
print(board_games == board_games_bigger)

maya = Attendee('Maya Rodriguez', 'maya@example.com')
maya_new_email = Attendee('Maya Rodriguez', 'maya.r@example.com')
print(maya == maya_new_email)
```

<details><summary>Answer</summary>

```
True
False
```

- `Event`'s hand-written `__eq__` compares only the name and the date. The two events match on both, so they are equal, even though their capacities and prices differ.
- `Attendee`'s `__eq__` was written by `@dataclass`, which compares every listed attribute. The emails differ, so the two attendees are not equal.

Writing `__eq__` by hand lets you choose which attributes make two objects the same. `@dataclass` compares all of them.

</details>
{% endhint %}

## Putting It Together: Reservations

A reservation connects one attendee to one event, so a `Reservation` holds an `Attendee` object and an `Event` object as its attributes. This `Reservation` only stores those two objects, so unlike the case study's, it can be a dataclass, and so can `Attendee`. `Event` is the class from Comparing Instances with `__eq__`, with its hand-written `__repr__` and `__eq__`:

```python
from dataclasses import dataclass

@dataclass
class Attendee:
    name: str
    email: str

@dataclass
class Reservation:
    attendee: Attendee
    event: Event
```

`attendee: Attendee` is a type annotation that names one of your own classes, saying that the `attendee` attribute is meant to hold an `Attendee` object.

{% hint style="warning" %}
**Predict, then run.** What do the four `print()` calls show?

```python
hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

maya = Attendee('Maya Rodriguez', 'maya@example.com')
first = Reservation(maya, hall.events[0])
print(first)
print(first.attendee.name)

second = Reservation(Attendee('Maya Rodriguez', 'maya@example.com'),
                     Event('Friday Night Jazz', date(2026, 12, 5), 60))
print(first == second)
print(first.event is hall.events[0])
```

<details><summary>What actually happens</summary>

```
Reservation(attendee=Attendee(name='Maya Rodriguez', email='maya@example.com'), event=Event('Friday Night Jazz', 2026-12-05))
Maya Rodriguez
True
True
```

- `print(first)` calls the `__repr__` that `@dataclass` wrote for `Reservation`. That `__repr__` shows each attribute with the attribute's own `__repr__`, so the attendee appears as the dataclass wrote it, and the event appears as `Event`'s hand-written `__repr__` wrote it.
- `first.attendee.name` reaches through the reservation to its `Attendee` object, and reads that attendee's name.
- `first == second` calls the `__eq__` that `@dataclass` wrote for `Reservation`, which compares the attendees with `==` and then the events with `==`. The attendees hold the same name and email, so `Attendee`'s `__eq__` says they are equal. The events share a name and a date, so `Event`'s `__eq__` says they are equal, even though the capacities differ. Both comparisons are `True`, so the reservations are equal.
- `first.event is hall.events[0]` is `True`, because `Reservation(maya, hall.events[0])` stored a reference to the event in the venue's list, not a copy of it.

Each object answers for its own part: printing a reservation asks each of its objects to print itself, and comparing two reservations asks each pair of objects to compare themselves.

</details>
{% endhint %}

### Challenge: One Ticket per Attendee

Give `Venue` a list of reservations, and a `book(attendee, event)` method that creates a `Reservation`, adds it to the list, and returns it. An attendee may hold only one ticket for an event, so `book()` must refuse a second reservation for the same attendee and event: it prints `<attendee's name> already has a ticket for <event's name>.`, adds nothing, and returns `None`.

```python
hall = Venue('Riverside Community Hall')
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
hall.add_event(jazz)

hall.book(Attendee('Maya Rodriguez', 'maya@example.com'), jazz)
hall.book(Attendee('Maya Rodriguez', 'maya@example.com'), jazz)
# Maya Rodriguez already has a ticket for Friday Night Jazz.
hall.book(Attendee('Sam Lee', 'sam@example.com'), jazz)

print(hall.reservations)
# [Reservation(attendee=Attendee(name='Maya Rodriguez', email='maya@example.com'), event=Event('Friday Night Jazz', 2026-12-05)), Reservation(attendee=Attendee(name='Sam Lee', email='sam@example.com'), event=Event('Friday Night Jazz', 2026-12-05))]
```

**<details><summary>Solution</summary>**

```python
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []
        self.reservations = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)

    def book(self, attendee, event):
        reservation = Reservation(attendee, event)
        if reservation in self.reservations:
            print(f'{attendee.name} already has a ticket for {event.name}.')
            return None
        self.reservations.append(reservation)
        return reservation
```

- `self.reservations = []` gives every venue its own list of reservations, the same way `self.events = []` does.
- `reservation in self.reservations` compares the new reservation with each stored one using the `__eq__` that `@dataclass` wrote, which compares the attendees and then the events. The second booking for Maya matches the first, so `book()` refuses it.
- Sam's booking has a different attendee, so it matches nothing and is added.

</details>

## Testing That a Venue Refuses a Duplicate

A refusal that stops working doesn't crash anything. The venue just lists the same concert twice, and a user is the first to notice. A test can catch the mistake the moment it is made, by adding an equal event a second time and checking that the venue still holds one.

Make a folder called `events-practice`, then create and activate a virtual environment in it and install `pytest`. Set it up the way every Mod 2 repository is set up, with the code in `src/` and the tests in `tests/`:

```
events-practice/
├── .venv/
├── pytest.ini
├── src/
│   └── venue.py
└── tests/
    └── test_venue.py
```

The test file lives in `tests/`, but the classes it imports live in `src/`, so pytest has to be told where to look. `pytest.ini` holds two settings. `pythonpath = src` lets the test file import from the `src` folder with `from venue import Event, Venue`, and `testpaths = tests` tells pytest where the tests are:

```
[pytest]
pythonpath = src
testpaths = tests
```

`src/venue.py` holds the two classes:

```python
# src/venue.py
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)
```

`tests/test_venue.py` holds two tests:

```python
# tests/test_venue.py
from datetime import date

from venue import Event, Venue


def test_adding_an_equal_event_again_is_refused():
    hall = Venue('Riverside Community Hall')
    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

    assert len(hall.events) == 1


def test_an_event_on_another_day_is_added():
    hall = Venue('Riverside Community Hall')
    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 12), 40))

    assert len(hall.events) == 2
```

Run them from inside `events-practice`:

```sh
pytest
```

Both tests pass. Each test builds its own venue, so nothing one test adds can reach the other.

- The first test adds an event that is equal to one already stored. It fails if `add_event()` lets the duplicate in.
- The second test adds an event on a different day. It fails if `add_event()` refuses too much, for example if `__eq__` compared only the names.

{% hint style="warning" %}
**Predict, then run.** In `src/venue.py`, delete the `__eq__` method from `Event`, and run `pytest` again. Which test fails, and what does pytest show?

<details><summary>What actually happens</summary>

Only the first test fails:

```
>       assert len(hall.events) == 1
E       AssertionError: assert 2 == 1
E        +  where 2 = len([Event('Friday Night Jazz', 2026-12-05), Event('Friday Night Jazz', 2026-12-05)])
E        +    where [Event('Friday Night Jazz', 2026-12-05), Event('Friday Night Jazz', 2026-12-05)] = <venue.Venue object at 0x104fa6ff0>.events
```

- Without `__eq__`, `in` checks identity, and the second Friday Night Jazz is a different object, so `add_event()` adds it and the venue holds two events.
- The second test still passes, because an event on a different day was never meant to match.
- The lines that start with `+ where` are pytest working out where each value came from. It prints each event with `Event`'s `__repr__`, so you can read that the venue holds the same concert twice. `Venue` has no `__repr__`, so the venue itself appears as `<venue.Venue object at 0x104fa6ff0>`.

A readable `__repr__` pays off in a failing test as much as in a `print()` call. Put the `__eq__` method back before moving on.

</details>
{% endhint %}

{% hint style="warning" %}
**Check for understanding.** The case study's `tests/test_attendee.py` holds two tests. `repr(attendee)` calls the attendee's `__repr__` and returns the string it gives back:

```python
def test_two_attendees_with_the_same_data_are_equal():
    assert Attendee('Maya Rodriguez', 'maya@example.com') == Attendee('Maya Rodriguez', 'maya@example.com')


def test_the_dataclass_writes_a_readable_repr():
    attendee = Attendee('Maya Rodriguez', 'maya@example.com')

    assert repr(attendee) == "Attendee(name='Maya Rodriguez', email='maya@example.com')"
```

Suppose someone removed the `@dataclass` line from `Attendee` and wrote an `__init__` by hand that stores the name and the email. Which of the two tests would fail, and why?

<details><summary>Answer</summary>

Both would fail:

- The first test compares two separately created attendees with `==`. Without the `__eq__` that `@dataclass` wrote, `==` checks identity, and two separate objects are not identical, so the assertion is `False`.
- The second test compares the printed form with an exact string. Without the `__repr__` that `@dataclass` wrote, `repr(attendee)` gives the default `<attendee.Attendee object at 0x...>`, which does not match.

So these tests protect the two methods that `@dataclass` writes beyond `__init__`, which a hand-written class would have to write itself.

</details>
{% endhint %}

## Advanced Topics

### Comparing with an Object of Another Type

The `__eq__` written earlier assumes `other` has a `name` and a `date`. Comparing an event with something else, such as a string, breaks that assumption:

```python
print(jazz == 'Friday Night Jazz')
# AttributeError: 'str' object has no attribute 'name'
```

`__eq__` received the string as `other` and tried to read `other.name`, which strings don't have. The fix is to check the type first and return `NotImplemented` when it doesn't match. `isinstance(other, Event)` asks whether `other` was made from the `Event` class:

```python
def __eq__(self, other):
    if not isinstance(other, Event):
        return NotImplemented
    return self.name == other.name and self.date == other.date
```

`NotImplemented` is a special value that tells Python "this method doesn't know how to compare these two objects." Python then falls back to its own answer, which for unrelated objects is identity, so `jazz == 'Friday Night Jazz'` is `False` instead of a crash. The `__eq__` that `@dataclass` writes already does this check.

### Objects with `__eq__` Cannot Be Dictionary Keys

A dictionary finds a value by working out a number from its key, called a **hash**, and two keys that are equal must produce the same number. When a class defines `__eq__`, Python can no longer be sure its default hash agrees with the new idea of equality, so it removes the hash altogether:

```python
tickets_sold = {jazz: 3}
# TypeError: cannot use 'Event' as a dict key (unhashable type: 'Event')
```

The same applies to a dataclass, because `@dataclass` writes an `__eq__`. When you need a lookup table of events, key it by something hashable that identifies the event, such as its name. The case study's `Venue` does this with attendees: its `_attendees` dictionary is keyed by email address, a string, rather than by `Attendee` objects.

### `__str__` and `__repr__`

Python has a second dunder method for turning an object into a string: `__str__`, which is meant for the user rather than the programmer. When a class defines both, `print(obj)` and `f'{obj}'` use `__str__`, while a printed list and `f'{obj!r}'` use `__repr__`. When a class defines only `__repr__`, Python uses it everywhere. Start with `__repr__`, and add `__str__` only when users need to see an object written differently from how a programmer needs to see it.

## Summary

Programs hold many objects at once, and composition is one object holding others as attributes: a `Venue` holds a list of `Event` objects, and `venue.events[0].name` reaches through the venue and its list to one event's data. An attribute stores a reference to the object it holds, not a copy. Once a program holds many objects, it has to tell them apart, and Python's built-in operations reach your objects through dunder methods. `print()` calls `__repr__`, so a printed list of events, or a failing test, shows which event is which. `==` calls `__eq__`, and without one, `==` checks identity, whether two names refer to the same object, which `is` checks. `in` compares with `==`, so an `__eq__` that compares an event's name and date lets the venue find an event it already holds and refuse to add it twice. That refusal turns down an action that would break the venue's data, says why, and changes nothing. `@dataclass` writes `__init__`, `__repr__`, and `__eq__` from the attribute names you list, which suits a class that mostly carries data, and a dataclass that holds other objects prints and compares them with their own `__repr__` and `__eq__`.
