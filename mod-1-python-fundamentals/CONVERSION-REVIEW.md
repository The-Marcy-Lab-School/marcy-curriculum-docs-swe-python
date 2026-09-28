# Conversion Review: Mod 1 JavaScript Fundamentals → Python Fundamentals

This file is for Ben's review of the `mod-1-python-fundamentals` folder. It is not listed in `SUMMARY.md` and should be deleted once the folder is approved. The raw output of `scripts/conversion-report.py` for every chapter is at the bottom.

## What was built

Twenty files in `mod-1-python-fundamentals/`, following the nineteen Mod 1 sessions in `scope-and-sequence.md`. Session 24 (the proctored assessment) has no chapter. Every code sample in every chapter was run under Python 3.12.4 before it was written down; every quoted error message, traceback, pip listing, and pytest report is genuine output. The three example programs in the new Reading Unfamiliar Code chapter, the full Task Manager case study program, and all nine pytest tests in the testing chapter were executed end to end.

| Session        | Chapter                                | Original                                                               |
| -------------- | -------------------------------------- | ---------------------------------------------------------------------- |
| 6              | 1-intro-to-programming.md              | 0-intro-to-programming.md                                              |
| 7              | 2-data-types-variables.md              | 1-data-types-variables.md                                              |
| 8              | 3-functions.md                         | 2-functions.md                                                         |
| 9              | 4-strings-conditional-statements.md    | 3-strings-conditional-statements.md                                    |
| 10             | 5-loops.md                             | 5-loops.md                                                             |
| 11             | 6-modules-main.md                      | 4-node-modules-testing.md (first half)                                 |
| 12             | 7-python-ecosystem.md                  | 4-node-modules-testing.md (second half)                                |
| 13             | 8-lists.md                             | 6-arrays.md                                                            |
| 14             | 9-dictionaries.md                      | 7-objects.md                                                           |
| 15             | 10-reading-unfamiliar-code.md          | none (new)                                                             |
| 16             | 11-errors-tracebacks.md                | 8-errors.md                                                            |
| 17             | 12-first-class-functions-hof.md        | 9-hof-callbacks.md                                                     |
| 18             | 13-comprehensions-builtin-iteration.md | 10-hof-array-methods.md                                                |
| 19             | 14-pytest-tdd.md                       | 11-unit-testing.md, plus the Jest section of 4-node-modules-testing.md |
| 20             | case-study.md                          | case-study.md                                                          |
| 21 to 23       | 15-project-week.md                     | 13-project-week.md                                                     |
| Friday reading | regex.md                               | 11-regex.md                                                            |
|                | cheatsheet.md, Overview.md, README.md  | same names                                                             |
|                | not converted                          | 12-memory-management.md                                                |

`12-memory-management.md` is a title and a Google Slides embed about the JavaScript engine. It has no Python counterpart and was not converted. The memory model it covered (heap, references) is taught in prose in the lists chapter.

Also changed outside the folder: `SUMMARY.md` lists the new folder under Q1 (the JavaScript block stays commented out beneath it); `conversion-decisions.md` gained a "Decisions from Mod 1" section; `scripts/conversion-report.py` accepts an optional second argument naming the original's path, because the new folder name differs from the old one.

## Decisions, chapter by chapter

Every chapter drops the "Follow along with code examples here" hint. No Python follow-along repositories exist yet, and a hint pointing at JavaScript code would mislead. The repositories that would need creating are listed under "For Ben to check" below.

**1. Intro to Programming.** The four DROPPED/ADDED pairs are renames (Node → the Python interpreter, `console.log` → `print()`). The one-billion-iteration loop became one hundred million, because Python takes about four seconds for that and a minute or more for a billion; `console.time` became the shell's `time` command plus a demonstration of `print(sep=, end=)`. The original's Python aside under "The Console" is cut because it was a Python example inside a JavaScript book. Images fell from 3 to 1: the two Run and Debug screenshots show `index.js` and a "JavaScript Debug Terminal" button and were dropped rather than relabelled; the language-neutral SVG of the debugger buttons stays. The style-guide link now points at PEP 8, because `how-tos/style-guide.md` is the Airbnb JavaScript guide. The debugger is not introduced in this chapter; it is introduced in chapter 3, at the first function call, where control flow first stops being linear. The Code Style section is rewritten: indentation is syntax in Python, so the "fix the style" question is about PEP 8 spacing and `snake_case` and has a hidden answer. An f-string subsection sits under `print()` so that chapter 2 can use f-strings without introducing them.

**2. Data Types and Variables.** Ternary → Conditional Expression and `typeof` → `type()` are renames. "Type Coercion & Truthy vs. Falsy" is not in this chapter: it moved to chapter 4, where conditions give it a reason to exist (see below). Because truthiness is no longer taught before the scope example, that example's guard reads `if friend == "":` rather than `if not friend:`. Declare/Assign/Reference → Assign/Reassign/Reference, since Python has no declaration step; a `count++` predict-then-run added. "The Four Ways To Declare Variables" → "Constants and the `global` Keyword" (no `const`/`let`/`var`; `ALL_CAPS` convention; `UnboundLocalError` predict-then-run). "Hoisting" → "Order Matters: Assign Before You Use" (no hoisting; the Python lesson is that a function is looked up when called, not when written). The JavaScript-history callout about never crashing a site is cut. The hidden question about `const` without a value becomes "Can you create a variable without giving it a value?" (answer: `None`). The hidden question about two `message` variables now uses two functions, because the original's example relied on block scope, which Python does not have. Scope levels Block/Function/Module/Global → Local/Global/Built-in, with an explicit statement that blocks do not create scope and a predict-then-run on it. `undefined` is gone from the type table (does not exist); `float` is added. The precedence section uses the Fahrenheit conversion from chapter 1 as its worked example, so the chapter imports no modules.

