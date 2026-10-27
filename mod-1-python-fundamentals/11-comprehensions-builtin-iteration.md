# 1.11 Comprehensions and Common List Operations

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/13-comprehensions-builtin-iteration/)
{% endhint %}

**Table of Contents**

- [Key Terms](#key-terms)
- [Name the Job, Choose the Tool](#name-the-job-choose-the-tool)
- [1. Do something with every value without producing a result](#1-do-something-with-every-value-without-producing-a-result)
  - [Challenge: Café Report, Part 1](#challenge-café-report-part-1)
- [2. Transforming with List Comprehensions](#2-transforming-with-list-comprehensions)
  - [Imperative vs. Declarative Code](#imperative-vs-declarative-code)
  - [Challenge: Refactor with Tests](#challenge-refactor-with-tests)
  - [Challenge: Café Report, Part 2](#challenge-café-report-part-2)
- [3. Filtering with an `if`](#3-filtering-with-an-if)
  - [Challenge: Café Report, Part 3](#challenge-café-report-part-3)
- [4. Reduce a List of Values Into One Value](#4-reduce-a-list-of-values-into-one-value)
  - [`sum()`, `min()`, `max()`, and `len()`](#sum-min-max-and-len)
  - [The Accumulator Pattern](#the-accumulator-pattern)
  - [Generating a Frequency Counter](#generating-a-frequency-counter)
  - [Challenge: Café Report, Part 4](#challenge-café-report-part-4)
- [5. Finding the First Match](#5-finding-the-first-match)
  - [Challenge: Café Report, Part 5](#challenge-café-report-part-5)
- [6. Sorting with `sorted()` and `.sort()`](#6-sorting-with-sorted-and-sort)
  - [Challenge: Café Report, Part 6](#challenge-café-report-part-6)
- [Combining Steps](#combining-steps)
  - [Challenge: Coffee Revenue](#challenge-coffee-revenue)
- [Advanced Topics](#advanced-topics)
  - [Finding the First Match with `next()`](#finding-the-first-match-with-next)
  - [A New List Shares Its Dictionaries](#a-new-list-shares-its-dictionaries)
- [Summary](#summary)

## Key Terms

- **Imperative vs. Declarative**
  - **Imperative Code** provides explicit instructions for every step to complete a task. This gives us a lot of control over every step, but it takes more effort.
  - **Declarative code** describes the desired solution and uses existing tools to handle the steps. We save time and effort by using existing tools but sacrifice the fine-tuned control that we get if we built it ourselves.
- **List comprehensions** provide declarative ways to build new lists from existing ones, making code more readable and reducing the need for explicit loops.
  - `[expression for item in items]` **transforms** each element and returns a new list with the transformed values, useful for converting data formats or applying calculations.
  - `[item for item in items if test]` **filters**, creating a new list containing only elements that pass a test condition.
- Patterns for using lists:
  - **`sum()`**, **`min()`**, and **`max()`** combine a list of numbers into a single value, and **`len()`** counts the elements in any list.
    - To use `sum()`, `min()`, or `max()` on a list of records, first build a list of numbers from the records with a comprehension.
  - The **accumulator pattern** combines a list into one value: create a variable that holds a starting value, update it once per element in a loop, and return it when the loop ends.
  - A **frequency counter** is an accumulator whose starting value is an empty dictionary. It builds a lookup table that maps each value in a list to the number of times that value appears.
  - Finding the **first** element that passes a test is a `for` loop with an early `return`.
  - **`sorted()`** returns a new sorted list and **`.sort()`** sorts a list **in place**, which means it changes the list itself and returns `None`. Both take `reverse=True` for descending order.

## Name the Job, Choose the Tool

The examples in this lesson use a café's list of purchases. Each purchase is a record with the customer's name, an item, a price, and the way the customer paid:

```python
purchases = [
    {"customer": "Ada",     "item": "coffee",   "price": 3.50,  "payment": "card"},
    {"customer": "Zo",      "item": "bagel",    "price": 2.25,  "payment": "cash"},
    {"customer": "Malik",   "item": "coffee",   "price": 3.50,  "payment": "card"},
    {"customer": "Priya",   "item": "juice",    "price": 4.00,  "payment": "cash"},
    {"customer": "Ada",     "item": "muffin",   "price": 3.00,  "payment": "card"},
]
```

When working with lists like this, the possibilities may seem endless with what you can do! And in some ways that is true, but really there are only a few categories of tasks you will do with a list. Below, we've listed 6 and the specific tools that Python provides for each job. Your role as a software engineer is to _identify_ which kind of task you're working on so you can choose the tool that does it.

Here are the most common jobs you will do with a list, and the Python tool for each:

| You want to...                                                    | Example                                         | Use                                                                                 |
| ----------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------- |
| 1. Do something with every value without producing a result       | Print the details of each purchase              | a `for` loop                                                                        |
| 2. Transform every value and collect the results in a new list    | Get a list of customers from the purchases      | a list comprehension                                                                |
| 3. Keep some values, discard the others (filter)                  | Get a list of the cash purchases                | a list comprehension with `if`                                                      |
| 4. Reduce a list down to one value                                | Calculate the total the price of every purchase | builtin functions `sum()`, `min()`, `max()`, and `len()` or the accumulator pattern |
| 5. Find the first value that passes a test (find the first match) | Find the first purchase of juice                | a `for` loop with `return`                                                          |
| 6. Compare values to put them in order                            | Order the prices from most to least expensive   | `sorted()` or `.sort()`                                                             |

Let's look at these jobs one at a time. The examples use each purchase's item and price. At the end of each section, a café report challenge asks you to write one more piece of the café's end-of-day report, and the challenges use each purchase's payment.

## 1. Do something with every value without producing a result

This is the simplest case and one that we've been practicing for the last few lessons. Suppose we wanted to print every purchase as a line of a receipt. A `for` loop already handles this task well.

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

# For every element in the list, do something
for purchase in purchases:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")

# coffee: $3.50
# bagel: $2.25
# coffee: $3.50
# juice: $4.00
# muffin: $3.00
```

### Challenge: Café Report, Part 1

Add to the report with one line per purchase that says the customer's name and how the customer paid. Write a loop that prints these lines:

```
Ada paid by card
Zo paid by cash
Malik paid by card
Priya paid by cash
Ada paid by card
```

**<details><summary>Solution</summary>**

```python
for purchase in purchases:
    print(f"{purchase['customer']} paid by {purchase['payment']}")
```

The loop's job is to print a line for each purchase. It doesn't build anything that the program uses later, so a plain `for` loop is the right tool.

</details>

## 2. Transforming with List Comprehensions

Often, we want to build a new list using data from an existing one. For example, we may want a list of the names of the customers from the `purchases` list.

We can start with an empty list and use a `for` loop through the existing `purchases` list, using `.append()` to fill the new list.

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

# Transform purchases into a list of customer names
customer_names = []
for purchase in purchases:
    customer_names.append(purchase["customer"])

print(customer_names)  # ['Ada', 'Zo', 'Malik', 'Priya', 'Ada']
```

This job, transforming every value and collecting the results in a new list, is so common that Python gives it its own syntax called a **List Comprehension**. It looks like this:

```python
customer_names = [purchase["customer"] for purchase in purchases]

print(customer_names)  # ['Ada', 'Zo', 'Malik', 'Priya', 'Ada']
```

You can read this syntax like this: "for each `purchase` in `purchases`, compute `purchase["customer"]` and collect it in the new list."

The list comprehension syntax can be generalized like this:

```python
[expression for item in source_list]
```

Python reads this and builds a new list by evaluating `expression` once for every element of a source list. The value of the expression is added to the new list. The new list always has exactly as many elements as the source.

The expression can be any expression, including a call to a function you wrote. In this example, `format_line` turns one purchase into a line of a receipt, and the comprehension calls it once for every purchase:

{% code title="transform.py" %}

```python
def format_line(purchase):
    return f"{purchase['item']}: ${purchase['price']:.2f}"

receipt_lines = [format_line(purchase) for purchase in purchases]
print(receipt_lines)
# ['coffee: $3.50', 'bagel: $2.25', 'coffee: $3.50', 'juice: $4.00', 'muffin: $3.00']
```

{% endcode %}

Keeping the work in a small function is what lets the comprehension stay one readable line.

### Imperative vs. Declarative Code

The loop and the comprehension build the same list, so which should you use? The comprehension is certainly faster to write and read if you know what you're doing, but everything in programming is a tradeoff so there _must_ be a reason to use a loop.

The `for` loop is the **Imperative** way to do this task meaning **you define and control every step of the process**. This means that you can insert additional steps to customize the solution but it does require more effort to both read and write this code:

```python
# Imperative: High Control & High Effort:
customer_names = []
for purchase in purchases:
    customer_names.append(purchase["customer"])
    # A custom print statement that is only possible when written imperatively
    print(f"Added {purchase['customer']}")

# Declarative: Low Control & Low Effort:
customer_names = [purchase["customer"] for purchase in purchases]
```

The list comprehension is the **Declarative** approach where we use purpose-built tools that allow us to **describe the outcome we want, not the process**. This means that we lose the ability to adjust the process. However, if adjustments aren't needed, it is easier to both read and write!

Neither approach is strictly "better", they just make different tradeoffs. The declarative approach is typically the right choice until you need to make adjustments to the process and you reach for the imperative tool that gives you more control.

{% hint style="info" %}
**Making a Peanut Butter and Jelly Sandwich:**

If you were to give someone **imperative** instructions you might need to specify where to find the ingredients, the exact peanut-butter-to-jelly ratio, and how to cut the bread.

A **declarative** approach would be to simply ask for a sandwich and let the person decide how to make it. You don't care as much about the details as long as it gets done.
{% endhint %}

### Challenge: Refactor with Tests

Every comprehension in this lesson replaces a loop that already works. How do you know the comprehension does _exactly_ what the loop did? You could run both and compare the output by eye, but tests do this job better: they check the same inputs every time, and they tell you exactly which check failed.

The lecture code for this lesson has a `refactor-with-tests` folder. Its `double_all.py` file holds this function, which returns a new list in which every number is doubled, every string is repeated, and every other value is left alone:

```python
def double_all_purely(items):
    doubled = []
    for value in items:
        doubled.append(double(value))
    return doubled


def double(value):
    if isinstance(value, (int, float, str)):
        return value * 2
    else:
        return value
```

The folder's `test_double_all.py` file has three tests for `double_all_purely`, and all three pass with the loop. Follow the setup steps in the lecture code's README to install pytest, then run `python3 -m pytest` from inside the `refactor-with-tests` folder to see them pass.

Refactor `double_all_purely` to use a list comprehension and run `python3 -m pytest` again. If every test still passes, the comprehension does what the loop did.

**<details><summary>Solution</summary>**

```python
def double_all_purely(items):
    return [double(value) for value in items]
```

The comprehension still calls the `double` helper function, so each value is still doubled, repeated, or left alone. Keeping that branching in its own small function is what lets the comprehension stay one readable line. All three tests still pass, so the refactor changed how `double_all_purely` works without changing what it does.

</details>

### Challenge: Café Report, Part 2

The report needs a list of how each purchase was paid so that we can tell if at least one customer paid in cash. Write a comprehension that builds it:

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

payments = ???

print(payments)
# Output: ['card', 'cash', 'card', 'cash', 'card']

print("At least one customer paid in cash" if "cash" in payments else "No one paid in cash")
# Output: At least one customer paid in cash
```

**<details><summary>Solution</summary>**

```python
payments = [purchase["payment"] for purchase in purchases]
```

Read from the `for` outward: for each `purchase` in `purchases`, compute `purchase["payment"]` and collect it. The source has five purchases, so the new list has five payments.

</details>

## 3. Filtering with an `if`

Filtering occurs whenever we want to keep some values in a list and not others. For example, we may want to look at only the purchases made by the customer named `"Ada"`.

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

adas_purchases = [purchase for purchase in purchases if purchase["customer"] == "Ada"]
print(adas_purchases)
# Output:
# [
#   {'customer': 'Ada', 'item': 'coffee', 'price': 3.5, 'payment': 'card'},
#   {'customer': 'Ada', 'item': 'muffin', 'price': 3.0, 'payment': 'card'}
# ]
```

In this example, `[purchase for purchase in purchases]` would return a new list with every purchase in its entirety. Adding the `if` to the end keeps only the purchases for which the expression `test` expression is true. Here is the general shape:

```python
[expression for item in source_list if test]
```

Use it when you want a copy of the source list with unwanted values removed.

Here is an example where we combine using an `expression` and an `if` to get the names of the items for purchases over $3:

{% code title="filter.py" %}

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

big_items = [purchase["item"] for purchase in purchases if purchase["price"] > 3]
print(big_items)  # ['coffee', 'coffee', 'juice']
```

{% endcode %}

Read it from the `for` outward: "for each `purchase` in `purchases`, keep it if its price is over 3, and collect its item."

### Challenge: Café Report, Part 3

The café counts its cash drawer at the end of the day, so the report lists the items that customers paid for in cash. Write one comprehension that builds the list:

```python
cash_items = ???

print(cash_items)  # ['bagel', 'juice']
```

**<details><summary>Solution</summary>**

```python
cash_items = [purchase["item"] for purchase in purchases if purchase["payment"] == "cash"]
```

The `if` keeps only the purchases paid in cash (filtering), and `purchase["item"]` turns each of those purchases into its item (transforming).

</details>

## 4. Reduce a List of Values Into One Value

When we have a list of values, we often want to reduce that list down to a single value. For example, we may want to get largest or smallest value in the list, or calculate the sum of all values. Let's explore the ways we can do this.

### `sum()`, `min()`, `max()`, and `len()`

Python has built-in functions for the most common ways to boil a list down to a single value:

```python
prices = [3.50, 2.25, 3.50, 4.00, 3.00]

print(sum(prices))   # 16.25
print(min(prices))   # 2.25
print(max(prices))   # 4.0
print(len(prices))   # 5
print(sum(prices) / len(prices))  # 3.25, the average
```

These functions have one limitation: `sum()`, `min()`, and `max()` only work on a list of numbers. Try them on the list of purchases:

```python
print(len(purchases))  # 5
print(sum(purchases))  # TypeError: unsupported operand type(s) for +: 'int' and 'dict'
```

`len()` works because it only counts the elements, and it never needs to look inside them. `sum()` adds the elements together, starting from `0`, and Python has no rule for adding a dictionary to a number, so it raises a `TypeError`. `min()` and `max()` raise a `TypeError` too, because Python has no rule for deciding which of two dictionaries is smaller.

The fix is to transform the purchases into a list of numbers first. A comprehension does that job, and the built-in function then reduces the numbers:

```python
prices = [purchase["price"] for purchase in purchases]
print(prices)       # [3.5, 2.25, 3.5, 4.0, 3.0]
print(sum(prices))  # 16.25
print(max(prices))  # 4.0
```

These are the "declarative" approaches. Let's look at the "imperative" approach which is sometimes needed.

### The Accumulator Pattern

The built-in functions cover the most common reductions. When none of them does the job you need, you write the loop yourself imperatively.

```python
def total(purchases):
    running_total = 0                       # the starting value
    for purchase in purchases:
        running_total += purchase["price"]  # combine the current value into the total so far
    return running_total                    # the final accumulated value

print(total(purchases))  # 16.25
```

This pattern is the **accumulator pattern**:

- create a variable holding a starting value
- update it once per element
- return it when the loop ends.

A loop that builds a list with `.append()` has this shape too: its starting value is an empty list, and its combining step is `.append()`. We saw this as the imperative approach for transforming a list:

```python
def get_customer_names(purchases):
    customer_names = []                             # the starting value
    for purchase in purchases:
        customer_names.append(purchase["customer"]) # combine the current value into the list so far
    return customer_names                           # the final accumulated value

print(get_customer_names(purchases)) # ['Ada', 'Zo', 'Malik', 'Priya', 'Ada']
```

`sum()` is this same loop, with `0` as the starting value and `+` as the combining step.

Change the starting value or the combining step, and the same shape does a different job.

### Generating a Frequency Counter

We've seen the accumulator pattern for building an _integer_ total and a _list_ of names. Now, Let's look at using the accumulator pattern to build a _dictionary_.

Here we have some code that creates a lookup table dictionary mapping each type of item to the number of purchases of that item (e.g. "coffee" is in 2 purchases, "bagel" is in 1 purchase, etc...). This kind of lookup table is called a **frequency counter**.

```python
def get_item_counts(purchases):
    # The starting value here is an empty {}
    counts = {}
    for purchase in purchases:
        item = purchase["item"]
        # if this is the first time we are looking at an item, .get returns 0 and we store it as 1
        # if we've already counted the item before, .get returns its count and we store that count + 1
        counts[item] = counts.get(item, 0) + 1
    return counts

print(get_item_counts(purchases))
# {'coffee': 2, 'bagel': 1, 'juice': 1, 'muffin': 1}
```

The combining step adds one to the count stored under the current item. The first time an item appears it is not a key yet, and `.get(key, 0)` returns `0` for a missing key, so the same line handles both a new item and one that has been seen before.

{% hint style="info" %}
This is so common that the standard library has it built in: `from collections import Counter` and then `Counter([purchase["item"] for purchase in purchases])` gives you a dictionary-like object with the same counts. Knowing the loop is what lets you recognize what `Counter` is doing.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** What does this program print?

```python
sizes = ["small", "large", "small", "small"]

counts = {}
for size in sizes:
    counts[size] = counts.get(size, 0) + 1

print(counts)
```

<details><summary>What actually happens</summary>

It prints `{'small': 3, 'large': 1}`.

- The first time `"small"` appears, it is not a key yet, so `counts.get("small", 0)` returns `0` and the count becomes `1`.
- `"large"` is new too, so its count also starts at `1`.
- Each later `"small"` is already a key, so `.get()` returns its current count and the loop adds one to it.

</details>
{% endhint %}

### Challenge: Café Report, Part 4

The report shows how many purchases were paid each way. Build a lookup table named `payment_counts` that maps each payment method to the number of purchases paid that way:

```python
payment_counts = {}
# your loop here

print(payment_counts)  # {'card': 3, 'cash': 2}
```

**<details><summary>Solution</summary>**

```python
payment_counts = {}
for purchase in purchases:
    payment = purchase["payment"]
    payment_counts[payment] = payment_counts.get(payment, 0) + 1
```

- The starting value is an empty dictionary.
- The combining step adds one to the count stored under the current purchase's payment method. `.get(payment, 0)` returns `0` the first time a payment method appears.
- When the loop ends, `payment_counts` holds one key for every payment method that appears in the purchases.

</details>

## 5. Finding the First Match

While a filtering comprehension is used to get ALL values that pass a test, sometimes you only want the first one. A comprehension cannot stop early: it checks every element and builds a whole list, even when the first element already passed. The plain way is a `for` loop that leaves as soon as it finds it:

```python
def find_purchase(purchases, item):
    for purchase in purchases:
        if purchase["item"] == item:
            return purchase
    return None  # nothing passed the test

def find_purchase_index(purchases, item):
    for index, purchase in enumerate(purchases):
        if purchase["item"] == item:
            return index
    return -1

print(find_purchase(purchases, "juice"))        # {'customer': 'Priya', 'item': 'juice', 'price': 4.0, 'payment': 'cash'}
print(find_purchase_index(purchases, "juice"))  # 3
print(find_purchase(purchases, "tea"))          # None
```

`return` inside the loop is what makes this "first": the loop stops at the first success and never looks at the rest. The line after the loop handles the case where nothing matched. Decide what that case should return before you write the function, because callers will need to check for it.

{% hint style="warning" %}
**Predict, then run.** `"coffee"` appears in `purchases` twice, at index `0` and at index `2`. What does this print?

```python
print(find_purchase_index(purchases, "coffee"))
```

<details><summary>What actually happens</summary>

It prints `0`. The first purchase is a coffee, so the `return` inside the loop runs on the first pass, and the function ends before the loop ever reaches index `2`.

</details>
{% endhint %}

### Challenge: Café Report, Part 5

The report names the first item paid for with each payment method. Complete `first_item_paid_by` so that it returns the item of the first purchase paid with `payment`, or `None` when no purchase was paid that way:

```python
def first_item_paid_by(purchases, payment):
    # return the item of the first purchase paid with payment, or None
    return None

print(first_item_paid_by(purchases, "cash"))   # should print bagel
print(first_item_paid_by(purchases, "card"))   # should print coffee
print(first_item_paid_by(purchases, "check"))  # should print None
```

**<details><summary>Solution</summary>**

```python
def first_item_paid_by(purchases, payment):
    for purchase in purchases:
        if purchase["payment"] == payment:
            return purchase["item"]
    return None
```

The loop returns `'bagel'` for `"cash"` as soon as it reaches the bagel, so it never checks the juice. No purchase was paid by `"check"`, so the loop finishes without returning and the function reaches `return None`.

</details>

## 6. Sorting with `sorted()` and `.sort()`

Given a list of numbers, `sorted()` returns a new list with them in ascending order, from smallest to largest. The source list is untouched:

```python
prices = [3.50, 2.25, 3.50, 4.00, 3.00]
ordered = sorted(prices)
print(ordered)  # [2.25, 3.0, 3.5, 3.5, 4.0]
print(prices)   # [3.5, 2.25, 3.5, 4.0, 3.0]
```

The list method `.sort()` does the same thing **in place** which means that the source list is modified and nothing is returned:

```python
prices = [3.50, 2.25, 3.50, 4.00, 3.00]
prices.sort()   # sorts prices "in place"
print(prices)   # [2.25, 3.0, 3.5, 3.5, 4.0]
```

`.sort()` is the only tool in this lesson that changes the list it is given. Every other tool leaves the source list unchanged: a comprehension produces a new list, the built-in functions and the accumulator produce a single new value, and `sorted()` produces a new sorted list. Choose `sorted()` when other code still needs the list in its original order, and `.sort()` when nothing does.

{% hint style="warning" %}
**Predict, then run.**

```python
prices = [3.50, 2.25, 3.50, 4.00, 3.00]
result = prices.sort()
print(result)
```

<details><summary>What actually happens</summary>

It prints `None`.

`.sort()` changes `prices` and returns nothing, so `result` gets `None`. This is one of the most common mistakes in Python: writing `x = my_list.sort()` and then wondering where the list went. If you want the sorted list as a value, use `sorted(prices)`. If you want to reorder `prices` itself, call `prices.sort()` on its own line and don't assign it to anything.

`.append()` and `.reverse()` work the same way: they change the list in place and return `None`. `.pop()` is different: it changes the list and also returns the element it removed.

</details>
{% endhint %}

Both take an optional keyword argument, `reverse=True`, that gives descending order:

```python
prices = [3.50, 2.25, 3.50, 4.00, 3.00]
print(sorted(prices, reverse=True))   # [4.0, 3.5, 3.5, 3.0, 2.25]
```

### Challenge: Café Report, Part 6

The report lists every price paid in cash, from highest to lowest. Build the list without changing `purchases`:

```python
cash_prices = ???

print(cash_prices)  # [4.0, 2.25]
```

**<details><summary>Solution</summary>**

```python
cash_prices = sorted([purchase["price"] for purchase in purchases if purchase["payment"] == "cash"], reverse=True)
```

The comprehension keeps the cash purchases and turns each one into its price, which gives `[2.25, 4.0]`. `sorted()` with `reverse=True` then returns a new list from highest to lowest. `purchases` itself is a list of dictionaries, which `sorted()` cannot compare, so the comprehension has to build the list of numbers first.

</details>

## Combining Steps

Because each of these tools takes a list and gives back a list (or a value), the output of one can feed straight into the next. Name the intermediate steps when it helps the reader. This example finds the two highest prices:

```python
prices = [purchase["price"] for purchase in purchases]  # transform each purchase into its price
ordered = sorted(prices, reverse=True)                  # put the prices in order, highest first
top_two = ordered[:2]                                   # keep the first two

print(top_two)
# [4.0, 3.5]
```

Or fold the steps into one line, which is fine while it stays readable:

```python
print(sorted([purchase["price"] for purchase in purchases], reverse=True)[:2])
# [4.0, 3.5]
```

### Challenge: Coffee Revenue

Write the code that calculates how much the café made from coffee. Name each job your code does before you write it.

```python
coffee_total = ???

print(coffee_total)  # should print 7.0
```

**<details><summary>Solution</summary>**

```python
coffee_prices = [purchase["price"] for purchase in purchases if purchase["item"] == "coffee"]
coffee_total = sum(coffee_prices)
```

The comprehension does two jobs: the `if` keeps only the coffee purchases (filtering), and `purchase["price"]` turns each one into its price (transforming). `sum()` then combines those prices into one value. The same thing fits on one line as `sum([purchase["price"] for purchase in purchases if purchase["item"] == "coffee"])`.

</details>

## Advanced Topics

### Finding the First Match with `next()`

A comprehension cannot stop early, but a **generator expression** can. A generator expression looks like a comprehension written with parentheses instead of square brackets. Instead of building a whole list at once, it produces one value at a time, and only when something asks it for the next value. The built-in function `next()` is what asks.

Together, they find the first match in one line:

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

first_juice = next((purchase for purchase in purchases if purchase["item"] == "juice"), None)
print(first_juice)  # {'customer': 'Priya', 'item': 'juice', 'price': 4.0, 'payment': 'cash'}

first_tea = next((purchase for purchase in purchases if purchase["item"] == "tea"), None)
print(first_tea)  # None
```

The line has three parts:

- `(purchase for purchase in purchases if purchase["item"] == "juice")` is the generator expression. It describes the purchases that pass the test, but it has not checked any of them yet.
- `next(...)` asks the generator for its first value. The generator checks the purchases one at a time and stops at the first one that passes, so it never looks at the muffin after the juice.
- `None` is the value `next()` returns when the generator runs out of purchases without finding one that passes. Without it, `next()` raises a `StopIteration` error when nothing matches.

This one line does the same job as a `for` loop that returns the first matching purchase and returns `None` after the loop ends. It is the declarative version of that loop, and the same tradeoff applies. The one-line version is shorter when the test is simple. The loop gives you control over each step, so it is easier to read when the search needs to do more, such as return the index of the match or print each purchase it checks.

### A New List Shares Its Dictionaries

A comprehension builds a new list, but when the source list holds dictionaries, the new list holds the same dictionaries, not copies of them. Changing a dictionary through the new list changes it in the source list too:

```python
purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50},
    {"customer": "Zo", "item": "bagel", "price": 2.25},
]

big_purchases = [purchase for purchase in purchases if purchase["price"] > 3]
big_purchases[0]["price"] = 0

print(purchases[0])                      # {'customer': 'Ada', 'item': 'coffee', 'price': 0}
print(big_purchases[0] is purchases[0])  # True
```

The list itself is new, so adding an element to `big_purchases` or removing one leaves `purchases` alone. Each dictionary inside it is shared, so changing a dictionary's values changes the one dictionary that both lists hold. To change the records without touching the originals, copy each one inside the comprehension: `[dict(purchase) for purchase in purchases if purchase["price"] > 3]`.

## Summary

Most loops over a list do one of six jobs: do something with every value, transform every value, keep the values that pass a test, combine every value into one, find the first value that passes a test, or put the values in order. Once you can name the job, you can choose the tool Python provides for it: a plain `for` loop to do something with every value; a comprehension to transform or filter; `sum()`, `min()`, `max()` and `len()`, or the accumulator pattern, to combine; a loop with an early `return` to find; and `sorted()` or `.sort()` to put values in order. A comprehension also connects the other tools to a list of records, because it builds the list of numbers that `sum()`, `min()`, `max()` and `sorted()` need. The declarative tools describe the result instead of the steps, so a reader can tell what a line produces without tracing it.
