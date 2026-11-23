# Code Block Audit: Lessons 1.1 to 2.7

This document tracks the work of making every runnable code block in the Module 1 and Module 2 lessons run in the LMS. It records which blocks are expected to fail, the questions still open, and how to check the work. It is a working document for the next session, not a page fellows read, so it is not listed in `SUMMARY.md`.

## The rule being applied

The LMS runs each Python block in a fresh interpreter, so a block can use only the names it defines itself. Every runnable block must run on its own and print exactly what its output comments say. [authoring-guide.md](authoring-guide.md) gives the full syntax. A block that depends on earlier code gets one of three fixes:

- **A visible copy** of a short definition, about 8 lines or fewer, under a comment such as `# unchanged from the previous example`. The visible copies already in the lessons stay visible.
- **A hidden setup:** a `<!-- setup: name … -->` comment placed directly after the visible block it copies, and a `<!-- uses: name -->` comment above the block that needs it.
- **A `<!-- not-runnable -->` comment,** used only for a block the browser cannot run: a challenge prompt that fellows complete in the lecture code repository, a project file that imports from `src/` or imports `pytest`, a syntax template, or a REPL transcript.

Two kinds of failing block are left alone:

- A block whose error is the one the lesson teaches.
- A block that calls `input()`. The checking script gives blocks no keyboard input, so it reports an `EOFError` for these blocks, but the LMS gives them a terminal that accepts typing.

## Status

Every numbered lesson in Modules 1 and 2, and the regex reading, has its setups and `not-runnable` comments. Every block that the checking script runs either prints what its output comments say or raises the error that its lesson teaches.

## Expected failures

`python3.14 scripts/check-code-blocks.py` prints 86 lines for these lessons. 55 are errors that the lessons teach, and 31 are `input()` blocks, which fail in the script only because the script gives them no keyboard input. The line numbers are the opening fence of each block, as of the commit that last changed this document.

| File | Intended errors | `input()` blocks |
| --- | --- | --- |
| `mod-1-python-fundamentals/1-intro-to-programming.md` | 301, 378, 420, 433, 442, 451, 462 | 404 |
| `mod-1-python-fundamentals/11-comprehensions-builtin-iteration.md` | 394 | — |
| `mod-1-python-fundamentals/12-reading-unfamiliar-code.md` | — | 314, 370 |
| `mod-1-python-fundamentals/2-data-types-variables.md` | 446, 512, 582, 708 | — |
| `mod-1-python-fundamentals/3-functions.md` | 269, 314, 432, 486, 538, 624, 676, 725 | — |
| `mod-1-python-fundamentals/4-conditional-statements.md` | — | 207, 217 |
| `mod-1-python-fundamentals/5-inputs-outputs.md` | 227, 251 | 96, 160, 203, 241, 297, 379, 458, 477, 579, 781 |
| `mod-1-python-fundamentals/6-loops.md` | — | 44, 143, 324, 358, 377, 401, 449 |
| `mod-1-python-fundamentals/7-lists.md` | 176, 599 | 47, 70 |
| `mod-1-python-fundamentals/8-dictionaries.md` | 144, 351 | 259, 500, 541 |
| `mod-1-python-fundamentals/9-modules-environments-pytest.md` | — | 63, 115, 456 |
| `mod-2-oop-python/1-intro-to-oop-classes-init-self.md` | 169, 194, 297, 396, 519, 854 | 155 |
| `mod-2-oop-python/2-instances-repr-eq-dataclass.md` | 352, 1066, 1087 | — |
| `mod-2-oop-python/3-properties-non-public-attributes.md` | 239, 323, 343, 567, 748 | — |
| `mod-2-oop-python/4-inheritance-attribute-lookup.md` | 557, 597, 828, 906 | — |
| `mod-2-oop-python/5-polymorphism-duck-typing-abc.md` | 677, 771, 935, 977, 1128 | — |
| `mod-2-oop-python/6-functions-as-values-hof.md` | 407, 437, 544, 626, 862 | — |
| `mod-2-oop-python/7-decorators.md` | 592 | — |

## Setups that copy code the page does not show

Eight setups name their source in a `# copies:` line, because they do not copy the block directly above them, so the checking script does not compare them with that block. Three of them hold code that the page never shows, because the visible block depends on it:

- 2.2's `case-study-classes` copies the case study's `Event` from `src/events.py` and the `Attendee` dataclass.
- 2.3's `venue-attendees` adds `is_valid_email()`, which the visible `Venue` leaves out behind its `...`, and the `Attendee` dataclass.
- 2.4's `attendee` holds the `Attendee` dataclass, which 2.4 uses but never defines.

1.3's `scope-example` setup keeps its top-level calls to `greet()` and `greet_friend()`, because its predict box asks fellows to add a line to the bottom of the code above, and the answer says the greetings print first. `authoring-guide.md` allows this one kind of printing setup.

Five setups leave out a call that prints a refusal, because the refused call changes nothing: 2.1's `event-methods` and `dictionary-event`, 2.2's `refusing-venue` and `one-jazz`, and 2.3's `sold-out-pottery`.

## Settled decisions

### Blocks of bare expressions

**The problem:** a block of bare expressions with each result written in a comment, such as `5 == 5  # True`, shows an empty terminal when run, because a script throws away the value of a bare expression. A fellow who expected to see `True` gets no feedback, and the checking script cannot detect this, because the block runs without error.

**The rule:** each expression in such a block is wrapped in `print()`, and each comment shows exactly what `print()` displays. `print()` shows a string without its quotes, so the comment reads `print("hi" * 3)  # hihihi`. When an intended error sits in the middle of a block, it moves to the last line of its group, or the block splits, so that every other line prints before the error stops the run. 1.2 follows this rule.

The one exception is 1.1's block at line 94 (`5 + 5       # Evaluates to 10`), which stays bare. The paragraph after it says that Python evaluates a bare expression and then throws the value away, and running the block and seeing nothing shows exactly that.

### Refusal messages in assignment 2-4

Lesson 2.7, the case study repository `swe-casestudy-2-venue-tickets` and the 2.7 lecture code print a refused call as `Reservation must be <status> in order to use <method>.`, such as `Reservation must be paid in order to use check_in.` Assignment 2-4's guards use the same wording when that assignment is rewritten. The copy of the case study in `F26_SWE_PYTHON_LECTURE_CODE/mod-2/` keeps its old message, because it already differs from the repository in four files.

## Accuracy problems found, not yet fixed

1. **Lesson 1.1, Logical Errors** (`1-intro-to-programming.md`, the `age = input(...)` block at line 405). `input()` returns a string, so `age < 21` raises `TypeError: '<' not supported between instances of 'str' and 'int'`. The prose presents the block as code that runs and gives a wrong answer. In the LMS, a fellow who runs the block and types an age sees the `TypeError`. Writing `age = int(input(...))` keeps it a logical error.
2. **Chapter numbers in prose**, which break the rule against citing chapters by number. Counting each "chapter" followed by a number, case ignored: 1.1 has 1, 1.2 has 6, 1.3 has 4, 1.4 has 1, 1.5 has 6, 1.6 has 5, 1.7 has 4, 1.8 has 5, 1.9 has 2, 1.10 has 8, 1.12 has 8, and the Module 1 case study has 5. Find them with `grep -ni "chapter [0-9]\.[0-9]" mod-1-python-fundamentals/*.md`.
3. **Two typos in 1.11:**
   - "the expression `test` expression is true", at line 321;
   - "Calculate the total the price of every purchase", in the table at line 74.
4. **Lesson 2.4, the `seats.label` block** (`4-inheritance-attribute-lookup.md`, line 602). The comment reads `AttributeError: 'list' object has no attribute 'label'`, but Python 3.14 adds `and no __dict__ for setting new attributes` to that message, so the comment no longer matches the output exactly.
5. **Lesson 1.11, the `adas_purchases` block in section 3.** The comment spreads the printed list over several indented lines, but `print()` shows it on one line. The values match.

## Not yet scanned

The scan covers the numbered lessons in Modules 1 and 2 and the regex reading. It leaves out the Module 1 cheat sheet, case study page and project page, and every page in other modules. The LMS also runs HTML and JavaScript blocks, which the checking script does not check.

## How to check the work

Run the checking script with Python 3.14, the version fellows install:

```sh
python3.14 scripts/check-code-blocks.py mod-1-python-fundamentals/[0-9]*.md mod-1-python-fundamentals/regex.md mod-2-oop-python/[0-9]*.md
```

Every line the script prints should be in the table under Expected failures. A line that is not in the table is a new failure. A line ending `differs from the block above it` means a visible block was edited and its hidden copy was not. After fixing a block, run the script on that lesson with `--show` and compare the block's output with its output comments.