**3. Functions.** The VS Code debugger is introduced here, under Function Calls, with the language-neutral SVG of its controls. A docstring paragraph follows the first function definition. "Arrow Functions vs. Function Declarations vs. Function Expressions" → "Default Values and Keyword Arguments". Python has one way to define a function, so the section's slot teaches the parameter feature that `print(sep=)`, `sorted(key=)`, and the case study all use. The implicit-return challenge is replaced by a challenge on defaults and a predict-then-run showing that functions without `return` produce `None`. `printSum('hello', 5)` and `printSum()` now raise `TypeError` (JavaScript printed `hello5` and `NaN`), presented as a predict-then-run. The `say_hello()` with no arguments in the challenge solution likewise raises.

**4. Strings and Conditional Statements.** Two sections arrive here from the data types chapter, placed between Guard Clauses and Conditional Expressions. "Type Conversion" opens with why conditions need it (`input()` gives strings) and keeps the original's `str()`/`int()`/`float()` examples; the `"1" + 1` question becomes a predict-then-run, because Python raises `TypeError` where JavaScript produced `"11"`, and the original's hidden answer (an error would alert the programmer) is now literally what happens, so its text is kept. "Truthy and Falsy Values" keeps the `bool()` table, shows `if not friend:` as a guard clause against empty input, and adds an `if "False":` predict-then-run. The other DROPPED/ADDED pairs are renames. `message[50]` raises `IndexError` and `message[0] = "J"` raises `TypeError`, both predict-then-run (JavaScript gave `undefined` and silence). `includes` → the `in` operator; `indexOf`/`lastIndexOf` → `find`/`rfind`; `replaceAll` → `replace`, which replaces all by default. Added: negative indexes, `strip`/`split`/`join`/`isdigit`, and method chaining, because the loops chapter and the project depend on them.

**5. Loops.** `for(;;)` → `for i in range()`, `Math.random` → `random.choice`, `isNaN(Number())` → `.isdigit()`. Both challenges are wrapped in `main()` because the original's top-level `return` is a `SyntaxError` in Python. Added a `range(5)` predict-then-run and a `KeyboardInterrupt` callout.

**6. Modules and `if __name__ == "__main__"`.** Half of the old chapter 4. "What is Node?" is cut: the interpreter is a chapter 1 key term, and the REPL, with the existing Python REPL screenshot, lives in chapter 2 beside the operators challenge where it is first useful. Images fell from 6 to 0 because the others are Node and npm screenshots. A callout explains the `__pycache__` folder that appears on first import. `module.exports`/`require`/destructuring → "Every Top-Level Name Can Be Imported" and "Importing with `import` and `from ... import`". The hidden question "why an object rather than an array for exports" (access by name) becomes "why not `from x import *`" (access by name, plus a verified shadowing hazard). NPM and `prompt-sync` → the built-in `input()`; the rest of the package material moved to chapter 7; the Jest section moved to chapter 14; NPM tips, `package.json` scripts, and `npm init -y` are cut because they have no equivalent (project setup is `python3 -m venv`, in chapter 7). New material: `__name__` and the guard, which the scope and sequence names. Callouts fell from 5 to 3: the `require('prompt-sync')()` pattern and the JSON definition have no counterpart here; JSON arrives in Mod 5.

**7. The Python Ecosystem.** The other half of the old chapter 4, so every section is ADDED. NPM registry → PyPI; `npm i` → `pip install`; `package.json` and `node_modules` → `requirements.txt` and `.venv`; sub-dependencies → `pip show`; `devDependencies` → developer dependencies with `pytest` in place of `nodemon`, which has no Python equivalent and is cut. The demonstration package is `rich`. New: a standard library section (fellows already used `random`) that also introduces `json` with `open()` and `with`, since reading and writing a JSON file is expected of a junior and powers the case study's persistence extension; and a full virtual environment section, because the Mod 0 environment setup documents install `venv` but do not teach it (the Windows document says "You will use both of these in Mod 1"). Version numbers in the quoted `pip` output came from a live install and carry a "may vary" note. Hidden questions: 4 → 4, with `nodemon` replaced by `pytest` and two new ones about `mdurl` and committing `.venv`.

**8. Lists.** Every DROPPED/ADDED pair is Arrays → Lists. "Reference vs. Primitive Values" → "Mutable Values and References", since mutability is Python's organising idea. The embedded Google Slides deck on the JavaScript memory model is not embedded; `id()` and `is` show the same thing live. The hidden question about mutating a `const` array becomes a question about why lists allow what strings refuse. `.length = 0` → `.clear()`; `splice` → `insert`, slice assignment, `remove`, `del`; spread → `[*items]`, `list()`, `[:]`. "Destructuring Assignment and Rest Operator" → "Unpacking" with `*rest`. `for friend in friends` and `enumerate` are introduced here because the case study needs them.

**9. Dictionaries.** Objects → Dictionaries throughout. Dot notation is gone (dictionaries have none); `.get()` and `KeyError` take its place, with a predict-then-run. `delete` → `del` and `.pop()`. "Object Shorthand Using Variables" is cut (no Python equivalent); its `make_user` example and its point survive under "Building a Dictionary from Parameters". "Destructuring" is cut; `.items()` unpacking and "Passing a Dictionary to a Function" carry the same jobs. A `dict_keys` predict-then-run is added.

