# Markdown Guide

**Table of Contents:**

- [What is Markdown?](how-to-write-markdown.md#what-is-markdown)
- [Headers](how-to-write-markdown.md#headers)
- [Bold and Italic](how-to-write-markdown.md#bold-and-italic)
- [Backticks for Inline Code](how-to-write-markdown.md#backticks-for-inline-code)
- [Code Fences for Blocks of Code](how-to-write-markdown.md#code-fences-for-blocks-of-code)
- [Bulleted Lists](how-to-write-markdown.md#bulleted-lists)
- [Numbered Lists](how-to-write-markdown.md#numbered-lists)
- [Links](how-to-write-markdown.md#links)
- [Previewing Your Markdown](how-to-write-markdown.md#previewing-your-markdown)
- [Quick Reference](how-to-write-markdown.md#quick-reference)

## What is Markdown?

Markdown is a way of writing formatted text using only plain characters that you can type on any keyboard. Instead of clicking a "Bold" button, you wrap a word in asterisks (e.g. `*bold word*`). Instead of choosing "Heading 1" from a menu, you start the line with a pound sign (e.g. `# heading`). A program then reads those characters and turns them into formatted text with headings, bold words, lists, and links.

You will write Markdown constantly at Marcy and in your career:

- Every `README.md` file in a GitHub repository is written in Markdown.
- Short response (swe-sr) assignments are written in Markdown files.
- GitHub issues, pull request descriptions, and code review comments all use Markdown.
- Many documentation sites, including this one, are written in Markdown.
- Most AI chat-based tools read and generate Markdown

Markdown files end in `.md`. When you open one in VS Code, you see the raw characters. When you view the same file on GitHub, you see the formatted result.

Each section below shows the characters you type, followed by what a reader sees.

## Headers

A header is a line that begins with one or more pound signs (`#`) followed by a space. One pound sign makes the largest header. Each additional pound sign makes a smaller header, down to six levels.

You type:

```markdown
# Title of the Document

Normal text

## A Major Section

Normal text

### A Subsection

Normal text
```

A reader sees:

> # Title of the Document
>
> Normal text
>
> ## A Major Section
>
> Normal text
>
> ### A Subsection
>
> Normal text

Use headers to give a document a structure that a reader can scan. A typical document has

- exactly one level-one header at the top
- level-two headers for its major sections
- level-three headers for subsections within those

The space after the pound signs is required. `#Title` without the space is not a header. It renders as a paragraph that happens to begin with a pound sign.

## Bold and Italic

To make text **bold**, wrap it in two asterisks on each side. To make text _italic_, wrap it in one asterisk on each side. To make text **_bold and italic_**, wrap it in three.

You type:

```markdown
This word is **bold**. This word is _italic_. This word is **_both_**.
```

A reader sees:

> This word is **bold**. This word is _italic_. This word is **_both_**.

Underscores work the same way as asterisks: `__bold__` and `_italic_` produce the same result. Pick one style and use it consistently.

Use bold to draw the eye to the one or two most important terms in a paragraph. Use italic for gentle emphasis or for the title of a book or article. If every other word is bold, nothing stands out.

## Backticks for Inline Code

When you mention a variable name, a function name, a file name, or a command inside a sentence, wrap it in single backticks. The backtick key is usually in the top-left corner of the keyboard, above the Tab key.

You type:

```markdown
The `get_area()` function is defined in `shapes.py`. Run `pytest` to test it.
```

A reader sees:

> The `get_area()` function is defined in `shapes.py`. Run `pytest` to test it.

Backticks tell the reader that the characters inside are code, to be typed exactly as shown. They also stop Markdown from interpreting special characters. For example, `*args` would normally begin italic text, but inside backticks the asterisk is displayed as an asterisk.

Use backticks for anything a reader might copy into an editor or a terminal: names of functions, variables, files, folders, packages, commands, and keyboard keys.

## Code Fences for Blocks of Code

To show several lines of code at once, put the code between two lines of three backticks. This is called a code fence. Write the name of the programming language immediately after the opening backticks so that the code is displayed with syntax highlighting.

You type:

````markdown
```python
def get_area(radius):
    return 3.14159 * radius ** 2

print(get_area(2))
```
````

A reader sees:

> ```python
> def get_area(radius):
>     return 3.14159 * radius ** 2
>
> print(get_area(2))
> ```

Everything between the fences is displayed exactly as written, including indentation and blank lines. Markdown formatting is turned off inside a code fence, so asterisks and pound signs appear as themselves.

The language name after the opening fence is optional but strongly recommended since they add colored syntax-highlighting which makes the code much easier to read. Here is the same example rendered without a language:

> ```
> def get_area(radius):
>     return 3.14159 * radius ** 2
>
> print(get_area(2))
> ```

Common values are `python`, `javascript`, `html`, `css`, `sql`, `sh` for terminal commands, and `json`. To show terminal commands and their output without highlighting, leave the language name off.

## Bulleted Lists

To make a bulleted list, start each line with a hyphen (`-`) followed by a space. Put a blank line before the first item so that Markdown knows a new list is starting.

You type:

```markdown
Things to check before submitting:

- All tests pass
- Code is formatted
- Work is committed and pushed
```

A reader sees:

> Things to check before submitting:
>
> - All tests pass
> - Code is formatted
> - Work is committed and pushed

To nest one list inside another, indent the inner items by two spaces.

You type:

```markdown
- Backend
  - Flask
  - Postgres
- Frontend
  - HTML and CSS
  - Jinja templates
```

A reader sees:

> - Backend
>   - Flask
>   - Postgres
> - Frontend
>   - HTML and CSS
>   - Jinja templates

An asterisk (`*`) or a plus sign (`+`) at the start of a line also makes a bullet. This guide uses hyphens because they never conflict with the asterisks used for bold and italic.

## Numbered Lists

To make a numbered list, start each line with a number, a period, and a space. Use a numbered list when the order of the items matters, such as steps to follow.

You type:

```markdown
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Run `pytest` to confirm the tests run
```

A reader sees:

> 1. Clone the repository
> 2. Run `pip install -r requirements.txt`
> 3. Run `pytest` to confirm the tests run

Markdown counts for you. If you write `1.` in front of every item, the list still renders as 1, 2, 3. This is useful when you insert a step in the middle of a long list, because you do not need to renumber everything after it.

## Links

A link has two parts: the text a reader clicks, in square brackets, followed immediately by the destination address, in parentheses. There is no space between the closing bracket and the opening parenthesis.

You type:

```markdown
Read the [Python documentation](https://docs.python.org/3/) for details.
```

A reader sees:

> Read the [Python documentation](https://docs.python.org/3/) for details.

Make the link text describe where the link goes. A reader scanning a document should understand the destination from the text alone. Write "read the [debugging guide](how-to-debug.md)" rather than "click [here](how-to-debug.md)".

A link can point to another file in the same repository by using a relative path instead of a full address. The example above links to `how-to-debug.md`, which sits in the same folder as this guide. To link to a file in a subfolder, include the folder name: `[setup steps](environment-setup/github-setup.md)`.

If you paste a full address on its own, GitHub turns it into a clickable link automatically, but the reader sees the whole address instead of a description. Prefer the bracket and parenthesis form.

## Previewing Your Markdown

VS Code can show you the formatted result while you type. With a `.md` file open, press `Cmd+Shift+V` on Mac or `Ctrl+Shift+V` on Windows to open a preview tab. To see the raw file and the preview side by side, press `Cmd+K` and then `V` on Mac, or `Ctrl+K` and then `V` on Windows.

Check the preview before you commit. The most common mistakes are a missing space after a pound sign, a missing blank line before a list, and a missing closing asterisk or backtick.

## Quick Reference

| To get this    | Type this                                                               |
| -------------- | ----------------------------------------------------------------------- |
| Header         | `# Title`                                                               |
| Smaller header | `## Section`                                                            |
| Bold           | `**word**`                                                              |
| Italic         | `*word*`                                                                |
| Inline code    | `` `code` ``                                                            |
| Code block     | Three backticks, a language name, the code, and three closing backticks |
| Bullet         | `- item`                                                                |
| Numbered item  | `1. item`                                                               |
| Link           | `[text](https://example.com)`                                           |
