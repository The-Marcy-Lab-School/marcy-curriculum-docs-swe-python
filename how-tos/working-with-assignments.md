# How to Work on Assignments

**Table of Contents:**

- [Submitting On Time](#submitting-on-time)
- [Before You Start: Set Up GitHub](#before-you-start-set-up-github)
- [Types of Assignments](#types-of-assignments)
- [Using AI on Assignments](#using-ai-on-assignments)
- [Assignment Setup](#assignment-setup)
- [Submitting the Assignment](#submitting-the-assignment)
  - [Resubmitting an Assignment](#resubmitting-an-assignment)
  - [How to Undo a Commit to Main and Move Commits to Draft](#how-to-undo-a-commit-to-main-and-move-commits-to-draft)

## Submitting On Time

"Grades" don't exist at Marcy. We only need performance data in order to know how you're doing, and make sure the people who need help get it as quickly as they can. It's ok if you didn't finish by the deadline! Just show us what you have. We'll have office hours and reviews, and we want to know what you are all struggling with so we can use those meetings effectively. **This is not about grades, it's about seeing what you know, and where we can help!**

## Before You Start: Set Up GitHub

Every assignment lives in a GitHub repository. To complete one, you clone the repository onto your computer, commit your work on a branch, push that branch back to GitHub, and open a pull request. Each of those steps needs your computer to be connected to your GitHub account, so complete the [GitHub Setup](../environment-setup/github-setup.md) guide before you start your first assignment.

To learn more about how Git and GitHub work, including what branches and pull requests are, read [Module 0: Command Line Interfaces, Git, and GitHub](../mod-0-command-line-interfaces-git-and-github/README.md).

## Types of Assignments

There are two kinds of assignments at Marcy, and each kind has its own guide:

- **Coding assignments** ask you to write, modify, and debug Python code, which automated tests check. Read the [Coding Assignments Guide](coding-assignments.md).
- **Short response assignments** ask you to explain a concept in writing. Read the [Short Response Assignments Guide](short-response-assignments.md).

Each guide explains how that kind of assignment is scored, what feedback to expect, and how you may use AI on it.

## Using AI on Assignments

Every assignment follows the [AI Policy](../guidelines-and-policies/ai-policy.md). Each assignment's `README.md` also has an **AI Use on This Assignment** section that says how you may use AI on that particular assignment. The [Coding Assignments Guide](coding-assignments.md#using-ai-on-coding-assignments) and the [Short Response Assignments Guide](short-response-assignments.md#using-ai-on-short-response-assignments) each explain what the policy means for that kind of assignment.

## Assignment Setup

For short response and coding assignments, you will create a new branch called `draft` to complete your work. When you are ready to submit, you will create a Pull Request (PR) and tag your instructor for review.

{% hint style="info" %}
Want to learn more about git branching and making Pull Requests? Check out the [Git Branching and PRs lesson](../mod-0-command-line-interfaces-git-and-github/4-git-branching.md)!
{% endhint %}

Upon receiving any assignment, you should do the following setup steps:

1. Accept the assignment using the provided GitHub classroom link. It should generate a repository that is unique to you.
2. Clone down your repository into the `development` folder for the current module (for example, `development/mod-1`) and `cd` into your repository.
3. Create and checkout a new branch called `draft`

   ```sh
   git checkout -b draft
   ```

4. (_For coding assignments only_) Create a virtual environment, install the packages the tests need, and run the tests. The [Coding Assignments Guide](coding-assignments.md#coding-assignment-setup) lists the commands.

## Submitting the Assignment

To submit an assignment, do the following:

1.  Add, commit, and push your `draft` branch to your repository.

    ```bash
    git add -A
    git commit -m "Finished up to problem 5"
    git push
    ```

2.  You may need to set an upstream branch using the command

    ```sh
    git push --set-upstream origin draft
    ```

3.  Create a pull request using the **Pull Request** tab (and ignore the "Compare & pull request" button).

    ![Create a pull request by clicking on the "Pull Request" tab. Ignore the "Compare & pull request" button.](../.gitbook/assets/assignment-create-a-pr.png)

4.  Change the **compare** branch to be your `draft` branch and then click **Create pull request**!

    ![Change the compare branch to be your draft branch](../.gitbook/assets/assignment-select-draft-branch.png)

5.  Tag your instructor as a **Reviewer**.

    ![Tag your instructor as a reviewer on the pull request](../.gitbook/assets/assignment-tag-reviewer.png)

Opening the pull request submits your assignment on the LMS, so there is nothing else to submit. Your instructor will provide feedback on GitHub and will either approve your branch to be merged or will request that you resubmit.

### Resubmitting an Assignment

An assignment that scores below 75% must be revised and resubmitted. To resubmit, commit your fixes on the same `draft` branch and push them. The new commits appear on the pull request you already opened, so you do not need to make a new pull request. Then resubmit the assignment on the LMS.

**There is no limit to the number of times you can submit an assignment.** As such, you are encouraged to **always submit your assignments on time to ensure that your instructor can provide you feedback and support** to complete your assignments.

### How to Undo a Commit to Main and Move Commits to Draft

If you've accidentally added code to your `main` branch and want to move it into a `draft` branch, no need to worry. You can undo this by moving your code into a `draft` branch and reverting your `main` branch to the previous commit.

First, do the following to create / update your `draft` branch with the latest changes in `main`:

1. On your own computer, `cd` into the repo and `git checkout main` and `git pull` to make sure your local main branch is in sync with the remote repository.
2. Then `git checkout draft` (`git checkout -b draft` if you don't have a `draft` branch).
3. Run `git merge main` to make sure that the `draft` branch is up to date with the `main` branch.
4. `git push` to push your `draft` branch to GitHub. You may need to run `git push --set-upstream origin draft` if this is your first time pushing your `draft` branch.
5. Go to GitHub and double check that your `draft` branch has been pushed and that it contains your work.

Then, do the following to revert your `main` branch back to the initial commit:

1. `git checkout main` and `git log` to see the full commit history.
2. Find the commit you want to return to. Copy the commit SHA code (a 40-digit code identifying the commit).

   ![A git log showing the commit SHA codes](../.gitbook/assets/git-log-commit-sha.png)

3. Run the command `git reset --hard <commit_sha>` replacing `<commit_sha>` with the copied SHA from the last step. This will return your `main` branch back to that commit.

{% hint style="danger" %}
**DANGER: Running this next command will permanently delete the most recent commit from your `main` branch's commit history. Make sure that your `draft` branch on GitHub contains all of your work before proceeding.**
{% endhint %}

4. Finally, in your `main` branch `git push -f` to force the remote `main` branch return to the previous commit as well.

Once you've done this, return to GitHub and confirm that the `main` branch has returned to the previous commit and that your `draft` branch still contains your work. Then follow the steps above to create a Pull Request.
