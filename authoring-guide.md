# Writing Lessons for GitBook and the LMS

This guide is for instructors who edit the lessons in this repository, or who write their own curriculum repository and want it to work in the same places. Every lesson is published twice from the same Markdown file:

- **GitBook** publishes the repository as a website that fellows read.
- **The LMS** copies each lesson into a course, shows it beside the fellow's other course work, and puts a Run button on code blocks so that fellows can run the code inside the lesson.

The two programs read the same file but support different features. A lesson that uses only the syntax in this guide looks right in GitBook and runs correctly in the LMS.

## Syntax That Works in Both

| Feature | How to write it | Notes |
| --- | --- | --- |
| Callouts | `{% hint style="info" %}` … `{% endhint %}` | The four styles are `info`, `warning`, `danger` and `success`. The LMS draws an unknown style as `info`. |
| Dropdowns | `<details><summary>Q: …</summary>` … `</details>` | See [Dropdowns](#dropdowns) for the blank lines the content needs. |
| Code block titles | `{% code title="04_parameters.py" %}` above the fence, `{% endcode %}` below it | The LMS draws the title above the block. |
| Embedded documents | `{% embed url="…" %}` | The LMS shows Google Docs, Sheets and Slides in a frame. Any other address, YouTube included, becomes a plain link that opens in a new tab. |
| Diagrams | A ` ```mermaid ` fence | In GitBook, a dunder name inside a diagram such as `__repr__()` is drawn in bold unless each underscore is escaped: write `\_\_repr\_\_()`. |
| Keyboard keys | `<kbd>Ctrl</kbd>` | |
| Images | `![description](img/file.png)`, or `<img src="…" width="400">` | The LMS loads images from GitHub at the commit the lesson was copied from, so commit and push an image in the same commit as the lesson that shows it. |
| Figures | `<figure>` with `<img>` and `<figcaption>` | |
| Tables, task lists, strikethrough | GitHub-flavoured Markdown | |
| Links to another lesson | A relative link to the lesson's `.md` file, such as `[Decorators](../mod-2-oop-python/7-decorators.md)` | The LMS opens the lesson's page in the same course. A link to any other file in the repository opens that file on GitHub. |
| Links to a heading | `[Closures](#closures)` | Search results in the LMS and the Tutor's references link to heading anchors, so renaming a heading breaks every link to it. |

Two rules about headings apply in both programs:

- **Never put a bare `&` in a heading. Write "and".** GitBook drops the ampersand when it builds the heading's anchor, so a heading such as "Keys & Values" gets the anchor `#keys--values`, and every link written as `#keys-values` fails.
- **Do not edit a table of contents by hand.** Run `python3 scripts/update-toc.py <file.md>` after changing a heading.

### Dropdowns

A dropdown holds a hidden answer or solution. Markdown inside a dropdown only renders when blank lines separate it from the HTML tags, so leave a blank line after the `<summary>` line and another before `</details>`:

```markdown
**<details><summary>Q: Why does the error mention `is_free()`?</summary>**

The error happens before `find_events()` runs.

</details>
```

Without the blank lines, both programs show the backticks and asterisks as plain characters instead of formatting them.

## Syntax That Does Not Work in the LMS

**Tabs.** The LMS does not yet draw `{% tabs %}` and `{% tab title="…" %}`. It shows the tags as plain text, and the course sync lists every tab group under the curriculum's problems in the LMS's Admin page. If a page has to work in the LMS now, write the alternatives one after another, each under a bold label such as **Mac** and **Windows**.

## Runnable Code Blocks

### Which blocks get a Run button

| Fence language | What the Run button does |
| --- | --- |
| `python`, `py`, `python3` | Runs the block in a copy of Python built for the browser, with a terminal that shows output and accepts `input()`. |
| `html` | Draws the page in a sandboxed frame. The `css` and `js` fences that follow it, up to the next heading or the next `html` fence, run inside the same page, so a lesson that shows HTML, then CSS, then JavaScript runs as one page. Those following fences get no Run button of their own. |
| `js`, `javascript` on their own | Runs the block in a hidden frame and shows only the console. A block that uses `require()` or a Node module fails, because there is no Node in the browser. |
| Every other language, such as `sh`, `sql`, `bash`, `json` | Shows the code with a Copy button and no Run button. |

Program output is not code, so fence it with no language (` ``` ` on its own). A block of output fenced as `python` gets a Run button, and running it raises an error.

### Every runnable block must run on its own

**The problem:** each Python block runs in a fresh interpreter, so it can use only the names that it defines itself. A block that calls `hall.find_events()` after an earlier block built `hall` stops with `NameError: name 'hall' is not defined`. A fellow who presses Run and sees an error the lesson never mentions will believe that they broke something.

The fresh interpreter is also what makes a block's output reliable: a block prints the same thing however many times a fellow runs it and in whatever order. So the rule is that every runnable block runs on its own and prints exactly what its output comments say. A block may still raise an error when that error is the one the lesson is teaching.

There are three ways to make a block that depends on earlier code run on its own:

1. **Copy a short definition into the block itself,** with a comment above it saying where it comes from. Use this when the definition is a few lines long, about 8 or fewer. The comment reads `# unchanged from the previous example`, or names a place in the same lesson, such as `# unchanged from Closures`. Never refer to another chapter by its number. An `import` line needs no comment.
2. **Give the block a hidden setup.** Use this when the earlier code is long enough to bury the point of the block, as a 30-line class above a 3-line example would.
3. **Mark the block as not runnable.** Use this only for a block that cannot run in the browser at all. The cases are listed in [Blocks That Cannot Run](#blocks-that-cannot-run).

### Hidden setup

A setup is a piece of Python code with a name, written inside an HTML comment, so that neither GitBook nor the LMS shows it to fellows. When a fellow runs a block, the LMS runs the setups that the block names first, in the same interpreter, and then runs the block.

**Defining a setup.** Write the setup once on the page:

```markdown
<!-- setup: event
from datetime import date

class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
-->
```

- The first line is exactly `<!-- setup: ` followed by the name. A name uses lowercase letters, digits and hyphens.
- The code starts on the next line, at the left margin, even when the setup sits inside a callout or a dropdown.
- The setup ends at a line that holds only `-->`. Because `-->` ends the comment, the code inside it can never contain `-->`.
- A setup prints nothing, because the output a fellow sees should come from the block they ran. The one exception is a block whose prompt asks fellows to add a line to the bottom of the code above it. There, the setup copies that code with its `print()` calls, so the block prints what the whole program would print.
- A setup belongs to its page. Another lesson cannot use it.

**Using a setup.** Put a `uses` comment on the line directly above the block's opening fence, naming one or more setups separated by commas:

````markdown
<!-- uses: event, find-events -->
```python
print(hall.find_events(is_free))   # [Event('Board Game Night', 2027-01-08)]
```
````

The setups run in the order they are listed, so a setup can rely on any setup listed before it. In the example, `find-events` builds `hall` with the `Event` class that `event` defines.

When a block is wrapped in `{% code %}`, put the comment above the `{% code %}` line instead, so that nothing comes between `{% code %}` and its fence:

````markdown
<!-- uses: event -->
{% code title="venue.py" %}
```python
...
```
{% endcode %}
````

When a block sits inside a list item, indent its `uses` or `not-runnable` comment to the same depth as the fence. Markdown reads a line indented to the item's content as part of the item, so the comment stays directly above its block. The indentation must reach the item's content without going past it: two spaces after a `-` bullet is enough, and eight or more turns the fence into an indented code block with no language, which gets no Run button. A setup never goes inside a list item, because it has to start at the left margin. Put it after the list instead.

**Where to put a setup, and what goes in it.** A setup is a copy of code that fellows have already seen on the page, so place each setup directly after the visible block it copies. Copy the code exactly, with the same names, keyword arguments, values and quotes, and leave out the `print()` lines. Placing the copy beside its original means that whoever next edits the visible block sees the hidden copy directly beneath it and can update both together.

Sometimes a setup cannot copy the block directly above it: the block it copies sits inside a list, the visible class has a `# ...` placeholder that the setup fills in, or the visible block depends on code the page never shows, such as a class from the case study. Then the setup's first line names where its code comes from:

```markdown
<!-- setup: attendee
# copies: the case study's src/attendee.py
from dataclasses import dataclass
...
-->
```

A running example that changes from section to section, such as an `Event` class that gains a method in each section, needs one setup for each version. Name each setup after what that version adds, such as `first-hall` and `find-events`.

### Blocks That Cannot Run

Put `<!-- not-runnable -->` on the line directly above the opening fence, or above the `{% code %}` line that wraps it. The LMS shows the block with a Copy button and no Run button. Use it for these blocks only:

- A challenge prompt that fellows complete in the lecture code repository, such as a block that calls a method the fellow has not written yet.
- A file from a project that imports from that project's `src/` folder, or imports `pytest`.
- A syntax template, such as `[expression for item in source_list]`.
- A JavaScript block that uses `require()` or a Node module.

Never mark a block as not runnable to hide an error that the lesson teaches. Running the block and seeing that exact error is the point of the block.

### Checking a lesson before publishing

`scripts/check-code-blocks.py` runs every Python block in a lesson the way the LMS runs it, with its setups, and prints one line for each block that fails:

```sh
python3.14 scripts/check-code-blocks.py mod-2-oop-python/6-functions-as-values-hof.md
```

Run it with the Python version fellows install, so that the results match what fellows see. Every line it prints should be one of these:

- an error that the lesson teaches;
- an `EOFError` from a block that calls `input()`, because the script gives blocks no keyboard input, although the LMS does.

The script also reports any setup whose code no longer appears, line for line and in the same order, in the visible block directly above it. That warning means someone edited the visible block and not its hidden copy. It ignores comments, blank lines and `import` lines, and it allows the setup to leave lines out, such as `print()` calls. It skips a setup that has a `# copies:` line.

Add `--show` to print every block's output, and compare each output with the block's output comments. The script checks Python blocks only. Run HTML and JavaScript blocks in the LMS.

## A Complete Example

The lesson below shows a class, then a block that uses it, with the class supplied by a hidden setup:

````markdown
```python
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)


hall = Venue('Riverside Community Hall')
hall.add_event('Friday Night Jazz')
print(hall.events)   # ['Friday Night Jazz']
```

<!-- setup: hall
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)


hall = Venue('Riverside Community Hall')
hall.add_event('Friday Night Jazz')
-->

{% hint style="warning" %}
**Predict, then run.** What does this print?

<!-- uses: hall -->
```python
print(len(hall.events))
```

<details><summary>What actually happens</summary>

```
1
```

</details>
{% endhint %}
````

- The first block runs on its own and shows the full class.
- The setup copies that block without its `print()` line.
- The predict box stays one line long, because the `uses: hall` comment supplies `Venue` and `hall` when a fellow presses Run.
- The answer's output is fenced with no language, so it gets no Run button.
