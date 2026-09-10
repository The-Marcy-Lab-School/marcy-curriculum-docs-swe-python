# Local Environment Setup - Windows

Today, we'll be setting up our local development environment for Windows 10. For the Mac instructions, see [here](local-environment-setup-mac.md).

## Table of Contents

- [Table of Contents](#table-of-contents)
- [WSL](#wsl)
  - [Enable WSL](#enable-wsl)
  - [Download WSL](#download-wsl)
    - [Upgrade from WSL 1 to WSL 2](#upgrade-from-wsl-1-to-wsl-2)
- [Visual Studio Code, Python, and Your Local development Environment](#visual-studio-code-python-and-your-local-development-environment)
  - [Download VSCode for Windows](#download-vscode-for-windows)
  - [Familiarize yourself with VS Code](#familiarize-yourself-with-vs-code)
  - [Configure VS Code](#configure-vs-code)
  - [Download Useful Extensions](#download-useful-extensions)
  - [Install Python](#install-python)
  - [Set up local development directory](#set-up-local-development-directory)
  - [Write your first Python program](#write-your-first-python-program)

## WSL

Windows Subsystem for Linux (WSL) is a Linux distribution that allows you to run Windows applications in a Linux environment, the environment used by most software developers.

### Enable WSL

Within a few easy steps, you can get this done. Press **Windows Key + S** open up the search bar, and type “Windows Features.”

![windows](../.gitbook/assets/windowfeature.webp)

Click on the “Turn Windows features on or off”

![wsl](../.gitbook/assets/wsl.webp)

Select **Windows Subsystem for Linux** and click OK. (This will require a restart of Windows to get things installed).

### Download WSL

After your computer starts up again, open the Windows Search, find the **Windows PowerShell** application, and **Run as Administrator**.

Type the following commands in the **Windows PowerShell** application:

```powershell
wsl --update
wsl --install
```

This will update and install WSL on your computer!

When WSL finishes installing, run this command to check your version (take note of the value under `NAME` and `VERSION`):

```powershell
wsl -l -v
```

If it is version 2, you're good to go! You may close Powershell.

If it says version 1, follow these steps below.

#### Upgrade from WSL 1 to WSL 2

> Note: These instructions are based on Microsoft's documentation found [here](https://learn.microsoft.com/en-us/windows/wsl/install#upgrade-version-from-wsl-1-to-wsl-2)

If the version is 1, you can change it to version 2 with a command like `wsl --set-version [NAME] [VERSION]`.

- For example, to switch to `Ubuntu` version 2, you would use the command `wsl --set-version Ubuntu 2`

You should see "Conversion in progress, this may take a few minutes (it can take as long as 30 minutes or more)

- If you see a warning telling you to install/update the WSL 2 kernel, you may be asked to visit https://aka.ms/wsl2kernel. Do so and install the WSL Linux kernel update package for x64 machines.
- If you see "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS." do the following:
  - In the Windows search bar, look for "Turn Windows features on or off"
  - Scroll down and select "Virtual Machine Platform" and then click "Ok"
  - Reboot your computer.
  - Re-open Powershell, check the version with `wsl -l -v` and restart these instructions.

## Visual Studio Code, Python, and Your Local development Environment

Visual Studio Code is the standard IDE used by developers.

### Download VSCode for Windows

Visit [this web site](https://code.visualstudio.com/) and download VS Code.

- Download the latest build and install it in your PC.
- Now open VS Code and press **Ctrl + Shift + P** to open the **Command Palette** and search "WSL".
- Then, select **WSL: Connect to WSL in New Window**. This should open a new VS Code window running using WSL!

VS Code should automatically detect your WSL installation and suggest an extension.

![extension](../.gitbook/assets/extention.webp)

If not, you can click on the “Extensions” tab in VS Code. Search for "Remote - WSL" and install (I will have a penguin icon).

![vscode](../.gitbook/assets/vscode.webp)

Visual Studio Code will open and will indicate its successfully connected to the server at WSL.

![](../.gitbook/assets/wslubuntu.webp)

When you open the terminal from VS Code you will see the bash terminal at WSL.

![](../.gitbook/assets/terminalubuntu.webp)

You should pin Ubuntu Terminal and VS Code to the taskbar since you'll be using them a lot.

![taskbar](../.gitbook/assets/taskbar.png)

### Familiarize yourself with VS Code

Now, let's get to know the VS Code layout!

- Your directories and files are in the left panel. You should see your `development` folder as the root with your sub-directories listed inside.
- VS Code has an integrated Terminal application that you can use by selecting **Terminal > New Terminal** from the top menu bar.
- The VS Code Terminal is _exactly_ the same as your Mac "Terminal". Anything you do in Terminal you can do here as well.

![VS Code on MacOS](../.gitbook/assets/vscode.png)

### Configure VS Code

1.  Go to your settings (click on the cog in the bottom-left corner) and search for "save".
    - Set **Files: Auto Save** to **onFocusChange**
    - CHECK the checkbox for **Editor: Format On Save**

    ![Turn on Auto Save and Format on Save.](../.gitbook/assets/vs-code-save-settings.png)

2.  Stay in your settings and search for "compact folders":
    - UNCHECK the checkbox for **Explorer: Compact Folders**.

    ![Turn off Compact Folders](../.gitbook/assets/vs-code-compact-folders.png)

3.  Finally, in your settings search for "AI Features"
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

### Install Python

Everyone in your cohort installs Python 3.14. This matters more than it sounds: when something breaks, it breaks the same way for you, for your classmates, and for your instructor, which is the difference between a five-minute fix and an afternoon. The last number in the version may differ slightly between Mac and Windows machines — `3.14.7` and `3.14.3` are both fine. What matters is the `3.14`.

Run all of these commands in the **Ubuntu terminal**, not in PowerShell.

1.  First, check which version of Ubuntu you have:

    ```bash
    lsb_release -d
    ```

    You need **Ubuntu 26.04** or newer. If you see an older version, stop here and tell your instructor. Older versions of Ubuntu install an older version of Python, and you would spend the quarter on a different version from everyone else without knowing it.

2.  Update the list of available software and upgrade what is already installed:

    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

    This asks for the Ubuntu password you chose when WSL first started, and it can take several minutes. `apt` is Ubuntu's package manager — the program that installs and updates software on this system.

3.  Install Python, along with two tools that come with it:

    ```bash
    sudo apt install python3 python3-pip python3-venv -y
    ```

    - `python3` is the Python interpreter itself, the program that runs your code.
    - `python3-pip` is `pip`, the tool for installing Python packages written by other people.
    - `python3-venv` is `venv`, the tool for keeping each project's packages separate from every other project's. You will use both of these in Mod 1.

4.  Confirm the install:

    ```bash
    python3 --version
    ```

    You should see `Python 3.14.3` or another `3.14` version.

You are now set up with Python!

### Set up local development directory

Every time you open your Terminal, you'll be in the home directory. Run `pwd` to see the current path. You'll see `home/your-user-name`.

![home](../.gitbook/assets/home.png)

Using your Terminal, create a folder structure where you can put all your Marcy Lab code by entering these commands, one at a time:

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

{% hint style="info" %}
💡 Lines starting with `#` are comments and are ignored by your Terminal
{% endhint %}

Next, type the command `code .` into your terminal and it will open VS Code at the current directory (your "development" folder). You'll use this command a lot so remember it!

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
**A note on `python` versus `python3`.** On Ubuntu, typing `python` on its own usually produces `command not found`. The command you want is always `python3`, with the 3 on the end.

This catches nearly every cohort in week one, and the reason is historical: `python` used to mean Python 2, a version of the language that is no longer used and is not installed here. Rather than let `python` mean two different things on different machines, Ubuntu leaves it undefined. Type `python3` every time and the question never comes up.
{% endhint %}
