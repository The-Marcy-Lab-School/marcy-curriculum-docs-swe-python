# Local Environment Setup - Mac

Today, we'll be setting up our local development environment for Mac. Click here for the [Windows instructions](local-environment-setup-windows.md).

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Set up local `development` directory](#set-up-local-development-directory)
- [Download VS Code](#download-vs-code)
  - [Familiarize yourself with VS Code](#familiarize-yourself-with-vs-code)
  - [Configure VS Code](#configure-vs-code)
  - [Download Useful Extensions](#download-useful-extensions)
- [Install Python](#install-python)
  - [Write your first Python program](#write-your-first-python-program)

## Set up local `development` directory

Now, let's get familiar with the **Terminal**. It's an application that you can use to manage your file system. At first, it may seem slow but you'll quickly learn how to use it and see how powerful it can be!

First, open the Terminal application. You can do this via Spotlight Search (<kbd>Command+Spacebar</kbd>) and search for "Terminal". Once it opens, type in the `ls` command and hit <kbd>Enter</kbd>

![The list command shows the directories at the root (~) of your file system](../.gitbook/assets/terminal-list.png)

Then, using your Terminal, create a folder structure where you can put all your Marcy Lab code by entering these commands, one at a time:

```sh
# list the contents of your "working directory" (where your terminal is working in your file system)
ls

# make a new directory called "development"
mkdir development

# change the working directory to "development"
cd development

# make directories with the names mod-0, mod-1, and mod-2
mkdir mod-{0..2}

# list the contents of "development". You should see the mod-0, mod-1, and mod-2 folders
ls
```

Pretty cool right? The Terminal is a very powerful tool in the hands of an expert.

## Download VS Code

While the Terminal can be used to manage files, we'll use VS Code to actually write code.

VS Code is a code editor we can use to edit files and write programs. First, make sure that you don't already have VS Code installed.

- Search for Visual Studio Code on your computer. You can so this via Spotlight Search (Command+Space) and type "Visual Studio Code":

![VS Code Spotlight](../.gitbook/assets/vs-code-spotlight.png)

If it shows up, then you can skip to the next section, [Familiarize yourself with VS Code](local-environment-setup-mac.md#familiarize-yourself-with-vs-code).

If it does not show up, follow these steps to install VS Code:

1. [Download VS Code for Mac](https://code.visualstudio.com/download)
2. Open up "Finder", navigate to your Downloads folder, click the `.zip` file, then drag Visual Studio Code to your Application folder.

![download](../.gitbook/assets/download.png)

### Familiarize yourself with VS Code

Now, let's get to know the VS Code layout!

- Your directories and files are in the left panel. You should see your `development` folder as the root with your sub-directories listed inside.
- VS Code has an integrated Terminal application that you can use by selecting **Terminal > New Terminal** from the top menu bar.
- The VS Code Terminal is _exactly_ the same as your Mac "Terminal". Anything you do in Terminal you can do here as well.

![VS Code on MacOS](../.gitbook/assets/vscode.png)

### Configure VS Code

First, we'll add the very helpful `code` command which can quickly open up a VS Code window from the Terminal.

1. Open VS Code and open the Command Palette by typing Shift+Command+P (⇧⌘P). Then type 'shell command' to find the Shell Command: Install 'code' command in PATH command. Click it to install.

   ![shell](../.gitbook/assets/shell.png)

2. If the Shell Command install was successful, you should see this pop-up in the bottom-right of your VS Code:

   ![installed](../.gitbook/assets/installed.png)

3. Test out that this worked by opening up your Terminal application
   - Enter `cd ~` to switch to the root folder (\~).
   - Enter `ls` to see the directories at the root.
   - Enter `code development` to open a new VS Code window rooted in the `~/development/` folder

   Remember this `code` command in the future. It can be used to open up a VS Code window in whatever folder you choose!

4. Go to your settings (click on the cog in the bottom-left corner) and search for "save".
   - Set **Files: Auto Save** to **onFocusChange**
   - CHECK the checkbox for **Editor: Format On Save**

   ![Turn on Auto Save and Format on Save.](../.gitbook/assets/vs-code-save-settings.png)

5. Stay in your settings and search for "compact folders":
   - UNCHECK the checkbox for **Explorer: Compact Folders**.

   ![Turn off Compact Folders](../.gitbook/assets/vs-code-compact-folders.png)

6. Finally, in your settings search for "AI Features"
   - CHECK the checkbox for **Chat: Disable AI Features**.

   ![Disable AI Features](../.gitbook/assets/vs-code-disable-ai-features.png)

   **This does not mean you are working without AI.** It means the AI you use will be something you deliberately open and ask, rather than something that finishes your sentences while you type.

   Inline suggestions complete your code as you go. There is never a moment where you say what you want — the editor infers it from what you have typed so far and offers you the next few lines. That is the opposite of how you will be taught to work here, which begins with writing down what you are building before anything gets generated. It also leaves no trace: suggested code and code you wrote yourself end up interleaved in the same file with no record of which was which, so afterward you genuinely cannot say which parts were yours. Being able to say which parts were yours is most of what this program certifies.

   There is a second reason, and it is about learning rather than accountability. A suggestion appears at exactly the moment you pause to think — and that pause is where the learning happens. A tool you have to go and ask does not interrupt it. A tool that fills it in by default does.

   You will turn this back on later in the program, deliberately, once you are working from written specifications. At that point a completion is filling in something you already decided, which is a different act. Until then, use a chat window as much as you want; the [AI Policy](../guidelines-and-policies/ai-policy.md) explains exactly what that looks like.

### Download Useful Extensions

VS Code includes a number of features out-of-the-box but it also allows you to customize your experience with **extensions**. VS Code extensions let you add languages, debuggers, and tools to your installation to support your development workflow.

You can browse and install extensions from within VS Code. Bring up the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of VS Code.

![VS Code Extensions Icon](https://code.visualstudio.com/assets/docs/configure/extensions/extension-marketplace/extensions-view-icon.png)

From the Extensions view you can search for and brose popular extensions.

![Browse the VS Code Extensions Marketplace](https://code.visualstudio.com/assets/docs/configure/extensions/extension-marketplace/extensions-popular.png)

Start by installing these extensions:

- **Code Spell Checker** — spelling checker for source code
- **Error Lens** — highlights errors directly in your code
- **Python** — Python language support from Microsoft
- **Ruff** — the formatter and linter we use for Python

## Install Python

Everyone in your cohort installs Python 3.14. This matters more than it sounds: when something breaks, it breaks the same way for you, for your classmates, and for your instructor, which is the difference between a five-minute fix and an afternoon. The last number in the version may differ slightly between Mac and Windows machines — `3.14.7` and `3.14.3` are both fine. What matters is the `3.14`.

1. Go to the [Python macOS downloads page](https://www.python.org/downloads/macos/) and click the large **Download Python** button at the top of the page. You should get Python 3.14.7.

2. Open the `.pkg` file from your Downloads folder and follow the installer, accepting the defaults.

3. Close your Terminal, open a new one, and confirm the install:

   ```sh
   python3 --version
   ```

   You should see a version beginning with `Python 3.14`.

{% hint style="info" %}
**If it prints anything other than `3.14`**, stop here and check with an instructor before going further. There are two ways this happens, and they have different fixes.

If it prints an **older** version — `Python 3.12`, say — you have another copy of Python already installed that your Terminal is finding first. Run `which -a python3` to list all of them and show an instructor the output.

If it prints a **newer** version, the download button has moved on to a release published after this guide was written. Go back to the [downloads page](https://www.python.org/downloads/macos/), scroll past the button to the list of stable releases, and download the most recent **3.14** version instead.
{% endhint %}

### Write your first Python program

Now, in your VS Code Terminal, enter these commands:

```sh
# See the contents of the "working directory"
ls

# Change directories to the "mod-0" directory
cd mod-0

# Create a new Python file called script.py
touch script.py
```

You should now see the file in your VS Code File Explorer panel on the left side of the screen. Then, do the following:

1. Click on `script.py` to open it.
2. Type in the code:

   ```py
   print("Hello World!")
   ```

3. Save the file by pressing `Ctrl+S` or by going to File > Save.
4. Run the command in your Terminal:

   ```sh
   python3 script.py
   ```

{% hint style="info" %}
**A note on `python` versus `python3`.** On macOS, typing `python` on its own usually produces `command not found`. The command you want is always `python3`, with the 3 on the end.

This catches nearly every cohort in week one, and the reason is historical: `python` used to mean Python 2, a version of the language that is no longer used and is not installed on your machine. Rather than let `python` mean two different things on different computers, macOS leaves it undefined. Type `python3` every time and the question never comes up.
{% endhint %}