**10. Reading Unfamiliar Code.** New, for session 15. The six orientation questions come from the master planning document's debugging ladder (§4.2, Q1). The worked example is a two-file inventory program; the "Reading Code a Model Wrote" section has two model-style functions with real defects (`input()` compared to an `int`; an accumulator that assigns instead of adding); the practice program is a bill splitter with two crashes to find. All three were run. The AI-policy paragraph is written to agree with `ai-policy.md`'s one-sentence test without restating its rules.

**11. Errors and Tracebacks.** "thrown" → "raised" (with a note that both words are used). `ReferenceError` → `NameError`; `SystemError` and the `errno` list → `FileNotFoundError` and a hidden list of `OSError` subclasses; `RangeError` is cut (no Python equivalent; `ValueError` and `IndexError` cover its cases). Added `IndentationError`, `ValueError`, `IndexError`, `KeyError`, `AttributeError`, `ZeroDivisionError`. "How to Read errors" → "How to Read a Traceback", rewritten rather than translated because Python prints the call stack top-down with the error at the bottom. Added "The Error You Will Catch Most" (`ValueError` from `input()`), which the project rubric relies on, and "Raising Your Own Errors". The one residue hit, "undefined variables", is ordinary English.

**12. First-Class Functions and Higher-Order Functions.** "Functions Stored in Objects are Referred to as Methods" → "Functions Stored in Dictionaries", teaching the dispatch table; the methods point survives as a callout. `setTimeout`/`setInterval` have no Python counterpart, so the chapter writes its own `repeat` and `repeat_every` with `time.sleep`; the spinner and alien examples are ported with `end="\r"`, were run, and sit in an optional collapsed block because they need `global`. "Array Iterators" and "forEach" → moved to chapter 13's toolkit table; the `for_each` challenge stays here under "Looping with Callbacks". Added `lambda`, a two-sentence pointer to functions returning functions (the Mod 2 decorators session), and `sorted(key=)`. The report's two "broken links" are the script matching `actions["greet"]('Ada')` inside a code block; nothing is broken.

**13. Comprehensions and Built-in Iteration.** Every array method section is replaced by its Python tool: `map` → list comprehension; `filter` → comprehension with `if`; `find`/`findIndex` → a loop with early `return` (with `next()` in a callout); `reduce` → `sum()`/`min()`/`max()`/`len()` plus the accumulator pattern; `sort(compare)` → `sorted()`/`.sort()` with `key` and `reverse`. The comparator-function contract (return -1, 0, 1) is cut because Python's `key` replaces it; the `sortAscendingByLength` challenge is shown as `key=len` in the body and the challenge itself becomes sorting dictionaries by age. "Using All Callback Parameters" → "Using the Index in a Comprehension"; "Chaining" → "Combining Steps". Added `zip`, `any`, `all`, dictionary comprehensions, a `.sort()` returns `None` predict-then-run, and a callout naming `map()`/`filter()`. The `=>` residue hit is the `x inches => y feet` format string from the original.

**14. pytest and Test-Driven Development.** Jest → pytest; `toBe`/`toEqual`/`.not` → `==`, `is`, `is not`. `sum.js` became `calc.py` with `add`, to avoid shadowing the built-in `sum`. The two Jest screenshots (`sum-passing-tests.png` here, `failing-tests.png` in the old chapter 4) are replaced by genuine pytest output, so the image count fell from 1 to 0 and a "Reading a Failure" section was added. Tests run with `python3 -m pytest`; the bare `pytest` command fails on the `src` import, which was verified and is explained in a callout. The Banking System Challenge is a one-paragraph pointer to the assignment, because it repeats the TDD cycle already taught on `double_all_purely`; the assignment version's tests were written and pass, and the original's two `withdraw` bugs (wrong parameters, mutating the account rather than the copy) are not carried over. Added `pytest.raises` to the extensions.

**Case Study.** "Arrays and Objects" → "Lists and Dictionaries"; "Array Higher-Order Methods" → "Built-in Iteration". Added "The Code" with all three files inline, since no Python repository exists; the program was run through every menu path. The screenshot from the original's unreferenced `img/` folder is language-neutral and is now used. Added questions on `__main__`, `enumerate(start=1)`, and a tests extension. Error Handling Q1 is rewritten because the Python version catches `ValueError` with `try`/`except`. Variables Q1 (about `let`) becomes reassignment versus mutation. Setup uses the venv commands.

**Project.** Three days, not a week, and a paragraph telling fellows they will return to this program in the December critique unit. Node → Python throughout; `package.json` → `requirements.txt` and `.gitignore`; `require`/`module.exports` → `import` and the `__main__` guard; "array higher-order method" → comprehension or built-in. User Interaction criterion 2 now says the program never crashes with a traceback on bad input. The `swe-project-1-cli-app` template is named but not linked; it is the JavaScript template.

**Regex.** JavaScript methods → `re.fullmatch`, `re.search`, `re.findall`, `re.sub`; `str.match` with the `g` flag → `findall` (there is no first-only variant to explain). Flags become arguments. Marked optional Friday reading per the scope and sequence.

**Cheat Sheet, Overview.** Restructured to the Python chapter order. The Overview gains a "by the end of this module" paragraph in the style of the Mod 0 Overview and names the assessment.

