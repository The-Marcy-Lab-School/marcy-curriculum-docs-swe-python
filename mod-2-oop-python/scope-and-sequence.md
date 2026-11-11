# Mod 2 Project: Object-Oriented Programming

# Proposed Learning Objectives

## How to read these

Every objective is written in **ABCD** form and tagged with its **Bloom** level
and the project requirement it serves.

| Part          | Where it lives                                                           |
| ------------- | ------------------------------------------------------------------------ |
| **A**udience  | The **Fellows will be able to…** heading, so it is not repeated 73 times |
| **B**ehavior  | The Bloom verb and its object — the observable thing                     |
| **C**ondition | The _Given…_ clause: what the fellow is handed                           |
| **D**egree    | The countable criterion: how many, how accurately, under what constraint |

Tags read **Bloom level · what it serves**:

- **R1**-**R9** are the project's nine requirements, **D1** its `DESIGN.md`
  deliverable, and **D4** the five-minute share-out. See the project proposal.
- **assignment only** means the objective is assessed by an assignment and the
  project does not require it.
- **(ADDED)** marks an objective with no topic behind it in the scope and
  sequence. These cover skills the project requires that no session teaches.
- **(deferred until after Mod 2)** marks an objective fellows meet in January, when Mod 3 starts and they hand their specification to a model.
- **(optional)** marks a preview objective an instructor may use in place of the one above it, when fellows have not yet been taught the skill that objective asks them to produce.

Each session splits into **In the session** — what the 90-minute lecture must
introduce, practice, and check — and **By the end of the module**, which the
reading, assignments, and project carry.

## Session calendar

| Chapter | Session                                                                | Week | Day        | Date         |
| ------- | ---------------------------------------------------------------------- | ---- | ---------- | ------------ |
| 2.1     | Intro to OOP: Classes, `__init__`, and `self`                          | 7    | 4          | Thu 11/12    |
| 2.2     | Composition, `__repr__`, `__eq__`, and `@dataclass` | 7    | 5          | Fri 11/13    |
| 2.3     | Properties: Non-Public Attributes and `@property`   | 8    | 1          | Mon 11/16    |
| 2.4     | Inheritance and Attribute Lookup                                       | 8    | 3          | Wed 11/18    |
| 2.5     | Polymorphism, Duck Typing, and Abstract Base Classes                   | 8    | 4          | Thu 11/19    |
| 2.6     | Functions as Values: Callbacks and Higher-Order Functions              | 8    | 5          | Fri 11/20    |
| 2.7     | Closures and Decorators                                                | 9    | 1          | Mon 11/23    |
| —       | Case Study                                                             | 9    | 3          | Wed 11/25    |
| 2.8     | System Design and UML Diagrams                                         | 10   | 1          | Mon 11/30    |
| 2.9     | System Design Strategies                                               | 10   | 3          | Wed 12/2     |
| 2.10    | Writing a Specification You Can Hand Off                               | 10   | 5          | Fri 12/4     |
| —       | Project, build days 1-4                                                | 11   | 1, 3, 4, 5 | 12/7 - 12/11 |
| —       | Project, build day 5, due end of day                                   | 12   | 1          | Mon 12/14    |
| —       | Project share-out                                                      | 12   | 3          | Wed 12/16    |
| —       | Mod 2 Assessment                                                       | 12   | 5          | Fri 12/18    |

## Testing Objectives

Every session that produces testable code carries one testing objective. Each session below points to its row here, so the testing objectives can be read and revised together.

| Session    | Placement                | Objective                                                                                                                                                                                          |
| ---------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.2        | In the session           | **Apply · R9** — Given a class with `__eq__` and a method that refuses to add an instance equal to one it already holds, implement a pytest test that adds an equal instance a second time and asserts that the collection still holds one. |
| 2.3        | In the session           | **Apply · R9** — Given a validating setter, implement one test that uses `pytest.raises(ValueError)` on an invalid assignment, and a second that asserts the stored value is unchanged afterwards. |
| 2.4        | By the end of the module | **Apply · R3** — Given a method overridden in two subclasses, implement one test per subclass that asserts the result each returns for the same call.                                              |
| 2.5        | By the end of the module | **Apply · assignment only** — Given an abstract base class, implement a test that uses `pytest.raises(TypeError)` to show that a subclass missing an abstract method cannot be instantiated.       |
| 2.7        | By the end of the module | **Apply · R7, R9** — Given a method guarded by a status-checking decorator, implement a test showing that a call from the wrong status leaves the object unchanged.                                |
| 2.9        | In the session           | **Apply · R9** — Given a coordinator or status-driven class, implement a test that attempts a refused action and asserts that the status and every collection are unchanged afterwards.            |
| Case study | In the session           | **Analyze · R9** — Given the case study's tests, name the rule each test protects.                                                                                                                 |

---

## 2.1 Intro to OOP: Classes, `__init__`, and `self`

**Week 7, Day 4 — Thursday 11/12**

**Fellows will be able to…**

_In the session:_

- **Understand · R1** — Given a function that builds and returns a dictionary and a class that stores the same data, explain in two or three sentences what the class provides that the function does not, naming encapsulation and the object's interface.
- **Apply · R1** — Given a description of an entity and the data it holds, define a class whose `__init__` stores at least three instance attributes on `self`, and one method that returns an answer computed from those attributes.
- **Understand · R1** — Given a method definition and a call on an instance, explain what `self` refers to, naming the instance the method was called on as the value Python passes in, and rewrite the call in the form `Event.can_refund(jazz, today)`.

_By the end of the module:_

- **Evaluate · R1** — Given a described piece of data, decide whether a dictionary or a class is the better container, and defend the choice in one sentence naming the behavior involved.
- **Understand · R2** — Given a class whose methods change its data, explain how the class's interface constrains the ways other code can change that data, naming the rule each method enforces and the values the data can hold as a result, and describe one way the data could go wrong if other code changed the attribute directly.
- **Analyze · R1** — Given a program that stores related data across parallel lists, identify the data and the behavior that belong together, and name the one class that should own both.

### Exit Ticket

**Learning Objective**: Fellows will be able to explain how a method call connects to the instance it was called on, describing what `self` refers to and why one method definition can return a different answer for each instance.

