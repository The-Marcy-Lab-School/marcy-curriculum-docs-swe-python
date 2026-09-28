# Regex (Optional Friday Reading)

{% hint style="info" %}
This chapter is optional reading. Nothing in the Mod 1 assessment or project depends on it, but regular expressions come up constantly in real code, and you will want to recognize one when you see it.

Use https://regexr.com/ to learn about and test regular expressions! Set it to the "Python" flavor.
{% endhint %}

**Table of Contents:**

- [Key Terms](#key-terms)
- [Intro](#intro)
  - [What is a Regular Expression](#what-is-a-regular-expression)
  - [What can you do with regular expressions?](#what-can-you-do-with-regular-expressions)
    - [Validate Strings](#validate-strings)
    - [Extract Strings From Text](#extract-strings-from-text)
- [Regular Expression Syntax](#regular-expression-syntax)
  - [There are a lot of cool ways to use regular expressions](#there-are-a-lot-of-cool-ways-to-use-regular-expressions)
  - [Special Characters](#special-characters)
- [How to Use Regular Expressions in Python](#how-to-use-regular-expressions-in-python)
  - [`re.search(pattern, string)` and `re.IGNORECASE`](#researchpattern-string-and-reignorecase)
  - [`re.findall(pattern, string)`](#refindallpattern-string)
  - [`re.sub(pattern, replacement, string)`](#resubpattern-replacement-string)

## Key Terms

- **Regular expressions (RegEx)** are patterns used to search for, match, and manipulate text strings, providing powerful text processing capabilities.
- In Python, regular expressions live in the standard library's **`re` module**, and patterns are written as raw strings (`r"pattern"`) that can include **special characters** like `^` (start), `$` (end), `\w` (word characters), and `+` (one or more).
- **String validation** is a common use case, allowing you to check if strings match specific formats like email addresses, phone numbers, or date formats.
- **Text extraction** enables finding and extracting specific patterns from larger text blocks, such as extracting all email addresses from a document.
- The `re` module provides several functions: **`fullmatch()`** for validation, **`search()`** for finding the first match and its position, **`findall()`** for extracting every match, and **`sub()`** for substitutions.
- **Flags** like `re.IGNORECASE` modify how patterns behave, making them more flexible and powerful.

## Intro

Consider this function:

{% code title="0_intro.py" lineNumbers="true" %}

```python
def is_only_alphanumeric(string):
    if len(string) == 0:
        return False
    valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    for char in string:
        if char not in valid:
            return False
    return True

print(is_only_alphanumeric('Hello world!'))  # False
print(is_only_alphanumeric('Hello_world'))   # True
```

{% endcode %}

Now, consider the function with regular expressions.

{% code title="0_intro.py" %}

```python
import re

def is_only_alphanumeric_regex(string):
    return re.fullmatch(r"\w+", string) is not None
```

{% endcode %}

### What is a Regular Expression

> A **regular expression** (or "Reg Ex") is a sequence of characters that specifies a "match pattern" to search for strings in text, extract information, or validate input.

In Python, a regular expression is written as a string, and by convention as a **raw string** with an `r` in front of the quotes. The `r` tells Python not to treat backslashes as escape characters, so that `\w` reaches the `re` module as the two characters `\` and `w` rather than being mangled.

```python
import re

pattern = re.compile(r"\w+")
print(type(pattern))  # <class 're.Pattern'>
```

The symbols and characters inside the string define the characteristics of the strings that the regular expression can be used to search for. In the example above, we have:

- `\w+` one or more word characters (letters, numbers, or `_`).
  - The `\w` represents a word character and the `+` modifier means "one or more"

`re.fullmatch` requires that the _whole_ string match the pattern, from the first character to the last, with nothing else (no spaces, no symbols, nothing!). It returns a match object if it does and `None` if it does not, which is why the function above compares against `None`.

### What can you do with regular expressions?

#### Validate Strings

Like the `is_only_alphanumeric` function, regular expressions are often used to validate if a string matches a specific pattern.

One of the most common challenges in applications is validating proper date formats. This function uses a regular expression to ensure that a given string is in the "MM-DD-YYYY" format:

{% code title="1_is_valid_date.py" %}

```python
import re

def is_valid_date_str(date_str):
    # requires 'MM-DD-YYYY' formatted date strings
    date_pattern = r"(0[1-9]|1[0-2])-([0-2][0-9]|3[01])-[0-9]{4}"
    return re.fullmatch(date_pattern, date_str) is not None

print(is_valid_date_str('10-12-1995'))    # True
print(is_valid_date_str('a 10-12-1995'))  # False
print(is_valid_date_str('12-32-2024'))    # False
```

{% endcode %}

#### Extract Strings From Text

One cool usage of regular expressions is to "find all instances of X in a string". For example, in a big block of text, grab all of the emails:

{% code title="0_intro.py" %}

```python
import re

def extract_emails(text):
    email_pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
    return re.findall(email_pattern, text)

message = """
Dear Team,

Thank you for attending the meeting earlier today. As discussed, please reach out to the following team members if you have any questions or need further clarification:

For project management updates, contact Sarah at sarah.jones@example.com.
For technical issues, reach out to Mike at mike.smith@example.com.
For client communications, please email Julia at julia.roberts@example.com.
Let me know if you need anything else.

Best regards,
John
john.doe@example.com
"""

emails = extract_emails(message)
print(emails)

# [
#   'sarah.jones@example.com',
#   'mike.smith@example.com',
#   'julia.roberts@example.com',
#   'john.doe@example.com'
# ]
```

{% endcode %}

The triple quotes `"""` make a string that spans several lines. You will see them again in Mod 2, where they are used for documentation.

## Regular Expression Syntax

### There are a lot of cool ways to use regular expressions

Here are some snippets to get started!

| **Name**                   | **Info**                              | **Example**           |
| -------------------------- | ------------------------------------- | --------------------- |
| Flags                      | passed as a separate argument         | `re.IGNORECASE`       |
| letters                    | You know letters                      | `r"dog"`              |
| digits                     | You know digits                       | `r"12"`               |
| Character Set/Class        | Brackets                              | `r"[aeiou]"`          |
| Negated Character Set      | Carrot and brackets                   | `r"[^aeiou]"`         |
| O or more                  | \*                                    | `r"a*"`               |
| 1 or more                  | +                                     | `r"a+"`               |
| 0 or 1                     | ?                                     | `r"a?"`               |
| Or                         | \|                                    | `r"cat\|dog"`         |
| Start of string            | Carrot, no brackets                   | `r"^hi"`              |
| End of string              | Dollar sign                           | `r"bye$"`             |
| Quantifier exactly         | Braces, one number                    | `r"AH{10}"`           |
| Quantifier at least X many | Braces, one number and comma          | `r"OH{3,}"`           |
| Quantifier exact range     | Braces, two comma separated numbers   | `r"WO{2,4}W"`         |
| Groups                     | Parens with optional pipe OR operator | `r"(my)\s(cat\|dog)"` |

### Special Characters

| Character Class | Definition                    |
| --------------- | ----------------------------- |
| [0-9]           | Any single digit              |
| [3-30]          | And number in range           |
| [a-z]           | Any lowercase letter          |
| [a-d]           | Any lowercase letter in range |
| [A-Z]           | Any uppercase letter          |
| [E-Q]           | Any uppercase letter          |
| [a-zA-Z]        | Any letter                    |
| \d              | Any single digit              |
| \D              | Any NON digit                 |
| \w              | Any alphanumeric (and \_)     |
| \W              | Any NON alphanumeric          |
| \s              | Any whitespace character      |
| \S              | Any NON whitespace character  |
| \b              | Any word break                |
| \B              | Any NON word break            |
| .               | Any character at all          |
| \\.             | An escaped period             |

## How to Use Regular Expressions in Python

The functions in the `re` module to be aware of are:

1. `re.fullmatch(pattern, string)` - validate that the whole string matches
2. `re.search(pattern, string)` - find the first match in a string and where it is
3. `re.findall(pattern, string)` - find every match in a string
4. `re.sub(pattern, replacement, string)` - replace one or more matches in a string

> Note that every one of these takes the pattern first and the string second.

### `re.search(pattern, string)` and `re.IGNORECASE`

`re.search` returns a match object if there is a match between the pattern and the given string anywhere in it, and `None` otherwise. Since a match object is truthy and `None` is falsy, you can use the result directly in an `if`:

```python
import re

print(re.search(r"cat", "the cat in the hat"))  # <re.Match object; span=(4, 7), match='cat'>
print(re.search(r"cat", "the dog in the hat"))  # None, because no "cat"
print(re.search(r"cat", "the Cat in the hat"))  # None, because of case sensitivity
```

By default, regular expressions are case sensitive and, unless otherwise specified, must be an exact match.

Passing the `re.IGNORECASE` flag as a third argument allows for case-**insensitive** matches:

```python
print(re.search(r"cat", "the cat in the hat", re.IGNORECASE))  # a match
print(re.search(r"cat", "the Cat in the hat", re.IGNORECASE))  # also a match
```

The match object knows where the match was found. `.start()` returns the index of the first match:

```python
phrase = 'How now brown cow?'
print(re.search(r"brow", phrase).start())  # 8
print(re.search(r"ow", phrase).start())    # 1
```

Be careful: if there is no match, `re.search` returns `None`, and `None.start()` raises an `AttributeError`. Check for `None` first.

### `re.findall(pattern, string)`

`re.findall` returns a list containing every match between the string and the given pattern.

```python
phrase = 'My cat named caterpillar loves catnip.'

print(re.findall(r"cat", phrase))       # ['cat', 'cat', 'cat']
print(len(re.findall(r"cat", phrase)))  # 3

print(re.findall(r"ow", 'How now brown cow?'))  # ['ow', 'ow', 'ow', 'ow']
```

There is no "first match only" version to worry about here. `re.search` finds the first, `re.findall` finds them all.

### `re.sub(pattern, replacement, string)`

`re.sub` replaces matches between the string and the given pattern with the given `replacement` string.

```python
phrase = "my cat is named Catherine"

# Replace every "cat", regardless of case
new_phrase = re.sub(r"cat", "dog", phrase, flags=re.IGNORECASE)

print(new_phrase)  # Prints 'my dog is named dogherine'
```

By default, `re.sub` replaces ALL matches. You can limit it with the `count` keyword argument:

```python
phrase = "my cat is named Catherine"

# Replace only the first "cat", regardless of case
new_phrase = re.sub(r"cat", "dog", phrase, count=1, flags=re.IGNORECASE)

print(new_phrase)  # Prints 'my dog is named Catherine'
```

Notice that `flags` has to be passed by keyword here, because `re.sub` has a `count` parameter in the position where `re.search` takes its flags. That is the kind of detail nobody memorizes; you look it up in the [`re` documentation](https://docs.python.org/3/library/re.html) when you need it.
