# Prose Review: Mod 0 and Mod 1

This review checks the explanatory prose of every published lesson in Mod 0 and Mod 1 against the writing rules in the global `CLAUDE.md`, in particular "Name the subject and the unit" and "Explain in the order the reader needs". It covers the four Mod 0 chapters, the thirteen Mod 1 chapters, the case study, the project, and the regex reading. Cheat sheets, overviews, and the learning objectives documents were left out because they are lists and references rather than explanations.

Seven reviewers each read a group of chapters and reported at most twelve findings per file, ranked by how much each passage would cost a fellow. Each finding gives the location, the passage, the rules it breaks, what a fellow would get wrong, and a proposed rewrite. The reviewers report that they ran every behavior claim in their rewrites with Python 3.12.4, pytest, zsh, or Git before writing it down. I have not re-run those checks myself, so each rewrite should be checked again when it is applied. No lesson file has been changed.

**Status:** the factual errors the reviewers found were fixed and checked by running the code on 2026-10-01. The clarity findings for Mod 1 chapters 1.1 to 1.9 were applied on 2026-10-07. The log at the end of this document records how Ben edited each batch of applied rewrites before committing them.

The full reports follow the summary below. The summary has two parts: the patterns that recur across chapters, and the decisions that only you can make.

## Patterns that recur across chapters

**Results without the rule that produces them.** This is the most common fault in every group of chapters. A hidden answer says what happened and leaves out the rule that made it happen, so a fellow cannot predict the next case. The single most frequent missing rule is "a `return` statement ends the function immediately, even from inside a loop", which is absent from the explanations of guard clauses in chapter 4, the `has_value` loop in chapter 7, the input loop in chapter 11, and the find-first pattern in chapter 13. Others are "Python evaluates every argument before it calls the function" (chapters 3 and 12), "any name a function assigns to is local to the whole function" (chapter 3 and the case study), and "a `def` creates a function without running its body" (chapters 3, 9, and 12).

**Verdicts in place of consequences.** Explanations stop at a judgment word such as "harmless", "clutter", "nonsense", "particularly useful", "earns its place", "mangled", "wouldn't look very good", or "teaches you nothing", without saying what a fellow or a user would see go wrong.

**Instructions with no stated problem.** This pattern is strongest in the Mod 0 Git chapters: check the README box, choose SSH, add a collaborator, edit the same line, merge `main` first, pull after merging. Each instruction appears with no reason, so it reads as ritual rather than as a fact about Git.

**Rules stated wrongly and then contradicted.** Several chapters state a rule early that a later section of the same chapter contradicts: "you can only interact with one directory at a time", "`cd` requires an argument", "`if` requires a boolean condition", "methods manipulate the value they are attached to", "`continue` prevents infinite loops", and "you can only push if your history is exactly the same as the remote's".

**Wrong cross-references.** Chapter numbers, line numbers, function names, and code fragments in the prose often point at the wrong place.

**JavaScript reasoning carried into Python.** Four passages explain Python with reasoning that is true only of JavaScript or Node: the REPL exit in chapter 0.1, the block-scope comment in chapter 5, the memory model in chapter 7, and the "first match only" sentence in the regex reading.

**Error messages quoted but not read.** Chapters 11, 12, and 13 quote Python error messages such as `'NoneType' object is not callable` without breaking them into their parts, which is rule 7 in the cases where it applies most.

## Decisions only you can make

- `14-project-week.md:199` — whether ties count in the Rock Paper Scissors win rate's denominator.
- `14-project-week.md:257` — what the shopping list does when a fellow removes more of an item than the list holds.
- `13-comprehensions-builtin-iteration.md:224` — whether `find_first_odd_index` should keep returning `-1` when nothing matches. `-1` is a valid index, so a caller who forgets to check gets the last element instead of an error.
- `case-study.md:92` to `:392` — these lines are inside an HTML comment, so GitBook currently hides every investigation section after User Interface Design, including all the hidden answers.
- The learning objectives at the top of `2-git-github.md`, `3-git-pulling-merging.md`, and `4-git-branching.md` use "Know", "Develop mental models", and "Define the terms", which break the ABCD rule in the root `CLAUDE.md`.

## Suggested order of work

Work through the clarity rewrites one batch of chapters at a time, starting with the hidden answers in each chapter, since those are where the missing rules cluster. Before applying a batch, read the log at the end of this document. After Ben commits a batch, compare the committed text with the applied rewrites and add what he changed to the log.

## Full findings: Mod 0: Command Line Interfaces, Git, and GitHub (chapters 0.1 to 0.4)

I checked every behaviour claim below in a scratch directory using zsh, Python 3.12.4 and Git 2.50.1 with an empty global Git configuration, and I marked the two claims I could not check. I did not edit any file.

**Warning about testing on your own machine.** Your global Git configuration sets `pull.rebase=false` and `push.autoSetupRemote=true`, and `environment-setup/github-setup.md` sets neither one. Because of those two settings, you will not see two of the errors below (finding 3-1 and finding 4-2) when you test the lessons on your laptop. A fellow with a fresh Git install will see both.

---

### 1-clis.md

**1. `1-clis.md:334`**

> To terminate the program, use the keyboard shortcut `Control+C` (you may need to cancel twice). You can also leave the Python REPL by entering `exit()`.

- **Rules broken:** 4, plus a factual error. The sentence came over from the Node original, and the Node REPL does exit on a double Control+C.
- **What a fellow gets wrong:** In the Python REPL, `Control+C` prints `KeyboardInterrupt` and gives back a fresh `>>>` prompt, so a fellow who follows this sentence keeps pressing `Control+C` and never leaves. I verified this: two presses printed two `KeyboardInterrupt` lines, and the REPL then still evaluated `1+1`.
- **Rewrite:** "To leave the REPL, type `exit()` and press Enter, or press `Control+D`. Don't bother with `Control+C` here: inside the REPL, Python treats `Control+C` as 'cancel the line I'm typing', prints `KeyboardInterrupt`, and hands you a fresh `>>>` prompt. `Control+C` is for stopping a program that is running and won't stop by itself. Try `sleep 100`, which waits for 100 seconds, and press `Control+C` to cut it short." I verified both `Control+D` and the `sleep 100` example. The surrounding paragraph at line 330 uses the REPL as its example of a program that "runs forever", so that paragraph needs the same change.

**2. `1-clis.md:268`**

> Using the `cd` command on its own will send you to the root of your entire file system (`~/`).

- **Rules broken:** subject/unit. The sentence names the wrong directory.
- **What a fellow gets wrong:** Line 107 defines the root as the top-most folder, so a fellow will believe that `~` is that folder. Running `cd` alone actually goes to `/Users/<name>` (I verified this in both zsh and bash).
- **Rewrite:** "Running `cd` on its own, with no argument, takes you to your **home directory**: the folder named after your username (`/Users/smith` in the tree above). `~` is the shortcut name for your home directory, so `cd` on its own is the same as `cd ~`. It's easy to hit Enter after `cd` before you've typed where you're going. If you do, you're suddenly far from your project, and the next `mkdir` or `touch` will make things in your home directory. Run `pwd` whenever you aren't sure where you landed."

**3. `1-clis.md:220`**

> However, unlike the previous commands, it requires an argument.

- **Rules broken:** 4. The sentence states a rule that is false twice over: `ls ..` (line 200) already gave a previous command an argument, and line 268 says `cd` works with no argument.
- **What a fellow gets wrong:** A fellow will read line 268 as contradicting this sentence and will not know which one to believe.
- **Rewrite:** "The `cd [directory]` command moves you to another directory. You tell `cd` where to go by giving it the destination as an **argument**. You've already used one argument: in `ls ..`, the `..` told `ls` which directory to report on."

**4. `1-clis.md:180`**

> In the terminal, you can only interact with one directory at a time, the **working directory**.

- **Rules broken:** 4. The sentence states the wrong rule.
- **What a fellow gets wrong:** Twenty lines later, `ls ..` acts on a different directory, so a fellow either decides the sentence is wrong or decides that `ls ..` must have moved them. The second belief is exactly the misconception that the box at line 213 tries to correct.
- **Rewrite:** "In the terminal, you are always located in exactly one directory, called the **working directory**. Commands act on the working directory unless you give them the path to somewhere else."

**5. `1-clis.md:370`**

> Another common occurrence is an unfinished string. You can test this with the `echo` command which will print a given string straight to the terminal.

- **Rules broken:** 1, 8, and subject. "Another" points back to nothing in this section; the sentence it referred to in the original was the Node REPL text.
- **What a fellow gets wrong:** The prose never says what goes wrong or how to get out of it. A fellow who sees `dquote>` will think the terminal is broken.
- **Rewrite:** "If you type an opening `"` and press Enter without the closing `"`, the terminal doesn't run your command. It waits for the rest of the string, and it shows a `dquote>` prompt instead of your usual one. Nothing is broken; the terminal is just waiting for you to finish. Type the closing `"` and press Enter to finish the command, or press `Control+C` to cancel it and get your normal prompt back. You can try this with `echo`, which prints whatever string you give it straight to the terminal." I verified this in zsh. Bash shows `>` instead of `dquote>`.

**6. `1-clis.md:258`** (the hidden answer)

> `cd ../../jones/Desktop`

- **Rules broken:** 4. The answer gives only the result.
- **What a fellow gets wrong:** A fellow who got the question wrong cannot see which part of the path they misread.
- **Rewrite:** Keep the command, then add: "Read the path one piece at a time, starting from `/Users/smith/Documents`. The first `..` takes you up to `/Users/smith`, and the second `..` takes you up to `/Users`. Then `jones` takes you down into `/Users/jones`, and `Desktop` takes you down into `/Users/jones/Desktop`."

**7. `1-clis.md:244`** (and line 252)

> the special directory name `..` which always refers to the parent directory of the working directory.

- **Rules broken:** 4 and 3. The rule as stated cannot explain `cd ../..`, and "again use `/`" at line 252 does not follow from it.
- **What a fellow gets wrong:** If `..` always means the parent of the working directory, then both copies of `..` in `../..` name the same folder, and a fellow cannot see why the command goes up two levels.
- **Rewrite:** "To go back 'up', use the special name `..`. Each `..` in a path means 'the parent of wherever the path has got to so far', so `cd ..` on its own takes you to the parent of the working directory." For line 252: "Because each `..` goes up one more level from where the last one left you, `cd ../..` takes you from `/Users/smith/Documents` up to `/Users/smith`, and then up again to `/Users`."

**8. `1-clis.md:213`**

> This is the distinction worth taking away: `ls` accepts a directory as an argument and _reports on_ it, while `cd` accepts a directory and _moves you into_ it. A command that looks at somewhere else does not put you there. Beginners frequently expect `ls ..` to have relocated them, and then get lost.

- **Rules broken:** 1 and 2. The verdict comes first, and the problem ("get lost") comes last without saying what getting lost leads to.
- **What a fellow gets wrong:** A fellow reads a rule before seeing why the rule matters.
- **Rewrite:** "A lot of beginners expect `ls ..` to have moved them into the parent directory. Their next `touch` or `mkdir` then makes files in the wrong place, and they can't work out where those files went. The rule is that `ls` only _reports on_ the directory you give it, while `cd` _moves you into_ the directory you give it. Looking at a directory never puts you there. Only `cd` changes your working directory."

**9. `1-clis.md:433`**

> This matters more than it looks. When you chain commands together (e.g. installing something and then running it, or saving your work and then uploading it) `&&` is what stops the second step from running on top of a first step that failed.

- **Rules broken:** 2. "Running on top of" is a judgment; the passage never names what goes wrong.
- **What a fellow gets wrong:** A fellow cannot tell what harm `&&` prevents.
- **Rewrite:** "This matters whenever the second command depends on the first. Take `cd my-project && python3 app.py`. If you misspell the folder, `cd` fails, `&&` stops, and you see one error that names the real problem. If you'd typed the two commands one after the other instead, `python3` would run anyway in the wrong folder and give you a second error, `can't open file ... No such file or directory`, about a file that exists. It just isn't where you are." I verified the wording of that error message.

**10. `1-clis.md:401`**

> First, `>>` _redirects_ the output — the text that would have gone to your screen goes into the file instead, so it cannot do both.

- **Rules broken:** subject and 3. "It" could mean the text, `>>`, or `echo`, and "so" rests on a premise that the sentence never states.
- **What a fellow gets wrong:** A fellow has to guess what "cannot do both".
- **Rewrite:** "First, `>>` _redirects_ the output of `echo`: the text that `echo` would have printed on your screen goes into the file instead. Output goes to one place only, so your screen gets nothing."

**11. `1-clis.md:154`**

> For this particular task it might be faster to use a GUI file manager like Finder, however there are many tasks where a CLI like the Terminal can outpace a GUI like Finder.

- **Rules broken:** subject and 2. "This particular task" has no clear referent, and the `mkdir` example is never compared with doing the same thing in Finder.
- **What a fellow gets wrong:** A fellow runs one command and makes eight folders, but is never told why that beats Finder.
- **Rewrite:** "For the handful of commands in that screenshot, clicking around in Finder might well be faster. But try making eight folders named `mod-0` through `mod-7` in Finder: you'd make a new folder and rename it, eight times over. In the Terminal, one command makes all eight:" (keep the code block, which I verified makes exactly eight folders in both zsh and bash) "And some things Finder simply can't do, like execute files with code."

**12. `1-clis.md:306`**

> Predicting silently lets you quietly adjust your prediction once you see the answer, which teaches you nothing. Writing it down first is what makes the gap between your expectation and reality concrete.

- **Rules broken:** 2 and 8. "Teaches you nothing" is a judgment, and the passage never says what the gap is good for.
- **What a fellow gets wrong:** The fellow has no reason to do the extra work.
- **Rewrite:** "If you only predict in your head, then once you see the answer it's very easy to decide you expected it all along. You walk away still holding whatever wrong idea produced your real guess. A written prediction can't change after the fact, so when it doesn't match, you can see exactly which part of your thinking was off."

### 2-git-github.md

**1. `2-git-github.md:129`**

> 1. The working directory (where we are editing files)

- **Rules broken:** subject. The same term carries a different meaning from the one defined one lesson earlier.
- **What a fellow gets wrong:** Chapter 1 defined the working directory as the one folder that `pwd` prints. A fellow will think Git's three places depend on where the terminal is.
- **Rewrite:** "1. The working directory: your project folder itself, where you edit files. Careful: Git uses 'working directory' to mean the whole project folder. That is a different meaning from the terminal's working directory in the last lesson, the one folder that `pwd` prints."

**2. `2-git-github.md:235`** (through line 250)

> Your local repository (on your computer) and your remote repository (on GitHub) are out of sync because I have a commit that exists locally but not on GitHub.

- **Rules broken:** 7 and subject. `origin/main` is never explained, and the sentence switches from "your" to "I".
- **What a fellow gets wrong:** A fellow has to guess what `origin` is. A fellow will also trust that "up to date" means up to date with GitHub as it is right now, which is the exact cause of the confusion in Chapter 3.
- **Rewrite:** "Each part of that last message does a different job. `On branch main` says which branch you're on (more on branches in lesson 4). `origin` is the name Git gave the GitHub repository when you cloned it, so `origin/main` means 'the `main` branch on GitHub'. `ahead of 'origin/main' by 1 commit` says your local repository has one commit that GitHub doesn't have yet. And `(use "git push" to publish your local commits)` tells you what to do about it. One catch: `git status` compares against what Git last downloaded from GitHub, not against GitHub as it is right now. Git only contacts GitHub when you run a command such as `git push` or `git pull`." I verified that `git status` still says "up to date" after a partner has pushed.

**3. `2-git-github.md:217`**

> Wherever your VC Code terminal is, the repository will be downloaded. If you want to clone the repository to a different location, you need to first change the directory you're in using `cd` before using `git clone`.

- **Rules broken:** 8 and subject. "Wherever" is vague, and the step of leaving `2-git-lecture` is missing.
- **What a fellow gets wrong:** A fellow who follows along stays inside `2-git-lecture`, where they ran `git init`, and clones a repository inside another repository.
- **Rewrite:** "`git clone` creates a new folder for the repository inside your terminal's working directory, so check where you are with `pwd` before you clone. If you're still inside `2-git-lecture`, where you ran `git init`, run `cd ..` first. Otherwise you'd be putting a repository inside another repository, and the next `git add -A` in `2-git-lecture` warns `adding embedded git repository`." I verified the warning.

**4. `2-git-github.md:137`** (the hidden answer)

> Check out [this StackOverflow post which does a great job of explaining!](...)

- **Rules broken:** 1 and 2. The hidden answer contains no answer.
- **What a fellow gets wrong:** A fellow has to leave the page to learn why the staging area exists.
- **Rewrite:** "The staging area lets you choose which changes go into a commit. Say you fixed a bug in one file and also started, but didn't finish, a new feature in another. If every change went straight into the next commit, your 'fixed the login bug' commit would also contain half a feature. Going back to that commit later would bring the half-feature back with it. With a staging area, you `git add` only the bug-fix file, commit it, and keep working on the feature until it's ready for its own commit. [This StackOverflow post](...) goes deeper."

**5. `2-git-github.md:190`**

> Make sure to check the **Add a README file** box.

- **Rules broken:** 1 and 2. The instruction gives no reason.
- **What a fellow gets wrong:** A fellow who skips the box gets a warning they can't interpret, and then has no `README.md` to edit in step 3.
- **Rewrite:** "Make sure to check the **Add a README file** box. Checking the box gives the new repository its first commit. Without it, GitHub creates a completely empty repository: `git clone` warns `You appear to have cloned an empty repository`, and step 3 has no `README.md` for you to edit." I verified the warning.

**6. `2-git-github.md:182`**

> Instead of using the `git init` command to create a _local repository_. We're going to start by creating a _remote repository_.

- **Rules broken:** 1. The passage gives the solution without the problem.
- **What a fellow gets wrong:** A fellow doesn't learn why the order matters, so later they will `git init` and then have nowhere to push.
- **Rewrite:** "This time, skip `git init`. A repository made with `git init` exists only on your computer and has no connection to GitHub, so `git push` has nowhere to send your commits. If you create the repository on GitHub first and then clone it, the clone comes already linked to GitHub."

**7. `2-git-github.md:98`**

> When we use Git for a project, the commits are stored alongside the code files.

- **Rules broken:** subject. "Alongside" does not say where the commits are.
- **What a fellow gets wrong:** A fellow who runs `ls` sees no commits and has to guess where they are.
- **Rewrite:** "When you use Git for a project, Git stores the commit history inside the project folder, in a hidden folder named `.git` that `git init` creates. Plain `ls` won't show `.git` because its name begins with `.`, but `ls -a` will. Together, the files and this commit history form a **Git repository**."

**8. `2-git-github.md:149`** (and line 150)

> The `echo` command combined with the `>` operator creates a new file ... After the `ls` and `git status` commands, we can see that the `myfile.txt` file has been created.

- **Rules broken:** 7 and subject. Chapter 1 taught `>>`, not `>`, and the "Untracked files" output goes unexplained.
- **What a fellow gets wrong:** A fellow thinks `>` is a typo for `>>`, and doesn't know what "untracked" means.
- **Rewrite:** "`echo` with the `>` operator creates a new file called `myfile.txt` containing `insert text here`. `>` works like the `>>` from the last lesson, except that `>` replaces whatever the file contained instead of adding to the end." For line 150: "`git status` now lists `myfile.txt` under `Untracked files`. Untracked means Git can see the file in the folder but isn't keeping a history of it yet, and the `(use "git add <file>...")` line tells you the next step." I verified both the behaviour of `>` and the `git status` output.

**9. `2-git-github.md:200`**

> make sure to select **SSH** (2)

- **Rules broken:** 1. The instruction gives no reason.
- **What a fellow gets wrong:** A fellow doesn't connect this choice to the SSH key from setup, and won't know why a clone made with the HTTPS address behaves differently when they push.
- **Rewrite:** Add "SSH is the connection you set up during environment setup: the SSH key on your computer is what lets GitHub recognise you when you push, without a password."

**10. `2-git-github.md:3`**

> We'll also they can back up and share their projects online

- **Rules broken:** subject. Words are missing from the sentence.
- **What a fellow gets wrong:** The second sentence of the chapter does not parse, so a fellow has to guess what it meant.
- **Rewrite:** "We'll also learn how they back up and share their projects online using..."

**11. `2-git-github.md:121`**

> So, you'll use Git and GitHub in tandem to manage your projects.

- **Rules broken:** 3. The "So" follows a list of Flask statistics, not the premise it rests on.
- **What a fellow gets wrong:** The sentence reads as a conclusion with nothing above it to support it.
- **Rewrite:** "So, Git and GitHub do two different jobs, and you'll use them together. Git runs on your own computer and records the changes to your project as commits. GitHub stores a copy of those commits online, where you can back them up and share them."

### 3-git-pulling-merging.md

**1. `3-git-pulling-merging.md:121`**

> So, the developer who pushed last should run `git pull`

- **Rules broken:** 8. A step is missing; the passage as written produces a different result for most fellows.
- **What a fellow gets wrong:** On a fresh Git install, this `git pull` stops with `fatal: Need to specify how to reconcile divergent branches.` and never reaches the merge conflict. I verified this on Git 2.50.1 with an empty configuration. The setup page does not set `pull.rebase`.
- **Rewrite:** "So, the developer who pushed last should run `git pull`. If Git has never been told how to combine two histories, `git pull` stops with `fatal: Need to specify how to reconcile divergent branches.` Run `git config --global pull.rebase false` once, which tells Git to combine histories by merging, then run `git pull` again." The better fix is to add that `git config` line to `environment-setup/github-setup.md`, next to the `user.name` and `user.email` lines.

**2. `3-git-pulling-merging.md:123`**

> However, in this situation, the conflict will cause a **Merge Conflict** like this:

- **Rules broken:** 3, 4 and 7. The sentence explains a conflict by saying that a conflict causes a conflict, and the output goes unexplained.
- **What a fellow gets wrong:** A fellow learns that pulling sometimes "conflicts", but not that the cause is two commits changing the same line.
- **Rewrite:** "`git pull` downloads developer 1's commit and then tries to merge it with developer 2's commit. Both commits replaced line 1 of `README.md` with a different name, and Git has no way to decide which name to keep. So Git stops partway through the merge:" (keep the output) "`Auto-merging README.md` says Git tried to combine the two versions of the file. `CONFLICT (content): Merge conflict in README.md` says the attempt failed because the same lines differ, and it names the file. `Automatic merge failed; fix conflicts and then commit the result.` tells you what to do next."

**3. `3-git-pulling-merging.md:111`**

> You are only allowed to push to the remote repository if your local repository has the exact same commit history as the remote repository.

