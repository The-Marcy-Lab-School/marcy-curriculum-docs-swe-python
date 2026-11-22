# Code Block Audit: Lessons 1.1 to 2.7

This document records the state of an audit of the Python code blocks in the GitBook lessons. It lists what has been fixed, what is waiting for Ben's decision, and how to check the work. It is a working document for the next session, not a page fellows read, so it is not listed in `SUMMARY.md`.

## The rule being applied

Fellows copy a single code block out of a lesson and run it. Every Python block in a lesson should run when copied alone, and print what its output comments say.

When a block uses a name that an earlier block defines, copy that definition to the top of the block and mark it with a comment on the line above:

- `# unchanged from the previous example` when the code comes from the block immediately before.
- An accurate equivalent that names the place in the same lesson when it comes from further back, such as `# unchanged from the first announce() example` or `# unchanged from A Decorator That Refuses` (a section heading). Never refer to another chapter by number.
- A bare `import` line, such as `import re` or `from datetime import date`, needs no comment.

Copy definitions exactly as the lesson writes them: the same keyword arguments, values and quotes. Use two blank lines after a top-level function or class, unless the lesson's other blocks consistently use one.

Do not make the change, and report the block to Ben instead, when either of these is true:

- **The fix would make the block hard to read quickly.** As a rough guide, this means the added lines would be longer than the code the block exists to show, or more than about 8 lines.
- **The block's point depends on leaving earlier code out.** Examples are a short "Predict, then run" box about the order lines print in, a challenge prompt that a fellow runs after writing their own solution, a solution that shows only the changed part of a class with a `# ...` placeholder, and a numbered sequence of steps that continue one example.

Leave a block alone, without reporting it, when its error is intended:

- The lesson teaches that error.
- The block is a syntax template, such as `[expression for item in source_list]`.
- The block is a file in a project that imports a local module or `pytest`.
- The block calls `input()`.

This rule is also saved in Claude's memory as `feedback_lesson_blocks_run_alone.md`.

## Status of the changes

None of the changes below is committed. Run `git diff` in this repository to see them.

