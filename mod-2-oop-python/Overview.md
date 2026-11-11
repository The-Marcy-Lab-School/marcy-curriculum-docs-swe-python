# Mod 2 - Object-Oriented Programming

In Mod 1 you learned to write a _program_: functions that work on lists and dictionaries. Nothing in that program ties data to the rules about it. If reservations are dictionaries in a list, any line anywhere can set `reservation["status"] = "chekced_in"`, and the typo goes in silently and turns into a bug somewhere else, later, where it is much harder to find.

In this module you learn to build a _system_ instead: several objects, each one owning its own data and protecting it. Then you learn to write that system down as a _specification_, a description clear enough that someone else could build it from the page. The hardest skill in the module is not writing a class. It is deciding which object is responsible for what, and writing that decision down.

That skill matters beyond this module. In Mod 3, AI moves from tutor to implementer: you will hand a design document to a model, ask it to build a new feature, and check what it built. A model can only build what your design document actually says, and you can only judge its work against a design you reasoned through yourself. The Mod 2 project is the last project you write entirely by hand, and it is where you practice the design half of that work.

**By the end of this module, you will be able to:**

- Design a system of classes for a stakeholder's problem, deciding which class owns each piece of data and each rule.
- Design each class's interface so that the rest of the system can use the class's data only in the ways it intends.
- Write classes that protect their own data, refusing an invalid value or an invalid action with a message that says why.
- Use inheritance and polymorphism so that one loop can work with several kinds of object without checking which kind each one is.
- Write a decorator that stops a method from running when an object is in the wrong state.
- Implement tests that prove a refusal happened and that it changed nothing.
- Write a specification another developer could build your system from without asking you a question.
- Explain each design decision in your system, naming the alternative you rejected and why.

## Two Ideas Throughout

### Refusal

A Mod 1 program accepts whatever it is given. A well-designed system refuses: it turns down a negative ticket count, a second check-in for the same reservation, or a booking for a sold-out show, and it says why. Every lesson in this module adds a new way for a system to refuse an invalid change instead of letting it in silently, and the project ends with you demonstrating a refusal live.

### Interfaces That Constrain How Data Is Used

The big shift in this module is from writing functions to designing a system of classes that work together. Two questions shape every decision in that design: which object owns each piece of data, and how that object lets the rest of the system use its data. A class answers the second question with its **interface**, the attributes and methods it offers to other code. A well-designed interface constrains whoever uses the class to use it only as intended. The venue owns its reservations, so other code books a ticket by calling `venue.book()`, which checks the venue's rules, rather than adding to the venue's list directly. A reservation's status can be read through `reservation.status`, but it can only change through `pay()`, `check_in()`, and `refund()`, and each of those refuses to act from the wrong status. Refusal is how an interface holds to its constraints when other code tries something it was not designed to allow.

Each lesson adds a tool for building interfaces like these, and your design document records which class owns each piece of data and what its interface lets other code do with it.

## The Case Study: Venue Tickets

Every lesson uses one application: a ticketing system for a community venue. You clone it in the first lesson and return to it in every lesson after. Each lesson's checks for understanding and exit ticket are questions about its code.

Much of the case study's code will be unfamiliar the first time you see it, and that is intended. Seeing the same application again and again makes the code familiar before the lesson that explains it, so when a lesson introduces a new idea, you have already seen it working.

The case study is a complete system, so it lets you explore what no single lesson can show on its own:

- **How one action travels through a system.** Buying a ticket passes through several objects, and tracing it shows what each one is responsible for.
- **Where the rules live.** Every refusal in the code belongs to a particular class, and each one enforces a rule about the venue.
- **What the tests protect.** Each test in the case study guards one rule, and reading the tests is a quick way to find the rules that matter most.
- **What the whole system looks like as a diagram.** In 2.8, drawing the case study's classes and their relationships shows the design the code carries out.

The case study session, after 2.7, reviews the whole module through the case study's tests. For each idea the module taught, you find the test that protects it and state its rule in one sentence, trace a user action from a test through every object it touches, and predict which tests fail when one rule in the code is broken. The session also introduces fixtures, the shared setup in `tests/conftest.py` that gives every test a new venue, and you leave with a rule that no test protects yet, which your own project's tests can learn from.

## Part 1: Objects That Own Their Data (2.1–2.3)

In Mod 1, data and the rules about it live in different places, so nothing stops bad data getting in. This part puts the data and its rules in the same object.

**2.1 Intro to OOP.** Strings and lists from Mod 1 already have methods, such as `'hello'.upper()`. `type('hello')` shows that the string was made from a class, `str`, and `dir('hello')` lists the methods that class gives it.

Then you write your own classes. Every event at the venue holds different data, but every event needs the same set of attributes: the same _shape_. When attributes are added to an object one at a time after it is created, one event can end up without a date, and any code that reads `event.date` crashes on that one event. `__init__` solves this. Every instance is built by the same method, which receives the instance's data as arguments, so every event has the same shape and its own values. Your methods receive the instance they were called on as `self`, because Python passes the value before the dot into the method as its first argument: `jazz.seats_left()` is the same call as `Event.seats_left(jazz)`, just as `'hello'.upper()` is the same call as `str.upper('hello')`. A class that bundles data with the methods that act on it gives the rest of the program one place to reach that data.

You also clone the case study and meet its classes:

