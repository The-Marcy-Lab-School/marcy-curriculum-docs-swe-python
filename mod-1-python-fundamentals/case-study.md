# Case Study: CLI Task Manager

{% hint style="info" %}
Find the code for this case study from the [GitHub Repository](https://github.com/The-Marcy-Lab-School/swe-casestudy-1-cli-task-manager).

Clone it then follow the **Setup** steps listed in the README.
{% endhint %}

**Table of Contents:**

- [Key Features and Usage Example](#key-features-and-usage-example)
- [Key Technologies and Packages](#key-technologies-and-packages)
- [Setup](#setup)
- [The Code](#the-code)
  - [Orient Yourself First](#orient-yourself-first)
- [Investigation Questions](#investigation-questions)
  - [User Interface Design](#user-interface-design)
  - [Data Types](#data-types)
  - [Variables and Scope](#variables-and-scope)
  - [Functions](#functions)
  - [Conditional Logic](#conditional-logic)
  - [Looping and Iteration](#looping-and-iteration)
  - [Lists and Dictionaries](#lists-and-dictionaries)
  - [Modules](#modules)
  - [Reading Unfamiliar Code](#reading-unfamiliar-code)
  - [Error Handling and Debugging](#error-handling-and-debugging)
  - [Higher-Order Functions](#higher-order-functions)
  - [Comprehensions and Built-in Iteration](#comprehensions-and-built-in-iteration)
  - [Test-Driven Development](#test-driven-development)
  - [Code Style](#code-style)
- [Extension Opportunities](#extension-opportunities)
  - [Tips](#tips)

This project is a simple command-line task manager where users can add, view, and complete tasks. The application stores tasks in a list of dictionaries, gives users options through prompts, and uses loops and list operations to handle interactions with tasks.

## Key Features and Usage Example

After running the application, the user is presented with a menu of options. They can:

1. Add a new task to their list of tasks
2. Mark a task as completed
3. Delete all tasks from the list
4. Exit the application.

In the screenshot below, you can see a user selecting the "Add Task" option and entering a task description "Return online order".

![The task manager shows the menu, the current tasks, and the prompt for a new task](img/task-manager-screenshot.png)

## Key Technologies and Packages

- Python
- `input()` and `print()` from the built-in functions
- The `os` module from the standard library
- The `pytest` testing library

## Setup

Follow the steps listed in the repository's README

## The Code

The application is three files in a `src` folder with accompanying tests in a `tests/` folder

The app has three modules:

- **`tasks.py`** holds the list of tasks data and functions for manipulating the tasks list.
- **`menu.py`** holds the functions for managing the menu user interface.
- **`main.py`** is the entry point.

### Orient Yourself First

Before you answer any of the investigation questions, read the program to the best of your ability. The first time you do this, you will likely be mostly confused. That's okay, write down what you understand and what you are guessing. Each time you come back to this application, you can go through this process to gauge how well you understand how the application works.

1. **Run it.** Run `python3 src/main.py` from the project folder and use every menu option. Give it bad input as well: a letter where a number belongs, a task number that does not exist, an empty description. Then write one sentence, from the user's point of view, saying what the program does.
2. **Find the entry point and map the files.** For each file in `src/`, read only the `import` lines and the `def` lines, and write one sentence saying what that file is for. Note which file imports which.
3. **Find the data.** Find every variable that lives at the top level of a file, and write down its shape.
4. **Trace one action.** Follow Add Task from the `if __name__ == "__main__":` guard in `main.py` to the confirmation message, and list every function it passes through, in order. If you lose your place, add a `print()` as the first line of each function you think the action passes through, run Add Task again, and read the order the messages appear in. Delete those `print()` lines when you are done.
5. **Predict, then run.** Choose one function in `tasks.py` and predict what it prints for one specific input. For example, predict what `add_task('')` prints. Then check: from the `src` folder, start the REPL with `python3` and run `from tasks import add_task` followed by `add_task('')`.
6. **Write down what you know and what you are guessing.** Keep two lists. Move an item from "guessing" to "know" only after you have checked it by running code.

## Investigation Questions

By answering these questions, you will be required to think critically about how the application is designed and understand WHY it is designed in this way. Your aim should be to:

- learn as much as you can from this application so that you can build an application of your own that leverages these same skills
- communicate clearly about the concepts you are using and the decisions you make for how you implement them.

### User Interface Design

The user interface is how humans interact with our programs. Even in a simple command-line application, thoughtful design choices can make the difference between a frustrating or confusing experience and one that feels intuitive and pleasant to use.

**Question 1** Look at the menu display in `show_menu()`. The menu shows numbered options (1, 2, 3, 4) and asks the user to "Choose an option (1-4)". Why do you think the menu uses numbers for the options? What are the benefits of using numbers? What are potential downsides of having the user type out in words what they would like to do? For example: "Choose an option: add a task, complete a task, clear all tasks, exit".

**Question 2** In the `view_tasks()` function, tasks are displayed with checkboxes: `[x]` for completed tasks and `[ ]` for incomplete tasks. Do you think this visual representation is easy to understand? What alternative ways of displaying this information can you think of? Propose at least one alternative display option.

**Question 3** Look at the `os.system('clear')` call at the end of the `while` loop in `show_menu()`. It occurs after a final `input()` for the user to press Enter and clears the terminal output on each loop. How would the user experience change if we didn't clear the screen? How would it change if we removed the `input()` that comes right before it?

_Tip: Remove the code and re-run the program to see how it changes._

**Question 4** When a user completes a task, the program shows a message like `Task "walk the dog" marked as completed!`. Why is it important that the user sees these messages? How would the user experience change without these messages?

### Data Types

Whether you are designing a new application or learning about an existing one, we always start by asking: _how is the data represented_? Once we know how to represent the data, we are better able to design how the application uses and manipulates it.

**Question 1**

Go to the `tasks.py` file and look at the `tasks` variable. It is a list of dictionaries. Each dictionary represents a task in the list. Each task has a `description` string and an `is_complete` boolean. For the `is_complete` value, we could also have represented it with the numbers: `"is_complete": 0` (incomplete) and `"is_complete": 1` (complete); or as strings `"is_complete": "complete"` and `"is_complete": "incomplete"`. If it were up to you, which would you choose to represent `is_complete` and why? Incorporate how the `is_complete` value is used throughout the program into your answer.

{% hint style="warning" %}
**Predict, then run.** In `tasks.py`, change the sample tasks' `True` to `"complete"` and their `False` to `"incomplete"`. Run the app. Which checkbox appears beside each task? Find the line in `view_tasks()` that decides, and explain the result. Undo the change when you are done.
{% endhint %}

**Question 2**

In `show_menu()`, the user's menu choice is compared with strings, as in `if menu_choice == '1':`, while the task number in Question 3 is converted with `int()` before it is used. What data type does `input()` return? Why does the menu compare `menu_choice` with `'1'` rather than converting it to an integer first?

{% hint style="warning" %}
**Predict, then run.** In `show_menu()`, change `if menu_choice == '1':` to `if menu_choice == 1:`. Run the app and choose `1`. What appears? Explain why. Undo the change when you are done.
{% endhint %}

**Question 3**

In `menu.py`, the user's chosen task number `task_choice` is converted to a number using the `int()` conversion function. Why is this code necessary? What happens if this type conversion is removed?

{% hint style="warning" %}
**Predict, then run.** In `menu.py`, change `int(task_choice) - 1` to `task_choice - 1`. Run the app, choose Complete Task, and enter `2`. What is the last line of the error message? The line you changed is inside a `try`. Explain why the `except` did or did not handle the error. Undo the change when you are done.
{% endhint %}

### Variables and Scope

Understanding where variables are declared (their **scope**) and therefore where they can be reached is crucial for building well-structured applications. In this CLI Task Manager, we can see variables declared in different locations that serve different purposes.

**Question 1**

In the `show_menu()` function in `menu.py`, the variable `is_running` is assigned `True` before the loop and reassigned to `False` inside it. The `tasks` list in `tasks.py`, by contrast, is never reassigned, and yet its contents change constantly. What is the difference between these two kinds of change? Why can `clear_tasks()` empty the list with `tasks.clear()`, when writing `tasks = []` inside that function would not empty it?

_Hint: research the difference between mutation of lists and reassignment._

**Question 2**

In the `show_menu()` function in `menu.py`, take a look at the `task_choice` and `task_index` variables. Consider that we could have also written the code without any variables, and it would still complete tasks:

```python
try:
    complete_task(int(input('Enter task number to complete: ').strip()) - 1)
except ValueError:
    print('That is not a number.')
```

This version's `except` prints a different message from the one in `menu.py`. Why couldn't it keep the original message? What are the tradeoffs of these approaches? What does that tell you more broadly about when, how, and why you use variables?

**Question 3**

Look at the `tasks` list in `tasks.py`. What is the scope of the `tasks` variable? What would happen if we moved the `tasks = []` line inside one of the functions? Why would this break the application?

{% hint style="warning" %}
**Predict, then run.** In `tasks.py`, delete the whole `tasks = [...]` assignment at the top of the file, and add the line `tasks = []` as the first line of `add_task()`. Run the app. At what moment does it fail, and what is the last line of the error message? Undo the change when you are done.
{% endhint %}

### Functions

Functions are the building blocks of reusable code. They allow us to break down complex problems into smaller, manageable pieces and avoid repeating the same code multiple times. Good function design and modular organization make code easier to understand, test, and maintain.

**Question 1**

The task list numbers tasks from 1, but `complete_task()` expects an index that starts at 0. The `- 1` that converts one to the other is in `menu.py`. Suppose `complete_task()` took the number the user typed and did the subtraction itself. What would change in `menu.py`, in `tasks.py`, and in `tests/test_tasks.py`? Which version would you choose, and why?

**Question 2**

What if the programmer had written all the task logic directly in `menu.py` instead of creating separate functions? For example, look at the code inside `clear_tasks()` — imagine copying all of that code and pasting it directly where `clear_tasks()` is called.

```python
elif menu_choice == '3':
    tasks.clear()
    print('All tasks cleared!')
```

Would this code even work? Assuming you could get it to work, what are the downsides of doing this for potentially all of the tasks-related functions?

**Question 3**

What if we combined all the task-related functions (`add_task`, `complete_task`, `view_tasks`, `clear_tasks`) into one giant function called `handle_task_operations()`? What parameters would you need to include in order for it to work with all task-related operations?

### Conditional Logic

Conditional Statements enable programs to behave differently depending on the state of the program. Without them, a program would run the exact same way every time!

**Question 1**

In `menu.py`, the `show_menu()` function uses `if/elif` statements to handle different menu choices. What would happen if we used separate `if` statements instead of `elif`? Try to think through what would happen if a user entered "1" as their menu choice.

{% hint style="warning" %}
**Predict, then run.** In `show_menu()`, change each `elif menu_choice` to `if menu_choice`. Run the app, choose `1`, and add a task. What appears after the confirmation message? Undo the change when you are done.
{% endhint %}

**Question 2**

Look at the `add_task()` function in `tasks.py`. The first few lines check `if not description:` and return early if no description is provided. This is called a "guard clause." What would happen if we removed this guard clause and a user tried to add a task with no description?

**Question 3**

Look at the `view_tasks()` function. It checks `if len(tasks) == 0:` before displaying tasks. Why is it there? What would happen if we removed this check and tried to display an empty task list?

{% hint style="warning" %}
**Predict, then run.** Delete the `if len(tasks) == 0:` check and the two lines inside it from `view_tasks()`. Run the app, choose Clear All Tasks, and press Enter. What does the task list show now? Undo the change when you are done.
{% endhint %}

### Looping and Iteration

Loops take repetitive tasks and boil them down to a process that can be repeated without having to type the same code multiple times. Choosing the right type of loop and ensuring it terminates properly are crucial skills for any programmer.

**Question 1**

Look at the `show_menu()` function in `menu.py`. There's a `while is_running:` loop that keeps the menu running until the user chooses to exit. What would happen if we forgot to set `is_running = False` when the user chooses option 4 (Exit)? What would happen if we instead forgot the `is_running = True` line before the loop?

{% hint style="warning" %}
**Predict, then run.** Delete the line `is_running = True` from `show_menu()`. Run the app. What is the last line of the error message? Explain what each part of that message is telling you. Undo the change when you are done.
{% endhint %}

**Question 2**

The `while` loop in `show_menu()` has a condition `while is_running:`. This means the loop will continue as long as `is_running` is `True`. What would happen if we changed the condition to `while True:` and removed the `is_running` variable entirely? How else could we break out of the loop?

**Question 3**

Why is a `while` loop the appropriate type of loop to use to display the menu (see `show_menu` in `menu.py`) as opposed to a `for` loop? Conversely, why is a `for` loop the appropriate type of loop to use to display the list of tasks (see `view_tasks` in `tasks.py`)?

**Question 4**

Find the `for` loop in the `view_tasks` function in `tasks.py`. Then look up the `enumerate` builtin function. How would you refactor (rewrite) the `for` loop to use `enumerate` instead?

**Question 5**

In `view_tasks()`, the number printed beside each task is `i + 1`. Why does it add 1 to `i` rather than print `i` itself?

{% hint style="warning" %}
**Predict, then run.** In `view_tasks()`, change `{i + 1}` to `{i}`. Run the app, choose Complete Task, and type the number shown beside "Answer investigation questions". Which task does the confirmation message name? Undo the change when you are done.
{% endhint %}

### Lists and Dictionaries

Lists and dictionaries are the two most common options we have for creating collections of data. Lists are a great choice for grouping together lists of similar values while dictionaries are a great way to represent a single thing that has many data points related to it.

**Question 1**

The entire collection of `tasks` is represented as a list of task dictionaries. Each task dictionary is represented with keys `"description"` and `"is_complete"`. Suppose we instead represented the tasks as a list of strings, such as `['walk the dog', 'take out the trash']`. What are the tradeoffs between a list of dictionaries and a list of strings?

**Question 2**

In `complete_task()`, the function gets a task with `task = tasks[task_index]` and then sets `task["is_complete"] = True`. The function never assigns anything into `tasks`, yet the task list shows the change. How? In your answer, say which of those two lines is an assignment and which is a mutation, and what each one does to the dictionary stored in `tasks`.

### Modules

A module is a file containing code, which can then be imported and utilized in other parts of a larger program or system. Rather than writing all of our code in one file, this project splits the code into three modules: `main.py`, `menu.py`, and `tasks.py`. As a result, we achieve "separation of concerns".

**Question 1**

Look at the top of `menu.py`. You'll see `add_task` is imported. What would happen if we tried to call `add_task()` in `menu.py` without this import statement? Why do we need to explicitly import these functions?

**Question 2**

In `menu.py`, look at the import line: `from tasks import add_task, view_tasks, complete_task, clear_tasks`. Notice that the `tasks` list itself isn't imported, even though Python would allow `from tasks import tasks`. This means that the `menu.py` file can't access it directly. Why do you think the programmer chose to leave `tasks` out of the import?

**Question 3**

If we wanted to add a new feature to the application, giving the user the option to mark all items as complete, how would you split up the code amongst the modules to implement this feature?

**Question 4**

`main.py` ends with `if __name__ == "__main__":`. `menu.py` and `tasks.py` do not have this line. Why does only one of the three files need it?

### Reading Unfamiliar Code

You read this whole application with the method from chapter 1.10 before you started these questions. Code that a model wrote deserves the same method with more suspicion, because it looks just as confident when it is wrong as when it is right.

**Question 1**

A model was asked to write a `delete_task()` function for the Delete Task extension, and it produced this:

```python
def delete_task(task_index):
    """Remove one task from the list by its index."""
    if task_index < 0 or task_index > len(tasks):
        print('Invalid task number.')
        return

    task = tasks.pop(task_index)
    print(f'Task "{task["description"]}" deleted!')
```

Compare it line by line with `complete_task()`. Then write a bug report for it: a concrete input, the actual output, the expected output, and where the problem is.

{% hint style="warning" %}
**Predict, then run.** Paste the function at the bottom of `tasks.py`. From the `src` folder, start the REPL with `python3`, then run `from tasks import delete_task` followed by `delete_task(2)`. The list starts with the two sample tasks. What happens? Delete the function from `tasks.py` when you are done, because the AI policy keeps code a model wrote out of your own work.
{% endhint %}

### Error Handling and Debugging

Real-world applications must handle unexpected situations gracefully. Understanding how to anticipate, catch, and respond to errors is essential for building robust software. Debugging skills help us identify and fix issues when things don't work as expected.

**Question 1**

What happens when the user enters invalid input (like letters when numbers are expected)? Find the `try` and `except` in `menu.py`. Which line inside the `try` can raise an error, and what type of error is it?

**Question 2**

Now take the protection away. Delete the `try:` line, the `except ValueError:` line, and the `print()` beneath the `except`, and move the two lines that were inside the `try` four spaces to the left. Run the app, choose Complete Task, and type `abc`. Read the traceback from the bottom up. What are the error type and the message? Which file and which line raised the error, and which file started the chain of calls that led there? Undo the change when you are done.

**Question 3**

How does the application handle edge cases like trying to complete a task that doesn't exist? Which function checks for this, and why does it check for _two_ conditions?

{% hint style="warning" %}
**Predict, then run.** Choose Clear All Tasks, then Complete Task, and enter `1`. What message appears, and which line of `tasks.py` produced it?
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** In `complete_task()`, delete `task_index < 0 or` from the guard. Run the app, choose Complete Task, and enter `0`. Which task, if any, is marked complete? Undo the change when you are done.
{% endhint %}

**Question 4**

In chapter 1.5, you checked a string with `isdigit()` before converting it with `int()`. This application uses `try`/`except` instead. Predict what each approach does with the input `-1`. Then type `-1` at the Complete Task prompt. Which part of the program refuses it?

**Question 5**

What debugging techniques could you use to understand what's happening when the program doesn't work as expected?

### Higher-Order Functions

Functions are values. They can be stored in a dictionary, passed to another function, and called later by whoever holds them. A menu program is one of the places where this pays off most clearly.

**Question 1**

Chapter 1.12 described a **dispatch table**: a dictionary that maps each choice to the function that handles it, so that one dictionary lookup replaces a long `if`/`elif` chain. Plan a version of `show_menu()` that uses one. Which menu options can go straight into the dictionary? Which need a small function of their own written first? Which option cannot go into the dictionary at all, and why not? What takes the place of the `else`?

**Question 2**

From the `src` folder, start the REPL with `python3` and run `from tasks import tasks`. Use `sorted()` with a `key` written as a `lambda` to build a list of the tasks with the incomplete ones first. Before you run it, predict whether `False` or `True` sorts first. After it runs, has the order of `tasks` itself changed?

### Comprehensions and Built-in Iteration

Comprehensions and Python's built-in iteration tools abstract away the logic for looping through a list by index and doing something with its values. While the programmer loses some fine-tuned control over how the loop is executed, the improved readability of the code is often worth the tradeoff.

**Question 1**

In Looping and Iteration Question 4, you rewrote the `for` loop in `view_tasks()` to use `enumerate`. Put your version beside the original `for i in range(len(tasks)):` loop. Which lines does your version no longer need? Which version leaves more room for an off-by-one mistake, and why?

**Question 2**

The Mark All as Completed extension needs to set every task's `is_complete` to `True`. A classmate adds this function to `tasks.py`:

```python
def complete_all_tasks():
    tasks = [{"description": task["description"], "is_complete": True} for task in tasks]
    print('All tasks marked as completed!')
```

{% hint style="warning" %}
**Predict, then run.** Paste the function at the bottom of `tasks.py`. From the `src` folder, start the REPL with `python3`, then run `from tasks import complete_all_tasks` followed by `complete_all_tasks()`. What happens? Delete the function from `tasks.py` when you are done.
{% endhint %}

Rewrite `complete_all_tasks()` so that it works. Should your version use a list comprehension or a `for` loop? Explain what a list comprehension produces, and why that does or does not fit a function whose job is to change the tasks that already exist.

**Question 3**

Suppose the user could complete a task by typing its description instead of its number. Using the pattern from Finding the First Match in chapter 1.13, write a function `find_task_index(description)` that returns the index of the first task whose description matches. What should it return when no task matches? Pass that value to `complete_task()` and predict what happens, then run it to check. Would the result be different if `find_task_index()` returned `None` when nothing matched?

### Test-Driven Development

Tests are code that checks other code. The tests in the `tests/` folder import the same modules as the application, and each time you run them, they check that the application still behaves the way the tests describe. That tells you when a change in one file affects another, before a user finds out. In test-driven development, you write the test for a feature before you write the feature itself.

**Question 1**

With your virtual environment activated, run `python3 -m pytest` from the project folder and check that every test passes. Then, in `clear_tasks()`, change the message `'All tasks cleared!'` to `'Tasks cleared!'`. Before you run the tests again, predict which tests will fail. Why does a test in `test_menu.py` fail when you changed only `tasks.py`? Undo the change when you are done.

The comment above `view_tasks()` also describes output: it shows an example of what the function prints. If a teammate changed the checkbox for a completed task from `[x]` to `[✓]`, which would tell them that something else needs updating, the comment or the tests? What does that suggest about what comments are good for, and what tests are good for?

**Question 2**

Open `tests/test_menu.py` and find `test_adding_a_task`. The test plays the part of the user: `type_answers('1', 'Buy groceries', '', '4', '')` lists everything the user types, in order, and `type_answers` (defined at the top of the file, with comments explaining it) hands those answers to `input()` one at a time. For each of the five answers, name the `input()` call in `show_menu()` that receives it.

{% hint style="warning" %}
**Predict, then run.** In `test_adding_a_task`, delete the last `''`, so that the test gives four answers. Run `python3 -m pytest`. Which test fails, and what does its message say? Undo the change when you are done.
{% endhint %}

**Question 3**

Open `tests/conftest.py`. The function `reset_tasks()` runs before every test and puts the two sample tasks back into `tasks`. Why do the tests need this? Think about what the list looks like after `test_clearing_all_tasks` has run.

{% hint style="warning" %}
**Predict, then run.** In `reset_tasks()`, replace the last line with `pass`, a statement that does nothing, so the function still runs before every test but no longer resets the list. Run `python3 -m pytest`. How many tests fail? Then run only `python3 -m pytest tests/test_tasks.py::test_sample_tasks_are_present_at_start`. Does it pass or fail on its own, and why is the result different? Undo the change when you are done.
{% endhint %}

**Question 4**

Open `tests/test_tasks.py` and find the test for `view_tasks()`. It uses `capsys` to capture what the function printed, because `view_tasks()` prints its output instead of returning it. In chapter 1.14, you tested functions by comparing their return value with `==`. Suppose `view_tasks()` built the same text as a string and returned it, and `show_menu()` printed it. What would the test look like then? What else would that change make easier?

**Question 5**

Chapter 1.14 described test-driven development: write a test for a feature before the feature exists, watch it fail (red), then write just enough code to make it pass (green). Try it on the [Toggle Complete extension](#extension-opportunities) (see below). In `tests/test_tasks.py`, add `toggle_task` to the import line at the top. Then write a test that calls `toggle_task(1)` twice and checks `tasks[1]["is_complete"]` after each call. What value should it have after the first call, and after the second?

{% hint style="warning" %}
**Predict, then run.** Before you write `toggle_task()`, run `python3 -m pytest`. What does the error say? What happened to the other tests in `test_tasks.py`, and to the tests in `test_menu.py` and `test_main.py`?
{% endhint %}

Now write `toggle_task()` in `tasks.py` and run the tests again. Chapter 1.14 says that a failing test proves the test is actually checking something. What could go wrong with a test that you only ever saw pass?

### Code Style

Code style encompasses the conventions and formatting choices that make code readable and maintainable. While the computer doesn't care about spacing or naming conventions, and Python only cares about indentation, these elements are crucial for human developers who need to read, understand, and modify the code. Consistent code style makes collaboration easier and reduces the cognitive load when working with code.

**Question 1**

Find the variables, functions, parameters, and dictionary keys in the application (search for `def` and `=`). Do they clearly describe the content they hold / the functionality they perform? What patterns do you see in naming, and how do they compare with the `snake_case` convention from PEP 8? Why is this important?

**Question 2**

How are imports, functions and code blocks organized? Is there a logical and consistent flow that makes the code easy to follow?

**Question 3**

What do you think the reason is that some files are in the `src` sub-folder while other files are in the root of the project. What is the purpose or benefit of this separation?

## Extension Opportunities

Now that the core Task Manager app is complete, it's time to add new features! Pick at least one feature to implement. If you finish quickly, try more than one!

- **Toggle Complete**: Right now, you can only mark a task as complete. Refactor the "Complete Task" menu option such that the user can toggle a task between complete and incomplete.
- **Delete Task**: Add a menu option to remove a single task from the list.
- **Show Completed Tasks**: Add a menu option to display only tasks that are completed.
- **Show Incomplete Tasks**: Add a menu option to display only tasks that are not completed.
- **Mark All as Completed**: Add a menu option that marks every task as completed.
- **Data Persistence**: Look into the `json.dump()` and `json.load()` functions from the `json` module, together with the built-in `open()` function, to figure out how to store the tasks in a `.json` file whenever the user exits and then retrieve those tasks when they start up again.
- **Tests**: The `tests/` folder already tests every function in `tasks.py`. Add tests to `tests/test_tasks.py` for each feature you build, following the pattern of the tests already there, and run them with `python3 -m pytest`.

### Tips

- Add a new menu option for each feature you implement.
- Don't delete old functionality — just extend your app.
- Test your feature with at least 3–4 tasks to make sure it works.
