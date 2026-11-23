# Code Block Audit: Lessons 1.1 to 2.7

This document tracks the work of making every runnable code block in the Module 1 and Module 2 lessons run in the LMS. It lists what each failing block needs, the decisions waiting for Ben, and how to check the work. It is a working document for the next session, not a page fellows read, so it is not listed in `SUMMARY.md`.

## The rule being applied

The LMS runs each Python block in a fresh interpreter, so a block can use only the names it defines itself. Every runnable block must run on its own and print exactly what its output comments say. [authoring-guide.md](authoring-guide.md) gives the full syntax. A block that depends on earlier code gets one of three fixes:

- **A visible copy** of a short definition, about 8 lines or fewer, under a comment such as `# unchanged from the previous example`. The visible copies already in the lessons stay visible.
- **A hidden setup:** a `<!-- setup: name … -->` comment placed directly after the visible block it copies, and a `<!-- uses: name -->` comment above the block that needs it.
- **A `<!-- not-runnable -->` comment,** used only for a block the browser cannot run: a challenge prompt that fellows complete in the lecture code repository, a project file that imports from `src/` or imports `pytest`, a syntax template, or a REPL transcript.

Two kinds of failing block are left alone:

- A block whose error is the one the lesson teaches.
- A block that calls `input()`. The checking script gives blocks no keyboard input, so it reports an `EOFError` for these blocks, but the LMS gives them a terminal that accepts typing.

The LMS does not read the `setup`, `uses` and `not-runnable` comments yet. Until it does, the blocks that rely on them still fail in the LMS, so the fixes below take effect only once the LMS supports the comments.

## Status

Lesson 2.6 is complete. Its four setups and its not-runnable challenge prompt are the model for the other lessons. The bare-expression blocks in 1.2, the full class in 2.1's "A Method That Takes Arguments", and the three one-line blocks in 2.3's "The Underscore Is a Convention" are also done.

`python3.14 scripts/check-code-blocks.py` reports 191 failing blocks across Modules 1 and 2. They divide as follows:

| Kind | Blocks |
| --- | --- |
| Needs a hidden setup | 79 |
| Needs `<!-- not-runnable -->` | 39 |
| Output fenced as code (accuracy problem 2) | 1 |
| Intended error, left alone | 41 |
| Calls `input()`, left alone | 31 |

Lessons 2.1 to 2.5 hold 50 of the 79 setups, because the `Event` class grows in each section and most of their blocks build on it. 1.11 holds another 16, all of which need the same 8-line `purchases` list.

## Settled decisions

### Blocks of bare expressions

**The problem:** a block of bare expressions with each result written in a comment, such as `5 == 5  # True`, shows an empty terminal when run, because a script throws away the value of a bare expression. A fellow who expected to see `True` gets no feedback, and the checking script cannot detect this, because the block runs without error.

**The rule:** each expression in such a block is wrapped in `print()`, and each comment shows exactly what `print()` displays. `print()` shows a string without its quotes, so the comment reads `print("hi" * 3)  # hihihi`. When an intended error sits in the middle of a block, it moves to the last line of its group, or the block splits, so that every other line prints before the error stops the run. 1.2 follows this rule.

The one exception is 1.1's block at line 94 (`5 + 5       # Evaluates to 10`), which stays bare. The paragraph after it says that Python evaluates a bare expression and then throws the value away, and running the block and seeing nothing shows exactly that.

### Refusal messages in assignment 2-4

Lesson 2.7, the case study repository `swe-casestudy-2-venue-tickets` and the 2.7 lecture code print a refused call as `Reservation must be <status> in order to use <method>.`, such as `Reservation must be paid in order to use check_in.` Assignment 2-4's guards use the same wording when that assignment is rewritten. The copy of the case study in `F26_SWE_PYTHON_LECTURE_CODE/mod-2/` keeps its old message, because it already differs from the repository in four files.

## Accuracy problems found, not yet fixed

