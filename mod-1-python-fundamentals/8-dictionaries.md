# 1.8 Dictionaries

{% hint style="info" %}
💡 Looking for another way to learn? Check out the [interactive reading for this lesson](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/08-dictionaries/)
{% endhint %}

**Table of Contents**:

- [Key Terms](#key-terms)
- [Dictionaries: From Rows to Records](#dictionaries-from-rows-to-records)
  - [What is a Dictionary?](#what-is-a-dictionary)
- [Records: One Thing's Information Together](#records-one-things-information-together)
  - [Reading Values with Bracket Notation and `.get()`](#reading-values-with-bracket-notation-and-get)
  - [Challenge: Phone Records](#challenge-phone-records)
  - [Changing a Record](#changing-a-record)
  - [Lists of Dictionaries](#lists-of-dictionaries)
  - [A Dictionary with a List](#a-dictionary-with-a-list)
  - [Challenge: Updating a Receipt](#challenge-updating-a-receipt)
- [Lookup Tables: Finding a Value from a Key](#lookup-tables-finding-a-value-from-a-key)
  - [Looking Up a Key Held in a Variable](#looking-up-a-key-held-in-a-variable)
  - [Challenge: Dynamic Keys](#challenge-dynamic-keys)
  - [Iterating Over Keys and Values of a Dictionary](#iterating-over-keys-and-values-of-a-dictionary)
  - [Challenge: Counting Items](#challenge-counting-items)
- [Dictionaries are Mutable and Held by Reference](#dictionaries-are-mutable-and-held-by-reference)
  - [Changing a Dictionary Inside a Function](#changing-a-dictionary-inside-a-function)
  - [Copying a Dictionary Before Changing It](#copying-a-dictionary-before-changing-it)
- [Advanced Topics](#advanced-topics)
  - [Which Values Can Be Keys](#which-values-can-be-keys)
  - [A Copy Shares Its Nested Values](#a-copy-shares-its-nested-values)
- [Summary](#summary)

## Key Terms

- A **dictionary** is a data structure that stores values under keys instead of positions, so a program looks each value up by name.
  - A **key** is the name a value is stored under and looked up by. Each key appears only once in a dictionary.
  - A **value** is the data stored under a key. It can be any type, including a list or another dictionary.
- Dictionaries are often used in two ways:
  - A **record** is a dictionary that keeps the pieces of information about one thing together, such as `{"item": "coffee", "price": 3.50}`. The programmer decides a record's keys in advance so that every purchase record has the same "shape".
  - A **lookup table** is a dictionary that finds a value from a key, such as a menu that maps each item to its price. Its keys are part of the data, so the program adds new keys as it runs.
- A **list of dictionaries** holds many records of the same kind, one dictionary for each thing, all with the same keys.
- Dictionary values are accessed using **bracket notation** (`my_dict["key"]`), which raises a `KeyError` for a missing key, or with the **`.get()`** method, which returns `None` (or a default you choose) instead. The `in` operator checks whether a key exists.
- Dictionaries are **mutable**, meaning you can add, modify, or delete key-value pairs after creation using assignment, `del`, or `.pop()`.
- Dictionaries can contain **nested data**, such as a receipt dictionary whose `"purchases"` key holds a list of records.
- A dictionary is considered an "iterable", meaning you can loop over its _keys_ with `for key in my_dict`. Dictionaries also have three methods that each return an iterable:
  - **`.keys()`** — all of the keys
  - **`.values()`** — all of the values
  - **`.items()`** — every key and its value as pairs
- Like lists, dictionaries are held by **reference**. Copy one with `dict(my_dict)` before changing it inside a function, so the caller's dictionary stays the same.

**Advanced Topics:**

- `dict()` makes a **shallow copy**: the outer dictionary is new, but any list or dictionary nested inside it is shared with the original.
- A key must be **hashable**, meaning its value can never change. Strings, numbers, and tuples are hashable. A list is not, so using one as a key raises `TypeError: unhashable type: 'list'`.

## Dictionaries: From Rows to Records

Chapter 1.7 started by introducing lists as a way to track items and their prices as parallel lists:

```python
items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]
print(f"{items[0]} costs {prices[0]}")
```

But this introduced the possibility of "drift" where you delete a value from one list (e.g. `items.remove('bagel')`) but forget to remove the same value from the other list. As a result, the prices no longer align with the items.

The chapter then ended with a receipt stored as a 2D list, one row for each purchase:

```python
receipt = [['coffee', 3.50], ['bagel', 2.25], ['juice', 4.00], ['muffin', 3.00]]

print(receipt[1][1])  # 2.25
```

Keeping each item and its price in one row means they cannot fall out of step. But a programmer who reads `receipt[1][1]` has to remember that for any row, index `0` holds the item and index `1` holds the price.

### What is a Dictionary?

A **dictionary** stores each value under a name, called a **key**, instead of at a position. Here is the first purchase as a dictionary:

```python
purchase_1 = {"item": "coffee", "price": 3.50}

print(purchase_1["price"])  # 3.5

# Dictionaries can be written in one line or across multiple
purchase_2 = {
    "item": "bagel",
    "price": 2.25
}
print(purchase_2["price"])  # 2.25
```

The code now says which piece of information it wants, so a reader no longer has to remember what each position means. Here's how it works:

- Curly braces `{}` surround the dictionary, and each entry is a **key: value** pair.
  - `"item"` and `"price"` are the keys, written as strings.
  - `"coffee"` and `3.50` are their values, which can be of any type.
- Keys are usually strings, and the quotes around them are required. Without quotes, Python reads `price` as a variable, and if no variable called `price` exists you get `NameError: name 'price' is not defined`.
- `purchase_1["price"]` reads the value stored under the key `"price"`.

{% hint style="info" %}
💡 You will also hear dictionaries called **maps** or **hashmaps**.
{% endhint %}

Dictionaries do two jobs.

1. A dictionary like `purchase_1` is a **record**: it keeps the pieces of information about one thing together.
2. A dictionary that acts like a menu is a **lookup table**: it finds the price of any item from the item's name. You will use one later in this lesson.

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00
}
```

## Records: One Thing's Information Together

The programmer decides a record's keys in advance so that every purchase record has the same "shape". For example, every purchase has an `"item"` and a `"price"`.

```python
purchase_1 = {"item": "coffee", "price": 3.50}
purchase_2 = {"item": "bagel", "price": 2.25}
purchase_3 = {"item": "juice", "price": 4.00}
purchase_4 = {"item": "muffin", "price": 3.00}
```

### Reading Values with Bracket Notation and `.get()`

Bracket notation reads a value by its key.

```python
purchase_1 = {"item": "coffee", "price": 3.50}

print(f"One {purchase_1['item']}, please")  # One coffee, please
```

{% hint style="warning" %}
**Predict, then run.** There is no `"discount"` in `purchase_1`.

```python
print(purchase_1["discount"])
```

<details><summary>What actually happens</summary>

```
KeyError: 'discount'
```

Asking a dictionary for a key it does not have is an error, just like asking a list for an index it does not have.

</details>
{% endhint %}

When you are not sure a key exists, use the `.get()` method instead. It returns `None` for a missing key, or a default value of your choosing:

```python
print(purchase_1.get("discount"))     # None
print(purchase_1.get("discount", 0))  # 0
print(purchase_1.get("item"))         # coffee
```

A default of `0` is the right answer here, because a purchase with no discount has a discount of zero.

You can also ask first using the `in` operator to avoid the error.

```python
if "discount" in purchase_1:
    print(purchase_1["discount"])
```

{% hint style="warning" %}
**Predict, then run.** `purchase_1` has a _value_ `"coffee"`. Does the `in` operator tell us if a value is in a dictionary?

```python
if "coffee" in purchase_1:
    print(purchase_1["item"])
```

<details><summary>What actually happens</summary>

The `in` operator on a dictionary checks the _keys_ only, so `"item" in purchase_1` is `True` but `"coffee" in purchase_1` is `False`, even though `"coffee"` is one of the values. So this doesn't print anything!

</details>
{% endhint %}

### Challenge: Phone Records

Create a dictionary "record" for a phone. It should have at least 3 keys with at least one string, boolean, and numeric value. Then, make a second phone record with the exact same shape but with different values. Store them in separate variables and then use bracket notation or `get` to print out one of their values.

**<details><summary>Solution</summary>**

```python
phone_1 = {"model": "Pixel 9", "storage_gb": 128, "is_unlocked": True}
phone_2 = {"model": "iPhone 16", "storage_gb": 256, "is_unlocked": False}

print(phone_1["model"])          # Pixel 9
print(phone_2["model"])          # iPhone 16
print(phone_1.get("storage_gb"))  # 128
print(phone_2.get("storage_gb"))  # 256
```

- `"model"` holds a string, `"storage_gb"` holds a number, and `"is_unlocked"` holds a boolean.
- Both records use the same three keys, so they have the same shape. Only the values differ.

Because the shapes match, any line written for one phone works on the other. `phone_1["model"]` and `phone_2["model"]` both find a model. If `phone_2` had named its key `"name"` instead, `phone_2["model"]` would raise a `KeyError`.

</details>

### Changing a Record

Dictionaries are mutable, like lists. This means that we can perform all four CRUD operations (Create, Read, Update, and Delete), the four things a program does with stored data:

- _Create_: `my_dict["key"] = value` (bracket notation)
- _Read_: `my_dict["key"]` (bracket notation)
- _Update_: `my_dict["key"] = value` (bracket notation)
- _Delete_: `del my_dict["key"]` or `my_dict.pop("key")`

Create and Update use the same line. Assigning to a key adds a new key-value pair if the key is not in the dictionary yet, and replaces the old value if it is.

```python
purchase_1 = {"item": "coffee", "price": 3.50}

# Bracket notation can be used to modify existing values, or create new ones!
purchase_1["price"] = 3.00
purchase_1["discount"] = 0.50
print(purchase_1)  # {'item': 'coffee', 'price': 3.0, 'discount': 0.5}

# Delete key-value pairs with the `del` keyword followed by bracket notation
del purchase_1["discount"]
print(purchase_1)  # {'item': 'coffee', 'price': 3.0}

# .pop() removes a key-value pair and returns its value
price = purchase_1.pop("price")
print(price)     # 3.0
print(purchase_1)  # {'item': 'coffee'}
```

### Lists of Dictionaries

The shape you will use more than any other is a list where every element is a dictionary with the same keys. It is how a program holds "many of the same kind of thing".

For example, a purchase record holds all data about one purchase, and a receipt is a list of many purchase records.

Here is the receipt program from chapter 1.7, rewritten to keep one list of purchase records instead of two parallel lists:

```python
purchases = []

while True:
    item = input("Item (or done to finish): ").strip()
    if item.lower() == "done":
        break

    # for now, assume the user enters a valid number
    price = float(input(f"Price of {item}: "))

    # one record holds both pieces of information about the purchase
    purchases.append({"item": item, "price": price})

total = 0
for purchase in purchases:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")
    total += purchase["price"]

print(f"Total: ${total:.2f}")
```

Two things changed from chapter 1.7:

- `purchases.append({"item": item, "price": price})` adds one record per purchase.
  - In chapter 1.7 we had two separate lists. Each pass through the loop had to append to `items` and to `prices` separately.
- The `for` loop hands you one record at a time. `purchase['item']` and `purchase['price']` come from the same record, so they always belong to the same purchase.
  - In chapter 1.7 we had to line up the two lists by index when printing so we looped with `for i in range(len(items))`.

Notice that in `{"item": item, "price": price}`, the key `"item"` and the variable `item` are spelled the same but are two different things. The key is a string inside the dictionary. The variable holds the value that gets stored under that key.

The same list, written out by hand:

```python
purchases = [
    {"item": "coffee", "price": 3.50},
    {"item": "bagel", "price": 2.25},
    {"item": "juice", "price": 4.00},
    {"item": "muffin", "price": 3.00},
]

# Reach one by position, then by key
print(purchases[1]["price"])  # 2.25

# Remove one the same way you remove from any list
purchases.pop(1)  # the bagel and its price leave together
print(len(purchases))  # 3
```

Compare `purchases[1]["price"]` with `receipt[1][1]` from the start of the lesson. Both read the second purchase's price, but only `purchases[1]["price"]` says that it is the price.

Giving every dictionary the same keys is what makes the loop work. `purchase['item']` runs once for every dictionary in the list, so a single dictionary without an `"item"` key would stop the loop with a `KeyError`.

### A Dictionary with a List

A dictionary can hold a list of records too. A receipt that also records who made the purchases "nests" the list inside a dictionary:

```python
receipt = {
    "customer": "Ada",
    "purchases": [
        {"item": "coffee", "price": 3.50},
        {"item": "bagel", "price": 2.25},
    ],
}

print(receipt["purchases"][0]["item"])  # coffee
```

Read `receipt["purchases"][0]["item"]` from left to right, one step at a time:

- `receipt["purchases"]` is the list of purchase records.
- `[0]` takes the first record in that list, `{"item": "coffee", "price": 3.50}`.
- `["item"]` reads that record's item, `"coffee"`.

The task manager case study stores its tasks as a list of dictionaries, and every project option in this module does too.

{% hint style="warning" %}
**Predict, then run.** The cashier makes Ada's coffee free by deleting its price. What does the program print?

```python
receipt = {
    "customer": "Ada",
    "purchases": [
        {"item": "coffee", "price": 3.50},
        {"item": "bagel", "price": 2.25},
    ],
}

del receipt["purchases"][0]["price"]

total = 0
for purchase in receipt["purchases"]:
    total += purchase["price"]
print(total)
```

<details><summary>What actually happens</summary>

```
KeyError: 'price'
```

- `del receipt["purchases"][0]["price"]` removes the `"price"` key from the coffee's record, so the coffee record is now `{'item': 'coffee'}`.
- The loop's first pass reaches the coffee record, and `purchase["price"]` asks it for a key it no longer has. The loop stops with a `KeyError` before `total` is ever printed.

Deleting a key changes the record's shape, and a loop that expects every record to have that key will crash on the record that lacks it. To make the coffee free while keeping its shape, set its price to `0` with `receipt["purchases"][0]["price"] = 0`.

</details>
{% endhint %}

### Challenge: Updating a Receipt

Start with Ada's receipt below. Without retyping any existing record, write code that:

1. Adds a muffin that costs `3.00` to Ada's purchases.
2. Changes the bagel's price to `2.00`, because it is on sale.
3. Adds a `"paid"` key to the receipt, set to `False`.
4. Prints each purchase as `item: $price`, followed by the total.

```python
receipt = {
    "customer": "Ada",
    "purchases": [
        {"item": "coffee", "price": 3.50},
        {"item": "bagel", "price": 2.25},
    ],
}
```

Your program should print:

```
coffee: $3.50
bagel: $2.00
muffin: $3.00
Total: $8.50
```

**<details><summary>Solution</summary>**

```python
receipt["purchases"].append({"item": "muffin", "price": 3.00})
receipt["purchases"][1]["price"] = 2.00
receipt["paid"] = False

total = 0
for purchase in receipt["purchases"]:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")
    total += purchase["price"]

print(f"Total: ${total:.2f}")
```

- The muffin is a new record, so it goes into the list with `.append()`, the same way any value is added to a list.
- The bagel already has a record. `receipt["purchases"][1]` reaches that record, and `["price"] = 2.00` updates one key inside it, leaving its `"item"` alone.
- `"paid"` describes the whole receipt rather than one purchase, so it goes on `receipt` itself.

</details>

## Lookup Tables: Finding a Value from a Key

A record's keys are chosen by the programmer in advance. A lookup table's keys are part of the data. Here is the café's menu from the start of the lesson, which maps each item to its price:

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

print(menu["bagel"])  # 2.25
```

The keys `"coffee"`, `"bagel"`, `"juice"`, and `"muffin"` are not names the programmer picked to describe a purchase. They are the items the café sells, and when the café adds a new item, the menu gains a new key.

{% hint style="warning" %}
**Check for understanding: record or lookup table?** For each scenario below, decide whether it is a record or a lookup table:

1. The number of `loyalty_points` each customer has (e.g. Ada has 50 while Zo has 25)
2. One customer's `account` data such as their name, email, and membership status
3. The remaining `inventory` for each item on the menu (e.g. 41 bagels left over, 20 muffins, etc...)
4. The café's `details`, such as its address, its phone number, and whether it has Wi-Fi

<details><summary>Answers</summary>

1. **Lookup table.** `loyalty_points = {"Ada": 50, "Zo": 25}`. Every key is a customer, and every value is the same kind of information about that customer: their points. The program finds any customer's points by looking up their name: `loyalty_points["Zo"]`.
2. **Record.** This represents information about a single customer: `account = {"name": "Ada", "email": "ada@marcy.org", "is_member": True}`. Each key names a different piece of information about Ada, so the values are different types: two strings and a boolean.
3. **Lookup table.** `inventory = {"bagel": 41, "muffin": 20}`. Every key is a menu item, and every value is how many of that item are left. The program finds any item's count by looking up its name: `inventory["bagel"]`.
4. **Record.** `details = {"address": "123 Main St", "phone": "555-0100", "has_wifi": True}`. This represents information about a single café. Each key names a different piece of information about it, just like the keys of `account`.

</details>
{% endhint %}

### Looking Up a Key Held in a Variable

The brackets can hold any expression, and Python works out its value before using it as the key. So the key can be a variable, and Python uses whatever value the variable holds:

```python
item = "bagel"
print(menu[item])  # 2.25, the value stored under the key 'bagel'
```

Watch the quotes. `menu[item]` uses the value of the variable `item`, which is `"bagel"`. `menu["item"]` uses the four-letter string `"item"` itself, and since nothing on the menu is called `"item"`, it raises `KeyError: 'item'`.

A key held in a variable is what makes a lookup table useful. The program below asks for each item by name and finds its price on the menu, so the user no longer types prices at all:

```python
purchases = []

while True:
    item = input("Item (or done to finish): ").strip().lower()
    if item == "done":
        break

    # Instead of asking for the price, we first check that the item is on the menu...
    if item not in menu:
        # ...print a message if it isn't there...
        print(f"Sorry, {item} is not on the menu")
        continue

    # ...and then use the price from the menu
    purchases.append({"item": item, "price": menu[item]})

total = 0
for purchase in purchases:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")
    total += purchase["price"]

print(f"Total: ${total:.2f}")
```

The program uses both jobs at once. `menu` is a lookup table that turns an item's name into its price, and each `{"item": item, "price": menu[item]}` is a record of one purchase.

`menu[item]` would raise a `KeyError` for an item the café does not sell, such as `"pizza"`, so the `if item not in menu:` check runs first. The check prints a message that tells the user what went wrong, and `continue` sends the loop back to ask for the next item before `menu[item]` ever runs.

### Challenge: Dynamic Keys

Complete the program below so that it lets the café owner add items to the menu!

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

while True:
    print("Here is your menu: ", menu)
    new_item = input("Add an item to your menu, or press q to exit. ")

    if new_item == 'q':  # a guard clause
        break

    # for now, assume the owner enters a valid number
    price = float(input(f"Okay, what is the price of {new_item}? "))

    # add the new item and its price to the menu!
```

**<details><summary>Solution</summary>**

To complete this program, add the line `menu[new_item] = price` to the end of the loop.

The menu started with four keys, and the program cannot know which items the owner will add. Each new key comes from what the owner types, which is what makes `menu` a lookup table rather than a record.

</details>

### Iterating Over Keys and Values of a Dictionary

In the previous examples, we iterated over a list of records, accessing each record one at a time.

```python
for purchase in purchases:
    print(purchase["item"])  # do something with each purchase record
```

A dictionary can be iterated over too, which is particularly useful when using a dictionary as a lookup table. A `for` loop over a dictionary visits its **keys**:

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

for item in menu:
    price = menu[item]
    print(f"{item} costs ${price:.2f}")
```

Dictionaries also have three methods that give you exactly the part you want to loop over:

- `menu.keys()` — all of the keys
- `menu.values()` — all of the values
- `menu.items()` — every key and its value, paired up

For example, `.values()` would help us calculate the total without needing to know the item names:

```python
total = 0
for price in menu.values():
    total += price

print(f"One of everything costs ${total:.2f}")  # One of everything costs $12.75
```

`.items()` is the one you will reach for most, because it hands you both halves of each pair and you unpack them right in the `for` line:

```python
for item, price in menu.items():
    print(f"{item} costs ${price:.2f}")
```

{% hint style="warning" %}
**Predict, then run.** The café wants a list of everything on the menu that costs less than $3.50. What does this program print?

```python
menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

cheap_items = []
for item, price in menu.items():
    if price < 3.50:
        cheap_items.append(item)

print(cheap_items)
```

<details><summary>What actually happens</summary>

```
['bagel', 'muffin']
```

- `.items()` hands the loop one key-value pair at a time, and the `for` line unpacks each pair into `item` and `price`.
- The `if` statement compares each `price` with `3.50`. Coffee costs exactly `3.50`, and `3.50 < 3.50` is `False`, so coffee is left out. Juice costs `4.00`, so it is left out too.
- Only the key, `item`, is appended, so `cheap_items` holds item names rather than prices.
- The names appear in the order they were added to the menu, because a dictionary remembers the order its keys were added in.

Use `.items()` whenever the loop needs both halves of each pair: here the price decides whether an item counts, and the item's name is what gets saved.

</details>
{% endhint %}

### Challenge: Counting Items

The café wants to know which items sell best. Complete `count_items` so that it returns a lookup table mapping each item to the number of times it appears in `purchases`:

```python
purchases = [
    {"item": "coffee", "price": 3.50},
    {"item": "bagel", "price": 2.25},
    {"item": "coffee", "price": 3.50},
    {"item": "juice", "price": 4.00},
    {"item": "coffee", "price": 3.50},
]

def count_items(purchases):
    # return a dictionary that maps each item to how many times it was bought
    return None

print(count_items(purchases))  # should print {'coffee': 3, 'bagel': 1, 'juice': 1}
```

Start with an empty dictionary. The first time an item appears it is not a key yet, so think about which way of reading a value can handle a missing key.

**<details><summary>Solution</summary>**

```python
def count_items(purchases):
    counts = {}
    for purchase in purchases:
        item = purchase["item"]
        current_count = counts.get(item, 0)
        counts[item] = current_count + 1
    return counts
```

- `counts` starts empty, because the function cannot know in advance which items the purchases contain.
- The first time `"coffee"` appears, `"coffee"` is not a key in `counts` yet. `counts["coffee"]` would raise a `KeyError`, but `counts.get("coffee", 0)` returns the default `0`, which is the right count for an item that has not been seen.
- `counts[item] = current_count + 1` either adds the key with a count of `1` or replaces the old count with one more.

Each key in `counts` comes from the data, so `counts` is a lookup table built from a list of records.

</details>

## Dictionaries are Mutable and Held by Reference

We've already learned that lists are mutable and that a variable holds a reference to a list rather than the list itself. Dictionaries work the same way.

So, when we assign a dictionary to a variable, we are storing a reference to the dictionary's location in memory, not the values themselves.

And when we assign a variable holding a dictionary to another variable, both variables hold a reference to the same dictionary. No copy is made, so a change made through either variable shows up when you look through the other one:

```python
purchase = {"item": "coffee", "price": 3.50}
receipt_line = purchase           # both variables reference the same dictionary
receipt_line["price"] = 3.00      # mutating the referenced dictionary

print(purchase)                   # {'item': 'coffee', 'price': 3.0}
print(receipt_line)               # {'item': 'coffee', 'price': 3.0}
print(purchase is receipt_line)   # True
```

### Changing a Dictionary Inside a Function

The same thing happens when you pass a dictionary to a function. The parameter holds a reference to the caller's dictionary, so if the function changes the parameter, it changes the caller's dictionary too.

A function whose _job_ is to change a record can rely on this. `apply_discount` lowers the price of the purchase it is given and returns nothing, because the caller's dictionary already holds the new price:

```python
def apply_discount(purchase, amount):
    purchase["price"] = purchase["price"] - amount

coffee = {"item": "coffee", "price": 3.50}
apply_discount(coffee, 0.50)
print(coffee)  # {'item': 'coffee', 'price': 3.0}
```

But this must be intentional. A caller who expected `coffee` to keep its original price would be charging every later customer the discounted price.

### Copying a Dictionary Before Changing It

To leave the caller's dictionary unchanged, have the function copy the dictionary first. The `dict()` function copies the key-value pairs of one dictionary into a new dictionary, and the function can then change the copy as much as it likes:

```python
def discounted_copy(purchase, amount):
    new_purchase = dict(purchase)  # copy the key-value pairs of purchase into a new dictionary
    new_purchase["price"] = new_purchase["price"] - amount
    return new_purchase

coffee = {"item": "coffee", "price": 3.50}
sale_coffee = discounted_copy(coffee, 0.50)

print(coffee)                 # {'item': 'coffee', 'price': 3.5}
print(sale_coffee)            # {'item': 'coffee', 'price': 3.0}
print(coffee is sale_coffee)  # False
```

`purchase.copy()` and `{**purchase}` do the same thing as `dict(purchase)`. You will see all three.

## Advanced Topics

### Which Values Can Be Keys

Keys can also be numbers, which comes in handy when you want to look something up by number, like a Roman numeral:

```python
roman_numerals = {
    1: "I",
    5: "V",
    10: "X",
}
```

A key has to be a value that cannot change: a string, a number, or a tuple. A dictionary finds a value by looking up its key, and a key that changed after it went in could no longer be found. A list can change, so a list cannot be a key. If you try, Python stops with `TypeError: unhashable type: 'list'`, and "unhashable" is Python's word for "not allowed as a key".

A tuple can be a key because a tuple cannot change. A tuple key lets a lookup table use two pieces of information at once, such as an item and its size:

```python
sized_menu = {
    ("coffee", "small"): 3.00,
    ("coffee", "large"): 3.50,
    ("juice", "small"): 3.25,
    ("juice", "large"): 4.00,
}

print(sized_menu[("coffee", "large")])  # 3.5
```

### A Copy Shares Its Nested Values

`dict()`, `.copy()`, and `{**my_dict}` all make a **shallow copy**: they copy only the outer dictionary. If a value inside it is a list or another dictionary, the copy and the original share that one inner list or dictionary, so changing it through the copy changes the original too.

Suppose a customer orders a second coffee like their first one, but with an extra shot. Copying the first coffee and adding to the copy's `add_ons` changes the first coffee as well:

```python
first_coffee = {"item": "coffee", "price": 3.50, "add_ons": ["oat milk"]}
second_coffee = dict(first_coffee)
second_coffee["add_ons"].append("extra shot")

print(first_coffee["add_ons"])  # ['oat milk', 'extra shot']
print(first_coffee["add_ons"] is second_coffee["add_ons"])  # True
```

To change a nested list without touching the original, copy that list as well before you change it: `second_coffee["add_ons"] = list(first_coffee["add_ons"])`.

## Summary

A dictionary stores values under names instead of positions, so a program can look each value up by what it means rather than by where it sits. Dictionaries do two jobs. As a **record**, a dictionary keeps the pieces of information about one thing together, such as one purchase's item and price. As a **lookup table**, a dictionary finds a value from a key, such as the price of any item on a menu. Combined with a list, records give a program its most common shape: a list of dictionaries, one for each thing, all with the same keys, so the pieces of information about one thing cannot drift apart the way two parallel lists can. Dictionaries are mutable and held by reference, exactly like lists, so the same decision applies: change the dictionary you were given, or copy it first.
