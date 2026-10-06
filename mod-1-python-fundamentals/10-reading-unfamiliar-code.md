# 1.10 Reading Unfamiliar Code

Every chapter so far has asked you to write code. This one asks you to read it. Specifically, to read code that somebody else wrote, that you have never seen before, and to come away knowing what it does and how it does it.

This is not a break from learning to program. It is the single most common thing a working engineer does all day. Starting in Q2, the code you spend most of your time with will have been written by a teammate, by the author of a library you installed, or by an AI model, and your job will be to understand it well enough to change it, fix it, or reject it. This chapter gives you a method for that, and you will practice it on a program that uses only what you have learned so far, plus a couple of things you have not.

**Table of Contents:**

- [Key Terms](#key-terms)
- [The Orientation Questions](#the-orientation-questions)
- [A Method for Reading Code You Did Not Write](#a-method-for-reading-code-you-did-not-write)
  - [Step 1: Run It Before You Read It](#step-1-run-it-before-you-read-it)
  - [Step 2: Find the Entry Point and Map the Files](#step-2-find-the-entry-point-and-map-the-files)
  - [Step 3: Find the Data](#step-3-find-the-data)
  - [Step 4: Trace One Action From Input to Output](#step-4-trace-one-action-from-input-to-output)
  - [Step 5: Predict, Then Run, Function by Function](#step-5-predict-then-run-function-by-function)
  - [Step 6: Write Down What You Know and What You Are Guessing](#step-6-write-down-what-you-know-and-what-you-are-guessing)
- [Worked Example: The Corner Shop](#worked-example-the-corner-shop)
  - [Step 1: Run It](#step-1-run-it)
  - [Step 2: The Entry Point and the Map](#step-2-the-entry-point-and-the-map)
  - [Step 3: The Data](#step-3-the-data)
  - [Step 4: Trace One Action](#step-4-trace-one-action)
  - [Step 5: Predict, Then Run](#step-5-predict-then-run)
  - [Step 6: Know vs. Guess](#step-6-know-vs-guess)
- [Reading Code a Model Wrote](#reading-code-a-model-wrote)
- [Practice: The Bill Splitter](#practice-the-bill-splitter)

## Key Terms

- Reading code means **building a model of someone else's intent** from the artifacts they left behind: files, names, and behavior. You are not trying to memorize the code. You are trying to be able to predict it.
- The **orientation questions** give you a place to stand before you dive in: what is this supposed to do, where does the behavior show up, which files matter, what do I know versus what am I guessing.
- The method has six steps: **run it, find the entry point, find the data, trace one action, predict then run, and write down what you know and what you are guessing**.
- Names are the author's notes to you. A function's name and its parameters tell you its intent; the body tells you whether it lives up to it.
- Reading code a model wrote is the same activity with more suspicion. Generated code is confident and plausible, and plausible is not the same as correct.

## The Orientation Questions

When you open an unfamiliar program, the danger is not that you will fail to understand it. The danger is that you will start changing things before you understand it, get lost, and not be able to say afterward what you changed or why. Engineers call this **thrashing**.

Before you touch anything, be able to answer these six questions. Write the answers down. Some of them will be "I don't know yet," and that is a fine answer, because it is honest.

1. **What is this program supposed to do?** One sentence, from the point of view of the person using it.
2. **Where does the behavior show up?** Which output, which prompt, which message on the screen?
3. **What files seem relevant?** Which one starts the program, and which ones does it import?
4. **What did I try?** Which inputs did I give it?
5. **What did I observe?** What actually came out?
6. **What do I know versus what am I guessing?** Two lists, kept separate.

The last one is the whole skill in miniature. Confident programmers are not the ones who are never wrong. They are the ones who know which of their beliefs about the code they have checked.

## A Method for Reading Code You Did Not Write

### Step 1: Run It Before You Read It

Before opening a single file, run the program and use it. Give it good input and bad input. Try to break it. You are collecting facts about what it _does_, which is the ground truth that everything you read afterward has to agree with.

If you start by reading, you build a picture of what you _think_ the code does, and then when you run it and something differs, you may not notice, because you already believe you know. Running first means the surprise arrives while you can still see it.

### Step 2: Find the Entry Point and Map the Files

The **entry point** is the file you run with `python3` and, inside it, the function that starts everything. In a Python program you already know what to look for: the `if __name__ == "__main__":` guard, and the `main()` it calls.

List the files. For each one, read only the `import` lines and the `def` lines, and write a single sentence about what that file is _for_. Do not read the bodies yet. You are drawing a map, not walking the territory.

### Step 3: Find the Data

Ask: what does this program remember? Find every variable that lives at the top level of a file (a list, a dictionary, a number) and every dictionary or list that gets built and passed around. Write down its shape. "A dictionary from item names to how many are in stock" is a shape. Once you know the shape of the data, every function becomes a question about what it does _to_ that data, and those questions have short answers.

### Step 4: Trace One Action From Input to Output

Pick one thing a user can do. Start at the entry point and follow that one action through every function it touches, in order, until the output appears. Ignore every other branch. You will come back for them, but trying to hold the whole program in your head at once is how you get lost.

This is the same thing you did in chapter 1.3 when you predicted the order in which a program's `print` lines run, only now the path crosses more functions.

### Step 5: Predict, Then Run, Function by Function

For each function, before you read its body carefully, write down what you think it returns for one specific input. Then check, either by reading the body closely or by importing the module in the REPL and calling the function. Every prediction you get wrong is a place where your model of the code and the code itself disagree, which is exactly the information you were looking for.

You have been doing this in the "Predict, then run" boxes all module. This is where that habit pays off.

### Step 6: Write Down What You Know and What You Are Guessing

At the end, go back to your two lists from the orientation questions. Move things from "guessing" to "know" only when you have checked them by running code. Whatever is left in "guessing" is your list of questions, and it is a much better list than the one you would have written at the start.

## Worked Example: The Corner Shop

Here is a small program. Someone else wrote it. It runs a very small shop's inventory. Do not read it yet. Copy it into two files, `inventory.py` and `main.py`, in a new folder, and then follow the steps.

{% code title="inventory.py" lineNumbers="true" %}

```python
stock = {"apples": 5, "bread": 2, "milk": 0}


def restock(name, quantity):
    stock[name] = stock.get(name, 0) + quantity
    return stock[name]


def sell(name, quantity):
    if name not in stock:
        return False
    if stock[name] < quantity:
        return False
    stock[name] -= quantity
    return True


def report():
    lines = []
    for name, quantity in sorted(stock.items()):
        marker = "" if quantity > 0 else " (out of stock)"
        lines.append(f"{name}: {quantity}{marker}")
    return "\n".join(lines)
```

{% endcode %}

{% code title="main.py" lineNumbers="true" %}

```python
from inventory import restock, sell, report


def main():
    print("Welcome to the corner shop.")
    while True:
        print("\n1. Restock  2. Sell  3. Report  4. Quit")
        choice = input("Choose (1-4): ").strip()
        if choice == "4":
            break
        if choice == "3":
            print(report())
        elif choice in ("1", "2"):
            name = input("Item name: ").strip().lower()
            quantity = input("How many? ").strip()
            if not quantity.isdigit():
                print("Please enter a whole number.")
                continue
            quantity = int(quantity)
            if choice == "1":
                total = restock(name, quantity)
                print(f"Now holding {total} {name}.")
            elif sell(name, quantity):
                print(f"Sold {quantity} {name}.")
            else:
                print(f"Can't sell {quantity} {name}.")
        else:
            print("That isn't an option.")
    print("Goodbye.")


if __name__ == "__main__":
    main()
```

{% endcode %}

### Step 1: Run It

`python3 main.py`. Choose `3`. Restock something. Sell something. Sell something you don't have. Sell more of something than there is. Type a word where a number is expected. Quit.

Write down what you observed for each. Here is one thing you should have seen:

```
Choose (1-4): 3
apples: 5
bread: 2
milk: 0 (out of stock)
```

**<details><summary>Q: You ran it before reading it. Based only on what you saw, what is this program supposed to do? One sentence.</summary>**

Something like: "It keeps track of how many of each item a shop has, lets you add to or sell from the count, and shows the list."

That is your answer to orientation question 1. Notice that you could write it without reading a line of code. Everything you read from here on has to agree with that sentence, or one of them is wrong.

</details>

### Step 2: The Entry Point and the Map

Two files. `main.py` has the `__main__` guard, so it is the entry point, and `main()` is where the program starts. It imports three names from `inventory`.

Reading only the `def` lines:

- `inventory.py` — has a `stock` variable and three functions: `restock`, `sell`, `report`. It is for keeping and changing the stock.
- `main.py` — has one function, `main`. It is for talking to the user and calling the inventory functions.

You have seen this split before. It is the same separation of concerns as `circle_helpers.py` and `main.py` in chapter 1.9.

### Step 3: The Data

There is exactly one piece of data that lives between actions: `stock`, at the top of `inventory.py`. Its shape is a dictionary from item name (a string) to quantity (an int). Everything the program does is a change to, or a report on, that one dictionary.

**<details><summary>Q: `stock` is a global variable, and `restock` and `sell` change it. Chapter 1.3 told you to avoid that. Is this program wrong?</summary>**

It is a tradeoff the author made, and you can name both sides of it. Keeping `stock` inside `inventory.py` and never importing it into `main.py` means only three functions can ever touch it, which makes it easy to find every place it changes. The cost is that `restock` and `sell` are impure: calling `sell("bread", 2)` twice returns `True` the first time and `False` the second, because the first call used up the bread. The case study in two weeks makes the same choice for the same reason, and you will make it in your project too. Knowing the cost is what matters.

Notice also that nothing here needs the `global` keyword. Mutating a dictionary through a global name is allowed; only _reassigning_ the name would need `global`. That is the distinction between mutability and reassignment from chapter 1.7, showing up in practice.

</details>

### Step 4: Trace One Action

Take "Sell 1 milk." Start in `main()`:

1. The `while True` loop prints the menu and reads `choice`. `.strip()` removes stray spaces. `choice` is `"2"`.
2. `"2"` is not `"4"`, so no `break`. It is not `"3"`. It _is_ in `("1", "2")`, so we go inside.
3. `name` becomes `"milk"`, lowercased and stripped. `quantity` becomes the string `"1"`, which passes `.isdigit()`, so it becomes the int `1`.
4. `choice` is not `"1"`, so we reach `elif sell(name, quantity)`. Now jump to `inventory.py`.
5. In `sell`, `"milk"` is in `stock`, so the first guard is skipped. `stock["milk"]` is `0`, which is less than `1`, so the second guard returns `False`.
6. Back in `main`, `False` means the `elif` fails and the `else` prints `Can't sell 1 milk.`
7. The loop goes around again.

That is one complete path through the program. Every other path is shorter or reuses pieces of this one.

### Step 5: Predict, Then Run

{% hint style="warning" %}
**Predict, then run.** Write down what each of these returns. Then open the REPL in the folder with `python3`, type `from inventory import *`, and check.

```python
sell("eggs", 1)
restock("eggs", 12)
sell("bread", 1)
report()
```

<details><summary>What actually happens</summary>

```
False
12
True
'apples: 5\nbread: 1\neggs: 12\nmilk: 0 (out of stock)'
```

`sell("eggs", 1)` is `False` because of the first guard: no such key. `restock("eggs", 12)` shows why the author wrote `stock.get(name, 0)`. `"eggs"` is not in the dictionary, so `.get` returns the default `0`, and `0 + 12` becomes the new entry. Without the default, `stock.get(name)` would return `None`, and `None + 12` raises a `TypeError`. With bracket notation instead, `stock[name] + 12` raises a `KeyError`, because the key is missing. Either way, restocking any new item would crash.

Two things in `report()` you may not have seen before: `sorted(stock.items())` puts the pairs in alphabetical order by key, and `"\n".join(lines)` glues a list of strings together with a newline between each. In `main.py`, `choice in ("1", "2")` uses a tuple from chapter 1.7 as a small fixed set of options. If you did not know those, the right move was to write "I am guessing `sorted` sorts alphabetically" in your list, run it, and move it to "I know."

</details>
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Run `python3 main.py`. Choose `2`, type `bread`, and when asked how many, type `abc`. Then type `7`. What happens on each of those two lines?

<details><summary>What actually happens</summary>

`abc` fails `.isdigit()`, prints `Please enter a whole number.`, and hits `continue`. `continue` jumps to the top of the `while` loop, which prints the menu again and asks for a _menu choice_. So your `7` is read as a menu choice, and the program says `That isn't an option.`

If you predicted that `7` would be taken as the quantity, you have just found the difference between "ask again for this one value" and "start the whole action over." The code does the second. Whether that is what the author intended is a fair question to write down. Nothing in the code tells you.

</details>
{% endhint %}

### Step 6: Know vs. Guess

Here is what a finished list might look like for this program.

**Know:** it stores counts in one dictionary; new items are created by restocking; you cannot sell what is not there or more than is there; the report is alphabetical.

**Still guessing:** whether the author meant the `continue` to go all the way back to the menu; whether the shop is supposed to remember its stock after you quit (it doesn't).

That second list is worth more than it looks. Those are the questions you would ask the author if you could, and the places you would look first if someone told you there was a bug.

## Reading Code a Model Wrote

An AI model will write code for you that looks like the program above, only faster, with better comments, and with a tone of total confidence. Reading it is the same activity with one adjustment: the confidence tells you nothing. You have to bring the suspicion yourself.

Marcy's [AI policy](../guidelines-and-policies/ai-policy.md) asks what job you gave the model. Code that a model wrote and you read, take apart, and never put in your own file is reading practice, and reading practice is the job you are here for. What the policy forbids is that code ending up in your submission.

The policy's [standing instruction you can paste](../guidelines-and-policies/ai-policy.md#a-standing-instruction-you-can-paste) is the right way to ask a model about code you are reading. It makes the model explain and question rather than rewrite.

Here are two functions a model produced when asked for pieces of a menu program. Read each one with the method. In particular, do Step 5 before you look at the answer.

{% hint style="warning" %}
**Predict, then run.** Copy this into a file and call it. Type `2` when asked.

```python
def get_menu_choice():
    choice = input("Choose an option (1-3): ")
    if choice == 1:
        return "add"
    elif choice == 2:
        return "view"
    elif choice == 3:
        return "quit"
    else:
        return "invalid"

print(get_menu_choice())
```

<details><summary>What actually happens</summary>

It prints `invalid`. It prints `invalid` no matter what you type.

`input()` returns a string, so `choice` is `"2"`, and `"2" == 2` is `False`. Every branch fails and the `else` runs. The function is perfectly readable, perfectly plausible, and useless. Either the comparisons need to be against `"1"`, `"2"`, `"3"`, or `choice` needs `int()` first (and then a guard for non-numbers).

You knew this. You have known it since chapter 1.6. The point is that knowing it did not stop the model, and it will not stop the model next time, so the check has to be yours.

</details>
{% endhint %}

{% hint style="warning" %}
**Predict, then run.**

```python
def total_price(prices):
    total = 0
    for price in prices:
        total = price
    return total

print(total_price([1.50, 4.00, 3.50]))
```

<details><summary>What actually happens</summary>

It prints `3.5`, the last price, not the total.

The name says `total`. The starting value of `0` says the author meant to accumulate. But the line in the loop is `total = price`, which throws away the running total every time and keeps only the current price. One character is missing: it should be `total += price`.

Describe this failure the way a good bug report would: "`total_price([1.50, 4.00, 3.50])` returns `3.5`. Expected `9.0`. The loop assigns instead of adding." Concrete input, actual output, expected output, and where. That sentence is worth more than "it's broken," and it is what you will be asked to produce for the rest of the year.

</details>
{% endhint %}

## Practice: The Bill Splitter

Here is one more program. Work through all six steps on your own, and write your answers down. There are at least two ways to make this program crash with ordinary input. Find them by running it, then find the lines responsible by reading it.

{% code title="tip.py" lineNumbers="true" %}

```python
def split_bill(total, people, tip_percent=18):
    tip = total * tip_percent / 100
    each = (total + tip) / people
    return round(each, 2)


def main():
    total = float(input("Bill total: "))
    people = int(input("How many people? "))
    answer = input("Tip percent (press Enter for 18): ").strip()
    if answer == "":
        print(f"Each person pays ${split_bill(total, people)}")
    else:
        print(f"Each person pays ${split_bill(total, people, int(answer))}")


if __name__ == "__main__":
    main()
```

{% endcode %}

**<details><summary>Check your answers</summary>**

**What it does:** asks for a bill, a group size, and an optional tip percentage, and prints what each person owes.

**The data:** three numbers, none of them remembered between runs. There is no top-level data at all, which is why this program can be pure where the shop could not: `split_bill(100, 4)` returns `29.5` every single time.

**Two crashes:**

1. Enter `0` for the number of people. `(total + tip) / 0` raises `ZeroDivisionError: float division by zero` on line 3.
2. Enter anything that is not a number, like `twenty`, for the bill total. `float("twenty")` raises a `ValueError` on line 8, before `split_bill` is ever called.

There is a third if you look: `int(answer)` on line 14 crashes on a tip like `15.5`.

You will learn how to catch these in the next chapter. For now, the skill was finding them, and being able to say on which line and why.

**Something to notice:** `tip_percent=18` is a default parameter value from chapter 1.3, and the `if answer == ""` branch exists only to leave it out so the default is used. That is the author telling you what the normal case is.

</details>
