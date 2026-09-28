# Mod 0 Learning Objectives and Key Terms

One entry per session, preceded by the orientation setup that happens before day 1. Key terms are copied from each chapter's **Key Terms** section by `scripts/sync-key-terms.py`, so edit them in the chapter and rerun the script rather than editing them here. Learning objectives are written so that each one could be checked with a short task. Each list is split in two. _In the session_ names the three or four objectives the 90-minute lecture is responsible for: introduced, practiced, and checked before it ends. _By the end of the module_ names the rest, which the chapter's reading and the assignments carry.

## Before Day 1: Environment Setup and Virtual Environments

**Key terms**

None listed. Setup runs in orientation rather than as a Technical Lecture session, from the [Mac](../environment-setup/local-environment-setup-mac.md) and [Windows](../environment-setup/local-environment-setup-windows.md) setup documents, which have no Key Terms section. Virtual environments are named in the orientation agenda, but neither setup document teaches them; the Windows document installs `venv` and says it will be used in Mod 1, where chapter 7 teaches it.

**You will be able to…**

_In orientation:_

- Open VS Code, open a folder in it, and open its built-in Terminal.
- Confirm from the Terminal that `python3 --version` reports a 3.14 release, and know who to ask if it does not.
- Create a `.py` file, put a `print()` in it, and run it with `python3`.
- Keep all course work inside one `development` directory, organized by module.

_Before day 1:_

- Explain what the Python interpreter is and what the `python3` command starts.
- Install and use the VS Code extensions the course relies on.
- Recover from the setup document's "before you move on" checklist without help.

## 1. Command Line Interfaces

<!-- key-terms-from: 1-clis.md -->

**Key terms**

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

**You will be able to…**

_In the session:_

- Explain what a command line interface is and when it beats a graphical one.
- Report where you are with `pwd`, see what is there with `ls`, and move with `cd`, including up with `..` and several levels at once.
- Create files and directories with `touch` and `mkdir`, and remove, rename, move, and copy them with `rm`, `mv`, and `cp`.
- Run a Python file with `python3` and stop a running program with `Control+C`.

_By the end of the module:_

- Explain what an argument is and give an example of a command with and without one.
- Predict what `ls ..` prints and that `pwd` afterward is unchanged, and explain the difference between a command that reports on a directory and one that moves into it.
- Predict that a file with a syntax error prints nothing at all, and explain why the interpreter reads the whole file first.
- Use `echo` and `>>` to append to a file, and explain why a command that prints nothing has usually worked.
- Predict what `cd no-such-folder && echo "ran"` prints, and explain what `&&` waits for.
- Open the Python REPL, evaluate an expression, and leave it.

## 2. Git and GitHub

<!-- key-terms-from: 2-git-github.md -->

**Key terms**

- **Repository (or just "repo")** — a centralized location where files are stored and managed. Any folder can be considered a repository.
- **Git** — A "version control system" that allows us to manage the history of changes made to a repo through commits.
- **Commit** — A "snapshot" of the changes made to a repo. A commit is typically created when a key milestone is reached in a project (e.g. a feature is completed).
- **Staging Area** — A place to temporarily store changed files to include in the next commit.
- **Github** — An online host of git repositories with tools for managing git projects and features for collaboration.
- **Local Repository** — A repository stored on a developers computer.
- **Remote Repository** — A repository stored online on a service like GitHub.
- **Clone** — Copy a remote repo's files and commit history and store them locally (creates a local repository)
- **Push** — Send a local repo's commit history to a remote repo to be synchronized.

**Important Git commands**

{% hint style="info" %}
**Note:** In the commands below, argument placeholders will be written like this: `[argument]`. When using these commands, replace the `[argument]` with your desired inputs, making sure to leave out the `[]` as well.
{% endhint %}

```sh
# add git to the current repo
git init
# check the status of changed files in the repo
git status
# add the given file to the staging area
git add [filename]
# add all changed files to the staging area
git add -A
# creates a new commit from the staged files
git commit -m "[commit message]"
# upload local commits to the remote (GitHub)
git push
# download a git repository from the remote (GitHub)
git clone
```