- **Rules broken:** 4. The rule is stated wrongly: with identical histories, there would be nothing to push.
- **What a fellow gets wrong:** The rule contradicts Chapter 2, where pushing worked precisely because the local repository was "ahead by 1 commit".
- **Rewrite:** "GitHub only accepts your push if your local repository already has every commit that GitHub has. Your push can add new commits on the end, but it can't leave any of GitHub's commits out. Developer 2 is missing developer 1's commit, so GitHub rejects the push. The `hint:` lines in the message say the same thing: 'the remote contains work that you do not have locally'." I verified that hint text.

**4. `3-git-pulling-merging.md:143`** (through line 157)

> The three "markers" outline the two conflicting pieces of code: ... Alternatively, we can just delete the markers and keep the code you want to keep!

- **Rules broken:** 7 and 2. The passage never says which half of the conflict belongs to whom, and it never says what happens if a marker is left in the file.
- **What a fellow gets wrong:** A fellow editing by hand can't tell which half is theirs. If they miss a marker, Git commits it without complaint (I verified this).
- **Rewrite:** "The markers split the conflict into two halves. Between `<<<<<<< HEAD` and `=======` is the **current change**, the code in your local repository (`HEAD` is Git's name for the commit you're on). Between `=======` and `>>>>>>> b737ff...` is the **incoming change**, the code from GitHub, and `b737ff...` is the ID of the commit it came from." For option 2: "Alternatively, edit the file by hand: keep the lines you want and delete all three marker lines. Git doesn't check for leftover markers, so if you miss one, your commit saves it into the file and your partner pulls it. In a Python file, a leftover `<<<<<<< HEAD` is a `SyntaxError`." I verified that a leftover marker is a `SyntaxError` in Python.

**5. `3-git-pulling-merging.md:135`**

> **Merge conflicts** occur when two developers edit the same lines of code in the same repo and unsuccessfully merge those changes together, as happened here.

- **Rules broken:** 4. The definition is circular: a merge conflict is a merge that failed.
- **What a fellow gets wrong:** The definition does not give the rule for when Git can merge on its own and when it can't.
- **Rewrite:** "A **merge conflict** happens when two commits change the same lines of a file, or lines right next to each other. Git combines changes to separate parts of a file without asking. When both commits change the same lines, Git can't know which version you want, so it puts both versions in the file and asks you to choose. That's what happened here." I verified both cases: edits to adjacent lines conflict, and edits to distant lines merge without asking.

**6. `3-git-pulling-merging.md:61`**

> `git pull` does the opposite. If the local repository (on your computer) is missing commits that are on the remote repository (on GitHub), `git pull` will download those commits.

- **Rules broken:** 8. The merge half of `git pull` is missing.
- **What a fellow gets wrong:** When `git pull` later produces a _merge_ conflict, a fellow has no reason to connect pulling with merging. Only the image caption at line 77 says "attempt to merge".
- **Rewrite:** "`git pull` does the opposite. If your local repository is missing commits that are on GitHub, `git pull` downloads those commits and then merges them into your local repository, so your files match GitHub's. When you have no new commits of your own, the merge just adds the downloaded commits to the end of your history. You'll see what happens when both sides have new commits later in this lesson."

**7. `3-git-pulling-merging.md:83`** (and line 85)

> But what if both developers want to work simultaneously? Before moving on, the owner of the shared repo should add their partner as a collaborator:

- **Rules broken:** 1 and 2. The problem named here is working at the same time, but the real problem is permission to push.
- **What a fellow gets wrong:** A fellow who skips this step gets a permission error during the race and mistakes it for the conflict this lesson is about.
- **Rewrite:** "So far only the owner has pushed. GitHub accepts pushes only from the repository's owner and from people the owner has added as **collaborators**. So before your partner can push anything, the owner has to add them. If you skip this, your partner's push in the next section fails with a permission error, which has nothing to do with the merge conflict you're about to create." I did not verify the exact GitHub permission message.

**8. `3-git-pulling-merging.md:113`**

> They _could_ try to "force" their push through by running `git push -f` but this would delete their partner's commit!

- **Rules broken:** subject and 1. "They" is undefined at this point (developer 2 is first named at line 117), and the hint comes before the situation it comments on.
- **What a fellow gets wrong:** A fellow can't tell who would force the push or why.
- **Rewrite:** Move the hint below line 117 and write: "Developer 2 _could_ force the push through with `git push -f`. Forcing makes GitHub replace its history with developer 2's, which deletes developer 1's commit from GitHub. Use this command with caution."

**9. `3-git-pulling-merging.md:3`**

> In this lesson, we'll learn how to use GitHub to create and manage branches, merge branches, create pull requests, and resolve merge conflicts.

- **Rules broken:** subject. This sentence is copied from Chapter 4; this chapter teaches neither branches nor pull requests.
- **What a fellow gets wrong:** A fellow will look for branching content that this chapter does not have.
- **Rewrite:** "In this lesson, we'll learn how to download your teammates' changes with `git pull`, and how to resolve the merge conflicts that happen when two of you change the same line."

**10. `3-git-pulling-merging.md:97`**

> **This is the most important step. It is essential that both developers edit the same line of code**

- **Rules broken:** 1 and 4. The instruction gives no reason.
- **What a fellow gets wrong:** A fellow doesn't learn why this matters, so it reads as a rule of the game rather than a fact about Git.
- **Rewrite:** Add "because Git only reports a conflict when two commits change the same lines. If you edit lines far apart, Git combines your changes without asking, and there's no conflict to practise on."

**11. `3-git-pulling-merging.md:158`**

> Once you've made your choice, save the file, stage the changes, commit them, and push the changes.

- **Rules broken:** 3. The passage never says why a commit is needed.
- **What a fellow gets wrong:** The commit looks like an optional extra step.
- **Rewrite:** Add "That commit finishes the merge that `git pull` started. Until you make the commit, Git considers the merge still in progress."

### 4-git-branching.md

The file changed on disk during the review. The only change was to the title, so the line numbers below are current.

**1. `4-git-branching.md:107`**

> After you push your branch to GitHub, you should be able to see the new commit on the main branch as well as the new branch in the list of branches on GitHub.

- **Rules broken:** factual error.
- **What a fellow gets wrong:** A fellow who finds no new commit on `main` will think something broke. A fellow who believes the sentence will think that branches do not protect `main`.
- **Rewrite:** "After you push your branch to GitHub, the new branch shows up in GitHub's list of branches, and your new commit is on that branch only. `main` on GitHub hasn't changed, and that's the whole point: `main` stays exactly as it was until you merge."

**2. `4-git-branching.md:107`** (with the code comment at line 96)

> Try these commands out for yourself! After you push your branch to GitHub...

- **Rules broken:** 8. The upstream step appears only as a code comment, and "upstream" is never defined.
- **What a fellow gets wrong:** The first plain `git push` on a new branch fails with `fatal: The current branch feature-x has no upstream branch.` (I verified this with an empty configuration.)
- **Rewrite:** "The first time you push a new branch, plain `git push` fails with `fatal: The current branch [branch_name] has no upstream branch.` The branch exists only on your computer, so Git doesn't know which branch on GitHub to push it to. The message tells you the fix: run `git push --set-upstream origin [branch_name]` once. That command creates the branch on GitHub and links your local branch to it, and after that, plain `git push` works on this branch."

**3. `4-git-branching.md:174`** (the hidden answer)

> This is all for the sake of ensuring our managers approve our PR! A PR with merge conflicts is unlikely to be approved.

- **Rules broken:** 1, 2 and 3. The verdict comes first, the reason given is a manager's approval rather than what Git does, and the third sentence's "This way" rests on a problem that was never stated.
- **What a fellow gets wrong:** A fellow thinks the step exists to please a reviewer, not to deal with commits that `main` gained in the meantime.
- **Rewrite:** "While developer 2 was working on `feature-y`, developer 1 merged `feature-x` into `main`. So `main` on GitHub now has commits that `feature-y` doesn't have. If both developers changed the same lines, GitHub can't merge `feature-y` into `main` by itself, and the PR is stuck until somebody resolves the conflict. When developer 2 runs `git merge main` on `feature-y` first, any conflicts show up on developer 2's own computer. There, developer 2 can resolve them, run the combined code to check it still works, and push the result. The PR then contains everything already in `main` plus developer 2's work, so GitHub can merge it with no conflicts."

**4. `4-git-branching.md:61`** (the hidden answer; line 152 has the same gap)

> other developers would see those mistakes! And, well, that just wouldn't look very good.

- **Rules broken:** 2. The answer names embarrassment, not the real harm.
- **What a fellow gets wrong:** A fellow concludes that branches are about appearances.
- **Rewrite:** "As mentioned above, whenever someone views the repository or clones it, they get the main branch, and your teammates pull `main` every time they start work. If you push a bug straight to `main`, every teammate who pulls gets your bug too. Code that worked for them yesterday breaks today, and they lose an afternoon hunting for a problem they didn't create. (And, well, it doesn't look great either.) If you could save your changes somewhere else until you were sure everything worked, nobody else would be affected while you finish."

**5. `4-git-branching.md:51`**

> Every repository's commit history has what is called a **"main branch"** or **"trunk"**.

- **Rules broken:** subject and 8. "Branch" is used without ever being defined; the Key Term at line 28 defines "main branch" as "the main branch".
- **What a fellow gets wrong:** A fellow has to guess what a branch is.
- **Rewrite:** "A **branch** is a named line of commits in a repository. Every repository starts with one branch, usually called **main** (or the **trunk**). You've already seen its name: every `git status` you've run began with `On branch main`. Whenever anyone visits a repository on GitHub or clones it, the main branch is what they see."

**6. `4-git-branching.md:139`**

> A common step that developers of all levels forget is to return to their local repository and pull down the latest changes from GitHub.

- **Rules broken:** 1 and 2. The passage never says what goes wrong when someone forgets.
- **What a fellow gets wrong:** A fellow doesn't realise that a merge on GitHub leaves their local `main` behind.
- **Rewrite:** "When you merge a pull request on GitHub, the merge happens on GitHub only. Your local `main` still looks the way it did before. If you start your next feature branch from that old `main`, the new branch starts without the feature you just merged. So after every merge, return to your local repository and pull:"

**7. `4-git-branching.md:163`** (and line 169)

> 4. Return to your local repository and `git pull`.

- **Rules broken:** 8. The `git checkout main` step is missing.
- **What a fellow gets wrong:** A fellow still on `feature-x` runs `git pull`, which updates only the branch they are on (`feature-x` tracks `origin/feature-x`; I verified this), so `main` stays stale.
- **Rewrite:** "4. Run `git checkout main`, then `git pull`. Switch first, because `git pull` only updates the branch you're on, and the PR changed `main`."

**8. `4-git-branching.md:190`**

> There are 10 steps in this process:

- **Rules broken:** subject/unit. The alt text of the diagram directly above says 6 steps, and step 6 ("Pull and handle merge conflicts") doesn't say what to pull or into which branch.
- **What a fellow gets wrong:** A fellow can't match the list to the diagram, and in step 6 a fellow will run plain `git pull` on their feature branch.
- **Rewrite:** "The diagram groups the process into six boxes. Written out one action at a time, the process has 10 steps:" and for step 6: "Pull the latest `main`, merge it into your branch, and handle any merge conflicts."

**9. `4-git-branching.md:121`**

> A **pull request** (PR) is a request for another developer to review their branch and either merge the branch or request modifications.

- **Rules broken:** subject. "Their" could mean the requester or the reviewer.
- **What a fellow gets wrong:** A fellow can't tell whose branch is reviewed.
- **Rewrite:** "A **pull request** (PR) is a request, from you to the other developers on the project, to review your branch and then either merge it into `main` or ask you for changes."

**10. `4-git-branching.md:81`** (the hidden answer)

> Pushing commits in the local repository to the remote repository is similar to merging a feature branch with the main branch.

- **Rules broken:** 3. The answer never says what the two actions have in common.
- **What a fellow gets wrong:** A fellow has to work out the similarity alone.
- **Rewrite:** Add ": in both cases, commits you made in the separate copy get added to the original."

**11. `4-git-branching.md:167`**

> 3. It is possible that merge conflicts occurred so resolve them and add, commit, and push!

- **Rules broken:** 3. The step never says which command might have caused the conflicts.
- **What a fellow gets wrong:** A fellow doesn't know what "occurred" refers to.
- **Rewrite:** "3. If `git merge main` reports a merge conflict, resolve it the way you did in the last lesson, then add, commit, and push."

---

**Minor findings left out:**

