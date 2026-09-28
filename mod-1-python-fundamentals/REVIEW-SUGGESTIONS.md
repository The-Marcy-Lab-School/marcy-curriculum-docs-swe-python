# Mod 1 Review: Keep, Cut, Add

**Status:** every item below was implemented on 2026-09-24, with these choices where the review offered two: the debugger lives in lesson 3; `print(sep=, end=)` stays in lesson 1; the REPL moved to lesson 2 beside the weird-expressions challenge; `__pycache__` is a callout in lesson 6 and a `.gitignore` line in lesson 7; tuples are in lesson 8; `json` and `open()` are in lesson 7's standard library section; the lesson 12 animations are an optional collapsed block; the banking challenge in lesson 14 is a pointer to the assignment. `type()` stays out of lesson 2 at Ben's direction. Kept for reference.

Suggestions for Ben to evaluate, chapter by chapter. The standard applied: does a junior programmer in 2026 need this, is it introduced before it is used, and does each lesson fit one 90-minute session. Nothing here has been changed in the chapters except the f-string insertion in lesson 1.

## What your edits to lessons 1 and 2 tell me

- Lesson 1 is a vocabulary lesson. You cut functions, function calls, and the debugger from it, added **state** as a key term, framed `print()` as a debugging tool with a motivating bug, and turned "Additional Notes" into a hidden question. The rest of this review treats lesson 1 as "words and the shape of a program" and pushes anything deeper to the lesson that owns it.
- Lesson 2 gained a reference-style operator catalogue (five tables with compatible types and notes) and a "weird expressions" challenge that rewards prediction. That is a different register from the surrounding prose and it works, but the tables pull in types and idioms that no lesson teaches (sets, tuples, `bytes`, `%` formatting, the walrus operator). Suggestions below trim the tables to what a fellow can act on in week 2 and point forward for the rest.
- You removed `type()` from lesson 2. It appears nowhere else in Mod 1 now. The Q1 design decision says introspection (`type()`, `dir()`, `id()`) belongs in Q1 because it makes "everything is an object" demonstrable in Mod 2. If the removal was deliberate, fine; if not, the "identify the data types" challenge you added is the natural place to reinstate it in three lines.
- Language edits I will match going forward: definitions that name the mechanism ("evaluates to a single value", "standard output"), `-` bullets, `py` fence tags on short snippets, and **Challenge:** prompts with a hidden answer.

## Cross-cutting

1. **The debugger has no home.** Lesson 1 no longer introduces the VS Code debugger, but lesson 3 says "run this with the debugger" twice (3-functions.md:150 and :277), lesson 5 says "try using the debugger" (5-loops.md:68), and lesson 10 says "the same thing you did with the debugger in chapter 3" (10-reading-unfamiliar-code.md:74). Either give lesson 3 a short "Inspecting a Function Call with the Debugger" section, which is the first place control flow stops being linear, or move it to `how-tos/how-to-debug.md` and link from those three places.
2. **Tuples are used but never taught.** `choice in ("1", "2")` in lesson 10 and `isinstance(value, (int, float))` in lesson 14, plus the `tuple` column in your lesson 2 tables and the pairs `zip()` and `.items()` produce. A six-line "Tuples" subsection in lesson 8 (a list that cannot change, written with parentheses, unpacks the same way) covers it.
3. **Generator expressions appear unexplained.** `any(score >= 90 for score in scores)` in lesson 13, and the `next()` callout. Either write `any([...])` with a list comprehension inside and drop the `next()` callout, or add one sentence naming the form.
4. **`print(sep=, end=)` in lesson 1 relies on keyword arguments from lesson 3.** Lesson 3 in turn says "you have been using keyword arguments since chapter 1". Keep the lesson 1 block as a preview, or cut it and change the lesson 3 sentence. Not both.
5. **`__pycache__` folders will appear in lesson 6** the moment a fellow imports a module, and nothing explains them. One line in lesson 7's `.gitignore` section (`__pycache__/` goes in the file too) removes a predictable question.
6. **Lesson 4 is the heaviest lesson** (two topics plus the moved type-conversion and truthiness sections, sixteen headings). Lesson 9 is the lightest. Cuts for lesson 4 are listed below; nothing needs to move.
7. **Bullet style is mixed.** Your edited files use `-`; most of mine use `*`. A mechanical pass, or Prettier on save, will settle it.
8. **File I/O and JSON are absent** except as a project stretch feature. A junior in 2026 is expected to read and write a JSON file. The lightest home is lesson 7's standard library section (`json.dump`, `json.load`, `open()` in eight lines) with the case study extension pointing back to it.

## 1. Intro to Programming

**Keep.** Your opening paragraph, the expanded key terms, the `print(mood)` at the end of the statements example, the Fahrenheit motivation for `print()`, the myth section with `time`, the IndentationError prediction, the uglier style question.