## Voice check

Original, chapter 1: "It is common to think that without `console.log()`, the program isn't doing anything. This is not the case!"
New, chapter 1: "Nothing was printed by the program, but the Terminal reports that it spent almost four seconds running it. (Your numbers will differ.)"

Original, chapter 2: "Depending on your perspective, you may think that it is nonsensical to allow this kind of operation. Why would anyone want to add a string and a number in this way?"
New, chapter 2: "Python will not add a string and a number. It does not know whether you wanted the string `"11"` or the number `2`, and rather than pick one it stops and tells you."

Original, chapter 5: "Doing this by hand certainly would take a while. We can write code to likely do it faster:"
New, chapter 10: "The danger is not that you will fail to understand it. The danger is that you will start changing things before you understand it, get lost, and not be able to say afterward what you changed or why. Engineers call this **thrashing**."

Original, chapter 6: "While you could figure this out, there is no need to reinvent the wheel!"
New, chapter 7: "The general rule: commit the recipe, not the meal."

## Look here first

1. `10-reading-unfamiliar-code.md:52` through `:85`, the six-step method. Wholly new prose with no original to check against, and it is the chapter the master plan singles out for week 4. Then `:264` to `:270`, the paragraph that positions reading model-written code against the AI policy; it needs to say what you want it to say.
2. `7-python-ecosystem.md:65` through `:100`, the virtual environment instructions. Fellows will follow these literally. The commands were run on macOS; the WSL sentence at `:95` and the VS Code interpreter sentence at `:97` were not verified here.
3. `2-data-types-variables.md:511` and `:554`, the two sections that replace the `const`/`let`/`var` and hoisting material. New teaching decisions: `ALL_CAPS` constants, the `UnboundLocalError` box, and "define before you call" as the Python version of the hoisting lesson.
4. `3-functions.md`, the "Inspecting a Function Call With the Debugger" subsection. The configuration label "Python File" and the claim that `breakpoint()` stops the VS Code debugger are from memory, not verification.
5. `case-study.md:69` through `:160`, the program itself. I wrote it; it runs; but it is now the reference implementation fellows will copy, so its shape (menu then tasks then prompt, `os.system('clear')`, `try`/`except` around `int()`) is a curriculum decision.

## For Ben to check or create

- Python follow-along repositories for chapters 2 to 14, the case study (`swe-casestudy-1-cli-task-manager`, Python version), and a Python `swe-project-1-cli-app` template with `.gitignore` and empty `requirements.txt`.
- Recapture the two Run and Debug screenshots against a `.py` file, and confirm the "Python File" configuration label and `breakpoint()` behaviour under the VS Code Python Debugger extension.
- Confirm `source .venv/bin/activate` and the `(.venv)` prompt on a fellow's WSL Ubuntu install, and what VS Code shows when it asks for an interpreter.
- Version strings quoted in chapter 7 (`rich 15.0.0`, `pip 24.0`) and chapter 14 (`pytest 9.1.1`, Python 3.12.4) are what installed here today; fellows on 3.14 will see different numbers and the text says so.
- `scripts/conversion-report.py` flags two false positives worth knowing about if it is run again: a `[key](arg)` dictionary lookup inside a code block reads as a Markdown link, and a bare word on the line after an untagged fence reads as a fence language.
- The regex chapter's `re.IGNORECASE` is passed positionally to `re.search` and by keyword to `re.sub`; both forms were run.

## Raw tool output

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/1-intro-to-programming.md
========================================================================

262 lines in the original  ->  307 lines now

SECTIONS  (6 of 12 kept)
------------------------
  DROPPED  Running a file with Node
  DROPPED  The Console
  DROPPED  Debunking The Console.log Myth
  DROPPED  Conditional Statements
  DROPPED  Functions and Function Calls.
  DROPPED  Inspecting the Control Flow With Node
  ADDED    Running a file with the Python interpreter
  ADDED    Printing to the Terminal with `print()`
  ADDED    Printing Values Inside Text with f-strings
  ADDED    Debunking The `print()` Myth

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            0        4
  Callout ({% hint %})              2        2
  Image / diagram                   3        0  <-- fewer
  Challenge prompt                  0        1
  Learning objectives               0        0
  Follow-along repo                 0        0

HIDDEN QUESTIONS IN THE ORIGINAL (0)
------------------------------------
  (none)

HIDDEN QUESTIONS NOW (4)
------------------------
  Q: In the statements above, what expressions can you see?
  Q: So, does it work?
  What actually happens
  Answer

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       21
  py           1
  python       14
  sh           2

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/2-data-types-variables.md
========================================================================

536 lines in the original  ->  709 lines now

SECTIONS  (8 of 14 kept)
------------------------
  DROPPED  Ternary Operator
  DROPPED  typeof Operator
  DROPPED  Type Coercion & Truthy vs. Falsy
  DROPPED  Using Variables: Declare, Assign, Reference
  DROPPED  The Four Ways To Declare Variables
  DROPPED  Hoisting: Why We Don't Use `var`
  ADDED    Arithmetic Operators
  ADDED    Comparison (Relational) Operators
  ADDED    Logical Operators
  ADDED    Membership and Identity Operators
  ADDED    Assignment Operators
  ADDED    The Conditional Expression
  ADDED    Using Variables: Assign, Reassign, Reference
  ADDED    Constants and the `global` Keyword
  ADDED    Order Matters: Assign Before You Use

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            7       11
  Callout ({% hint %})              5        7
  Image / diagram                   1        2
  Challenge prompt                  1        5
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (7)
------------------------------------
  Q: Open up YouTube.com. What examples can you come up with for each of the primitive and reference data types listed above?
  Q: So, what is the order of operations? What is the value stored in result?
  Answers
  Answer
  Tradeoffs of each approach
  Q: Can you declare a `const` variable without an initial value? Why or why not?
  Q: Why is it even possible to have two variables called `message` within the `greetFriend` function?