1. **Lesson 1.1, Logical Errors** (`1-intro-to-programming.md`, the `age = input(...)` block at line 404). `input()` returns a string, so `age < 21` raises `TypeError: '<' not supported between instances of 'str' and 'int'`. The prose presents the block as code that runs and gives a wrong answer. In the LMS, a fellow who runs the block and types an age sees the `TypeError`. Writing `age = int(input(...))` keeps it a logical error.
2. **Lesson 1.3, the `print_B` prediction answer** (`3-functions.md`, line 211). The block holding `A C B B` is program output fenced as `py`, so the LMS gives it a Run button, and running it raises `NameError: name 'A' is not defined`. Fence it with no language.
3. **Chapter numbers in prose**, which break the rule against citing chapters by number. Counting each "chapter" followed by a number, case ignored: 1.1 has 1, 1.2 has 6, 1.3 has 4, 1.4 has 1, 1.5 has 6, 1.6 has 5, 1.7 has 4, 1.8 has 5, 1.9 has 2, 1.10 has 8, 1.12 has 8, and the Module 1 case study has 5. Find them with `grep -ni "chapter [0-9]\.[0-9]" mod-1-python-fundamentals/*.md`.
4. **Two typos in 1.11:**
   - "the expression `test` expression is true", at line 305;
   - "Calculate the total the price of every purchase", in the table at line 74.

## Work remaining, by lesson

Line numbers are the line of the opening ` ```python ` fence as of the commit that last changed this document. Each setup added to a file shifts every line below it, so work from the bottom of a file upward, or match each block by its first line.

Under **Leave alone**, each lesson lists its intended errors and its `input()` blocks, so that the checking script's output can be matched against them.

### 1.1 Intro to Programming

No block needs a fix. Line 94 stays bare, as the bare-expressions rule says, and line 404 is accuracy problem 1.

**Leave alone:** intended errors at 301, 378, 420, 433, 442, 451 and 462; `input()` at 404.

### 1.2 Data Types, Variables, and Operators

| Line | First line | Fix |
| --- | --- | --- |
| 195 | `print("Story time!")` | Setup: the variables assigned in step 1 of Assign, Reassign, Reference |
| 208 | `print("Story time!")` | Setup: the variables after steps 1 and 2 |
| 392 | `# Python3 REPL` | Not runnable: a REPL transcript with `>>>` prompts |
| 404 | `# Python3 REPL` | Not runnable: a REPL transcript with `>>>` prompts |

**Leave alone:** intended `TypeError` at the end of the blocks at 431, 497, 567 and 693.

### 1.3 Functions

| Line | First line | Fix |
| --- | --- | --- |
| 211 | `A` | Fence with no language (accuracy problem 2) |
| 304 | `say_hello('Ben', 'code')` | Not runnable: challenge prompt |
| 351 | `print(add(12, add(5, 3)))` | Setup: `add()` |
| 583 | `print(message, my_name)` | Setup: the code above it, since the prompt adds this line to the bottom of that code |

**Leave alone:** intended errors at 269, 313 (the final `say_hello()` call), 422, 476, 528, 635 and 684.

### 1.4 Conditional Statements

**Leave alone:** `input()` at 207 and 217.

### 1.5 Inputs and Outputs

| Line | First line | Fix |
| --- | --- | --- |
| 326 | `def is_marcy_email(email):` | Not runnable: a question with a blank for fellows to fill |
| 490 | `def starts_and_ends_with_a(text):` | Not runnable: a question with a blank for fellows to fill |

**Leave alone:** intended errors at 227 and 251; `input()` at 96, 160, 203, 241, 297, 378, 457, 476, 577 and 779.

### 1.6 Loops

**Leave alone:** `input()` at 44, 143, 324, 358, 377, 401 and 449.

### 1.7 Lists

| Line | First line | Fix |
| --- | --- | --- |
| 192 | `prices.clear()` | Setup: `prices` |

