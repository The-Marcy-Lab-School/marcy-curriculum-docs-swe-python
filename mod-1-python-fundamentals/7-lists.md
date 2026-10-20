# 1.7 Lists

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/07-lists/)
{% endhint %}

**Table of Contents**

- [Key Terms](#key-terms)
- [Keeping Every Value](#keeping-every-value)
- [List Basics](#list-basics)
  - [Lists Are Mutable](#lists-are-mutable)
  - [Adding and Removing Values](#adding-and-removing-values)
- [References](#references)
  - [A List Is a Row of References](#a-list-is-a-row-of-references)
  - [Two Names, One List](#two-names-one-list)
  - [Adding to the Front vs. the Back](#adding-to-the-front-vs-the-back)
  - [Passing a List to a Function](#passing-a-list-to-a-function)
- [Copying a List Before Changing It](#copying-a-list-before-changing-it)
  - [Copying List Challenge](#copying-list-challenge)
- [Advanced List Syntax](#advanced-list-syntax)
  - [Unpacking](#unpacking)
  - [Looping with `enumerate()`](#looping-with-enumerate)
  - [2D Lists](#2d-lists)
  - [Tuples: Lists That Cannot Change](#tuples-lists-that-cannot-change)
- [Summary](#summary)

## Key Terms

- **Lists** are ordered collections of values, called **elements**. Like strings, they have indexes starting at `0`, support bracket notation and slicing, and work with `len()` and the `in` operator.
- Unlike strings, lists are **mutable** so methods like `append`, `insert`, `pop`, and `remove` change a list in place.
- A variable does not hold a value: it holds a **reference** to the value. Two variables can reference the same list, and a function receiving a list receives a reference to the caller's list.
- Two variables that reference the same list are **aliases**: a change made through one shows up through the other.
- **Copying** a list with `list(items)` or `items[:]` makes a new list with the same elements. A function that copies a list before changing it leaves the caller's list unchanged.

**Advanced Topics:**

- **Unpacking** assigns the elements of a list to several variables in one statement: `item, price = ["coffee", 3.50]`.
- The built-in **`enumerate()`** function produces `(index, item)` pairs that can be iterated over with a `for` loop. Often, the loop unpacks each pair into two variables: `for index, item in enumerate(items):`.
- Lists can contain other lists (**2D lists**).
- A **tuple** is a list that cannot change, written with parentheses.

## Keeping Every Value

Recall the dollar program in chapter 1.6 which added dollar amounts entered by a user to a `total` and printed it out.

```python
total = 0

while True:
    amount = input("Enter an amount in dollars (like 4.50), or done to finish: ").strip()

    # exit on "done"
    if amount.lower() == "done":
        break

    # skip a blank answer
    if amount == "":
        continue

    total += float(amount)

print(f"Your total is ${total:.2f}")
```

Now, we want a full receipt which lists every item the customer bought and what each one cost. A variable holds one value, so a program would need one variable per item, and it cannot know in advance how many items the customer will buy.

A **list** solves this. A list is a single value that holds any number of values in order, and a program can add to it one value at a time. This program keeps two lists, one for the names of the items and one for their prices, and prints a receipt when the user types `done`:

```python
items = []
prices = []

while True:
    # now we also ask for an item (or done)
    item = input("Item (or done to finish): ").strip()
    if item.lower() == "done":
        break

    # then we ask for the price (for now, assume the user enters a valid number)
    price = float(input(f"Price of {item}: "))

    # add the item to the items list and price to the prices list
    items.append(item)
    prices.append(price)

# Once the while loop is done collecting inputs, calculate the total and print out the receipt
total = 0
for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")
    total += prices[i]

print(f"Total: ${total:.2f}")
```

The loop that asks for input works the same way as the dollar program, and three new things make the receipt possible:

- `items = []` and `prices = []` create two **empty lists**, lists with nothing in them yet.
- `items.append(item)` adds `item` to the end of the `items` list, and `prices.append(price)` does the same for the price. Each pass through the loop makes both lists one element longer.
- After the loop, `range(len(items))` produces the index of every item. The item at index `0` and the price at index `0` belong to the same purchase, so `items[i]` and `prices[i]` print side by side.

## List Basics

A list is written with square brackets `[]` around its values, separated by commas.

```py
items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]
```

The values in a list are called the **elements of the list**, and each element stays in its position until the list is changed.

Like strings lists also...

- have indexes starting at `0`
- use bracket notation to access individual elements: `my_list[index]`
- work with `len()` to get the number of elements in the list
- support slicing with `[start:end]` and the `in` operator
- Unlike strings, lists are mutable.

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
print(f"type() on a list returns {type(items)}")

print(f"I bought {len(items)} items")
print(f"My first item was {items[0]}")
print(f"My last item was {items[-1]}")
print(f"My first two items were {items[0:2]}")
print(f"Did I buy a bagel? {'bagel' in items}")
print('Here is everything I bought:')

for item in items:
    # item holds the "current" item that we're looking at in this iteration of the loop
    print(item)
```

That last loop is the most common thing you will ever do with a list. `for item in items` visits each element in order and assigns it to `item`, with no index and no `range()` in sight. The receipt loop needed `range(len(items))` only because it also had to get the matching price from a second list.

**Challenge: This function can verify whether or not a given list `items` contains a given value `value`. For each numbered comment below, add a comment explaining the logic of the function!**

```python
def has_value(items, value):
    for item in items:  # 1.
        if item == value:  # 2.
            return True  # 3.
    return False  # 4.

items = ['coffee', 'bagel', 'juice', 'muffin']
print(has_value(items, 'bagel'))   # Prints True
print(has_value(items, 'cookie'))  # Prints False
```

**<details><summary>Check out this example</summary>**

```python
def has_value(items, value):
    for item in items:  # Look at every element in the list, one at a time
        if item == value:  # Check whether the current element matches the value
            return True  # If it does, we can immediately return True
        # if it doesn't, keep going!
    return False  # The return True above would have ended the function on a match, so reaching this line means no element matched. Return False.

items = ['coffee', 'bagel', 'juice', 'muffin']
print(has_value(items, 'bagel'))   # Prints True
print(has_value(items, 'cookie'))  # Prints False
```

Python has this built in, of course: `value in items` does exactly what `has_value` does. Writing it yourself still matters, because the same loop, check, and return shape answers questions `in` cannot, like "does this list contain any word longer than five letters?"

</details>

### Lists Are Mutable

Strings have methods like `upper()`, and strings support slicing, but both return a new string and leave the original alone. If you do not store the new string in a variable, the new string is gone: after `item.upper()` runs on its own line, `item` is still `'bagel'`. Trying to change a string in place with bracket notation is an error.

```python
item = 'bagel'
item.upper()   # doesn't mutate the string, it makes a copy
item[0] = 'B'  # TypeError: 'str' object does not support item assignment
```

Unlike strings, lists let you **mutate** them directly (change their contents without reassignment). If the bagel on the receipt was on sale, the program can fix its price in place:

```python
prices = [3.50, 2.25, 4.00, 3.00]
prices[1] = 1.75
print(prices)  # [3.5, 1.75, 4.0, 3.0]
```

We can even empty a list in one go:

```python
prices.clear()  # prices now has no values
print(prices)  # []
```

**<details><summary>Q: We changed the list without ever writing `prices = ...`. Strings would not allow that. Why do lists?</summary>**

Strings are **immutable**: once a string is created, its characters cannot change, so the only way to get a different string is to make a new one and assign it to a variable. Lists are **mutable**: Python lets you change the elements inside an existing list, with bracket notation or with methods like `clear()`. Notice that we never reassign `prices`! The variable still points at the same list, and only the contents of that list changed.

Whether a type is mutable decides whether a change made through one variable can show up through another variable, which is what the References section is about. Strings, numbers, booleans, and `None` are immutable. Lists and dictionaries are mutable.

</details>

### Adding and Removing Values

Since lists are mutable, they not only have read-only operations like slicing and `in`, they also have methods for adding to and removing from the list.

These methods let you add values to a list

- `my_list.append(value)` — adds a given value to the end of a list, increasing the length by 1
- `my_list.insert(index, value)` — adds a given value at the given index, pushing everything after it one place to the right

These methods let you remove values from a list

- `my_list.pop()` — removes and returns the last element of a list, reducing the length by 1
- `my_list.pop(index)` — removes and returns the element at the given index
- `my_list.remove(value)` — removes the first element equal to the given value
- `my_list.clear()` — removes every element

```python
items = ['coffee', 'bagel', 'juice', 'muffin']

items.append('cookie')      # adds 'cookie' to the end
items.insert(0, 'tea')      # adds 'tea' to the beginning
print(items)  # Prints ['tea', 'coffee', 'bagel', 'juice', 'muffin', 'cookie']

items.pop()                 # removes the last item ('cookie')
items.pop(0)                # removes the first item ('tea')
print(items)  # Prints ['coffee', 'bagel', 'juice', 'muffin']

items.insert(2, 'scone')    # At index 2, inserts 'scone'
print(items)  # Prints ['coffee', 'bagel', 'scone', 'juice', 'muffin']

items[2] = 'croissant'      # At index 2, replaces 'scone' with 'croissant'
print(items)  # Prints ['coffee', 'bagel', 'croissant', 'juice', 'muffin']

items.remove('croissant')   # Removes the first 'croissant' it finds
print(items)  # Prints ['coffee', 'bagel', 'juice', 'muffin']
```

Each of these methods changes one list. The receipt keeps two lists that have to change together, and nothing in Python keeps them in step.

{% hint style="warning" %}
**Predict, then run.** The customer changes their mind about the bagel. What does the receipt print?

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]

items.remove('bagel')

for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")
```

<details><summary>What actually happens</summary>

```
coffee: $3.50
juice: $2.25
muffin: $4.00
```

- `items.remove('bagel')` removes the bagel from `items`, so `juice` moves to index `1` and `muffin` moves to index `2`.
- `prices` was never changed, so index `1` still holds the bagel's price, `2.25`, and index `2` still holds the juice's price, `4.00`.
- The loop pairs elements by index, so every item after the bagel prints beside the wrong price.

The program does not crash, so nothing tells the store that the receipt is wrong. Removing the element at the same index from both lists, with `items.pop(1)` and `prices.pop(1)`, keeps them in step, but the programmer has to remember to change both lists every time. In chapter 1.8, a list of dictionaries keeps each item's name and price together in one element, so they cannot drift apart.

</details>
{% endhint %}

## References

Lists and dictionaries are considered **mutable types**, and that changes how variables that hold them behave. Let's see why.

### A List Is a Row of References

Python stores every value, whether it is a number, a string, or a list, in an area of memory called the **heap**. A variable does not hold the value itself. It holds a **reference to the value's heap address**: a note saying where in memory the value is stored.

A list works the same way, one level deeper. The list itself is a row of numbered slots, and each slot holds a reference to one element:

```
items ──► [ slot 0 | slot 1 | slot 2 ]
              │        │        │
              ▼        ▼        ▼
          'coffee'  'bagel'  'juice'
```

The variable `items` references the row, and each slot references an element. Bracket notation follows those references: `items[1]` goes to the row that `items` references, then follows slot `1` to `'bagel'`.

You can see a reference for yourself. The `id()` function returns a number that identifies where a value lives:

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
receipt = items

print(id(items))        # some large number, like 4395782592
print(id(receipt))      # the exact same number
print(items is receipt) # True: `is` asks whether two variables reference the same object
```

Because `items` and `receipt` hold the same reference, they are two names for one list, not two separate lists. Two variables that reference the same list are called **aliases**.

{% hint style="info" %}
💡 Outside of a programming context, the word "alias" is used as another name that refers to the same person. For example, "Batman" is the alias of "Bruce Wayne".
{% endhint %}

### Two Names, One List

{% hint style="warning" %}
**Predict, then run.** What will `items` and `receipt` hold after the program runs?

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
receipt = items
receipt[1] = 'scone'

print(items)
print(receipt)
```

<details><summary>What actually happens</summary>

```
['coffee', 'scone', 'juice', 'muffin']
['coffee', 'scone', 'juice', 'muffin']
```

Both `items` and `receipt` hold `['coffee', 'scone', 'juice', 'muffin']`. Why?

- When we assign `receipt = items`, the "value" of `items` is the **reference** to the list, not the list itself. So, `receipt` also holds a reference to the exact same list
- When we mutate `receipt[1]`, we are mutating the list referenced by `receipt` which is the same list referenced by `items`. So, both `items` and `receipt` show the mutated list.

If you expected `items` to still hold `'bagel'`, your mental model was that `receipt = items` copies the list. It copies the _address_.

</details>
{% endhint %}

### Adding to the Front vs. the Back

The row of references also explains why some list operations take longer than others. `append()` writes a reference into the empty slot at the end of the row, and nothing else moves. `insert(0, value)` has to make room at the front, so every reference already in the row shifts one slot to the right first.

{% hint style="warning" %}
**Predict, then run.** This program adds 100000 numbers to the back of one list and to the front of another. `time.perf_counter()` returns the current time in seconds, so subtracting the start time from the end time measures how long each loop took. Which loop is slower, and by roughly how much?

```python
import time

start = time.perf_counter()
back = []
for number in range(100000):
    back.append(number)
print(f"append took {time.perf_counter() - start:.3f} seconds")

start = time.perf_counter()
front = []
for number in range(100000):
    front.insert(0, number)
print(f"insert(0) took {time.perf_counter() - start:.3f} seconds")
```

<details><summary>What actually happens</summary>

The exact numbers depend on your computer. On one laptop, the program printed:

```
append took 0.003 seconds
insert(0) took 1.493 seconds
```

- Each `append()` writes one reference into the next empty slot, so 100000 appends do 100000 small steps.
- Each `insert(0, ...)` first shifts every reference already in the list. The 1000th insert shifts 999 references, and the 100000th shifts 99999, so the work adds up much faster than the number of values.

Change both `range(100000)` calls to `range(10000)` and run it again. Both loops finish so quickly that the difference is hard to notice. With 10 times as many values, `append()` takes about 10 times as long, but `insert(0, ...)` takes about 100 times as long. When a program adds to a list in a loop, add to the back.

</details>
{% endhint %}

### Passing a List to a Function

The same thing happens when we invoke a function and provide a list as an argument:

```python
def clear_receipt(receipt_items):
    # 3. Upon receiving the reference, this function modifies the list
    receipt_items.clear()

# 1. The list below is created in the heap and the "reference" to its location is stored in items
items = ['coffee', 'bagel', 'juice', 'muffin']

# 2. When we invoke clear_receipt, we assign the "reference" to the function parameter "receipt_items"
clear_receipt(items)

# 4. The list referenced by items has been modified by the function!
print(items)  # Prints []
```

Sometimes this is exactly what you want. A function whose _job_ is to change a list can change the caller's list directly. Because the caller and the function share one list, the function does not need to build a new list and return it, and every part of the program that references the list sees the change. But this must be intentional.

{% hint style="info" %}
💡 A function can never change a caller's string, number, or boolean this way. The parameter still receives a reference, but an immutable value has no method or bracket assignment that changes it in place.

You can still _reassign_ a variable to change what value it stores but you cannot _mutate_ the value itself.

```python
def add_one_and_print(x):
    x += 1 # shorthand for x = x + 1
    print(x)

my_num = 10
add_one_and_print(my_num)  # 11
print(my_num) # 10
```

`x += 1` looks like it changes the value in `x`, but the number `10` cannot change. Python computes the new value `11` and reassigns `x` to reference it. `my_num` still references `10`.

{% endhint %}

## Copying a List Before Changing It

Suppose the store runs a sale that takes $1 off every item, and the receipt should show each item's regular price next to its sale price. This function calculates the sale prices:

```python
def apply_discount(prices):
    for i in range(len(prices)):
        prices[i] = prices[i] - 1
    return prices

prices = [3.50, 2.25, 4.00, 3.00]
sale_prices = apply_discount(prices)

print(prices)       # [2.5, 1.25, 3.0, 2.0]
print(sale_prices)  # [2.5, 1.25, 3.0, 2.0]
```

The sale prices are correct, but the regular prices are gone. The parameter `prices` inside the function references the same list as the variable `prices` outside it, so every `prices[i] = ...` overwrote one of the caller's regular prices. Nothing in the line `sale_prices = apply_discount(prices)` suggests that it changes `prices`, so a programmer reading that line has no reason to suspect that the regular prices were lost there.

To leave the caller's list alone, the function can copy the list first and change only the copy. There are two common ways to copy a list, and they do the same thing:

```python
prices = [3.50, 2.25, 4.00, 3.00]

# Two ways to copy:
copy1 = list(prices)   # the list() function builds a new list from any sequence
copy2 = prices[:]      # a slice with no start or end creates a copy of the whole thing
```

With a copy, `apply_discount` changes only its own list and returns it, and the caller keeps the regular prices:

```python
def apply_discount(prices):
    sale_prices = list(prices)
    for i in range(len(sale_prices)):
        sale_prices[i] = sale_prices[i] - 1
    return sale_prices

prices = [3.50, 2.25, 4.00, 3.00]
sale_prices = apply_discount(prices)

print(prices)       # [3.5, 2.25, 4.0, 3.0]
print(sale_prices)  # [2.5, 1.25, 3.0, 2.0]
```

A third way, `[*prices]`, uses unpacking, which is covered in Advanced List Syntax below.

### Copying List Challenge

This function changes the list it is given. Rewrite it so that the caller's list stays the same!

```python
def shorten(items):
    items.pop()
    return items

items = ['coffee', 'bagel', 'juice', 'muffin']
shorter_items = shorten(items)

print(items)          # should print ['coffee', 'bagel', 'juice', 'muffin']
print(shorter_items)  # should print ['coffee', 'bagel', 'juice']
```

**<details><summary>Solution</summary>**

```python
def shorten(items):
    new_items = list(items)
    new_items.pop()
    return new_items
```

Or, with a slice that leaves off the last element in the first place. `items[:-1]` runs from the start of the list up to, but not including, index `-1`, which is the last element. A slice always builds a new list, so `items` is untouched:

```python
def shorten(items):
    return items[:-1]
```

</details>

## Advanced List Syntax

### Unpacking

In chapter 1.5, `split()` broke a string into a list of pieces. Often you want each piece in its own variable. **Unpacking** makes it possible to take the values from a list and assign them to distinct variables in one statement.

The syntax puts several variable names, separated by commas, on the left side of the assignment operator `=` and the list on the right side:

```python
line = "coffee: 3.50"
item, price = line.split(": ")

print(item)   # coffee
print(price)  # 3.50
```

The number of variables has to match the number of elements. If the numbers do not match, Python stops with a `ValueError`: `too many values to unpack` when the list has more elements than variables, and `not enough values to unpack` when it has fewer. The exception is a variable with a `*` in front. That variable collects "the rest" as a list:

```python
items = ['coffee', 'bagel', 'juice', 'muffin']

first_item, *other_items = items

print(first_item)   # coffee
print(other_items)  # ['bagel', 'juice', 'muffin']
```

The `*` also works inside square brackets. There, it unpacks the elements of one list into a new list, which makes a copy of the list. You can even add extra elements while you copy:

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
copy = [*items]

def add_item(items, item):
    new_items = [*items, item]
    return new_items

more_items = add_item(items, 'cookie')

print(items)       # Prints ['coffee', 'bagel', 'juice', 'muffin']
print(more_items)  # Prints ['coffee', 'bagel', 'juice', 'muffin', 'cookie']
```

### Looping with `enumerate()`

When you need the position of each element as well as the element, `enumerate()` hands you both. On each pass, `enumerate()` produces a pair, an index and an element, and unpacking splits the pair into two variables:

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]

for index, item in enumerate(items):
    print(f"{item}: ${prices[index]:.2f}")

# coffee: $3.50
# bagel: $2.25
# ...
```

This is the receipt loop again. `item` holds the name directly, and `index` is still there to find the matching price.

### 2D Lists

A list can contain other lists! When the inner lists contain values, we call this a "2-Dimensional (2D)" list or a **"matrix"**.

The receipt can be stored as one 2D list instead of two parallel lists. Each row is a list holding one item and its price, so the matrix below has 4 rows and 2 columns:

```python
receipt = [
    ['coffee', 3.50],
    ['bagel', 2.25],
    ['juice', 4.00],
    ['muffin', 3.00],
]

print(receipt[1])      # ['bagel', 2.25]
print(receipt[1][0])   # bagel
print(receipt[1][1])   # 2.25

print(len(receipt))     # 4, the number of rows
print(len(receipt[0]))  # 2, the number of columns in the first row
```

When accessing a 2D list, the first index picks the "row" and the second index picks the "column". Python reads `receipt[1][1]` in two steps: `receipt[1]` produces the row `['bagel', 2.25]`, and `[1]` then picks index 1 of that row, which is `2.25`.

Keeping each item and its price in one row means that removing a row removes both, so they cannot fall out of step. But nothing in `receipt[1][1]` says that index `1` holds the price, so a reader has to remember what each position means. In chapter 1.8, a dictionary stores the price under the name `"price"` instead.

### Tuples: Lists That Cannot Change

A **tuple** is a list that cannot be changed after it is created. It is written with parentheses instead of square brackets, and everything that reads a list works on it: indexing, slicing, `len()`, `in`, and `for`.

```python
line = ('coffee', 3.50)

print(line[0])          # coffee
print(len(line))        # 2
print(3.50 in line)     # True

line[1] = 3.00          # TypeError: 'tuple' object does not support item assignment
```

Use a tuple when the values belong together and should never be added to or removed from, like one line of a receipt that has already been printed. Python itself hands you tuples constantly: `enumerate()` produces `(index, value)` pairs, and a dictionary's `.items()` produces `(key, value)` pairs. When you see `choice in ("1", "2")`, that is a tuple being used as a small fixed set of options.

## Summary

A list stores many values in order under one name, so a program can collect values it doesn't know in advance (every amount the user typed, not only their total) and work with them later, using the same indexing, slicing and loops as with strings. Unlike a string, a list can be changed in place, and a variable holds a reference to a list, not a copy of it. So when two variables, or a function and its caller, share a list, a change made through one name shows up through the other. The programmer therefore has to decide whether code should change the list it was given or build a new one.