HIDDEN QUESTIONS NOW (11)
-------------------------
  Q: Open up YouTube.com. What examples can you come up with for each of the data types listed above?
  Answers
  Q: So, what is the order of operations? What is the value stored in result?
  Answers
  Tradeoffs of each approach
  What actually happens
  Q: Can you create a variable without giving it a value?
  What actually happens
  Q: Why is it even possible to have two variables called `message` in the same program?
  What actually happens
  What actually happens

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       34
  py           6
  python       22

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/3-functions.md
========================================================================

319 lines in the original  ->  375 lines now

SECTIONS  (8 of 9 kept)
-----------------------
  DROPPED  Arrow Functions vs. Function Declarations vs. Function Expressions
  ADDED    3. Functions
  ADDED    Inspecting a Function Call With the Debugger
  ADDED    Default Values and Keyword Arguments

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            3        6
  Callout ({% hint %})              2        4
  Image / diagram                   0        1
  Challenge prompt                  2        4
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (3)
------------------------------------
  Q: What are the benefits of using Variables in our code?
  Q: What isn't great about this code?
  Solution

HIDDEN QUESTIONS NOW (6)
------------------------
  Q: What are the benefits of using Variables in our code?
  Q: What isn't great about this code?
  What actually happens
  Solution
  What actually happens
  Answer

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       25
  python       17

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/4-strings-conditional-statements.md
========================================================================

367 lines in the original  ->  475 lines now

SECTIONS  (11 of 15 kept)
-------------------------
  DROPPED  4. String Methods & Conditional Statements
  DROPPED  Escaping Characters
  DROPPED  String Interpolation
  DROPPED  Use Ternary Operators To Simplify Conditionals
  ADDED    4. Strings and Conditional Statements
  ADDED    String Interpolation with f-strings
  ADDED    Type Conversion
  ADDED    Truthy and Falsy Values
  ADDED    Use Conditional Expressions To Simplify Conditionals

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            2        6
  Callout ({% hint %})              1        5
  Image / diagram                   2        2
  Challenge prompt                  0        4
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (2)
------------------------------------
  Q: In the decision tree above, what are the variables that will impact the end result?
  Q: Why doesn't the last return statement need an `if` statement?

HIDDEN QUESTIONS NOW (6)
------------------------
  What actually happens
  What actually happens
  Q: In the decision tree above, what are the variables that will impact the end result?
  Q: Why doesn't the last return statement need an `if` statement?
  What actually happens
  What actually happens

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       30
  python       24

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/6-modules-main.md
========================================================================

599 lines in the original  ->  374 lines now

SECTIONS  (4 of 16 kept)
------------------------
  DROPPED  5. Node Modules & Testing
  DROPPED  What is Node?
  DROPPED  Exporting with `module.exports` (CommonJS)
  DROPPED  Importing with `require()` (CommonJS)
  DROPPED  Destructuring Shorthand
  DROPPED  Node Package Manager (NPM)
  DROPPED  Installing and Using Dependencies from NPM
  DROPPED  Dependencies, `package.json`, and `node_modules`
  DROPPED  Developer Dependencies
  DROPPED  Jest Module and Testing
  DROPPED  NPM Tips and Tricks
  DROPPED  `package.json` Scripts
  ADDED    5. Modules and `if __name__ == "__main__"`
  ADDED    Every Top-Level Name Can Be Imported
  ADDED    Importing with `import` and `from ... import`
  ADDED    What Happens When You Import a File?
  ADDED    The `if __name__ == "__main__":` Guard
  ADDED    Getting Input from the User with `input()`

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            4        5
  Callout ({% hint %})              5        4  <-- fewer
  Image / diagram                   6        0  <-- fewer
  Challenge prompt                  0        2
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (4)
------------------------------------
  Q: Why do we use an Object to export many values instead of an Array?
  Q: How does this file structure demonstrate separation of concerns? What is the concern of each file?
  Q: Why is `nodemon` installed as a developer dependency and not a required dependency of the project?
  Q: Solution

HIDDEN QUESTIONS NOW (5)
------------------------
  Q: How does this file structure demonstrate separation of concerns? What is the concern of each file?
  Q: Why write `import circle_helpers` and then `circle_helpers.get_area(...)`, or list the names you want, when `from circle_helpers import *` would let you write `get_area(...)` with less typing?
  What actually happens
  What actually happens
  Q: Solution

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       21
  python       15

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/7-python-ecosystem.md
========================================================================

599 lines in the original  ->  306 lines now

