# Using Git Commands and Managing GitHub Projects
## Introduction
Branches are the heart of workflows in Git-based version control systems like GitHub. In this module you will become familiar with creating and using branches, and merging your changes to the main branch with Pull Requests. As you start working with GitHub repositories and automating workflows, using the web interface can be limiting and more time-consuming. This is where Git commands come in. You can use from your own desktop or a Cloud IDE - wherever you develop your code. In this module you will also become familiar with and utilize various Git commands to clone and fork repositories, as well as commit, push and pull your changes using the command line.

## Learning Objectives
* Explain how branches are used and describe pull requests.
* Describe the function of Git commands like push, pull, and fetch.
* Differentiate between cloning and forking GitHub projects.
* List the roles common in large projects.
* Execute Git commands to work with GitHub repositories from a terminal.
* Create a fork and clone of a GitHub repository, make code changes, and submit a pull request.
* Create GitHub branches and perform merge operations using the GitHub Web interface.

## Laboratories
* [**Hands-on Lab 2:** Create and merge a branch in your GitHub repository](./files/GitHub2_Branch_Merge.pdf)
* [**Hands-on Lab 3:** Getting started with branches using git commands on a local repository](./files/GitHubTest01_Getting_Started.pdf)
* [**Hands-on Lab 4:** Get familiar with fork and pull requests](./files/Fork_and_pull_requests.pdf)

## Readings
* [Forking and Cloning GitHub repos](./files/Forking_and_Cloning_GitHub.pdf)

## Module Summary
In this module, you learned that:
* Branches are used to isolate changes to code. When the changes are complete, they can be merged back into the main branch.
* Repositories can be cloned to make it possible to work locally, then sync changes back to the original.
* Repositories can be forked to be used as a base for a new project, or so that the developer can work independently.
* A​ Pull Request (PR) can be submitted to have your changes reviewed and merged.
* Large projects include people working in different roles:
* Developer – creates code
* Integrator – manages changes made by developers
* Repository Administrator – configures and maintains access to the repository

## Using Git Commands from your Desktop
I​n the previous lab you used a Cloud-based IDE to work with Git commands. In many cases, you will be developing code on your own workstation on your desktop/laptop. Linux systems  typically come pre-installed with Git commands or if needed you can install them using **dnf** on rpm based distributions (e.g. Red Hat / Fedora):

**sudo dnf install git-all**

o​r, **apt** on Debian-based distributions (e.g. Ubuntu):

**sudo apt install git-all**

O​n MacOS you can activate Git by typing:

**git version**

H​owever if it is not installed, or if you want to update it, you can download and install the latest version of the [MacOS Git Installer](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect), and run the above command to verify the version.

O​n Windows based systems, you can install **Git Bash** by downloading the [Git for Windows installer](https://gitforwindows.org/).  Git Bash includes popular Linux Bash shell commands (such as ls, pwd, cat, etc.) as well as Git commands.

Y​ou can also get the [GitHub desktop](https://desktop.github.com/) for Windows and MacOS, which provides a UI for GitHub on your desktop.

W​hen you are working with GitHub repositories from your desktop you will also need to setup an ssh key.

**The remaining labs in this module are optional however recommended for those with a Windows desktop.** In the following labs you will install Git Bash on your Windows machine, and configure an ssh key to work with your GitHub repo using Git commands on your system.

## **[Optional]** Laboratories
* [Installing Git Bash](./files/GitBash_Install.pdf)
* [Generate a SSH Key](./files/SSH_Key.pdf)
* [Adding a SSH key to GitHub](./files/GitHub_AddSSHtoRepo.pdf)
* [Cloning, committing and pushing your GitHub repo from the command line](./files/Git_Clone_Commit_Push.pdf)
