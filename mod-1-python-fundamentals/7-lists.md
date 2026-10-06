# 1.7 Lists

**Table of Contents**

- [Key Terms](#key-terms)
- [List Basics](#list-basics)
  - [Lists Are Mutable](#lists-are-mutable)
  - [List Methods for Adding and/or Removing Values](#list-methods-for-adding-andor-removing-values)
- [Mutable Values and References](#mutable-values-and-references)
  - [How Lists Are Stored in Memory](#how-lists-are-stored-in-memory)
  - [Mutability vs. Reassignment](#mutability-vs-reassignment)
  - [Impure and Pure Functions](#impure-and-pure-functions)
  - [Making Copies of Lists to Make Pure Functions](#making-copies-of-lists-to-make-pure-functions)
  - [Copying List Challenge](#copying-list-challenge)
- [Advanced List Syntax](#advanced-list-syntax)
  - [2D Lists](#2d-lists)
  - [Tuples: Lists That Cannot Change](#tuples-lists-that-cannot-change)
  - [Unpacking](#unpacking)

## Key Terms

- **Lists** are ordered collections of values. Like strings, they have indexes starting at `0`, support bracket notation and slicing, and work with `len()` and the `in` operator.
- Unlike strings, lists are **mutable**. Methods like `append`, `insert`, `pop`, and `remove` change a list in place.
- A variable does not hold a list. It holds a **reference** to the list. Two variables can reference the same list, and a function receiving a list receives a reference to the caller's list.
- A **pure function** returns the same output for the same input and has no side effects. Functions that mutate the list they are given are impure. To keep a function pure, make a copy first with `list(arr)`, `arr[:]`, or `[*arr]`.
- Lists can contain other lists (**2D lists**), and a list can be **unpacked** into several variables at once. A **tuple** is a list that cannot change, written with parentheses.

## List Basics

- Lists are lists of data (order matters). Values in a list are called **elements of the list**.
- Lists use square brackets `[]` to encapsulate the data
- Like strings lists also...
  - have indexes starting at `0`
  - use bracket notation to access individual elements: `my_list[index]`
  - work with `len()` to get the number of elements in the list
  - support slicing with `[start:end]` and the `in` operator
- Unlike strings, lists are mutable.

```python
friends = ['bert', 'ernie', 'big bird', 'kermit', 'miss piggy', 'elmo']
print(f"type() on a list returns {type(friends)}")

print(f"I have {len(friends)} friends")
print(f"My best friend is {friends[2]}")
print(f"My newest friend is {friends[-1]}")
print(f"My first three friends are {friends[0:3]}")
print(f"Is kermit my friend? {'kermit' in friends}")
print('But here are all of my friends:')

for friend in friends:
    # friend holds the "current" friend that we're looking at in this iteration of the loop
    print(friend)
```

That last loop is the most common thing you will ever do with a list. `for friend in friends` visits each element in order and assigns it to `friend`, with no index and no `range()` in sight. When you _do_ need the position of each element as well, `enumerate()` hands you both:

```python
for index, friend in enumerate(friends):
    print(f"{index}: {friend}")

# 0: bert
# 1: ernie
# ...
```

**Challenge: This function can verify whether or not a given list `items` contains a given value `value`. For each numbered comment below, add a comment explaining the logic of the function!**

```python
def has_value(items, value):
    for item in items:  # 1.
        if item == value:  # 2.
            return True  # 3.
    return False  # 4.

letters = ['a', 'b', 'c', 'd']
print(has_value(letters, 'c'))  # Prints True
print(has_value(letters, 'e'))  # Prints False
```

**<details><summary>Check out this example</summary>**

```python
def has_value(items, value):
    for item in items:  # Look at every element in the list, one at a time
        if item == value:  # Check whether the current element matches the value
            return True  # If it does, we can immediately return True
        # if it doesn't, keep going!
    return False  # If we make it to the end of the loop, we must not have found it. Return False.

letters = ['a', 'b', 'c', 'd']
print(has_value(letters, 'c'))  # Prints True
print(has_value(letters, 'e'))  # Prints False
```

Python has this built in, of course: `value in items` does exactly what `has_value` does. But being able to write it yourself is the point.

</details>

### Lists Are Mutable

Strings have read-only methods like `upper()` and slicing that make a copy of the string but don't change the original string. Trying to change a string in place is an error.

```python
my_name = 'ben'
my_name.upper()   # doesn't mutate the string, it makes a copy
my_name[0] = "J"  # TypeError: 'str' object does not support item assignment
```

Unlike strings, lists let you **mutate** them directly (change their contents without reassignment).

```python
end_letters = ["x", "y", "z"]
end_letters[1] = "foo"
print(end_letters)  # ["x", "foo", "z"]
```

We can even empty a list in one go:

```python
end_letters.clear()  # end_letters now has no values
print(end_letters)  # []
```

**<details><summary>Q: We changed the list without ever writing `end_letters = ...`. Strings would not allow that. Why do lists?</summary>**

Strings are **immutable**: once created, the characters in a string cannot change, so the only way to get a different string is to make a new one and assign it somewhere. Lists are **mutable**: the list object itself can be changed while the variable keeps referencing it. Notice that we never reassign `end_letters`! The variable still references the same list, we're just changing the contents of the list.

Which values are mutable and which are not is one of the most important things to know about any type in Python. Strings, numbers, booleans, and `None` are immutable. Lists and dictionaries are mutable.

</details>

### List Methods for Adding and/or Removing Values

Since lists are mutable, they not only have read-only operations like slicing and `in`, they also have methods for adding to and removing from the list.

These methods let you add values to a list

- `my_list.append(value)` — adds a given value to the end of a list, increasing the length by 1
- `my_list.insert(index, value)` — adds a given value at the given index, pushing everything after it one place to the right

These methods let you remove values from a list

- `my_list.pop()` — removes and returns the last element of a list, reducing the length by 1
- `my_list.pop(index)` — removes and returns the element at the given index
- `my_list.remove(value)` — removes the first element equal to the given value
- `del my_list[index]` — removes the element at the given index (a statement, not a method)

```python
letters = ['a', 'b', 'c', 'd', 'e']

letters.append('f')      # adds 'f' to the end of letters
letters.insert(0, 'z')   # adds 'z' to the beginning of letters
print(letters)  # Prints ['z', 'a', 'b', 'c', 'd', 'e', 'f']

letters.pop()    # removes the last element ('f')
letters.pop(0)   # removes the first element ('z')
print(letters)  # Prints ['a', 'b', 'c', 'd', 'e']

letters.insert(2, 'Hi!')  # At index 2, inserts 'Hi!'
print(letters)  # Prints ['a', 'b', 'Hi!', 'c', 'd', 'e']

letters[2] = 'Hey ;)'  # At index 2, replaces 1 element with 'Hey ;)'
print(letters)  # Prints ['a', 'b', 'Hey ;)', 'c', 'd', 'e']

letters.remove('Hey ;)')  # Removes the first 'Hey ;)' it finds
print(letters)  # Prints ['a', 'b', 'c', 'd', 'e']
```

## Mutable Values and References

Lists and dictionaries are considered **mutable types**, and that changes how variables that hold them behave. Let's see why.

### How Lists Are Stored in Memory

Python stores every value, whether it is a number, a string, or a list, in an area of memory called the **heap**. A variable does not hold the value itself. It holds a **reference to the value's heap address**. Before, we might have thought of a variable like a locker with a value stored inside. In reality, the heap is the locker room and the variable stores which locker the value is stored in, not the locker itself.

You can see the address for yourself. The `id()` function returns a number that identifies where a value lives:

```python
nums = [1, 2, 3]
clone = nums

print(id(nums))          # some large number, like 4395782592
print(id(clone))         # the exact same number
print(nums is clone)     # True: `is` asks whether two variables reference the same object
```

Because `nums` and `clone` hold the same reference, they are two names for one list, not two separate lists.

### Mutability vs. Reassignment

{% hint style="warning" %}
**Predict, then run.** What will the value of `nums` and `clone` be after the program runs?

```python
nums = [1, 2, 3]
clone = nums
clone[1] = 20

print(nums)
print(clone)
```

<details><summary>What actually happens</summary>

```
[1, 20, 3]
[1, 20, 3]
```

Both `nums` and `clone` hold the values `[1, 20, 3]`. Why?

- When we assign `clone = nums`, the "value" of `nums` is the **reference** to the list `[1, 2, 3]`, not the list itself. So, `clone` also holds a reference to the exact same list
- When we mutate `clone[1]`, we are mutating the list referenced by `clone` which is the same list referenced by `nums`. So, both `nums` and `clone` show the mutated list.

If you expected `nums` to still be `[1, 2, 3]`, your mental model was that `clone = nums` copies the list. It copies the _address_.

</details>
{% endhint %}

The same thing happens when we invoke a function and provide a list as an argument:

```python
def empty_the_list(items):
    # 3. Upon receiving the reference, this function modifies the list
    items.clear()

# 1. The list below is created in the heap and the "reference" to its location is stored in letters
letters = ['a', 'b', 'c']

# 2. When we invoke empty_the_list, we assign the "reference" to the function parameter "items"
empty_the_list(letters)

# 4. The list referenced by letters has been modified by the function!
print(letters)  # Prints []
```

A function can never change a caller's string, number, or boolean this way. The parameter still receives a reference, but an immutable value has no method or bracket assignment that changes it in place. The only way to "change" one is to reassign a variable, and reassignment changes only the variable on the left of the `=`, not the immutable value on the right.

```python
x = 10
y = x
y += 1  # shorthand for y = y + 1

print(x)  # 10
print(y)  # 11
```

In this example, even though it _looks_ like we're mutating the value `y`, we are NOT. We're reassigning `y` to reference a completely different value (`11`). `x` never notices.

```python
str = 'hello'
str[0] = 'j'
# TypeError: 'str' object does not support item assignment
```

In this example, when we try to reassign the first character in `str`, a `TypeError` is raised.

### Impure and Pure Functions

Functions are considered **impure functions** if they:

1. Produce different outputs when given the same inputs
2. Produce side effects (like mutating incoming values)

The functions below are impure functions:

```python
import random

# This function can't return the same output each time it is invoked.
def roll_die():
    return random.randint(1, 6)

print(roll_die())  # ???
print(roll_die())  # ???


# This function mutates the incoming list
def empty_the_list(items):
    items.clear()

letters = ['a', 'b', 'c']
empty_the_list(letters)

print(letters)  # Prints []
```

### Making Copies of Lists to Make Pure Functions

Functions that accept lists and modify them are impure. To make a function that modifies a list pure, we need to make a copy of it first. There are three common ways to copy a list, and they all do the same thing:

```python
copy1 = list(letters)   # the list() function builds a new list from any sequence
copy2 = letters[:]      # a slice with no start or end is a copy of the whole thing
copy3 = [*letters]      # the * unpacks the elements into a new list literal
```

The third form is the most flexible, because you can add extra elements while you copy:

```python
def extend(items, value):
    new_items = [*items, value]
    return new_items

letters = ['a', 'b', 'c']
more_letters = extend(letters, 'd')

print(letters)       # Prints ['a', 'b', 'c']
print(more_letters)  # Prints ['a', 'b', 'c', 'd']
```

### Copying List Challenge

Make this impure list function pure!

```python
def shorten(items):
    items.pop()
    return items
```

**<details><summary>Solution</summary>**

```python
def shorten(items):
    new_items = list(items)
    new_items.pop()
    return new_items
```

Or, with a slice that leaves off the last element in the first place:

```python
def shorten(items):
    return items[:-1]
```

</details>

## Advanced List Syntax

### 2D Lists

A list can contain other lists! When the inner lists contain values, we call this a "2-Dimensional (2D)" list or a **"matrix"**.

The matrix below has 2 columns and 5 rows:

```python
coordinates = [
    [30, 90],
    [40, 74],
    [34, 118],
    [42, 88],
    [39, 77],
]

new_orleans = coordinates[0]
new_orleans_lat = coordinates[0][0]
new_orleans_long = coordinates[0][1]

print(new_orleans)
print(new_orleans_lat)
print(new_orleans_long)

print(len(coordinates))     # 5, the number of rows
print(len(coordinates[0]))  # 2, the number of columns in the first row
```

When accessing a 2D list, the first index references the "row" and the second index references the "column"

### Tuples: Lists That Cannot Change

A **tuple** is a list that cannot be changed after it is created. It is written with parentheses instead of square brackets, and everything that reads a list works on it: indexing, slicing, `len()`, `in`, and `for`.

```python
coordinate = (30, 90)

print(coordinate[0])      # 30
print(len(coordinate))    # 2
print(90 in coordinate)   # True

coordinate[0] = 31        # TypeError: 'tuple' object does not support item assignment
```

Use a tuple when the values belong together and should never be added to or removed from, like a latitude and a longitude. Python itself hands you tuples constantly: `enumerate()` produces `(index, value)` pairs, and a dictionary's `.items()` produces `(key, value)` pairs. When you see `choice in ("1", "2")`, that is a tuple being used as a small fixed set of options.

### Unpacking

**Unpacking** makes it possible to take the values from a list and assign them to distinct variables in one statement.

The syntax puts several variable names, separated by commas, on the left side of the assignment operator `=` and the list on the right side (the "source variable"):

```python
coordinates = [
    [30, 90],
    [40, 74],
    [34, 118],
    [42, 88],
    [39, 77],
]

# Unpack the two values from the second row.
new_york_lat, new_york_long = coordinates[1]

print(new_york_lat)   # 40
print(new_york_long)  # 74
```

The number of variables has to match the number of elements, unless one of the variables has a `*` in front. That variable collects "the rest" as a list:

```python
# Unpack the first three rows into their own variables and collect the rest
new_orleans, new_york, los_angeles, *lesser_cities = coordinates

print(los_angeles)    # [34, 118]
print(lesser_cities)  # [[42, 88], [39, 77]]
```

You have seen this pattern already, without the name. `for index, friend in enumerate(friends)` unpacks each `(index, friend)` tuple as it comes out of `enumerate`.