SECTIONS  (3 of 16 kept)
------------------------
  DROPPED  5. Node Modules & Testing
  DROPPED  What is Node?
  DROPPED  Modules
  DROPPED  Exporting with `module.exports` (CommonJS)
  DROPPED  Importing with `require()` (CommonJS)
  DROPPED  Destructuring Shorthand
  DROPPED  Node Package Manager (NPM)
  DROPPED  Installing and Using Dependencies from NPM
  DROPPED  Dependencies, `package.json`, and `node_modules`
  DROPPED  Jest Module and Testing
  DROPPED  NPM Tips and Tricks
  DROPPED  `package.json` Scripts
  DROPPED  Madlib Challenge
  ADDED    6. The Python Ecosystem: pip, venv, and requirements.txt
  ADDED    The Standard Library
  ADDED    Third-Party Packages and PyPI
  ADDED    Virtual Environments with `venv`
  ADDED    Installing Packages with `pip`
  ADDED    Dependencies and Sub-Dependencies
  ADDED    Keep `.venv` Out of Git
  ADDED    The Commands, All Together

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            4        4
  Callout ({% hint %})              5        2  <-- fewer
  Image / diagram                   6        0  <-- fewer
  Challenge prompt                  0        1
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (4)
------------------------------------
  Q: Why do we use an Object to export many values instead of an Array?
  Q: How does this file structure demonstrate separation of concerns? What is the concern of each file?
  Q: Why is `nodemon` installed as a developer dependency and not a required dependency of the project?
  Q: Solution

HIDDEN QUESTIONS NOW (4)
------------------------
  What actually happens
  Q: `rich` requires `markdown-it-py` and `pygments`. Where did `mdurl` come from?
  Q: Why not just commit `.venv` so that nobody has to run `pip install`?
  Q: Why is `pytest` a developer dependency and not a required dependency of the project?

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       26
  python       4
  sh           10

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/5-loops.md
========================================================================

276 lines in the original  ->  315 lines now

SECTIONS  (7 of 8 kept)
-----------------------
  DROPPED  Loops
  ADDED    7. Loops

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            2        3
  Callout ({% hint %})              3        4
  Image / diagram                   0        0
  Challenge prompt                  0        1
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (2)
------------------------------------
  Check out the solution!
  Check out the solution!

HIDDEN QUESTIONS NOW (3)
------------------------
  What actually happens
  Check out the solution!
  Check out the solution!

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       13
  python       11

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/8-lists.md
========================================================================

358 lines in the original  ->  415 lines now

SECTIONS  (2 of 13 kept)
------------------------
  DROPPED  Arrays
  DROPPED  Array Basics
  DROPPED  Arrays Are Mutable
  DROPPED  Array Methods for Adding and/or Removing Values
  DROPPED  Reference vs. Primitive Values
  DROPPED  How Reference Types (Arrays and Objects) are Stored in Memory
  DROPPED  Making Copies of Arrays to Make Pure Functions with the Spread Syntax
  DROPPED  Copying Array Challenge
  DROPPED  Advanced Array Syntax
  DROPPED  2D Arrays
  DROPPED  Destructuring Assignment and Rest Operator
  ADDED    8. Lists
  ADDED    Summary
  ADDED    List Basics
  ADDED    Lists Are Mutable
  ADDED    List Methods for Adding and/or Removing Values
  ADDED    Mutable Values and References
  ADDED    How Lists Are Stored in Memory
  ADDED    Making Copies of Lists to Make Pure Functions
  ADDED    Copying List Challenge
  ADDED    Advanced List Syntax
  ADDED    2D Lists
  ADDED    Tuples: Lists That Cannot Change
  ADDED    Unpacking

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            2        4
  Callout ({% hint %})              1        1
  Image / diagram                   0        0
  Challenge prompt                  0        1
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (2)
------------------------------------
  Check out this example
  Question: How are we allowed to modify the array if it is stored in a `const` variable?

HIDDEN QUESTIONS NOW (4)
------------------------
  Check out this example
  Q: We changed the list without ever writing `end_letters = ...`. Strings would not allow that. Why do lists?
  What actually happens
  Solution

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       24
  python       22

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/9-dictionaries.md
========================================================================

340 lines in the original  ->  330 lines now

SECTIONS  (2 of 10 kept)
------------------------
  DROPPED  Objects
  DROPPED  Accessing Objects with Dot Notation and Bracket Notation
  DROPPED  Dynamic Properties Challenge
  DROPPED  Objects are Reference Types
  DROPPED  Iterating Over Keys and Values of an Object
  DROPPED  Advanced Object Syntax
  DROPPED  Object Shorthand Using Variables
  DROPPED  Destructuring
  ADDED    9. Dictionaries
  ADDED    Accessing Values with Bracket Notation and `.get()`
  ADDED    Dynamic Keys Challenge
  ADDED    Dictionaries are Mutable and Held by Reference
  ADDED    Iterating Over Keys and Values of a Dictionary
  ADDED    Lists of Dictionaries
  ADDED    Dictionaries and Functions
  ADDED    Building a Dictionary from Parameters
  ADDED    Passing a Dictionary to a Function

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            1        3
  Callout ({% hint %})              1        2
  Image / diagram                   0        0
  Challenge prompt                  0        2
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (1)
------------------------------------
  Solution

HIDDEN QUESTIONS NOW (3)
------------------------
  What actually happens
  Solution
  What actually happens

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       23
  python       19

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/10-reading-unfamiliar-code.md
========================================================================

No JavaScript original at ../marcy-curriculum-docs/mod-1-python-fundamentals/10-reading-unfamiliar-code.md.
This document is new or was rewritten from scratch, so there is no
coverage baseline. Review it as original writing.

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       9
  False        1
  python       6

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/11-errors-tracebacks.md
========================================================================

257 lines in the original  ->  386 lines now