**Fix.**
- The Fahrenheit example (line 96) says "converts 212° Fahrenheit" but the code sets `fahrenheit = 100`, and the expression has a precedence bug (`100 - 32 * 5 / 9` is 82.2). If the bug is the point, say so with a prediction box whose answer is the parentheses fix; the new f-string section right below it uses the corrected expression, so the two now sit side by side.
- The `for` loop in Control Flow (line 213) uses `x += 1` with no `x = 0` above it.

**Cut.** The `print(sep=, end=)` block (lines 181 to 189), or keep it and accept the forward reference (cross-cutting item 4). Chapter 4 already teaches the same thing.

**Add.** The f-string section is in. Nothing else; the lesson is the right size.

## 2. Data Types and Variables

**Keep.** Both type tables, the YouTube question, your identify-the-types challenge, the light-switch motivation for operators, the weird-expressions challenge (the strongest prediction exercise in the module), precedence with the coin flip, everything under Variables.

**Fix.**
- The weird-expressions answers omit two of the twelve prompts: `"5" + 5` (a `TypeError`, and the single most important line in the set) and `[] or "Python"` (which is `"Python"`, and depends on truthiness from lesson 4).
- The Assignment Operators example ends with a dangling `if (n := len(items)) > 5:` (line 307). The walrus operator is not junior-necessary; cut the line.
- The five operator sections are H2 headings, so the table of contents lists them beside "Operators" rather than under it, and "The Conditional Expression" and "Resolution Order of Operations" are nested under "Assignment Operators". Make the five H3 and move the two back under "Operators".
- The Summary still says "arithmetic, comparison, and logical operators" while the body covers five categories.

**Cut from the tables.** Rows and examples about types no lesson teaches: `tuple`, `set`, `frozenset`, `bytes`, `range` in the compatible-types columns; `{1, 2} - {2}` and `{1} < {1, 2}` in the examples; the `%` string-formatting row and `"%s" % "hi"` (legacy, actively discouraged). The Logical Operators table's "returns the first falsy operand" semantics and the `[] and "hi"` example depend on truthiness, which is now lesson 4: keep `and`/`or`/`not` on booleans here and let lesson 4's truthiness section add the short-circuit note. The Augmented Assignment note about mutating in place is lesson 8's job.

**Keep but shorten.** The `is` row. It is a fair teaser for lesson 8, and `x is None` is the idiom to name. One sentence and a forward pointer rather than "memory address".

**Add.** `type()`, three lines, right after the identify-the-types challenge, as the way to check your answers. The REPL, one callout, as the place to try the weird expressions (lesson 6 introduces it today, which is late for its most useful moment).

## 3. Functions

**Keep.** The sum-and-average motivation, the DRY question, the temperature challenge, the parameter/argument prediction, the `None` return prediction, resolution order, multiple returns, default values and keyword arguments.

**Fix.** The two debugger references (cross-cutting item 1) and the `sep=` sentence (item 4).

**Cut.** The first code block under "Variables Review" repeats lesson 2's example verbatim; the section can open with the three-copies block instead.

**Add.** A one-line docstring convention, five lines. Generated code in lesson 10 and every library fellows read in Q2 will have them, and `help()` on a function shows them, which is introspection in the spirit of the Q1 decision.

## 4. Strings and Conditional Statements

**Keep.** Bracelet image, negative indexes, the `IndexError` and immutability predictions, `in`/`startswith`/`find`, slicing, `strip`/`split`/`join`/`isdigit`, method chaining, all of Conditional Statements, the moved Type Conversion and Truthy/Falsy sections.

**Cut.** Escaping Characters to a callout (three lines). The `len(message) - 1` indexing block is redundant now that negative indexes are taught above it; keep one example. `has_only_one` with `find`/`rfind`: clever, low value, six lines saved.

**Add.** One sentence in the truthiness section: to test for `None`, write `is None`, because `0` and `""` are falsy too and `if not value:` cannot tell them apart. It pairs with the `is` row you added in lesson 2.

## 5. Loops

**Keep.** Coin flip, `range()` and its prediction, both challenges wrapped in `main()`, `break`/`continue`, the `break` vs `return` callout, `KeyboardInterrupt`, nested loops, the GOTO callout.

**Add.** Looping over a string's characters, four lines, as the bridge to "for item in list" in lesson 8. It also gives `for` a use before lists exist.

**Cut.** Nothing.

## 6. Modules and `if __name__ == "__main__"`

**Keep.** The circle program and its split, both import forms, the `import *` question, the "importing runs the file" prediction, `__name__`, the guard, `input()` and its prediction, the madlib challenge.

**Cut.** "What is the Python interpreter?" restates lesson 1's key term; keep only the REPL paragraph, or move the REPL to lesson 2 (see above) and cut the section entirely.

**Add.** `import circle_helpers as ch`, one line. Fellows will meet `import numpy as np` style aliases in every tutorial they read.

## 7. The Python Ecosystem

**Keep.** All of it. This is the chapter the cohort is most likely to stall on, and it is written for that.

