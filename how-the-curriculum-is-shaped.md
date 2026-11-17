# How the Python Curriculum Is Shaped

These are the judgment rules behind the Python curriculum: its lessons, assignments, case studies and short responses. Apply them when writing or reviewing any of those. The source is the Claude Docs page "How the Python Curriculum Is Shaped" (https://claude.ai/artifact/YRG29xTk8bwmYQsbLw3jwq), copied here so that every session loads it; when the two disagree, update this file.

## The question behind almost every decision

Nearly every decision about this curriculum comes back to one question: **what does a fellow need at this point, knowing only what came before it, and what would they wrongly believe or do without it?** Fellows are learning Python as their first programming language. They cannot fill gaps from experience, they cannot compare Python with anything, and they take the examples literally. Every principle below applies that one question.

## Sequencing: when an idea appears

**An idea appears when a problem in visible code needs it.** Every section opens with something going wrong in code that runs, and the new idea is the fix. The test for a lesson is: "Is there a clear problem that motivates everything new being introduced?" For example, lesson 2.3 was rebuilt around the code from 2.1, where `seats_sold` was set by hand and the class's rules were skipped. Properties then fix a bug that fellows have already watched happen.

**The limit of one idea motivates the next.** Group tools by the job they do, not by the kind of syntax. Lesson 2.5 is a chain of problems:

- An `isinstance()` chain has to be repeated in every function, so the methods move into each class, which is polymorphism.
- A class written by another team cannot inherit from `Event`, which calls for duck typing.
- A method that duck typing relies on may be missing, and nobody finds out until the code calls it.
- So the lesson ends with abstract base classes, which refuse an incomplete class as soon as an object is created.

**Place an idea where its definition needs it.** Closures moved from 2.7 into 2.6 for two reasons. The callbacks in 2.6 already close over variables, as `upcoming_events()` does with `today`. And 2.6 defines a higher-order function as one that takes *or returns* a function. Moving closures left 2.7 to teach decorators alone.

**Never rely on an idea before it has been taught, and check what fellows know at that point.** When a draft check used a pytest fixture, the question was "Do students know what a fixture is at this point?" They did not, so the checks rebuild their objects inside each test, and fixtures moved to the case study session.

**Teach Python the Python way, not in the order inherited from JavaScript.** The scope and sequence was ported from a JavaScript curriculum, so many of its groupings carry JavaScript's reasons. For each grouping, ask what reason it has in Python. Lesson 2.1 opens with `'hello'.upper()` being the same call as `str.upper('hello')`. Lesson 2.4 teaches attribute lookup rather than naming the method resolution order. Check each topic against PEP 8 and the Google Python Style Guide, and say where the two disagree.

**Spread the load across sessions, but accept a long lesson when splitting it would break an idea apart.** Class attributes moved from 2.3 to 2.4, because 2.3 was overloaded and 2.4 was light. In 2.6, both `lambda` and `sorted()` stayed and the lesson stayed long, because moving `lambda` to Advanced Topics would have separated it from the callbacks it serves.

**Read the assignment before planning its lesson.** The assignment shows what fellows will actually be asked to do, and a lesson planned without it can teach less than the assignment needs. Assignment 2-1 needs `__init__`, `__repr__`, and composition, and that need decided where `__init__` belongs.

## Keeping and cutting

**For anything doubtful, ask "If we remove it, what do we lose?"** Three examples:

- A section on assigning to a class attribute was cut, because it taught the fix for a mistake that fellows rarely make.
- The refund deadline challenge in 2.5 was cut, because the sections before it had already solved the same problem in the same setting.
- The "Writing Down the Contract" section was merged into "Abstract Base Classes", because both sections opened with the same problem.

**Present the alternative to what is being taught.** An idea becomes clear once the fellow can see what it replaces. Duck typing was not clear until the lesson set it beside checking the class with `isinstance()`. That check asks "What is this object's class?", while duck typing asks "Can this object perform the action I need?"

**Block a false generalization in the same place as the example that invites it.** The lesson shows that `append` lives in `list.__dict__`, not on the list itself. A sentence beside that example adds that instances of built-in types have no `__dict__` of their own. Without that sentence, fellows could conclude that no instance can store attributes, which is false.

**Teach what working programmers do.** The question "What is the case for non-public methods in production code? Is it worth teaching?" decides whether a topic belongs, and the answer depends on whether professionals use it. The Google style guide says never to use `staticmethod`, so fellows learn to read `@classmethod` and `@staticmethod` in other people's code but never write them.

**Surprises go in Advanced Topics, not in checks.** A "Predict, then run" box confirms what the section just taught, using an ordinary case, and tests one idea per box. A surprising behaviour belongs at the end of the lesson.

**Drop trap questions.** The questions in an assignment repository are a bank, and the lead instructor chooses which ones reach fellows. A question that tests whether a fellow spots a trick, rather than whether they can apply the lesson, gets dropped. Every question in the bank must still be accurate, because any of them may be chosen.

## The shape of a lesson

Every lesson follows the same outline, so a fellow always knows where the problem, the new idea, and the practice will be.

1. **Opening:** a prose opening, then Key Terms.
2. **Sections**, each with three parts:
    - **The Problem** says what goes wrong, and for whom.
    - **New Concepts** has one bullet per idea, with each new term in bold.
    - **Code** runs, with its outputs written in comments.
3. **Devices**, with a check every few sections:
    - "Predict, then run" boxes;
    - checks for understanding written as near transfer, meaning different classes that cover the same range of cases (the restaurant check in 2.4 is an example);
    - hidden `Q:` questions;
    - challenges as `###` headings, each with a solution;
    - questions about the real case study code.
4. **Ending:** Advanced Topics, then a Summary of the lesson's one idea.

**Keep one running example consistent.** The venue's events appear in every Module 2 lesson, with the same dates, names, and output format. A before version and an after version of the code should differ only in the idea being taught. For example, the polymorphism loop in 2.5 matches the `isinstance()` loop line for line, refund marker included, so the only change a fellow sees is `ticket_price(event)` becoming `event.ticket_price()`.

**Divide the labour.** Claude drafts the structure and writes every device in full, with each output checked by running the code. The curriculum lead writes the explanatory prose.

## Assignments, case studies, and short responses

**The case study** reviews what fellows already know, and it deliberately shows them code they have not learned yet. Repeated exposure makes that code familiar before the lesson that teaches it. The case study is never described as "assessed", and its questions never include hidden answers. In Module 2, the case study session reviews the module through its tests.

**Assignments** are written so that fellows can skim them before reading the lessons:

- A "Before You Start" section lists the ideas to look for.
- Each question opens with facts about the domain, never with a motivation built on imagined code.
- Refusals get tests. In assignment 2-1, fellows test that a station refuses a duplicate bike and refuses a bike when it is full.

**Short responses** use a scenario the lesson never shows, so that a fellow has to transfer the idea rather than repeat the lesson. Their answer keys read like a beginning fellow's answer that is still accurate and complete, because instructors grade fellows against the key and a key written in expert language sets a standard no fellow can reach.

## Language

**Question unusual phrasing.** A draft described attributes as "the names that `jazz` answers to". That phrasing is not how programmers talk about attributes, so a fellow who learned it would not recognize the idea in documentation or in conversation. It was replaced everywhere.

**Do not give Python feelings or intentions.** Python does not "care" about types. `len()` calls `__len__` without checking the argument's type, and duck typing follows from how the shared method names were designed.

**Leave out two kinds of reference:**

- comparisons with other languages, because fellows have no other language to compare against;
- references to earlier chapters by number, because fellows may not remember the earlier example, and chapters get reordered.

**Use your own confusion as evidence.** If the author keeps forgetting the order of constructor arguments, a beginner will too. That is why every number in an event call is labeled, as in `capacity=40`.

**Follow the written rules** in the repository's root `CLAUDE.md`. Learning objectives use the ABCD approach and Bloom verbs. Explanations state the problem before the solution, state the consequence rather than only a judgment, and name the subject of every sentence.

## Working habits

- **Read drafts line by line, and verify individual lines.** A question such as "Is this right?" about one code comment gets answered by running the code, not by reassurance.
- **Ask for a review of your own edits** before committing them.
- **Decide the scope of a change, then apply it everywhere.** The keyword-argument change covered about 120 calls in seven lessons, plus the case study and the lecture code, so that no file teaches the old style.
- **Expect pushback, and ask for a recommendation rather than a list of options.**
- **Record each settled decision where future work will find it:** the `CLAUDE.md` files, `scope-and-sequence.md`, or `conversion-decisions.md`.
- **Commit one reviewed lesson at a time.**
- **Settle the module objectives document first.** Each module's `scope-and-sequence.md` shows in two pages whether the module teaches the right things in the right order, so it is reviewed before any chapter.

## Knowledge the role needs

- **Python, deep enough to know which explanation is true.** This covers the data model, attribute lookup, `type` as a metaclass, closures, decorators, abstract base classes, and pytest.
- **Teaching methods:** Bloom's taxonomy and ABCD objectives; SOLO levels for exit tickets; prediction before execution; near transfer; and spaced exposure through the case study.
- **The program:** 90-minute lectures on Monday, Wednesday, Thursday and Friday; two lessons per assignment; fellows use AI in tutor mode only during Q1; and decorators must come before Q2's Flask unit, because Flask routes are written with `@app.route("/")`.
- **The tooling:** GitBook breaks heading anchors that contain `&`, and renders unescaped dunder names in Mermaid diagrams as bold. The scripts `update-toc.py`, `sync-key-terms.py`, and `conversion-report.py` do the housekeeping, and the repositories' layout is described in each `CLAUDE.md`.

The judgement that no file records is the hardest part to hand over: how common a mistake must be before it earns a section, or when a lesson has become too long. The quickest way to pass that judgement on is to review one lesson together, with this document open.