**Leave alone:** intended errors at 176 and 593; `input()` at 47 and 70.

### 1.8 Dictionaries

| Line | First line | Fix |
| --- | --- | --- |
| 400 | `receipt["purchases"].append(...)` | Setup: `receipt`. A hidden setup keeps the solution true to its prompt, which says to update the receipt without retyping any existing record. |
| 458 | `item = "bagel"` | Setup: `menu` |
| 541 | `for purchase in purchases:` | Setup: `purchases` |
| 569 | `total = 0` | Setup: `menu` |
| 579 | `for item, price in menu.items():` | Setup: `menu` |

**Leave alone:** intended errors at 144 and 339; `input()` at 259, 467 and 508.

### 1.9 Modules, Environments, and pytest

| Line | First line | Fix |
| --- | --- | --- |
| 235 | `from orders import is_on_menu` | Not runnable: project file |
| 282 | `# Import the whole module…` | Not runnable: project file |
| 319 | `import orders as o` | Not runnable: project file |
| 400 | `import orders` | Not runnable: project file |
| 503 | `from madlib import madlib` | Not runnable: project file |

**Leave alone:** `input()` at 63, 115 and 452.

### 1.10 Test-Driven Development

| Line | First line | Fix |
| --- | --- | --- |
| 107 | `# test_calc.py` | Not runnable: project file |
| 242 | `import pytest` | Not runnable: test file |
| 279 | `nums = [1, 2, 3, 4]` | Setup: `double_all_purely()` |
| 301 | `from double_all import double_all_purely` | Not runnable: project file |
| 478 | `import pytest` | Not runnable: test file |
| 543 | `import pytest` | Not runnable: test file |

### 1.11 Comprehensions and Common List Operations

Every setup in this lesson is the 8-line `purchases` list, so one setup on the page serves all 16 blocks.

| Line | First line | Fix |
| --- | --- | --- |
| 118 | `for purchase in purchases:` | Setup: `purchases` (challenge solution) |
| 152 | `customer_names = [purchase["customer"] …` | Setup: `purchases` |
| 162 | `[expression for item in source_list]` | Not runnable: syntax template |
| 172 | `def format_line(purchase):` | Setup: `purchases`. This block is the titled file `03_transform.py`, and the titled file `04_filter.py` shows the list visibly, so a visible copy would make the two files match. |
| 191 | `# Imperative: High Control & High Effort:` | Setup: `purchases` |
| 255 | `purchases = [` | Not runnable: challenge prompt with `???` |
| 275 | `payment_methods = […]` | Setup: `purchases` (challenge solution) |
| 307 | `[expression for item in source_list if test]` | Not runnable: syntax template |
| 338 | `cash_items = ???` | Not runnable: challenge prompt |
| 346 | `cash_items = […]` | Setup: `purchases` (challenge solution) |
| 374 | `print(len(purchases))  # 5` | Setup: `purchases`. The block then reaches its intended `TypeError`. |
| 383 | `prices = [purchase["price"] …]` | Setup: `purchases` |
| 396 | `def total(purchases):` | Setup: `purchases` |
| 414 | `def get_customer_names(purchases):` | Setup: `purchases` |
| 500 | `payment_counts = {}` | Setup: `purchases` (challenge solution) |
| 548 | `print(find_purchase_index(purchases, "coffee"))` | Setup: `purchases` and `find_purchase_index()` |
| 563 | `def first_item_paid_by(purchases, payment):` | Not runnable: challenge prompt |
| 639 | `cash_prices = ???` | Not runnable: challenge prompt |
| 647 | `cash_prices = sorted([…])` | Setup: `purchases` (challenge solution) |
| 659 | `prices = [purchase["price"] …]` | Setup: `purchases` |
| 670 | `print(sorted([…], …))` | Setup: `purchases` |
| 679 | `coffee_total = ???` | Not runnable: challenge prompt |
| 687 | `coffee_prices = […]` | Setup: `purchases` (challenge solution) |

