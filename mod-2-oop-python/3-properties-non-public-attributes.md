# 2.3 Properties: Non-Public Attributes and `@property`

**Table of Contents**:

- [Key Terms](#key-terms)
- [Going Around the Rules](#going-around-the-rules)
- [Non-Public Attributes and `@property`](#non-public-attributes-and-property)
  - [Step 1. A Value Other Code Can Read but Not Assign](#step-1-a-value-other-code-can-read-but-not-assign)
  - [Step 2. Refusing a Wrong Value with a Setter](#step-2-refusing-a-wrong-value-with-a-setter)
  - [Challenge: Base Price](#challenge-base-price)
- [Which Attributes Need a Rule?](#which-attributes-need-a-rule)
- [The Underscore Is a Convention](#the-underscore-is-a-convention)
- [Testing a Refusal](#testing-a-refusal)
  - [Challenge: Test the Base Price](#challenge-test-the-base-price)
- [Advanced Topics](#advanced-topics)
  - [A Getter That Reads Its Own Name](#a-getter-that-reads-its-own-name)
  - [Two Underscores](#two-underscores)
  - [Class Methods](#class-methods)
  - [Static Methods](#static-methods)
- [Summary](#summary)

## Key Terms

- A **public attribute** has a plain name and anything in the program may read or change it.
- A **non-public attribute** has a name that begins with a single underscore, such as `_capacity`. The underscore is a message to other programmers: do not reach for this directly. Python does not stop them, which is why the convention has to be respected rather than enforced. Python's style guide, PEP 8, uses the word "non-public". Other references call the same convention "private", "protected", or "internal".
- A **`@property`** turns a method into something that reads like an attribute, so a value can be computed on the way out, or checked on the way in.
  - A **getter** is the method a `@property` decorates. It returns the value.
    ```py
    @property
    def capacity(self):
        return self._capacity
    ```
  - A **setter** is the method decorated with `@<name>.setter`. It runs when something assigns to the attribute, which is where validation belongs.
    ```python
    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError(f'Capacity must be at least 1, not {value}.')
        self._capacity = value
    ```
  - **Validation** is checking a value before storing it, and refusing it when it is wrong.

**Advanced Topics**:

- A **`@classmethod`** receives the class itself as its first parameter, named **`cls`**, instead of an instance, and is called on the class. You will read them in other code: `date.today()` is called on the `date` class and returns a new date.
- A **`@staticmethod`** receives neither `self` nor `cls`. It is a plain function placed inside a class. Python's style guides prefer a function at the top level of a module, so you will read static methods more often than you write them.

## Going Around the Rules

Here is the venue's `Event` class. It stores how many seats the event has and how many are sold, and it refuses to sell a ticket once the event is full:

```python
from datetime import date

class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
        self.seats_sold = 0

    def seats_left(self):
        return self.capacity - self.seats_sold

    def sell_ticket(self):
        if self.seats_left() == 0:
            print(f'{self.name} is sold out.')
            return
        self.seats_sold += 1
```

`pottery` is an instance of `Event` for a workshop with capacity for two attendees. The third sale is refused, which is exactly what the class is for:

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.sell_ticket()
pottery.sell_ticket()
pottery.sell_ticket()        # Intro to Pottery is sold out.
```

That third call is a **refusal**: `sell_ticket()` turned down an action that would have broken the event's data, said why, and changed nothing. A venue refuses in the same way when it turns down an event that is already on its calendar.

{% hint style="warning" %}
`sell_ticket()` is meant to be the only way the seat count changes, because it is the method that checks for a free seat first. But nothing in the class makes it the only way.

Any line anywhere in the program can change `seats_sold` directly:

```python
pottery.seats_sold += 1
print(pottery.seats_left())   # -1
```

That line never runs `sell_ticket()`, so the sold-out check never runs either, and the workshop is now oversold by one seat. A programmer reading the class would expect `seats_sold` never to pass `capacity`, but that holds only as long as every other programmer remembers to call `sell_ticket()`.

Assigning a wrong value directly causes the same kind of trouble. A staff member updates a new workshop and types `0` when they meant `10`:

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.sell_ticket()
pottery.sell_ticket()

pottery.capacity = 0
pottery.sell_ticket()
print(pottery.seats_left())   # -3
```

The workshop just sold a ticket for a seat that does not exist, and nothing printed an error. Here is what happened, one step at a time:

- `pottery.capacity = 0` is an ordinary attribute assignment. No line of the `Event` class runs when it happens, so the class gets no chance to look at the value.
- Inside `sell_ticket()`, `seats_left()` returns `0 - 2`, which is `-2`.
- `-2 == 0` is `False`, so the `if` statement does not refuse the sale, and `seats_sold` goes up to `3`.

**<details><summary>Q: How would you debug this error?</summary>**

The mistake happened on the line that set the capacity by hand, but the error showed up later, inside `sell_ticket()`. Whoever investigates an oversold workshop starts from `sell_ticket()`, which is working correctly, and has to work backwards to find the line that set the capacity. The same thing happens if the capacity is wrong from the start: `Event('Intro to Pottery', date(2026, 11, 20), 0, 15)` creates the event without complaint.

</details>

{% endhint %}

Both problems have the same cause: assigning to an attribute runs no code in the class, so the class has no chance to refuse the assignment. This chapter gives the class two ways to take part in an assignment:

1. Let other code read a value but never assign it
2. Check a new value at the moment it is assigned, and refuse it there.

## Non-Public Attributes and `@property`

Putting an attribute behind a property starts the same way every time: store the value under a non-public name that begins with an underscore, such as `_seats_sold`, and add a **getter**, so that other code still reads `pottery.seats_sold`. What comes next depends on the attribute:

- `seats_sold` should never be assigned from outside the class, so it gets a getter and nothing else.
- `capacity` has to change sometimes, when a workshop moves to a bigger room, so it also gets a **setter** that checks each new value before storing it.

### Step 1. A Value Other Code Can Read but Not Assign

The first step is to store the seat count under a new name that starts with an underscore, `_seats_sold`, and to give the class a method that reads it:

```python
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
        self._seats_sold = 0

    @property
    def seats_sold(self):
        return self._seats_sold

    def seats_left(self):
        return self.capacity - self.seats_sold

    def sell_ticket(self):
        if self.seats_left() == 0:
            print(f'{self.name} is sold out.')
            return
        self._seats_sold += 1
```

The **`@property`** line above `seats_sold()` changes how the method is used. You never call `seats_sold()` with parentheses. Instead, when code reads `pottery.seats_sold`, Python runs the method for you and hands back whatever it returns, so the method looks like an attribute from the outside.

{% hint style="info" %}
💡 A line that starts with `@` and sits directly above a method is called a **decorator**. It is how Python changes what that method does, and you will learn how these lines work later in this module. For now, read `@property` as "accessing this property runs the method below."
{% endhint %}

This method is called a **getter**, because it gets the value. Notice what did not change:

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.sell_ticket()
print(pottery.seats_sold)      # Python runs the seats_sold getter, which returns self._seats_sold -> 1
print(pottery.seats_left())    # 1
```

`pottery.seats_sold` still works, and `seats_left()` still reads `self.seats_sold` exactly as it did before. Any code anywhere in the program that read `event.seats_sold` keeps working unchanged.

`sell_ticket()` assigns to `self._seats_sold`, the plain attribute that holds the value, so the assignment works. Only the class's own code is meant to touch the underscore name, and `sell_ticket()` checks for a free seat before it does.

{% hint style="warning" %}
**Predict, then run.** The class defines how to read `seats_sold` and nothing else. What happens when code outside the class tries to add a seat directly?

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.seats_sold += 1
```

<details><summary>What actually happens</summary>

```
AttributeError: property 'seats_sold' of 'Event' object has no setter
```

- `seats_sold` is no longer an attribute stored on the instance. It is a property: a method defined on the class, and the value itself lives in `_seats_sold`.
- `pottery.seats_sold += 1` reads the property, adds one, and assigns the result back to `seats_sold`. Assigning to a property runs its setter, and this property has no setter, so Python refuses the assignment and the count stays at `0`.

</details>
{% endhint %}

That error is what we actually want! It acts as a refusal to any code that tries to modify `seats_sold` directly. The only way left to change that value is through `sell_ticket()`, which checks for a free seat first, so the seat count can no longer pass the capacity.

### Step 2. Refusing a Wrong Value with a Setter

`capacity` needs a different kind of protection. A getter alone would refuse every assignment, including the one that moves a workshop to a bigger room. The class needs a way to accept a good capacity and refuse a bad one.

A **setter** is a second method with the same name as the `@property` method, marked with `@capacity.setter` (where the `@capacity` part is the method name). Python runs it for you every time something assigns to `capacity`, and it receives the new value as a parameter:

```python
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity      # runs the setter below
        self.base_price = base_price
        self._seats_sold = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError(f'Capacity must be at least 1, not {value}.')
        self._capacity = value

    # ... the seats_sold property, seats_left(), and sell_ticket() from above ...
```

The getter works the same way as the one for `seats_sold`: it returns the value stored under the underscore name. Now the staff member's typing mistake is caught on the line where it happens:

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

pottery.capacity = 0
# ValueError: Capacity must be at least 1, not 0.
```

Here is how the setter refuses the value and keeps the old one:

- `pottery.capacity = 0` runs the setter with `value` set to `0`.
- `0 < 1` is `True`, so the `raise` statement raises a `ValueError`. A `raise` statement ends the method immediately, so `self._capacity = value` never runs.

The error message does two jobs. `Capacity must be at least 1` states the rule, and `not 0` says which value was refused, so whoever reads the traceback knows both what the rule is and what broke it.

Notice that `__init__` assigns `self.capacity = capacity`, without an underscore. Assigning to `self.capacity` inside the class runs the setter, exactly as assigning to `pottery.capacity` does outside it. So the check runs when the event is first created as well, and the only line that writes `_capacity` directly is the setter's last line, after the value has passed the check.

{% hint style="warning" %}
**Predict, then run.** What happens when the event is created with a capacity of `0`?

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 0, 15)
print(pottery.name)
```

<details><summary>What actually happens</summary>

```
ValueError: Capacity must be at least 1, not 0.
```

Creating the event runs `__init__`, and the line `self.capacity = capacity` in `__init__` runs the setter. The setter raises before `__init__` finishes, so `pottery` is never created and the `print()` line never runs. A program can no longer hold an event with a capacity below 1, because there is no way to make one.

</details>
{% endhint %}

### Challenge: Base Price

Give the `Event` class a `base_price` property. Its setter should refuse a negative price by raising a `ValueError` whose message names the rule and the refused value, and `__init__` should run the setter. A price of `0` is allowed, because the venue runs free events.

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.base_price = 20
print(pottery.base_price)   # 20

pottery.base_price = -15    # ValueError: A price cannot be negative, not -15.
```

**<details><summary>Solution</summary>**

```python
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price    # runs the base_price setter
        self._seats_sold = 0

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            raise ValueError(f'A price cannot be negative, not {value}.')
        self._base_price = value

    # ... the capacity property, the seats_sold property, seats_left(), and sell_ticket() ...
```

- The value is stored under `_base_price`, and the getter returns it, so `pottery.base_price` reads the way it always did.
- The setter checks `value < 0` rather than `value < 1`, because the rule is "not negative" and `0` is a valid price. The comparison in a setter is the rule written in code, so it has to match the rule exactly.
- `__init__` assigns to `self.base_price`, not `self._base_price`, so an event cannot be created with a negative price either.

</details>

{% hint style="warning" %}
**Check for understanding.** Suppose the last line of `sell_ticket()` were `self.seats_sold += 1` instead of `self._seats_sold += 1`. What happens on the first sale, and why does the original line work?

<details><summary>Answer</summary>

The first sale raises `AttributeError: property 'seats_sold' of 'Event' object has no setter`, and the seat count stays at `0`.

- `self.seats_sold += 1` assigns to `seats_sold`, the property. Assigning to a property runs its setter wherever the assignment is written, inside the class or outside it, and this property has no setter.
- The original line assigns to `self._seats_sold`, a plain attribute with no property in front of it, so the assignment stores the new count.

Being a method of the class gives `sell_ticket()` no special permission. What lets it change the count is the name it assigns to. The underscore asks code outside the class not to use that name, which leaves `sell_ticket()`, with its sold-out check, as the only code that should.

</details>
{% endhint %}

## Which Attributes Need a Rule?

`Event` now protects two of its attributes in two different ways and leaves the others alone. Not every attribute needs protecting. To decide, ask of each attribute: **is there a value that would break the program?**

**<details><summary>Q: For each attribute of `Event` (`name`, `date`, `capacity`, `base_price`, `seats_sold`), is there a value that would break the program? Should it therefore be public or non-public and why?</summary>**

| Attribute    | Is there a value that would break the program?                                                         | Decision                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| `name`       | No. Any string works as an event's name.                                                               | Stays a public attribute.                                                         |
| `date`       | No. The venue lists events that have already happened, so no date is wrong.                            | Stays a public attribute.                                                         |
| `capacity`   | Yes. A capacity below 1 breaks the seat count.                                                         | Becomes non-public, behind a property with a setter that refuses values below 1.  |
| `base_price` | Yes. A negative price means the venue pays the attendee.                                               | Becomes non-public, behind a property with a setter that refuses negative values. |
| `seats_sold` | Yes. Only `sell_ticket()` should change it, because only `sell_ticket()` checks for a free seat first. | Becomes non-public, behind a property with no setter at all.                      |

</details>

Python's two most widely used style guides agree on three rules:

1. **Plain data with no rule stays public.** Google's Python style guide says that a property which only reads and writes a stored value, with no check in between, is unnecessary, and the attribute should be made public instead. `name` stays `name`.
2. **Data with a rule goes behind a property.** PEP 8 says that when a simple public attribute needs to grow behavior, a property can add it while code keeps using the same attribute syntax. That is what happened to `seats_sold`: code that read `pottery.seats_sold` kept working after it became a property. If `seats_sold` had become a method such as `get_seats_sold()` instead, every line that read `pottery.seats_sold` would have had to change.
3. **If you are unsure whether other code should rely on an attribute, make it non-public.** PEP 8 explains why: once other code uses a public attribute, removing it or changing what it means breaks that code. A non-public attribute made no promise to anyone, so the class can change it freely.

{% hint style="warning" %}
**Check for understanding: which case study attributes have a rule?** Here is part of the case study's `events.py`, in `src/`:

```python
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
    ...
```

The case study also defines `Workshop`, a kind of event that stores one more value in its `__init__`, with `self.materials_fee = materials_fee`. A workshop's ticket price is its base price plus its `materials_fee`.

In the case study, `capacity` and `base_price` are reached through properties, and `name`, `date`, and `materials_fee` are plain public attributes. For each of the five attributes, decide whether a wrong value would break the program. Which attribute does the case study leave public even though it has a rule? (The case study marks it with a comment that asks the same question.)

<details><summary>Answers</summary>

- `name`: no wrong value breaks anything, so it is public.
- `date`: the venue lists events that have already happened on purpose (the sample data includes a past screening), so a date in the past is not wrong. It is public.
- `capacity` and `base_price`: a capacity below 1 breaks the seat count and a negative price means paying the attendee, so both have a rule and both are behind properties.
- `materials_fee`: **this one has a rule but is public.** A workshop's ticket price adds the fee to the base price, so a negative fee such as `-20` would make a $15 workshop ticket cost `-5` dollars. Following the three rules above, `materials_fee` should be non-public behind a property whose setter refuses a negative fee, the same as `base_price`.

</details>
{% endhint %}

## The Underscore Is a Convention

The underscore in `_capacity` does not stop anything. Python lets any code read or assign an attribute whose name starts with an underscore:

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery._capacity = -5            # no error
print(pottery.seats_left())       # -5
```

The assignment goes straight to the stored value and skips the setter, so the check never runs. Python has no way of making an attribute unreachable.

What the underscore does is send a message to other programmers: **this attribute belongs to the class, so do not reach for it directly.** Code outside the class should go through `pottery.capacity`, where the rule is checked. The property is the class's interface for the capacity: it constrains other code to change the capacity only through the setter, and the setter's refusal is how the class holds to that constraint. Only the class's own methods, such as the setter and `sell_ticket()`, touch the underscore names. Some code-checking tools will warn you when code outside a class uses an underscore attribute, but Python itself will run the line.

{% hint style="info" %}
💡 PEP 8 calls these attributes **non-public**, and that is the word this course uses. You will also see Google's style guide and other references call the same convention "private", "protected", or "internal". All four words describe the same single underscore.
{% endhint %}

{% hint style="warning" %}
**Check for understanding.** Here is part of the case study's `Venue` class, in `src/venue.py`:

```python
class Venue:
    def __init__(self, name):
        self.name = name
        self._events = []
        self._attendees = {}
        self._reservations = []
        ...

    @property
    def attendees(self):
        return list(self._attendees.values())

    def add_attendee(self, attendee):
        if not Venue.is_valid_email(attendee.email):
            raise ValueError(f'"{attendee.email}" is not a valid email address.')
        if attendee.email in self._attendees:
            print(f'{attendee.email} is already registered.')
            return None
        self._attendees[attendee.email] = attendee
        return attendee
```

`sam = Attendee('Sam Ortiz', 'sam')` has an email address with no `@` in it. Run each line below on its own, against a new venue. What does each one do to the venue's attendees, and which one does the underscore in `_attendees` ask you not to write?

```python
venue.attendees.append(sam)       # Line 1
venue._attendees['sam'] = sam     # Line 2
venue.add_attendee(sam)           # Line 3
```

<details><summary>Answer</summary>

- **Line 1** changes nothing in the venue. The `attendees` property returns `list(...)`, a new list, so `append()` adds Sam to that new list and the venue's own `_attendees` dictionary never receives Sam.
- **Line 2** registers Sam with no checks at all. It assigns straight into the venue's own dictionary, so `add_attendee()` never runs, and neither the email check nor the duplicate check happens. Python allows it.
- **Line 3** raises `ValueError: "sam" is not a valid email address.`, and Sam is not registered.

The underscore in `_attendees` asks other programmers not to write Line 2. The dictionary belongs to the venue, and the only way meant for adding to it is `add_attendee()`, where the venue's rules are checked.

</details>
{% endhint %}

## Testing a Refusal

A setter's refusal is part of what the class does, so it deserves tests like any other behavior. A refusal makes two promises, and each one needs its own test:

1. The wrong value raises a `ValueError`.
2. After the refusal, the stored value is the one that was there before.

Set up a project with the `Event` class in `src/event.py` and its tests in `tests/test_event.py`:

```
refusal-practice/
├── .venv/
├── pytest.ini
├── src/
│   └── event.py
└── tests/
    └── test_event.py
```

`pytest.ini` holds the same two settings as every Mod 2 repository: `pythonpath = src` lets the test file import from the `src` folder, and `testpaths = tests` tells pytest where the tests are:

```
[pytest]
pythonpath = src
testpaths = tests
```

Then write the two tests, one per promise:

```python
from datetime import date

import pytest
from event import Event


def test_a_capacity_below_one_is_refused():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    with pytest.raises(ValueError):
        pottery.capacity = 0


def test_a_refused_capacity_leaves_the_stored_value_unchanged():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    with pytest.raises(ValueError):
        pottery.capacity = 0

    assert pottery.capacity == 2
```

With the virtual environment turned on and pytest installed, run `pytest` from the `refusal-practice` folder. Both tests pass.

The second test needs `with pytest.raises(ValueError):` as well. Without it, the `ValueError` would end the test as a failure before the `assert` line was ever reached. Inside the `with` block, the error is the result the test expects, so the test carries on to the `assert` and checks the stored value.

{% hint style="warning" %}
**Predict, then run.** Swap the two lines in the setter so that it stores the value before it checks it. Which test fails, and what does pytest report?

```python
@capacity.setter
def capacity(self, value):
    self._capacity = value
    if value < 1:
        raise ValueError(f'Capacity must be at least 1, not {value}.')
```

<details><summary>What actually happens</summary>

```
>       assert pottery.capacity == 2
E       assert 0 == 2
```

`test_a_refused_capacity_leaves_the_stored_value_unchanged` fails and `test_a_capacity_below_one_is_refused` still passes. The setter still raises a `ValueError`, so the first test is satisfied. But it raises after `self._capacity = value` has already stored the `0`, so the refusal leaves the bad value behind. Only the second test checks what is stored afterwards, which is why a refusal needs both tests. Swap the lines back before moving on.

</details>
{% endhint %}

### Challenge: Test the Base Price

Write the same two tests for the `base_price` setter from Challenge: Base Price: one that shows a negative price is refused, and one that shows the stored price is unchanged afterwards. Then add a third test that shows a price of `0` is accepted.

**<details><summary>Solution</summary>**

```python
def test_a_negative_price_is_refused():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    with pytest.raises(ValueError):
        pottery.base_price = -15


def test_a_refused_price_leaves_the_stored_price_unchanged():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    with pytest.raises(ValueError):
        pottery.base_price = -15

    assert pottery.base_price == 15


def test_a_price_of_zero_is_accepted():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    pottery.base_price = 0

    assert pottery.base_price == 0
```

The third test protects the edge of the rule. If someone later writes `value < 1` in the setter by mistake, the first two tests still pass, because `-15` is refused either way. Only the test for `0` notices that free events are now refused.

</details>

{% hint style="warning" %}
**Check for understanding.** These two tests are based on two in the case study's `tests/test_events.py`, with the event built inside each test. (In the case study's file, the event comes from shared setup in `tests/conftest.py`, which the case study session explains.)

```python
def test_capacity_setter_refuses_a_capacity_below_one():
    jazz = Event('Friday Night Jazz', date(2026, 12, 13), 40, 25)

    with pytest.raises(ValueError):
        jazz.capacity = 0


def test_a_refused_capacity_leaves_the_stored_value_unchanged():
    jazz = Event('Friday Night Jazz', date(2026, 12, 13), 40, 25)

    with pytest.raises(ValueError):
        jazz.capacity = -5

    assert jazz.capacity == 40
```

Name the rule each test protects. Then say what a bug would have to look like for the first test to pass and the second to fail.

<details><summary>Answer</summary>

- The first test protects the rule that a capacity below 1 is refused with a `ValueError`.
- The second test protects the rule that a refused capacity leaves the event's capacity as it was, `40`.

For the first test to pass and the second to fail, the setter would have to raise the `ValueError` after storing the value, for example with `self._capacity = value` above the `if` statement. The error is still raised, so the first test passes, but `jazz.capacity` is now `-5`, so the second test's `assert` fails.

</details>
{% endhint %}

## Advanced Topics

### A Getter That Reads Its Own Name

A getter has to read the underscore name. This getter reads `self.capacity` instead:

```python
@property
def capacity(self):
    return self.capacity
```

Reading `pottery.capacity` runs the getter, the getter reads `self.capacity`, which runs the getter again, and so on. Python stops the chain with `RecursionError: maximum recursion depth exceeded`. The same thing happens in a setter that ends with `self.capacity = value` instead of `self._capacity = value`: assigning to `self.capacity` runs the setter again. Inside the getter and the setter, always use the underscore name, because that is the one that holds the value.

### Two Underscores

You will sometimes see an attribute name that starts with two underscores, such as `self.__capacity`. Python changes such a name inside the class by putting the class name in front of it, which is called **name mangling**:

```python
class Event:
    def __init__(self, capacity):
        self.__capacity = capacity

pottery = Event(5)
print(pottery._Event__capacity)   # 5
print(pottery.__capacity)         # AttributeError: 'Event' object has no attribute '__capacity'
```

Python stored the value under the name `_Event__capacity`. `pottery.__capacity` raises `AttributeError`, but the changed name still reaches the value, so two underscores make an attribute no more protected than one does. PEP 8 says the double underscore exists to stop a subclass from accidentally reusing the same attribute name, and Google's style guide asks programmers to prefer a single underscore. Recognize it when you see it, and use one underscore in your own classes.

### Class Methods

Every object in this chapter is created by calling its class, such as `Event('Intro to Pottery', date(2026, 11, 20), 2, 15)`, and that is how you will create objects throughout this module. You will also meet two kinds of method in code you read, including Python's own libraries and the case study, that work differently from the methods you write.

A method marked `@classmethod` is called on the class itself, not on an instance, and Python passes in the class as its first argument, named `cls`. The case study's `src/main.py` calls one: `build_sample_venue(date.today())`. `date.today()` is called on the `date` class from the `datetime` module, and it returns a new `date` holding today's date:

```python
from datetime import date

today = date.today()
print(today)        # the current date, such as 2026-11-16
```

Python's standard library includes a version of the `datetime` module written in Python, and this is its definition of `today()`, shortened to the lines that matter here:

```python
class date:
    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)
```

- `date.today()` is called on `date`, the class. There is no date yet to call it on, because making one is the method's job.
- Python passes `date` in as `cls`, the same way it passes the instance in as `self` for an ordinary method.
- `cls.fromtimestamp(t)` builds the new date from the current time and returns it.

### Static Methods

A method marked `@staticmethod` receives neither `self` nor `cls`. Python passes in nothing extra, so its parameters are only the arguments you give it. The case study has one, in `src/venue.py`:

```python
class Venue:
    ...
    @staticmethod
    def is_valid_email(email):
        if '@' not in email:
            return False
        domain = email.split('@')[-1]
        return '.' in domain
```

`add_attendee()` calls it through the class name, as `Venue.is_valid_email(attendee.email)`. The method never reads `self`, so it is really a plain function that has been placed inside the class.

Google's Python style guide says not to write static methods, and to write a plain function at the top level of the module instead. The case study keeps `is_valid_email` as a static method so that you recognize one when you meet it in other people's code, where they are common.

{% hint style="warning" %}
**Check for understanding.** For each call below, what does Python pass in as the method's first argument?

1. `pottery.sell_ticket()`, where `pottery` is an `Event`
2. `date.today()`
3. `Venue.is_valid_email('maya@example.com')`

<details><summary>Answers</summary>

1. **`pottery`**, the instance the method was called on. `sell_ticket()` is an ordinary method, so Python passes the value before the dot in as `self`.
2. **The `date` class.** `today()` is a class method, so Python passes the class it was called on in as `cls`.
3. **`'maya@example.com'`.** `is_valid_email()` is a static method, so Python passes in nothing extra, and the first argument is the first value you gave it, which becomes `email`.

</details>
{% endhint %}

## Summary

Nothing in a plain class stops code from going around its rules. A line that changes `seats_sold` directly skips the sold-out check in `sell_ticket()`, and a line that sets the capacity to `0` breaks the seat count, with the mistake showing up far from the line that made it. Data with no rule stays a public attribute. Data with a rule becomes non-public, stored under a name with a single leading underscore, and is reached through a `@property`, so code that read `event.seats_sold` or `event.capacity` before keeps working unchanged. A property with no setter lets other code read a value but never assign it, so the only way to change the seat count is the method that checks first. A property with a setter refuses an invalid value by raising a `ValueError` whose message names the rule, and it leaves the stored value unchanged, which two tests prove: one that the error is raised and one that the value stayed the same. The property constrains other code to change the value only through the class's own code, and the refusal holds the class to that constraint. The underscore is a convention, not enforcement: Python lets anyone reach `_capacity`, and the underscore asks other programmers to go through the property instead.