SECTIONS  (7 of 10 kept)
------------------------
  DROPPED  Errors
  DROPPED  What is an error? Why are they “thrown”?
  DROPPED  How to Read errors
  ADDED    11. Errors and Tracebacks
  ADDED    What is an error? Why are they "raised"?
  ADDED    `FileNotFoundError` and the `OSError` family
  ADDED    How to Read a Traceback
  ADDED    A Traceback Across Two Files
  ADDED    The Error You Will Catch Most: `ValueError` from `input()`
  ADDED    Raising Your Own Errors

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            1        4
  Callout ({% hint %})              1        3
  Image / diagram                   0        0
  Challenge prompt                  0        2
  Learning objectives               0        0
  Follow-along repo                 0        0

HIDDEN QUESTIONS IN THE ORIGINAL (1)
------------------------------------
  This is a list of system errors commonly-encountered when writing a Node.js program.

HIDDEN QUESTIONS NOW (4)
------------------------
  What actually happens
  This is a list of operating-system errors commonly encountered when writing a Python program.
  What actually happens
  Q: Chapter 7 checked input with `.isdigit()` instead. Why might `try`/`except` be the better tool here?

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  undefined            1  e.g. undefined

CODE FENCE LANGUAGES
--------------------
  (none)       20
  python       18

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/12-first-class-functions-hof.md
========================================================================

297 lines in the original  ->  358 lines now

SECTIONS  (4 of 9 kept)
-----------------------
  DROPPED  Higher-Order Functions and Callbacks
  DROPPED  Functions Stored in Objects are Referred to as "Methods"
  DROPPED  Some Fun Examples
  DROPPED  Array Iterators
  DROPPED  forEach
  ADDED    12. First-Class Functions and Higher-Order Functions
  ADDED    Functions Stored in Dictionaries
  ADDED    Anonymous Functions with `lambda`
  ADDED    Functions That Return Functions
  ADDED    Higher-Order Functions Built Into Python
  ADDED    Looping with Callbacks

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            5        6
  Callout ({% hint %})              1        1
  Image / diagram                   0        0
  Challenge prompt                  0        0
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (5)
------------------------------------
  Answers
  Answer
  Q: Why does an error get thrown? Why is it saying callback is not a function
  Solution
  Solution

HIDDEN QUESTIONS NOW (6)
------------------------
  Answers
  Answer
  Optional: two animations built on `repeat_every`
  Q: Why does an error get raised? Why is it saying `'NoneType' object is not callable`?
  Solution
  Solution

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       18
  python       18

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  'Ada'
  4

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/13-comprehensions-builtin-iteration.md
========================================================================

373 lines in the original  ->  402 lines now

SECTIONS  (2 of 14 kept)
------------------------
  DROPPED  Array Higher Order Methods
  DROPPED  Imperative vs. Declarative Code: Why we use Higher Order Functions
  DROPPED  Array Iterators
  DROPPED  .map(mutate)
  DROPPED  .filter(test)
  DROPPED  .find(test) and .findIndex(test)
  DROPPED  .reduce(accumulate, startingValue)
  DROPPED  .sort(compare)
  DROPPED  Using All Callback Parameters
  DROPPED  Chaining Array Methods
  DROPPED  Generating a Frequency Counter with Reduce
  DROPPED  Nested Arrays
  ADDED    13. Comprehensions and Built-in Iteration
  ADDED    Imperative vs. Declarative Code: Why We Use Built-in Iteration
  ADDED    The Toolkit
  ADDED    Transforming with List Comprehensions
  ADDED    Filtering with an `if`
  ADDED    Finding the First Match
  ADDED    Combining Into One Value
  ADDED    Sorting with `sorted()` and `.sort()`
  ADDED    Combining Steps
  ADDED    Generating a Frequency Counter
  ADDED    Nested Lists
  ADDED    `zip()`, `any()`, and `all()`

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            3        4
  Callout ({% hint %})              1        4
  Image / diagram                   0        0
  Challenge prompt                  1        2
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (3)
------------------------------------
  Solution
  Solution
  Solution

HIDDEN QUESTIONS NOW (4)
------------------------
  Solution
  Solution
  What actually happens
  Solution

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  arrow function       1  e.g. =>

CODE FENCE LANGUAGES
--------------------
  (none)       23
  python       23

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/14-pytest-tdd.md
========================================================================

495 lines in the original  ->  365 lines now

SECTIONS  (14 of 20 kept)
-------------------------
  DROPPED  12. Jest & Test Driven Development
  DROPPED  Jest
  DROPPED  `toEqual` and `.not`
  DROPPED  Refactoring with Confidence
  DROPPED  Adding a New Feature with TDD
  DROPPED  Key Takeaways
  ADDED    14. pytest and Test-Driven Development
  ADDED    pytest
  ADDED    Reading a Failure
  ADDED    `==` vs. `is`

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            8        5  <-- fewer
  Callout ({% hint %})              1        1
  Image / diagram                   1        0  <-- fewer
  Challenge prompt                  0        0
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (8)
------------------------------------
  Q: Imagine you were given this function and asked to verify that it works. How would you test it? What do you expect to happen when testing?
  Solution
  Challenge: Refactor `doubleArrayPurely` to use the higher-order method `map`
  Solution
  Solution
  Challenge: Refactor `deposit` to use the higher-order method `map`
  Solution
  Solution

HIDDEN QUESTIONS NOW (5)
------------------------
  Q: Imagine you were given this function and asked to verify that it works. How would you test it? What do you expect to happen when testing?
  Solution
  Challenge: Refactor `double_all_purely` to use a list comprehension
  Solution
  Solution

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       22
  python       9
  sh           3

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/case-study.md
========================================================================

