# Case Study: CLI Task Manager

{% hint style="info" %}
The complete code for this case study is reproduced below, in the [The Code](#the-code) section, so that you can read it here and type it in yourself. Your instructor will share the repository link in class.
{% endhint %}

**Table of Contents:**

- [Key Features and Usage Example](#key-features-and-usage-example)
- [Key Technologies and Packages](#key-technologies-and-packages)
- [Setup](#setup)
- [The Code](#the-code)
- [Investigation Questions](#investigation-questions)
  - [User Interface Design](#user-interface-design)
  - [Data Types](#data-types)
  - [Variables and Scope](#variables-and-scope)
  - [Functions](#functions)
  - [Conditional Logic](#conditional-logic)
  - [Modules](#modules)
  - [Looping and Iteration](#looping-and-iteration)
  - [Lists and Dictionaries](#lists-and-dictionaries)
  - [Built-in Iteration](#built-in-iteration)
  - [Error Handling and Debugging](#error-handling-and-debugging)
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

## Setup

Follow these steps to get started:

```sh
# Clone the repo
git clone [repo_url]
cd [repo_name]

# Create and activate a virtual environment, then install dependencies.
# This project has no third-party packages, so requirements.txt is empty,
# but the habit is the point.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the src/main.py file
python3 src/main.py
```

## The Code

The application is three files in a `src` folder. Read them in this order, or better, follow the method from the [Reading Unfamiliar Code](10-reading-unfamiliar-code.md) chapter: run it first, then map the files by their `def` lines, then find the data, then trace one action.

{% code title="src/main.py" lineNumbers="true" %}
```python
from menu import show_menu


def start_app():
    print('Welcome to the Task Manager!')
    show_menu()
    print('Goodbye!')


if __name__ == "__main__":
    start_app()
```
{% endcode %}

{% code title="src/menu.py" lineNumbers="true" %}
```python
import os

from tasks import add_task, view_tasks, complete_task, clear_tasks


def show_menu():
    is_running = True
    while is_running:
        print('\nMenu:')
        print('1. Add Task')
        print('2. Complete Task')
        print('3. Clear All Tasks')
        print('4. Exit')

        view_tasks()

        menu_choice = input('\nChoose an option (1-4): ').strip()

        if menu_choice == '1':
            description = input('Enter task description: ').strip()
            add_task(description)
        elif menu_choice == '2':
            task_choice = input('Enter task number to complete: ').strip()
            try:
                task_index = int(task_choice) - 1
                complete_task(task_index)
            except ValueError:
                print(f'"{task_choice}" is not a number.')
        elif menu_choice == '3':
            clear_tasks()
        elif menu_choice == '4':
            is_running = False
        else:
            print('Invalid option. Please choose 1-4.')

        input('\nPress Enter to continue...')
        os.system('clear')
```
{% endcode %}

{% code title="src/tasks.py" lineNumbers="true" %}
```python
# The list of tasks. Each task is a dictionary with a description and a completion flag.
tasks = []


def add_task(description):
    # A guard clause: refuse an empty description
    if not description:
        print('Task description cannot be empty.')
        return

    task = {"description": description, "is_complete": False}
    tasks.append(task)
    print(f'Task "{description}" added!')


def view_tasks():
    if len(tasks) == 0:
        print('\nNo tasks yet. Add one!')
        return

    print('\nYour Tasks:')
    for index, task in enumerate(tasks, start=1):
        checkbox = '[x]' if task["is_complete"] else '[ ]'
        print(f'{index}. {checkbox} {task["description"]}')


def complete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print('Invalid task number.')
        return

    task = tasks[task_index]
    task["is_complete"] = True
    print(f'Task "{task["description"]}" marked as completed!')


def clear_tasks():
    tasks.clear()
    print('All tasks cleared!')
```
{% endcode %}

## Investigation Questions

By answering these questions, you will be required to think critically about how the application is designed and understand WHY it is designed in this way. Your aim should be to:

- learn as much as you can from this application so that you can build an application of your own that leverages these same skills
- communicate clearly about the concepts you are using and the decisions you make for how you implement them.

### User Interface Design

The user interface is how humans interact with our programs. Even in a simple command-line application, thoughtful design choices can make the difference between a frustrating or confusing experience and one that feels intuitive and pleasant to use.

**Question 1**

Look at the menu display in `show_menu()`. The menu shows numbered options (1, 2, 3, 4) and asks the user to "Choose an option (1-4)". Why do you think the menu uses numbers for the options? What are the potential downsides of having the user type out in words what they would like to do? For example: "Choose an option: add an item, view tasks, complete a task, exit".

**Question 2** In the `view_tasks()` function, tasks are displayed with checkboxes: `[x]` for completed tasks and `[ ]` for incomplete tasks. Do you think this visual representation is easy to understand? What alternative ways of displaying this information can you think of?

**Question 3** Look at the `os.system('clear')` call at the end of the `while` loop in `show_menu()`. It occurs after a final `input()` for the user to press Enter. How would the user experience change if we didn't clear the screen? How would it change if we removed the `input()` that comes right before it?

**Question 4** When a user completes a task, the program shows a message like `Task "walk the dog" marked as completed!`. Why is it important that the user sees these messages? How would the user experience change without these messages?

### Data Types

Whether you are designing a new application or learning about an existing one, we always start by asking: _how is the data represented_? Once we know how to represent the data, we are better able to design how the application uses and manipulates it.

**Question 1**

Go to the `tasks.py` file and look at the `tasks` variable. It is a list of dictionaries. Each dictionary represents a task in the list. Each task has a `description` string and an `is_complete` boolean. For the `is_complete` value, we could also have represented it with the numbers: `"is_complete": 0` (incomplete) and `"is_complete": 1` (complete); or as strings `"is_complete": "complete"` and `"is_complete": "incomplete"`. If it were up to you, which would you choose to represent `is_complete` and why?

**Question 2**

In `tasks.py` in the `add_task` function, there is this conditional statement: `if not description:`. What data type does the expression `not description` evaluate to? and what is the purpose of this conditional statement?

**Question 3**

In `menu.py`, the user's chosen task number `task_choice` is converted to a number using the `int()` conversion function. Why is this code necessary? What happens if this type conversion is removed?

### Variables and Scope

Understanding where variables are declared (their **scope**) and therefore where they can be reached is crucial for building well-structured applications. In this CLI Task Manager, we can see variables declared in different locations that serve different purposes.

**Question 1**

In the `show_menu()` function in `menu.py`, the variable `is_running` is assigned `True` before the loop and reassigned to `False` inside it. It is the only variable in the whole application that is ever reassigned. The `tasks` list in `tasks.py`, by contrast, is never reassigned, and yet its contents change constantly. What is the difference between these two kinds of change? Which chapter did you learn it in?

**Question 2**

In the `show_menu()` function in `menu.py`, take a look at the `task_choice` and `task_index` variables. Consider that we could have also written the code without any variables and it would still work properly:

```python
complete_task(int(input('Enter task number to complete: ')) - 1)
```

What are the tradeoffs of these approaches?

**Question 3**

Look at the `tasks` list in `tasks.py`. What is the scope of the `tasks` variable? What would happen if we moved the `tasks = []` line inside one of the functions? Why would this break the application?

### Functions

Functions are the building blocks of reusable code. They allow us to break down complex problems into smaller, manageable pieces and avoid repeating the same code multiple times. Good function design and modular organization make code easier to understand, test, and maintain.

**Question 1**

In `menu.py`, take a look at how the `input()` function is being invoked. Based on what you're seeing, how many parameters does the function seem to have? If you were the designer of that function what name would you give to its parameter?

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

**Question 2**

Look at the `add_task()` function in `tasks.py`. The first few lines check `if not description:` and return early if no description is provided. This is called a "guard clause." What would happen if we removed this guard clause and a user tried to add a task with no description?

**Question 3**

Look at the `view_tasks()` function. It checks `if len(tasks) == 0:` before displaying tasks. What would happen if we removed this check and tried to display an empty task list?

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

### Looping and Iteration

Loops take repetitive tasks and boil them down to a process that can be repeated without having to type the same code multiple times. Choosing the right type of loop and ensuring it terminates properly are crucial skills for any programmer.

**Question 1**

Look at the `show_menu()` function in `menu.py`. There's a `while is_running:` loop that keeps the menu running until the user chooses to exit. What would happen if we forgot to set `is_running = False` when the user chooses option 4 (Exit)? What would happen if we forgot to include that line of code?

**Question 2**

Why is a `while` loop the appropriate type of loop to use to display the menu as opposed to a `for` loop?

**Question 3**

The `while` loop in `show_menu()` has a condition `while is_running:`. This means the loop will continue as long as `is_running` is `True`. What would happen if we changed the condition to `while True:` and removed the `is_running` variable entirely? How else could we break out of the loop?

### Lists and Dictionaries

Lists and dictionaries are the two most common options we have for creating collections of data. Lists are a great choice for grouping together lists of similar values while dictionaries are a great way to represent a single thing that has many data points related to it.

**Question 1**

The entire collection of `tasks` is represented as a list of task dictionaries. Each task dictionary is represented with keys `"description"` and `"is_complete"`. Suppose we instead represented the tasks as a list of strings, such as `['walk the dog', 'take out the trash']`. What are the tradeoffs between a list of dictionaries and a list of strings?

**Question 2**

What ideas do you have for differentiating incomplete tasks and complete tasks?

### Built-in Iteration

Python's built-in iteration tools abstract away the logic for looping through a list by index and doing something with its values. While the programmer loses some fine-tuned control over how the loop is executed, the improved readability of the code is often worth the tradeoff.

**Question 1**

In the `view_tasks()` function in `tasks.py`, there's a `for` loop: `for index, task in enumerate(tasks, start=1):`. This is a different kind of loop than the `while` loop. What are the tradeoffs of using `for ... in enumerate(...)` when compared to using a `while` loop with a counter, or `for i in range(len(tasks))`?

**Question 2**

Look at the `for` loop in `view_tasks()`. The loop variable is called `task` and it represents each individual task dictionary. What would happen if we changed the variable name from `task` to `item` or `t`? Would the code still work the same way?

**Question 3**

What does the `start=1` argument to `enumerate` do? What would the user see if it were removed?

### Error Handling and Debugging

Real-world applications must handle unexpected situations gracefully. Understanding how to anticipate, catch, and respond to errors is essential for building robust software. Debugging skills help us identify and fix issues when things don't work as expected.

**Question 1**

What happens when the user enters invalid input (like letters when numbers are expected)? Find the `try` and `except` in `menu.py`. Which line inside the `try` can raise an error, and what type of error is it? What would happen without the `try`/`except`?

**Question 2**

How does the application handle edge cases like trying to complete a task that doesn't exist? Which function checks for this, and why does it check for _two_ conditions?

**Question 3**

What debugging techniques could you use to understand what's happening when the program doesn't work as expected?

{% hint style="warning" %}
**Predict, then run.** Choose Clear All Tasks, then Complete Task, and enter `1`. What message appears, and which line of `tasks.py` produced it?

<details><summary>What actually happens</summary>

`Invalid task number.` With the list empty, `len(tasks)` is `0`, so `task_index >= len(tasks)` is `0 >= 0`, which is `True`, and the guard on line 28 returns before `tasks[task_index]` can raise an `IndexError`. That is the second of the two conditions Question 2 asks about, and it is the one doing the work here. The first, `task_index < 0`, catches a user who types `0`.

</details>
{% endhint %}

### Code Style

Code style encompasses the conventions and formatting choices that make code readable and maintainable. While the computer doesn't care about spacing or naming conventions, and Python only cares about indentation, these elements are crucial for human developers who need to read, understand, and modify the code. Consistent code style makes collaboration easier and reduces the cognitive load when working with code.

**Question 1**

Look at the indentation in `tasks.py`. Notice how the code inside functions is indented with 4 spaces, and code inside `if` statements is indented even further. How does this indentation impact your ability to understand the code?

**Question 2**

Find the variables, functions, parameters, and dictionary keys in the application (search for `def` and `=`). Do they clearly describe the content they hold / the functionality they perform? What patterns do you see in naming? Why is this important?

**Question 3**

How are imports, functions and code blocks organized? Is there a logical and consistent flow that makes the code easy to follow?

**Question 4**

What do you think the reason is that some files are in the `src` sub-folder while other files are in the root of the project. What is the purpose or benefit of this separation?

## Extension Opportunities

Now that the core Task Manager app is complete, it's time to add new features! Pick at least one feature to implement. If you finish quickly, try more than one!

- **Toggle Complete**: Right now, you can only mark a task as complete. Refactor the "Complete Task" menu option such that the user can toggle a task between complete and incomplete.
- **Delete Task**: Add a menu option to remove a single task from the list.
- **Show Completed Tasks**: Add a menu option to display only tasks that are completed.
- **Show Incomplete Tasks**: Add a menu option to display only tasks that are not completed.
- **Mark All as Completed**: Add a menu option that marks every task as completed.
- **Show Task Stats**: Add a message to the `view_tasks` function that shows the user how many tasks are complete vs. incomplete.
- **Data Persistence**: Look into the `json.dump()` and `json.load()` functions from the `json` module, together with the built-in `open()` function, to figure out how to store the tasks in a `.json` file whenever the user exits and then retrieve those tasks when they start up again.
- **Tests**: Add a `tests/test_tasks.py` file and write pytest tests for `add_task`, `complete_task`, and `clear_tasks`. You will find that testing functions that print is awkward. What small change to `tasks.py` would make them easier to test?

### Tips

- Add a new menu option for each feature you implement.
- Don't delete old functionality — just extend your app.
- Test your feature with at least 3–4 tasks to make sure it works.