### 1.12 Reading Unfamiliar Code

| Line | First line | Fix |
| --- | --- | --- |
| 125 | `from inventory import restock, sell, report` | Not runnable: project file |
| 226 | `sell("eggs", 1)` | Setup: the data and functions from `inventory.py` |

**Leave alone:** `input()` at 284 and 340.

### 2.1 Intro to OOP, Classes, `__init__`, and `self`

| Line | First line | Fix |
| --- | --- | --- |
| 53 | `jazz = Event(...)` | Setup: `Event` (Key Terms example) |
| 270 | `jazz.name = 'Friday Night Jazz'` | Setup. The block then reaches its intended `AttributeError`. |
| 449 | `jazz = Event(...)` | Setup: `Event` |
| 491 | `jazz = Event(...)` | Setup: `Event` (predict box) |
| 562 | `studio = Room(...)` | Not runnable: challenge prompt |
| 654 | `pottery['seats_sold'] += 1` | Setup: the `pottery` dictionary |
| 665 | `# The dictionary version…` | Setup: `make_event()` and the class |
| 677 | `print(dir(pottery))` | Setup: the class version of `pottery` |

**Leave alone:** intended errors at 154, 179, 369, 465 and 744; `input()` at 140.

### 2.2 Composition, `__repr__`, `__eq__`, and `@dataclass`

| Line | First line | Fix |
| --- | --- | --- |
| 86 | `print(hall.events[0].name)` | Setup: `hall` |
| 104 | `jazz.capacity = 60` | Setup (predict box) |
| 175 | `hall.add_event(Event('New Year Concert', …))` | Not runnable: challenge prompt |
| 227 | `print(hall.events_on(...))` | Setup: `hall` |
| 248 | `class Event:` | Setup: `Venue` and `hall` |
| 276 | `def __repr__(self):` | Setup: `hall`, built from an `Event` whose `__repr__` prints instead of returning. The visible block shows that method on its own, so the setup has to supply the class that holds it for the block to reach its intended `TypeError`. |
| 291 | `blue_notes = Performer(...)` | Not runnable: challenge prompt |
| 349 | `class Venue:` | Setup: `Event` |
| 373 | `jazz = Event(...)` | Setup: `Event` with `__eq__` |
| 409 | `hall = Venue(...)` | Setup: `Event` and `Venue` |
| 422 | `hall.add_event(...)` | Setup (predict box) |
| 452 | `print(Performer(...) == Performer(...))` | Not runnable: challenge prompt |
| 582 | `board_games = Event(...)` | Setup: the case study's `Event`, which takes `base_price`. The lesson never shows that class, so copy it from the case study repository's `src/`. |
| 630 | `hall = Venue(...)` | Setup (predict box) |
| 668 | `hall = Venue(...)` | Not runnable: challenge prompt |
| 767 | `# tests/test_venue.py` | Not runnable: test file |
| 860 | `print(jazz == 'Friday Night Jazz')` | Setup: `jazz` |
| 880 | `tickets_sold = {jazz: 3}` | Setup: `jazz` |

### 2.3 Properties: Non-Public Attributes and `@property`

| Line | First line | Fix |
| --- | --- | --- |
| 34 | `@capacity.setter` | Not runnable: a setter shown on its own in Key Terms |
| 75 | `pottery = Event(...)` | Setup: `Event` |
| 89 | `pottery.seats_sold += 1` | Setup: `pottery` |
| 98 | `pottery = Event(...)` | Setup: `Event` |
| 169 | `pottery = Event(...)` | Setup: `Event` with the `seats_sold` property |
| 183 | `pottery = Event(...)` | Setup (predict box) |
| 232 | `pottery = Event(...)` | Setup: the class at line 208 with its `# ...` placeholder filled in from the class before it |
| 251 | `pottery = Event(...)` | Setup (predict box) |
| 271 | `pottery = Event(...)` | Not runnable: challenge prompt |
| 377 | `pottery = Event(...)` | Setup |
| 516 | `from datetime import date` | Not runnable: test file |
| 546 | `@capacity.setter` | Not runnable: a setter for fellows to paste into `src/event.py` |

