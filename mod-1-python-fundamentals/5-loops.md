# 1.5 Loops

**Table of Contents**:

- [Key Terms](#key-terms)
- [Intro to Iteration](#intro-to-iteration)
- [The `for` loop](#the-for-loop)
  - [For Loop Challenge:](#for-loop-challenge)
- [While Loops and Infinite Loops](#while-loops-and-infinite-loops)
  - [While Loop Challenge](#while-loop-challenge)
- [Nested Loops](#nested-loops)

## Key Terms

- **Loops** allow you to repeat code multiple times, making it easy to automate repetitive tasks and process collections of data.
- The **`for` loop** with **`range()`** is best for repeating a process a known number of times, such as counting.
- An **iterable** is any value a `for` loop can walk through one element at a time. A `range()` and a string are both iterables.
- The **`while` loop** is useful for repeating a process an unknown number of times, continuing until a condition is no longer true.
- **Infinite loops** occur when the loop's condition never becomes false; use `break` to exit early and `continue` to skip to the next iteration.
- **Nested loops** let you loop inside another loop, useful for working with multi-dimensional data or complex processes.
- Loop challenges help you practice using loops to solve real problems, such as counting results or repeating until something happens.

## Intro to Iteration

**Iteration** is the repetition of a process, getting closer to some result each time.

You are assigned the task of flipping a coin 100 times and documenting the result of each. To do this you will:

1. Gather your materials (pen, paper, a coin)
2. Until you've flipped 100 times you will:
   1. flip a coin
   2. record the result by writing: `"flip number [flip number] was [heads|tails]"`
3. Make sure to increase the `flip number` after each flip.

Doing this by hand certainly would take a while. We can write code to likely do it faster:

```python
import random

def flip_coin():
    return random.choice(["heads", "tails"])

print(f"Flip number 1 was {flip_coin()}")
print(f"Flip number 2 was {flip_coin()}")
print(f"Flip number 3 was {flip_coin()}")
print(f"Flip number 4 was {flip_coin()}")
print(f"Flip number 5 was {flip_coin()}")
# and so on until you reach 100! 🫠
```

The first line, `import random`, loads a tool that comes with Python, and `random.choice(["heads", "tails"])` picks one of the two words at random. Chapter 1.9 explains how importing works. For now, it is a coin.

But even so, we have to manually update each number. What a pain! If only there was some way to do this more efficiently.

## The `for` loop

`for` loops are best used to repeat a process a known number of times. Paired with the `range()` function, the syntax looks like this:

```python
for i in range(how_many_times):
    # do something
```

Armed with this syntax, we can easily loop 100 times!

```python
for i in range(100):
    result = flip_coin()
    print(f"Flip number {i} was {result}")
```

`range(100)` produces the numbers `0`, `1`, `2`, ... up to `99`, and `i` takes each one in turn. Try using the debugger and you will see the order of operations

1. Take the next number from the range and assign it to `i`
2. Execute the code block
3. **Go to 1**, until the range runs out

{% hint style="info" %}
Even in the most basic programming languages, the concept of the **GOTO** statement has existed. Programmers used to have to label a specific line with a name like `"StartLoop"` and then write a statement to `Go To StartLoop` if they wanted to repeat a portion of code. In high-level programming languages like Python, that is abstracted away for us by the `for` loop.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** How many lines does this print, and what is the first number and the last number?

```python
for i in range(5):
    print(i)
```

<details><summary>What actually happens</summary>

Five lines: `0`, `1`, `2`, `3`, `4`.

`range(5)` means "five numbers, starting at zero," so the last one is `4`, not `5`. Counting from zero is the convention everywhere in Python, and it means the flip counter above printed "Flip number 0" for the first flip. If you want it to say 1, either print `i + 1` or give `range` a starting point.

</details>
{% endhint %}

`range()` can take a starting point and a step size as well:

```python
for i in range(1, 101):      # 1, 2, 3, ... 100
    print(f"Flip number {i} was {flip_coin()}")

for i in range(0, 20, 5):    # 0, 5, 10, 15
    print(i)

for i in range(10, 0, -1):   # 10, 9, 8, ... 1
    print(i)
```

`for` can also walk through the characters of a string, one at a time, with no `range()` at all:

```python
for letter in "hello":
    print(letter)

# h
# e
# l
# l
# o
```

Anything a `for` loop can walk through one element at a time like this is called an **iterable**. A `range()` is an iterable of numbers, and a string is an iterable of characters. In chapter 1.7, the same loop walks through the elements of a list, because lists are iterables too.

### For Loop Challenge:

Write a function called `count_heads` that does the following:

1. Takes in a number of flips as a parameter.
2. Flips a coin that many times, keeping count of how many times heads was flipped.
3. Prints back the final number of heads like this:

```
You flipped [heads flipped] heads out of [total] flips! That is [percent]%!
```

Here is some starter code:

```python
import random

def flip_coin():
    return random.choice(["heads", "tails"])

def count_heads(flips):
    # add your code here

count_heads(10)
count_heads(100)
```

**<details><summary>Check out the solution!</summary>**

```python
import random

def flip_coin():
    return random.choice(["heads", "tails"])

def count_heads(flips):
    # We want to use this variable after the loop is done, so we create it outside the loop
    heads = 0
    for i in range(flips):
        result = flip_coin()
        heads += 1 if result == 'heads' else 0

    print(f"You flipped {heads} heads out of {flips}. Thats {heads / flips * 100}%!")

count_heads(10)
count_heads(100)
```

Run it a few times. The more flips you ask for, the closer the percentage gets to 50.

</details>

## While Loops and Infinite Loops

An **infinite loop** is one in which the condition is ALWAYS `True`. This will cause a program to run forever, either depleting resources or just causing the computer to stall while it waits for the program to end.

Infinite loops are most often created using `while` loops which are best used to repeat a process an _unknown_ number of times.

To ensure that a loop does not go on infinitely, we use these two statements:

- `break` prematurely breaks out of a loop
- `continue` prematurely goes to the next iteration of the loop

```python
import random

while True:
    roll = random.randint(1, 6)
    if roll == 6:
        print("A 6! Bye!")
        break  # <--- how is this different from return??
    if roll % 2 == 1:
        print(f"{roll} is odd. Skipping it.")
        continue
    print(f"{roll}? That's a great number!")

print("See you next time!")
```

`random.randint(1, 6)` rolls a six-sided die. Nobody knows in advance how many rolls it will take to get a 6, which is exactly the job a `while` loop is for. `while True` is always true, so the only way out of this loop is the `break`.

{% hint style="info" %}
**Q: How is `break` different from `return`?** A `break` statement will exit the current loop and continue executing code that follows the loop. A `return` statement inside of a loop will exit the current loop AND the current function being executed.
{% endhint %}

{% hint style="info" %}
If you do end up in an infinite loop, `Control+C` in the Terminal stops the program. You will see a `KeyboardInterrupt` message. That is Python telling you that you interrupted it, not that anything is wrong with your computer.
{% endhint %}

### While Loop Challenge

Write a program in which the computer plays a guessing game against itself:

1. Generates a random number from 1-10. This is the secret number.
2. Guesses a random number from 1-10 and prints the guess.
3. If the guess is correct, print a message and end the program.
4. If it is incorrect, guess again.

**Bonus Features**

1. Keep track of the guesses, and when the guess is correct, print how many guesses it took.
2. Limit the computer to 5 guesses. If it guesses 5 times incorrectly, it loses!

**<details><summary>Check out the solution!</summary>**

```python
import random

random_num = random.randint(1, 10)
print("I'm thinking of a random number. Let me guess what it is!")

# We're going to pull out this `guess` value so we can check it on every loop
guess = None

# We're also going to keep track of remaining guesses
guesses_remaining = 5

# As long as the guess doesn't match the random number above
while guess != random_num:
    guess = random.randint(1, 10)
    guesses_remaining -= 1

    # If the guess matches, celebrate and exit the loop
    if guess == random_num:
        print(f"{guess}! Got it!! And with {guesses_remaining} guesses to spare!!!")
        break

    # Assuming we didn't exit the loop, break the bad news
    print(f"{guess}? That's a great number! But not mine!")

    # And do a final check to see if the game keeps going!
    if guesses_remaining == 0:
        print("Out of guesses :(")
        break

print("Thanks for playing!")
```

In chapter 1.6 you will learn to read what the user types, and you can come back and let a person make the guesses.

</details>

## Nested Loops

A **nested loop** is a loop written inside the body of another loop. For each iteration of the outer loop, the inner loop will complete ALL of its iterations.

```python
# The outer loops runs 3 times, for i = 0 through i = 2
for i in range(3):

    # This statement is executed 3 times, once per outer loop.
    print(f"Outer loop {i}:")

    # The inner loop runs 5 times, for j = 0 through j = 4
    for j in range(5):
        # This statement is executed a total of 15 times, 5 times per outer loop
        print(f"  {i} - {j}")

# Outer loop 0:
#   0 - 0
#   0 - 1
#   0 - 2
#   0 - 3
#   0 - 4
# Outer loop 1:
#   1 - 0
#   1 - 1
#   1 - 2
#   1 - 3
#   1 - 4
# Outer loop 2:
#   2 - 0
#   2 - 1
#   2 - 2
#   2 - 3
#   2 - 4
```
