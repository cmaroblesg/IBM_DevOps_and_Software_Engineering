# Introduction to Shell Scripting
## Introduction
A shell is a powerful user interface for Unix-like operating systems. It can interpret commands and run other programs. It also enables access to files, utilities, and applications, and is an interactive scripting language. Additionally, you can use a shell to automate tasks. Linux shell commands are used for navigating and working with files and directories. You can also use them for file compression and archiving. In this module, you will learn about the characteristics of shell scripting. You will explore the different Linux commands and their outputs, Bash scripting, and how to schedule jobs using crontab. You will learn how to work with filters, pipes, and variables.

## Learning Objectives
* Explain what a script is.
* Describe the ‘shebang’ interpreter directive.
* Use pipes and filters.
* Create and work with shell and environment variables.
* Schedule cron jobs with crontab.
* Understand the cron syntax.
* Perform command substitution.
* Execute commands in concurrent mode.

## Readings
* [Examples of pipes](./files/pipes.pdf)
* [Linux and Bash Command Cheat Sheet: The Basics](./files/ShellCommandsCheatSheet.pdf)

## Laboratories
* [**Hands-on Lab 4:** Getting Started with Shell Scripting](./files/Getting_Started_with_Shell_Scripting.pdf)
* [**Hands-on Lab 5:** Bash Scripting Advanced](./files/Bash_Scripting_Advanced.pdf)
* [**Hands-on Lab 6:** Scheduling Jobs Using Crontab](./files/Scheduling_Jobs_Using_Crontab.pdf)

## Summary & Highlights
Congratulations! You have completed this module. At this point, you know:  
* A shell script is an executable text file that begins with a ‘shebang’ interpreter directive
* Shell scripts are used to run commands and programs and can interpret command line arguments
* Filters are shell commands, and the pipe operator allows you to chain filter commands
* Shell variables can be assigned values with ‘=’ and listed using ‘set’
* Environment variables are shell variables with extended scope; create with ‘export,’ list with ‘env’
* Jobs can be scheduled to run periodically at selected times
* ‘m h dom mon dow command’ is the cron job syntax
* Command substitution is used to replace a command with its output
* The Bash shell-scripting feature ‘concurrent mode’ allows commands to run in parallel