| File | Change |
| --- | --- |
| `mod-2-oop-python/7-decorators.md` | Unclear uses of "it" replaced with the noun they stand for (Ben's review). `loud_greet` and `loud_shout` renamed to `announced_greet` and `announced_shout` throughout, following Ben's edit. Five blocks given the definitions they need (listed below). This file also holds Ben's own uncommitted edits. |
| `mod-2-oop-python/scope-and-sequence.md` | The 2.7 Key Terms for **wrapper** and **decorator factory** updated to match the lesson. `scripts/sync-key-terms.py` has no marker for 2.7, so these two terms are copied by hand. |
| 13 lesson files in `mod-1-python-fundamentals/` and `mod-2-oop-python/` | Definitions or imports added to 29 blocks (listed below). Every change in these files adds lines and none removes or changes one. |

### Blocks fixed in lesson 2.7

| Block | Added | Comment |
| --- | --- | --- |
| `@announce` above `greet` | `announce()` | `# unchanged from the first announce() example` |
| Challenge: Keep the Return Value, the `announced_shout` prompt | `announce()` | `# unchanged from the previous example` |
| Advanced Topics, the `seat_label` block that raises `TypeError` | the one-argument `announce()` | `# unchanged from the first announce() example` |
| `functools.wraps`, the block that prints `wrapper` | `requires_paid` and a `Reservation` holding only `check_in()` | `# unchanged from A Decorator That Refuses` and `# only check_in() is needed for this example` |
| `functools.wraps`, the block that prints `check_in` | the same one-method `Reservation` | `# unchanged from the previous example` |

### Blocks fixed in the other lessons

| Lesson | Blocks | Added |
| --- | --- | --- |
| 1.2 | 1 | `fahrenheit = 212` |
| 1.3 | 4 | `convert_C_to_F`, `print_sum`, `say_hello` with defaults, and `count = 0`. These use one blank line after each `def`, because every block in 1.3 does. |
| 1.5 | 2 | `message` and `fruits` |
| 1.6 | 2 | `import random` |
| 1.8 | 5 | `purchase_1` in four blocks, and `menu` in the lookup-table block |
| 1.10 | 1 | `withdraw()` |
| 1.11 | 2 | the `purchases` list, in the two blocks whose own code is at least 8 lines |
| Regex reading | 5 | `import re` |
| 2.1 | 1 | `from datetime import date` |
| 2.2 | 2 | `from datetime import date` and `from dataclasses import dataclass` |
| 2.4 | 1 | `from datetime import date` |
| 2.5 | 2 | `from datetime import date, timedelta` |
| 2.6 | 1 | `make_announcer()`, with `# unchanged from Closures` |

## Decisions waiting for Ben

### 1. The running examples

Most of the blocks still failing continue one running example. Copying the example's setup into each block would add more lines than the block shows:

| Running example | Lesson | Lines the setup would add | Blocks affected |
| --- | --- | --- | --- |
| `purchases` | 1.11 | 8 | 16 |
| `menu` | 1.8 | 7 | 4 |
| `Event`, which grows section by section | 2.1 to 2.5 | 16 to 55 | about 45 |
| `hall` | 2.2 and 2.6 | 25 to 30 | about 20 |

The recommendation is one sentence before the first block that builds on the example, telling fellows to run the following blocks together, for example: "The blocks in this section continue from the `hall` above; add each one to the bottom of the same file." This costs one line per section instead of 7 to 55 lines per block. Ben has not yet chosen between drafting those sentences and handling the blocks one by one.

### 2. Blocks whose intended error cannot be reached alone

These blocks are meant to raise one error, but when a fellow runs one alone it stops earlier with a `NameError`. They matter more than the other unfixed blocks, because the fellow sees a different error from the one the lesson explains.

| Lesson | Line | Intended error | Fix size |
| --- | --- | --- | --- |
| 1.11 | 374 | `TypeError` | 8 lines (`purchases`) |
| 2.1 | 270 | `AttributeError` | about 9 lines |
| 2.4 | 734 | `AttributeError` | about 20 lines (`Event`) |
| 2.6 | 339, 361, 459 | `TypeError` | about 30 lines (`hall`) |

### 3. Other open questions from the lesson 2.7 review

- **Refusal messages should state the rule.** Ben asked for each refusal message to say what the reservation needs, such as "Reservation must be reserved in order to pay" and "Reservation must be paid in order to check in". This applies to lesson 2.7 and to the case study repository `assignments-case-studies-lecture-code/mod-2/swe-casestudy-2-venue-tickets` (`src/reservation.py`, the three `capsys` assertions in `tests/test_reservation.py` and `tests/test_venue.py`, and the sample output in `README.md`). The previous messages leaving the rule out was not deliberate.
  - The open question is the method name. The decorators build the message from `method.__name__`, which is `check_in`, with an underscore. The options are to keep the underscore, to convert it with `method.__name__.replace('_', ' ')`, or to phrase the rule without repeating the name, such as "Reservation must be paid first." The recommendation is to keep the underscore, because the line that teaches `method.__name__` then gains no new syntax, and the lesson's before and after versions print the same text.
  - Leave the copy of the case study in `F26_SWE_PYTHON_LECTURE_CODE/mod-2/` alone. It already differs from the repository in four files.
  - Assignment 2-4's guards get the same rule when that assignment is rewritten.
- **The `"checked"` in typo at line 31 of 2.7.** The text should read `"checked_in"` or "checked in".
- **The blank line after `def greet` in 2.7.** Ben's edited block, the first code block under Wrapping a Function, has one blank line between `def greet` and `greet('Maya')`. PEP 8 asks for two.

## Accuracy problems found, not yet fixed

1. **Lesson 1.1, Logical Errors** (`1-intro-to-programming.md`, the `age = input(...)` block). `input()` returns a string, so `age < 21` raises `TypeError: '<' not supported between instances of 'str' and 'int'`. The prose presents the block as code that runs and gives a wrong answer. Writing `age = int(input(...))` keeps it a logical error.
2. **Lesson 1.2, Membership and Identity** (`2-data-types-variables.md`, the block starting `'a' in 'apple'`). The block uses `x`, `a` and `b`, which the lesson never defines. Its `# True` comments hold only if `x` is `None` and `a` and `b` are different objects. A fix needs about 3 new lines.
3. **Lesson 1.3, the `print_B` prediction answer.** The block holding `A C B B` is fenced as `py` but contains program output.
4. **Lesson 2.6, Challenge: Finding Attendees.** The solution redefines `Venue`, but `hall` is still an object built from the old class. A fellow who reruns the prompt without rebuilding `hall` gets `AttributeError: 'Venue' object has no attribute 'add_attendee'`.
5. **Chapter numbers in prose**, which break the rule against citing chapters by number:
   - "chapter 1.8" in 1.7;
   - "chapter 1.7", several times, in 1.8;
   - "Chapter 1.7" in 1.10;
   - "chapter 1.9", "Chapter 1.3" and "chapter 1.7" in 1.12.
6. **Two typos in 1.11:**
   - "the expression `test` expression is true", in section 3;
   - "Calculate the total the price of every purchase", in the table.

## Unfixed blocks, by lesson

Line numbers are the line of the opening ```` ```python ```` fence, as of the current uncommitted state. They shift as soon as a file is edited, so match each block by its first line as well. The numbers for 2.4 to 2.7 are already out of date, because each section's Code now comes before its New Concepts; match those blocks by their first line only.

The **Reason** column uses three codes:

- **Long:** the setup would be too long to read quickly.
- **Omits:** the block deliberately leaves the earlier code out.
- **Error:** the block's intended error cannot be reached when it runs alone (see decision 2).

### 1.2 Data Types, Variables, and Operators

| Line | First line | Reason |
| --- | --- | --- |
| 194 | `print("Story time!")` | Omits: step 2 of Assign, Reference and Reassign |
| 207 | `print("Story time!")` | Omits: step 3 of the same list |
| 726 | `'a' in 'apple'    # True` | See accuracy problem 2 |

### 1.3 Functions

| Line | First line | Reason |
| --- | --- | --- |
| 304 | `say_hello('Ben', 'code')` | Omits: challenge prompt |
| 351 | `print(add(12, add(5, 3)))` | Omits: one-line predict box; the fix is 3 lines |
| 583 | `print(message, my_name)` | Omits: a line the reader adds to the bottom of the code above |

### 1.7 Lists

| Line | First line | Reason |
| --- | --- | --- |
| 192 | `prices.clear()` | Omits: the question that follows says the list changed without `prices = ...` |

### 1.8 Dictionaries

| Line | First line | Reason |
| --- | --- | --- |
| 404 | `receipt["purchases"].append(...)` | Omits: the prompt says "without retyping any existing record" |
| 462 | `item = "bagel"` | Long: `menu`, 7 lines |
| 545 | `for purchase in purchases:` | Long: `purchases`, 7 lines |
| 573 | `total = 0` | Long: `menu`, 7 lines |
| 583 | `for item, price in menu.items():` | Long: `menu`, 7 lines |

### 1.10 Test-Driven Development

| Line | First line | Reason |
| --- | --- | --- |
| 279 | `nums = [1, 2, 3, 4]` | Long: 8 lines; the function sits directly above the question |

### 1.11 Comprehensions and Common List Operations

Every fix in this lesson would add the 8-line `purchases` list.

| Line | First line | Reason |
| --- | --- | --- |
| 118 | `for purchase in purchases:` | Omits: challenge solution |
| 152 | `customer_names = [purchase["customer"] ...` | Long |
| 172 | `def format_line(purchase):` | Long. This block is the titled file `03_transform.py`, and the titled file `04_filter.py` does include the list, so the two files may be worth matching. |
| 191 | `customer_names = []` | Long |
| 275 | `payment_methods = [...]` | Omits: challenge solution |
| 346 | `cash_items = [...]` | Omits: challenge solution |
| 374 | `print(len(purchases))  # 5` | Error: intended `TypeError` |
| 383 | `prices = [purchase["price"] ...]` | Long |
| 396 | `def total(purchases):` | Long |
| 414 | `def get_customer_names(purchases):` | Long |
| 501 | `payment_counts = {}` | Omits: challenge solution |
| 550 | `print(find_purchase_index(purchases, "coffee"))` | Omits: predict box; the fix is about 15 lines |
| 565 | `def first_item_paid_by(purchases, payment):` | Omits: challenge prompt |
| 649 | `cash_prices = sorted([...])` | Omits: challenge solution |
| 661 | `prices = [...]  # tr...` | Long |
| 672 | `print(sorted([...], ...))` | Long |
| 689 | `coffee_prices = [...]` | Omits: challenge solution |

### 2.1 Intro to OOP, Classes, `__init__`, and `self`

| Line | First line | Reason |
| --- | --- | --- |
| 53 | `jazz = Event(...)` | Long: Key Terms example, about 8 lines |
| 270 | `jazz.name = 'Friday Night Jazz'` | Error: intended `AttributeError`; about 9 lines |
| 449 | `jazz = Event(...)` | Long: about 16 lines |
| 491 | `jazz = Event(...)` | Omits: predict box that tells fellows to use the class above |
| 520 | `class Event:` | Omits: `# __init__, seats_left, and sell_ticket as above` placeholder |
| 546 | `studio = Room(...)` | Omits: challenge prompt |
| 638 | `pottery['seats_sold'] += 1` | Long: about 10 lines |
| 649 | `pottery = make_event(...)` | Long: more than 20 lines |
| 661 | `print(dir(pottery))` | Long: more than 20 lines |

### 2.2 Composition, `__repr__`, `__eq__`, and `@dataclass`

| Line | First line | Reason |
| --- | --- | --- |
| 86 | `print(hall.events[0].name)` | Long: `hall`, about 25 lines |
| 104 | `jazz.capacity = 60` | Omits: predict box |
| 175 | `hall.add_event(...)` | Omits: challenge prompt |
| 227 | `print(hall.events_on(...))` | Long: about 30 lines |
| 248 | `class Event:` | Long: about 11 lines; the closest case to the limit |
| 276 | `def __repr__(self):` | Omits: one method shown alone |
| 291 | `blue_notes = Performer(...)` | Omits: challenge prompt |
| 349 | `class Venue:` | Long: about 11 lines |
| 373 | `jazz = Event(...)` | Long: about 8 lines, longer than the block |
| 409 | `hall = Venue(...)` | Long: about 20 lines |
| 422 | `hall.add_event(...)` | Omits: predict box |
| 452 | `print(Performer(...) == Performer(...))` | Omits: challenge prompt |
| 582 | `board_games = Event(...)` | Uses the case study's `Event`, which takes `base_price`; the lesson never defines that class, so there is nothing to copy |
| 611 | `from dataclasses import dataclass` | Long: about 12 lines on Python 3.12. On Python 3.14 the block already runs alone, because 3.14 no longer evaluates annotations when a class is defined. |
| 630 | `hall = Venue(...)` | Omits: predict box; more than 30 lines |
| 668 | `hall = Venue(...)` | Omits: challenge prompt |
| 860 | `print(jazz == 'Friday Night Jazz')` | Long: about 13 lines |
| 880 | `tickets_sold = {jazz: 3}` | Long: about 13 lines |

### 2.3 Properties: Non-Public Attributes and `@property`

Every block here needs a 19-to-30-line `Event` with properties.

| Line | First line | Reason |
| --- | --- | --- |
| 34 | `@capacity.setter` | Omits: Key Terms example showing a setter alone |
| 75 | `pottery = Event(...)` | Long |
| 89 | `pottery.seats_sold += 1` | Long |
| 98 | `pottery = Event(...)` | Long |
| 169 | `pottery = Event(...)` | Long |
| 183 | `pottery = Event(...)` | Omits: predict box |
| 232 | `pottery = Event(...)` | Long: the class above has a `# ...` placeholder, so the fix would merge two classes |
| 251 | `pottery = Event(...)` | Omits: predict box |
| 271 | `pottery = Event(...)` | Omits: challenge prompt |
| 377 | `pottery = Event(...)` | Long |
| 419 | `venue.attendees.append(sam)` | Omits: a question to reason about, not run |
| 495 | `@capacity.setter` | Omits: a setter for fellows to paste into `src/event.py` |

### 2.4 Inheritance and Attribute Lookup

Most of these blocks need the 18-line `Event`, plus `Concert` or `Screening`.

| Line | First line | Reason |
| --- | --- | --- |
| 178 | `coco = Screening(...)` | Omits: predict box |
| 246 | `class Concert(Event):` | Long |
| 261 | `jazz = Concert(...)` | Omits: predict box |
| 291 | `class Screening(Event):` | Long |
| 307 | `class Screening(Event):` | Omits: a check whose point is a misspelled method name; it calls nothing |
| 340 | `class Concert(Event):` | Long |
| 362 | `pottery = Workshop(...)` | Omits: challenge prompt |
| 372 | `class Workshop(Event):` | Long: challenge solution |
| 419 | `class Concert(Event):` | Omits: `# ... can_refund() from above ...` placeholder |
| 440 | `jazz = Concert(...)` | Omits: predict box |
| 484 | `jazz = Concert(...)` | Long: about 30 lines; its final `AttributeError` is intended |
| 573 | `class Concert(Event):          # a concert is an event` | Long: a sketch with a `...` body |
| 734 | `class Concert(Event):` | Error: intended `AttributeError` |
| 748 | `jazz = Concert(...)` | Long |
| 771 | `jazz = Concert(...)` | Long |
| 791 | `print(Concert.__mro__)` | Long |

### 2.5 Polymorphism, Duck Typing, and Abstract Base Classes

| Line | First line | Reason |
| --- | --- | --- |
| 117 | `class Tour(Event):` | Omits: hidden question; about 45 lines |
| 236 | `class Event:` | Omits: predict box; about 45 lines |
| 493 | `class MuseumTour:` | Long: about 45 lines |
| 532 | `class GardenTour:` | Omits: predict box; about 55 lines |
| 622 | `class MidnightConcert(Event):` | Long: about 17 lines |
| 741 | `class Screening(Event):` | Omits: predict box |
| 788 | `gallery = MuseumTour(...)` | Long: about 35 lines |

### 2.6 Functions as Values: Callbacks, Higher-Order Functions, and Closures

Most of these blocks need `hall`, which is `Event`, `Venue` and five setup lines, about 30 lines in all.

| Line | First line | Reason |
| --- | --- | --- |
| 108 | `def is_free(event):` | Long |
| 190 | `class Venue:` | Long: about 15 lines |
| 224 | `def is_cheap(event):` | Long |
| 273 | `from dataclasses import dataclass` | Omits: challenge prompt |
| 339 | `print(hall.find_events(is_free))` | Error: intended `TypeError` |
| 361 | `board_games = hall.events[3]` | Error: intended `TypeError` |
| 394 | `print(hall.find_events(lambda ...))` | Long |
| 410 | `print(hall.find_events(lambda ...))` | Long |
| 438 | `def event_date(event):` | Long |
| 459 | `print(sorted(hall.events))` | Error: intended `TypeError` |
| 492 | `latest_first = sorted(...)` | Long |
| 522 | `def matches_month(month):` | Long |
| 689 | `cheap = list(filter(...))` | Long |
| 709 | `hall.add_event(Event('Holiday Crafts', ...))` | Long |
| 728 | `def list_events(venue):` | Long: needs the five-event `hall`, which includes Holiday Crafts |

### 2.7 Decorators

| Block | Reason |
| --- | --- |
| The predict box `announced_greet = announce(greet)` / `print('ready')` | Omits: a three-line box about the order lines print in |
| The `@requires_reserved` challenge prompt, `sam.pay()` twice | Omits: challenge prompt |
| The `@requires_reserved` solution and the decorator factory block | Omits: `# ... from above ...` placeholders |
| The two test blocks in Testing a Status Guard | Project files that import from `src/`; expected |

## Not yet scanned

The cheat sheet, the case study page and the project page in `mod-1-python-fundamentals/` were left out of the scan, along with any page outside Modules 1 and 2. Ben has not said whether they should be included.

## How to check the work

The environment setup instructions have fellows install Python 3.14, which is at `/opt/homebrew/bin/python3.14` on this machine. The scan behind this document ran on Python 3.12, which explains the line 611 difference in 2.2. Run future scans with 3.14.

The script below extracts every ```` ```python ```` and ```` ```py ```` block from the lessons, runs each block alone in an empty folder, and prints each block that fails, with its last error line. Save it in the session's scratchpad, not in this repository, and run it from there.

```python
import os, re, subprocess

ROOT = '/Users/benspector/Documents/curriculum-development/marcy-curriculum-docs-swe-python'
PYTHON = '/opt/homebrew/bin/python3.14'
LESSONS = (
    [f'mod-1-python-fundamentals/{f}' for f in os.listdir(f'{ROOT}/mod-1-python-fundamentals') if re.match(r'\d+-.*\.md$', f) or f == 'regex.md']
    + [f'mod-2-oop-python/{f}' for f in os.listdir(f'{ROOT}/mod-2-oop-python') if re.match(r'\d+-.*\.md$', f)]
)

for rel in sorted(LESSONS):
    lines = open(f'{ROOT}/{rel}').read().split('\n')
    i = 0
    while i < len(lines):
        fence = re.match(r'^(\s*)```(python|py)\s*$', lines[i])
        if fence:
            indent = len(fence.group(1))
            j = i + 1
            while not re.match(r'^\s*```\s*$', lines[j]):
                j += 1
            folder = f'run/{rel.replace("/", "_")}-{i + 1}'
            os.makedirs(folder, exist_ok=True)
            open(f'{folder}/b.py', 'w').write('\n'.join(line[indent:] for line in lines[i + 1:j]))
            try:
                result = subprocess.run([PYTHON, '-I', 'b.py'], cwd=folder, capture_output=True, text=True, timeout=5, stdin=subprocess.DEVNULL)
                if result.returncode:
                    print(f'{rel}:{i + 1}  {result.stderr.strip().splitlines()[-1]}')
            except subprocess.TimeoutExpired:
                print(f'{rel}:{i + 1}  TIMEOUT')
            i = j
        i += 1
```

Each failure the script prints falls into one of four groups:

- an intended error;
- `EOFError` from a block that calls `input()`;
- a project file whose import fails;
- one of the unfixed blocks listed above.

After any fix, the block must print exactly what its output comments say, and the full list of failures should shrink by that block only.
