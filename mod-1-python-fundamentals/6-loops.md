# 1.6 Loops

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/06-loops/)
{% endhint %}

**Table of Contents**:

- [Key Terms](#key-terms)
- [Intro to Iteration](#intro-to-iteration)
- [The `for` loop](#the-for-loop)
  - [Looping Over a String](#looping-over-a-string)
  - [Looping a Number of Times with `range()`](#looping-a-number-of-times-with-range)
  - [Changing the Starting Point for `range()`](#changing-the-starting-point-for-range)
  - [For Loop Challenge](#for-loop-challenge)
- [While Loops](#while-loops)
  - [Asking Until the Input Is Valid](#asking-until-the-input-is-valid)
  - [Break and Continue](#break-and-continue)
  - [While Loop Challenge](#while-loop-challenge)
- [Summary](#summary)

## Key Terms

- **Loops** allow you to repeat code multiple times, making it easy to automate repetitive tasks and process collections of data.
- The **`for` loop** runs its code block once for each element of an iterable. Paired with **`range()`**, it repeats a process a known number of times.
- An **iterable** is any value a `for` loop can walk through one element at a time. A `range()` and a string are both iterables.
- **Iterating** over an iterable means going through its elements one at a time, running the loop's code block once for each element.
- The **`while` loop** is useful for repeating a process an unknown number of times, continuing until a condition is no longer true.
- **Infinite loops** occur when the loop's condition never becomes false; use `break` to exit early and `continue` to skip to the next iteration.

## Intro to Iteration

**Iteration** is the repetition of a process, getting closer to some result each time.

Picture this: someone asks you to count the vowels in a word. To do this you will:

- Keep a mental tally (starting at 0)
- Scan through each character in the word
  - If you see a vowel: update the tally (add 1)
  - If you've reached the end of the word: stop

You could write a program that does the same thing with the string tools from chapter 1.5, checking one letter with each `if` statement:

```python
word = input("Give me a word: ").strip().lower()

vowels = 0
if word[0] in "aeiou":
    vowels += 1
if word[1] in "aeiou":
    vowels += 1
if word[2] in "aeiou":
    vowels += 1
if word[3] in "aeiou":
    vowels += 1

print(f"{word} has {vowels} vowels.")
```

This program has two problems, and both come from the same cause: **the program cannot know in advance how long a word the user will type.**

- If the user types `ada`, the program crashes with an `IndexError` at `word[3]`, because a three-letter word has no index `3`.
- If the user types `lovelace`, the program checks only the first four letters, so it reports 2 vowels instead of 4.

Adding more `if` statements does not fix it, because every length of word needs a different number of them.

## The `for` loop

A `for` loop runs its code block once for each "element" in an "iterable" value such as a string. The "elements" of a string are its characters, so a `for` loop over a string runs once for each character:

```python
for letter in "hello":
    print(letter)

# h
# e
# l
# l
# o
```

Each time through the loop, Python does these steps in order:

| Loop # | 1. Take the next element from the iterable and assign it to the variable | 2. Execute the code block | 3. If the iterable has more elements, go to step 1. Otherwise, exit |
| ------ | ------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------- |
| 1      | `letter = "h"` →                                                         | `print("h")` →            | Back to step 1. Go to loop 2 ↩                                      |
| 2      | `letter = "e"` →                                                         | `print("e")` →            | Back to step 1. Go to loop 3 ↩                                      |
| 3      | `letter = "l"` →                                                         | `print("l")` →            | Back to step 1. Go to loop 4 ↩                                      |
| 4      | `letter = "l"` →                                                         | `print("l")` →            | Back to step 1. Go to loop 5 ↩                                      |
| 5      | `letter = "o"` →                                                         | `print("o")` →            | All done! 🎉                                                        |

{% hint style="info" %}
💡 Anything a `for` loop can walk through one element at a time like this is called an **iterable**, and going through its elements one at a time is called **iterating** over it. A string is an iterable of characters. Later in this chapter you will meet `range()`, which produces an iterable of numbers, and in chapter 1.7, we'll go over lists, which are iterables too.
{% endhint %}

Every `for` loop has the same form, whatever it iterates over:

```
for variable_name in iterable:
    # code block
```

- `for` and `in` are keywords that every `for` loop uses.
- `variable_name` is the name of a variable that the loop creates. You choose this name, just as you choose the name of any other variable.
- `iterable` is the value the loop walks through, such as a string, list, or an iterable produced by `range()`.
- The colon and the indented code block work the same way as they do in an `if` or `def` statement.

{% hint style="warning" %}
**Predict, then run.** The variable names in these loops do not match what the loops iterate over. Does each loop run? What does each one print?

```python
for number in "abc":
    print(number)

for letter in "123":
    print(letter)
```

<details><summary>What actually happens</summary>

```
a
b
c
1
2
3
```

- Both loops run, because Python does not read the meaning of a variable name. `number` and `letter` are labels that the programmer chose.
- `"abc"` is a string, so on each pass `number` holds the next character: `"a"`, then `"b"`, then `"c"`.
- `"123"` is also a string, so `letter` holds the strings `"1"`, `"2"`, and `"3"`, not numbers.

Python never checks whether a name makes sense, so the name is there for the people who read the code. Choose a name that describes what the variable will hold, such as `letter` for the characters of a word, so that the next person who reads your code, including you, can tell what it holds.

</details>
{% endhint %}

### Looping Over a String

With a `for` loop, the vowel counter checks every letter of the word, however many letters there are:

```python
word = input("Give me a word: ").strip().lower()

vowels = 0
for letter in word:
    if letter in "aeiou":
        vowels += 1

print(f"{word} has {vowels} vowels.")
```

The loop runs once for each character, so `ada` gets three checks and `lovelace` gets eight, and the program never asks for an index that does not exist. `strip()` and `lower()` clean the input first, so `letter in "aeiou"` also counts capital vowels such as the `A` in `Ada`.

### Looping a Number of Times with `range()`

Not every repetition has a string to walk through. Picture this: you are assigned the task of rolling a 6-sided die 100 times and documenting the result of each.

```
1. a 4 was rolled
2. a 2 was rolled
3. a 6 was rolled
4. a 6 was rolled
5. a 1 was rolled
...
```

We can write code to do this one roll at a time, but this becomes very repetitive:

```python
import random

print(f"1. a {random.randint(1, 6)} was rolled")
print(f"2. a {random.randint(1, 6)} was rolled")
print(f"3. a {random.randint(1, 6)} was rolled")
print(f"4. a {random.randint(1, 6)} was rolled")
print(f"5. a {random.randint(1, 6)} was rolled")
# and so on until you reach 100! 🫠
```

{% hint style="info" %}
💡 The first line, `import random`, loads a tool that comes with Python, and `random.randint(1, 6)` returns a random integer between 1 and 6 (including 1 and 6). Chapter 1.9 explains how importing works, but for now, just focus on what `random.randint(1, 6)` does.
{% endhint %}

This time there is no string to iterate over, only a number of times to repeat. The `range(stop)` function fills that gap by producing an iterable of numbers starting at `0` and ending before the given `stop` value: `range(100)` produces the numbers `0`, `1`, `2`, ... up to `99`.

A `for` loop over `range(100)` therefore runs 100 times.

**Predict, then run.** What is the first number assigned to `roll_number` and what is the last number?

```python
for roll_number in range(100):
    print(f"{roll_number + 1}. a {random.randint(1, 6)} was rolled")
```

<details><summary>What actually happens</summary>

100 lines:

```
1. a 4 was rolled
2. a 2 was rolled
3. a 6 was rolled
...
99. a 1 was rolled
100. a 6 was rolled
```

Notice that the first value that `roll_number` gets from `range(100)` is `0` and the last number is `99`, not `100`! That's why we print `roll_number + 1` to have the number of rolls start at `1` in the output and end at `100`.

Counting from zero is the convention in Python.

</details>

### Changing the Starting Point for `range()`

`range()` can take a starting point and a step size as well, but note that the `stop` will always be excluded from the range:

```python
for i in range(1, 101):      # 1, 2, 3, ... 100
    print(f"{i}. a {random.randint(1, 6)} was rolled")

for i in range(0, 20, 5):    # 0, 5, 10, 15
    print(i)

for i in range(10, 0, -1):   # 10, 9, 8, ... 1
    print(i)
```

{% hint style="warning" %}

Because `range()` produces numbers, it can also produce the indexes of a string. This is one of the main reasons why `range()` starts counting at `0`!

**Predict, then run.** This loop iterates over a `range()` instead of over the string itself. It uses the variable `i` (short for "index") to hold each number in `range(len(word))`.

```python
word = "loop"
for i in range(len(word)):
    print(i, word[i])
```

<details><summary>What actually happens</summary>

```
0 l
1 o
2 o
3 p
```

- `len(word)` is `4`, so `range(len(word))` produces `0`, `1`, `2`, and `3`, which are exactly the indexes of `word`.
- On each pass, `i` holds one index, and `word[i]` uses bracket notation to get the character at that index.

Iterating over `range(len(word))` gives you each character's position as well as the character. When you need only the characters, `for letter in word` is shorter and leaves no index for you to get wrong.

</details>
{% endhint %}

### For Loop Challenge

Write a function called `count_heads` that does the following:

1. Takes in a number of flips as a parameter.
2. Flips a coin that many times, keeping count of how many times heads was flipped.
3. Prints back the final number of heads like this:

```
You flipped [heads flipped] heads out of [total] flips! That is [percent]%!
```

Here is some starter code. A function body cannot be empty, so the starter code uses `pass`, a statement that does nothing, to hold its place until you write your own code:

```python
import random

def flip_coin():
    flip_result = random.randint(0, 1)
    return "heads" if flip_result == 1 else "tails"

def count_heads(flips):
    pass  # replace this line with your code

count_heads(10)
count_heads(100)
```

**<details><summary>Check out the solution!</summary>**

```python
import random

def flip_coin():
    flip_result = random.randint(0, 1)
    return "heads" if flip_result == 1 else "tails"

def count_heads(flips):
    # Create heads before the loop. If heads = 0 were inside the loop, it would reset to 0 on every flip, and the count could never get past 1.
    heads = 0
    for i in range(flips):
        result = flip_coin()
        heads += 1 if result == 'heads' else 0

    print(f"You flipped {heads} heads out of {flips} flips! That is {heads / flips * 100:.1f}%!")

count_heads(10)
count_heads(100)
```

The `:.1f` format specifier from chapter 1.5 displays the percentage with one digit after the decimal point. Run it a few times. With 10 flips, the percentage jumps around a lot from run to run. With 100 flips, the percentage usually lands closer to 50.

</details>

## While Loops

A `for` loop runs a known number of times. You provide it an iterable, and it runs once for each element until that iterable runs out.

A `while` loop repeats its code block for as long as its condition is `True`. Think of it like an `if` statement that repeats itself. One of the most common use-cases for `while` loops is to create an infinitely prompting REPL program that takes in user input until they type a message like `"Exit"`:

```py
user_input = None # user hasn't typed in anything yet
while (user_input != "Exit"):
    user_input = input("type something and hit enter: ")
    print(f"you typed: {user_input}")

print("Good bye!")
```

Before each pass, Python checks the condition (`user_input != "Exit"`). If the condition is `True`, the block runs again. If the condition is `False`, the loop ends and the program continues with the code after it. That makes `while` loops the right tool for repeating a process an _unknown_ number of times, like rolling a die _until_ you get a 6.

```py
import random

roll = None
roll_count = 0
while (roll != 6):
    roll = random.randint(1, 6)
    roll_count += 1

print(f"It took {roll_count} rolls to get a 6!")
```

### Asking Until the Input Is Valid

In chapter 1.5, a program that asked for an age could validate the answer with `isdigit()`, but when the answer was not a number, all it could do was print a message and stop. The user had to run the program again to get another try. A `while` loop can ask again instead, as many times as it takes, because the program cannot know in advance how many wrong answers the user will type:

```python
age = input("How old are you? ").strip()

while not age.isdigit():
    print(f"Sorry, {age} is not a number")
    age = input("How old are you? ").strip()

age = int(age)
print(f"Next year you will be {age + 1}")
```

The loop runs only while `age` fails validation, so by the time the program reaches `int(age)`, `age` is guaranteed to hold digits, and the cast cannot crash.

### Break and Continue

The validation loop above writes the same `input()` line twice: once before the loop, so that `age` holds a value the first time the condition is checked, and once inside the loop, to ask again. If the question ever changes, both lines have to change, and a programmer who updates only one of them gives the user two different questions.

Two statements let you control a loop from inside its code block:

- `break` ends the loop immediately, and the program continues with the first line after the loop. `break` is how you get out of a loop whose condition is always `True`.
- `continue` skips the rest of the current pass and jumps back to the top of the loop for the next one. `continue` keeps the loop going, so it cannot get you out of an infinite loop.

With `break`, the validation loop asks its question in one place:

```python
while True:
    age = input("How old are you? ").strip()
    if age.isdigit():
        break
    print(f"Sorry, {age} is not a number")

age = int(age)
print(f"Next year you will be {age + 1}")
```

`while True` is always true, so the condition never ends this loop. The only way out is the `break`, which runs only when the user has typed a number.

Here is a program that uses both. It adds up the dollar amounts the user types until they type `done`. For now, the program assumes that every answer is either a number, `done`, or blank:

```python
total = 0

while True:
    amount = input("Enter an amount in dollars (like 4.50), or done to finish: ").strip().lower()
    if amount == "done":
        break

    if amount == "":
        continue

    total += float(amount)

print(f"Your total is ${total:.2f}")
```

Nobody knows in advance how many amounts the user will enter, which is exactly the job a `while` loop is for. `while True` never ends the loop by itself, so the two statements inside it do that work:

- `break` runs when the user types `done`. The loop ends, and the program continues with the `print()` after the loop.
- `continue` runs when the user presses Enter without typing an amount. In that case, `input()` returns an empty string, and `float("")` would crash with a `ValueError`. `continue` skips the rest of the pass, so `float(amount)` never receives the empty string, and the loop goes straight back to asking for the next amount.

{% hint style="info" %}
**Q: How is `break` different from `return`?** `break` ends the loop, and the program carries on with the first line after the loop. `return` ends the whole function the loop is inside, so any lines after the loop in that function never run. If the dollar program above were the body of a function and used `return` instead of `break`, the function would end as soon as the user typed `done`, and `Your total is ...` would never print.
{% endhint %}

{% hint style="info" %}
If the condition never becomes `False`, the loop never ends. This is called an **infinite loop**, and the program runs forever.

If you do end up in an infinite loop, `Control+C` in the Terminal stops the program. You will see a `KeyboardInterrupt` message. `KeyboardInterrupt` is Python reporting that you stopped the program from the keyboard. Nothing is wrong with your computer.
{% endhint %}

### While Loop Challenge

Write a number guessing game program that:

1. Generates a random number from 1-10. This is the secret number.
2. Asks the user to guess the number using the `input()` function.
3. If the guess is correct, prints a winning message and ends the program.
4. If the guess is incorrect, asks the user to guess again.
5. If the user ever types `"Exit"`, ends the program.

**Bonus Features**

1. Keep track of the guesses, and when the guess is correct, print how many guesses it took.
2. Limit the user to 5 guesses. If they guess incorrectly 5 times, they lose! (you'll need to use `break`)

**<details><summary>Check out the solution!</summary>**

```python
import random

random_num = random.randint(1, 10)
print("I'm thinking of a random number. Guess what it is!")

# The while condition below checks guess before the first guess is made, so guess has to exist already.
# Without this line, Python stops with NameError: name 'guess' is not defined.
guess = None
guesses = 0

# Keep asking until the user types "Exit". A correct guess or running out of guesses ends the loop early with break.
while guess != "Exit":
    # Bonus feature 2: break exits the loop early
    if guesses == 5:
        print("Out of guesses :(")
        break

    guess = input("What is your guess? ").strip()
    guesses += 1
    # input() returns a string, so validate the guess with isdigit() and cast it with int() before comparing it to random_num.
    # Without the cast, "7" == 7 is False, and no guess could ever win.
    if guess.isdigit() and int(guess) == random_num:
        print(f"{guess}! Got it!! And it only took you {guesses}!!!")
        break
    else:
        print("That isn't it! Try again!")


print("Thanks for playing!")
```

</details>

## Summary

A loop lets a program repeat a block of code without the programmer writing that block out again. Which loop to use depends on what the program knows before it starts. When the number of repetitions is known, such as 100 rolls or every character in a string, a `for` loop walks through an iterable. When the program has to keep going until something happens, such as rolling a 6 or the user typing `Exit`, a `while` loop repeats for as long as its condition is `True`. Either way, the programmer decides what changes from one pass to the next and when the loop stops, and `break` and `continue` let the code inside a loop end the loop early or skip the rest of a pass.
