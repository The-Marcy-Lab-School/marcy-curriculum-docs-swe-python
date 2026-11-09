# 2.1 Intro to OOP: Classes, `__init__`, and `self`

**Table of Contents**:

- [Key Terms](#key-terms)
- [The Case Study: Venue Tickets](#the-case-study-venue-tickets)
- [How a Method Reaches Its Value](#how-a-method-reaches-its-value)
  - [Idea 1. Every Value Comes from a Class](#idea-1-every-value-comes-from-a-class)
  - [Idea 2. The Methods Available to a Value Live in its Class](#idea-2-the-methods-available-to-a-value-live-in-its-class)
  - [Idea 3. The Value Before the Dot Is the First Argument](#idea-3-the-value-before-the-dot-is-the-first-argument)
  - [Challenge: Rewrite the Call](#challenge-rewrite-the-call)
- [Classes and Instances](#classes-and-instances)
  - [Defining a Class](#defining-a-class)
  - [`__init__` Gives Every Instance the Same Shape](#__init__-gives-every-instance-the-same-shape)
  - [Data Goes on `self`](#data-goes-on-self)
- [Methods and `self`](#methods-and-self)
  - [Writing a Method](#writing-a-method)
  - [`self` Is the Value Before the Dot](#self-is-the-value-before-the-dot)
  - [A Method That Takes Arguments](#a-method-that-takes-arguments)
  - [Challenge: Room Rentals](#challenge-room-rentals)
- [Encapsulation and the Interface](#encapsulation-and-the-interface)
  - [Parallel Lists Drift Apart](#parallel-lists-drift-apart)
  - [Dictionaries Keep the Data Together but Not the Rules](#dictionaries-keep-the-data-together-but-not-the-rules)
  - [One Place for the Data and Its Rules](#one-place-for-the-data-and-its-rules)
  - [The Interface](#the-interface)
  - [Dictionary or Class?](#dictionary-or-class)
  - [Case Study Check: The Event Interface](#case-study-check-the-event-interface)
- [Advanced Topics](#advanced-topics)
  - [Calling a Method Through the Wrong Class](#calling-a-method-through-the-wrong-class)
- [Summary](#summary)

## Key Terms

- **Object-oriented programming (OOP)** is a way of organizing a program around objects, where each object holds its own data and the methods that work on that data.
  - The act of bundling data and the methods that work on that data is called **encapsulation**.
  - The resulting bundle of attributes and methods that the rest of the program uses to interact with the data is called an **interface**.
  - As a result, the rest of the program is constrained to change the data through those methods rather than from anywhere in the program.
- A **class** is a blueprint for making "objects" that conform to an interface of your own design. The `class` syntax names the "attributes" an object will hold and defines the "methods" that are available.
  - An **object**, also called an **instance**, is one thing made from a class. Each instance of the same class holds separate data.
  - An **attribute** is a piece of data stored on an object, reached with a dot: `event.name`.
  - A **method** is a function defined inside a class. It is called on an object, and it can read and change that object's attributes.
  - **`__init__`** is the method Python runs when you create an instance. It receives the arguments passed to the class and stores them as attributes.
    ```python
    class Event:
        def __init__(self, name, date, capacity):
            self.name = name
            self.date = date
            self.capacity = capacity
        def can_refund(self, today):
            return today < self.date
    ```
  - **Instantiation** is the act of making an instance by invoking the class name. Python invokes the `__init__` method for you:
    ```py
    jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
    ```
  - **`self`** is the first parameter of every method, and it refers to the instance the method was called on. `jazz.can_refund(today)` passes `jazz` in as `self`.
  - A **dunder method** is a method whose name begins and ends with two underscores, such as `__init__`. Python calls them for you at the right moment.
- **Introspection** is asking an object about itself while the program is running.
  - **`type(obj)`** returns the class an object was made from. `type('hello')` returns `<class 'str'>`.
  - **`dir(obj)`** returns the names of everything the object answers to, including its methods.

## The Case Study: Venue Tickets

Every lesson in this module uses one application: a ticketing system for Riverside Community Hall, a community venue that hosts concerts, workshops, and movie screenings. Attendees book tickets, pay for them, check in at the door, and ask for refunds, and the system refuses any action that breaks one of the venue's rules.

Clone it into your `development/mod-2` folder and run it:

```sh
git clone git@github.com:The-Marcy-Lab-School/swe-casestudy-2-venue-tickets.git
cd swe-casestudy-2-venue-tickets

# Create a virtual environment in a folder named .venv, then turn it on
python3 -m venv .venv
source .venv/bin/activate

# Install the packages listed in requirements.txt (pytest and the packages it needs)
pip install -r requirements.txt

# Run the application
python3 src/main.py
```

Choose a few options from the menu. Try to book the Intro to Pottery workshop, which starts sold out, and try to refund a movie ticket, which the venue never refunds. Both refusals are rules the code enforces.

Most of the code in the case study will be unfamiliar the first time you open it, and that is on purpose. Every lesson in this module comes back to the same files, so you will see the same code again and again. By the time a lesson explains an idea, you will already have seen it working in this application. Today, you only need to read the parts each question quotes.

## How a Method Reaches Its Value

Strings and lists come with methods. `'hello'.upper()` returns `'HELLO'`, and `seats.append('A3')` adds `'A3'` to the end of the list `seats`. A method is a function attached to a value, and you call it with dot notation: `value.method()`.

That raises a question. A function only knows what its parameters are given, and `upper()` is called with empty parentheses. So how does `upper()` know which string to capitalize?

The answer is the idea this whole module is built on, and it requires understanding three things:

1. Every value in Python comes from a class
2. The methods available to a value live in its class
3. The value before the dot is the first argument of the method

### Idea 1. Every Value Comes from a Class

The `type()` function returns the class a value was made from:

```python
from datetime import date

print(type('hello'))              # <class 'str'>
print(type(['A1', 'A2']))         # <class 'list'>
print(type(3.5))                  # <class 'float'>
print(type(date(2026, 12, 5)))    # <class 'datetime.date'>
```

A **class** is a blueprint for making values of one kind.

- `str` is the class for strings
- `list` is the class for lists
- `float` is the class for floats
- `date` is the class for dates (remember this new type of value! we will use it later in this lesson)
- and so on...

Each string you have ever written is one **instance** of `str`: one value made from that blueprint. `'hello'` and `'goodbye'` are two instances of the same class, holding different text.

In fact, when you had previously used the `float` function to convert an input string into a float, you were creating a new "float instance".

```python
user_input = input("enter a number: ")
print(type(user_input))  # <class 'str'>

user_float = float(user_input)
print(type(user_float))  # <class 'float'>
```

### Idea 2. The Methods Available to a Value Live in its Class

Python stores the methods available to a value in its class. The `dir()` function lists every name a value answers to:

```python

print(dir('hello'))
# ['__add__', '__class__', '__contains__', ..., 'swapcase', 'title', 'translate', 'upper', 'zfill']

print(dir(str))
# The same as above

print('upper' in dir('hello')) # True
print('hello'.upper()) # HELLO

print('upper' in dir(5.5)) # False
print(5.5.upper()) # AttributeError: 'float' object has no attribute 'upper'
```

`dir('hello')` returns 81 names in Python 3.14. The ones at the end, such as `'title'` and `'upper'`, are the string methods you already use. The ones at the start, wrapped in double underscores, are **dunder methods** ("double underscore"). Python calls those for you at the right moment. For example, it calls `__add__` when you write `'hello' + ' there'`. You will write your own dunder method later in this lesson.

{% hint style="info" %}
💡 Asking a value about itself while the program runs, as `type()` and `dir()` do, is called **introspection**.
{% endhint %}

**<details><summary>Take a guess: when does Python call `__contains__` and `__eq__` for you?</summary>**

Python calls `__contains__` for you when checking membership with `in` and `not in`. It calls `__eq__` when comparing two strings for equality with the `==` and `!=` operators.

</details>

### Idea 3. The Value Before the Dot Is the First Argument

As we saw with `print(dir(str))`, `.upper()` is a function stored in the class `str`, and `'hello'` can use it because it is an instance of `str`. This means that you can call it through the string _or_ through the class:

```python
print(str.upper('hello'))    # called on the class str, with 'hello' as the argument -> HELLO
print('hello'.upper())       # called on the string instance with no argument -> HELLO
```

The two lines make the same call. Here is Python's rule for invoking methods: **when you call a method on a value (`'hello'.upper()`), Python finds the method in the value's class (`str.upper`) and calls it with the value as the first argument (`str.upper('hello')`).**

`'hello'.upper()` is a shorter way to write `str.upper('hello')`. The method never needed the string inside its parentheses, because Python put it there for you.

The same rule holds for every class:

{% hint style="warning" %}
**Predict, then run.** Each call below is written on the class instead of on the value. What does the program print?

```python
seats = ['A1', 'A2']
list.append(seats, 'A3')
print(seats)

print(str.upper('sold out'))
```

<details><summary>What actually happens</summary>

```
['A1', 'A2', 'A3']
SOLD OUT
```

- `list.append(seats, 'A3')` is the same call as `seats.append('A3')`. `seats` is the first argument, so `append` adds `'A3'` to the list `seats` refers to.
- `str.upper('sold out')` is the same call as `'sold out'.upper()`, so it returns a new, capitalized string.

</details>
{% endhint %}

Nobody writes `str.upper('hello')` in a real program, because `'hello'.upper()` is shorter and says the same thing. The long form is worth knowing because it shows what the short form does. When you write your own classes later in this lesson, the methods you write will receive their value the same way.

### Challenge: Rewrite the Call

For each value and method call below, use `type()` to name its class, check with `dir()` that the method is one of the names the value answers to, and then rewrite the method call so that it is made through the class. Each rewritten line should print the same result as the original.

```python
event_names = ['Friday Night Jazz', 'Intro to Pottery', 'Friday Night Jazz']
print(event_names.count('Friday Night Jazz'))

price = 25.0
print(price.is_integer())
```

For example:

```py
# What is given
email = 'MAYA@EXAMPLE.COM'
print(email.lower())

# You write
email = 'MAYA@EXAMPLE.COM'
print(type(email))              # <class 'str'>
print('lower' in dir(email))    # True
print(str.lower(email))         # maya@example.com
```

**<details><summary>Solution</summary>**

```python
event_names = ['Friday Night Jazz', 'Intro to Pottery', 'Friday Night Jazz']
print(type(event_names))                        # <class 'list'>
print('count' in dir(event_names))              # True
print(list.count(event_names, 'Friday Night Jazz'))  # 2

price = 25.0
print(type(price))                  # <class 'float'>
print('is_integer' in dir(price))   # True
print(float.is_integer(price))      # True
```

- `type()` names the class, and that class name goes before the dot in the rewritten call.
- The value that was before the dot becomes the first argument.
- `count` already took an argument, `'Friday Night Jazz'`. That argument moves to second place, after the list.

</details>

## Classes and Instances

Strings, lists, and dates are classes written into Python by its creators. A program can define its own classes too, which lets the programmer define new types of data and the methods their instances can use.

### Defining a Class

A class is defined with the `class` keyword, a name, and a colon. By convention, class names use **CapWords**: each word starts with a capital letter and there are no underscores, such as `Event` or `TicketOffice`. Python's style guide, PEP 8, sets this convention, and it is how you can tell a class from a function at a glance.

```python
class Event:
    pass

jazz = Event()
pottery = Event()

print(type(jazz))        # <class '__main__.Event'>
print(type(pottery))     # <class '__main__.Event'>
print(jazz is pottery)   # False
```

- `pass` is a placeholder that does nothing. A class body cannot be empty, so `pass` fills it until the class has something in it.
- `Event()` calls the class, like a function, and the call returns a new instance. Making an instance is called **instantiation**.
- `type(jazz)` reports that `jazz` was made from `Event`. The `__main__` in front is Python's name for the file you ran, so `__main__.Event` means "the `Event` class defined in this file".
- `jazz is pottery` is `False`, because each call to `Event()` makes a separate object.

An **attribute** is a piece of data stored on an object, and you reach it with a dot. You could add attributes to each instance one at a time:

```python
jazz.name = 'Friday Night Jazz'
jazz.date = date(2026, 12, 5)

pottery.name = 'Intro to Pottery'

print(pottery.date)
# AttributeError: 'Event' object has no attribute 'date'
```

Whoever set up `pottery` forgot its date, and nothing stopped them. The mistake only shows up later, when some other line reads `pottery.date` and the program stops with an `AttributeError`. The error message names the class (`'Event' object`) and the attribute it could not find (`'date'`), but it cannot tell you which line forgot to set it. Every event needs the same set of attributes, the same _shape_, and adding them by hand leaves that to memory.

{% hint style="info" %}
💡 `date` is a class and calling `date(2026, 12, 5)` creates a new instance of the `date` class. So, why is it written in lowercase and not `Date`?

Built-in classes like `str` and `float` are written in lowercase, and `date` follows the same style. PEP 8 allows a class that is used mainly by calling it, as `date(2026, 12, 5)` is, to be named like a function.
{% endhint %}

### `__init__` Gives Every Instance the Same Shape

`__init__` is a method you define inside a class, and Python runs it every time you create an instance. It receives the arguments passed to the class and stores them on the new instance:

```python
from datetime import date


class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.seats_sold = 0


jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)

print(jazz.name)          # Friday Night Jazz
print(pottery.capacity)   # 2
```

Here is what happens when Python runs `Event('Friday Night Jazz', date(2026, 12, 5), 40)`:

1. Python creates a new, empty `Event` instance.
2. Python calls `__init__`, passing the new instance as the first argument, `self`, followed by the three arguments you wrote.
3. Each line of `__init__` stores one argument on the instance. `self.name = name` creates an attribute called `name` on the new instance and gives it the value of the parameter `name`.
4. `self.seats_sold = 0` gives every new event a starting value that does not come from an argument. A brand-new event has sold no seats, so `__init__` sets the count itself rather than asking for it.
5. Python returns the finished instance, and `jazz` refers to it.

`__init__` never uses `return`. Its job is to fill in the instance Python already made, and Python hands that instance back for you.

Every event is now built by the same method, so every event has a name, a date, and a capacity. Leaving one out is no longer something that can happen quietly: calling `Event('Intro to Pottery', date(2026, 11, 20))` without a capacity raises a `TypeError` on that line, which names the missing argument.

`__init__` is a **dunder method**, like `__add__` on strings. You never call `__init__` yourself. Python calls it at the right moment, which is when you create an instance.

{% hint style="info" %}
💡 In `self.name = name`, the two `name`s are two different things. `self.name` is an attribute stored on the instance, and it lasts as long as the instance does. `name` is a parameter of `__init__`, and it disappears when `__init__` finishes. They share a spelling only because the parameter holds the value the attribute should get.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Both events below, `jazz` and `pottery`, are made from the same `Event` class. What does the program print?

```python
from datetime import date


class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.seats_sold = 0


jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)

print(pottery.capacity)
print(jazz.capacity)
```

<details><summary>What actually happens</summary>

```
2
40
```

Each call to `Event(...)` creates a new instance and runs `__init__` on it, so `self` is a different object each time. `pottery.capacity` was stored when `pottery` was built, and `jazz.capacity` was stored when `jazz` was built, so each event holds its own capacity.

</details>
{% endhint %}

### Data Goes on `self`

An attribute only exists if `__init__` stores it on `self`. This version forgets `self.` on one line:

```python
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        seats_sold = 0


jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
print(jazz.name)        # Friday Night Jazz
print(jazz.seats_sold)
# AttributeError: 'Event' object has no attribute 'seats_sold'
```

`seats_sold = 0` declares the variable `seats_sold` only for the duration of the `__init__` call. The value is never stored on the instance, so it disappears when `__init__` finishes, along with every other parameter. Python does not treat this as a mistake when it happens. The `AttributeError` appears later, on the line that tries to read `jazz.seats_sold`.

The rule is: **a value lasts beyond `__init__` only if it is assigned to an attribute of `self`.** `self` is the instance being built, so `self.seats_sold = 0` is what puts the value on `jazz`.

## Methods and `self`

### Writing a Method

A **method** is a function defined inside a class. Here is `Event` with two methods, `seats_left()` and `sell_ticket()`, and one more attribute:

```python
from datetime import date


class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.seats_sold = 0

    def seats_left(self):
        return self.capacity - self.seats_sold

    def sell_ticket(self):
        if self.seats_left() == 0:
            print(f'{self.name} is sold out.')
            return
        self.seats_sold += 1


pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
pottery.sell_ticket()
pottery.sell_ticket()
pottery.sell_ticket()        # Intro to Pottery is sold out.
print(pottery.seats_left())  # 0
```

- `seats_left()` reads two attributes of the event it was called on (`self.capacity` and `self.seats_sold`) and returns the difference.
- `sell_ticket()` is the only "official" way to change the `seats_sold` attribute. It refuses to sell a seat when none are left, and says why. Otherwise, it adds one to the event's count.
  - `sell_ticket()` calls `self.seats_left()`. Since `self` is the event, `self.seats_left()` asks the same event how many seats it has left.

The venue's rule now travels with the data. Any code holding an event can call `sell_ticket()` on it, and finds the rule there instead of in some other file.

### `self` Is the Value Before the Dot

Every method's first parameter is `self`, and `self` follows the same rule as `'hello'.upper()`. When you call a method on an instance, Python finds the method in the instance's class and passes the instance in as the first argument:

```python
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)

print(jazz.seats_left())
# finds the Event.seats_left method and invokes it with jazz as the self argument -> 40

print(Event.seats_left(jazz))
# Invokes the method on the class directly, passing in jazz as self -> 40
```

`jazz.seats_left()` is a shorter way to write `Event.seats_left(jazz)`. Inside the method, `self` refers to `jazz`, so `self.capacity` is `jazz`'s capacity. That is how one method definition works for every event: the method's body is the same each time, but `self` is whichever event the method was called on.

{% hint style="warning" %}

Because Python always passes the instance in, a method has to have a parameter to receive it. A method defined without one fails as soon as it is called:

```python
class Event:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def seats_left():
        return 0


jazz = Event('Friday Night Jazz', 40)
jazz.seats_left()
# TypeError: Event.seats_left() takes 0 positional arguments but 1 was given
```

Read the message in two parts. `Event.seats_left() takes 0 positional arguments` describes the definition: it lists no parameters. `but 1 was given` describes the call: you wrote empty parentheses, but Python passed in `jazz` anyway. The one argument it is counting is the instance.

{% endhint %}

{% hint style="info" %}
💡 `self` is a name, not a keyword. Python would accept any name for the first parameter, but PEP 8 says to always use `self`, and every Python programmer does. A method that names it anything else is harder for everyone else to read.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Using the `Event` class with `seats_left()` and `sell_ticket()` from above, what does this program print?

```python
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)

pottery.sell_ticket()
pottery.sell_ticket()

print(pottery.seats_left())
print(jazz.seats_left())
```

<details><summary>What actually happens</summary>

```
0
40
```

- Both calls to `sell_ticket()` were made on `pottery`, so `self` was `pottery` each time, and `pottery.seats_sold` went from `0` to `2`.
- `pottery.seats_left()` returns `2 - 2`, which is `0`.
- `jazz.seats_left()` runs the same method with `self` set to `jazz`. Nothing was ever sold for `jazz`, so it returns `40 - 0`.

</details>
{% endhint %}

### A Method That Takes Arguments

A method can take more arguments after `self`. They work the same way as any function's parameters, and the instance still arrives first:

```python
class Event:
    # __init__, seats_left, and sell_ticket as above

    def can_refund(self, today):
        return today < self.date


jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
today = date(2026, 11, 12)

print(jazz.can_refund(today))          # True
print(Event.can_refund(jazz, today))   # True
```

The venue refunds a ticket on any day before the event. Python compares dates by when they fall, so `today < self.date` is `True` when today comes before the event's date. In `jazz.can_refund(today)`, `jazz` becomes `self` and `today` becomes `today`. Written through the class, the instance takes the first slot and the argument you wrote takes the second.

### Challenge: Room Rentals

Riverside Community Hall also rents out its rooms. Write a class `Room` whose `__init__` takes a room's name, its number of seats, and its hourly rate in dollars, and stores all three on the instance. Give it two methods:

- `cost(hours)` returns what renting the room for that many hours costs.
- `fits(group_size)` returns `True` when a group of that size has enough seats, and `False` otherwise.

Then rewrite one of your method calls in the form `Room.cost(...)`.

```python
studio = Room('Dance Studio', 25, 40)
hall = Room('Main Hall', 200, 150)

print(studio.cost(3))     # 120
print(hall.fits(180))     # True
print(studio.fits(30))    # False
```

**<details><summary>Solution</summary>**

```python
class Room:
    def __init__(self, name, seats, hourly_rate):
        self.name = name
        self.seats = seats
        self.hourly_rate = hourly_rate

    def cost(self, hours):
        return self.hourly_rate * hours

    def fits(self, group_size):
        return group_size <= self.seats


studio = Room('Dance Studio', 25, 40)
hall = Room('Main Hall', 200, 150)

print(studio.cost(3))       # 120
print(hall.fits(180))       # True
print(studio.fits(30))      # False
print(Room.cost(hall, 2))   # 300, the same call as hall.cost(2)
```

- Each method's first parameter is `self`, so Python has somewhere to put the room the method was called on.
- `cost()` and `fits()` read the room's attributes through `self`, so the same methods give different answers for the studio and the hall.
- `Room.cost(hall, 2)` passes `hall` in the first slot by hand, which is what `hall.cost(2)` does for you.

</details>

## Encapsulation and the Interface

A class keeps an event's data and its rules together. To see why that matters, here is what goes wrong when a program keeps them apart, first in parallel lists and then in dictionaries.

### Parallel Lists Drift Apart

A venue needs to know each event's name, its capacity, and how many seats are sold. One way to store that is three lists, lined up by position:

```python
names = ['Movie Night: Coco', 'Friday Night Jazz', 'Intro to Pottery']
capacities = [30, 40, 2]
seats_sold = [5, 12, 2]

def seats_left(i):
    return capacities[i] - seats_sold[i]

print(f'{names[1]}: {seats_left(1)} seats left')
# Friday Night Jazz: 28 seats left

names.sort() # sorts the names but not the capacities or seats_sold

print(f'{names[1]}: {seats_left(1)} seats left')
# Intro to Pottery: 28 seats left
```

Sorting `names` moved each name to a new position, but it did not move the capacities or the seat counts. Python has no way to know that the three lists belong together, so nothing errors. The program now reports 28 seats left for a workshop that is sold out, and a customer who reads that will try to book a seat that does not exist.

### Dictionaries Keep the Data Together but Not the Rules

A list of dictionaries fixes the drift, because each event's data lives in one record. The rules about that data still live somewhere else, in separate functions:

```python
def make_event(name, capacity):
    return {'name': name, 'capacity': capacity, 'seats_sold': 0}

def seats_left(event):
    return event['capacity'] - event['seats_sold']

def sell_ticket(event):
    if seats_left(event) == 0:
        print(f"{event['name']} is sold out.")
        return
    event['seats_sold'] += 1

pottery = make_event('Intro to Pottery', 2)
sell_ticket(pottery)
sell_ticket(pottery)
sell_ticket(pottery)    # Intro to Pottery is sold out.
```

The venue's rule, "never sell more seats than the event holds", is written in `sell_ticket()`. But nothing connects the dictionary to that function. Any line anywhere in the program can change the record directly:

```python
pottery['seats_sold'] += 1
print(seats_left(pottery))    # -1
```

That code bypassed `sell_ticket()`, so the rule never ran, and the workshop is now oversold. Someone reading `pottery` also has no way to discover that `sell_ticket()` exists, because a dictionary only shows its keys. The rule is in one file and the data is in another, and **the program only works if every programmer remembers to use the `sell_ticket` function, which enforces the rule**.

### One Place for the Data and Its Rules

**Encapsulation** is bundling data together with the methods that operate on it, so that the class constrains how the rest of the program changes that data. The `Event` class encapsulates an event's name, date, capacity, and seat count together with `seats_left()` and `sell_ticket()`. Compare the two versions:

```python
# The dictionary version: data in one place, rules in another
pottery = make_event('Intro to Pottery', 2)
sell_ticket(pottery)

# The class version: the rule is a method of the event
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
pottery.sell_ticket()
```

Both lines sell a ticket, but they differ in what a reader needs to know. `sell_ticket(pottery)` only works if you know a function called `sell_ticket` exists somewhere and that it expects this particular shape of dictionary. `pottery.sell_ticket()` is found through the event itself, and introspection can list it:

```python
print(dir(pottery))
# ['__class__', '__delattr__', '__dict__', ..., '__weakref__', 'can_refund', 'capacity', 'date', 'name', 'seats_left', 'seats_sold', 'sell_ticket']
```

The list starts with the dunder methods that Python provides. Read past them, and the names at the end are everything this class gave the event: its four attributes and its three methods, including `sell_ticket`.

{% hint style="info" %}
💡 So far, the constraint is an agreement rather than a lock. `pottery.seats_sold = 99` still works on the class version and goes around the rule. A later lesson shows how a class can refuse a change like that, so that the constraint holds.
{% endhint %}

### The Interface

An object's **interface** is the set of attributes and methods the rest of the program uses to interact with it, and it constrains other code to use the object only as intended. For `Event`, the interface is `name`, `date`, `capacity`, `seats_left()`, `sell_ticket()`, and `can_refund()`.

The interface also decides how each piece of data is allowed to change. Other code can read `seats_sold` at any time, but the only way the interface offers to change it is `sell_ticket()`, which adds one seat and refuses when the event is full. Because every sale goes through that one method, the seat count can only change in one way: up by one, and never past `capacity`. A programmer reading the class can therefore predict every value `seats_sold` will ever hold, without searching the whole program for lines that touch it. Code that wrote `pottery.seats_sold += 1` instead would skip the sold-out check, and the seat count would stop being predictable.

Thinking in terms of an interface tells you two things about a class:

1. Code that uses the class should only need the interface, so it can ignore how the class works inside. 2. The class's author can change anything that is not part of the interface, such as how the seat count is stored, without breaking the code that _uses_ it.

**<details><summary>Q: Compare and contrast these two ideas about interfaces with the interface of a car. What does the user of a car's interface need to know? What can the maker of the car's interface change without impacting the user?</summary>**

A user only needs to know what the inputs are for the steering wheel (rotation) and the pedals (pressure). They don't need to know how those inputs actually work under the hood.

The designer of the car can change things like what kind of energy provides power to the engine (gas or electric). As long as they don't change how the steering wheel and pedals work, users won't be affected!

</details>

### Dictionary or Class?

A class is not always the better container. A dictionary still suits data that has no behavior of its own, such as a lookup table:

```python
ROOM_RATES = {'Dance Studio': 40, 'Main Hall': 150}
```

Nothing needs to happen to `ROOM_RATES` except looking a rate up by name, and a dictionary already does that. The question to ask is whether the data comes with rules or actions that belong to it. An event has to refuse a sale when it is full, so its data and that rule belong together in a class. A table of rates has no rule to enforce, so a dictionary is enough.

### Case Study Check: The Event Interface

The case study's `Event` class is at the top of `src/events.py`. Read its `__init__` and its methods, and skip the four methods with a line starting with `@` above them, and `__repr__`, for now: later lessons explain them. `Event` offers two methods to the rest of the program, `ticket_price()` and `can_refund(today)`.

1. Search the `src` folder for `ticket_price(` and `can_refund(` with VS Code's search (`Command+Shift+F` on a Mac, `Ctrl+Shift+F` on Windows). Skip the results in `src/events.py` and `src/events_abc.py`, and list each line in another file that calls one of the two methods.
2. The venue decides to add a $1 booking fee to every ticket. Which code would you change? Why would none of the lines you found need to change?
3. Suppose `menu.py` and `reservation.py` each worked out the price themselves from `event.base_price`, instead of calling `ticket_price()`. What would the same change involve, and what could go wrong?

**<details><summary>Answer</summary>**

1. Three lines call them:
   - `src/menu.py` calls `event.ticket_price()` to list each event's price.
   - `src/reservation.py` calls `event.ticket_price()` in `self.price = event.ticket_price()`, to record what the attendee pays.
   - `src/venue.py` calls `reservation.event.can_refund(today)` to check whether a refund is still allowed.

   The search also finds a comment in `src/menu.py` that mentions `ticket_price()`. It names the method but does not call it.

2. You would change one line, inside `Event.ticket_price()`: `return self.base_price` becomes `return self.base_price + 1`. Every caller asks the event for its price, so each one gets the new price without being edited. The interface stays the same, `event.ticket_price()`, and only the code inside the class changes.
3. You would have to find and change both files, and missing one would make them disagree: the menu could show a ticket at $30 while the reservation charged $31. Because the price rule lives in `Event` and the rest of the program goes through `ticket_price()`, the class constrains every caller to use the same rule.

</details>

## Advanced Topics

### Calling a Method Through the Wrong Class

Calling a method through its class only works when the first argument is an instance of that class:

```python
str.upper(5)
# TypeError: descriptor 'upper' for 'str' objects doesn't apply to a 'int' object
```

`descriptor 'upper' for 'str' objects` is Python's way of saying "`upper`, the method that belongs to `str`". `doesn't apply to a 'int' object` says what you passed in instead: an `int`. When you call a method the short way, as in `'hello'.upper()`, Python chooses the class from the value, so the two can never be mismatched. Writing the class yourself is the one way to get them wrong.

## Summary

Strings and lists already have methods, and a method reaches its value because Python passes the value before the dot in as the first argument: `'hello'.upper()` is the same call as `str.upper('hello')`, where `str` is a class and the string is an instance of it. `type()` and `dir()` show this, by naming a value's class and listing the methods it answers to. Programs that keep data in one place and the functions that change it in another, as parallel lists or dictionaries passed to functions, let any line change the data, with nothing tying the rules to the data. A class bundles the data with the methods that work on it, which is called **encapsulation**, and the methods the rest of the program uses are its **interface**. `__init__` runs when an instance is created and stores its data on `self`, so every instance has the same shape and its own values. A method you write receives its instance as `self` by the same rule `str.upper()` follows: `jazz.can_refund(today)` is `Event.can_refund(jazz, today)`.
