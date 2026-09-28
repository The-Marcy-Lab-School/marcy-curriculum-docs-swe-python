# 9. Dictionaries

**Table of Contents**:

- [Key Terms](#key-terms)
- [The basics](#the-basics)
  - [Accessing Values with Bracket Notation and `.get()`](#accessing-values-with-bracket-notation-and-get)
  - [Dynamic Keys Challenge](#dynamic-keys-challenge)
- [Dictionaries are Mutable and Held by Reference](#dictionaries-are-mutable-and-held-by-reference)
- [Iterating Over Keys and Values of a Dictionary](#iterating-over-keys-and-values-of-a-dictionary)
- [Lists of Dictionaries](#lists-of-dictionaries)
- [Dictionaries and Functions](#dictionaries-and-functions)
  - [Building a Dictionary from Parameters](#building-a-dictionary-from-parameters)
  - [Passing a Dictionary to a Function](#passing-a-dictionary-to-a-function)

## Key Terms

- **Dictionaries** are data structures that store multiple pieces of data as key-value pairs, useful for representing real-world entities like users or products.
- Dictionary values are accessed using **bracket notation** (`my_dict["key"]`), which raises a `KeyError` for a missing key, or with the **`.get()`** method, which returns `None` (or a default you choose) instead.
- Dictionaries are **mutable**, meaning you can add, modify, or delete key-value pairs after creation using assignment, `del`, or `.pop()`.
- Dictionaries can contain **nested data** including lists and other dictionaries, allowing for complex data structures.
- Like lists, dictionaries are held by **reference**. Copy one with `dict(my_dict)` before changing it inside a pure function.
- **`.keys()`**, **`.values()`**, and **`.items()`** let you loop over a dictionary. `.items()` hands you each key and value together.

## The basics

- Dictionaries are a data type that can store multiple pieces of data as **key: value** pairs
- You will also hear dictionaries called **maps** or **hashmaps**:

```python
# Lists store values in an order
words = [
    "hello",
    "rainbow",
    "cat",
]

# Dictionaries store key: value pairs
dictionary = {
    "hello": "a casual greeting",
    "rainbow": "a colorful arc of light",
    "cat": "the superior pet",
}
```

- Dictionaries are useful for storing collections of data related to a single "thing", like data about a user.
- Dictionaries can have lists and other dictionaries nested inside.

```python
user = {
    "user_id": 44292,
    "username": 'c0d3rkid',
    "password": 'pywiz1234',
    "friends": ['iLoveSoccer123', 'rubyNinja', 'messiGOAT'],
    "favorite_meal": {
        "name": 'PB&J',
        "ingredients": ['peanut butter', 'jelly', 'bread'],
    },
}
```

- Keys are usually strings, and the quotes around them are required. Keys can also be numbers, which will come in handy when you want to count things.

```python
roman_numerals = {
    1: "I",
    5: "V",
    10: "X",
}
```

A key can be any value that cannot change: a string, a number, or a tuple. A list cannot be a key.

### Accessing Values with Bracket Notation and `.get()`

- Dictionary values can be accessed and/or mutated using bracket notation with the key inside the brackets

```python
# Bracket notation requires the key
print(f"Hi, my name is {user['username']}")

# Bracket notation can be used to modify existing values, or create new ones!
user["password"] = 'try to break in now!'
user["is_admin"] = False

print(user)

# If a value is a dictionary or list, we can use bracket notation on that value!
print(f"My favorite meal is {user['favorite_meal']['name']}")
print(f"My best friend is {user['friends'][0]}")

# Delete key-value pairs with the `del` keyword followed by bracket notation
del user["user_id"]
del user["friends"]
```

{% hint style="warning" %}
**Predict, then run.** There is no `"age"` in `user`.

```python
print(user["age"])
```

<details><summary>What actually happens</summary>

```
KeyError: 'age'
```

Asking a dictionary for a key it does not have is an error, just like asking a list for an index it does not have. When you are not sure a key exists, use the `.get()` method instead. It returns `None` for a missing key, or a default value of your choosing:

```python
print(user.get("age"))          # None
print(user.get("age", 0))       # 0
print(user.get("username"))     # c0d3rkid
```

You can also ask first. The `in` operator on a dictionary checks the _keys_:

```python
if "age" in user:
    print(user["age"])
```

</details>
{% endhint %}

### Dynamic Keys Challenge

Because the key goes inside the brackets as an expression, it does not have to be typed out as a literal string. It can be a variable:

```python
key = 'some key'
my_dict[key] = 'new value'  # adds the key 'some key'
```

Complete the program below so that it lets users add words to the dictionary!

```python
dictionary = {
    "hello": "a casual greeting",
    "rainbow": "a colorful arc of light",
    "cat": "the superior pet",
}

while True:
    print("Here are your words: ", dictionary)
    new_word = input("Add a word to your dictionary, or press q to exit. ")

    if new_word == 'q':  # a guard clause
        break

    definition = input(f"Okay, what is the definition of {new_word}? ")

    # add the new word and its definition to the dictionary!
```

**<details><summary>Solution</summary>**

To complete this program, add the line `dictionary[new_word] = definition` to the end of the loop.

</details>

## Dictionaries are Mutable and Held by Reference

We've already learned that lists are mutable and that a variable holds a reference to a list rather than the list itself. Dictionaries work the same way.

So, when we assign a dictionary to a variable, we are storing a reference to the dictionary's location in memory, not the values themselves.

And when we assign a variable holding a dictionary to another variable, each variable holds a reference to the same dictionary

```python
sheep = {'name': 'benny', 'noise': 'baaaa'}
clone = sheep           # both variables reference the same dictionary
clone['noise'] = 'BAAAAA'  # mutating the referenced dictionary

print(sheep)  # {'name': 'benny', 'noise': 'BAAAAA'}
print(clone)  # {'name': 'benny', 'noise': 'BAAAAA'}
```

We can use the `dict()` function to copy the key-value pairs of one dictionary into a new dictionary. This is particularly useful when creating pure functions:

```python
sheep = {'name': 'benny', 'noise': 'baaaa'}

def make_loud_clone(animal):
    clone = dict(animal)  # copy the key-value pairs of animal into a new dictionary
    clone['noise'] = clone['noise'].upper()
    return clone

clone = make_loud_clone(sheep)

print(sheep)  # {'name': 'benny', 'noise': 'baaaa'}
print(clone)  # {'name': 'benny', 'noise': 'BAAAA'}
```

`animal.copy()` and `{**animal}` do the same thing as `dict(animal)`. You will see all three.

## Iterating Over Keys and Values of a Dictionary

One of the key benefits of a list is that we can easily iterate through its values with a `for` loop.

```python
friends = ['bert', 'ernie', 'elmo']
print("here are my friends:")

for friend in friends:
    print(friend)
```

A `for` loop over a dictionary visits its **keys**:

```python
dictionary = {
    "hello": "a casual greeting",
    "rainbow": "a colorful arc of light",
    "cat": "the superior pet",
}

for word in dictionary:
    print(f"The definition of {word} is {dictionary[word]}")
```

Dictionaries also have three methods that give you exactly the part you want to loop over:

- `dictionary.keys()` — all of the keys
- `dictionary.values()` — all of the values
- `dictionary.items()` — every key and its value, paired up

```python
definitions = dictionary.values()

print("Can you tell what word each of these definitions are for?")
for definition in definitions:
    print(definition)
```

`.items()` is the one you will reach for most, because it hands you both halves of each pair and you unpack them right in the `for` line:

```python
for word, definition in dictionary.items():
    print(f"The definition of {word} is {definition}")
```

{% hint style="warning" %}
**Predict, then run.**

```python
print(dictionary.keys())
print(len(dictionary))
print(list(dictionary.keys())[0])
```

<details><summary>What actually happens</summary>

```
dict_keys(['hello', 'rainbow', 'cat'])
3
hello
```

`.keys()` does not return a list. It returns a `dict_keys` object, which you can loop over and check membership in, but cannot index with `[0]`. If you need a real list, wrap it in `list()`, which is what the third line does. `len()` on the dictionary itself counts the key-value pairs.

</details>
{% endhint %}

## Lists of Dictionaries

The shape you will use more than any other is a list where every element is a dictionary with the same keys. It is how a program holds "many of the same kind of thing":

```python
users = [
    {"name": "Ben", "age": 28, "is_admin": False},
    {"name": "Maya", "age": 25, "is_admin": True},
    {"name": "Reuben", "age": 41, "is_admin": True},
]

# The loop hands you one dictionary at a time
for user in users:
    print(f"{user['name']} is {user['age']}")

# Reach one by position, then by key
print(users[1]["name"])   # Maya

# Add a new one the same way you add to any list
users.append({"name": "Gonzalo", "age": 30, "is_admin": False})
```

The task manager case study stores its tasks this way, and every project option in this module does too.

## Dictionaries and Functions

### Building a Dictionary from Parameters

Functions often build a dictionary from their parameters, together with some default values. This one makes a user with the provided properties, `is_admin` set to `False`, and an empty `friends` list:

```python
def make_user(name, age):
    new_user = {
        "name": name,
        "age": age,
        "is_admin": False,
        "friends": [],
    }
    return new_user

user1 = make_user('ben', 30)
```

Notice that the key `"name"` and the variable `name` are spelled the same but are two different things. The key is a string inside the dictionary. The variable holds the value that gets stored under that key.

### Passing a Dictionary to a Function

When a dictionary is passed to a function, the function reaches into it with bracket notation for only the values it cares about:

```python
user_ben = {
    "name": "Ben",
    "age": 28,
    "is_admin": False,
}

def introduce_self(user):
    print(f"Hello! My name is {user['name']} and I am {user['age']} years old.")

introduce_self(user_ben)
```

`introduce_self` never looks at `is_admin`, and it doesn't need to. A function that takes a dictionary only has to know about the keys it uses.