**Question**

This excerpt is from the case study's `Event` class:

```python
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def can_refund(self, today):
        return today < self.date
```

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
jazz = Event('Friday Night Jazz', date(2026, 11, 28), 40, 25)
today = date(2026, 11, 25)

print(pottery.can_refund(today))
print(jazz.can_refund(today))
```

Both lines call the same `can_refund` method. What does each line print, and why does the same method give two different answers?

**Level 2 Example**

The first line prints `False` and the second prints `True`, because the pottery workshop already happened and the jazz concert hasn't happened yet.

**Level 3 Example**

The first line prints `False` and the second prints `True`. When I call `pottery.can_refund(today)`, Python passes `pottery` into the method as `self`, so `self.date` is the date `pottery` stored in `__init__`, November 20. November 25 is not before November 20, so the method returns `False`. When I call `jazz.can_refund(today)`, `self` is `jazz`, so `self.date` is November 28, and November 25 is before it, so the method returns `True`. There is only one `can_refund` method, but each instance holds its own `date`, and `self` decides whose date the method reads.

## 2.2 Composition, `__repr__`, `__eq__`, and `@dataclass`

**Week 7, Day 5 — Friday 11/13**

**Fellows will be able to…**

_In the session:_

- **Apply · R5 (ADDED)** — Given a class that must manage many entities, store a list of instances as an attribute and write a method that returns only those instances whose attribute matches a given value.
- **Apply · R6 (ADDED)** — Given two existing instances, define a third class that stores both as attributes, and reach a value on one of them through the new object in a single expression, such as `reservation.attendee.name`.
- **Apply · R1** — Given a class with no `__repr__`, write one that returns the class name and at least two attribute values, so that printing an instance identifies which instance it is.
- **Evaluate · R1** — Given two instances that hold identical data, predict whether `==` returns `True` with and without an `__eq__` method, and explain the difference between two names referring to the same object (`is`) and two objects holding equal data (`==`).
- **Create · R1** — Given a class that only carries data and defines `__init__`, `__repr__`, and `__eq__` by hand, refactor it with `@dataclass`, and confirm that comparing its instances gives the same results as before and that printing an instance still identifies it.
- **Testing** — See the 2.2 row of [Testing Objectives](#testing-objectives).

_By the end of the module:_

- **Analyze · R1** — Given an object printed as `<Event object at 0x104e2f10>`, explain what that output does and does not tell you, and state what `__repr__` would add.
- **Evaluate · D1** — Given a class that only carries data, decide whether `@dataclass` or a plain class suits it better, and defend the choice by naming at least one method `@dataclass` would write for you.

### Exit Ticket

**Learning Objective**: Fellows will be able to explain where an object's data is stored, distinguishing a value an instance copies into its own attribute from another object that it holds and reaches through.

**Question**

This excerpt is from the case study's `Reservation` class. An event's `ticket_price()` returns its `base_price`.

```python
class Reservation:
    def __init__(self, number, attendee, event):
        self.number = number
        self.attendee = attendee
        self.event = event
        self.price = event.ticket_price()
```

```python
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40, 25)
maya_ticket = Reservation(1001, maya, jazz)

jazz.base_price = 30

print(maya_ticket.price)
print(maya_ticket.event.base_price)
```

What do the two `print()` calls show, and why do they show different prices when both are about Maya's ticket to the same concert?

**Level 2 Example**

The first shows `25` and the second shows `30`, because the price changed after Maya booked her ticket.

**Level 3 Example**

The first shows `25` and the second shows `30`. When Maya's reservation was created, `__init__` called `event.ticket_price()` and stored the answer, the number `25`, in the reservation's own `price` attribute. That number belongs to `maya_ticket`, so changing the concert's price later doesn't touch it. But `self.event` stores the `jazz` object itself, not a copy of it, so `maya_ticket.event.base_price` reaches through the reservation to the same concert that was just changed and shows `30`. That's why Maya keeps the price she agreed to, while the reservation still knows the event's current details.

## 2.3 Properties: Non-Public Attributes and `@property`

**Week 8, Day 1 — Monday 11/16**

**Fellows will be able to…**

_In the session:_

- **Evaluate · R2** — Given a class with four public attributes, decide for each one whether it should stay public or become non-public behind a `@property`, by asking whether an invalid value there would break the program, and give a one-sentence reason per attribute.
- **Apply · R2** — Given a non-public attribute, expose it through a `@property` getter so that code which previously read the attribute directly still works unchanged.
- **Apply · R2** — Given a rule an attribute must satisfy, write a setter that raises `ValueError` with a message naming the rule, and leaves the stored value unchanged when an assignment is rejected.
- **Understand · R2** — Explain what a single leading underscore asks of another programmer and what it does not prevent, naming at least one way the attribute can still be reached.
- **Testing** — See the 2.3 row of [Testing Objectives](#testing-objectives).

_By the end of the module:_

- **Understand · assignment only** — Given a method marked `@classmethod` or `@staticmethod` in code you are reading, such as `date.today()`, explain what Python passes in as its first argument (the class, or nothing) and how the method is called.

### Exit Ticket

**Learning Objective**: Fellows will be able to explain how a non-public attribute and a property setter work together to refuse an invalid value, and describe what the single leading underscore does and does not prevent.

**Question**

This excerpt is from the case study's `Event` class:

```python
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError(f'Capacity must be at least 1, not {value}.')
        self._capacity = value
```

```python
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