280 lines in the original  ->  402 lines now

SECTIONS  (16 of 18 kept)
-------------------------
  DROPPED  Arrays and Objects
  DROPPED  Array Higher-Order Methods / Iterator Functions
  ADDED    The Code
  ADDED    Lists and Dictionaries
  ADDED    Built-in Iteration

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            0        1
  Callout ({% hint %})              1        2
  Image / diagram                   0        1
  Challenge prompt                  0        1
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (0)
------------------------------------
  (none)

HIDDEN QUESTIONS NOW (1)
------------------------
  What actually happens

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       6
  python       5
  sh           1

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/15-project-week.md
========================================================================

613 lines in the original  ->  615 lines now

SECTIONS  (26 of 27 kept)
-------------------------
  DROPPED  CLI Projects
  ADDED    Project: CLI Application

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            0        0
  Callout ({% hint %})              0        1
  Image / diagram                   0        0
  Challenge prompt                  0        0
  Learning objectives               0        0
  Follow-along repo                 3        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (0)
------------------------------------
  (none)

HIDDEN QUESTIONS NOW (0)
------------------------
  (none)

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       5
  python       4
  sh           1

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/regex.md
========================================================================

293 lines in the original  ->  275 lines now

SECTIONS  (10 of 13 kept)
-------------------------
  DROPPED  Lecture: Intro to RegEx
  DROPPED  How to Regular Expressions in JavaScript
  DROPPED  `str.match(RegExp)` and the `g` flag
  ADDED    Regex (Optional Friday Reading)
  ADDED    How to Use Regular Expressions in Python

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            0        0
  Callout ({% hint %})              1        1
  Image / diagram                   0        0
  Challenge prompt                  0        0
  Learning objectives               0        0
  Follow-along repo                 1        0  <-- fewer

HIDDEN QUESTIONS IN THE ORIGINAL (0)
------------------------------------
  (none)

HIDDEN QUESTIONS NOW (0)
------------------------
  (none)

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       11
  python       11

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/cheatsheet.md
========================================================================

664 lines in the original  ->  682 lines now

SECTIONS  (15 of 35 kept)
-------------------------
  DROPPED  JavaScript Fundamentals Cheat Sheet
  DROPPED  Node Modules and Testing
  DROPPED  npm and package.json
  DROPPED  Jest Testing
  DROPPED  Arrays
  DROPPED  Array Basics
  DROPPED  Mutating Arrays
  DROPPED  Reference Types and Pure Functions
  DROPPED  Destructuring Arrays
  DROPPED  Objects
  DROPPED  Object Basics
  DROPPED  Modifying Objects
  DROPPED  Iterating Over Objects
  DROPPED  Destructuring Objects
  DROPPED  Array Higher-Order Methods
  DROPPED  map, filter, find, findIndex
  DROPPED  reduce
  DROPPED  sort
  DROPPED  Method Chaining
  DROPPED  Regular Expressions (Bonus)
  ADDED    Python Fundamentals Cheat Sheet
  ADDED    Modules and the Ecosystem
  ADDED    User Input
  ADDED    Files and JSON
  ADDED    venv, pip, and requirements.txt
  ADDED    Lists
  ADDED    List Basics
  ADDED    Mutating Lists
  ADDED    References and Pure Functions
  ADDED    Unpacking
  ADDED    Tuples
  ADDED    Dictionaries
  ADDED    Dictionary Basics
  ADDED    Modifying Dictionaries
  ADDED    Iterating Over Dictionaries
  ADDED    Comprehensions and Built-in Iteration
  ADDED    Comprehensions
  ADDED    Combining
  ADDED    Sorting
  ADDED    Other Built-ins
  ADDED    Testing with pytest
  ADDED    Regular Expressions (Optional)

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            0        0
  Callout ({% hint %})              0        0
  Image / diagram                   0        0
  Challenge prompt                  0        0
  Learning objectives               0        0
  Follow-along repo                 0        0

HIDDEN QUESTIONS IN THE ORIGINAL (0)
------------------------------------
  (none)

HIDDEN QUESTIONS NOW (0)
------------------------
  (none)

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)       41
  python       39
  sh           2

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

========================================================================
CONVERSION REPORT  mod-1-python-fundamentals/Overview.md
========================================================================

19 lines in the original  ->  27 lines now

SECTIONS  (1 of 2 kept)
-----------------------
  DROPPED  Mod 1 - JavaScriptFundamentals
  ADDED    Mod 1 - Python Fundamentals

  Each DROPPED line is a concept that was in the original and is not
  in a same-named section now. It may have moved into another section,
  been merged, or been deliberately cut — say which, for each one.

PEDAGOGICAL DEVICES  (placement ignored)
---------------------------------------
  device                     original      now
  Hidden Q&A (<details>)            0        0
  Callout ({% hint %})              0        0
  Image / diagram                   0        0
  Challenge prompt                  0        0
  Learning objectives               0        0
  Follow-along repo                 0        0

HIDDEN QUESTIONS IN THE ORIGINAL (0)
------------------------------------
  (none)

HIDDEN QUESTIONS NOW (0)
------------------------
  (none)

JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)
----------------------------------------------------
  (none)

CODE FENCE LANGUAGES
--------------------
  (none)

BROKEN LOCAL LINKS AND IMAGES
-----------------------------
  (none)

