# 1. Command Line Interfaces

At the end of the day, a program is just a text file on a computer. So, before we begin programming, we need to learn how programmers create, organize, and otherwise manage the files on their computers.

In this lesson, we'll learn about the Terminal, a program for interacting with a computer's files and executing programs through a command line interface (CLI).

You will be able to…

- Understand what a command line interface (CLI) is.
- Compare and Contrast CLIs and Graphical User Interfaces (GUIs)
- Navigate your local file tree
- Create, copy, delete, and move files and directories
- How to run a Python program using your CLI
- Explain what an "argument" is

**Table of Contents:**

- [Key Terms](#key-terms)
- [Common CLI Commands](#common-cli-commands)
- [The File Tree](#the-file-tree)
  - [Applications for Viewing the File Tree (CLI vs. GUI)](#applications-for-viewing-the-file-tree-cli-vs-gui)
  - [Using the Terminal in VS Code](#using-the-terminal-in-vs-code)
- [Essential Commands](#essential-commands)
  - [Looking at the Working Directory with `pwd` and `ls`](#looking-at-the-working-directory-with-pwd-and-ls)
  - [Navigating Between Directories with `cd`](#navigating-between-directories-with-cd)
    - [Be Careful when using the `cd` command!](#be-careful-when-using-the-cd-command)
  - [Making Files and Directories with `mkdir` and `touch`](#making-files-and-directories-with-mkdir-and-touch)
  - [Executing Python files with `python3`](#executing-python-files-with-python3)
    - [Terminating a Program with `Control+C`](#terminating-a-program-with-controlc)
- [Additional Commands](#additional-commands)
  - [Unfinished Double Quotes, `echo`, and `>>`](#unfinished-double-quotes-echo-and-)
  - [The `cat` Command and Combining Commands with `&&`](#the-cat-command-and-combining-commands-with-)
  - [Removing, Renaming, Moving, and Copying](#removing-renaming-moving-and-copying)
- [Challenges](#challenges)

## Key Terms

You will find a section with key terms at the top of every chapter. These are the definitions that you will be expected to commit to memory but that will take time and practice. When you first read a chapter, skim through these terms and make note of the ones that you are confused about. Then, return to these terms and see which ones you can easily recall and which ones you need to practice.

- **Terminal** — A program for interacting with a computer's files and executing programs through a command line interface.
- **Command Line Interface** — a type of user interface (UI) that let's a users perform actions by entering text-based commands.
- **Graphical User Interface** — a type of user interface that uses visual elements such as icons, buttons, windows, and dialog boxes, allowing users to perform actions such as clicking, drag-and-drop, and more.
- **Directory** — Another term for a "folder" in your computer that contains references to files or possibly other directories.
- **Working Directory** — The directory where your commands will be executed.
- **Command** - A single action to be performed on your computer. Examples include creating a new file, listing the contents of the current directory, navigating to a different directory, or executing a program.
- **Argument** — An additional piece of information provided to a command to change the command's behavior.
- **Python** — The programming language you will be writing in for the rest of this program.
- **Interpreter** — The program that reads a Python file and executes it, one statement at a time.
- **`python3`** — The command that runs the Python interpreter on a file.

## Common CLI Commands

{% hint style="info" %}
**Note:** In the commands below, argument placeholders will be written like this: `[argument]`. When using these commands, replace the `[argument]` with your desired inputs, making sure to leave out the `[]` as well.
{% endhint %}

```sh
# Run a given `.py` file using the Python interpreter.
python3 [filename.py]

# Terminate the currently running program
Control + C

# Print the working directory, a.k.a where your terminal navigation currently is located.
pwd

# Prints ("lists") the contents of the working directory
ls

# Change directories to the given subdirectory
cd [subdirectory]

# Change directories to the parent of the working directory
cd ../

# Make a new directory with the given name.
mkdir [subdirectory]

# Make a new file with the given name
touch [filename]

# Move a file to the given directory
cp [file] [dest]
```

## The File Tree

The files and folders in your computer are organized in a tree-like structure called the **File Tree**.

![](../.gitbook/assets/file-structure.png)

We refer to each folder in the file tree as a **directory**. The **root directory** is the top-most folder that contains all other **sub-directories**.

**<details><summary>Q: What are the ways that the file tree is tree-like?</summary>**

The root is like the trunk of the tree and each sub-directory is a branch that can have more branches.

</details>

### Applications for Viewing the File Tree (CLI vs. GUI)

Most operating systems have an application that lets you view the device's file tree. For example, on MacOS there is Finder and on Windows there is Explorer:

![The finder program](../.gitbook/assets/finder.png)

These applications allow you to manage files through a **graphical user interface (GUI)** — a user interface with buttons and icons that let you do things like click and drag-and-drop.

These GUIs are examples of an "abstraction"—an interface that hides complexity and technical detail in favor of ease-of-use—and GUIs present a tradeoff:

- GUIs are easy to use and easy to learn for beginners
- What you can do with GUIs is limited to how the designers wanted you to use them

When we want more fine-tuned control over how we interact with our computer's files, we can turn to a **command line interface (CLI)**, often called the **Terminal**. The Terminal is a program for interacting with a computer's files by executing typed-in commands:

![The Terminal program](../.gitbook/assets/1-cli-terminal.png)

In the screenshot above, you can see this user entering commands:

```sh
pwd
ls
mkdir unit-5
ls
ls unit-0
cd unit-0
touch bye.txt hey.txt
ls
echo "hello world"
echo "hello world" >> output.txt
ls && cat output.txt
rm hey.txt && ls
mv bye.txt goodbye.txt && ls
```

Note that some commands like `pwd` can be entered on their own. Other commands like `mkdir` may use inputs called **arguments**. Some commands like `ls` can be used on their own or with arguments.

**<details><summary>Q: Why use The Terminal?? It would be wayyy faster to do this in the Finder</summary>**

For this particular task it might be faster to use a GUI file manager like Finder, however there are many tasks where a CLI like the Terminal can outpace a GUI like Finder.

For example, try this command below to create 8 folders at once!

```sh
mkdir mod-{0..7}
```

In addition, there are some things that Finder simply can't do, like execute files with code.

</details>

### Using the Terminal in VS Code

While you can use the Terminal application that comes with your laptop, it is often just as convenient to use the one that comes built into your VS Code code editor.

To open up the Terminal panel, go to **File** > **Terminal** and it should show up at the bottom:

![Use the keyboard shortcut Control+` to open/close the Terminal](../.gitbook/assets/vscode-terminal.png)

## Essential Commands

Let's go through some of the most important and commonly used commands.

### Looking at the Working Directory with `pwd` and `ls`

In the terminal, you can only interact with one directory at a time, the **working directory**.

Think of it as the "you are here" icon in a map.

![The working directory is your current location in your file tree.](../.gitbook/assets/you-are-here.png)

The `pwd` command prints the full file path to the working directory while the `ls` command prints the contents of the working directory:

![](../.gitbook/assets/ls.png)

{% hint style="info" %}
**Note:** In computing, all actions that interact with data fall into one of the four categories called CRUD: **c**reating, **r**eading, **u**pdating, or **d**eleting data.

Which of these actions do you think `pwd` and `ls` are?
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Write down your answers to both of these before you run anything.

```sh
ls ..
pwd
```

1. What will `ls ..` print?
2. After running it, what will `pwd` print?

<details><summary>What actually happens</summary>

`ls ..` prints the contents of the **parent** directory — the folder that contains the one you are currently in.

`pwd` then prints exactly what it printed before. You did not move.

This is the distinction worth taking away: `ls` accepts a directory as an argument and _reports on_ it, while `cd` accepts a directory and _moves you into_ it. A command that looks at somewhere else does not put you there. Beginners frequently expect `ls ..` to have relocated them, and then get lost.

</details>
{% endhint %}

### Navigating Between Directories with `cd`

The `cd [directory]` command allows you to move to another directory in the file system. However, unlike the previous commands, it requires an **argument**.

An **argument** is an additional piece of information that changes that behavior of a given command. For the `cd` command, we have to also provide a destination.

{% hint style="info" %}
Use the Tab key to autocomplete commands and filenames! Just start typing and hit Tab to autocomplete.
{% endhint %}

For example, suppose we were located in the `/Users` directory inside the following file system:

![The file tree](../.gitbook/assets/file-structure.png)

I could navigate to "down" to the `/Users/smith` directory with the command:

```
cd smith
```

You can also extend the directory provided with a `/` to quickly navigate to directories within directories. For example, if I were located in the `/Users` directory, I could navigate to the `/Users/smith/Documents` directory in one command:

```
cd smith/Documents
```

To navigate back "up" to the "parent" directory, you can use the special directory name `..` which always refers to the parent directory of the working directory.

For example, if I were in the directory `/Users/smith/Documents` and wanted to go back up to the `/Users/smith` directory, I could enter the command:

```
cd ..
```

If I had wanted to go up two levels from `/Users/smith/Documents` to `/Users`, I can again use `/` to extend the provided directory name:

```
cd ../..
```

**<details><summary>Suppose I were located in the `/Users/smith/Documents` directory, how could I navigate to the `/Users/jones/Desktop` directory in one `cd` command?</summary>**

```
cd ../../jones/Desktop
```

</details>

#### Be Careful when using the `cd` command!

Using the `cd` command on its own will send you to the root of your entire file system (`~/`). This is the equivalent of using the command:

```sh
cd ~
```

### Making Files and Directories with `mkdir` and `touch`

`mkdir [dir_name]` creates a new directory in the working directory

`touch [file_name]` creates a new file in the working directory. Make sure to include the file extension!

You can also create multiple files/directories at once by listing multiple file/directory names:

```sh
touch file1.txt file2.txt
mkdir dir1 dir2 dir3
```

### Executing Python files with `python3`

A Python program is any file with a `.py` extension, like `hello.py`

The code can be as simple as `print("Hello World")`

To run the program, use the command `python3 hello.py`

{% hint style="info" %}
**Why `python3` and not `python`?**

Typing `python` on its own will most likely tell you `command not found`. The command always has the 3 on the end.

The reason is historical. `python` used to mean Python 2, an older version of the language that is no longer used and that you will never write. Rather than let one word mean two different languages on two different computers, both macOS and Ubuntu leave `python` undefined and give you `python3` instead.
{% endhint %}

{% hint style="warning" %}
**Predict, then run.** Throughout this curriculum you will find boxes like this one. Each asks you to write down what you expect to happen _before_ you run anything.

Do not skip the writing-down part. Predicting silently lets you quietly adjust your prediction once you see the answer, which teaches you nothing. Writing it down first is what makes the gap between your expectation and reality concrete.

Make a file called `broken.py` containing these two lines, then predict what `python3 broken.py` will print:

```python
print("first line")
print("second line"
```

<details><summary>What actually happens</summary>

Nothing is printed. Not even `first line`.

Python reads the _entire_ file and checks that it is valid before it executes any of it. The second `print` is missing its closing parenthesis, so the whole file is rejected and you get a `SyntaxError` instead of any output.

This is worth knowing early: if you expected to see `first line` before the error, your mental model was that Python runs a file line by line from the top. It does execute line by line — but only after it has read and accepted the whole file first.

</details>
{% endhint %}

#### Terminating a Program with `Control+C`

Many programs will end ("terminate") on their own when each statement has been executed.

Other programs can run forever, requiring us to stop them ourselves. For example, when we use the command `python3` on its own — with no file after it — it will start the **Python REPL (Read, Evaluate, Print Loop)** program which just waits for Python input, executes it, and then prints the result:

![The Python REPL is useful for testing out expressions.](../.gitbook/assets/1-python-repl-expressions.png)

To terminate the program, use the keyboard shortcut `Control+C` (you may need to cancel twice). You can also leave the Python REPL by entering `exit()`.

## Additional Commands

### Unfinished Double Quotes, `echo`, and `>>`

Another common occurrence is an unfinished string. You can test this with the `echo` command which will print a given string straight to the terminal.

![An unfinished double quote will be produce dquote> in the Terminal, waiting for you to finish the string.](../.gitbook/assets/1-cli-echo-unfinished-dquote.png)

You can also use the output from an `echo` command and send the output into another file using the `>>` append operator.

For example, this command will take the text `"hello world"` and append it to the file `output.txt` (it will create `output.txt` if it doesn't exist)

```sh
echo "hello world" >> output.txt
```

{% hint style="warning" %}
**Predict, then run.** Write down what you expect the terminal to print for each of these three commands, in order.

```sh
echo "hello world"
echo "hello world" >> output.txt
echo "hello world" >> output.txt
```

Then run `cat output.txt` and predict that too.

<details><summary>What actually happens</summary>

The first command prints `hello world` to the terminal.

The second and third commands print **nothing at all**. The terminal stays silent and you get your prompt back.

`cat output.txt` then prints `hello world` twice, on two separate lines.

Two things are going on. First, `>>` _redirects_ the output — the text that would have gone to your screen goes into the file instead, so it cannot do both. Second, `>>` **appends**, meaning it adds to the end of whatever the file already contains rather than replacing it. That is why running the same command twice gives you two lines rather than one.

A command that prints nothing has not necessarily done nothing. Silence in a terminal usually means "it worked."

</details>
{% endhint %}

### The `cat` Command and Combining Commands with `&&`

The `cat` command is used to read the contents of a given file.

You can combine any two commands with the `&&` operator.

```sh
ls && cat output.txt
```

For example, the command above lists the contents of the current working directory and print the contents of `output.txt`

{% hint style="warning" %}
**Predict, then run.** Assume there is no directory called `no-such-folder`. What will this print?

```sh
cd no-such-folder && echo "the second command ran"
```

<details><summary>What actually happens</summary>

You get an error from `cd` saying that no such file or directory exists, and then **nothing else**. The message `the second command ran` never appears.

`&&` does not mean "run both of these." It means "run the first one, and _then, only if it succeeded_, run the second one." Every command reports back whether it succeeded or failed, and `&&` reads that report before deciding whether to continue.

This matters more than it looks. When you chain commands together (e.g. installing something and then running it, or saving your work and then uploading it) `&&` is what stops the second step from running on top of a first step that failed.

</details>
{% endhint %}

### Removing, Renaming, Moving, and Copying

`rm [file_name]` removes a file from the working directory

`rm -r [directory_name]` removes a directory and all of its contents from the working directory. `-r` stands for "recursive".

`mv [file_name] [new_file_name]` renames a file in the working directory or allows you to move the file to another directory.

`cp [file_name] [dir_name]` copies a file into a directory.

## Challenges

Check out these [awesome challenges](https://github.com/mssalvatore/command-line-challenges) for additional practice. A lot of these challenges go way beyond what we've learned in this lesson and will push you to research and learn on your own!

We're using Linux commands so whenever you are researching a topic, add "Linux" to the end of your search so that you get appropriate results! For example, for the first challenge you may search **"how to unzip .tar.gz file linux"**.

Challenges 1-19 are the basics of what you'll want to know for this course.

Challenges 20 you should skip. It involves executing a file that we can't see the contents of.

Challenges 21-50 are more advanced.