- `Venue` runs the whole system. It holds every event, attendee, and reservation, and it refuses actions that break the venue's rules, such as booking a sold-out event.
- `Event` holds what every event has: a name, a date, a capacity, and a price. Its subclasses `Concert`, `Workshop`, and `Screening` each set their own ticket price and refund rule.
- `Attendee` is a person who books tickets.
- `Reservation` connects one attendee to one event, records the price paid, and moves from reserved, to paid, to checked in, or to refunded.

Each event's date is a `datetime.date` object from Python's standard library, the most common way to store a date in Python.

**2.2 Composition.** A program holds many objects at once. Composition is one object holding others as attributes: a `Venue` holds a list of events, and `venue.events[0].name` reaches through the venue to one event's data. Once a program holds many objects, it has to tell them apart, and Python's built-in operations work on your objects through dunder methods:

- `print()` calls `__repr__`, so a printed list of events says which event is which.
- `==` calls `__eq__`, and without one, `==` only asks whether two names refer to the same object. `in` compares with `==`, so an `__eq__` that compares an event's name and date lets the venue find an event it already holds and refuse to add it twice.
- `@dataclass` writes `__init__`, `__repr__`, and `__eq__` for you, from the attribute names you list, which suits a class that mostly carries data.

A `Reservation` that holds an `Attendee` and an `Event` brings these ideas together. You also write your first test of an object, which proves that the venue refuses a duplicate event.

**2.3 Properties.** Nothing so far stops code from going around a class's rules: a line that changes an event's seat count directly skips the sold-out check, and a line that sets its capacity to `0` breaks the seat count, because assigning to an attribute runs no code in the class. A class can take part in those assignments. Data with no rule stays a public attribute. Data with a rule becomes non-public, with a name that starts with an underscore, and a `@property` reads it. A property with no setter lets other code read the value but never assign it, and a setter refuses an invalid value by raising `ValueError`. Code that read `event.capacity` before keeps working unchanged. A test using `pytest.raises` proves the refusal works.

## Part 2: Families of Objects (2.4–2.7)

Concerts, workshops, and screenings are alike in most ways and different in a few, such as price and refund rule. Written in the Mod 1 style, every function would branch with `if`/`elif` on the kind of event, and adding a new kind of event would mean editing every one of those functions. This part lets each kind of event answer for itself.

**2.4 Inheritance.** An `Event` superclass holds what is shared, and subclasses override what differs. `super().__init__()` runs the parent's setup. When code reads an attribute or calls a method, Python looks on the instance first, then on its class, then on the parent class, and uses the first one it finds. That search is how a subclass's version of a method replaces the parent's. A class attribute belongs to the class rather than to one instance, so it holds a value every instance shares, such as a concert's service fee, and the same search is how an instance finds it.

**2.5 Polymorphism.** `len()` already works on a string, a list, and a dictionary, and a `for` loop works over all three: each type answers the same request in its own way. That is polymorphism, and your own classes can do it too. One loop asks every event in a mixed list for its price, with no `isinstance()` check. The loop works because the same method names can be accessed through every kind of event, and that list of names is the **contract**. Writing the contract down is the first time you record an agreement between pieces of code, which makes it a small specification.

Decorators are built from two earlier ideas, functions as values and closures, so they take two lessons.

**2.6 Functions as Values.** Functions are values: they can be stored, passed to another function, and returned from one. A higher-order function takes or returns a function, as `sorted(events, key=...)` does, and a `lambda` writes a short function directly where one is expected.

**2.7 Closures and Decorators.** A closure is an inner function that keeps access to the variables of the function around it, and a decorator uses a closure to wrap one function in another.

A decorator is a **reusable refusal**. A reservation may only be checked in once it is paid, so `check_in()` should refuse to run from any other status. Without a decorator, every method that requires a status repeats the same check, and forgetting it in one method lets an invalid change through. You write one decorator per status, named for the rule it enforces, such as `@requires_paid` above `check_in()`.

You also read a decorator factory, such as `@requires_status("paid")`: a function that takes an argument and builds a decorator from it. Flask, which you use in Mod 3, writes every route with one: `@app.route("/")`.

## Part 3: Designing the System Before Building It (2.8–2.10)

Once a system has five or more classes, the hard question is no longer how to write a class but which class owns what. Deciding that at the keyboard leads to restructuring halfway through the build. This part makes the design a document that comes before the code.

**2.8 UML.** You draw the classes, their responsibilities, and their relationships, and you decide whether each relationship is one-way or bidirectional. The case study is the first system you draw.

**2.9 Strategies.** This lesson names three patterns that the case study has used since the first lesson:

- **Coordinator:** `Venue`, which owns the collections and enforces the rules.
- **Status-driven behavior:** a `Reservation` moving from reserved, to paid, to checked in, with each step refused from the wrong status.
- **Intermediary:** the same `Reservation`, linking an attendee to an event and holding what belongs to that pairing, such as the price paid.

The refusals from 2.3 and 2.7 become rules for the whole system, and you write a test that proves a refused action leaves everything unchanged.

**2.10 Specification.** You write the design down so that another developer could build it without asking a question, and you use AI in tutor mode to find the sentences that could be read more than one way.

## The Project

A stakeholder brings you a problem, and you design and build a system that solves it. You write the design document first. Then you build the system in the order the module taught it: the objects and their class hierarchy, the protected data and its first test, the coordinator and its refusals with the second test, and finally the menu, the reports, and a higher-order function. The project ends with a five-minute share-out, where you walk through your design, explain the decision you found hardest, and demonstrate one refusal live.
