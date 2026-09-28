# 12. First-Class Functions and Higher-Order Functions

**Table of Contents**:

- [Key Terms](#key-terms)
- [Functions are "First-Class" Values](#functions-are-first-class-values)
  - [Functions Stored in Dictionaries](#functions-stored-in-dictionaries)
  - [Functions Passed into Other Functions Are "Callbacks". The Function That Receives the Callback is a "Higher Order Function".](#functions-passed-into-other-functions-are-callbacks-the-function-that-receives-the-callback-is-a-higher-order-function)
  - [Do Not Invoke The Callback](#do-not-invoke-the-callback)
  - [Anonymous Functions with `lambda`](#anonymous-functions-with-lambda)
  - [Functions That Return Functions](#functions-that-return-functions)
- [Higher-Order Functions Built Into Python](#higher-order-functions-built-into-python)
- [Looping with Callbacks](#looping-with-callbacks)

## Key Terms

- **Functions are "first-class" values** meaning they can be stored in variables and data structures (lists/dictionaries), passed to functions as arguments, and returned from functions.
- A **method** is a function attached to a value, like `"abc".upper()`. In Mod 2 you will write your own.
- **Higher-order functions (HOFs)** are functions that accept other functions as input and/or return functions, enabling powerful programming patterns and code reuse.
- **Callback functions** are functions passed as arguments to higher-order functions, allowing you to customize behavior without modifying the HOF itself.
- When passing callbacks to HOFs, avoid invoking them (don't use parentheses) - the HOF will handle the invocation with the correct parameters.
- **`lambda`** creates a small anonymous function in one expression, a concise way to define callbacks when they won't be reused elsewhere.
- `sorted()`, `min()`, and `max()` are built-in higher-order functions. Their `key` parameter takes a callback that says what to compare.

## Functions are "First-Class" Values

Pop Quiz! Identify the data types stored in each variable below:

```python
a = 'hello world'
b = 42
c = True
d = [1, 2, 3]
e = {'name': 'Ada'}

def f():
    print("hello world")
```

**<details><summary>Answers</summary>**

1. `str`
2. `int`
3. `bool`
4. `list`
5. `dict`
6. function

Check with `type()`. `print(type(f))` prints `<class 'function'>`. `print(f)` on its own, with no parentheses, prints something like `<function f at 0x104fccd60>`: the function itself, with its address in memory, not the result of calling it.

</details>

What we can see from this is that functions are just another type of data and, like other data types, it can be stored in a variable. In fact, `def f():` _is_ an assignment: it creates a function and stores it in the variable `f`. This ability to be stored in a variable is the first quality that describes **functions as "first class" values**.

You can even give a function a second name, and the second name works exactly like the first:

```python
def say_hi():
    print("Hi")

greet = say_hi  # no parentheses: we are copying the function, not calling it
greet()         # Hi
```

### Functions Stored in Dictionaries

Functions can also be stored in dictionaries and lists. Here, a dictionary of functions turns a word into an action:

```python
def say_hi():
    print("Hi")

def greet(name):
    print(f"Hello {name}")

def is_even(number):
    return number % 2 == 0

actions = {
    "hi": say_hi,
    "greet": greet,
    "even": is_even,
}

actions["hi"]()              # Hi
actions["greet"]('Ada')      # Hello Ada
print(actions["even"](4))    # True
```

`actions["hi"]` looks up the function, and the `()` after it calls whatever was looked up. Try adding your own `is_odd` function to the dictionary and test it out!

This pattern has a name, a **dispatch table**, and it is how a menu program can replace a long chain of `if choice == "1": ... elif choice == "2": ...` with a single dictionary lookup. Keep it in mind for your project.

{% hint style="info" %}
When a function is attached to a value, we call it a **method**. You have been using methods since chapter 4: `upper` is a function stored inside every string, and `"abc".upper()` looks it up and calls it, the same way `actions["hi"]()` does. In Mod 2 you will learn how to attach functions to values of your own.
{% endhint %}

### Functions Passed into Other Functions Are "Callbacks". The Function That Receives the Callback is a "Higher Order Function".

Here is a "normal" function that takes in a string as an argument:

```python
def greet(name):
    print(f"Hello {name}")

greet('Ada')  # Passing a string as an argument
```

Just like strings, functions can be passed to other functions as arguments. In these cases, we call the function argument a **"callback function"** and the function receiving the callback is a **"higher order function"**

Let's write our own higher-order function. It takes a callback and a number, and invokes the callback that many times:

```python
def repeat(callback, times):
    for i in range(times):
        callback()

# First, we define the callback
def tick():
    print("Tick")

repeat(tick, 3)  # This higher order function takes in a callback and a number
# Tick
# Tick
# Tick
```

`repeat` never says the word `tick`. It calls whatever it was given. That is what makes it reusable: the same `repeat` can print, or roll dice, or do anything, depending on the callback it receives.

Adding a pause between calls gives us a timer. `time.sleep(seconds)` from the standard library pauses the program:

```python
import time

def repeat_every(callback, seconds, times):
    for i in range(times):
        callback()
        time.sleep(seconds)

repeat_every(tick, 1, 5)  # Prints "Tick" once a second, five times
```

**Q: What is the difference between `repeat(tick, 5)` and `repeat_every(tick, 1, 5)`?**

**<details><summary>Answer</summary>**

Both call `tick` five times. `repeat` does it as fast as it can, so all five lines appear at once. `repeat_every` waits one second between calls. The callback is identical; only the higher-order function's behavior changed.

</details>

**<details><summary>Optional: two animations built on `repeat_every`</summary>**

This one creates a "loading wheel" animation. Each frame prints over the previous one, because `end="\r"` moves the cursor back to the start of the line instead of down to the next one:

{% code title="fun_examples.py" %}

```python
import time

chars = ["\\", "|", "/", "-"]
i = 0

# print the next character in the sequence, on top of the previous one
def loop_through_chars():
    global i
    print(chars[i], end="\r", flush=True)
    i += 1
    if i >= 4:
        i = 0

repeat_every(loop_through_chars, 0.25, 40)
```

{% endcode %}

This one animates an alien that bounces across the screen:

{% code title="fun_examples.py" overflow="wrap" %}

```python
import shutil

alien = '👾'
forward = True

def animate_alien():
    global alien, forward
    print(alien, end="\r", flush=True)

    if forward:
        # add white space to the front
        alien = ' ' + alien
    else:
        # remove 1 white space from the front
        alien = alien[1:]

    # Turn around when reaching either side of the terminal
    terminal_width = shutil.get_terminal_size().columns
    if len(alien) >= terminal_width or len(alien) == 1:
        forward = not forward

repeat_every(animate_alien, 0.05, 200)
```

{% endcode %}

Both examples use `global`, which chapter 3 told you to avoid. They need it because each call has to remember where the previous call left off, and a callback that takes no arguments has nowhere else to keep that. In Mod 2 you will learn the right tool for a function that needs memory between calls. For now, treat this as a place where the rule bends and you can see exactly why.

</details>

### Do Not Invoke The Callback

When passing in a callback to a higher-order function, avoid invoking the callback.

In this example, since `execute_callback` is the higher-order function, it will invoke the callback on our behalf. Invoking the callback will produce an error:

```python
def say_hello():
    print("hello world")

def execute_callback(callback):
    callback()

execute_callback(say_hello)
# hello world

execute_callback(say_hello())
# TypeError: 'NoneType' object is not callable
```

**<details><summary>Q: Why does an error get raised? Why is it saying `'NoneType' object is not callable`?</summary>**

When you invoke `execute_callback(say_hello())`, the `say_hello()` function call gets resolved first. Since `say_hello()` returns `None`, that is what `execute_callback` gets as its callback:

```python
say_hello()              # this gets resolved first, prints "hello world", and returns None
execute_callback(None)   # None is not a function, so callback() fails
```

Notice that `hello world` _does_ print, once, before the error. That is your clue that the callback ran too early.

</details>

### Anonymous Functions with `lambda`

When a callback is short and will only be used once, defining it with `def` and a name a few lines earlier can feel like a lot of ceremony. Python lets you write a small function inline with `lambda`:

```python
repeat(lambda: print("Tock"), 3)
# Tock
# Tock
# Tock
```

A `lambda` has parameters before the colon and a single expression after it, and that expression's value is what the function returns. There is no `return` keyword and no room for more than one expression:

```python
square = lambda x: x * x   # same as def square(x): return x * x
print(square(4))           # 16
```

Use `lambda` for a callback that fits comfortably on one line. The moment it needs a second line or a name to explain it, use `def`.

### Functions That Return Functions

The last part of being first-class: a function can be the return value of another function, and the returned function remembers the variables that were in scope when it was made. You will spend a whole session on this at the end of Mod 2, because it is the mechanism behind decorators. For now, notice only that it follows from everything above.

## Higher-Order Functions Built Into Python

The most commonly used built-in higher-order function is `sorted()`, together with its `key` parameter. `key` takes a callback that is called on each element to produce the value to sort by:

```python
animals = ['aardvark', 'bear', 'cheetah', 'deer']

print(sorted(animals))            # ['aardvark', 'bear', 'cheetah', 'deer']  alphabetical
print(sorted(animals, key=len))   # ['bear', 'deer', 'cheetah', 'aardvark']  by length
```

`len` is passed with no parentheses, because `sorted` will call it, once per animal. `min()` and `max()` take `key` the same way:

```python
users = [
    {'id': 1, 'username': 'ben', 'age': 30},
    {'id': 2, 'username': 'maya', 'age': 25},
    {'id': 3, 'username': 'reuben', 'age': 41},
]

oldest = max(users, key=lambda user: user['age'])
print(oldest['username'])   # reuben
```

The next chapter is about the rest of this family: the built-in ways to loop, transform, filter, and combine data, and when to reach for each one.

## Looping with Callbacks

Here is a higher-order function you can build yourself, and building it shows that a loop and a callback are two spellings of the same idea. Start with a plain loop. This one changes the `is_admin` value of every dictionary in the `users` list:

{% code title="for_each.py" %}

```python
# revoke is_admin status from all users
users = [
    {'id': 1, 'username': 'ben', 'is_admin': False},
    {'id': 2, 'username': 'maya', 'is_admin': True},
    {'id': 3, 'username': 'reuben', 'is_admin': True},
    {'id': 4, 'username': 'gonzalo', 'is_admin': False},
]

for user in users:
    user['is_admin'] = False
```

{% endcode %}

**Challenge 1:**

Loop over `users` and update the `username` value for each dictionary such that the first letter is capitalized.

**<details><summary>Solution</summary>**

```python
for user in users:
    user['username'] = user['username'].capitalize()
```

`capitalize()` is a string method that uppercases the first character and lowercases the rest. Without it: `user['username'][0].upper() + user['username'][1:]`.

</details>

**Challenge 2:**

Implement your own `for_each` function that takes a list `items` and a `callback`:

It should iterate through the input `items` and do the following:

- Invoke the `callback` with the following arguments:
  - The value at the current index
  - The current index
  - The source list itself
- Return nothing (or manually return `None`)

**Usage Example**

```python
def for_each(items, callback):
    # ???

for_each(['a', 'b', 'c'], print)
# a 0 ['a', 'b', 'c']
# b 1 ['a', 'b', 'c']
# c 2 ['a', 'b', 'c']
```

**<details><summary>Solution</summary>**

```python
def for_each(items, callback):
    # Iterate through the input list, with the index of each element
    for index, value in enumerate(items):
        callback(value, index, items)
```

`print` is passed as the callback, with no parentheses, and `for_each` calls it with three arguments each time. `print` accepts any number of arguments and prints them separated by spaces, which is where the output format comes from.

</details>
