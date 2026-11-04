# Mod 2 - Object-Oriented Programming

In Mod 1 you learned to write a _program_: functions that work on lists and dictionaries. Nothing in that program ties data to the rules about it. If reservations are dictionaries in a list, any line anywhere can set `reservation["status"] = "chekced_in"`, and the typo goes in silently and turns into a bug somewhere else, later, where it is much harder to find.

In this module you learn to build a _system_ instead: several objects, each one owning its own data and protecting it. Then you learn to write that system down as a _specification_, a description clear enough that someone else could build it from the page. The hardest skill in the module is not writing a class. It is deciding which object is responsible for what, and writing that decision down.

That skill matters beyond this module. In Mod 3, AI moves from tutor to implementer: you will hand a design document to a model, ask it to build a new feature, and check what it built. A model can only build what your design document actually says, and you can only judge its work against a design you reasoned through yourself. The Mod 2 project is the last project you write entirely by hand, and it is where you practice the design half of that work.

**By the end of this module, you will be able to:**

- Design a system of classes for a stakeholder's problem, deciding which class owns each piece of data and each rule.
- Write classes that protect their own data, refusing an invalid value or an invalid action with a message that says why.
- Use inheritance and polymorphism so that one loop can work with several kinds of object without checking which kind each one is.
- Write a decorator that stops a method from running when an object is in the wrong state.
- Implement tests that prove a refusal happened and that it changed nothing.
- Write a specification another developer could build your system from without asking you a question.
- Explain each design decision in your system, naming the alternative you rejected and why.

## One Idea Throughout: Refusal

A Mod 1 program accepts whatever it is given. A well-designed system refuses: it turns down a negative ticket count, a second check-in for the same reservation, or a booking for a sold-out show, and it says why. Every lesson in this module adds a new way for a system to refuse an invalid change instead of letting it in silently, and the project ends with you demonstrating a refusal live.

## The Case Study: Venue Tickets

Every lesson uses one application: a ticketing system for a community venue. You clone it in the first lesson and return to it in every lesson after. Each lesson's checks for understanding and exit ticket are questions about its code.

Much of the case study's code will be unfamiliar the first time you see it, and that is intended. Seeing the same application again and again makes the code familiar before the lesson that explains it, so when a lesson introduces a new idea, you have already seen it working.

The case study is a complete system, so it lets you explore what no single lesson can show on its own:

- **How one action travels through a system.** Buying a ticket passes through several objects, and tracing it shows what each one is responsible for.
- **Where the rules live.** Every refusal in the code belongs to a particular class, and each one enforces a rule about the venue.
- **What the tests protect.** Each test in the case study guards one rule, and reading the tests is a quick way to find the rules that matter most.
- **What the whole system looks like as a diagram.** Drawing the classes and their relationships, or matching a provided diagram to the code, shows the design the code carries out.

## Part 1: Objects That Own Their Data (2.1–2.3)

In Mod 1, data and the rules about it live in different places, so nothing stops bad data getting in. This part puts the data and its rules in the same object.

**2.1 Intro to OOP.** A class bundles data with the methods that act on it, and `self` is the object a method was called on. Introspection (`type()`, `dir()`, `__dict__`) shows that the lists and dictionaries from Mod 1 were objects all along.

You also clone the case study and meet its classes:

- `Venue` runs the whole system. It holds every event, attendee, and reservation, and it refuses actions that break the venue's rules, such as booking a sold-out event.
- `Event` holds what every event has: a name, a date, a capacity, and a price. Its subclasses `Concert`, `Workshop`, and `Screening` each set their own ticket price and refund rule.
- `Attendee` is a person who books tickets.
- `Reservation` connects one attendee to one event, records the price paid, and moves from reserved, to paid, to checked in, or to refunded.

Each event's date is a `datetime.date` object from Python's standard library, the most common way to store a date in Python.