pottery.capacity = 0     # Line A
pottery._capacity = 0    # Line B
```

Imagine each line is run on its own, straight after `pottery` is created. What happens on Line A, and what happens on Line B? Explain why the two lines behave differently, and what the underscore in `_capacity` asks of other programmers.

**Level 2 Example**

Line A raises a `ValueError` because the capacity can't be 0. Line B works and sets the capacity to 0.

**Level 3 Example**

Line A raises `ValueError: Capacity must be at least 1, not 0.` Assigning to `pottery.capacity` runs the setter, which checks the value before storing it. Since 0 is less than 1, the setter raises the error before it reaches `self._capacity = value`, so the capacity stays 2. Line B assigns straight to `_capacity`, the attribute where the value is actually stored, so it skips the setter and the capacity becomes 0 with no check. Python doesn't stop this. The underscore makes `_capacity` non-public, which is a message to other programmers to go through the `capacity` property, where the rule is checked. Line B ignores that message, so the event now has a capacity the rule was written to refuse.

## 2.4 Inheritance and Attribute Lookup

**Week 8, Day 3 — Wednesday 11/18**

**Fellows will be able to…**

_In the session:_

- **Apply · R3** — Given a superclass and a described subtype, define a subclass that calls `super().__init__()` and adds at least one attribute of its own.
- **Apply · R3** — Given a superclass method, override it in two subclasses so that each returns a different result for the same call, using `super().method()` in at least one to extend rather than replace the parent's version.
- **Analyze · assignment only** — Given a two-level hierarchy and an attribute access, trace where Python finds the attribute, naming each place it looked in order (the instance, its class, then the parent class) and the place it stopped.
- **Apply · assignment only** — Given an unfamiliar object, use `obj.__dict__` and `dir()` to report the current value of every attribute it holds and at least three of its methods.

_By the end of the module:_

- **Apply · assignment only** — Given a value that every instance of a class shares, such as a service fee added to every concert ticket, store it as a class attribute and read it through the class name.
- **Evaluate · R3** — Given two classes where one holds the other, decide whether inheritance or composition describes the relationship, and defend the choice using "is a" and "has a".
- **Evaluate · R3** — Given two proposed subclasses that differ only in the value of one attribute, judge whether they should be two classes, and name the alternative.
- **Testing** — See the 2.4 row of [Testing Objectives](#testing-objectives).

## 2.5 Polymorphism, Duck Typing, and Abstract Base Classes

**Week 8, Day 4 — Thursday 11/19**

**Fellows will be able to…**

_In the session:_

- **Understand · R4** — Given `len()` called on a string, a list, and a dictionary, and three classes that answer the same method name differently, define polymorphism in one sentence that names the caller's ignorance of the type as the benefit.
- **Apply · R4** — Given a list holding instances of at least two subtypes, write one loop that calls a shared method on every element, with no `isinstance()` and no `type()` in the loop body.
- **Apply · R4** — Given a function containing an `if isinstance(...)` branch per subtype, refactor it so each subtype answers for itself, and confirm the function's output is unchanged.

_By the end of the module:_

- **Apply · assignment only** — Given a hierarchy, define an abstract base class with at least one `@abstractmethod`, and predict the error raised when a subclass that omits it is instantiated.
- **Evaluate · R4, D1** — Given a hierarchy, decide whether to enforce its contract with an abstract base class or to document a duck-typed contract, and defend the choice by naming the case in which each one fails.
- **Analyze · R4** — Given a group of classes meant to be interchangeable, state their shared contract by listing every method name all of them must answer.
- **Testing** — See the 2.5 row of [Testing Objectives](#testing-objectives).

## 2.6 Functions as Values: Callbacks and Higher-Order Functions

**Week 8, Day 5 — Friday 11/20**

**Fellows will be able to…**

_In the session:_

- **Understand · R7** — Given examples including `sorted(items, key=...)`, define a higher-order function in one sentence, and state for each example which of the two conditions it meets.
- **Apply · R7** — Given a list of objects, use `sorted()` with a `key=` function, written once as a named function and once as a `lambda`, to order the objects by one attribute.
- **Apply · R5, R7** — Given a list of objects and two different criteria, write one method that takes a function as a parameter and returns only the elements for which it is true, then call that method with both criteria.

_By the end of the module:_

- **Analyze · R7** — Given a call that passes a function's result, such as `is_sold_out()`, where the function itself, `is_sold_out`, was expected, explain the error Python raises and correct the call.

## 2.7 Closures and Decorators

**Week 9, Day 1 — Monday 11/23**

**Fellows will be able to…**

_In the session:_

- **Apply · R7** — Given a function, write a decorator that prints a line before the function runs and returns the wrapped function's result unchanged.
- **Analyze · R7** — Given a decorator, explain which variable the wrapper closes over, and why the wrapper can still reach it after the decorator has returned.
- **Apply · R6, R7** — Given a method that moves an object from one status to the next and may only run from one status, write a decorator named for that status, such as `@requires_paid`, that refuses the call from any other status, so that the method body never runs.

_By the end of the module:_

- **Understand · assignment only** — Given a decorator factory such as `@requires_status("paid")` or `@app.route("/")`, explain the two steps Python performs when it applies one, naming the call that builds the decorator and the function the decorator then wraps.
- **Testing** — See the 2.7 row of [Testing Objectives](#testing-objectives).

## Case Study

**Week 9, Day 3 — Wednesday 11/25**

**Fellows will be able to…**

_In the session:_

- **Analyze · R6** — Given one user action, trace it through every object it touches, in order, naming the method called at each step.
- **Analyze · R6** — Given the codebase, locate every place an invalid action is refused, name the class that performs each refusal, and state the status or rule it checks.
- **Create · D1 (ADDED)** — Given the case study codebase, draw a UML class diagram showing every class, every attribute marked public or non-public, and every relationship between them.
- **Remember · D1 (optional)** — Given a provided UML class diagram of the case study, identify the class in the code that each box describes, for every box in the diagram.
- **Testing** — See the Case study row of [Testing Objectives](#testing-objectives).

_By the end of the module:_

- **Analyze · R1** — Given the case study codebase, list every class and state in one line what data each one owns.
- **Analyze · R2** — Given the codebase's non-public attributes, explain for each one what would break if it were public.
- **Evaluate · D1** — Given one structural decision the author made, judge it against one named alternative, and state what each one makes easy and what it makes hard.
- **Evaluate · D1** — Compare the case study's structure with the structure chosen for your own project, naming at least one place the two differ and why.

## 2.8 System Design and UML Diagrams

**Week 10, Day 1 — Monday 11/30**

**Fellows will be able to…**

_In the session:_

- **Create · D1** — Given a stakeholder's description of a problem, draw a UML class diagram naming every class, its responsibilities, and its relationships.
- **Apply · D1** — Given a class diagram, mark every attribute and method `+` or `-`, give a one-sentence reason for each `-`, and identify any helper that needs none of the object's data as a module function rather than a method.
- **Evaluate · D1** — Given two related classes, decide whether the reference between them is one-way or bidirectional, and defend the choice by naming the question each direction makes easy to answer.

_By the end of the module:_

- **Create · D1** — Given only a spoken description of a system, produce a diagram with at least four classes and every relationship labeled.
- **Evaluate · R1** — Given a class carrying more than four responsibilities, judge whether it should be split, and name the classes that would replace it.

## 2.9 System Design Strategies

**Week 10, Day 3 — Wednesday 12/2**

**Fellows will be able to…**

_In the session:_

- **Analyze · R5, R6** — Given a designed system, identify its coordinator and state which collections it owns and which rules it enforces.
- **Create · R6** — Given a multi-step process, design status-driven behavior for the object that moves through it: name every status, and specify which method performs each transition and what each one refuses.
- **Create · R6** — Given two entities with data belonging to neither alone, design an intermediary class holding references to both plus at least one attribute of the pairing.
- **Testing** — See the 2.9 row of [Testing Objectives](#testing-objectives).

_By the end of the module:_

- **Evaluate · D1** — Given a connection that must be created between two objects, decide which object creates it, and defend the choice by naming the real-world action it mirrors.
- **Evaluate · R6** — Given a system with several interacting entities, choose between a coordinator and direct relationships, and name one cost of the option rejected.

## 2.10 Writing a Specification You Can Hand Off

**Week 10, Day 5 — Friday 12/4**

**Fellows will be able to…**

_In the session:_

- **Create · D1** — Given your own system design, write a specification another developer could build from without asking a question, covering every class, every relationship, and every rule.
- **Analyze · D1** — Given a specification, identify at least two sentences a reader could satisfy in more than one way, and rewrite each so only one reading remains.
- **Apply · D1** — Given your specification and an AI model in tutor mode, obtain at least three questions the model cannot answer from the document, and resolve each one in the text — without asking the model to write any part of it.

_By the end of the module:_

- **Evaluate · D1 (deferred until after Mod 2)** — Given code generated from a specification, judge it against that specification and name every place the two disagree.

## Project: Object-Oriented System

**Week 11, Days 1-5 — 12/7 to 12/11, plus Week 12, Day 1 — Monday 12/14, the
fifth build day and the due date. Presented Week 12, Day 3 — 12/16. Assessed
Week 12, Day 5 — 12/18.**

**Fellows will be able to…**

- **Create · R1-R7** — Given a stakeholder brief, design and build a working CLI system of at least five classes that meets all nine project requirements.
- **Apply · R8** — Given your own system, organize it across at least three modules with an `if __name__ == "__main__":` guard, and validate every `input()` so the program never raises in front of a user.
- **Apply · R9** — Given your own class with a validating setter, write a pytest test proving the setter raises `ValueError`, and a second proving that a refused action left the collection unchanged.
- **Evaluate · D1** — Defend every design decision in your system to a reviewer, naming the alternative rejected and the reason.
- **Evaluate · D4** — Given five minutes and your own system, explain the stakeholder's problem, walk a room through your UML diagram, demonstrate one refusal live, and defend the design decision you found hardest.

---

# Proposed Key Terms

Grouped by session, in the order fellows meet them. Definitions are written to
be read by a fellow, not by an instructor.

## 2.1 Intro to OOP: Classes, `__init__`, and `self` — Thu 11/12

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
  - **`dir(obj)`** returns the names of every attribute that can be accessed through the object, including its methods.

## 2.2 Composition, `__repr__`, `__eq__`, and `@dataclass` — Fri 11/13

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

## 2.3 Properties: Non-Public Attributes and `@property` — Mon 11/16

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

## 2.4 Inheritance and Attribute Lookup — Wed 11/18

- **Inheritance** is a relationship between two classes, where a subclass receives the attributes and methods of a superclass and can add to them.
- A **superclass**, also called a **parent class**, is the class being inherited from.
- A **subclass**, also called a **child class**, is the class doing the inheriting: `class Concert(Event):`.
- **`super()`** reaches the superclass from inside a subclass. `super().__init__(...)` runs the parent's setup, and `super().method()` runs the parent's version of a method you are overriding.
- **Overriding** is defining a method in a subclass that already exists on the superclass. The subclass's version is the one that runs.
- A **class attribute** is defined in the class body rather than in `__init__`, and every instance shares the one copy. A service fee added to every concert ticket lives here: `Concert.SERVICE_FEE`.
- **Attribute lookup** is the order Python searches when code reads an attribute or calls a method: the instance first, then its class, then the superclass, and onward to `object`. Python uses the first match it finds, which is why a subclass's override runs instead of the parent's version.
  - **`obj.__dict__`** holds the attributes stored on one object. Comparing an instance's `__dict__` with its class's `__dict__` shows which step of attribute lookup finds a name.
- **`object`** is the class every Python class inherits from, and it is the last place attribute lookup searches.

## 2.5 Polymorphism, Duck Typing, and Abstract Base Classes — Thu 11/19

- **Polymorphism** is different types of object answering the same request in their own way, so that code making the request does not need to know which type it is holding. `len()` works on a string, a list, and a dictionary, and each type answers in its own way.
- A **shared interface**, or **contract**, is the set of method names every type in a group promises to answer. It is what makes polymorphism safe.
- **Duck typing** is Python's habit of caring what an object can do rather than what class it came from. If it answers `ticket_price()`, it can be treated as something with a ticket price.
- An **abstract base class (ABC)** is a class that cannot be instantiated and exists to declare the methods its subclasses must provide.
- **`@abstractmethod`** marks a method a subclass is required to define. A subclass that forgets one raises `TypeError` the moment anything tries to instantiate it, rather than failing later at the call site.
- A **concrete class** is a class you can actually instantiate, because every abstract method has been defined.

## 2.6 Functions as Values: Callbacks and Higher-Order Functions — Fri 11/20

- A **first-class function** is a function treated as a value: assigned to a variable, stored in a list, passed as an argument, or returned from another function. Python functions are first class.
- A **higher-order function** is a function that takes a function as an argument, returns a function, or both. `sorted(events, key=...)` is one: it takes a function that tells it what to sort by.
- A **callback** is a function passed into another function so that it can be called later, at the moment the receiving function decides.
- A **`lambda`** is a function written in one expression without a name, such as `lambda event: event.date`. It is most often written directly where a callback is expected.

## 2.7 Closures and Decorators — Mon 11/23

- A **closure** is formed when an inner function refers to a variable from the function that enclosed it. The inner function keeps access to that variable after the outer function has returned, which is how a decorator remembers the function it wrapped.
- A **decorator** is a higher-order function that takes a function, wraps it in another function, and returns the wrapper. The wrapper can run code before and after the original.
- The **`@` syntax** applies a decorator: writing `@requires_paid` above a method is the same as reassigning the method to the decorator's result.
- A **wrapper** is the inner function a decorator returns. It is what gets called in place of the original function.
- A **decorator factory** is a function that takes an argument and builds a decorator from it. `@requires_status("paid")` first calls `requires_status("paid")`, which returns a decorator, and then applies that decorator to the method. `@app.route("/")` in Flask works the same way.

## Case Study — Wed 11/25

- An **investigation question** asks you to find an answer in code you did not write, rather than to write new code.
- To **trace** an action is to follow it through every object it touches, in order, naming what each one does with it.

## 2.8 System Design and UML Diagrams — Mon 11/30

- **System design** is deciding which classes exist, what each one is responsible for, and how they are related, before writing the code.
- A **UML class diagram** is a drawing of those decisions: one box per class, listing its attributes and methods, with lines showing the relationships.
- A **responsibility** is a piece of data a class owns or a job it performs. A class with too many responsibilities is usually two classes.
- A **relationship** is one class knowing about another, drawn as a line between their boxes.
- A **one-way reference** means class A holds a reference to class B, and B knows nothing about A.
- A **bidirectional reference** means each class holds a reference to the other. It makes more questions easy to answer and gives you two places to keep in step.
- In a diagram, **`+`** marks a public attribute or method and **`-`** marks a non-public one (one whose name begins with `_`).
- A **helper** is a method or function that other code in the class or module calls, rather than the rest of the program. A helper that reads or changes the object's data is a non-public method. A helper that only works on the values it is given is a module function.

## 2.9 System Design Strategies — Wed 12/2

- The **Coordinator pattern** puts one class in charge of the collections of entities and the rules governing them. It stores them, validates interactions, and answers questions about them.
- **Status-driven behavior** means an object holds a status, and its methods check that status before acting, so an invalid step is refused rather than performed.
- A **status** is the stage an object has reached in a process, such as `"checked_out"` or `"returned"`.
- A **state transition** is a move from one status to the next. Transitions happen through methods, so the rules run every time.
- An **intermediary object**, also called a **join** or **association** class, represents the relationship between two entities and holds the data belonging to that pairing. A `Loan` holds the member, the item, and the due date, because the due date belongs to neither of them alone.
- **Creator responsibility** is the question of which object should create a connection object. The entity that initiates the action in the real world is usually the answer.
- A **business rule** is a constraint that comes from the stakeholder's world rather than from the code, such as a member holding no more than three items at once.
- An **invariant** is something that must always be true about the system. Protecting an attribute is how you keep one.

## 2.10 Writing a Specification You Can Hand Off — Fri 12/4

- A **specification** is a written description of what a system must do, complete enough that someone who was not in the room could build it.
- An **ambiguity** is a sentence a reader can satisfy in more than one way. Every ambiguity in a specification becomes a decision someone else makes for you.
- **Tutor mode** is using an AI model to question and check your thinking rather than to produce the work. Asking a model what your diagram is missing is tutor mode; asking it to draw the diagram is not.
- A **handoff** is giving your specification to another developer, or to a model, and having them build from it without you.

# Project Proposal

Github Link:

[https://github.com/The-Marcy-Lab-School/swe-project-2-oop-app.git](https://github.com/The-Marcy-Lab-School/swe-project-2-oop-app.git)

**Table of Contents**

- [Overview](#overview)
  - [Choose Your Path](#choose-your-path)
  - [What Both Paths Must Have](#what-both-paths-must-have)
  - [Above and Beyond](#above-and-beyond)
  - [Deliverables](#deliverables)
- [Getting Started](#getting-started)
  - [Setup Instructions](#setup-instructions)
  - [Git Workflow](#git-workflow)
- [Path A: Borough Food Rescue](#path-a-borough-food-rescue)
- [Path B: The Library of Things](#path-b-the-library-of-things)
- [Project Grading](#project-grading)
- [Tips / Common Mistakes to Avoid](#tips--common-mistakes-to-avoid)
- [Stuck Getting Started?](#stuck-getting-started)
- [How to Submit](#how-to-submit)

## Overview

A stakeholder has a problem, and they have come to you to solve it with software.

In Mod 1 you built a program. In this project you design a _system_: several
classes that each hold their own data, protect it from invalid changes, and
talk to each other through interfaces you decide on. The hard part is no longer
getting the code to run. The hard part is deciding which object is responsible
for what, and that decision is what this project assesses.

### Choose Your Path

Choose **one** of two stakeholders. Both require the same work and are graded by
the same rubric, so pick the problem you are most interested in solving.

**Path A: Borough Food Rescue** — Goal: move surplus food to neighborhood fridges
before it spoils.

**Path B: The Library of Things** — Goal: Lend tools, laptops, and instruments without
losing track of them.

Read [What Both Paths Must Have](#what-both-paths-must-have) first. Then read
your path's section and ignore the other one.

### What Both Paths Must Have

Your rubric checks these nine things. Every number below is countable, so you
can check your own work before you submit it. The _names_ of your classes depend
on your path.

**1. Classes.** Define **at least five classes**, filling these roles:

| Role                                                                | How many   |
| ------------------------------------------------------------------- | ---------- |
| A coordinator that owns the collections and enforces the rules      | 1          |
| A superclass whose subclasses behave differently                    | 1          |
| Subclasses of that superclass                                       | at least 2 |
| An intermediary that represents a relationship between two entities | 1          |

Every class you define has **at least 3 attributes**, **at least 2 methods**, and
a `__repr__` that returns something you would want to see in a traceback.

**2. Encapsulation.** **At least 3 attributes that have a rule** across your
system are non-public and guarded by a `@property`. A read-only property counts.
**At least 1 setter refuses an invalid value** and tells the user why, instead
of storing it.

Ask of each attribute: would your system break if this held a wrong value? A fridge's capacity or a member's borrowing limit cannot go negative, and a loan's status has to be one of checked out, returned, overdue, or lost. Those need protecting. A donor's phone number or an item's description does not, because there is no wrong value to catch.

**3. Inheritance.** One superclass and **at least 2 subclasses**. Each subclass
calls `super().__init__()`, and **at least 1 method is overridden** so that it
returns a different result in each subclass.

A subclass that only sets `self.kind = "laptop"` doesn’t behave differently. The subclasses have to _behave_ differently.

**4. Polymorphism.** **At least 1 loop** calls the same method on a list holding
more than one subtype. That loop contains **no `isinstance()` and no `type()`**thus relying solely on method overrides to alter behavior.

In `DESIGN.md`, list the method names that every one of those subtypes defines. That list is the contract the loop depends on: the loop can stay the same because the same method names can be accessed through every object in it.

**5. Collections of objects.** **At least 1 class stores a list of instances of another class you wrote** as an attribute — a fridge holding its deliveries, a member holding their loans — and has **at least 2 methods that search or filter that list** and return the matches. A list of dictionaries does not count.

**6. Design strategies — all three.** You are already building all three. Requirement 1 asks for a coordinator and an intermediary, and both paths need a delivery or a loan that moves through states. So these are not three new things to invent. Each one has to meet the counts in the table below, and each one has to be named in `DESIGN.md` with the class that implements it.

| Strategy                   | What it takes to count                                                                                                            |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Coordinator**            | One class stores at least 2 collections and refuses at least 1 invalid action with a message to the user                          |
| **Status-Driven Behavior** | One class holds a `_status`, and at least 2 of its methods refuse to run from the wrong status                                    |
| **Intermediary Object**    | One class holds references to 2 other objects, plus at least 1 attribute that belongs to the pairing rather than to either object |

**7. A higher-order function.** Write **at least 1**, in either form:

- a **decorator** you wrote, wrapping a method that changes state — a
  `@requires_status` guard is the natural one here, or
- a **method that takes a function as a parameter** and uses it to filter or
  sort a collection.

Say in `DESIGN.md` which form you chose and what it bought you.

**8. Skills from Mod 1, still required.** Nothing you learned in Mod 1 expires.

- **At least 3 modules**, connected with `import`, with an
  `if __name__ == "__main__":` guard in the entry point
- **At least 1 dictionary** used as a lookup
- **At least 1 comprehension or built-in iteration tool** (`sorted()`, `sum()`,
  `enumerate()`, `any()`, `all()`) inside a report
- **Every `input()` validated**, with `try`/`except ValueError` or a string
  method such as `.isdigit()`, so the program never raises in front of a user
- **f-strings** for every message you print
- `requirements.txt` exists and `.venv/` is listed in `.gitignore`

1. **Tests, on the parts that refuse.** pytest is a Mod 1 skill and it does not expire either. Write **at least 2 tests** in a `tests/` directory that pass when you run `pytest` from the project root:
   - **At least 1 test uses `pytest.raises(ValueError)`** to prove your `@property` setter refuses an invalid value.
   - **At least 1 test proves a refusal changed nothing** — after the coordinator turns down an action, the collection is the same length it was, or the status is the one it started with.

Your data lives in memory while the program runs. **You are not asked to save
anything to a file**, so do not build a save system.

### Above and Beyond

Not graded, not required. This is where to go once your required work runs.

1. **An abstract base class (ABC).** Replace your documented duck-typed contract with
   an ABC and at least one `@abstractmethod`, so a subclass that forgets a method
   fails at instantiation rather than at the call site.
2. **A `@dataclass`** for a value object your system carries around and compares.
   Your `DESIGN.md` already argues about whether one belongs here — this is
   building the version you argued for.
3. **A second higher-order function**, in the form you did not use for
   requirement 7.
4. **Issue each ID from the coordinator.** The coordinator stores the next ID
   and hands it to each new record it creates, so no two records can collide.
5. **More tests than the two required.** Cover every status transition, including the ones that are supposed to fail, and use a fixture so each test starts from a system you did not have to build by hand.
6. **Persistence.** Save to JSON on exit and load on start.

### Deliverables

**1. `DESIGN.md`, due at the start of project week.** Five things:

1. A **UML class diagram**. Draw it by hand and photograph it, or write it as text. Mark every attribute `+` public or `-` non-public (one whose name begins with `_`).
2. **One line per class**: what data it owns, and what it can do.
3. **One line per relationship**: which class knows about which, whether that is one-way or bidirectional, and why.
4. **The three design strategies** you used, each named with its class, and one sentence on your higher-order function: which form you chose and what it bought you.
5. **One design decision you struggled with**, the options you saw, and how you settled it. A decision about something you chose _not_ to build counts — "`Loan` could have been a `@dataclass`, and here is why it is not" is a good answer. Being able to explain the option you rejected is the point, because an engineer who can only defend what they built cannot be reviewed.

Write it so that another developer could build your system from it without asking you a single question.

**Using AI on `DESIGN.md`.** Tutor mode is the right mode here, and you are encouraged to use it. Ask a model to find a relationship your diagram is missing, to tell you which responsibility is ambiguous, or to argue the other side of your design decision. Do not ask it to produce the diagram. You have to be able to defend every line, because in December you will hand this document to a model, ask it to build a new feature from it, and find what it got wrong. A document you did not reason through gives you nothing to judge the output against.

Practice saying it out loud. You will be asked to explain this system and defend the decisions inside it, and the explanation you want in that moment is the one you already wrote here.

**2. The application**, meeting your path's requirements.

**3. `REFLECTIONS.md`**, two responses of 150-250 words each. Prompts are in [Project Grading](#project-grading).

**4. A five-minute share-out**, presented on the sixth day.

1. The stakeholder's problem, in your own words, in two sentences.
2. A walk through your UML diagram, naming what each class owns.
3. **One refusal, demonstrated live.** Try the thing your system will not allow and let everyone see the message.
4. The design decision you struggled with, and how you settled it.
5. What you would change if you started again.

Every piece in step 4 except the live demo is already written in `DESIGN.md`. You are not preparing new material; you are saying out loud what you already decided, which is also what the module assessment asks you to do.

## Getting Started

### Setup Instructions

1. Go to the `swe-project-2-oop-app` template repository and click "Use this
   template". Set yourself as the owner and give your project a descriptive name.
2. Clone your repo down to your computer.
3. Create and activate a virtual environment: `python3 -m venv .venv` and then
   `source .venv/bin/activate`.
4. Check that `.venv/` is listed in your `.gitignore` file.
5. Create `requirements.txt` with `pip freeze > requirements.txt`. Add to it if
   you install anything.
6. Add, commit, and push all files with the message `"initializing project"`.

### Git Workflow

Your `main` branch holds the most recent **working** version of your
application. Build on a branch and merge when the feature runs.

```bash
git checkout -b feature-name
# write code, test it, commit
git checkout main
git merge feature-name
```

Commit every time something works. A commit you can return to is worth more
than a commit that is tidy.

## Path A: Borough Food Rescue

> **Borough Food Rescue** moves surplus food from restaurants and grocers to
> twelve neighborhood fridges. Today one coordinator runs the whole operation
> from a group chat and a spreadsheet, and two things keep going wrong. Food gets promised to a fridge that is already full, so a volunteer drives across the
> borough and has nowhere to leave it. And perishable food sits in the
> spreadsheet long enough to expire, so it gets thrown away at the fridge instead
> of eaten. They have asked you to build a system that tracks what food is
> available, where it is allowed to go, and what state every delivery is in.

**The entities in this domain** are donor sites, fridge locations, food items,
and deliveries. Food items come in at least two kinds: **perishable** items,
which expire, and **shelf-stable** items, which do not. How those entities are
structured, which of them owns which data, and which of them are related is your
design work.

**Required features**

1. **Register a donor site and a fridge location.** A fridge has a capacity, and
   the system knows how full it is right now.
2. **Add a food item to the system**, from a donor site. Perishable and
   shelf-stable items both answer "how many days until you expire?" — and they
   answer it differently.
3. **Claim an item for a fridge.** This creates a delivery. The system **refuses**
   the claim when the fridge has no room, and when a perishable item would expire
   before it could be delivered.
4. **Move a delivery through its states**: claimed, in transit, delivered. A
   delivery that has already been delivered cannot be delivered again, and
   attempting it gets a clear message rather than a second delivery.
5. **Report**: what food is available now, what is in transit, what each fridge is
   holding, and what expired before anyone moved it.

**Stretch features to consider**

- A volunteer entity, assigned to deliveries, with a cap on how many they carry
  at once.
- Expiry-aware prioritization: the report suggests which item to move first.
- A second fridge-level rule, such as refusing items a fridge cannot store.

## Path B: The Library of Things

> **The Library of Things** lends more than books. It lends power tools, laptops,
> and musical instruments, and it lends them on paper index cards. Two things keep going wrong. An item gets lent twice, because the card for the first loan is in a different drawer, and the second borrower arrives to collect something that
> left the building yesterday. And members walk out with eight items at once,
> because nothing stops them, and those items do not come back. They have asked you to build a system that tracks every item, every member, and the state of every loan.

**The entities in this domain** are members, catalog items, loans, and the
lending desk itself. Catalog items come in at least two kinds — tools, laptops,
instruments — and they do not all behave the same way. How those entities are
structured, which of them owns which data, and which of them are related is your
design work.

**Required features**

1. **Register a member and add items to the catalog.** A member has a borrowing
   limit, and the system knows how many items they are holding right now.
2. **Items answer two questions differently by kind**: "when are you due back?"
   and "what is the late fee per day?" A laptop is not due back on the same
   schedule as a hammer.
3. **Check an item out to a member.** This creates a loan. The system **refuses**
   the checkout when the item is already on loan, and when the member is at their
   limit.
4. **Move a loan through its states**: checked out, returned, overdue, lost. A
   loan that has been returned cannot be returned again, and attempting it gets a
   clear message rather than a second return.
5. **Report**: what is on the shelf, what is out, what each member is holding, and
   what is overdue along with the fees owed.

**Stretch features to consider**

- A hold queue: a member requests an item that is out and is notified in turn.
- A condition log on each item, recorded at checkout and return.
- A second desk-level rule, such as blocking checkout for a member who owes fees.

## Project Grading

Every line below is countable, so you can check your own project against it
before you submit. Your project is assessed out of 3**5 points**.

- Stakeholder Requirements — 5 features x1 (5 Points)
- Core OOP Concepts (7 points)
- Design Strategies, Collections, and Higher-Order Functions (6 points)
- System Design (3 points)
- Tests (2 points)
- Skills from Mod 1 and Code Organization (3 points)
- Reflection.md + presentation (4 points)
- Professionalism and Craftsmanship (5 points)

### Stakeholder Requirements (5 points)

One point per required feature in your path's brief. These lines ask only whether the feature works, so run each one before you submit.

1. Both kinds of record can be registered, and the system reports the current state that limits them — how full a fridge is, or how many items a member is holding.
2. Both kinds of item answer their shared question, and the two kinds give different answers.
3. Claiming or checking out creates the delivery or the loan, and is refused in both of the cases your brief names, each with a message the user can read.
4. The delivery or loan moves through its states, and repeating a step that is already done is refused with a message rather than happening twice.
5. Every report your brief asks for runs and prints the right rows.

### Core OOP Concepts (7 points)

1. At least 5 classes are defined, each with at least 3 attributes and at least 2 methods, covering coordinator, superclass, 2 subclasses, and intermediary.
2. Every class returns a useful string from `__repr__`.
3. At least 3 attributes that have a rule are non-public and guarded by a `@property`. A read-only property counts.
4. At least 1 `@property` setter refuses an invalid value and says why.
5. Every subclass calls `super().__init__()`.
6. At least 1 method is overridden and returns a different result per subclass.
7. At least 1 loop calls a shared method on mixed subtypes, with no `isinstance()` and no `type()` inside it, and `DESIGN.md` lists the method names every subtype defines.

### Design Strategies, Collections, and Higher-Order Functions (6 points)

1. Coordinator, Status-Driven Behavior, and Intermediary Object all appear in the code and are named in `DESIGN.md` with their class.
2. The coordinator stores at least 2 collections and refuses at least 1 invalid action, with a message to the user rather than a silent failure.
3. The status-driven class holds a `_status`, and at least 2 of its methods refuse to run from the wrong status.
4. The intermediary holds references to 2 other objects and at least 1 attribute that belongs to the pairing rather than to either object.
5. At least 1 class stores a list of instances of another class, not dictionaries, and has at least 2 methods that search or filter it.
6. At least 1 higher-order function is written, and `DESIGN.md` says which form it takes and what it bought.

### System Design (3 points)

1. `DESIGN.md` contains a UML class diagram that marks every attribute public or non-public, every class in the diagram exists in the code, and each class has a line saying what data it owns and what it can do.
2. Every relationship is listed with a direction and a reason.
3. One design decision is written up with the options considered and the reasoning that settled it.

### Tests (2 points)

1. At least 1 test uses `pytest.raises(ValueError)` to prove a `@property` setter refuses an invalid value.
2. At least 1 test proves a refused action changed nothing: after the refusal the collection is the same length, or the status is unchanged.

Both live in `tests/` and pass when `pytest` is run from the project root.

### Skills from Mod 1 and Code Organization (3 points)

1. Code is split across at least 3 modules, connected with `import`, with an `if __name__ == "__main__":` guard in the entry point.
2. At least 1 dictionary lookup and at least 1 comprehension or built-in iteration tool appear in a report, and every printed message uses an f-string.
3. Every `input()` is validated, the program never raises in normal use, `requirements.txt` exists, and `.venv/` is in `.gitignore`.

### Reflection.md + Presentation (4 points)

In `REFLECTIONS.md`, respond to both prompts in 150-250 words each.

1. Describe one design decision where you chose between two reasonable structures. What did you choose, what did you give up, and what would make you choose differently next time?
2. Explain one Mod 2 concept you understand more deeply after building this, in plain terms, and point to the place in your code where it earns its keep.

In the share-out on 12/16:

1. All five beats are covered in five minutes, and the refusal is demonstrated live rather than described.
2. Every class named in the walkthrough matches a class in the code, and every question about why a decision was made gets an answer.

### Professionalism and Craftsmanship (5 points)

1. Code is functional and raises no errors under expected use.
2. Code is well organized, names are descriptive, comments are purposeful, and no unused code remains.
3. Commits are small, frequent, and meaningfully described.
4. A branch is used for development, and `main` always runs.
5. `README.md` explains setup, usage, and functionality. Writing in `README.md`, `DESIGN.md`, and `REFLECTIONS.md` is polished.

## Tips / Common Mistakes to Avoid

| Mistake                                    | What to Do Instead                                                                                                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Designing at the keyboard                  | Draw the UML first. Thirty minutes on paper saves a day of restructuring.                                                             |
| One class that does everything             | If a class's name needs "and" in it, it is two classes.                                                                               |
| Storing relationship data on an entity     | A loan's due date belongs to the loan, not to the item and not to the member. That is what the intermediary object is for.            |
| Making every attribute public              | Ask of each one: would the system break if this held a wrong value? If yes, protect it.                                               |
| Subclasses that differ only by a string    | A subclass earns its place by behaving differently. If every method is identical, you wanted an attribute.                            |
| Asking AI to draw your UML                 | Ask it to find what your diagram is missing. You cannot defend a design you did not reason through, and in December you will have to. |
| `if isinstance(...)` branching on subtype  | Move the differing behavior into the subclasses and call the method. That is polymorphism doing the work.                             |
| Letting any object change another's status | Status changes go through a method on the object that owns the status, so the rules run every time.                                   |
| Building all five features, then testing   | Build one feature, run it, commit, move on.                                                                                           |

## Stuck Getting Started?

Five build days, and the share-out on the sixth. Commit at the end of every step, not at the end of every day.

**Before Day 1: `DESIGN.md` is already done.** It was due at the start of the week. Keep it open beside your editor, and when the code disagrees with the diagram, change the diagram.

**Day 1 — the entities, running.** Pick the simplest entity. Write `__init__` and `__repr__`, create two instances in `main.py`, and print them. Then write the superclass and its two subclasses, give them the one method each subclass answers differently, and loop over a mixed list calling it. By the end of today, objects exist and print.

**Day 2 — protect the data, then connect it.** Make the attributes that could hold wrong values non-public with a `@property`, and make one setter raise `ValueError`. **Write your first test now**, while the setter is fresh: one `pytest.raises(ValueError)`. Then write the intermediary — the class that connects two entities, holding a `_status` and the methods that move it from one status to the next, each refusing to act from the wrong status.

**Day 3 — the coordinator and the rules.** Write the class that owns the collections. Put the refusals in it: the capacity or limit check, and the already-out check. Add the methods that search or filter its lists, because the reports are going to need them. **Write your second test**: refuse an action, then assert the collection is the same length it was.

**Day 4 — the menu and the reports.** Wire the features to numbered choices and validate every input. Build the reports out of the search methods you wrote yesterday. Split the code across at least three modules if you have not already, and put the `if __name__ == "__main__":` guard in the entry point. Write your higher-order function today — if you chose the decorator, it wraps the transition methods from Day 2.

**Day 5 — polish and rehearse.** The project is due at the end of today. Make `DESIGN.md` match the code you actually wrote, write `REFLECTIONS.md`, run `pytest` one more time, and reread every message your program prints for spelling. Then run your five beats out loud once, with a timer.

## How to Submit

1. Push your work to `main` and confirm the application runs from a fresh clone.
2. Run `pytest` from the project root and confirm both required tests pass.
3. Confirm `DESIGN.md`, `REFLECTIONS.md`, and `README.md` are all present and polished.
4. Submit your repository link.
5. Bring your five beats to the share-out on 12/16, ready to demonstrate a refusal live.