**Add.** `__pycache__/` in the `.gitignore` section. `json` in the standard library section (cross-cutting item 8). A sentence on what to do when the prompt does not show `(.venv)`: it is the first thing to check, and the chapter says so only inside a hidden answer.

**Cut.** Nothing. "The Commands, All Together" duplicates the cheat sheet, but a fellow mid-setup wants it on the page.

## 8. Lists

**Keep.** Basics, `for friend in friends`, `enumerate`, `has_value`, mutability and its question, the method list, `id()` and `is`, the aliasing prediction, `empty_the_list`, pure and impure functions, copies, the copy challenge, 2D lists, unpacking.

**Cut.** Slice assignment (`letters[2:4] = [...]`): rare in beginner code. The `increment_by` example with `global`: it is the third appearance of the `global` lesson; `roll_die` and `empty_the_list` already make the impure point.

**Add.** Tuples (cross-cutting item 2). `len()` on a nested list to answer "how many rows". Both short.

## 9. Dictionaries

**Keep.** All of it; it is the right length for the session.

**Add.** A "list of dictionaries" example with a loop over it (`for user in users: print(user["name"])`). It is the data shape of the case study, all three projects, and the testing chapter, and no lesson shows it before the case study. One sentence that keys must be immutable, which tuples (lesson 8) makes sayable.

## 10. Reading Unfamiliar Code

**Keep.** The orientation questions, the six steps, the shop program, the trace, both predictions, the generated-code section, the practice program.

**Cut.** The lesson is the second longest. The "Step 6" sample know/guess lists can lose half their entries, and the closing "Key Takeaways" repeats the Summary. Ten percent shorter without losing a device.

**Fix.** `choice in ("1", "2")` is a tuple (cross-cutting item 2). Either teach tuples in lesson 8 first or name it here as one of the deliberate unknowns alongside `sorted` and `join`.

**Add.** One line linking to the AI policy's "standing instruction you can paste", as the way to ask a tutor-mode model about code you are reading. A link, not new prose.

## 11. Errors and Tracebacks

**Keep.** Raised vs. thrown, syntax vs. runtime with the prediction, the error catalogue, the traceback read bottom-up, the two-line-numbers prediction, `try`/`except`, the `input()` section, raising your own.

**Cut.** The hidden `OSError` list to three entries (`FileNotFoundError`, `PermissionError`, `ConnectionRefusedError`).

**Add.** A traceback that crosses two files, since lesson 6 taught modules and the project will have three. Six lines: the `File` line changes, the reading rule does not.

## 12. First-Class Functions and Higher-Order Functions

**Keep.** The pop quiz with `type()` (which now assumes lesson 2 reinstates it), functions stored in dictionaries as a dispatch table (directly useful in the project), `repeat` and `repeat_every`, do-not-invoke, `lambda`, `sorted(key=)` and `max(key=)`.

**Cut.** "Some Fun Examples": the spinner and the alien are fun, but they need `global`, `end="\r"`, `flush=True`, and `shutil`, and they teach a pattern the chapter then apologises for. Make them an optional callout with a link, or drop them. "Functions That Return Functions" to a two-sentence pointer at the Mod 2 decorators session. "Looping with Callbacks" prose; keep Challenge 2 (write `for_each`) as the exercise.

**Add.** Nothing.

## 13. Comprehensions and Built-in Iteration

**Keep.** Imperative vs. declarative, the toolkit table, transform and filter, first match with a loop, `sum`/`min`/`max` and the accumulator pattern, `sorted` vs `.sort()` with the `None` prediction, `key=`, the frequency counter and `Counter`, the smiley face, `zip`.

**Cut.** "Using the Index in a Comprehension": the example is contrived. The `next()` callout (cross-cutting item 3). Dictionary comprehensions to a two-line callout.

**Fix.** `any`/`all` generator expressions (item 3).

## 14. pytest and Test-Driven Development

**Keep.** Test files and why, install and layout, first test, `python3 -m pytest` and its callout, reading a failure, `==` vs `is`, refactor with confidence, the TDD loop on `double_all_purely`.

**Cut.** The Banking System Challenge (deposit, refactor, withdraw by TDD) is the second half of the lesson and repeats the cycle already taught. Move it to an assignment and keep a one-paragraph pointer. "Key Takeaways" repeats "Test Files" and the TDD bullets word for word, as the original did; cut it.

**Add.** Nothing.

## Case Study and Project

**Keep.** Both as they are. The case study's inline code and the project's phases are what fellows will copy from.

**Fix.** The project's template repository (15-project-week.md:81) is the JavaScript one until a Python template exists.

**Add.** In the case study, one prediction: after Clear All Tasks, choose Complete Task and enter 1. It exercises the two-condition guard in `complete_task` that Investigation Question 2 asks about.

## Regex and Cheat Sheet

Regex stays optional and untouched. The cheat sheet should absorb whatever the lesson 2 operator tables settle on, and gain a tuple line and a `json` line if those additions go in.