**2.2 Classes.** Every event at the venue holds different data, but every event needs the same set of attributes: the same _shape_. When attributes are added to an object one at a time after it is created, one event can end up without a date, and any code that reads `event.date` crashes on that one event. `__init__` solves this. Every instance is built by the same method, which receives the instance's data as arguments, so every event has the same shape and its own values. `__repr__` makes each instance identify itself when printed. Once objects exist, related classes can hold one another: a `Reservation` holds an `Event` and an `Attendee`, and a `Venue` holds a list of reservations. You also write your first test of an object.

**2.3 Conventions.** Nothing so far stops code from setting an event's capacity to `-5` or a reservation's status to a misspelled value, because the class has not declared anything about how its data changes. A class can enforce rules about how its data is changed, so that a setter called with an invalid value refuses it. An attribute whose name starts with an underscore, a `@property` that reads it, and a setter that raises `ValueError` together make the module's first refusal. A test using `pytest.raises` proves the refusal works. `@dataclass`, class methods, and static methods round out the tools a class can offer.

## Part 2: Families of Objects (2.4–2.7)

Concerts, workshops, and screenings are alike in most ways and different in a few, such as price and refund rule. Written in the Mod 1 style, every function would branch with `if`/`elif` on the kind of event, and adding a new kind of event would mean editing every one of those functions. This part lets each kind of event answer for itself.

**2.4 Inheritance.** An `Event` superclass holds what is shared, and subclasses override what differs. `super().__init__()` runs the parent's setup, and the method resolution order tells you which version of a method runs.

**2.5 Polymorphism.** One loop asks every event in a mixed list for its price, with no `isinstance()` check. The loop works because every kind of event answers the same method names, and that list of names is the **contract**. Writing the contract down is the first time you record an agreement between pieces of code, which makes it a small specification.

Decorators are built from two earlier ideas, functions as values and closures, so they take two lessons.

**2.6 Functions as Values.** Functions are values: they can be stored, passed to another function, and returned from one. A higher-order function takes or returns a function, as `sorted(events, key=...)` does, and a `lambda` writes a short function directly where one is expected.

**2.7 Closures and Decorators.** A closure is an inner function that keeps access to the variables of the function around it, and a decorator uses a closure to wrap one function in another.

A decorator is a **reusable refusal**. A reservation may only be checked in once it is paid, so `check_in()` should refuse to run from any other status. Without a decorator, every method that requires a status repeats the same check, and forgetting it in one method lets an invalid change through. You write one decorator per status, named for the rule it enforces, such as `@requires_paid` above `check_in()`.

You also read a decorator factory, such as `@requires_status("paid")`: a function that takes an argument and builds a decorator from it. Flask, which you use in Mod 3, writes every route with one: `@app.route("/")`.

## Part 3: Designing the System Before Building It (2.8–2.10)

Once a system has five or more classes, the hard question is no longer how to write a class but which class owns what. Deciding that at the keyboard leads to restructuring halfway through the build. This part makes the design a document that comes before the code.

**2.8 UML.** You draw the classes, their responsibilities, and their relationships, and you decide whether each relationship is one-way or bidirectional.

**2.9 Strategies.** This lesson names three patterns that the case study has used since the first lesson:

- **Coordinator:** `Venue`, which owns the collections and enforces the rules.
- **Status-driven behavior:** a `Reservation` moving from reserved, to paid, to checked in, with each step refused from the wrong status.
- **Intermediary:** the same `Reservation`, linking an attendee to an event and holding what belongs to that pairing, such as the price paid.

The refusals from 2.3 and 2.7 become rules for the whole system, and you write a test that proves a refused action leaves everything unchanged.

**2.10 Specification.** You write the design down so that another developer could build it without asking a question, and you use AI in tutor mode to find the sentences that could be read more than one way.

## The Project

A stakeholder brings you a problem, and you design and build a system that solves it. You write the design document first. Then you build the system in the order the module taught it: the objects and their class hierarchy, the protected data and its first test, the coordinator and its refusals with the second test, and finally the menu, the reports, and a higher-order function. The project ends with a five-minute share-out, where you walk through your design, explain the decision you found hardest, and demonstrate one refusal live.