**Leave alone:** intended errors at 472 (Line 3 of the check for understanding) and 651.

### 2.4 Inheritance and Attribute Lookup

| Line | First line | Fix |
| --- | --- | --- |
| 181 | `coco = Screening(...)` | Setup: `Event` and `Screening` (predict box) |
| 243 | `class Concert(Event):` | Setup: `Event` |
| 265 | `jazz = Concert(...)` | Setup (predict box) |
| 290 | `class Screening(Event):` | Setup: `Event` |
| 311 | `class Screening(Event):` | Setup: `Event`. The block then runs without output, which suits a check about a misspelled method name. |
| 338 | `class Concert(Event):` | Setup: `Event` |
| 366 | `pottery = Workshop(...)` | Not runnable: challenge prompt |
| 376 | `class Workshop(Event):` | Setup: `Event` (challenge solution) |
| 416 | `class Concert(Event):` | Setup: `Event`. The `# ... can_refund() from above ...` placeholder leaves out a method that the block never calls, so the block runs correctly. |
| 445 | `jazz = Concert(...)` | Setup (predict box) |
| 479 | `jazz = Concert(...)` | Setup. The block then reaches its intended `AttributeError`. |
| 573 | `class Concert(Event):          # a concert is an event` | Setup: `Event` |
| 650 | `from datetime import date` | Not runnable: test file |
| 736 | `class Concert(Event):` | Setup: `Event`. The block then reaches its intended `AttributeError`. |
| 755 | `jazz = Concert(...)` | Setup |
| 772 | `jazz = Concert(...)` | Setup |
| 795 | `print(Concert.__mro__)` | Setup |

**Leave alone:** intended errors at 519 and 811.

### 2.5 Polymorphism, Duck Typing, and Abstract Base Classes

| Line | First line | Fix |
| --- | --- | --- |
| 117 | `class Tour(Event):` | Setup (hidden question) |
| 237 | `class Event:` | Setup (predict box) |
| 484 | `class MuseumTour:` | Setup |
| 533 | `class GardenTour:` | Setup (predict box) |
| 612 | `class MidnightConcert(Event):` | Setup |
| 742 | `class Screening(Event):` | Setup (predict box) |
| 783 | `gallery = MuseumTour(...)` | Setup |
| 839 | `from datetime import date` | Not runnable: test file |

**Leave alone:** intended errors at 626 and 933.

### 2.6 Functions as Values

Complete. **Leave alone:** intended errors at 407, 437, 544, 626 and 862.

### 2.7 Decorators

| Line | First line | Fix |
| --- | --- | --- |
| 136 | `announced_greet = announce(greet)` | Setup: `announce()` and `greet()` (predict box) |
| 357 | `sam = Reservation(1002, 'Sam Lee')` | Not runnable: challenge prompt |
| 430 | `from reservation import Reservation` | Not runnable: test file |
| 485 | `from datetime import date` | Not runnable: test file |

**Leave alone:** intended error at 575.

## Not yet scanned

The scan covers the numbered lessons in Modules 1 and 2 and the regex reading. It leaves out the Module 1 cheat sheet, case study page and project page, and every page in other modules. The LMS also runs HTML and JavaScript blocks, which the checking script does not check.

## How to check the work

Run the checking script with Python 3.14, the version fellows install:

```sh
python3.14 scripts/check-code-blocks.py mod-1-python-fundamentals/[0-9]*.md mod-1-python-fundamentals/regex.md mod-2-oop-python/[0-9]*.md
```

When this work is finished, every line the script prints should be an intended error or an `input()` block from the **Leave alone** lists above. After fixing a block, run the script on that lesson with `--show` and compare the block's output with its output comments.
