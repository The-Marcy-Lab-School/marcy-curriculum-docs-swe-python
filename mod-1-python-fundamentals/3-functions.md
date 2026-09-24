# 3. Functions

**Table of Contents:**

- [Key Terms](#key-terms)
- [Don't Repeat Yourself (DRY)](#dont-repeat-yourself-dry)
- [Functions](#functions)
  - [Invoking a Function](#invoking-a-function)
  - [Function Calls Change the Control Flow](#function-calls-change-the-control-flow)
  - [Parameters and Arguments](#parameters-and-arguments)
  - [Return Statements](#return-statements)
  - [Default Values and Keyword Arguments](#default-values-and-keyword-arguments)
- [Functions Create Local Variable Scope](#functions-create-local-variable-scope)
  - [Order Matters: Assign Before You Use](#order-matters-assign-before-you-use)
  - [The `global` Keyword](#the-global-keyword)

## Key Terms

- **Don't Repeat Yourself (DRY)** is a principle of software engineering aimed at making it easier to maintain, update, and debug code.
- **Functions** are named containers for statements that can be invoked to execute code, improving readability and reducing repetition.
- **Parameters** are placeholders for inputs given to the function. Parameters can be used by their function to change the function's behavior.
- **Arguments** are the actual values given when invoking a function.
- **Return statements** allow functions to produce values that can be used elsewhere in your program and terminate function execution. A function with no `return` statement returns `None`.
- Parameters can have **default values**, and arguments can be passed by **keyword** as well as by position.
- **Order matters.** A name has to be assigned before the line that uses it runs. Functions are looked up when they are called, not when they are written.
- **Scope** determines where variables can be accessed. Global scope variables are accessible everywhere, while local scope variables are only accessible within their function.

## Don't Repeat Yourself (DRY)

Suppose we had a series of temperatures in Celsius that we needed to convert to Fahrenheit? We could just copy and paste the code and swap out the numbers like this:

```python
boiling_point_C = 100
boiling_point_F = boiling_point_C * 9/5 + 32
print(boiling_point_F) # Output: 212

freezing_point_C = 0
freezing_point_F = freezing_point_C * 9/5 + 32
print(freezing_point_F) # Output: 32

best_temperature_C = 20
best_temperature_F = best_temperature_C * 9/5 + 32
print(best_temperature_F) # Output: 68
```

**<details><summary>Q: What isn't great about this code?</summary>**

It breaks the fundamental software engineering principle "DRY" which stands for "Don't Repeat Yourself". Repetition is a problem for two primary reasons:

- If we need to change the format of our print statements, we need to change the format in 3 places.
- If we need to fix a bug in the code, we need to fix it in 3 places.p[p]

The solution is to create a function!

</details>

## Functions

A **Function** is a reusable block of statements. They are created with the `def` keyword and are followed by:

- a descriptive name
- a list of input variables called "**parameters** inside of parentheses `()`
- a colon `:` (don't forget the colon!)

```python
def convert_C_to_F(celsius):
    celsius = 20
    fahrenheit = celsius * 9/5 + 32
    print(fahrenheit)
```

The code is indented to indicate that it is _inside_ the function block.

Notice that we've replaced the _specific_ variable names (`boiling_point_C`, `freezing_point_C`, `best_temperature_C`) with a generic parameter named `celsius`. The variable in the function is also a generic name `fahrenheit`. Otherwise, the logic is the exact same!

### Invoking a Function

A function can be **invoked** to execute its statements by typing the function name and input values within parentheses `()`.

```python
convert_C_to_F(100) # 212
convert_C_to_F(0)   # 32
convert_C_to_F(20)  # 68
```

{% hint style="info" %}
💡 A function can also carry a short description of what it does, written as a string on the first line of its body. It is called a **docstring**, and VS Code and the built-in `help()` function show it to whoever is about to call the function:

```python
def print_sum_and_average(a, b, c, d):
    """Print the sum and average of four numbers."""
    sum = a + b + c + d
    average = sum / 4
    print(f"The sum of {a} + {b} + {c} + {d} is {sum} and the average is {average}")
```

You will see docstrings in nearly every library and every piece of generated code you read. Write one whenever a function's name alone does not say what it does.

{% endhint %}

**Challenge**: Refactor this highly repetitive code for printing a star rating for a book. First, what does each `print()` statement output? What should the function be called? What are the inputs that make each instance of code different (and what should those parameters be called)?

```py
title1 = "The Great Gatsby"
score1 = 4
stars1 = "*" * score1
print(title1 + ": " + stars1)

title2 = "Paradise Lost"
score2 = 2
stars2 = "*" * score2
print(title2 + ": " + stars2)

title3 = "1984"
score3 = 5
stars3 = "*" * score3
print(title3 + ": " + stars3)
```

**<details><summary>Answer</summary>**

```py
def print_rating(title, score):
    stars = "*" * score
    print(f"{title}: {stars}")

print_rating("The Great Gatsby", 4)
print_rating("Paradise Lost", 2)
print_rating("1984", 5)

# Output:
# The Great Gatsby: ****
# Paradise Lost: **
# 1984: *****
```

</details>

### Function Calls Change the Control Flow

Recall that the Python interpreter will execute code from the top of the file to the bottom.

However, code within a function only runs when it is invoked (in other words, when the function is "called"). When that happens, the interpreter jumps up into the function and executes the first line.

Look at the code below and **predict what will happen**:

```python
print('A')

def print_B():
    print('B')

print('C')

print_B()
print_B()
```

**<details><summary>Answer</summary>**

```py
A
C
B
B
```

Note that the order in which statements are executed in our code is not always top to bottom. Defining the function doesn't cause the code inside to run. We only execute the code inside of `say_hello` when it is invoked a few lines later.

</details>

### Parameters and Arguments

```py
def say_hello():
    print("hello")

say_hello() # hello
say_hello() # hello
say_hello() # hello
```

The function `say_hello` does the same thing. Every. Single. Time. It always prints `"hello"`. This function has no parameters.

**Parameters** give functions more flexibility to change their behavior based on provided input values, called **arguments**.

```python
# print_sum can add and print any two given values
# x and y are parameters that reference the values provided when the function is called.
def print_sum(x, y):
    print(x + y)

# 5 and 3 are the arguments. 8 is printed
print_sum(5, 3)

# This time, 10 and 2 are the arguments. 12 is printed
print_sum(10, 2)
```

Some things to remember:

- Function definition variables -> "Parameters"
- Function invocation inputs -> "Arguments"
- The order of the arguments must match the order of the parameters.

{% hint style="warning" %}
**Predict, then run.** What does each of these two calls do?

```python
print_sum('hello', 5)

print_sum()
```

**<details><summary>What actually happens</summary>**

Both crash, with different messages.

```
TypeError: can only concatenate str (not "int") to str
```

The first call gets as far as `x + y` and then refuses: Python will not add a string and a number, and the next chapter says more about why. Python checks types at the moment an operation runs, not at the moment the function is called.

```
TypeError: print_sum() missing 2 required positional arguments: 'x' and 'y'
```

The second call never gets inside the function at all. Python checks that the _number_ of arguments matches the number of parameters before it runs a single line of the body. Every parameter without a default value (more on those below) is required.

</details>

{% endhint %}

**Challenge:** Refactor this function so that it can print any name and hobby.

```python
def say_hello():
    print("Hi, my name is Ben. I like to code!")

say_hello()
```

Test your code by invoking the function with various inputs. What happens when no input is provided?

**<details><summary>Solution</summary>**

```python
def say_hello(name, hobby):
    print(f"Hi, my name is {name}. I like to {hobby}!")

say_hello("Ben", "rock climb")
# Output: Hi, my name is Ben. I like to rock climb!

say_hello("Gonzalo", "play the bass")
# Output: Hi, my name is Gonzalo. I like to play the bass!

say_hello()
# TypeError: say_hello() missing 2 required positional arguments: 'name' and 'hobby'
```

</details>

### Return Statements

The functions above use `print` to print out a result to the console, but that result can't be used later in the program. If we want a function to produce a value that we can be used outside of the function, we add a `return` statement.

A `return` statement does two things:

1. It returns a value to the location of the function call.
2. It terminates the execution of the function

```python
def add(x, y):
    return x + y

# The value of 5 + 3 is returned, resolving to `sum = 8`
sum = add(5, 3)

# We can now use the computed value outside of the function
print(sum)
```

**Predict, then run.** What does it print?

```py
print(add(12, add(5, 3)))
```

**<details><summary>Answer</summary>**

The output is `20`. The function calls are evaluated (a.ka.a "resolve") in this order:

- `add(5, 3)` resolves to `8`
- `add(12, 8)` resolves to `20`
- `print(20)` prints 20

</details>

{% hint style="warning" %}
**Predict, then run.** What does this print? There are two lines of output.

```python
def say_hello(name):
    print(f"Hello, {name}!")

result = say_hello("Ada")
print(result)
```

<details><summary>What actually happens</summary>

```
Hello, Ada!
None
```

Every function call produces a value, even one with no `return` statement. When a function ends without returning anything, the value it produces is `None`. `say_hello` printed its greeting and then handed back `None`, which is what got stored in `result`.

This is the single most common mistake with functions: writing `print` where you meant `return`, and then wondering why the variable you saved the result in is empty. `print` shows a value to the human at the Terminal. `return` hands a value back to the program. They are different jobs.

</details>
{% endhint %}

### Default Values and Keyword Arguments

There is some flexibility in how a function's parameters are set up.

A parameter can be given a **default value**. If the caller leaves that argument out, the default is used:

```python
def say_hello(name="friend", hobby="code"):
    print(f"Hi, my name is {name}. I like to {hobby}!")

say_hello()
# Output: Hi, my name is friend. I like to code!

say_hello("Ben", "rock climb")
# Output: Hi, my name is Ben. I like to rock climb!
```

Arguments can also be passed by **keyword**, naming the parameter they belong to. When you do, the order no longer matters:

```python
say_hello(hobby="play the bass", name="Gonzalo")
# Output: Hi, my name is Gonzalo. I like to play the bass!
```

You may recall seeing keyword arguments in chapter 1. `print("a", "b", sep="-")` passes `"a"` and `"b"` by position and `sep` (separator) by keyword. `sep` has a default value of a single space, which is why you never had to write it before.

**Challenge:** Which of these calls work, and what do they print? Which one crashes, and why?

```python
def make_greeting(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

print(make_greeting("Ada"))
print(make_greeting("Ada", "?"))
print(make_greeting(punctuation="...", name="Ada"))
print(make_greeting())
```

**<details><summary>Answer</summary>**

The first three work:

```
Hello, Ada!
Hello, Ada?
Hello, Ada...
```

The last one crashes with `TypeError: make_greeting() missing 1 required positional argument: 'name'`. `punctuation` has a default, so it can be left out. `name` does not, so it cannot.

</details>

## Functions Create Local Variable Scope

**Scope** refers to where a variable is assigned. The scope of the variable impacts the "reachability" of the variable (where it can be referenced).

For example, a variable assigned in the **scope** of a function can only be referenced within that function. It is not reachable outside of the function.

```python
def print_x():
    # x is reachable anywhere in this function
    x = 10

    print(x)

print_x()

print(x)  # NameError: name 'x' is not defined
```

Variables can be assigned at the following levels of scope, listed from the least reachability to the most reachability:

- **Local Variables** — Variables and parameters assigned within a function. They exist only while that function is running.
- **Global Variables** — Variables assigned in a file, outside of any function. Reachable anywhere in that file.
- **Built-in Names** — Names provided by Python itself, like `print`, `len`, and `type`. Reachable everywhere. Avoid reassigning these.

Scopes can contain other scopes. For example, a file can contain a function and functions can contain inner functions. Variables declared in the "outer" scope can be referenced anywhere within the "inner" scopes, but not vice-versa.

```python
# my_name is global. Reachable anywhere in this file.
my_name = 'Jayson'

def say_hi():
    # `my_name` is reachable anywhere within this file, even in lower scopes like in this function
    print(f"Hi, my name is {my_name}")

say_hi() # prints "Hi, my name is Jayson"

def greet_friend(friend):
    # Parameters like `friend` are local. Reachable anywhere in this function.

    if friend == "":
        # message is local to greet_friend. It can't be accessed outside of the function
        message = "I can't say hi if I don't know your name!"
    else:
        # This is the same variable as the one above, assigned a different value.
        message = f"Hi, {friend}, I'm {my_name}. Nice to meet you."

    # message is still reachable here, after the if/else is finished.
    print(message)

greet_friend("")
# Output: I can't say hi if I don't know your name!

greet_friend('Jane')
# Output: "Hi, Jane, I'm Jayson. Nice to meet you."
```

{% hint style="warning" %}
**Predict, then run.** Add this line to the very bottom of the file above. What happens?

```python
print(message, my_name)
```

<details><summary>What actually happens</summary>

```
NameError: name 'message' is not defined
```

Both greetings print first, because the program runs top to bottom and the error is on the last line. Then the interpreter looks for `message` in the global scope and cannot find it. `message` was local to `greet_friend`, and it stopped existing the moment `greet_friend` returned.

Notice what did _not_ cause an error: `print(message)` inside `greet_friend`, after the `if`/`else`. The `if` block did not hide `message` from the rest of the function.

</details>
{% endhint %}

When a variable that is out of scope is referenced, a `NameError` is raised.

{% hint style="info" %}
As a best practice, aim to declare variables in the lowest possible scope where the variable is needed (local rather than global).

For example, in the code snippet above, we must declare the `my_name` variable in the global scope since it is referenced in both the `say_hi` function and `greet_friend` function.

`message`, on the other hand, is only needed inside `greet_friend`, so it lives there. Assigning it once in each branch of the `if`/`else` and printing it once afterward is the natural shape for this kind of function in Python, and it avoids repeating the `print` call.
{% endhint %}

**<details><summary>Q: Why is it even possible to have two variables called `message` in the same program?</summary>**

```python
def greet_friend(friend):
    message = f"Hi, {friend}!"
    print(message)

def say_goodbye(friend):
    message = f"Bye, {friend}!"
    print(message)
```

We can have two variables with the same name as long as they are in different scopes. This is the entire point of scope! Each function gets its own `message`, and neither can see or overwrite the other's. Without scope, every function in a program would have to invent a unique name for every one of its variables.

</details>

### Order Matters: Assign Before You Use

A name has to be assigned before the line that uses it runs. This sounds obvious, but it has one consequence that trips people up with functions.

{% hint style="warning" %}
**Predict, then run.** Write down what each of these two programs prints.

Program 1:

```python
say_hi()

def say_hi():
    print("hi")
```

Program 2:

```python
def say_hi():
    wave()

def wave():
    print("👋")

say_hi()
```

<details><summary>What actually happens</summary>

Program 1 crashes with `NameError: name 'say_hi' is not defined`. When line 1 runs, the `def` on line 3 has not run yet, so the name `say_hi` does not exist.

Program 2 works and prints 👋. Defining `say_hi` does not run its body, so the reference to `wave` inside it is not looked up until `say_hi()` is called on the last line. By then, both functions exist.

The rule is the same in both cases: a name is looked up at the moment the line using it _runs_, not the moment it is written. That is why the convention is to put every `def` at the top of a file and every function call at the bottom.

</details>
{% endhint %}

### The `global` Keyword

Reading a global variable inside a function is fine.

```py
# A global that a function reads.
greeting = "Hello"

def greet(name):
    print(f"{greeting}, {name}!")

greet("Reuben")
```

Changing a global variable is where trouble starts.

{% hint style="warning" %}
**Predict, then run.**

```python
count = 0

def increment():
    count = count + 1

increment()
print(count)
```

<details><summary>What actually happens</summary>

```
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

The moment Python sees `count = ...` inside `increment`, it decides that `count` is a _local_ variable of `increment`. Then it tries to evaluate `count + 1` using that local variable, which has not been given a value yet. It never even looks at the global `count`.

You can force Python to use the global one by adding `global count` as the first line of the function. **Do not.** A function that reaches out and changes variables that live outside of it is a function whose behavior you cannot predict by reading it. Pass the value in as a parameter and `return` the new value instead. We'll see exactly why in the chapter on lists, where these functions get a name: impure.

</details>
{% endhint %}