- 1-clis.md: 7 more. These include line 321 (the reason the `SyntaxError` matters comes after the verdict), line 298 ("the command always has the 3 on the end" overstates the case; I could not check Ubuntu), line 456 (Challenge 20 says "skip" without saying what running a file you can't read could do), line 170 (VS Code has no **File > Terminal** menu item; the Terminal menu is a top-level menu, but I could not check this here), and lines 128, 150 and 410.
- 2-git-github.md: 3 more.
- 3-git-pulling-merging.md: 2 more.
- 4-git-branching.md: 3 more.

**Problems in the code blocks and objectives, which I was told to skip:**

- `1-clis.md:72` labels `cp` as "Move a file".
- `4-git-branching.md:44` lists `git checkout -B`, but the hint at line 100 teaches `-b`. The capital `-B` flag silently resets a branch that already exists.
- The objectives at `2-git-github.md:7-10`, `3-git-pulling-merging.md:7-8` and `4-git-branching.md:7-11` use "Know", "Develop mental models" and "Define the terms", which break the ABCD rule in the root `CLAUDE.md`.

**Recurring patterns.** The four chapters fail in two ways that recur. First, they state the action without the problem that makes it necessary: check the README box, select SSH, add a collaborator, edit the same line, merge `main` first, don't forget to pull. Each instruction appears with no reason, or with a judgment in place of a consequence ("wouldn't look very good", "teaches you nothing", "this matters more than it looks"). Second, several explanations state a rule that is wrong or circular, and the next section of the chapter then contradicts it: "only one directory at a time", "`cd` requires an argument", "`..` always means the parent of the working directory", "exact same commit history", and "merge conflicts occur when changes unsuccessfully merge". Several of these errors, along with the Python REPL `Control+C` error, came over unchanged from the JavaScript original. Finally, the Git chapters assume Git settings that your machine has and a fresh install lacks. Because of that, two of the lesson activities stop with a `fatal:` error for fellows that you will not see when you test them yourself.

## Full findings: Mod 1: chapters 1.1 to 1.3

I did not edit any file. I checked every Python fact in the rewrites with Python 3.12.4 in the scratchpad directory, including outputs, error messages, `help(print)` and the indentation error.

### 1-intro-to-programming.md

**1. `1-intro-to-programming.md:116`**

> **Question:** Why are we not seeing anything when we run this file?

- **Rules broken:** 3.
- **What a fellow gets wrong:** The only `main.py` on the page so far is the code block at line 79, which ends with `print(mood)`. A fellow who typed that block sees `happy`, so the question's premise is false for them, and the page never gives an answer.
- **Rewrite:** Either tell fellows what to put in the file before the question (for example, "Delete the `print(mood)` line and run the file again"), or reword the question: "Run `python3 main.py`. Only one word shows up in the Terminal, even though the file has six statements. Why?" Add a short hidden answer: "Only `print()` sends anything to the Terminal. The other statements still ran, but they change the program's state, and you can't see state unless you print it."

**2. `1-intro-to-programming.md:187`**

> `print()` itself also has more to it than a single message. It can take several values at once, and you can control what goes between them and what comes after them:

- **Rules broken:** 7, 8.
- **What a fellow gets wrong:** The code block uses `sep` and `end` with no explanation and no output. A fellow has to guess what each one does and what the defaults are. Chapter 3, line 381, later says "`sep` has a default value of a single space, which is why you never had to write it before", but that fact never appears in this chapter.
- **Rewrite:** "`print()` can also take several values at once. By default it puts a space between them and starts a new line after the last one. `sep` changes what goes between the values, and `end` changes what goes after the last one:" Then give the output under the code block:
  ```
  start
  the value of x is 10
  a-b-c
  no new line after this one <- see?
  ```
  The output was checked by running the code. The paragraph also sits inside "Debunking The `print()` Myth", which is about something else. It reads better at the end of "Printing to the Terminal".

**3. `1-intro-to-programming.md:137`**

> No. `print(celsius)` shows `194.22222222222223`, not `100.0`. Multiplication and division happen before subtraction, so Python computed `32 * 5 / 9` first and subtracted that from 212. The fix is parentheses: `(fahrenheit - 32) * 5 / 9`.
>
> Without the `print()`, this bug would have gone unnoticed, and that is exactly what `print()` is for.

- **Rules broken:** 1, 3, 4.
- **What a fellow gets wrong:** The answer never states the problem: the formula says to subtract 32 _first_. It never says why parentheses fix the problem. "Would have gone unnoticed" depends on a premise that is missing from the page: Python raises no error for a calculation that is valid but wrong.
- **Rewrite:** "No. The formula says to subtract 32 first and then multiply by 5/9, but Python does multiplication and division before subtraction. So Python worked out `32 * 5 / 9` first and subtracted that from 212, and `print(celsius)` shows `194.22222222222223` instead of `100.0`. Parentheses are always evaluated first, so `(fahrenheit - 32) * 5 / 9` makes the subtraction happen first. Notice that Python never complained. A wrong formula is still valid code, so the program runs happily and stores the wrong number. The only way you'd find out is by looking at the value, and that is exactly what `print()` is for."

**4. `1-intro-to-programming.md:99`**

> The `instructor` and `"ben"` expressions are combined using the `!=` operator to create an expression that returns the value `False`

- **Rules broken:** 4, 8.
- **What a fellow gets wrong:** The answer names only the condition. A fellow would conclude that `"ben"` on line 83, `None`, `"sad"`, `"happy"` and `mood` inside `print(mood)` are not expressions, which contradicts line 66. The answer also never says why the result is `False`.
- **Rewrite:** "Every value is an expression: `"ben"` and `None` on lines 2 and 3, and `"sad"` and `"happy"` inside the `if`/`else`. So is every variable name you read, like `mood` in `print(mood)`. The biggest one is the condition `instructor != "ben"`. It combines the `instructor` and `"ben"` expressions with the `!=` operator. `instructor` holds `"ben"`, so asking whether they are _not_ equal evaluates to `False`."

**5. `1-intro-to-programming.md:270`**

> Nothing runs. The interpreter cannot tell what belongs to `can_vote`, so it refuses the whole file before executing a single line. Indentation is not a style choice you make for your readers. It is part of the language, and getting it wrong is a syntax error.

- **Rules broken:** 1, 3.
- **What a fellow gets wrong:** The "so" depends on a premise that is not on the page: the interpreter checks the structure of the whole file before it runs any of it. A fellow can't see why one bad line stops lines that come earlier. The answer also never states the problem: a line ending in a colon must be followed by at least one indented line, and here no line is indented. The example file contains only a `def`, so a fellow can't observe that "nothing runs".
- **Rewrite:** "Line 1 ends with a colon, so the interpreter expects the next line to be indented as the body of `can_vote`. Line 2 isn't indented, so `can_vote` has no body at all. Before running anything, the interpreter reads the whole file to check that its structure makes sense. Because the structure is broken, it stops right there and runs nothing, not even the lines above the mistake. (Put `print("start")` at the top of the file and you'll see it never prints.) So indentation is part of the language itself, and getting it wrong is a syntax error." I checked the claim in the parenthesis by running the file. One caution: with that `print` line added, the error message names line 3 instead of line 2.

**6. `1-intro-to-programming.md:242`**

> Indentation shows the scope of each line of code, and it is how the interpreter knows which lines belong to which block.

- **Rules broken:** subject/unit (an undefined term of art).
- **What a fellow gets wrong:** "Scope" is not defined here. In chapter 3, "scope" means where a variable can be reached. A fellow would either guess at the word now or carry the wrong meaning into chapter 3. "Block" is also undefined.
- **Rewrite:** "Indentation is how the interpreter knows which lines belong to which block. A block is the group of lines that sit under a line ending in a colon `:`, like the body of a function or of an `if` statement. Whenever a line ends with a colon, the lines that belong to it must be indented underneath it."

**7. `1-intro-to-programming.md:75`**

> Expressions on their own do nothing. Expressions become useful when used within statements.

- **Rules broken:** 2, 8.
- **What a fellow gets wrong:** Line 66 says a function call is an expression, and `print("hello")` on a line by itself clearly does something. A fellow is left unsure whether `print()` counts as an expression. "Do nothing" also doesn't say what happens to the value.
- **Rewrite:** "An expression on a line by itself, like `5 + 5`, works out its value and then throws the value away, so the program is no different afterward. To keep a value or act on it, you use the expression inside a statement, for example by storing it in a variable."

**8. `1-intro-to-programming.md:165`** (with lines 175 and 185)

> This program below runs a loop one hundred million times! Even if you don't see any output, notice that it takes a moment for it to finish running:

- **Rules broken:** 3, 8.
- **What a fellow gets wrong:** The step that makes the delay count as evidence is missing: a program that did nothing would finish instantly. A fellow also has to guess how to "notice" the delay.
- **Rewrite:** "This program below runs a loop one hundred million times! Run it and watch the Terminal. You won't see any output, but the prompt takes a few seconds to come back. A program that did nothing would finish instantly. Those seconds are your computer adding 1 to `x`, one hundred million times." At line 185: "Nothing was printed, but the Terminal reports that the program ran for almost four seconds, and every one of those seconds went to the loop. (Your numbers will differ.)"

**9. `1-intro-to-programming.md:211`**

> For example, `if` statements can cause certain statements to be skipped.

- **Rules broken:** 4.
- **What a fellow gets wrong:** The code comments say which line is skipped but not why. A fellow has to work out for themselves that the condition is `False` because `instructor` holds `"ben"`.
- **Rewrite:** "For example, `if` statements can cause certain statements to be skipped. Below, `instructor` holds `"ben"`, so `instructor != "ben"` is `False`. The interpreter skips the indented line under `if` and jumps to the line under `else`."

**10. `1-intro-to-programming.md:306`**

> Four spaces per level, all the way down. Spaces around `<=`. No spaces inside the parentheses. No extra blank lines. And the function is renamed from `saythetime` to `say_the_time`, because that is how Python names things.

- **Rules broken:** 2, 8.
- **What a fellow gets wrong:** The answer is a list of fixes with no stated cost to the reader. A fellow learns the rules but not why the original code was hard to read, which is the point of the section.
- **Rewrite:** "The original indents each block by a different amount (1, 12, 2 and 4 spaces). Python accepts that, but a reader can't tell at a glance which `print` belongs to which branch. So use four spaces per level, all the way down. Add spaces around `<=` so the comparison stands out from the names on either side. Remove the spaces inside the parentheses and the stray blank line. Rename `saythetime` to `say_the_time`, because Python names use `snake_case` and the underscores let a reader see the three words."

**11. `1-intro-to-programming.md:66`**

> **Expressions** are any piece of code that evaluates to a single value. the results of evaluating an operation (e.g. `5 + 5`) or a function call (e.g. `len("hi")`). A standalone values (e.g. the string literal `"hello world"`) is also considered an expression because it evaluates to itself.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** The second "sentence" has no subject or verb, so a fellow has to guess how it connects to the first.
- **Rewrite:** "**Expressions** are any piece of code that evaluates to a single value, such as an operation (`5 + 5`) or a function call (`len("hi")`). A value on its own (the string `"hello world"`) is also an expression, because it evaluates to itself."

### 2-data-types-variables.md

**1. `2-data-types-variables.md:178`** (a comment in the hidden answers)

> Why: Some operations you simply can't perform. In this case, you can't add different types.

- **Rules broken:** 4.
- **What a fellow gets wrong:** The stated rule is false. `5 + 2.5` gives `7.5` and `True + 1` gives `2`; I checked both. A fellow would predict that `4 * 2.5` and `True + True + False` fail too, and those appear a few lines away.
- **Rewrite:** `# Why: + can add two numbers or join two strings, but it has no meaning for a string and a number. Python won't guess whether you meant "55" or 10, so it stops with a TypeError. (Different kinds of numbers, like 5 + 2.5, are fine.)`

**2. `2-data-types-variables.md:268`**

> If arithmetic did _not_ come before comparison, Python would have read it as `temperature - (10 > 70)`, which is `85 - False`, which is `85`, and then `"hot" if 85 else "mild"`. That gives the same answer here by luck, and a different one for other temperatures.

- **Rules broken:** 3, 4.
- **What a fellow gets wrong:** Why `"hot" if 85 else "mild"` gives `"hot"` depends on truthiness, which is not taught until chapter 4. "Other temperatures" leaves the fellow to find a case where the answer changes.
- **Rewrite:** "If arithmetic did _not_ come before comparison, Python would have read it as `temperature - (10 > 70)`. That is `85 - False`, which is `85`. The conditional expression would then be checking `85` instead of `True` or `False`. Chapter 4 explains that any number other than 0 counts as true, so the result would still be `"hot"`, but only by luck. Try `temperature = 60`. The real order gives `50 > 70`, which is `False`, so the result is `"mild"`. The wrong order gives `60`, which counts as true, so the result is `"hot"`. Knowing the order is what lets you predict the result instead of hoping." I checked both results with `temperature = 60` by running them.

**3. `2-data-types-variables.md:113`**

> How you make that decision almost entirely depends on the kinds of **operators** that you can use with each data type. Operators are used to create expressions that generate new data. However, you must learn how each data type interacts with each operator to avoid `TypeError`s

- **Rules broken:** 1, 2, 3.
- **What a fellow gets wrong:** The paragraph never connects operators back to the light switch. "However" contrasts with nothing. `TypeError` appears with no statement that it stops the program.
- **Rewrite:** "How you make that decision depends mostly on what you want to do with the value, and that comes down to which **operators** work with each type. An operator, like `+` or `not`, takes values and produces a new one. With booleans, `not is_on` flips the switch in one step. With the strings `"on"` and `"off"`, no operator does that, so you'd need an `if` statement. Each type works with some operators and not others. Use an operator on a type it doesn't support and the program stops with a `TypeError`:"

**4. `2-data-types-variables.md:527`**

> That is what the `[] or "Python"` line in the challenge above was doing.

- **Rules broken:** 3.
- **What a fellow gets wrong:** The challenge contains `0 or "Python"`, not `[] or "Python"`. A fellow who looks back finds no such line.
- **Rewrite:** "That is what the `0 or "Python"` line in the challenge above was doing."

**5. `2-data-types-variables.md:202`** (a comment in the hidden answers)

> Why: `is` checks for identity equality, not value equality. While they both contain the same values, Python creates two distinct list objects in memory.

- **Rules broken:** 1, 5.
- **What a fellow gets wrong:** The comment opens with "identity equality" versus "value equality", which are undefined terms, before the fact a fellow can actually picture: two separate lists were created.
- **Rewrite:** `# Why: Each [1, 2] you type creates a brand-new list, so this line makes two separate lists that happen to hold the same values. == asks "are these equal?", which is why the line above is True. is asks "are these the very same list?", and two separate lists are not.`

**6. `2-data-types-variables.md:314`** (a comment in the hidden answers)

> `# True -> \`True and 4\` produces 4, and 4 == 4`

- **Rules broken:** 4.
- **What a fellow gets wrong:** The only rule taught for `and` so far (the table at line 514) says it produces `True` or `False`. A fellow can't see why `True and 4` produces `4`.
- **Rewrite:** `# True -> When the left side of and counts as true, and hands back the right side, so True and 4 produces 4 (chapter 4 explains this). Then 4 == 4 is True.`
- Line 313 (`# True -> Arithmetic and comparison combined with logical`) gives no order of steps either. A better comment there is `# 2 + 2 first, then > and ==, then and`.

**7. `2-data-types-variables.md:407`**

> Be careful about adding strings together. If you don't put a space in between the words, then the words will be combined directly!
>
> The entire statement gets evaluated in this order:

- **Rules broken:** 1, 4.
- **What a fellow gets wrong:** The warning comes before the steps, and the steps never say _why_ `'!' * 3` goes first. The steps also don't say that the whole right side is finished before `+=` acts.
- **Rewrite:** "Python evaluates the whole right side before `+=` touches `msg`, and within the right side `*` goes before `+`:" followed by the three steps, then: "Notice there's no space between `hello` and `world`. `+` joins strings exactly as they are and adds nothing between them, so if you want a space, you have to put it in a string yourself."

**8. `2-data-types-variables.md:250`**

> They differ right at step 1. Everything after that is downstream of which operator got to go first.

- **Rules broken:** 4, 8, subject/unit ("downstream" is an idiom).
- **What a fellow gets wrong:** The fellow has to work out for themselves what actually differs at step 1 and why that changes the end result.
- **Rewrite:** "They differ right at step 1. Without parentheses, Python multiplies first. With parentheses, it subtracts first. Every later step works on the number that step 1 produced, so a different first step gives a different final answer."

**9. `2-data-types-variables.md:435`**

> A global variable whose value should never change is written in `ALL_CAPS`, and every Python programmer reads that as "do not reassign me". It is just a convention, so it is still possible to reassign them.

- **Rules broken:** 2, subject/unit.
- **What a fellow gets wrong:** "Global variable" is not taught until chapter 3. "Them" could mean the names or the programmers. The consequence of the convention is missing: Python gives no warning when a constant is reassigned.
- **Rewrite:** "A variable whose value should never change is called a constant, and its name is written in `ALL_CAPS`. Every Python programmer reads that as "do not reassign me". But it's only a convention. Python itself doesn't enforce it, so reassigning a constant raises no error, and nothing warns you if you do it by accident."

**10. `2-data-types-variables.md:345`**

> The first approach can be written in one line, however, it is very long. This makes it more difficult to read and predict the output. Additionally the `4 + 3 + 2 + 1` expression must be calculated twice since that calculation is not saved anywhere.

- **Rules broken:** 2.
- **What a fellow gets wrong:** "Calculated twice" is stated as a cost, but the harm is not named.
- **Rewrite:** "...Additionally, the `4 + 3 + 2 + 1` expression is written out twice, because the first result isn't saved anywhere. If you change one of the numbers, you have to remember to change it in both places. Miss one, and the sum and the average quietly disagree."

**11. `2-data-types-variables.md:162`** (a comment in the hidden answers)

> Why: Alphabetically, B comes after A

- **Rules broken:** 4.
- **What a fellow gets wrong:** Python orders strings by character code, not by the alphabet. A fellow following "alphabetically" would predict that `"apple" > "Banana"` is `False`, but it is `True` (checked by running it).
- **Rewrite:** `# Why: Strings are compared character by character, using each character's position in Python's character table. "B" comes after "A" in that table. (Every uppercase letter comes before every lowercase one, so "a" > "Z" is True too.)`

**12. `2-data-types-variables.md:190`** (a comment in the hidden answers)

> Why: `or` treats 0 as False and hands back the other value.

- **Rules broken:** 4.
- **What a fellow gets wrong:** "The other value" doesn't state the rule for which side `or` returns.
- **Rewrite:** `# Why: or hands back the left side if it counts as true, and otherwise hands back the right side. 0 counts as false, so you get "Python". Chapter 4 explains which values count as false.`

### 3-functions.md

**1. `3-functions.md:98`** (a code block, flagged because it makes the prose at lines 106 and 113 false)

> `celsius = 20` (the first line of the body of `convert_C_to_F`)

- **Rules broken:** 3.
- **What a fellow gets wrong:** That line overwrites the parameter. Every call prints `68.0`, which I confirmed by running it. A fellow who runs the code sees results that contradict the comments `# 212` and `# 32` and "the logic is the exact same!"
- **Fix:** Delete line 99. Related: the output comments at lines 55, 63, 67, 71 and 113 to 115 say `212`, `32` and `68`, but Python prints `212.0`, `32.0` and `68.0`. Chapter 1 made a point of `100.0` versus `100`, so fellows will notice the difference.

**2. `3-functions.md:200`**

> Note that the order in which statements are executed in our code is not always top to bottom. Defining the function doesn't cause the code inside to run. We only execute the code inside of `say_hello` when it is invoked a few lines later.

- **Rules broken:** 3, 4, 5.
- **What a fellow gets wrong:** The example's function is `print_B`; `say_hello` does not exist yet. The answer also never explains why `B` appears twice and after `C`.
- **Rewrite:** "`A` prints first. Then the interpreter reaches the `def`. A `def` stores the function under the name `print_B` but does not run the code inside it, so no `B` yet. `C` prints next. Then each `print_B()` call jumps into the function, prints `B`, and comes back, and there are two calls, so you get two `B`s. The order the statements run in is not always the order they are written."

**3. `3-functions.md:78`** (with line 74, "But this approach doesn't scale well.")

> It breaks the fundamental software engineering principle "DRY" which stands for "Don't Repeat Yourself". Repetition is a problem for two primary reasons:
>
> - If we need to change the format of our print statements, we need to change the format in 3 places.
> - If we need to fix a bug in the code, we need to fix it in 3 places.
>
> The solution is to create a function!

- **Rules broken:** 1, 2, 3.
- **What a fellow gets wrong:** The verdict ("breaks DRY") comes before the problem. "Change it in 3 places" leaves out the real harm, which is missing one of the places. "The solution is to create a function" doesn't say how a function solves the problem.
- **Rewrite:** "The formula `* 9/5 + 32` is written out three times. Suppose it has a bug, or you want to change how the result prints. You'd have to make the same change in three places, and if you miss one, two conversions are right and one is quietly wrong. Add a fourth temperature and that's a fourth copy to keep in sync. Engineers call this principle "DRY": Don't Repeat Yourself. A function fixes the problem by holding the formula in one place, so a fix made there reaches every conversion."

**4. `3-functions.md:44`**

> `print` is a **function**—a custom-made statement that is designed to do a particular task many times within a program.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** Chapter 1 taught that a function call is an _expression_. Calling a function a "statement" muddles the two terms a week after they were introduced, and "custom-made" is odd for a built-in function.
- **Rewrite:** "`print` is a **function**: a named block of code that does one particular task, which you can run as many times as you like."

**5. `3-functions.md:255`**

> The first call gets as far as `x + y` and then refuses: Python will not add a string and a number, and the next chapter says more about why. Python checks types at the moment an operation runs, not at the moment the function is called.

- **Rules broken:** 3, 4.
- **What a fellow gets wrong:** Chapter 4 never mentions `TypeError`. Chapter 2 is the chapter that covered it, so the cross-reference sends fellows to the wrong chapter. The answer also skips the step where the arguments are substituted.
- **Rewrite:** "The first call starts fine: `x` becomes `'hello'` and `y` becomes `5`. Then the body runs `x + y`, which is now `'hello' + 5`. As you saw in the last chapter, `+` can't join a string and a number, so Python stops with a `TypeError`. Python checks types at the moment an operation runs, which is why the call itself got through."

**6. `3-functions.md:324`**

> The output is `20`. The function calls are evaluated (a.ka.a "resolve") in this order:

- **Rules broken:** 4.
- **What a fellow gets wrong:** The order is listed but the rule behind it is missing, so a fellow can't predict the next nested call. ("a.ka.a" is also a typo.)
- **Rewrite:** "The output is `20`. Python has to know the value of every argument before it can call a function, so it works from the inside out. The function calls resolve in this order:"

**7. `3-functions.md:609`**

> You can force Python to use the global one by adding `global count` as the first line of the function. **Do not.** A function that reaches out and changes variables that live outside of it is a function whose behavior you cannot predict by reading it. Pass the value in as a parameter and `return` the new value instead.

- **Rules broken:** 2, 8.
- **What a fellow gets wrong:** "Cannot predict by reading it" is a judgment with no stated consequence. "Pass the value in and return it" comes with no code, so a fellow has to guess what the call looks like.
- **Rewrite:** "...**Do not.** If `increment` changes `count` directly, you can no longer tell what `count` holds by reading the lines around it. Any function anywhere in the file might have changed it, so tracking down a wrong value means reading every function. Pass the value in as a parameter and `return` the new value instead:" Then show the code:
  ```python
  def increment(count):
      return count + 1

  count = increment(count)
  ```
  Then: "Now the only line that changes `count` is the one you can see."

**8. `3-functions.md:607`**

> The moment Python sees `count = ...` inside `increment`, it decides that `count` is a _local_ variable of `increment`. Then it tries to evaluate `count + 1` using that local variable, which has not been given a value yet. It never even looks at the global `count`.

- **Rules broken:** 4, 3.
- **What a fellow gets wrong:** "The moment Python sees" suggests that Python decides line by line. In fact the decision covers the whole function, and the rule is never stated. The error is `UnboundLocalError`, not the `NameError` the chapter has taught, and the answer never links the two.
- **Rewrite:** "The rule: if a function assigns to a name anywhere inside it, that name is local to the whole function. `increment` assigns `count = ...`, so `count` is local to `increment`, even on the right side of that same line. Python evaluates the right side first, `count + 1`, and the local `count` has no value yet. So Python never reaches the global `count`, and it raises an `UnboundLocalError`, a close cousin of `NameError` for exactly this situation."

**9. `3-functions.md:175`**

> However, code within a function only runs when it is invoked (in other words, when the function is "called"). When that happens, the interpreter jumps up into the function and executes the first line.

- **Rules broken:** 8.
- **What a fellow gets wrong:** The passage leaves out the return trip. To predict output like `A C B B`, a fellow needs to know that the interpreter comes back to the line after the call.
- **Rewrite:** "...When that happens, the interpreter jumps up into the function and runs its lines from top to bottom. After the last one, it jumps back to where the call was and carries on from there."

**10. `3-functions.md:298`**

> The functions above use `print` to print out a result to the console, but that result can't be used later in the program. If we want a function to produce a value that we can be used outside of the function, we add a `return` statement.

- **Rules broken:** 3, subject/unit.
- **What a fellow gets wrong:** The passage doesn't say _why_ a printed result can't be used. "Console" is a new word for what chapter 1 called the Terminal. "That we can be used" is a typo.
- **Rewrite:** "The functions above use `print` to show a result in the Terminal. `print` puts the value on the screen for you to read, but the program keeps no copy of it, so the rest of the program can't use it. If we want a function to produce a value that the rest of the program can use, we add a `return` statement."

**11. `3-functions.md:510`**

> As a best practice, aim to declare variables in the lowest possible scope where the variable is needed (local rather than global).

- **Rules broken:** 1, 2.
- **What a fellow gets wrong:** The passage gives the practice with no problem it prevents. "Lowest" is undefined: the list at line 449 orders scopes by reachability, not by height. Line 514's "the natural shape for this kind of function" is a judgment with no reason given.
- **Rewrite:** "Any function in the file can read a global variable, so when a global holds the wrong value, you have to search the whole file for the cause. A local variable can only be touched by its own function, so there's only one place to look. That's why the best practice is to make each variable local to the one function that needs it, and to make it global only when several functions need it."

**12. `3-functions.md:502`**

> Notice what did _not_ cause an error: `print(message)` inside `greet_friend`, after the `if`/`else`. The `if` block did not hide `message` from the rest of the function.

- **Rules broken:** 5.
- **What a fellow gets wrong:** The point is made through negations. The fellow has to turn "did not hide" into the rule themselves.
- **Rewrite:** "Notice that `print(message)` inside `greet_friend`, after the `if`/`else`, worked fine. A variable assigned inside an `if` or `else` block belongs to the whole function, so it is still there after the block ends."

### Minor findings left out

- `1-intro-to-programming.md`: 3 further minor findings.
- `2-data-types-variables.md`: 5 further minor findings.
- `3-functions.md`: 6 further minor findings.

### Pattern across the three files

The hidden answers often state a result and a verdict but leave out the rule that produces the result. Examples are "Alphabetically", "you can't add different types", "`True and 4` produces 4", "the solution is to create a function!" and "they differ at step 1". In several places the missing rule is one the fellow has not been taught yet, either truthiness or the fact that `and`/`or` return one of their operands. A second recurring pattern is cross-references that point at the wrong thing:

- `[] or "Python"` where the challenge has `0 or "Python"`.
- `say_hello` where the example has `print_B`.
- "the next chapter" for `TypeError`, when chapter 2 is the one that covers it.
- chapter 3 recalling a `sep` default that chapter 1 never explained.

A third pattern is the `convert_C_to_F` bug: the code under discussion contradicts the prose and its output comments. The same thing happens on a smaller scale with `212` versus `212.0`. Outside the prose brief: code blocks at chapter 2, line 336 and chapter 3, lines 124 and 310 name a variable `sum`. That reassigns a built-in name, which chapter 3, line 453 tells fellows to avoid.

## Full findings: Mod 1: chapters 1.4 to 1.7

I did not edit any file. I checked every claim about Python behaviour that appears in a rewrite below by running it with `python3` in the scratchpad.

### 4-conditional-statements.md

**1. `4-conditional-statements.md:138`**

> If the program makes it to the last `return "Nah"` statement, we can assume that the temperature is less than or equal to 75 because none of the other conditions were `True`.

- **Rules broken:** 3 and 4.
- **What a fellow gets wrong:** The answer leaves out two steps. It never says that `return` ends the function, and that rule is the only reason that reaching the last line means every condition was `False`. It also never says why an `if` would be useless on that line. A fellow could reasonably think the `if` was left out only to save typing.
- **Rewrite:** "A `return` statement ends the function the moment it runs, so the program only reaches the last line when every `if` above it was `False`. If `temp > 75` was `False`, the temperature must be 75 or less. An `if temp <= 75:` on that line would check a condition that can only ever be `True`, so you can leave it off and just `return "Nah"`."

**2. `4-conditional-statements.md:118`**

> When working with a function that changes the value returned based on a condition, we can avoid using conditional chains and only use `if` statements called "guard clauses".
>
> A **guard clause** is an `if` statement that returns before subsequent return statements have a chance to be executed.

- **Rules broken:** 1 and 4.
- **What a fellow gets wrong:** The passage never says why plain `if` statements can replace an `elif` chain, which is that `return` ends the function. A fellow is left to guess why the guard clauses do not all run, the way the `if`s in the section above did.
- **Second problem:** The example directly below this passage returns `"Eh"` for 105 (I confirmed this by running it). No text in the section says so, so the first guard clause a fellow ever sees gives the wrong answer and nothing explains why.
- **Rewrite:** "When a function returns a different value depending on a condition, you can replace the `elif`/`else` chain with plain `if` statements. This works because a `return` statement ends the function the moment it runs. Once one `if` returns, none of the lines below it get a chance to run. An `if` statement used this way is called a **guard clause**." After the example, add a hidden answer: "It prints `Eh`. Order still matters: `105 > 75` is `True`, so the first guard clause returns before the others are checked."

**3. `4-conditional-statements.md:69`**

> Only the first condition that is `True` will be executed. This means we have to be careful with the order in which we write our conditional statements.

- **Rules broken:** 3, 2, and subject. Conditions are checked, not executed.
- **What a fellow gets wrong:** The step that connects "first true" to "order matters" is missing: a broad condition placed first catches values that were meant for narrower conditions below it. The question that follows has no answer, so this sentence is the only explanation a fellow gets.
- **Rewrite:** "Python checks the conditions from top to bottom and runs the code block under the first condition that is `True`. As soon as one block runs, Python skips every remaining `elif` and `else` without checking them. So if a broad condition like `temp > 75` comes first, it catches 95 and 105 too, and the narrower conditions below it never get a turn."

**4. `4-conditional-statements.md:185`**

> If you ever compare user input to a boolean, remember that the user typed a string.

- **Rules broken:** 2. The verb "compare" is also wrong for this case.
- **What a fellow gets wrong:** The trap in this example is using input as a condition, not comparing it. A fellow is not told the consequence, which is that the `True` branch runs for a user who typed `no`. (I confirmed that `bool("no")` is `True` and that `"False" == False` is `False`.)
- **Rewrite:** "If you ever use what a user typed as a condition, remember that the user typed a string. A user who types `no` or `False` still gives you a non-empty string, so `if answer:` runs the `True` branch for them. Compare the string itself instead: `if answer == "yes":`."

**5. `4-conditional-statements.md:169`**

> One caution. `if not value:` cannot tell `None` apart from `0` or `""`, because all three are falsy.

- **Rules broken:** 2.
- **What a fellow gets wrong:** The passage gives a warning but no harm. A fellow cannot tell when the problem would actually bite.
- **Rewrite:** "One caution. `if not value:` cannot tell `None` apart from `0` or `""`, because all three are falsy. Suppose `score` is `None` until a player finishes a game. A player who finishes with a score of `0` also makes `if not score:` `True`, and your program would treat them as if they had never played. When the question you are asking is specifically "is this `None`?", write `if score is None:`. That is what the `is` operator from chapter 2 is for."

**6. `4-conditional-statements.md:167`**

> `not friend` is `True` when `friend` is the empty string, because `""` is falsy.

- **Rules broken:** 3 and 8.
- **What a fellow gets wrong:** "Falsy" means `False`, yet the sentence concludes `True`. The step where `not` flips the result is missing.
- **Rewrite:** "When `friend` is the empty string, `bool("")` is `False`, and `not` flips `False` to `True`. So `not friend` is `True`, and the guard clause returns the message."

**7. `4-conditional-statements.md:144`**

> Python has a function called `bool()` that converts any value to `True` or `False`, and it is the one conditions use without being asked.

- **Rules broken:** subject and 6.
- **What a fellow gets wrong:** "The one conditions use without being asked" has no named actor. A fellow has to guess what it means for a condition to "use" a function.
- **Rewrite:** "Python has a function called `bool()` that converts any value to `True` or `False`. An `if` statement calls `bool()` on its condition for you whenever the condition is not already a boolean." Line 155 then repeats this point and can be cut back to the guard-clause sentence.

**8. `4-conditional-statements.md:63`**

> `if` and `elif` statements require a boolean condition to evaluate to `True` in order to run.

- **Rules broken:** 3. This line contradicts the truthy section that comes later.
- **What a fellow gets wrong:** A fellow reads that the condition must be a boolean. Eighty lines later the chapter shows `if not friend:` and `if "False":`, and the fellow has to work out which of the two statements is true.
- **Rewrite:** "The condition after `if` or `elif` is usually a comparison like `temp > 100`. The code block under it runs only when the condition is `True`. `elif` is short for "else if"."

**9. `4-conditional-statements.md:155`**

> When an `if` is given something that is not already a boolean, it calls `bool()` on it for you. That makes a guard clause against empty input very short:

- **Rules broken:** 3 and subject.
- **What a fellow gets wrong:** "Very short" compared to what? The longer version is never shown, so a fellow cannot see what was saved.
- **Rewrite:** "Because an `if` calls `bool()` for you, `if not friend:` does the same job as `if friend == "":`, in fewer characters:"

**10. `4-conditional-statements.md:196` (the "Okay" and "Better" labels) and the bullets at line 192**

- **Rules broken:** 2.
- **What a fellow gets wrong:** The section calls one version "Better" and never says what the "Okay" version costs a reader.
- **Rewrite (add after the code):** "Both versions print the same message. The conditional expression is easier to read because `message` is assigned on one line, with both possible values side by side. A reader does not have to scan two branches to find out what `message` can hold."

### 5-loops.md

**1. `5-loops.md:181`**

> An **infinite loop** is one in which the condition is ALWAYS `True`. This will cause a program to run forever, either depleting resources or just causing the computer to stall while it waits for the program to end.
>
> Infinite loops are most often created using `while` loops which are best used to repeat a process an _unknown_ number of times.

- **Rules broken:** 1 and 4.
- **What a fellow gets wrong:** The chapter never says what a `while` loop does. It introduces the failure mode before the tool. A fellow has to guess what "the condition" refers to and when it is checked.
- **Rewrite:** "A `while` loop repeats its code block for as long as its condition is `True`. Before each pass, Python checks the condition. If the condition is `True`, the block runs again. If the condition is `False`, the loop ends and the program continues with the code after it. That makes `while` loops the right tool for repeating a process an _unknown_ number of times, like rolling a die until you get a 6. If the condition never becomes `False`, the loop never ends. This is called an **infinite loop**, and the program runs forever, or until you stop it."

**2. `5-loops.md:185`**

> To ensure that a loop does not go on infinitely, we use these two statements:
>
> - `break` prematurely breaks out of a loop
> - `continue` prematurely goes to the next iteration of the loop

- **Rules broken:** 3.
- **What a fellow gets wrong:** `continue` never ends a loop, but this passage tells a fellow it prevents infinite loops. "Prematurely" is a judgment, and the definitions never say where execution goes next.
- **Rewrite:** "Two statements let you control a loop from inside its code block. `break` ends the loop immediately, and the program continues with the first line after the loop. `continue` skips the rest of the current pass and jumps back to the top of the loop for the next one. `break` is how you get out of a loop whose condition is always `True`. `continue` keeps the loop going, so it cannot get you out of an infinite one."

**3. `5-loops.md:163` (a code comment inside the hidden solution)**

> # We want to use this variable after the loop is done, so we create it outside the loop

- **Rules broken:** 3. The stated reason is false in Python, and it looks like a leftover from the JavaScript original.
- **What a fellow gets wrong:** In Python, a variable created inside a `for` loop is still available after the loop ends. (I confirmed this by running it.) A fellow learns a rule that does not exist and misses the real reason, which is that `heads = 0` inside the loop would reset the count on every flip.
- **Rewrite:** "# Create heads before the loop. If heads = 0 were inside the loop, it would reset to 0 on every flip, and the count could never get past 1."

**4. `5-loops.md:238` (a code comment inside the hidden solution)**

> # We're going to pull out this `guess` value so we can check it on every loop

- **Rules broken:** 3 and 1.
- **What a fellow gets wrong:** The comment never says what goes wrong without this line. The `while` condition reads `guess` before the first guess is made, so without the line the program crashes. (I confirmed that this raises `NameError: name 'guess' is not defined`.)
- **Rewrite:** "# The while condition below checks guess before the first guess is made, so guess has to exist already. Without this line, Python stops with NameError: name 'guess' is not defined."

**5. `5-loops.md:209`**

> A `break` statement will exit the current loop and continue executing code that follows the loop. A `return` statement inside of a loop will exit the current loop AND the current function being executed.

- **Rules broken:** 2.
- **What a fellow gets wrong:** The visible difference between the two statements is never shown. The dice example is not inside a function, so a fellow cannot see what `return` would skip.
- **Rewrite:** "`break` ends the loop, and the program carries on with the first line after the loop. `return` ends the whole function the loop is inside, so any lines after the loop in that function never run. If the dice loop above were inside a function and used `return` instead of `break`, `See you next time!` would never print."

**6. `5-loops.md:53`**

> But even so, we have to manually update each number. What a pain!

- **Rules broken:** 2 and subject. "Even so" points back across a code block.
- **What a fellow gets wrong:** The cost of the copy-and-paste approach, which is the problem the `for` loop solves, is left implied.
- **Rewrite:** "The computer flips faster than you do, but the program still needs one line per flip, with each flip number typed by hand. The program for 100 flips would be 100 nearly identical lines, and 1,000 flips would mean 900 more. What a pain! If only there was some way to do this more efficiently."

**7. `5-loops.md:72`**

> Try using the debugger and you will see the order of operations
>
> 1. Take the next number from the range and assign it to `i`
> 2. Execute the code block
> 3. **Go to 1**, until the range runs out

- **Rules broken:** 8.
- **What a fellow gets wrong:** The steps never say what happens when the range runs out, so a fellow has to guess where execution goes after the loop.
- **Rewrite step 3:** "**Go to 1.** When the range has no numbers left, the loop ends and the program continues with the first line after the loop."

**8. `5-loops.md:175`**

> Run it a few times. The more flips you ask for, the closer the percentage gets to 50.

- **Rules broken:** 4. The sentence states a guarantee where the true rule is a tendency.
- **What a fellow gets wrong:** A fellow who sees 50% from 10 flips and 46% from 100 flips will think the code is broken.
- **Rewrite:** "Run it a few times. With 10 flips, the percentage jumps around a lot from run to run. With 100 flips, the percentage usually lands closer to 50."

**9. `5-loops.md:79`**

> In high-level programming languages like Python, that is abstracted away for us by the `for` loop.

- **Rules broken:** subject. "Abstracted away" is jargon, and "that" has no clear subject.
- **What a fellow gets wrong:** A fellow has to guess what the `for` loop does in place of the `GOTO`.
- **Rewrite:** "In Python, the `for` loop does that jump back to the top for you, so you never write the label or the `Go To` yourself."

**10. `5-loops.md:213`**

> You will see a `KeyboardInterrupt` message. That is Python telling you that you interrupted it, not that anything is wrong with your computer.

- **Rules broken:** 7 and subject.
- **What a fellow gets wrong:** The name `KeyboardInterrupt` is not broken into its parts, so the message stays cryptic to a fellow.
- **Rewrite:** "You will see a `KeyboardInterrupt` message. `KeyboardInterrupt` is Python reporting that you stopped the program from the keyboard. Nothing is wrong with your computer."

### 6-inputs-outputs.md

**1. `6-inputs-outputs.md:490`**

> `is_happy` has to be a boolean, but the user can only type a string.

- **Rules broken:** 2 and 3.
- **What a fellow gets wrong:** The passage says "has to be" without giving the consequence. The consequence ties directly back to chapter 4: `"N"` is truthy, so the story ends happily anyway. (I confirmed that `bool("N")` is `True`.)
- **Rewrite:** "`is_happy` has to be a boolean. The user can only type a string, and every non-empty string is truthy (chapter 4). If you passed their answer straight to `madlib`, typing `N` would still give the story a happy ending. Ask them to type `Y` or `N`, and turn their answer into `True` or `False`."

**2. `6-inputs-outputs.md:141`**

> A **method** is a function that is attached to a value. Often, methods are used to manipulate the value they are attached to.

- **Rules broken:** 3. The passage contradicts the immutability section just above it.
- **What a fellow gets wrong:** A fellow will believe that `message.upper()` changes `message`.
- **Rewrite:** "A **method** is a function that is attached to a value, and a method usually does something with that value. Strings are immutable, so a string method never changes the string it is called on. Methods like `upper()` and `replace()` return a new string instead."

**3. `6-inputs-outputs.md:120`**

> Python refuses. A string, once created, cannot be changed. If you want a different string, you make a new one, which is exactly what the string methods below do.

- **Rules broken:** 7 and 8.
- **What a fellow gets wrong:** The term "item assignment" in the error is never explained. The step of storing the new string is also missing, so a fellow will call `message.replace(...)` on its own line and expect `message` to change.
- **Rewrite:** "Python refuses. In the error, `'str' object` means the value is a string, and `item assignment` is the name for putting a value at an index with `message[0] = ...`. A string, once created, cannot be changed. If you want a different string, you make a new one and assign it to a variable, as in `message = message.replace("H", "J")`. Every string method below works this way: each one returns a new string and leaves the original alone."

**4. `6-inputs-outputs.md:163`**

> The methods `find` and `rfind` return a number representing the index of a particular character we're looking for. `rfind` searches from the right:

- **Rules broken:** 4 and 2.
- **What a fellow gets wrong:** After reading "searches from the right", a fellow may expect `rfind` to count the index from the right. The text also never warns that `-1`, the not-found result, is a valid index. (I confirmed that `'abc'['abc'.find('z')]` silently returns `'c'`.)
- **Rewrite:** "The methods `find` and `rfind` return the index of a character, or a longer piece of text, that you are looking for. `find` returns the index of the first match, and `rfind` returns the index of the last match. Both methods count the index from the left, the normal way. When there is no match, both methods return `-1`. Be careful with that `-1`: `-1` is also a valid index, so `fruits[fruits.find('z')]` quietly gives you the last character instead of an error."

**5. `6-inputs-outputs.md:224`**

> This is called **method chaining**, and it works because every one of these methods returns a string.

- **Rules broken:** subject and 4.
- **What a fellow gets wrong:** "Every one of these" includes `split` and `isdigit`, which return a list and a boolean. A fellow who chains onto either one gets a crash. (I confirmed the `AttributeError` for both.)
- **Rewrite:** "This is called **method chaining**. Method chaining works here because `strip()` returns a string, and `lower()` is a string method. You can only chain a method onto a call that returns the right type of value. `split()` returns a list, so `'a, b'.split(', ').lower()` crashes with an `AttributeError`."

**6. `6-inputs-outputs.md:443`**

> Between kinds of numbers, conversion happens on its own: `5 / 2` produces the float `2.5`, and `5 + True` produces `6` because `True` counts as `1` in arithmetic.

- **Rules broken:** 4.
- **What a fellow gets wrong:** `5 / 2` involves two integers, so no conversion between kinds of number takes place. A fellow learns the wrong rule. (I confirmed that `4 / 2` is `2.0` and `5 + 2.5` is `7.5`.)
- **Rewrite:** "Between kinds of numbers, conversion happens on its own. `5 + 2.5` turns the integer `5` into a float and produces `7.5`, and `5 + True` produces `6` because `True` counts as `1` in arithmetic. Division with `/` always produces a float, even between two integers, so `4 / 2` produces `2.0`."

**7. `6-inputs-outputs.md:357`**

> Users type messily. They add spaces, they use capitals when you expected lowercase. The string methods from earlier in this chapter clean that up,

- **Rules broken:** 2.
- **What a fellow gets wrong:** The text never says what messy input breaks, which is that the comparison fails. (I confirmed that `"YES" == "yes"` is `False`.)
- **Rewrite:** "Users type messily. They add spaces, and they use capitals when you expected lowercase. Python compares strings character by character, so `"YES" == "yes"` is `False`. The program below would tell a user who typed `YES` "Okay, see you later." The string methods from earlier in this chapter clean that up,"

**8. `6-inputs-outputs.md:335`**

> `.1f` keeps one digit after the decimal point. The same calculation, displayed for a human instead of for the computer.

- **Rules broken:** 4 and subject. The second sentence has no verb.
- **What a fellow gets wrong:** "Keeps" suggests that `.1f` cuts off the extra digits, when it actually rounds them. (I confirmed that `f"{58.36:.1f}"` produces `58.4`.) "For the computer" is also wrong, because both lines are printed for a person to read.
- **Rewrite:** "`.1f` rounds the number to one digit after the decimal point. Both lines print the same calculation. The second line shows only as many digits as a person reading a percentage needs."

**9. `6-inputs-outputs.md:299`**

> That is why f-strings are the way most Python programmers build a message: the words and the values sit in the order they will be printed, and you never have to convert anything yourself.

- **Rules broken:** 1 and 3.
- **What a fellow gets wrong:** "Never have to convert" only means something if the fellow has seen the alternative, building a message with `+`, which does need conversion. That alternative is not shown until line 427.
- **Rewrite:** "Like `print()` with commas, an f-string turns each value into text for you. Building the same message with `+` would need `"Your name has " + str(len(name)) + " letters."`, and forgetting the `str()` crashes the program (you will see that crash in Type Conversion below). Because of this conversion, f-strings are the way most Python programmers build a message: the words and the values sit in the order they will be printed, and you never have to convert anything yourself."

**10. `6-inputs-outputs.md:395`**

> Arithmetic and comparisons only make sense between values of the right type.

- **Rules broken:** 2.
- **What a fellow gets wrong:** "Make sense" and "the right type" are vague. The passage never says that both `age + 1` and `age >= 18` crash. (I confirmed the `TypeError` for both.)
- **Rewrite:** "Every value that comes out of `input()` is a string, even when the user typed a number. If `age` holds the string `"20"`, both `age + 1` and `age >= 18` crash with a `TypeError`, because Python will not do arithmetic or a `>=` comparison between a string and a number. Before you can write either one, you need to convert `age` to a number."

**11. `6-inputs-outputs.md:411`**

> That last line is why the `.isdigit()` method from earlier in this chapter exists: check the string before you convert it, and you can give the user a message instead of a crash.

- **Rules broken:** 6 and 3.
- **What a fellow gets wrong:** The causal claim that this crash is why `.isdigit()` exists is false. The passage also leaves out that `.isdigit()` rejects `" 20"`, `"-5"`, and `"4.2"`, even though `int(" 20")` works. (I confirmed all four.)
- **Rewrite:** "That last line is the crash that `.isdigit()` lets you avoid: check the string before you convert it, and you can give the user a message instead of a crash. `.isdigit()` is strict, though. It returns `False` for `" 20"` with a space in it, for `"-5"`, and for `"4.2"`. Strip the input first, and expect negative numbers and decimals to be rejected."

**12. `6-inputs-outputs.md:452`**

> A program is considered **hard-coded** if the program code must be modified in order to produce a new result.
>
> The `input()` function is really useful for creating programs that will produce new results depending on the user's input.

- **Rules broken:** 1 and 2.
- **What a fellow gets wrong:** The definition is given, but the problem it names is not. Nothing says who suffers or how.
- **Rewrite (second paragraph):** "In the program below, the only way to get a different story is to open `main.py` and edit the variables, which a friend playing your madlib cannot do. The `input()` function fixes that problem: the person running the program supplies the words, and every run can tell a new story."

### 7-lists.md

**1. `7-lists.md:175`**

> When a variable is created, a chunk of your computer's memory is assigned to hold some data. Small, immutable values like numbers can effectively be stored as-is. Lists and dictionaries however can grow to be any size and therefore cannot be contained within a single memory slot.

- **Rules broken:** 3. The "therefore" rests on a fixed slot size the page never states.
- **What a fellow gets wrong:** This is the JavaScript memory model, and it contradicts line 251 of the same chapter ("reassigning `y` to reference ... `11`"). It also contradicts `id()` and `is`, which work on integers too. (I confirmed that `x = 10; y = x; x is y` is `True`.) A fellow is given two incompatible pictures of memory.
- **Rewrite (replacing lines 175 and 177):** "Python stores every value in an area of memory called the **heap**, and a variable holds a **reference** to the value: its heap address. Think of the variable as a slip of paper with an address written on it, not as the house itself. For immutable values like numbers, the reference makes no visible difference, because nothing can change the number at that address. For a list, which can change, the reference matters a great deal, as you are about to see."

**2. `7-lists.md:255` (the impure function list) and `7-lists.md:285` ("To make a function that modifies a list pure, we need to make a copy of it first.")**

- **Rules broken:** 1 and 2.
- **What a fellow gets wrong:** The chapter never says why impurity is a problem. A fellow is asked to make copies to solve a problem nobody has shown them. The "if they:" list also leaves open whether a function needs both properties to count as impure, or just one.
- **Rewrite (insert before line 285):** "Why care? Whoever calls `empty_the_list(letters)` may only have wanted to use the list, and afterwards their `letters` is empty. The line that emptied `letters` is inside the function, so when the empty list causes a problem later, the line where the problem shows up is nowhere near the line that caused it. A pure function cannot surprise its caller this way, because it leaves its inputs alone and communicates only through what it returns." At line 255, write "if they do either of these:".

**3. `7-lists.md:126`**

> Lists are **mutable**: the list object itself can be changed while the variable keeps referencing it. ... Which values are mutable and which are not is one of the most important things to know about any type in Python.

- **Rules broken:** 4, 1, and 2.
- **What a fellow gets wrong:** The question asks why lists allow change, and "lists are mutable" restates the question. "Referencing" is used here before references are taught at line 177. "Most important" is a judgment with no stated consequence.
- **Rewrite:** "Strings are **immutable**: once a string is created, its characters cannot change, so the only way to get a different string is to make a new one and assign it to a variable. Lists are **mutable**: Python lets you change the elements inside an existing list, with bracket notation or with methods like `clear()`. Notice that we never reassign `end_letters`! The variable still points at the same list, and only the contents of that list changed. Whether a type is mutable decides whether a change made through one variable can show up through another variable, which is what the next section is about. Strings, numbers, booleans, and `None` are immutable. Lists and dictionaries are mutable."

**4. `7-lists.md:101`**

> Strings have read-only methods like `upper()` and slicing that make a copy of the string but don't change the original string.

- **Rules broken:** 2.
- **What a fellow gets wrong:** The consequence is missing. `my_name.upper()` on a line by itself appears to do nothing, because the new string is thrown away. A fellow will expect `my_name` to be `'BEN'`. (I confirmed that `my_name` is still `'ben'`.)
- **Rewrite:** "Strings have methods like `upper()`, and they support slicing, but both return a new string and leave the original alone. If you do not store the new string in a variable, the new string is gone: after `my_name.upper()` runs on its own line, `my_name` is still `'ben'`. Trying to change a string in place with bracket notation is an error."

**5. `7-lists.md:240` and `7-lists.md:251`**

> It is impossible for this behavior to occur when dealing with immutable values like strings, numbers, and booleans.
>
> In this example, even though it _looks_ like we're mutating the value `y`, we are NOT.

- **Rules broken:** subject, 3, and 4.
- **What a fellow gets wrong:** "This behavior" could mean either a function changing the caller's value or two variables seeing one change. The rule that makes it impossible is never stated: immutable values have no in-place operations, so only reassignment is possible, and reassignment affects only one variable.
- **Rewrite:** "A function can never change a caller's string, number, or boolean this way. Those values are immutable, so no method or bracket assignment can change them in place. The only way to "change" one is to reassign a variable, and reassignment changes only the variable on the left of the `=`." Then for line 251: "`y += 1` looks like it changes the value in `y`, but the number `10` cannot change. Python computes the new value `11` and reassigns `y` to reference it. `x` still references `10`."

**6. `7-lists.md:190`**

> As a result, we can mutate the contents of a list without reassigning the variable because the variable doesn't hold the list, it holds a reference to the list!

- **Rules broken:** 3 and 5.
- **What a fellow gets wrong:** "As a result" follows an `id()` demonstration that showed two names sharing one list, not mutation without reassignment. The real consequence of that demonstration, which the next example depends on, goes unsaid.
- **Rewrite:** "Because `nums` and `clone` hold the same reference, they are two names for one list. Anything you do to the list through one name shows up through the other name, as the next example shows."

**7. `7-lists.md:326`**

> Or, with a slice that leaves off the last element in the first place:

- **Rules broken:** 4.
- **What a fellow gets wrong:** The chapter has not taught a negative index as a slice end, so `[:-1]` is unexplained. The passage also never says that a slice builds a new list, which is the reason the solution is pure.
- **Rewrite:** "Or, with a slice that leaves off the last element in the first place. `items[:-1]` runs from the start of the list up to, but not including, index `-1`, which is the last element. A slice always builds a new list, so `items` is untouched."

**8. `7-lists.md:88` (a code comment inside the hidden answer)**

> # If we make it to the end of the loop, we must not have found it. Return False.

- **Rules broken:** 3.
- **What a fellow gets wrong:** "Must not have found it" depends on `return True` having ended the function on a match, and the comment never says so. This is the same gap as the guard clause in chapter 4.
- **Rewrite:** "# The return True above would have ended the function on a match, so reaching this line means no element matched. Return False."

**9. `7-lists.md:404`**

> The number of variables has to match the number of elements, unless one of the variables has a `*` in front.

- **Rules broken:** 2.
- **What a fellow gets wrong:** "Has to" is stated without saying what happens when the numbers do not match. (I confirmed both `ValueError` messages.)
- **Rewrite:** "The number of variables has to match the number of elements. If the numbers do not match, Python stops with a `ValueError`: `too many values to unpack` when the list has more elements than variables, and `not enough values to unpack` when it has fewer. The exception is a variable with a `*` in front. That variable collects "the rest" as a list:"

**10. `7-lists.md:95`**

> Python has this built in, of course: `value in items` does exactly what `has_value` does. But being able to write it yourself is the point.

- **Rules broken:** 2.
- **What a fellow gets wrong:** "The point" is asserted, not shown. A fellow may conclude the exercise was busywork.
- **Rewrite:** "Python has this built in, of course: `value in items` does exactly what `has_value` does. Writing it yourself still matters, because the same loop, check, and return shape answers questions `in` cannot, like "does this list contain any word longer than five letters?""

**11. `7-lists.md:364`**

> When accessing a 2D list, the first index references the "row" and the second index references the "column"

- **Rules broken:** 8.
- **What a fellow gets wrong:** The two-step evaluation of `coordinates[0][1]` is never spelled out. A fellow may picture a single operation that takes two numbers.
- **Rewrite:** "When accessing a 2D list, the first index picks the "row" and the second index picks the "column". Python reads `coordinates[0][1]` in two steps: `coordinates[0]` produces the row `[30, 90]`, and `[1]` then picks index 1 of that row, which is `90`."

**12. `7-lists.md:30`**

> Lists are lists of data (order matters). Values in a list are called **elements of the list**.

- **Rules broken:** 4. The definition is circular. "Encapsulate", on the next line, is jargon.
- **What a fellow gets wrong:** "Lists are lists" gives a newcomer nothing, and "order matters" is left without a meaning.
- **Rewrite:** "A list is a single value that holds several values in a particular order. The values in a list are called the **elements of the list**, and an element stays in its position until you move it. Lists use square brackets `[]` around their elements, separated by commas."

### Minor findings left out

- **4-conditional-statements.md:** 2 further minor findings (for example, line 99 says "only one statement will be executed" where it means one code block).
- **5-loops.md:** 2 further minor findings. One is that the solution at line 169 prints a format that differs from the format the challenge specifies.
- **6-inputs-outputs.md:** 8 further minor findings: the IndexError answer at 94, "the one conditions use without being asked" at 448, the prompt space at 355, "every `print()` starts on a new line" at 242, the case-sensitive `in` result at 153 that has no comment, float inexactness at 315, "`*` does what its name suggests" at 178, and `quantity` at 526.
- **7-lists.md:** 5 further minor findings: "source variable" at 386, "variables that hold them" at 171, "When the inner lists contain values" at 339, the errors from `remove` and `pop` at 145, and "can't return the same output" at 265.

### Patterns across the files

Explanations of why code behaves as it does routinely give the verdict and skip the rule that produces it. The clearest case is that "`return` ends the function" is missing from both the guard-clause answer in chapter 4 and the `has_value` comment in chapter 7.

Warnings routinely carry a judgment with no consequence: "order matters", "users type messily", "`None` versus `0`", "impure", "hard-coded", and "has to match". In each case the reader is never told what would go wrong.

Several sentences overstate a claim in a way that a later page contradicts:

- "methods manipulate the value"
- "every one of these methods returns a string"
- "`continue` prevents infinite loops"
- "`if` requires a boolean"
- "`5 / 2` is a conversion"

Two passages carry reasoning over from the JavaScript original that is false in Python. The first is the block-scope reason for `heads = 0` in chapter 5. The second is the claim in chapter 7 that numbers are stored as-is while lists are stored by reference.

The phrase "the one conditions use without being asked" appears in both chapter 4, line 144, and chapter 6, line 448.

Finally, a structural issue that sits outside the prose rules: the questions marked `???` at chapter 4, lines 71, 97, and 122 have no hidden answers. Chapter 4, line 122 matters most, because that example returns the wrong answer.

## Full findings: Mod 1: chapters 1.8 and 1.9

I did not edit either file. I ran every Python, venv and pytest behaviour that a rewrite below relies on in a scratch directory (Python 3.12.4, pytest 9.1.1), and each one behaved as the rewrite says.

### 8-dictionaries.md

**1. `8-dictionaries.md:183`**

> We can use the `dict()` function to copy the key-value pairs of one dictionary into a new dictionary. This is particularly useful when creating pure functions:

- **Rules broken:** 1, 3.
- **What goes wrong for the reader:** The passage gives the fix before the problem. It never says that a function which changes its parameter also changes the caller's dictionary, so a fellow cannot tell why "particularly useful" applies.
- **Rewrite:** "The same thing happens when you pass a dictionary to a function. The parameter holds a reference to the caller's dictionary, so if the function changes the parameter, it changes the caller's dictionary too, and the function is impure. To keep the function pure, have it copy the dictionary first. The `dict()` function copies the key-value pairs of one dictionary into a new dictionary, and the function can then change the copy as much as it likes:"

**2. `8-dictionaries.md:264`**

> `.keys()` does not return a list. It returns a `dict_keys` object, which you can loop over and check membership in, but cannot index with `[0]`. If you need a real list, wrap it in `list()`, which is what the third line does. `len()` on the dictionary itself counts the key-value pairs.

- **Rules broken:** 4, 2.
- **What goes wrong for the reader:** The chapter opens by saying that "Lists store values in an order", but this answer never states the rule that a dictionary keeps its keys in the order they were added. A fellow may therefore believe `'hello'` came first by luck. The answer also never shows what actually happens when you use `[0]` on a `dict_keys` object.
- **Rewrite:** "`.keys()` hands you a `dict_keys` object rather than a list, even though the printout looks like one. You can loop over a `dict_keys` object and use `in` with it. But if you try `dictionary.keys()[0]`, Python stops with `TypeError: 'dict_keys' object is not subscriptable`, which is Python's way of saying "you can't use square brackets on this". Wrapping it in `list()` builds a real list, and that is what the third line does. That list starts with `'hello'` because a dictionary remembers the order its keys were added in, and `"hello"` went in first. `len()` on the dictionary itself counts the key-value pairs: three pairs, so `3`."

**3. `8-dictionaries.md:132`**

> Because the key goes inside the brackets as an expression, it does not have to be typed out as a literal string. It can be a variable:

- **Rules broken:** 4, 8.
- **What goes wrong for the reader:** The passage leaves out the step that Python evaluates the variable and uses the value it holds. A fellow will mix up `my_dict[key]` and `my_dict['key']`, and the Solution at line 162 depends on knowing that difference.
- **Rewrite:** "The brackets can hold any expression, and Python works out its value before using it as the key. So the key can be a variable, and Python uses whatever value the variable holds: [code block]. Watch the quotes. `my_dict[key]` uses the value of the variable `key`, which is `'some key'`. `my_dict['key']` uses the three-letter string `'key'` itself."

**4. `8-dictionaries.md:199`**

> `animal.copy()` and `{**animal}` do the same thing as `dict(animal)`. You will see all three.

- **Rules broken:** 4. This is partly a gap in content.
- **What goes wrong for the reader:** The text never says that these three copy only the outer dictionary. A fellow who copies the chapter's own `user` and appends to `clone['friends']` changes the original's list too, and will believe the function is pure. I verified this.
- **Rewrite:** append "All three copy only the outer dictionary. If a value is a list or another dictionary, the copy and the original share that same list. `clone = dict(user)` followed by `clone['friends'].append('elmo')` adds `'elmo'` to `user['friends']` as well. To change a nested list inside a pure function, copy that list too: `clone['friends'] = list(user['friends'])`."

**5. `8-dictionaries.md:172`**

> And when we assign a variable holding a dictionary to another variable, each variable holds a reference to the same dictionary

- **Rules broken:** 2, 8.
- **What goes wrong for the reader:** The consequence appears only in a code comment. A fellow who sees a variable named `clone` will assume it is a copy.
- **Rewrite:** "And when we assign a variable holding a dictionary to another variable, both variables hold a reference to the same dictionary. No copy is made, so a change made through either variable shows up when you look through the other one:"

**6. `8-dictionaries.md:64`**

> Keys are usually strings, and the quotes around them are required. Keys can also be numbers, which will come in handy when you want to count things.

- **Rules broken:** 4, 2.
- **What goes wrong for the reader:** The passage says the quotes are required but not what happens without them. It also suggests that counting uses number keys. In a counting dictionary the counts are the values, and the example that follows (Roman numerals) is a lookup by number.
- **Rewrite:** "Keys are usually strings, and the quotes around them are required. Without quotes, Python reads `name` as a variable, and if no variable called `name` exists you get `NameError: name 'name' is not defined`. Keys can also be numbers, which comes in handy when you want to look something up by number, like a Roman numeral:"

**7. `8-dictionaries.md:74`**

> A key can be any value that cannot change: a string, a number, or a tuple. A list cannot be a key.

- **Rules broken:** 3, 4.
- **What goes wrong for the reader:** A fellow has to infer that lists are excluded because a list can change. They will not connect the real error, `TypeError: unhashable type: 'list'`, to this sentence.
- **Rewrite:** "A key has to be a value that cannot change: a string, a number, or a tuple. A dictionary finds a value by looking up its key, and a key that changed after it went in could no longer be found. A list can change, so a list cannot be a key. If you try, Python stops with `TypeError: unhashable type: 'list'`, and "unhashable" is Python's word for "not allowed as a key"."

**8. `8-dictionaries.md:331`**

> `introduce_self` never looks at `is_admin`, and it doesn't need to. A function that takes a dictionary only has to know about the keys it uses.

- **Rules broken:** 2.
- **What goes wrong for the reader:** The passage states the fact but not what it buys the programmer, or what breaks when one of those keys is missing.
- **Rewrite:** "`introduce_self` never looks at `is_admin`, and it doesn't need to. So `introduce_self` works on any dictionary that has a `"name"` and an `"age"`. You could pass it a user with twenty other keys, or add an `"email"` key to every user next week, and `introduce_self` would not need to change. What it does need is those two keys: pass it a dictionary without `"age"` and it stops with `KeyError: 'age'`."

**9. `8-dictionaries.md:297`**

> This one makes a user with the provided properties, `is_admin` set to `False`, and an empty `friends` list:

- **Rules broken:** subject/unit.
- **What goes wrong for the reader:** "This one" has no named subject. "Properties" is left over from the JavaScript original and is not a term this chapter teaches. The chapter's terms are keys and values.
- **Rewrite:** "The `make_user` function below builds a user dictionary that stores the `name` and `age` it is given, sets `is_admin` to `False`, and starts with an empty `friends` list:"

**10. `8-dictionaries.md:120`**

> You can also ask first. The `in` operator on a dictionary checks the _keys_:

- **Rules broken:** 2.
- **What goes wrong for the reader:** The italics hint at a consequence that the sentence never states. A fellow will try `"c0d3rkid" in user` and expect `True`.
- **Rewrite:** "You can also ask first. The `in` operator on a dictionary checks the _keys_ only, so `"username" in user` is `True` but `"c0d3rkid" in user` is `False`, even though `"c0d3rkid"` is one of the values:"

**11. `8-dictionaries.md:271`**

> The shape you will use more than any other is a list where every element is a dictionary with the same keys.

- **Rules broken:** 3.
- **What goes wrong for the reader:** The text never says why every dictionary needs the same keys.
- **Rewrite:** add after the code block: "Giving every dictionary the same keys is what makes the loop work. `user['name']` runs once for every dictionary in the list, so a single dictionary without a `"name"` key would stop the loop with a `KeyError`."

### 9-modules-environments-pytest.md

**1. `9-modules-environments-pytest.md:246`**

> This is usually fine, because most of what is in a module is `def` statements and defining a function is harmless. But it raises a question: what if a file is _both_ a program you sometimes run directly _and_ a module other files import? `main()` gets called at the bottom of `main.py`. If another file ever imported `main.py`, `main()` would run during the import, which is almost never what anyone wants.

- **Rules broken:** subject/unit, 4, 2.
- **What goes wrong for the reader:** "This" comes after a hint about `__pycache__`, so it could point at either the hint or the import. "Harmless" skips the rule that a `def` does not run the function body. "Almost never what anyone wants" is a judgment with no harm named, so the guard that follows reads as a ritual.
- **Rewrite:** "Running a module during the import is usually fine, because most of what is in a module is `def` statements, and a `def` statement only creates a function without running the code inside it. But what if a file is _both_ a program you sometimes run directly _and_ a module other files import? `main.py` ends with a call to `main()`. If another file imported `main.py` to reuse one function, `main()` would run during the import. The circle results would print in the middle of the other program's output. Worse, if that file were the madlib `main.py`, the person using the other program would suddenly be asked to `Choose a name:`."

**2. `9-modules-environments-pytest.md:603`** (the import line in the code that follows)

> Then, add the following code:

- **Rules broken:** 3, 8.
- **What goes wrong for the reader:** `from src.calc import add` uses folder-dot-module syntax that the chapter never teaches. Line 144 says only that a module's name is its filename, so a fellow has to guess what `src.` means.
- **Rewrite:** add after the code block: "The first line imports `add` from `src/calc.py`. When a module sits inside a folder, you write the folder name, a dot, and then the module name, so `src.calc` means "the `calc` module inside the `src` folder". Python starts looking from the folder you run the tests in, which is why the hint below says to run them from the project's root folder."

**3. `9-modules-environments-pytest.md:646`**

> Running it through `python3 -m` adds the current folder to that list, and the import works. Use `python3 -m pytest`, from the project's root folder, every time.

- **Rules broken:** 3.
- **What goes wrong for the reader:** "From the project's root folder" has no stated reason. A fellow who runs the command from inside `tests/` gets `ModuleNotFoundError` again and will not know why. I verified that this fails.
- **Rewrite:** "Running it through `python3 -m` adds the folder you are in to that list. The project's root folder, `9-testing/`, contains `src/`, so from there `from src.calc import add` works. If you `cd tests` first, Python adds `tests/` instead, finds no `src` there, and you are back to `ModuleNotFoundError`. So run `python3 -m pytest` from the project's root folder every time."

**4. `9-modules-environments-pytest.md:96`**

> As a project grows in scale and complexity, **separation of concerns** becomes increasingly important.

- **Rules broken:** 1, 2.
- **What goes wrong for the reader:** A fellow is looking at a 30-line file that works and is told to split it, without hearing what goes wrong if they don't.
- **Rewrite:** "This file is short enough to read in one go. Now imagine it with fifty circle functions, a dozen display helpers, and the code that ties them together. To fix a wrong area, you would scroll past all of the display code to find `get_area`. Two teammates fixing different things would be editing the same file at the same time. As a project grows, **separation of concerns** is what keeps it manageable."

**5. `9-modules-environments-pytest.md:144`**

> To use a module's names, use the `import` statement. A module's name is its filename without the `.py`.

- **Rules broken:** 8.
- **What goes wrong for the reader:** The passage leaves out where Python looks for the file. A fellow who puts `display.py` in another folder gets `ModuleNotFoundError` with nothing in the text to explain it. I verified that this fails.
- **Rewrite:** append "When you run `python3 main.py`, Python looks for `circle_helpers.py` and `display.py` in the same folder as `main.py`, so keep the three files side by side. Move `display.py` into a different folder and `from display import display` stops with `ModuleNotFoundError: No module named 'display'`."

**6. `9-modules-environments-pytest.md:418`**

> If you ever get a `ModuleNotFoundError` for a package you are sure you installed, look at the prompt before you do anything else. Nine times out of ten, `(.venv)` is missing. From now on, in this Terminal window, `python3` and `pip` refer to the copies inside `.venv`:

- **Rules broken:** 1, 3.
- **What goes wrong for the reader:** The troubleshooting tip comes before the fact that explains it, so "`(.venv)` is missing" reads as a superstition rather than a cause.
- **Rewrite:** "Your Terminal prompt changes to show `(.venv)` at the front. That is how you know it is on. From now on, in this Terminal window, `python3` and `pip` refer to the copies inside `.venv`: [code block]. Because of that, a package you install with the environment on lives only inside `.venv`. If you ever get a `ModuleNotFoundError` for a package you are sure you installed, look at the prompt before you do anything else. Nine times out of ten, `(.venv)` is missing, which means `python3` is your computer's own Python, and that Python has never had the package installed."

**7. `9-modules-environments-pytest.md:564`**

> With manual testing, you're always left with this question. You've spent time and effort to create the tests so deleting them is wasteful, but we can't just leave them in our code because they add clutter.

- **Rules broken:** 2, subject/unit.
- **What goes wrong for the reader:** "The tests" are never named; in manual testing they are the `print()` calls. "Clutter" is a judgment with no consequence, and the obvious consequence connects to the import lesson earlier in the same chapter.
- **Rewrite:** "With manual testing, your tests are the `print()` calls you added to check each function, and you're always left with this question. You've spent time and effort writing them, so deleting them is wasteful. But if you leave them in, they run every time the program runs, and, as you saw earlier in this lesson, every time another file imports that file. Whoever runs the program sees your check results mixed in with its real output and has no idea what they mean."

**8. `9-modules-environments-pytest.md:748`**

> `1` is truthy, but it is not the boolean `True`. A function named `is_even` promises a boolean, and `is True` is the assertion that holds it to that promise.

- **Rules broken:** 2.
- **What goes wrong for the reader:** The answer ends on a judgment ("holds it to that promise") without saying what the broken function would do to a user, so `is` looks like a technicality.
- **Rewrite:** "`1` is truthy, but it is not the boolean `True`. That difference shows up as soon as someone uses the function: `print(f"Is 4 even? {is_even(4)}")` prints `Is 4 even? 1`, and whoever reads that has to guess what `1` means. A function named `is_even` promises a boolean. The `==` version lets the broken function pass, and the `is True` version catches it." I verified that the f-string prints `1`.

**9. `9-modules-environments-pytest.md:552`**

> `pytest` makes it easier to check that your code works, but the functionality of the program is not changed by it. Someone who just wants to _run_ your program never needs it. It is a convenience for developers.

- **Rules broken:** 4, 6.
- **What goes wrong for the reader:** The passive "is not changed by it" hides the concrete rule a fellow could check for themselves: no file in `src/` imports `pytest`.
- **Rewrite:** "Only the files in `tests/` import `pytest`. The files in `src/` that make up the program never do, so someone who just wants to _run_ your program can do it without `pytest` installed. `pytest` serves the people building the program."

**10. `9-modules-environments-pytest.md:382`**

> `open()` is a built-in that opens a file, and the `with` statement closes it again when the indented block ends.

- **Rules broken:** 8.
- **What goes wrong for the reader:** The `"w"` is never explained, and the second `open()` leaves it out. A fellow has to guess what `"w"` means and why it disappears.
- **Rewrite:** "`open()` is a built-in function that opens a file. The `"w"` means "open it for writing": it creates `tasks.json` if the file does not exist and replaces whatever was in it if it does. The second `open()` has no `"w"`, so it opens the file for reading, which is what `open()` does by default. The `with` statement closes the file again when the indented block ends." I verified that `"w"` replaces the contents and that the default mode is `r`.

**11. `9-modules-environments-pytest.md:108`**

> Every name assigned at the top level of a file, meaning every function and every variable that is not indented inside something else, can be imported by another file. / So we can move the `display` function into its own file:

- **Rules broken:** 3.
- **What goes wrong for the reader:** The "So" skips the link between the two sentences: `main.py` can import the function back after it moves.
- **Rewrite:** "...can be imported by another file. That means a function can leave `main.py` and `main.py` can still call it, by importing it back. So we can move the `display` function into its own file:"

**12. `9-modules-environments-pytest.md:215`**

> Importing a file **runs it**, top to bottom, exactly as if you had typed `python3 circle_helpers.py`.

- **Rules broken:** 4 (the rule is stated imprecisely).
- **What goes wrong for the reader:** "Exactly as if" is contradicted 35 lines later by `__name__`, and a second import does not run the file again (verified). A fellow who sees `__name__` differ may conclude that they misread this sentence. In the same block, line 235 says `import circle_helpers` is "on line 1 of `main.py`", but the numbered listing shows it on line 2.
- **Rewrite:** "Importing a file **runs it**, top to bottom, the first time it is imported, almost exactly as if you had typed `python3 circle_helpers.py`. The one difference is a variable called `__name__`, which is coming up shortly." Also change "line 1" to "line 2" at line 235.

**Factual notes outside the clarity rules, found while checking claims:**

- **Lines 491 and 540:** these lines say `.venv` "contains a copy of Python" and is "often hundreds of megabytes". On macOS, `.venv/bin/python3` is a symbolic link (a pointer to the computer's own Python, not a copy of it). A `.venv` with only `pytest` installed measured 30 MB. The argument that `.venv` is specific to your machine still holds, and the link makes it stronger: the link points at a path that exists only on your computer.
- **Line 243:** this line names `circle_helpers.cpython-314.pyc`, but the pytest output shown later reports Python 3.12.4, which writes a file named `cpython-312.pyc`.

### Findings left out

- **8-dictionaries.md:** I left out 3 further minor findings.
- **9-modules-environments-pytest.md:** I left out 6 further minor findings.

**Pattern across both files:** Explanations of _why_ tend to stop at a verdict word ("particularly useful", "harmless", "almost never what anyone wants", "clutter", "holds it to that promise", "doesn't need to") without saying what a fellow or a user would see go wrong. Several passages also give the solution before the problem: `dict()` before the mutation problem, separation of concerns before any pain, and the `.venv` troubleshooting tip before the mechanism behind it. A third pattern is that code which introduces new syntax often comes without a sentence for that syntax, so the reader has to guess at it: `src.calc`, `"w"`, a variable inside brackets, and where Python looks for an imported file.

## Full findings: Mod 1: chapters 1.10 and 1.11

I reviewed both files and edited neither. I checked every behaviour claim below with Python 3.12.4 in a scratch folder, and checked the pytest output with pytest installed in a scratch virtual environment. Several of the findings are factual errors, not only clarity problems, and I have marked those **[accuracy]**.

### 10-reading-unfamiliar-code.md

**1. `10-reading-unfamiliar-code.md:238` [accuracy]**

> `restock("eggs", 12)` is where `stock.get(name, 0)` earns its place. `"eggs"` is not in the dictionary, so `.get` returns the default `0`, and `0 + 12` becomes the new entry. Without the default, this line would have raised a `KeyError` on any new item.

- **Rules broken:** 1, 2, and the plain-vocabulary rule ("earns its place" is the same idiom as "earns its keep").
- **What a fellow would get wrong:** the passage gives its verdict first and the problem last. The problem it names is also wrong. `stock.get(name) + 12` with no default raises `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. Only bracket notation, `stock["eggs"] + 12`, raises `KeyError`.
- **Rewrite:** "`sell("eggs", 1)` is `False` because of the first guard clause: `"eggs"` is not a key in `stock`. `restock("eggs", 12)` shows why the author used `.get`. If the line used bracket notation, `stock["eggs"]` would raise a `KeyError`, because `"eggs"` is not in the dictionary yet, and restocking any new item would crash. `stock.get(name, 0)` returns its default, `0`, when the key is missing. So `0 + 12` becomes the new entry, and `restock` returns `12`."

**2. `10-reading-unfamiliar-code.md:197` [accuracy]**

> It is a tradeoff the author made, and you can name both sides of it. Keeping `stock` inside `inventory.py` and never importing it into `main.py` means only three functions can ever touch it, which makes it easy to find every place it changes. The cost is that `restock` and `sell` are impure: calling `sell("apples", 1)` twice gives different results. The case study in two weeks makes the same choice for the same reason, and you will make it in your project too. Knowing the cost is what matters.

- **Rules broken:** 1, 2, 8.
- **What a fellow would get wrong:** they would run the example and find that it disproves the claim. `sell("apples", 1)` returns `True` both times. The answer also gives the benefit before the problem, never says what "impure" costs a reader, and never answers "Is this program wrong?". The summary line says "Chapter 2 told you to avoid that", but that warning is in chapter 3, in the section "The `global` Keyword".
- **Rewrite:** "No, but the author paid a price for it, and you should be able to name the price. Chapter 3 warned that a function which changes a variable outside itself is a function whose behaviour you cannot predict by reading it. `sell` is that kind of function: `sell("bread", 2)` returns `True` the first time and `False` the second, because the first call used up the bread. To predict what `sell` returns, you need its arguments and also what `stock` holds at that moment. The author accepted that cost to get one benefit. `main.py` never imports `stock`, so the only code that changes it is the three functions in `inventory.py`, and when the stock is wrong you know exactly where to look. The case study in two weeks makes the same trade, and so will your project."
- **Also:** the summary line should say "Chapter 3".

**3. `10-reading-unfamiliar-code.md:370` [accuracy]**

> There is a third if you look: `int(answer)` on line 13 crashes on a tip like `15.5`.

- **Rules broken:** 4.
- **What a fellow would get wrong:** they would look at line 13 and find `else:`. The call `int(answer)` is on line 14. The passage also states the crash without the rule that causes it.
- **Rewrite:** "There is a third if you look: `int(answer)` on line 14 crashes on a tip like `15.5`. `int()` only converts strings that look like whole numbers, and for anything with a decimal point it raises `ValueError: invalid literal for int() with base 10: '15.5'`."

**4. `10-reading-unfamiliar-code.md:363`**

> There is no top-level data at all, which is why this program can be pure where the shop could not: `split_bill(100, 4)` returns `29.5` every single time.

- **Rules broken:** 3 and subject/unit.
- **What a fellow would get wrong:** "which is why" skips the premise that a function's result depends only on its arguments when it reads nothing from outside itself. "This program" is also not pure, because `main` calls `input()`. The pure function is `split_bill`. "Could not" contradicts finding 2, which calls the shop's design a choice.
- **Rewrite:** "**The data:** three numbers, none of them remembered between runs. `split_bill` reads nothing except its own parameters, so its result depends only on the arguments you pass it: `split_bill(100, 4)` returns `29.5` every single time. That makes `split_bill` pure. The shop's `sell` was not pure, because its result also depended on what `stock` held at the moment you called it."

**5. `10-reading-unfamiliar-code.md:193`**

> There is exactly one piece of data that lives between actions: `stock`, at the top of `inventory.py`. Its shape is a dictionary from item name (a string) to quantity (an int). Everything the program does is a change to, or a report on, that one dictionary.

- **Rules broken:** subject/unit.
- **What a fellow would get wrong:** "lives between actions" is undefined. `choice`, `name` and `quantity` are also data, so a fellow would wonder why they do not count.
- **Rewrite:** "Only one piece of data keeps its value from one menu choice to the next: `stock`, at the top of `inventory.py`. The other variables (`choice`, `name`, `quantity`) get new values every time the loop goes around. `stock` is a dictionary from item name (a string) to quantity (an int), and everything the program does either changes that dictionary or reports on it."

**6. `10-reading-unfamiliar-code.md:299`**

> `input()` returns a string, so `choice` is `"2"`, and `"2" == 2` is `False`. Every branch fails and the `else` runs.

- **Rules broken:** 4.
- **What a fellow would get wrong:** the passage gives the result but not the rule. A fellow could think `"2" == 2` is a special case, not that a string is never equal to a number.
- **Rewrite:** "`input()` always returns a string, so when you type `2`, `choice` holds `"2"`. Python never treats a string as equal to a number, even when the two look the same, so `"2" == 2` is `False`. Every `if` and `elif` compares `choice` to a number, so every comparison is `False` and the `else` runs. The function is perfectly readable, perfectly plausible, and useless. Either compare against `"1"`, `"2"`, `"3"`, or convert `choice` with `int()` first. If you convert it, add a guard too, because `int("abc")` crashes."

**7. `10-reading-unfamiliar-code.md:374`**

> `tip_percent=18` is a default parameter value from chapter 3, and the `if answer == ""` branch exists only to leave it out so the default is used. That is the author telling you what the normal case is.

- **Rules broken:** 6 and subject/unit ("it" means the argument, and the verb is "exists").
- **What a fellow would get wrong:** they would have to work out for themselves that "leave it out" means calling `split_bill` with two arguments.
- **Rewrite:** "**Something to notice:** `tip_percent=18` is a default parameter value from chapter 3. When the user presses Enter without typing a tip, the `if answer == ""` branch calls `split_bill(total, people)` with only two arguments, and Python fills in `tip_percent` with `18`. The default value is the author telling you what they expect most people to tip."

**8. `10-reading-unfamiliar-code.md:176`**

> Everything you read from here on has to agree with that sentence, or one of them is wrong.

- **Rules broken:** subject/unit and 2.
- **What a fellow would get wrong:** "one of them" could mean the sentence, the code, or the reader's reading of the code. Nothing says what to do when they disagree.
- **Rewrite:** "Everything you read from here on has to agree with that sentence. If the code seems to do something the sentence does not describe, then either your sentence is wrong because you have not tried enough inputs, or your reading of the code is wrong. Running the program again will tell you which."

**9. `10-reading-unfamiliar-code.md:271`**

> Marcy's [AI policy](../guidelines-and-policies/ai-policy.md) asks what job you gave the model. Code that a model wrote and you read, take apart, and never put in your own file is reading practice, and reading practice is the job you are here for. What the policy forbids is that code ending up in your submission.

- **Rules broken:** 1 and 8.
- **What a fellow would get wrong:** the link between "what job you gave the model" and "reading practice" is missing, so the first sentence reads as unrelated to the second.
- **Rewrite:** "Marcy's [AI policy](../guidelines-and-policies/ai-policy.md) does not ask whether you used a model. It asks what job you gave the model. Ask a model for code that you then read and take apart, without copying it into your own file, and the job you gave it is producing reading practice, which is what this chapter is for. The policy forbids a different job: code the model wrote ending up in your submission."

**10. `10-reading-unfamiliar-code.md:250`**

> `abc` fails `.isdigit()`, prints `Please enter a whole number.`, and hits `continue`.

- **Rules broken:** 6.
- **What a fellow would get wrong:** the sentence makes the input `abc` the thing that prints and hits `continue`. A fellow tracing actors would have to supply the real one, which is the program.
- **Rewrite:** "When you type `abc`, `.isdigit()` returns `False`, so the program prints `Please enter a whole number.` and reaches `continue`."

**11. `10-reading-unfamiliar-code.md:77`**

> Then check, either by reading the body closely or by importing the module in the REPL and calling the function.

- **Rules broken:** 3 (it conflicts with a premise elsewhere on the page).
- **What a fellow would get wrong:** Step 6 (line 83) says to move a belief to "know" "only when you have checked them by running code". A fellow would not know whether reading the body counts as checking.
- **Rewrite:** "Then check it by importing the module in the REPL and calling the function with that input. Reading the body closely helps you make a better prediction, but only running the function tells you whether the prediction was right."

**12. `10-reading-unfamiliar-code.md:73` [accuracy]**

> This is the same thing you did with the debugger in chapter 3.

- **Rules broken:** 3 (the premise is not on any page).
- **What a fellow would get wrong:** chapter 3 never uses the debugger. The only mention in Mod 1 before this chapter is one sentence in chapter 5 (line 72), so a fellow would go looking for a lesson that does not exist.
- **Rewrite:** "You can do this with the debugger, too. Put a breakpoint at the start of `main()` and step through, and the debugger shows you each line in the order Python runs it."

### 11-errors-tracebacks.md

**1. `11-errors-tracebacks.md:412` and `:421` [accuracy]**

> Delete the `raise` line from `withdraw` so that it quietly allows the overdraft, and run the tests again.
>
> `test_withdraw` still passes, and `test_withdraw_overdraft` fails. The function no longer does what the test says it should, and pytest tells you exactly which promise it broke.

- **Rules broken:** 3, 4, and 8 in the answer.
- **What a fellow would get wrong:** a fellow who follows the instruction exactly leaves `if amount > balance:` with no body. pytest then reports `IndentationError: expected an indented block after 'if' statement on line 2` and `1 error during collection`, not `DID NOT RAISE`. I ran this to confirm. The answer also never says why `test_withdraw` still passes.
- **Rewrite of the prompt:** "Delete the `if` statement from `withdraw` (both the `if` line and the `raise` line beneath it) so that it quietly allows the overdraft, and run the tests again."
- **Rewrite of the answer:** "`test_withdraw` still passes, because `withdraw(100, 30)` never reached the `raise` anyway: 30 is not more than 100. `test_withdraw_overdraft` fails, because `withdraw(100, 500)` now returns `-400` instead of raising, and `pytest.raises(ValueError)` requires the indented block to raise. `DID NOT RAISE ValueError` names exactly the behaviour the function lost. Put the `if` statement back before moving on."

**2. `11-errors-tracebacks.md:372` [accuracy]**

> `.isdigit()` only accepts strings made entirely of digits, so it rejects `-5` and `5` even though `int()` would happily convert both. The `try`/`except` version lets `int()` be the judge of what it can convert, which is exactly the right judge. Use `.isdigit()` when you specifically want non-negative whole numbers with no surprises; use `try`/`except` when you want "whatever `int()` accepts."

- **Rules broken:** 2 and 4.
- **What a fellow would get wrong:** `"5".isdigit()` is `True`, so a fellow who tests the claim finds it false. The intended example was probably `" 5"`, with a space in front. "No surprises" is also untrue: `"²".isdigit()` is `True`, but `int("²")` raises `ValueError`.
- **Rewrite:** "`.isdigit()` answers a different question from the one you care about. `.isdigit()` asks whether every character is a digit, so it returns `False` for `-5` and for ` 5` (with a space in front), even though `int()` converts both without complaint. The question you care about is whether `int()` can convert the string, and the `try`/`except` version asks `int()` directly. Use `.isdigit()` when you want only digits, with no minus sign; use `try`/`except` when you want whatever `int()` accepts."

**3. `11-errors-tracebacks.md:286`**

> It saves function calls in a last-in-first-out (LIFO) order which means that the most recent function call is always on top, followed by the function that called it, and so on. A traceback is a printout of the call stack at the moment the error was raised.

- **Rules broken:** 3 and 8.
- **What a fellow would get wrong:** two sentences earlier, line 261 says the most recent call is at the _bottom_ of the traceback. A fellow told that a traceback "is a printout of" a stack with the most recent call "on top" would see a contradiction, and nothing on the page resolves it.
- **Rewrite:** "The **call stack** is a list the interpreter keeps of every function call that has started and not yet finished. When a function is called, Python adds it to the top of the stack, and when the function returns, Python removes it. The last call added is the first one removed, which is called last-in-first-out (LIFO). A traceback is a printout of the call stack at the moment the error was raised, printed with the top of the stack at the bottom. That is why a traceback says `most recent call last`."

**4. `11-errors-tracebacks.md:350`**

> A bare `except:` with no type catches everything, including mistakes you would rather know about, so name the type.

- **Rules broken:** 2.
- **What a fellow would get wrong:** "mistakes you would rather know about" is a judgment. A fellow cannot picture what the bare `except:` would hide, or what they would wrongly believe as a result.
- **Rewrite:** "A bare `except:` with no type catches everything, including your own mistakes. If you misspelled `items` as `itmes` inside the `try`, Python would raise a `NameError`, and a bare `except:` would catch it. The program would print `Oops!` and carry on, and you would believe the input was the problem when the real problem was a typo. With `except AttributeError`, the typo crashes with a traceback that points straight at it, so name the type."
- **Verified:** the bare `except:` prints the message, and `except AttributeError` lets the `NameError` through.

**5. `11-errors-tracebacks.md:368`**

> The `return` inside the `try` ends the loop and the function the moment the conversion succeeds. If it fails, the `except` prints a message and the `while True` asks again.

- **Rules broken:** 4 and subject/unit ("it").
- **What a fellow would get wrong:** a fellow would wonder why the `return` does not run when the conversion fails. The rule that Python skips the rest of the `try` block is never stated. Neither is the rule that `return` ends the function even from inside a loop.
- **Rewrite:** "If `int(answer)` succeeds, `return` hands the number back. `return` ends the function immediately, so it ends the `while True` loop along with it. If `int(answer)` raises a `ValueError`, Python skips the rest of the `try` block, so the `return` never happens, and jumps to the `except` block, which prints a message. The loop then goes around again and asks for another answer."

**6. `11-errors-tracebacks.md:254`**

> The first line says it: `most recent call last`. A traceback is printed in the order the calls happened, so the place where the error actually occurred is at the **bottom**.

- **Rules broken:** 3 and subject/unit.
- **What a fellow would get wrong:** "it" has no referent. The "so" also skips the step that the error happens inside the call that started last.
- **Rewrite:** "The first line of the traceback tells you how to read it: `most recent call last`. Python lists the calls in the order they started, so `main()` comes first and `cause_trouble` comes last. The error happened inside the last call that started, so the line that actually failed is at the **bottom**."

**7. `11-errors-tracebacks.md:305`**

> `85.0` prints first, because the first call works. Then the traceback names line 2, `ZeroDivisionError: division by zero`. `len([])` is `0`.
>
> If you said line 6, you pointed at the call that _caused_ the problem rather than the line where the error _occurred_. Both appear in the traceback. The bottom one is where Python was standing when it gave up, and it is usually where the fix goes, or where you learn that the caller sent something the function never expected.

- **Rules broken:** 4 and 8.
- **What a fellow would get wrong:** "`len([])` is `0`" leaves out that `sum([])` is also `0` and that Python does not allow dividing by zero. The last sentence leaves the fellow unsure where the fix belongs.
- **Rewrite:** "`85.0` prints first, because the first call works. Then the traceback names line 2, with `ZeroDivisionError: division by zero`. For an empty list, `sum([])` is `0` and `len([])` is `0`, so line 2 computes `0 / 0`, and Python does not allow dividing by zero. If you said line 6, you named the line that passed in the empty list rather than the line where the error occurred. Both lines appear in the traceback: line 6 is higher up, as the call from `main`, and line 2 is at the bottom, as the line Python was running when it raised the error. Start your investigation at the bottom line. Then decide where the fix belongs: either `average` should handle an empty list itself, or `main` should never have passed one."

**8. `11-errors-tracebacks.md:378` and `:387`**

> A function that is handed a value it cannot work with should say so loudly rather than carry on and produce nonsense:
>
> … Either way, the failure happens where the mistake is, with a message that says what went wrong, instead of three functions later with a confusing one.

- **Rules broken:** 1 and 2.
- **What a fellow would get wrong:** "nonsense" and "a confusing one" are judgments. The fellow never sees what `withdraw` would actually do without the check.
- **Rewrite of line 378:** "Without a check, `withdraw(100, 500)` returns `-400`, and nothing complains. The program carries on with a balance of -400 dollars, and the problem shows up later, perhaps as a negative number on a statement, in a function far away from the mistake. A function that is handed a value it cannot work with should raise an error straight away instead:"
- **Rewrite of line 387:** "The caller can then choose to catch the `ValueError` or let it crash the program. Either way, the program stops on the line where the bad withdrawal happened, with a message that names both the amount and the balance."

**9. `11-errors-tracebacks.md:409`**

> It is the same `with` statement that opened files in chapter 9: it sets something up, runs the indented block, and then checks what happened.

- **Rules broken:** 8.
- **What a fellow would get wrong:** chapter 9 (line 382) teaches that `with` _closes_ the file. "Checks what happened" does not describe what `with` did there, so the comparison does not hold.
- **Rewrite:** "It is the same `with` statement that opened files in chapter 9. A `with` statement sets something up, runs the indented block, and then does a finishing step when the block ends. For `open()`, the finishing step closes the file. For `pytest.raises`, the finishing step checks whether the block raised a `ValueError`."

**10. `11-errors-tracebacks.md:205` [accuracy]**

> When you learn `pytest` at the end of this module, every failing test will be one of these.

- **Rules broken:** 3 (the premise is false).
- **What a fellow would get wrong:** pytest was taught in chapter 9, and this same chapter uses the `9-testing` project at line 391. A fellow would think there is a second pytest lesson still to come.
- **Rewrite:** "Every failing test you wrote with `pytest` in chapter 9 failed with one of these."

**11. `11-errors-tracebacks.md:186`**

> Python raises these when an application violates an operating system constraint.

- **Rules broken:** subject/unit and the plain-vocabulary rule.
- **What a fellow would get wrong:** a fellow new to programming has no idea what "an operating system constraint" is.
- **Rewrite:** "Python raises these when your program asks the operating system to do something with a file, a folder, or a network connection, and the operating system refuses. For example, `open()` raises a `FileNotFoundError` when you ask for a file that does not exist."

**12. `11-errors-tracebacks.md:93`**

> A runtime error, by contrast, only happens when the program reaches the broken line, so everything before it runs first. That difference is the fastest way to tell which kind of error you are looking at.

- **Rules broken:** 8.
- **What a fellow would get wrong:** the passage never says how to use the difference, meaning what to look for in the output.
- **Rewrite of the last sentence:** "So when you see an error, look at what printed before it. If lines above the broken one should have printed something and nothing printed, the error is a syntax error. If those earlier lines printed, Python got as far as running the file, and the error is a runtime error."

### Further minor findings left out

- **10-reading-unfamiliar-code.md:** I left out 4 further minor findings. They include line 49 ("the whole skill in miniature" is a judgment with no consequence) and line 67 ("those questions have short answers" gives no reason).
- **11-errors-tracebacks.md:** I left out 5 further minor findings:
  - Line 41 says "An error is any code…", but an error is not code.
  - Line 104 says syntax errors are "almost always indicative of a broken program".
  - Line 177 says "Exactly what it says".
  - Line 283 says "where the bad value came from" without naming line 7 of `main.py`.
  - Line 113 says "specific to Python", which is the kind of language-contrast disclaimer your memory notes ask to avoid.

### Pattern across both files

Hidden answers often state a result without the rule that produces it, for example "`"2" == 2` is `False`", "crashes on a tip like `15.5`" and "`len([])` is `0`". They also give a judgment such as "earns its place", "nonsense", "impure" or "mistakes you would rather know about" before, or instead of, the problem it refers to. The more serious pattern is that the hidden answers and cross-references contain factual errors that a fellow who runs the code will catch. There are wrong chapter numbers (2 for 3, 3 for 5, "end of this module" for chapter 9), a wrong line number (13 for 14), and wrong Python behaviour (`KeyError` for `TypeError`, `"5".isdigit()`, `sell("apples", 1)` twice). There is also an instruction that produces an `IndentationError` instead of the output it promises. These sections teach "predict, then run", so each of these errors undermines the habit the chapter is building. The hidden answers in the rest of the module are worth an accuracy pass of their own.

## Full findings: Mod 1: chapters 1.12 and 1.13

### 12-first-class-functions-hof.md

**1. `12-first-class-functions-hof.md:343`**

> Read the order of events carefully, because three functions are involved and only one of them runs at the end: … 3. `loud_greet("Maya")` calls `wrapper`, which prints a line, calls `func("Maya")`, and prints another line.

- **Rules broken:** 3, 8, and subject/unit.
- **What a fellow gets wrong:** Chapter 3 (3-functions.md:32) teaches that a parameter "exists only while that function is running". `announce` has already returned by step 3, so a fellow has to guess how `wrapper` can still reach `func`. A fellow may also decide that the lesson in chapter 3 was wrong. The phrase "only one of them runs at the end" is also false, because step 3 runs both `wrapper` and `greet`.
- **Proposed rewrite:** "Read the order of events carefully, because three functions are involved and they do not all run at the same time: … 3. `loud_greet("Maya")` calls `wrapper`, which prints a line, calls `func("Maya")`, and prints another line. Step 3 should surprise you. Chapter 3 said a parameter exists only while its function is running, and `announce` finished running back in step 2. So how does `wrapper` still have `func`? A function defined inside another function keeps access to the outer function's variables, even after the outer function has returned. `wrapper` was created inside `announce`, so `wrapper` carries `func` along with it, and `func` still references `greet`."
- I checked this with `python3`: `loud_greet.__closure__` holds `greet`.

**2. `12-first-class-functions-hof.md:234`**

> When you invoke `execute_callback(say_hello())`, the `say_hello()` function call gets resolved first. Since `say_hello()` returns `None`, that is what `execute_callback` gets as its callback:

- **Rules broken:** 4 and 7.
- **What a fellow gets wrong:** The question asks why the message says `'NoneType' object is not callable`. The answer never says that `NoneType` is the type of `None` or that "callable" means "can be called with `()`". The answer also never states the rule that Python evaluates every argument before it calls the function, so the words "gets resolved first" have to be taken on trust.
- **Proposed rewrite:** "Python evaluates every argument before it calls a function. So in `execute_callback(say_hello())`, Python runs `say_hello()` first. `say_hello` prints `hello world` and, because it has no `return` statement, returns `None`. That `None` is what `execute_callback` receives as `callback`: [code block unchanged]. The error message names both halves of the problem. `'NoneType'` is the type of `None`, so `'NoneType' object` means "the value `None`". `is not callable` means that value cannot be called with `()`. When `execute_callback` reaches `callback()`, it is asking Python to call `None`, and Python refuses."
- I checked the message with `python3`. It is exactly `'NoneType' object is not callable`.

**3. `12-first-class-functions-hof.md:425`**

> Store the call's value in `result`, print the closing line, then return it. Without the last `return`, `wrapper` returns `None` and the original return value is lost.

- **Rules broken:** 1 and 3.
- **What a fellow gets wrong:** Most fellows will write `return func(name)`. The solution never says why that version is wrong, so the `result` variable looks like a matter of style.
- **Proposed rewrite:** "The tempting fix is `return func(name)`, but a `return` statement ends `wrapper` on the spot, so `--- finished ---` would never print. Instead, store the wrapped function's return value in `result`, print the closing line, and only then return `result`. Without that last `return`, `wrapper` reaches its end with no `return` statement, so it returns `None`, and `loud_shout("Maya")` gives back `None` instead of `HI, MAYA!`."
- I checked this with `python3`: with an early `return`, the line `--- finished ---` never prints.

**4. `12-first-class-functions-hof.md:214`**

> When passing in a callback to a higher-order function, avoid invoking the callback. In this example, since `execute_callback` is the higher-order function, it will invoke the callback on our behalf. Invoking the callback will produce an error:

- **Rules broken:** subject/unit, 1, and 3.
- **What a fellow gets wrong:** The sentence "Invoking the callback will produce an error" names no actor. `execute_callback` also invokes the callback, so a fellow cannot tell which invocation causes the error. The rule also comes before the problem it prevents.
- **Proposed rewrite:** "When you pass a callback to a higher-order function, write its name without parentheses. The higher-order function will call the callback itself, at the moment it needs to. If you add the parentheses, Python calls the callback right away, before the higher-order function even starts, and hands over whatever the callback returned instead of the callback itself. Here, `execute_callback` is the higher-order function, and the second call shows what goes wrong:"

**5. `12-first-class-functions-hof.md:379`**

> `ready` comes first. Calling `announce(greet)` builds `wrapper` and returns it, and building a function prints nothing. The three announcements wait until `loud_greet("Maya")` actually calls the wrapper on the last line.

- **Rules broken:** 4 and subject/unit.
- **What a fellow gets wrong:** "Building a function prints nothing" is a result, not the rule that the body of a function runs only when the function is called. Also, "the three announcements" miscounts. Only two of the three lines are announcements, and `Hi, Maya!` comes from `greet`.
- **Proposed rewrite:** "`ready` comes first. A `def` statement creates a function, but the body of that function runs only when something calls it. Calling `announce(greet)` runs `announce`'s body, which defines `wrapper` and returns it without calling it, so nothing inside `wrapper` has run yet. The other three lines wait until the last line, when `loud_greet("Maya")` calls `wrapper`: `wrapper` prints `--- starting ---`, calls `greet`, which prints `Hi, Maya!`, and then prints `--- finished ---`."

**6. `12-first-class-functions-hof.md:208`**

> They need it because each call has to remember where the previous call left off, and a callback that takes no arguments has nowhere else to keep that.

- **Rules broken:** 3 and 8.
- **What a fellow gets wrong:** The words "nowhere else" skip two steps. A local variable would reset on every call. The callback takes no arguments only because `repeat_every` calls `callback()` with none. Without those steps, a fellow will ask why a local variable would not work.
- **Proposed rewrite:** "They need it because each call has to remember where the previous call left off: which character comes next, or how far the alien has moved. A local variable cannot hold that, because a local variable disappears when its function returns, so the next call would start over from the beginning. A parameter cannot hold it either, because `repeat_every` calls `callback()` with no arguments. A global variable is the only place left."

**7. `12-first-class-functions-hof.md:316`**

> That works, and it is exactly the repetition chapter 3 warned you about. The announcing has nothing to do with greeting, but it is now tangled up with it, and you will have to pick it back out when you are done debugging.

- **Rules broken:** 2 and subject/unit.
- **What a fellow gets wrong:** The code shows only `greet` being edited, so a fellow sees no repetition. The phrase "it is now tangled up with it" uses two pronouns for two different things.
- **Proposed rewrite:** "That works for `greet`. Now do the same to `farewell`, and to every other function you want to watch, and you are pasting the same two `print` lines into each one: exactly the repetition chapter 3 warned you about. Worse, the announcing has nothing to do with greeting, but those two lines now sit inside `greet`, and when you finish debugging you will have to find and delete them from every function you edited."

**8. `12-first-class-functions-hof.md:280`**

> `min()` and `max()` take `key` the same way:

- **Rules broken:** 4.
- **What a fellow gets wrong:** A fellow may expect `max(users, key=...)` to return `41`. The text never says that `key` decides only the comparison, and that `max` returns the whole element.
- **Proposed rewrite:** Add after the code: "`max` calls the `lambda` on each user and compares the ages that come back, but it returns the whole user dictionary with the largest age, not the age itself. The returned value is a dictionary, so the next line can read `oldest['username']`."

**9. `12-first-class-functions-hof.md:148`**

> The callback is identical; only the higher-order function's behavior changed.

- **Rules broken:** subject/unit and 6.
- **What a fellow gets wrong:** Two different higher-order functions are involved, so "the higher-order function's behavior changed" suggests that one function was edited.
- **Proposed rewrite:** "The callback is the same in both calls. The difference comes entirely from the higher-order function: `repeat_every` calls `time.sleep(1)` after each call to `tick`, and `repeat` does not."

**10. `12-first-class-functions-hof.md:451`**

> The guard clause from chapter 4, now protecting a function that `skip_empty` knows nothing about. This is how a real decorator checks whether a user is logged in before letting a page load.

- **Rules broken:** 4 and 8.
- **What a fellow gets wrong:** The solution never explains what the bare `return` does, or why `not name` is true for `""`. A fellow who wrote an `else:` branch cannot tell whether that version is equivalent.
- **Proposed rewrite:** "The `if not name:` line is the guard clause from chapter 4. An empty string counts as false, so `not name` is `True` when the name is empty, and the bare `return` ends `wrapper` before it ever reaches `func(name)`. Notice that `skip_empty` knows nothing about greeting: it can protect any one-argument function. A real decorator uses the same move to check whether a user is logged in before letting a page load."

**11. `12-first-class-functions-hof.md:256`**

> A `lambda` has parameters before the colon and a single expression after it

- **Rules broken:** 3.
- **What a fellow gets wrong:** The `lambda` just above this sentence, `lambda: print("Tock")`, has nothing before its colon. A fellow has to guess whether that `lambda` is a special form.
- **Proposed rewrite:** "A `lambda` lists its parameters before the colon (the `lambda` above has none, so the colon comes right after the word `lambda`) and a single expression after it, and that expression's value is what the function returns."

**12. `12-first-class-functions-hof.md:54`**

> What we can see from this is that functions are just another type of data and, like other data types, it can be stored in a variable.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** The singular "it" has no singular antecedent, so a fellow has to work out whether "it" means a function or a data type.
- **Proposed rewrite:** "What we can see from this is that functions are just another type of data, and, like a string or a list, a function can be stored in a variable."

### 13-comprehensions-builtin-iteration.md

**1. `13-comprehensions-builtin-iteration.md:286`**

> `.sort()` changes `nums` and returns nothing, so `result` gets `None`. … The same rule applies to `.append()`, `.reverse()`, and every other method that mutates a list in place: they return `None`.

- **Rules broken:** 3 and 4, plus a factual error.
- **What a fellow gets wrong:** The answer says "returns nothing, so `result` gets `None`" without the rule from chapter 3 that a call with no return value gives back `None`. The phrase "the same rule" refers to a rule the answer never stated. The claim about "every other method that mutates a list" is false: `.pop()` changes the list and returns the element it removed. Any fellow who trusts that sentence will misuse `.pop()`.
- **Proposed rewrite:** "It prints `None`. `.sort()` reorders `nums` and has no return value, and a call with no return value gives back `None` (chapter 3). So `result` holds `None`, while `nums` itself is now `[1, 2, 3, 4, 5]`. This is one of the most common mistakes in Python: you write `x = my_list.sort()`, print `x`, see `None`, and conclude the list is gone, when the sorted list was in `my_list` all along. If you want the sorted list as a new value, use `sorted(nums)`. If you want to reorder `nums` itself, call `nums.sort()` on its own line and don't assign it to anything. `.append()` and `.reverse()` work the same way: they change the list and return `None`. `.pop()` is the exception you will meet most often: it removes an element and returns that element."
- I checked all four methods with `python3`.

**2. `13-comprehensions-builtin-iteration.md:307`**

> Sort this list of user dictionaries by age, youngest first, and then by username alphabetically.

- **Rules broken:** subject/unit. The instruction is ambiguous.
- **What a fellow gets wrong:** "By age, and then by username" reads as one sort that breaks ties between equal ages by username. The data even contains a tie at age 25, which makes that reading more likely. The solution, however, gives two separate sorts, so a fellow who solved the tie-breaking version will think they got the challenge wrong.
- **Proposed rewrite:** "Sort this list of user dictionaries two ways: once by age, youngest first, and once by username, alphabetically."

**3. `13-comprehensions-builtin-iteration.md:347`**

> Or fold the transform and the filter into one comprehension, which is fine while it stays readable:

- **Rules broken:** 3 and 4.
- **What a fellow gets wrong:** The text never explains why `num * 3` appears twice. A fellow will write `if num > 12` and get a different count.
- **Proposed rewrite:** "Or fold the transform and the filter into one comprehension, which is fine while it stays readable. Notice that `num * 3` appears twice. The `if` test runs on each original `num` from `my_nums`, before the expression at the front is evaluated, so the test cannot see the tripled value. To keep only the tripled values bigger than 12, the test has to do the tripling itself:"
- I checked the order with `python3`: the test runs on each item first, and the expression runs only for items that pass.

**4. `13-comprehensions-builtin-iteration.md:466`**

> Since we are now working with a mutable type (a list), we need to test two different things: that the _contents_ are right, and that the function gave us a _new_ list rather than the one we passed in.

- **Rules broken:** 2 and 3.
- **What a fellow gets wrong:** The word "Since" links mutability to the need for a second test without the step between them. Without that step, the `is not` test and the `original == [...]` test look like extra ceremony.
- **Proposed rewrite:** "A list is mutable, and a function that receives a list can change the caller's list directly. So a version of `double_all_purely` could double the values inside the list you passed in and hand that same list back. A test that only compared contents would pass for that version, even though your original numbers are gone. So we need to test two different things: that the _contents_ are right, and that the function gave us a _new_ list and left the one we passed in alone."
- I checked with `python3` that a version which mutates the list in place passes the contents-only assertion.

**5. `13-comprehensions-builtin-iteration.md:552`**

> Run it. It fails with `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`. The numbers and the string were never the problem, because `'a' * 2` is already `'aa'`. `None` is: it cannot be multiplied, and the comprehension has no way to know it should be left alone. A failing test is the point of this step: it proves the test is actually checking something.

- **Rules broken:** 7, 2, and 8.
- **What a fellow gets wrong:** The error message is quoted but never read, and the fragment "`None` is:" makes the reader rebuild the sentence. The phrase "proves the test is actually checking something" never says what a test that passed at this point would have failed to tell you.
- **Proposed rewrite:** "Run it. It fails with `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`. Read the message in two parts. `unsupported operand type(s) for *` says the `*` operator was given values it cannot multiply, and `'NoneType' and 'int'` names those values: `None` on the left and the `2` on the right. You may have expected the string to break the function, but `'a' * 2` is already `'aa'`, so the numbers and the string pass through fine. The `None` breaks it, because `None` cannot be multiplied and the comprehension multiplies every value it is given. This failure is what you want at this step. A test that passed before you wrote any new code could not tell you whether the new code works, because it would pass either way. A test that fails now and passes after your change proves that your change is what made it pass."
- I checked the error text with `python3`.

**6. `13-comprehensions-builtin-iteration.md:224`**

> `return` inside the loop is what makes this "first": the loop stops at the first success and never looks at the rest. The line after the loop handles the case where nothing matched. Decide what that case should return before you write the function, because callers will need to check for it.

- **Rules broken:** 4, 3, and 2.
- **What a fellow gets wrong:** The passage never states the rule that `return` ends the whole function, even from inside a loop. It never says why reaching the line after the loop means nothing matched. It also gives no reason for returning `-1` in one function and `None` in the other.
- **Proposed rewrite:** "A `return` statement ends the whole function immediately, even from inside a loop. So the loop stops at the first number that passes the test and never looks at the rest, which is what makes this "first". The only way to reach the line after the loop is for every element to fail the test, so that line handles the case where nothing matched. Decide what that case should return before you write the function, because every caller has to check for it. Choose carefully: `-1` is a valid index in Python, so a caller who forgets to check and writes `nums[find_first_odd_index(nums)]` gets the last element of `nums` instead of an error."
- I checked with `python3` that `-1` used as an index returns the last element. You may prefer to change that function to return `None` instead.

**7. `13-comprehensions-builtin-iteration.md:169`**

> Notice that the expression before the `for` is just `score`. Filtering keeps values as they are. You can transform _and_ filter in one comprehension by changing that expression, and the result can be shorter than the source.

- **Rules broken:** 8.
- **What a fellow gets wrong:** "The result can be shorter than the source" is attached to transforming and filtering together. A fellow will read it as a consequence of changing the expression, when it follows from the `if`. The sentence also leaves unmarked the contrast with line 117, which says a transform always keeps the same length.
- **Proposed rewrite:** "Notice that the expression before the `for` is just `score`, so each value that passes the test goes into the new list unchanged. Because the `if` removes elements, the new list can be shorter than the source, unlike a transform, which always keeps the same length. To transform _and_ filter in one comprehension, change that expression: `[score + 5 for score in scores if score >= 75]` adds 5 to each passing score."

**8. `13-comprehensions-builtin-iteration.md:117`**

> Read a comprehension from the `for` outward: "for each `inches` in `inches_list`, compute `get_feet_and_inches_str(inches)` and collect it." The new list always has exactly as many elements as the source.

- **Rules broken:** 8 and subject/unit.
- **What a fellow gets wrong:** A fellow has to guess what "outward" means. The guaranteed length is stated without the reason for it.
- **Proposed rewrite:** "Read a comprehension starting at the `for`, then jump back to the front: "for each `inches` in `inches_list`, compute `get_feet_and_inches_str(inches)` and collect the result." The comprehension computes one result for every element, so the new list always has exactly as many elements as the source."

**9. `13-comprehensions-builtin-iteration.md:574`**

> It is the tool for "what kind of thing is this?" checks, and it reads better inside a comprehension when the branching lives in its own small function.

- **Rules broken:** subject/unit, 2, and 3.
- **What a fellow gets wrong:** The second "it" could mean `isinstance` or the comprehension. The sentence never says why the branching needs its own function: an `if`/`elif`/`else` statement cannot go inside a comprehension.
- **Proposed rewrite:** "It is the tool for "what kind of thing is this?" checks. The checks live in their own function, `double`, because a comprehension holds a single expression, and an `if`/`elif`/`else` statement cannot go inside one. Moving the branching into `double` lets the comprehension stay a short, readable call."

**10. `13-comprehensions-builtin-iteration.md:419`**

> The same syntax with curly braces and a `key: value` expression builds a dictionary: `{user['id']: user['username'] for user in users}` produces `{1: 'ben', 2: 'maya'}`.

- **Rules broken:** subject/unit, plus a factual error.
- **What a fellow gets wrong:** The hint sits under `zip`/`any`/`all`, so "the same syntax" has no nearby antecedent. The output shown matches none of the `users` lists in the chapter. The four-user list with `id` keys produces four entries. The `users` most recently defined, in the sorting challenge, has no `'id'` key, so running the hint against that list raises a `KeyError`.
- **Proposed rewrite:** "Swap the square brackets of a list comprehension for curly braces and put a `key: value` expression at the front, and you build a dictionary instead. With the four-user list from the filtering section, `{user['id']: user['username'] for user in users}` produces `{1: 'ben', 2: 'maya', 3: 'reuben', 4: 'gonzalo'}`."
- I checked this output with `python3`.

**11. `13-comprehensions-builtin-iteration.md:326`**

> Dictionaries have no natural order, so `sorted(users)` with no `key` would raise a `TypeError`.

- **Rules broken:** 4 and 3.
- **What a fellow gets wrong:** Chapter 8 may have taught that dictionaries keep insertion order, so "no natural order" can be misread. The rule underneath is that `sorted` compares elements with `<`, and `<` is not defined between two dictionaries.
- **Proposed rewrite:** "Without a `key`, `sorted` would have to compare the dictionaries themselves with `<`, and Python has no rule for deciding whether one dictionary is less than another, so `sorted(users)` raises `TypeError: '<' not supported between instances of 'dict' and 'dict'`."
- I checked the error text with `python3`.

**12. `13-comprehensions-builtin-iteration.md:46`**

> What is the value of these tools? They allow us to write our code in a more _declarative_ manner rather than in an _imperative_ manner.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** This is the first sentence of the chapter, and no tools have been named yet.
- **Proposed rewrite:** "What is the value of the tools in this chapter, list comprehensions and built-in functions like `sum()` and `sorted()`? They allow us to write our code in a more _declarative_ manner rather than in an _imperative_ manner."

### Minor findings left out

- **12-first-class-functions-hof.md:** I left out 6 further minor findings. One worth knowing: the code comment at line 62, "copying the function", contradicts the prose. Both names refer to the same function; nothing is copied.
- **13-comprehensions-builtin-iteration.md:** I left out 10 further minor findings. One worth knowing: line 525 lists 4 TDD steps, but line 584 says "the same three steps you just did", and step 4 has no section.

### Pattern across both files

Hidden answers and challenge solutions show what happened but leave out the rule that made it happen. Examples are "gets resolved first" with no rule about argument evaluation, "returns nothing, so `None`", a closure used with no mention of why `func` survives, and `return` ending a loop. In two places the missing rule contradicts what an earlier chapter taught, and the text does not acknowledge it. Python error messages are quoted but never broken into their parts. Short references such as "the same rule", "the same syntax", "these tools", and "only one of them" point at something far away or at nothing, and two of those vague claims turn out to be false: the claim about every mutating method and the dictionary comprehension's output.

## Full findings: Mod 1: case study, project, and regex

I edited no files. I tested every behaviour claim below in a scratch copy of the task manager and in scratch scripts, using the case study's `.venv` (Python 3.12.4).

**Read this first.** Lines 92–392 of `case-study.md` sit inside an HTML comment that opens with `<!--` at line 92 and closes with `-->` at line 392. That range holds every section after "User Interface Design", including all the "What actually happens" answers. GitBook does not show any of it to fellows at the moment. I reviewed it anyway, because it will be published once the comment is removed.

### case-study.md

**1. `case-study.md:196`**

> The heading `Your Tasks:` appears with nothing beneath it. Nothing crashes, because a `for` loop over an empty list runs zero times. So the check is not there to prevent an error. It is there so that the user reads `No tasks yet. Add one!`, which tells them what to do next, instead of a heading over an empty space.

- **Rules broken:** 1, 2, 3, 4, 5, 6, 7, 8.
- **What a fellow gets wrong:** The answer never says what harm an empty heading does, so a fellow has to take on trust that it is bad. Some users will think the program froze.
- **Rewrite (the clear version from the rules):**

> The heading `Your Tasks:` appears with nothing beneath it. Nothing crashes because a `for` loop is allowed to iterate over an empty list, it just runs zero times. Some users may correctly understand that there aren't any tasks, but others may believe that the program froze while trying to display tasks. So, rather than introduce uncertainty, the `if` statement causes the program to display a clear message about the state of the program (`'No tasks yet'`) and what to do next (`'Add one!'`) instead of showing a header and an empty space.

**2. `case-study.md:315`**

> `Invalid task number.` With the list empty, `len(tasks)` is `0`, so `task_index >= len(tasks)` is `0 >= 0`, which is `True`, and the guard on line 45 returns before `tasks[task_index]` can raise an `IndexError`. That is the second of the two conditions Question 3 asks about, and it is the one doing the work here. The first, `task_index < 0`, catches a user who types `0`.

- **Rules broken:** 3, 8, 2.
- **What a fellow gets wrong:** The answer skips two steps: typing `0` becomes index `-1`, and Python accepts `-1` as "the last item". A fellow will likely assume `tasks[-1]` would simply raise an `IndexError`, so the first condition looks pointless. I confirmed that without that condition, `tasks[-1]` returns "Answer investigation questions".
- **Rewrite:**

> `Invalid task number.` When you type `1`, `menu.py` subtracts 1 and passes index `0` to `complete_task()`. With the list empty, `len(tasks)` is `0`, so the second condition, `task_index >= len(tasks)`, becomes `0 >= 0`, which is `True`. The guard on line 45 prints the message and returns before `tasks[task_index]` runs, and that matters, because indexing into an empty list raises an `IndexError`. The first condition, `task_index < 0`, protects against a different user: one who types `0`. Subtracting 1 turns that into index `-1`, and Python allows negative indexes, so without the check, `tasks[-1]` would quietly complete the last task in the list instead of reporting a mistake.

**3. `case-study.md:361`**

> The numbers now start at `0`, so "Answer investigation questions" is shown as `1`. Typing `1` makes `menu.py` subtract 1, which gives index `0`, so the confirmation names "Complete the CLI Task Manager project", the task above the one you meant. The display and the `- 1` in `menu.py` have to agree. `start=1` numbers the tasks from 1 for the user, and the `- 1` turns the user's number back into an index that starts at 0. Change one without the other, and every choice is off by one.

- **Rules broken:** 1, 2.
- **What a fellow gets wrong:** "Have to agree" comes before the job of each piece is explained. "Off by one" is a verdict, and the answer never says what the user actually sees. I confirmed that the user gets a confirmation for a task that was already complete, while the task they meant still shows `[ ]`. Typing the `0` shown beside the first task prints `Invalid task number.`.
- **Rewrite:**

> The confirmation names "Complete the CLI Task Manager project", the task above the one you meant. Two pieces of code have to agree about numbering. `start=1` makes `view_tasks()` number the tasks from 1 for the user, and the `- 1` in `menu.py` turns the user's number back into a list index, which starts at 0. Without `start=1`, the display starts at `0`, so "Answer investigation questions" is shown as `1`. Typing `1` makes `menu.py` subtract 1, which gives index `0`, the first task. The user reads a confirmation for a task that was already done, and the task they meant still shows `[ ]`. Worse, typing the `0` shown beside the first task gives index `-1`, which `complete_task()` refuses with `Invalid task number.` The program rejects a number it displayed itself.

**4. `case-study.md:136`**

> It fails before you choose anything, as soon as the menu has printed: `NameError: name 'tasks' is not defined`. `show_menu()` calls `view_tasks()` every time the menu displays, and `view_tasks()` looks for `tasks` in its own local scope and then in the global scope of `tasks.py`, and finds it in neither. The `tasks` inside `add_task()` is local to `add_task()`, so no other function can reach it. Even `add_task()` could not remember anything with it, because every call would start a brand new empty list.

- **Rules broken:** 1, 8.
- **What a fellow gets wrong:** The cause comes last. The new `tasks = []` is local to `add_task()`, so `tasks.py` no longer has a global `tasks`. Until the fellow reaches that sentence, they have to guess why `view_tasks()` cannot see a list the fellow just added.
- **Also:** On Python 3.12 the last line of the error actually reads `NameError: name 'tasks' is not defined. Did you mean: 'task'?`. The question asks fellows for that exact line, so they will notice the difference.
- **Rewrite:**

> It fails before you choose anything, right after the menu prints. The last line reads `NameError: name 'tasks' is not defined. Did you mean: 'task'?` A variable assigned inside a function is local to that function, so the new `tasks = []` exists only while `add_task()` runs, and no other function can reach it. With the top-level assignment gone, `tasks.py` has no global `tasks` at all. `show_menu()` calls `view_tasks()` every time the menu displays, and `view_tasks()` looks for `tasks` in its own local scope, then in the global scope of `tasks.py`, and finds it in neither. Even `add_task()` could not remember anything this way, because every call would start a brand new empty list.

**5. `case-study.md:214`**

> … Because `show_menu()` assigns `is_running = False` further down, Python treats `is_running` as a local variable of `show_menu()` for the whole function. When `while is_running:` runs, that local variable has not been given a value yet. This is the same rule as the `count` example in chapter 1.3.

- **Rules broken:** 4, 3.
- **What a fellow gets wrong:** The question asks what type of error appears. A fellow who deleted the variable will predict `NameError`, and the answer never says why the error is `UnboundLocalError` instead. The rule behind it is also left unstated: Python decides which names are local before the function runs.
- **Rewrite:**

> `Welcome to the Task Manager!` prints, and then, before the menu appears: `UnboundLocalError: cannot access local variable 'is_running' where it is not associated with a value`. Python decides which names in a function are local before the function starts running: any name the function assigns to, anywhere in its body, is local for the whole function. `show_menu()` still assigns `is_running = False` in the Exit branch, so `is_running` is a local variable from the very first line. When `while is_running:` runs, that local variable exists but has no value yet, which is why the error is `UnboundLocalError` and not `NameError`. This is the same rule as the `count` example in chapter 1.3.

**6. `case-study.md:178`**

> The task is added, and then `Invalid option. Please choose 1-4.` appears as well. With separate `if` statements, the `else` belongs only to the last one, `if menu_choice == '4':`. A choice of `'1'` runs the first `if`, and then Python goes on to check the other three. It finds that `'1' == '4'` is `False`, so it runs the `else`. …

- **Rules broken:** 4, 8.
- **What a fellow gets wrong:** The answer never states the rule that each separate `if` is checked on its own, whether or not an earlier one was true. The trace also jumps from "the other three" straight to `'4'`, so a fellow has to wonder what happened to the checks against `'2'` and `'3'`. I confirmed the output.
- **Rewrite:**

> The task is added, and then `Invalid option. Please choose 1-4.` appears as well. Python checks every separate `if` statement on its own, whether or not an earlier one was true, and an `else` pairs only with the `if` directly above it. Here, that is `if menu_choice == '4':`. A choice of `'1'` runs the first `if` and adds the task. Then Python checks `'1' == '2'` and `'1' == '3'`, finds both `False`, and skips them. Last, it checks `'1' == '4'`, which is also `False`, so it runs that `if`'s `else`. In an `if`/`elif` chain, Python stops at the first true condition, and the `else` runs only when none of them was true.

**7. `case-study.md:342`**

> Comprehensions and Python's built-in iteration tools abstract away the logic for looping through a list by index and doing something with its values. While the programmer loses some fine-tuned control over how the loop is executed, the improved readability of the code is often worth the tradeoff.

- **Rules broken:** subject/unit, 2.
- **What a fellow gets wrong:** "Abstract away" is jargon a new fellow will not know. "Fine-tuned control" never says what control is lost, so the fellow cannot weigh the tradeoff the paragraph asks them to weigh.
- **Rewrite:**

> A comprehension, or a built-in like `sum()` or `sorted()`, writes the loop for you: you say what should happen to each value, and Python handles stepping through the list. You give up some control in exchange. A comprehension cannot `break` out early, and it cannot easily look at the item before or after the current one. Most loops never needed that control, and the shorter code is easier to read.

**8. `case-study.md:265`**

> Code that a model wrote deserves the same method with more suspicion, because it looks just as confident when it is wrong as when it is right.

- **Rules broken:** 2, 6.
- **What a fellow gets wrong:** "Looks confident" says how the code seems without saying what follows from it. The consequence is that nothing on the page tells you whether the code is wrong.
- **Rewrite:**

> Code that a model wrote deserves the same method with more suspicion. Wrong code from a model is just as neatly named, commented, and formatted as right code, so nothing on the page warns you which one you have. Reading it line by line and running it are the only ways to find out.

**9. `case-study.md:229`**

> Lists are a great choice for grouping together lists of similar values while dictionaries are a great way to represent a single thing that has many data points related to it.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** The sentence defines a list as a way of grouping "lists", which is circular, so the fellow learns nothing about when to choose one.
- **Rewrite:**

> A list is a great choice for holding many values of the same kind, like all of your tasks. A dictionary is a great way to describe one thing with several named details, like one task's description and whether it is complete.

**10. `case-study.md:330`**

> A menu program is one of the places where this pays off most clearly.

- **Rules broken:** subject/unit, 2.
- **What a fellow gets wrong:** "This" could mean any of three things in the previous sentence, and "pays off" never says what the benefit is.
- **Rewrite:**

> A menu program is one of the clearest places to use this: a dictionary can map each menu choice to the function that handles it, and one lookup replaces the whole `if`/`elif` chain.

**11. `case-study.md:241`**

> As a result, we achieve "separation of concerns".

- **Rules broken:** 2.
- **What a fellow gets wrong:** The sentence names the principle (chapter 1.9 teaches the term) but not what it buys in this program. The fellow sees a label where a consequence should be.
- **Rewrite:**

> Each module has one job: `tasks.py` manages the data, `menu.py` talks to the user, and `main.py` starts the program. That is separation of concerns, and it means you can change how the menu looks without touching the code that stores tasks.

**12. `case-study.md:285`**

> Delete the function from `tasks.py` when you are done, because the AI policy keeps code a model wrote out of your own work.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** "The AI policy" is not named or linked, and "keeps … out" reads oddly. A fellow could conclude that pasting the function in at all breaks a rule.
- **Rewrite:** This keeps to `conversion-decisions.md`, which says chapters should link to the policy rather than restate its rules.

> Delete the function from `tasks.py` when you are done, so that code a model wrote does not stay in your project. The [AI Policy](../guidelines-and-policies/ai-policy.md) explains why.

### 14-project-week.md

**1. `14-project-week.md:141`**

> `main.py` — the entry point of the application that displays a menu to the user.
> `menu.py` — handles the main menu loop and handles user input.

- **Rules broken:** 6, subject/unit.
- **What a fellow gets wrong:** The rubric says both files show the menu, and that contradicts both the case study and the Phase 1 code. A fellow has to guess which file prints the menu, and may lose Code Organization points either way.
- **Rewrite:**

> `main.py` — the entry point: it greets the user, calls the menu, and says goodbye.
> `menu.py` — displays the menu, reads the user's choices with `input()`, and calls the function that matches each choice.
> A data layer (choose a name!) — holds your application's data and the functions that change it.

**2. `14-project-week.md:367`**

> Use a **list of dictionaries** to store quiz questions. Each question should be a dictionary with a `question` string, a `choices` list, and an `answer_index` indicating the index of the answer in `choices`, like this:

- **Rules broken:** 8.
- **What a fellow gets wrong:** The text leaves out that `answer_index` counts from 0 while the user sees choices numbered from 1. A fellow will compare the typed number with `answer_index` directly and mark every correct answer wrong. This is the same off-by-one mistake the case study's `- 1` handles.
- **Rewrite** (add after the code block):

> The `answer_index` counts from 0, like every list index, but the user sees the choices numbered from 1. A user who types `1` is choosing `choices[0]`, so subtract 1 from the user's number before you compare it with `answer_index`. The task manager does exactly this with the `- 1` in `menu.py`.

**3. `14-project-week.md:250` and `:263`**

> The user should then see a message summarizing the items they have added.
> When viewing the list, the user can see the total quantity of items in the list and the total price.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** The stored `price` is per item, but the list view shows `3 apples: $1.50`, which is the cost of that line. The text never says this, so a fellow has to work out from the examples whether to print the price or the price times the quantity. "The items they have added" also suggests a summary of the whole list, when the example confirms only the one item just added.
- **Rewrite:**

> When adding an item, the user enters the item's `name`, its `quantity`, and its price per item. The program then confirms what it just added, naming the quantity, the item, and the price per item.
>
> When viewing the list, the user sees each item with its quantity and its cost, which is the quantity times the price per item. Below the items come the total number of items and the total price.

**4. `14-project-week.md:53`**

> Create a CRUD application where users can add, remove, and view items in their shopping list through a menu system.

- **Rules broken:** subject/unit (a term of art used without a definition).
- **What a fellow gets wrong:** No Mod 1 chapter teaches "CRUD"; this is the only place it appears. A fellow has to guess what the label requires of them.
- **Rewrite:**

> Create an application where users can add, remove, and view items in their shopping list through a menu system. Programmers call this a CRUD application, for the four things it does with data: Create, Read, Update, and Delete.

**5. `14-project-week.md:199`**

> When viewing stats, the user can see games won, games lost, games tied, total games played, and win rate as a rounded percentage.

- **Rules broken:** subject/unit (the unit of "win rate" is never defined).
- **What a fellow gets wrong:** The example has 0 ties, so a fellow cannot tell whether ties belong in the denominator. Two fellows will build two different formulas. Ben needs to decide this; the rewrite shows one option.
- **Rewrite:**

> When viewing stats, the user can see games won, games lost, games tied, total games played, and win rate: the games won divided by all games played, ties included, shown as a percentage rounded to a whole number.

**6. `14-project-week.md:257`**

> When removing an item from the list, the user can specify the `name` of the item (case insensitive) and the `quantity` to remove.

- **Rules broken:** 8.
- **What a fellow gets wrong:** Phase 4 later asks "What if they try to remove an item that doesn't exist?", but the requirements never say what happens when the user removes every unit of an item, or more units than the list holds. A fellow has to invent the behaviour. This is also a decision for Ben.
- **Rewrite** (add):

> If the user removes the whole quantity, the item leaves the list entirely. If the user asks to remove more than the list holds, or names an item that is not on the list, the program says so and changes nothing.

**7. `14-project-week.md:347`**

> If the user's score is in the top 5, they are prompted again to enter their name to add their score to the high score leaderboard.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** "Again" implies the user was asked for their name earlier, and they never were. "In the top 5" is also unclear when the leaderboard holds fewer than five scores, which is the case at the start.
- **Rewrite:**

> If the user's score would place among the five highest scores on the leaderboard, the program asks for their name and adds the score to the leaderboard. While the leaderboard holds fewer than five scores, every score makes it.

**8. `14-project-week.md:133` (repeated at `:573`)**

> String Methods: Uses string methods (like `.lower()`, `.strip()`, etc.) to validate user input
> **Add input validation** — What if the user types something unexpected?

- **Rules broken:** 2, 3.
- **What a fellow gets wrong:** `.strip()` and `.lower()` tidy input but reject nothing. The examples under line 573 only tidy, so a fellow will believe that calling `.strip()` counts as validating input, and will skip the `if` that actually checks it.
- **Rewrite for 133:**

> String Methods: Uses string methods (like `.lower()`, `.strip()`, etc.) to clean up user input before checking it

- **Rewrite for 573:**

> **Clean up input, then check it.** `.strip()` and `.lower()` do not reject anything. They tidy the input so that `' Yes '` and `'yes'` count as the same answer. The check comes after, in an `if` that compares the tidied input with the answers you accept:

**9. `14-project-week.md:85`**

> Create an empty `requirements.txt` with `pip freeze > requirements.txt`. You will add to it if you install anything.

- **Rules broken:** 3, 8.
- **What a fellow gets wrong:** The text does not say why the command produces an empty file, and "add to it" does not say how. A fellow may type package names in by hand. I confirmed that `pip freeze` in a new virtual environment prints nothing.
- **Rewrite:**

> Run `pip freeze > requirements.txt`. Your virtual environment is brand new and has nothing installed yet, so the file starts out empty, which is fine. Whenever you `pip install` something, run `pip freeze > requirements.txt` again so the file lists it.

**10. `14-project-week.md:44`**

> You have three lecture sessions plus assignment time for this project, and it ends with the Mod 1 assessment. Keep it in a good state as you go, …

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** Here "it" could mean the project or the three sessions. A fellow could read the sentence as saying the project is the assessment. `scope-and-sequence.md` shows the assessment is a separate proctored hand-coding session on week 6 day 4. "A good state" is also vague.
- **Rewrite:**

> You have three lecture sessions plus assignment time for this project. The session after the third project day is the Mod 1 assessment, which is separate from the project: a proctored session where you write code by hand. Keep your project working and committed as you go, because you will see this application again: …

**11. `14-project-week.md:90`**

> To ensure that your `main` branch contains the most up-to-date working version of your application, you should use this workflow:

- **Rules broken:** 1.
- **What a fellow gets wrong:** The text never states the problem the branch solves: a half-finished feature committed to `main` leaves you with nothing that runs. Without that, the extra checkout and merge steps look like ceremony.
- **Rewrite:**

> If you commit a half-finished feature straight to `main`, then `main` is broken until you finish it, and you have no working version to show or submit. So build each feature on a `development` branch, and merge it into `main` only once it works:

**12. `14-project-week.md:428`**

> Start with just a menu that prints and exits:

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** The code does not exit straight away. It reads a choice and repeats it back, so a fellow may think the code is wrong when it pauses for input.
- **Rewrite:**

> Start with a menu that prints once, reads one choice, and repeats it back. There is no loop yet, so after one choice the function ends and `main.py` says goodbye:

### regex.md

**1. `regex.md:212`**

> Note that every one of these takes the pattern first and the string second.

- **Rules broken:** subject/unit (the claim is false).
- **What a fellow gets wrong:** `re.sub` takes the replacement second and the string third. A fellow who trusts this note will write `re.sub(pattern, string, replacement)`.
- **Rewrite:**

> Every one of these takes the pattern first. The first three take the string second; `re.sub` takes the replacement second and the string third.

**2. `regex.md:73`**

> The `r` tells Python not to treat backslashes as escape characters, so that `\w` reaches the `re` module as the two characters `\` and `w` rather than being mangled.

- **Rules broken:** 1, 2.
- **What a fellow gets wrong:** "Mangled" is a verdict with no harm named. The example also fails to show any harm: on 3.12, `"\w"` without the `r` still reaches `re` unchanged, and Python only prints a `SyntaxWarning`. A fellow who tests it will conclude the `r` does nothing. The real damage happens with `\b`. I confirmed that `re.search("\bcat\b", "the cat sat")` returns `None`, while the raw-string version matches.
- **Rewrite:**

> In Python, a regular expression is written as a string, and by convention as a **raw string** with an `r` in front of the quotes. The `r` settles an argument over the backslash. You saw in chapter 1.6 that an ordinary string turns a backslash and a letter into one special character: `"\n"` becomes a new line. Regular expressions use backslashes for their own special characters, and the two meanings collide. In an ordinary string, `"\b"` becomes a single backspace character, so the pattern `"\bcat"` reaches the `re` module without its `\b` (a word break) and quietly matches nothing. The `r` tells Python to leave every backslash alone, so `r"\bcat"` reaches the `re` module exactly as you typed it.

**3. `regex.md:284`**

> Notice that `flags` has to be passed by keyword here, because `re.sub` has a `count` parameter in the position where `re.search` takes its flags.

- **Rules broken:** 2, 3.
- **What a fellow gets wrong:** The text never says what goes wrong if you pass the flag by position. I confirmed what happens: `re.IGNORECASE` is the number `2`, so it becomes `count`, the search stays case sensitive, and the call prints `'my dog is named Catherine'` with no error. That output looks like success.
- **Rewrite:**

> Notice that `flags` has to be passed by keyword here. `re.sub` takes `count` as its fourth argument, in the position where `re.search` takes its flags, and `re.IGNORECASE` is secretly just the number `2`. So `re.sub(r"cat", "dog", phrase, re.IGNORECASE)` sets `count` to `2`, leaves the search case sensitive, and prints `'my dog is named Catherine'` without a single error. That is the kind of detail nobody memorizes; …

**4. `regex.md:226`**

> By default, regular expressions are case sensitive and, unless otherwise specified, must be an exact match.

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** "Must be an exact match" suggests that `r"cat"` will not match inside `"caterpillar"`, but the `findall` example a few lines later shows that it does. The fellow cannot tell which statement to believe.
- **Rewrite:**

> By default, a pattern is case sensitive: `r"cat"` matches a lowercase `c`, `a`, and `t` in that order, so it finds nothing in `"the Cat in the hat"`.

**5. `regex.md:258`**

> There is no "first match only" version to worry about here. `re.search` finds the first, `re.findall` finds them all.

- **Rules broken:** 5.
- **What a fellow gets wrong:** The sentence denies a belief no fellow holds; it reads as a leftover from JavaScript, where `match` behaves differently without the `g` flag. A fellow will wonder what "version" they were supposed to worry about.
- **Rewrite:**

> To get only the first match, use `re.search`. `re.findall` always returns every match.

**6. `regex.md:216`**

> Since a match object is truthy and `None` is falsy, you can use the result directly in an `if`:

- **Rules broken:** 3.
- **What a fellow gets wrong:** The colon promises an `if`, but the code below it contains only `print()` calls. A fellow has to work out the `if` form for themselves.
- **Rewrite:** Change the lead-in to:

> `re.search` returns a match object if the pattern appears anywhere in the string, and `None` if it does not:

Then, after the code block, add:

> A match object is truthy and `None` is falsy, so you can put the call straight into an `if`, as in `if re.search(r"cat", sentence):`, with no comparison needed.

**7. `regex.md:87`**

> It returns a match object if it does and `None` if it does not, which is why the function above compares against `None`.

- **Rules broken:** 3.
- **What a fellow gets wrong:** "Which is why" depends on a premise the paragraph never states: the function promises `True` or `False`, not a match object. Without it, the comparison looks unnecessary.
- **Rewrite:**

> It returns a match object if the whole string matches and `None` if it does not. The function is supposed to return `True` or `False`, so it compares the result with `is not None`, which turns a match into `True` and `None` into `False`.

**8. `regex.md:36` and `:56`**

> Consider this function:
> Now, consider the function with regular expressions.

- **Rules broken:** 1.
- **What a fellow gets wrong:** Neither sentence says what the function checks or what is costly about the first version, so a fellow does not know what to compare. The name "alphanumeric" also hides the fact that `_` is allowed.
- **Rewrite:** I avoided "the same check", because I confirmed that `\w` also matches `é`, while the loop version does not.

> Consider this function, which checks that a string holds only letters, digits, and underscores. It has to list every allowed character by hand and loop over the string one character at a time:
>
> Now, consider the function with regular expressions. The pattern `\w+` takes the place of both the list of allowed characters and the loop:

**9. `regex.md:95`**

> This function uses a regular expression to ensure that a given string is in the "MM-DD-YYYY" format:

- **Rules broken:** 8.
- **What a fellow gets wrong:** The pattern goes unexplained until the syntax tables, and the `12-32-2024` example suggests that impossible dates are rejected. I confirmed that `02-31-2024` passes.
- **Rewrite** (add after the code block):

> Don't worry about reading the pattern yet; the tables below cover every piece of it. Notice what it does and doesn't catch. It rejects `12-32-2024` because `([0-2][0-9]|3[01])` lets a day start with `3` only when the next digit is `0` or `1`. But it checks the format, not the calendar: `02-31-2024` passes, even though February has no 31st.

**10. `regex.md:82`**

> The symbols and characters inside the string define the characteristics of the strings that the regular expression can be used to search for. In the example above, we have:

- **Rules broken:** 8, subject/unit.
- **What a fellow gets wrong:** `re.compile()` appears in the code above and is never explained or used again. "In the example above" could also mean either of the two code blocks.
- **Rewrite:**

> `re.compile()` turns the string into a pattern object, which shows that a regular expression is a value with its own type. You won't need `re.compile()` in this chapter, because every `re` function also accepts the pattern as a plain string. The characters inside the string describe which strings the pattern matches. In `r"\w+"`:

**11. `regex.md:235`**

> `.start()` returns the index of the first match:

- **Rules broken:** subject/unit.
- **What a fellow gets wrong:** "Index of the first match" could be read as which match it is, rather than where in the string the match begins.
- **Rewrite:**

> The match object's `.start()` method returns the index where the match begins:

### Minor findings left out

- case-study.md: 4 further minor findings left out.
- 14-project-week.md: 3 further minor findings left out, for example "systems-level thinking skills" at line 42 and "(The most challenging and new!)" at line 56.
- regex.md: 3 further minor findings left out, mostly vague Key Terms wording such as "powerful" and "flexible".

### Problems outside the review scope (code blocks and tables)

- **regex.md table, `[3-30]` row:** The row says "And number in range", but I confirmed the class matches only the single characters `3` and `0`.
- **regex.md table, `[E-Q]` row:** The row says "Any uppercase letter", but the class covers only E through Q.
- **14-project-week.md, Phase 1 code:** The code prints "Goodbye!" twice, once in `menu.py` and once in `main.py`.

### Recurring pattern

The most common fault across all three files is that a sentence states a verdict or a label without the consequence that would justify it: "have to agree", "doing the work", "mangled", "pays off", "exact match", and "separation of concerns" each tell the fellow that something matters without saying what goes wrong for a user or a programmer. The second most common fault is a missing link between two correct sentences: why typing `0` becomes `-1`, why the function compares with `None`, why the flag must be passed by keyword, and why a deleted variable produces `UnboundLocalError` rather than `NameError`. In the project document, the same gap shows up as requirements given by example only, with the rule left out. The fellow has to infer the denominator of the win rate, that `answer_index` counts from 0, and whether the list shows the price or the line cost. Two fellows will infer these differently.

## Log of Ben's edits to applied rewrites

Each entry records how Ben changed a batch of applied rewrites before committing it, found by comparing the commit with the text Claude generated. An observation describes one situation and applies only to situations like it. An observation becomes a candidate rule for the project `CLAUDE.md` only after it appears in at least two batches, and Ben approves each rule before it is added.

### Batch 1: chapters 1.1 to 1.4 (commits `6c181f1` and `1775d48`)

Most rewrites were committed word for word, including every rewrite that states a rule and its consequence. Informal phrases such as "runs happily" and "quietly wrong" were kept.

- **Promoted to `CLAUDE.md`:** hidden answers that trace three or more steps were rewritten as one step per bullet, with the general lesson moved to its own paragraph after the list (1.1 expressions answer, 1.1 indentation answer, 1.3 `print_B` trace, 1.3 `TypeError` trace). Seen four times in this batch, so Ben promoted it immediately.
- **Fix sentence separated from the diagnosis.** In the 1.1 Celsius answer, the sentence giving the fix ("Parentheses are always evaluated first…") became its own paragraph. Seen once.
- **A described mistake became code.** The 1.4 caution about using user input as a condition was expanded into a sentence naming where the mistake happens (`input()`), a code block with the wrong version, and a code block with the fix. Seen once.
- **A sentence introducing code.** Ben added sentences saying what a code block is before it appears ("For example, this function uses these statements to print a message"). Seen twice, both in 1.4, both in passages the review did not touch.
- **Naming the syntax fully.** "A `def`" became "A `def` statement", and "so no `B` yet" became "so `B` is not printed yet". Seen once each.
- **A keyword's rule stated where the keyword appears.** Ben added the rule for `elif` (it runs only if the earlier conditions were `False` and its own is `True`). Seen once.
- **Not rejections:** four first-round rewrites in 1.2 are absent because Ben deleted or replaced the examples they belonged to (the sum and average example, the `msg +=` question, the precedence "Combined" challenge, and the `is_on = not is_on` sentence).
