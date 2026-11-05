# Coding Assignments Guide

**Table of Contents:**

- [What is a Coding Assignment?](#what-is-a-coding-assignment)
  - [Tips for Working on Coding Assignments](#tips-for-working-on-coding-assignments)
- [Coding Assignment Setup](#coding-assignment-setup)
- [pytest and Testing](#pytest-and-testing)
- [Scoring on Coding Assignments](#scoring-on-coding-assignments)
- [Feedback on Coding Assignments](#feedback-on-coding-assignments)
- [Using AI on Coding Assignments](#using-ai-on-coding-assignments)

## What is a Coding Assignment?

Software Engineering coding assignments are opportunities for you to practice the skills learned in your Software Engineering fellowship at The Marcy Lab School. In these assignments, you can expect to:

- Create code from scratch
- Modify existing code
- Debug broken code

Coding assignments have a `src` directory where you will be writing your code. They also have a `tests` directory with test files whose names start with `test_`. Those files test your code automatically each time you run them.

To set up, submit, and resubmit a coding assignment, follow the steps in [How to Work on Assignments](working-with-assignments.md). This guide covers everything that is specific to coding assignments.

### Tips for Working on Coding Assignments

As you work on your coding assignment, you may be tempted to jump right in and start coding. However, it is often best to slow down and plan out your approach first. Look at the problem and make sure you understand fully what it is asking you to do. At Marcy, we recommend that you use the PEDAC approach ([read more about PEDAC here](how-to-pedac.md)).

You may get stuck along the way, which can always be frustrating. Debugging is an essential skill but it's hard to know where to start sometimes. That's why we love the "rubber duck" approach ([read more about debugging with the rubber duck approach here](how-to-debug.md)).

## Coding Assignment Setup

The tests in a coding assignment need a package called `pytest`, which is not part of Python itself. Each assignment installs `pytest` into a **virtual environment**: a `.venv` folder inside the repository that holds the packages for that one project, so that each assignment's packages stay separate from every other assignment's. You will learn more about virtual environments in [lesson 1.9](../mod-1-python-fundamentals/9-modules-environments-pytest.md), but for now you only need to run these commands from inside your repository after you clone it:

```sh
# create a virtual environment folder .venv
python3 -m venv .venv
# turn the virtual environment on
source .venv/bin/activate
# install required packages
pip install -r requirements.txt
# run the tests
pytest
```

These commands install `pytest` and then show you all the tests you need to work on. We may explain each function in the `README.md`, but always run the tests because they are crucial to explaining what the code literally must do.

A virtual environment stays on only in the terminal where you turned it on. Each time you open a new terminal to work on the assignment, run `source .venv/bin/activate` again from inside the repository. If the terminal reports `command not found: pytest`, the virtual environment is off.

## pytest and Testing

Tests are an essential part of professional software development. Without testing our code, we run the risk of deploying code with unexpected bugs. With testing, we are forced to think critically about how we expect our program to behave and then write our code to satisfy those tests. This process of first writing tests and then writing code to satisfy those tests is called **Test-Driven Development (TDD)**.

At Marcy, we use [pytest](https://docs.pytest.org/) to write automated tests for coding assignments. Automated tests are Python files that:

1. Import functions from source code
2. Run those functions with various inputs
3. Compare the returned values against the expected values.

A pytest test file has a name that starts with `test_`, and each test inside it is a function whose name also starts with `test_`. Each `assert` statement in a test checks that a comparison is `True`, and the test fails at the first `assert` that is `False`. Here is a test from a coding assignment:

{% code title="tests/test_from_scratch.py" lineNumbers="true" %}

```python
# Import the function to be tested
from from_scratch import calculate_area


# Test the calculate_area function with a series of assertions
def test_calculate_area():
    """calculate_area - returns width times height"""
    # Translation: We expect calculate_area(5, 3) to return 15
    assert calculate_area(5, 3) == 15
    assert calculate_area(10, 7) == 70
    assert calculate_area(1, 1) == 1

    # It is useful to think about what should be returned for edge cases, like a width of 0.
    assert calculate_area(0, 9) == 0


# ...more tests
```

{% endcode %}

Each assignment will have automated test files in the `tests` directory. They will show you exactly how we expect your functions to behave. **DO NOT MODIFY THE TESTS**.

To run these automated tests, use the command:

```sh
pytest                    # run all of the tests
# or
pytest -k calculate_area  # run only the tests whose names include "calculate_area"
```

After running this command, you will see output like the following. Before you write any code, nearly every test fails. The output below is shortened, and each `...` marks lines that were left out.

```
============================= test session starts ==============================
collected 17 items

tests/test_debug.py::test_describe_mood_output FAILED                    [  5%]
tests/test_debug.py::test_describe_mood_uses_f_strings FAILED            [ 11%]
tests/test_from_scratch.py::test_calculate_area FAILED                   [ 17%]
tests/test_from_scratch.py::test_is_even FAILED                          [ 23%]
...

=================================== FAILURES ===================================
...
_____________________________ test_calculate_area ______________________________

    def test_calculate_area():
        """calculate_area - returns width times height"""
>       assert calculate_area(5, 3) == 15
E       assert None == 15
E        +  where None = calculate_area(5, 3)

tests/test_from_scratch.py:17: AssertionError
...
=========================== short test summary info ============================
FAILED tests/test_from_scratch.py::test_calculate_area - assert None == 15
...
========================= 16 failed, 1 passed in 0.03s =========================
```

The test output provides some really useful information.

- We can see which tests failed, listed by file and test name (`tests/test_from_scratch.py::test_calculate_area`).
- For each failing test, the `>` symbol marks the `assert` statement that failed.
- We can see what our function actually returned and what the test expected. `assert None == 15` means that our function returned `None` and the test expected `15`, and the `+  where` line beneath it names the call that returned `None`: `calculate_area(5, 3)`. A function that reaches its end without a `return` statement returns `None`, so every function that has not been written yet fails this way.

Armed with this information, we can more confidently build our functions knowing that we have a specific set of targets to aim for. Automated tests allow us to repeatedly run our code against the same set of tests until all expectations are met.

All assignments will also come with a `src/playground.py` file that you can use to manually test your code as you develop. Nothing in `playground.py` is graded, and you run it with `python3 src/playground.py`. We recommend the following workflow:

1. Run the automated tests to see what you are aiming for.
2. Copy the function you are currently working on into the `playground.py` file and use the test cases to manually test your code
3. Once you are satisfied, copy your function back into the original file and run the automated tests again.
4. If anything fails, return to the `playground.py` file to make adjustments.
5. Repeat.

## Scoring on Coding Assignments

Each question in a coding assignment is scored out of 3 points. Your grader decides each question's score from two sources: the tests, which show whether your function returns the right values, and your code itself, which shows whether the logic behind those values is correct and whether your names describe what they hold.

| Score                      | What the code looks like                                                                                                                                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **3 - All Tests Pass**     | Every test for the question passes. The logic is correct throughout, the approach solves the problem efficiently, the variable names describe what they hold, and the code has no syntax errors.                            |
| **2 - Almost There**       | The approach is right, and one small fix would make every test pass. That fix might be an argument in the wrong order, an off-by-one error, a missing check for an edge case, or one or two syntax errors or unclear names. |
| **1 - Significant Issues** | The code shows some understanding of the problem but needs more than one fix: several implementation errors, the wrong approach or tool for the problem, or many syntax errors or unclear names.                            |
| **0 - Does Not Work**      | The code produces no solution or a solution that is far from correct, or the question has no attempt or no recognizable approach.                                                                                           |

These rules decide the score where two bands meet:

- A function with the right name, the right parameters, and a `return` statement earns at least 1 point, however many mistakes it holds.
- Correct logic in the wrong file, or output in the wrong format (such as the wrong letter case or an extra word), earns 2 points, because one small fix makes the tests pass.
- A mistake repeated across several branches or functions, such as returning a string in every branch where a boolean belongs, counts once.
- Commented-out code never costs points. Code that runs but that nothing uses, such as a variable that is never read, costs points only when it changes what the program does or goes against what the question asks for.

{% hint style="info" %}
Your assignment score is the total of your question scores. In order for a coding assignment to be marked as "Complete", you must score at least 75% of the possible points.

For example, an assignment with 8 questions has a total possible score of 24. You must score at least 18 on that assignment.

Assignments below 75% must be revised and [resubmitted](working-with-assignments.md#resubmitting-an-assignment).
{% endhint %}

## Feedback on Coding Assignments

Only the criteria in the scoring table above change your score. To support you in your growth as a software engineer, your instructor may also provide feedback on any of the following areas (expand each category to see more details):

**<details><summary>Code Quality</summary>**

- Adherence to coding standards and conventions (e.g., PEP 8 conventions such as `snake_case` names)
- Use of proper naming conventions (variables, functions)
- Avoidance of code duplication
- Clear and concise comments

</details>

**<details><summary>Functionality</summary>**

- Does the code meet the project requirements?
- Does it pass all tests, both automated and edge cases?
- Correctness of input/output handling

</details>

**<details><summary>Modularity and Reusability</summary>**

- Proper use of functions or classes
- Modular and reusable code (avoiding large, monolithic functions)
- Clear separation of logic

</details>

**<details><summary>Version Control Practices</summary>**

- Meaningful commit messages
- Consistent use of branches
- Proper use of pull requests and code reviews

</details>

**<details><summary>Code Structure and Organization</summary>**

- File structure
- Separation of concerns
- Readability and logical flow

</details>

**<details><summary>Error Handling</summary>**

- Proper use of `try` and `except` blocks
- Graceful handling of unexpected inputs or states
- Meaningful error messages

</details>

**<details><summary>Efficiency and Performance</summary>**

- Time and space complexity
- Use of appropriate data structures and algorithms
- Avoidance of unnecessary computations

</details>

## Using AI on Coding Assignments

On a coding assignment, you use AI in one of the two modes described in the [AI Policy](../guidelines-and-policies/ai-policy.md): Tutor mode or Implementer mode. The **AI Use on This Assignment** section of each assignment's `README.md` says which modes that assignment allows, so read it before you start.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you write every line of code you submit. Ask it what a piece of syntax does, have it walk you through an error message, or have it quiz you on code you wrote until you can predict what that code will do. Do not ask it for the function, and do not copy its code into your file. Paste this at the start of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question is asking, clarify confusing wording, and highlight the relevant concepts I need to know — but do not provide the full solution or code that directly answers the question. Instead, rephrase the problem in simpler terms, identify what is being tested, and suggest what steps or thought processes might help. Ask me guiding questions to make sure I am thinking critically. Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from that specification, and then you verify the code line by line. Your specification gives each function's inputs, its return value, and at least one example. If the code that comes back does more than you asked for, reject it: over-delivery is a defect, and catching it is part of the job. Implementer mode is for concepts you already understand. If you still need the AI to tell you whether its own code is correct, stay in Tutor mode.

You own every line either way, and you will be asked to explain it.

Your editor's inline AI suggestions put code in your file before you have decided what it should be, so the AI Policy counts accepting one as generation. In Tutor mode, turn them off by following the [AI Policy's autocomplete instructions](../guidelines-and-policies/ai-policy.md#can-i-use-autocomplete).
