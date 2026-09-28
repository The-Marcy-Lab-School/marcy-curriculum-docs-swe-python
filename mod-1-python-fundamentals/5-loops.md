# 5. Loops

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
- The **`while` loop** is useful for repeating a process an unknown number of times, continuing until a condition is no longer true.
- **Infinite loops** occur when the loop's condition never becomes false; use `break` to exit early and `continue` to skip to the next iteration.
- **Nested loops** let you loop inside another loop, useful for working with multi-dimensional data or complex processes.
- Loop challenges help you practice using loops to solve real problems, such as counting results or building interactive programs.

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

The first line, `import random`, loads a tool that comes with Python, and `random.choice(["heads", "tails"])` picks one of the two words at random. Chapter 6 explains how importing works. For now, it is a coin.

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

`range(5)` means "five numbers, starting at zero," so the last one is `4`, not `5`. This is the same reason the first character of a string is at index `0`. Counting from zero is the convention everywhere in Python, and it means the flip counter above printed "Flip number 0" for the first flip. If you want it to say 1, either print `i + 1` or give `range` a starting point.

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

In chapter 8, the same loop walks through the elements of a list.

### For Loop Challenge:

Write a program that does the following:

1. Asks the user to enter a number.
2. Flips a coin that many times, keeping count of how many times heads was flipped.
3. Prints back the final number of heads to the user like this:

```
You flipped [heads flipped] heads out of [total] flips! That is [percent]%!
```

Here is some starter code:

```python
import random

def flip_coin():
    return random.choice(["heads", "tails"])

def main():
    flips = input('How many times do you want to flip the coin? ')

    # a guard clause that makes sure they entered a number
    if not flips.isdigit():
        print(f"Sorry, {flips} is not a number")
        return

    # add your code here

main()
```

**<details><summary>Check out the solution!</summary>**

```python
import random

def flip_coin():
    return random.choice(["heads", "tails"])

def main():
    # ask the user for flips
    flips = input('How many times do you want to flip the coin? ')

    # make sure they entered a number
    if not flips.isdigit():
        print(f"Sorry, {flips} is not a number")
        return

    # input() gave us a string. We need a number to count with.
    flips = int(flips)

    # We want to use this variable after the loop is done, so we create it outside the loop
    heads = 0
    for i in range(flips):
        result = flip_coin()
        heads += 1 if result == 'heads' else 0

    print(f"You flipped {heads} heads out of {flips}. Thats {heads / flips * 100}%!")

main()
```

</details>

## While Loops and Infinite Loops

An **infinite loop** is one in which the condition is ALWAYS `True`. This will cause a program to run forever, either depleting resources or just causing the computer to stall while it waits for the program to end.

Infinite loops are most often created using `while` loops which are best used to repeat a process an _unknown_ number of times.

To ensure that a loop does not go on infinitely, we use these two statements:

- `break` prematurely breaks out of a loop
- `continue` prematurely goes to the next iteration of the loop

```python
while True:
    user_input = input("Enter a number or q to quit: ")
    if user_input == "q":
        print("Bye!")
        break  # <--- how is this different from return??
    if not user_input.isdigit():
        print("please enter a number")
        continue
    print(f"{user_input}? That's a great number!")

print("See you next time!")
```

{% hint style="info" %}
**Q: How is `break` different from `return`?** A `break` statement will exit the current loop and continue executing code that follows the loop. A `return` statement inside of a loop will exit the current loop AND the current function being executed.
{% endhint %}

{% hint style="info" %}
If you do end up in an infinite loop, `Control+C` in the Terminal stops the program. You will see a `KeyboardInterrupt` message. That is Python telling you that you interrupted it, not that anything is wrong with your computer.
{% endhint %}

### While Loop Challenge

Write a program that does the following:

1. Generates a random number from 1-10.
2. Asks the user to guess the number.
3. If the user is correct, print a message congratulating them and end the program.
4. If they are incorrect, ask them again.

**Bonus Features**

1. Keep track of their guesses and when they guess correctly, tell them how many guesses it took for them to get it right.
2. Limit their guesses to 5 guesses. If they guess 5 times incorrectly, they lose!

**<details><summary>Check out the solution!</summary>**

```python
import random

random_num = random.randint(1, 10)
print("I'm thinking of a random number. Guess what it is!")

# We're going to pull out this `guess` value so we can check it on every loop
guess = None

# We're also going to keep track of remaining guesses
guesses_remaining = 5

# As long as the guess doesn't match the random number above
while guess != random_num:
    # Get the user input and do some input checking
    user_input = input("Enter a number or q to quit: ")
    if user_input == "q":
        print("Bye!")
        break
    if not user_input.isdigit():
        print("please enter a number")
        continue

    # Now that we know we've got a number, we can convert it and decrement the guesses
    guess = int(user_input)
    guesses_remaining -= 1

    # If the guess matches, congratulate the user and exit the loop
    if guess == random_num:
        print(f"You got it!! And with {guesses_remaining} guesses to spare!!!")
        break

    # Assuming we didn't exit the loop, break them the bad news
    print(f"{guess}? That's a great number! But not mine!")

    # And do a final check to see if they will keep going!
    if guesses_remaining == 0:
        print("Sorry, you've ran out of luck :(")
        break

print("Thanks for playing!")
```

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
