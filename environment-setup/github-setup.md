# GitHub Setup

## Configure Your GitHub Account

You will be using GitHub individually to store your portfolio projects and collaboratively to work on group projects. We will set up your development environment to be able to communicate with your GitHub account. You'll be able to clone code from a remote repo to your local computer by using the Secure Shell (SSH) protocol in the Terminal and make changes to it on your computer.

**Table of Contents:**

- [Configure Your GitHub Account](#configure-your-github-account)
  - [What you are setting up](#what-you-are-setting-up)
  - [Create a GitHub Account](#create-a-github-account)
  - [Configuring Your Terminal to Work With Your GitHub](#configuring-your-terminal-to-work-with-your-github)
  - [Create A Repository](#create-a-repository)
  - [Create an SSH Key](#create-an-ssh-key)
  - [Clone Using SSH](#clone-using-ssh)
- [Final Step](#final-step)

### What you are setting up

The [Mac](local-environment-setup-mac.md) and [Windows](local-environment-setup-windows.md) setup documents got your computer to the point where it can do three things: open VS Code, keep all of your work in one `development` folder, and run Python. This document covers the fourth and last thing:

- **Connect your computer to your GitHub account**, so that you can download (clone) the repositories we assign you and upload (push) the work you do in them.

Two names come up constantly in this document, and they are not the same thing:

- **`git`** is a program that is already on your computer. It watches a folder and records the changes you make to it, one snapshot at a time. Each snapshot is called a **commit**.
- **GitHub** is a website that stores copies of those folders, so that your work exists somewhere other than your laptop and other people can see it.

Your work for the program moves back and forth between the two. You **clone** a repository to copy it from GitHub down onto your computer, you **commit** as you work to record what you have changed, and you **push** to send those commits back up to GitHub. By the end of this document you will have done each of those once, on a repository of your own.

### Create a GitHub Account

**GitHub** is like a social network for developers, making it easy to backup, share and collaborate on projects. Your GitHub profile will become the first thing that employers look at to see the projects you've worked on and to get a sense of the kind of developer you are!

Start by [creating a free GitHub Account](https://github.com/join).

**The username you choose for your profile should include your first and last name.** Keep it professional.

If you already have an account and it does not include your first and last name, you may update it in the settings or you can create a new account.

Write down your username and password so you don't forget it!

### Configuring Your Terminal to Work With Your GitHub

GitHub is where we store our code online. It does have a drag-and-drop upload tool but it is more common to use the `git` tool in your Terminal to upload your code.

To do so, we need to connect your Terminal to your GitHub account. There are two separate things to set up, and this section is the first of them: telling `git` who you are, so that every commit you make is stamped with your name and email address. Without that, `git` refuses to record a commit at all, because a commit with no author is not much use to anybody.

1.  Open the Terminal application. Start by running the command:

    ```bash
    git --version
    ```

    which will print the current version of the `git` tool on your computer. This just confirms that you have the `git` tool

2.  If you are using a Mac and this is your first time, a popup called **Install Command Line Developer Tools** will appear. Follow the instructions to install them on your computer.
3.  Once this is done, in your Terminal, run the following lines. Be sure to replace `[Your Name]` and `[Your GitHub Email Address]` with your actual GitHub login information:

```sh
git config --global user.name "[Your Name]"
git config --global user.email "[Your GitHub Email Address]"
git config --global credential.helper store
```

4. Confirm that the configuration was successful by running

```sh
git config --global user.name
git config --global user.email
```

The terminal should print out your name and email.

`--global` means these settings apply to every repository on your computer, so this is a one-time setup rather than something you repeat for each project.

### Create A Repository

A **repository** is a digital place where we store our code. It's essentially a folder. By creating that repository on GitHub, instead of on our own computer, anyone can see the code we're writing and can collaborate on it (with permission).

Navigate to GitHub in the browser and log in. On the left side you should see a **New** button to create a new repository. Click it.

![Step 1. Create a new repository.](../.gitbook/assets/github-setup-1.png)

Then, fill out the form to configure the repository:

- Choose your account as the owner of this repository.
- Name your repository _exactly_ the same as your username. You should see a message below saying that the repo is a "✨special✨ repository".
- Toggle the switch for **Add README** to "On".
- Click **Create repository**.

![Step 2. Configure your repository](../.gitbook/assets/github-setup-2.png)

### Create an SSH Key

If we wanted to add files to this repository or download the contents of it, GitHub has a fairly standard drag-and-drop file system for upload and a button to download.

However, it is more common to use the `git` tool in our Terminal to send and receive code via the Secure Shell (SSH) communication protocol.

This is the second half of connecting your Terminal to GitHub. Every time your computer talks to GitHub, GitHub has to be satisfied that the computer really belongs to you. Typing a password on every single upload would be tedious, so instead your computer generates a pair of matching files called an **SSH key**: a private half that stays on your computer and that you never share with anyone, and a public half that you paste into your GitHub account. From then on the two halves recognize each other and GitHub lets your computer in without asking you anything.

> SSH is a communication protocol. Other communication protocols you may have heard of include:
>
> - SMS (Short Messaging Service): the original, non-encrypted protocol used by cellular networks to send and receive text-only messages.
> - HTTP (Hypertext Transfer Protocol): the foundation of the World Wide Web, used for receiving website code and other data from web servers.

To enable this communication between our Terminal and our GitHub repos, we need to generate and add an **SSH Key** to our account.

1. First, check if you already have an SSH key by running `ls ~/.ssh`. If the terminal lists out any file(s) with a name called `id_ed25519.pub` then you already have a key.
2. If the running previous step printed "No such file or directory", then run `ssh-keygen -t ed25519` to create a key.
   - It will ask you to enter a file to save the key. Just press enter which will use a default location. It will say that it created the directory `/Users/[your_username]/.ssh`
   - It will ask you to enter a passphrase. Just press Enter.
   - If you've done every correctly, you should be something like this printed to your terminal (read it!):

     ![The SSH key has been generated](../.gitbook/assets/ed25519.png)

3. Run `cat ~/.ssh/id_ed25519.pub` in your terminal and copy the output (starting from `ssh-ed25519`). You'll need it for the next step
4. Navigate to the homepage of GitHub in your browser. Go to your account settings:

   ![Go to GitHub Settings](../.gitbook/assets/github-setup-5.png)

5. Click "SSH and GPG Keys":

   ![Select SSH and GPG Keys](../.gitbook/assets/github-setup-6.png)

6. Click the "New SSH key" button:

   ![Click New SSH Key](../.gitbook/assets/github-setup-7.png)

7. Configure the new SSH key on GitHub:
   - The title should identify the computer that the SSH key came from. For example, "personal laptop" or "Marcy Macbook".
   - Open the **Key type** dropdown and select "Authentication Key".
   - Paste the key in the text area.
   - The form should look like this: ![Configure your SSH key](../.gitbook/assets/addSSHkey.png)
8. Click **Add SSH key**

### Clone Using SSH

Now that your GitHub profile has stored the SSH key generated by your computer, your computer will be authorized to upload and download code from your repositories using the Secure Shell (SSH) protocol.

1. Go back to your repository on GitHub.
2. Then, click on the green **Code** button. Select the SSH protocol, and copy the `git@github.com...` by clicking on the copy button.

   ![Copy the SSH URL](../.gitbook/assets/github-setup-13.png)

3. Open up VS Code and open your terminal.
4. Navigate in your terminal to your `development/mod-0` folder. If you set up your directories properly, you should be able to use the command:

   ```sh
   cd ~/development/mod-0
   ```

   This step matters more than it looks. `git clone` creates a new folder inside whatever folder your terminal is currently working in, so the folder you are in when you run it decides where the project ends up on your computer. Moving to `mod-0` first is what keeps all of your Mod 0 work in one place instead of scattered around your file system.

5. Clone (download) down the project using the command:

   ```sh
   git clone [git_url_here]
   ```

   replacing `[git_ssh_url]` with the URL you copied from your GitHub repository.

   If asked, "Are you sure you want to continue connecting", type `yes`. This question appears the first time your computer talks to GitHub over SSH and will not be asked again.

6. Enter the command `ls` to see that a new folder with the name of your repo has been added to the `mod-0` directory!
7. Navigate into that folder with the command `cd [repo_name]` (replace `[repo_name]` with the name of your repository)
8. Once your repo can been cloned down (downloaded), you should see also it in your file system in VS Code. Expand the folder and open the `README.md` file.
9. In The `README.md` file, **Add a short bio about yourself**. Be sure to save the file. Below is a template you can get started with. It is written using Markdown which is a language used for formatting text. Copy the entire text and fill in your information where you see blank spaces:

   ```md
   # Hi, I'm **\_** 👋

   ## 👨‍🏫 About Me

   - Student at the [Marcy Lab School](https://www.marcylabschool.org/) studying to become a Software Engineer
   - Born in **\_** → Raised in **\_** → Currently in **\_**.
   - Outside of work I like to **\_**
   - Let's connect via email: **\_**

   ## Tech Stack:

   ### Languages

   - Python

   ### Tools

   - Git
   - GitHub
   - VS Code
   ```

10. Push (upload) the changes to GitHub using the `git` commands below:

    ```sh
    git status
    git add README.md
    git commit -m "added bio"
    git push
    ```

    Each of those four commands does one job:
    - `git status` lists the files you have changed since your last commit. It changes nothing; it just tells you where you stand.
    - `git add README.md` chooses which of those changed files will go into the next commit.
    - `git commit -m "added bio"` records a snapshot of the files you added, together with a short message describing what changed. This snapshot is saved on your computer only.
    - `git push` sends the commits saved on your computer up to GitHub.

    Notice the order: nothing is recorded until you commit, and nothing leaves your computer until you push. You will run these four commands hundreds of times over the next nine months.

11. You've just uploaded your code from your computer to GitHub. Go back to GitHub to view your repository in the browser. Refresh the page and confirm that you see your newly added bio!

    Any time that you would like to add to your bio (for example, to highlight a portfolio project or to share a link to your LinkedIn), just return to this repository in your terminal and repeat steps 9 and 10!

## Final Step

Once you have completed all the steps in these instructions, reach out to a technical instructor to verify you are finished.
