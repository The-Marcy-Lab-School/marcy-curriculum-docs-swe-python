# Debugging and Problem Solving

**Table of Contents:**
- [PEDAC Problem Solving](#pedac-problem-solving)
  - [Example PEDAC](#example-pedac)
- [Tips for Making Your Own PEDAC](#tips-for-making-your-own-pedac)
  - [P — State the Problem](#p--state-the-problem)
  - [E — Examples / Test Cases](#e--examples--test-cases)
  - [D — Data Structures and Tools](#d--data-structures-and-tools)
  - [A — Algorithm](#a--algorithm)
  - [C — Code!](#c--code)

## PEDAC Problem Solving

Imagine that you had the following problem to solve:

> Consider this list.
> ```python
> users = [
>     {"id": 1, "name": "ben", "is_admin": False},
>     {"id": 2, "name": "maya", "is_admin": True},
>     {"id": 3, "name": "reuben", "is_admin": True},
>     {"id": 4, "name": "gonzalo", "is_admin": False},
>     {"id": 5, "name": "ana", "is_admin": True},
> ]
> ```
> Write a function `get_admin_ids` that has one parameter, a list `users` full of dictionaries that have `"id"`, `"name"`, and `"is_admin"` keys. The function should return a list containing the `id` numbers of the users where the `"is_admin"` value is `True`. If none are found, return an empty list. If `users` is not a list, return `None`. Do not modify the original list.

You might have an idea of how to solve the problem, but before you do, try planning out your approach first! Doing so has a number of benefits:
* You can work on the skill of problem solving separately from the skill of coding!
* You will have a roadmap for writing a solution that you can return to if you get lost while coding.
* If you are having trouble implementing your solution, you can bring your planning to an instructor, mentor, or peer to quickly get them up to speed on the problem.

At Marcy, we use **PEDAC** which is an acronym that stands for the following problem solving strategy:
* State the **P**roblem
* Think of **E**xamples and **e**dge cases
* List the **D**ata Structures and tools you can use
* Plan out the **A**lgorithm
* **C**ode the solution!

### Example PEDAC

Here is an example of our PEDAC process:

```python
# PEDAC
#
# State the Problem
# - inputs:
#   - users: a list of dictionaries, each with the keys "id", "name", and "is_admin"
#
# - output:
#   - a list of integers representing the id numbers of the admins in users
#
# Examples / Test Cases:
#
# users = [
#     {"id": 1, "name": "ben", "is_admin": False},
#     {"id": 2, "name": "maya", "is_admin": True},
#     {"id": 3, "name": "reuben", "is_admin": True},
#     {"id": 4, "name": "gonzalo", "is_admin": False},
#     {"id": 5, "name": "ana", "is_admin": True},
# ]
#
# get_admin_ids(users) -> [2, 3, 5]
# get_admin_ids([{"id": 1, "name": "ben", "is_admin": False}]) -> []
# get_admin_ids([{"id": 1, "name": "ben", "is_admin": True}]) -> [1]
# get_admin_ids([]) -> []
# get_admin_ids(None) -> None
# get_admin_ids(5) -> None
#
# Data Structures and Tools
# - isinstance() to check that users is a list
# - a list to hold the ids of the admins (this is the return value)
# - a for loop to visit each dictionary in the list
# - bracket notation to look up a dictionary's values by key
# - an if statement to check if a user is an admin
#
# Algorithm
# - If users is not a list, return None
# - Set `ids` to be a new list to store the ids of admins
# - Iterate through the input `users` list. For each dictionary...
#   - If the current user is an admin...
#   - Add that user's id to the `ids` list
# - Return the `ids` list after the iteration is complete.


def get_admin_ids(users):
    if not isinstance(users, list):
        return None

    ids = []
    for user in users:
        if user["is_admin"]:
            ids.append(user["id"])
    return ids


# Test Code

users = [
    {"id": 1, "name": "ben", "is_admin": False},
    {"id": 2, "name": "maya", "is_admin": True},
    {"id": 3, "name": "reuben", "is_admin": True},
    {"id": 4, "name": "gonzalo", "is_admin": False},
    {"id": 5, "name": "ana", "is_admin": True},
]

print(get_admin_ids(users))  # -> [2, 3, 5] because three admins with these ids were found
print(get_admin_ids([{"id": 1, "name": "ben", "is_admin": False}]))  # -> [] because no admins were found
print(get_admin_ids([{"id": 1, "name": "ben", "is_admin": True}]))  # -> [1] because only 1 admin was found
print(get_admin_ids([]))  # -> [] because no admins were found
print(get_admin_ids(None))  # -> None because a list was not provided
print(get_admin_ids(5))  # -> None because a list was not provided
```

## Tips for Making Your Own PEDAC

Let's look at how we arrived at the PEDAC above.

### P — State the Problem

Before you can solve a problem, you must fully understand the problem. When you have a problem in front of you, start by listing **inputs** and **outputs**

{% hint style="info" %}
Tip: Write this planning in a comment directly in your code!
{% endhint %}

When listing inputs and outputs, you want to be as descriptive as possible. 
* Rather than _"a list"_ say _"a list of integers"_
* Rather than _"a dictionary"_ say _"a dictionary with the keys x, y, and z"_
* Rather than _"a list of dictionaries" say "a list of dictionaries, each with the keys x, y, and z"_

```python
# PEDAC
#
# State the Problem
# - inputs:
#   - users: a list of dictionaries, each with the keys "id", "name", and "is_admin"
#
# - output:
#   - a list of integers representing the id numbers of the admins in users
```

### E — Examples / Test Cases

When listing examples, imagine you are invoking your own function. Come up with a few different examples with "good" inputs, a few with "bad" inputs, such as a value of the wrong type, and a few with empty inputs, such as `None` or an empty list. For each example, include the expected result of calling the function.

```python
# Examples / Test Cases:
#
# get_admin_ids(users) -> [2, 3, 5]
# get_admin_ids([{"id": 1, "name": "ben", "is_admin": False}]) -> []
# get_admin_ids([{"id": 1, "name": "ben", "is_admin": True}]) -> [1]
# get_admin_ids([]) -> []
# get_admin_ids(None) -> None
# get_admin_ids(5) -> None
```

### D — Data Structures and Tools

List all of the relevant tools that you might use to solve the problem, including:
* Data you need to store in variables
  * Single values: strings, integers, floats, or booleans to represent x, y or z
  * Collections: lists or dictionaries to hold x, y, and z
* Control Flow Constructs
  * `for` or `while` loops to repeat x or to iterate through y
  * `if`/`elif`/`else` statements to determine whether to x, y, or z
* Built-in Functions / Methods
  * Built-in functions like `len()` and `isinstance()`
  * List methods
  * String methods
  * Dictionary methods
  * etc...

```python
# Data Structures and Tools
# - isinstance() to check that users is a list
# - a list to hold the ids of the admins (this is the return value)
# - a for loop to visit each dictionary in the list
# - bracket notation to look up a dictionary's values by key
# - an if statement to check if a user is an admin
```

### A — Algorithm

Plan out the order of operations to process the inputs and return the desired output. During this stage, you should be writing "pseudocode". Pseudocode should be written such a way that anyone with basic programming knowledge could implement your algorithm in any language.

```python
# Algorithm
# - If users is not a list, return None
# - Set `ids` to be a new list to store the ids of admins
# - Iterate through the input `users` list. For each dictionary...
#   - If the current user is an admin...
#   - Add that user's id to the `ids` list
# - Return the `ids` list after the iteration is complete.
```

### C — Code!

Once you've completed the first four steps, go ahead and build your solution! Use your examples to test your solution.

```python
def get_admin_ids(users):
    if not isinstance(users, list):
        return None

    ids = []
    for user in users:
        if user["is_admin"]:
            ids.append(user["id"])
    return ids


print(get_admin_ids(users))  # -> [2, 3, 5]
print(get_admin_ids([{"id": 1, "name": "ben", "is_admin": False}]))  # -> []
print(get_admin_ids([{"id": 1, "name": "ben", "is_admin": True}]))  # -> [1]
print(get_admin_ids([]))  # -> []
print(get_admin_ids(None))  # -> None
print(get_admin_ids(5))  # -> None
```