**You will be able to…**

_In the session:_

- Explain what a repository, a commit, and the staging area are, using the camera analogy, and tell Git apart from GitHub.
- Turn a folder into a repository with `git init` and read `git status` to say which files are changed, staged, or untracked.
- Stage and commit with `git add` and `git commit -m`, and read the history with `git log`.
- Create a repository on GitHub, clone it with `git clone`, commit locally, and upload with `git push`.

_By the end of the module:_

- Distinguish a local repository from a remote one and say which command moves commits in each direction.
- Write a commit message that says what changed and why, at a milestone rather than after every keystroke.
- Explain the difference between `git add [filename]` and `git add -A`, and choose the right one.

## 3. Git Pulling and Merging

<!-- key-terms-from: 3-git-pulling-merging.md -->

**Key terms**

- **Pull** — to download changes from a remote repository
- **Merge** - to combine two or more branches into one
- **Merge Conflict** — a situation in which two or more branches need to be merged but have modified the same lines of code, causing the merge to fail. This happens all the time and can be resolved through the Github GUI or the CLI.

**Important Git commands**

{% hint style="info" %}
**Note:** In the commands below, argument placeholders will be written like this: `[argument]`. When using these commands, replace the `[argument]` with your desired inputs, making sure to leave out the `[]` as well.
{% endhint %}

```sh
git pull # download changes from a remote repository
```

**You will be able to…**

_In the session:_

- Add a collaborator to a GitHub repository and clone a repository you were added to.
- Download a collaborator's commits with `git pull` and explain why a push is rejected when the remote has commits you do not have.
- Recognize a merge conflict from Git's output, open the file, read the conflict markers, and say which lines came from where.
- Resolve a merge conflict by editing the file, removing the markers, committing, and pushing.

_By the end of the module:_

- Explain what a merge is and why two people editing the same lines produces a conflict while editing different lines does not.
- Follow the pull-before-push habit so that conflicts are found locally rather than on GitHub.

## 4. Git Branching and Pull Requests

<!-- key-terms-from: 4-git-branching.md -->

**Key terms**

* **Main Branch** — The main branch of a repository. Whenever anyone visits a repository on GitHub or clones it down, this is what they will see.
* **Feature Branch** — a copy of a repository at a point in time that allows developers to work on a feature without impacting the rest of the project.
* **Merge** - to combine the commit history of two or more branches into one.
* **Pull Request** — a request for another developer to pull down your branch and review your code. If they approve the changes, they will merge your branch into the main branch!
* **Fork** — a copy of a repository that is disconnected from the main repository. Typically they include the entire commit history of the main repository at the time the fork was created.

**Important Git commands**

{% hint style="info" %}
**Note:** In the commands below, argument placeholders will be written like this: `[argument]`. When using these commands, replace the `[argument]` with your desired inputs, making sure to leave out the `[]` as well.
{% endhint %}

```sh
git branch # see all branches in the local repository
git branch [branch_name] # create a new branch
git checkout [branch_name] # switch to a branch
git checkout -B [branch_name] # create a new branch and switch to it
git merge [branch_name] # merge a branch into the current branch
git branch -D [branch_name] # delete a branch 
```

**You will be able to…**

_In the session:_

- Explain what a branch is, why the main branch is kept stable, and what a feature branch is for.
- Create a branch, switch to it, and list branches with `git branch` and `git checkout`.
- Commit on a feature branch, push it, and open a pull request on GitHub with a description a reviewer can act on.
- Review and merge a pull request on GitHub, then pull the merged main branch locally.

_By the end of the module:_

- Merge one branch into another locally with `git merge` and delete a finished branch.
- Resolve a merge conflict through the GitHub interface as well as from the command line.
- Fork a repository and explain how a fork differs from a branch and from a clone.
- Describe how a team of several people uses branches and pull requests so that main always works.
