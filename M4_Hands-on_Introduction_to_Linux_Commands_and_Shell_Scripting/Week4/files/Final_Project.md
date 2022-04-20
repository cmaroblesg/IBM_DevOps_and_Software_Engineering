---
markdown-version: 
title: labs/Final Project/Final_Project
branch: lab-306-instruction
version-history-start-date: 2022-03-01T20:13:10Z
---

# Linux Commands and Shell Scripting - Final Project

<center>
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_darkmode.png" width="300">
</center>

**Estimated time needed:** 90 minutes

Congratulations!! You have finished the modules. Now is the time to put your skills to test. Read through the scenario below.

This lab may use some bash concepts we haven't yet covered in this course. Whenever this happens, we will provide sufficient hints and/or the code for you.

## Scenario

You are a lead linux developer at the top-tech company "ABC International INC." ABC currently suffers from a huge bottleneck - each day, interns must painstakingly access encrypted password files on core servers, and backup those that were updated within the last 24-hours. This introduces human error, lowers security, and takes an unreasonable amount of work.

As ABC INC's most trusted linux developer, you have been tasked with creating a script `backup.sh` which automatically backs up any of these files that have been updated within the past 24 hours.

## Objectives

*   The objective of this lab is to incorporate much of the shell scripting you've learned over this course into a single script.
*   You will schedule your shell script to run every 24 hours using `crontab`.
*   TIP: If you're unsure whether some of your code will work as wanted, you can try the command directly in the terminal - and even create your own test scripts!

# Task 0

1.  Open a new terminal by clicking on the menu bar and selecting **Terminal**->**New Terminal**:

2.  Download the template file `backup.sh` by running the command below:

```
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/backup.sh
```

{: codeblock}

3.  Open the file in the IDE by clicking **File**->**Open** as seen below:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/file-open.png" width="50%" height="auto">  

and then click on the file, which should have been downloaded in the project directory:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/prompt-open.png" width="50%" height="auto">  

# About the template script, `backup.sh`

1.  You will notice the template script contains comments (lines starting with the `#` symbol). Do **not** delete these.

*   The ones that look like "`# [TASK {number}]`" will be used by your grader:

    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/task-comments.png" width="50%" height="auto">  

2.  Also, please do **not** modify any existing code above `# [TASK 1]` in the script.

# <span style="color: rgb(183, 55, 62); font-weight:bold;">Saving your progress</span>

Your work **will not** be saved if you exit your session.

In order to save your progress:

1.  Save the current working file (`backup.sh`) with `CTRL-S` \[Windows/Linux], `CMD-S` \[MAC], or navigate to **File**->**Save** as seen below:

    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/file-save.png" width="50%" height="auto">  

2.  Download the file to your local computer by navigating to **File**->**Download** as seen below:

    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/file-download.png" width="50%" height="auto"> 

3.  Unfortunately, our editor does **not** currently support file uploading, so you will need to use 'copy and paste' as follows:
    *   To "upload" your in-progress `backup.sh` file and continue working on it:
        1.  Open a terminal and type `touch backup.sh`
        2.  Open the empty `backup.sh` file in the editor
        3.  Copy paste the contents of your locally-saved `backup.sh` file into the empty `backup.sh` file in the editor

# Task 1

Navigate to `# [TASK 1]` in the code.

Set two variables equal to the values of the first and second command line arguments, as follows:

1.  Set `targetDirectory` to the first command line argument
2.  Set `destinationDirectory` to the second command line argument

(This task is meant to help with code readability)

<details>
<summary>Click here for Hint</summary>

> The command line arguments interpreted by the script can be accessed via `$1` (first argument) and `$2` (second argument)

</details>

# Task 2

1.  Display the values of the two command line arguments in the terminal.

<details>
<summary>Click here for Hint</summary>

> Rememeber, you can use the command `echo` as a print command.
>
> *   Ex: `echo "The year is $year"`

</details>

# Task 3

1.  Define a variable called `currentTS` as the current timestamp, expressed in seconds.

<details>
<summary>Click here for Hint</summary>

> Remember you can customize the output format of the `date` command.
>
> *   To set a variable equal to the output of a command you can use command substitution: `$()` or `` ` ` ``
>     *   For example: `currentYear=$(date +%Y)`

</details>

# Task 4

1.  Define a variable called `backupFileName` to store the name of the archived and compressed backup file that the script will create.

*   The variable `backupFileName` should have the value `"backup-[$currentTS].tar.gz"`
    *   For example, if `currentTS` has the value `1634571345`, then `backupFileName` should have the value `backup-1634571345.tar.gz`.

# Task 5

1.  Define a variable called `origAbsPath` with the absolute path of the current directory as the variable's value.

<details>
<summary>Click here for Hint</summary>

> You can get the absolute path of the current directory using the `pwd` command.

</details>

# Task 6

1.  Define a variable called `destAbsPath` with value equal to the absolute path of the destination directory.

<details>
<summary>Click here for Hint</summary>

> First use `cd` to go to `destinationDirectory`, and then use the same method you used in **Task 5**

</details>

# Checkpoint

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/save.png" width="50%" height="auto" align="center">

Friendly reminder to save your work to your local computer!

# Task 7

1.  Change directories from the current working directory to the target directory `targetDirectory`.

<details>
<summary>Click here for Hint</summary>

> `cd` into the original directory `origAbsPath` and then `cd` into `targetDirectory`.

</details>

# Task 8

You need to find files that have been updated within the past 24 hours.\
This means you need to find all files who's last modified date was 24 hours ago or less.

To do make this easier:

1.  Define a numerical variable called `yesterdayTS` as the timestamp (in seconds) 24 hours prior to the current timestamp, `currentTS`

<details>
<summary>Click here for Hint</summary>

> Math can be done using `$(())`; for example: `zero=$((3 * 5 - 6 - 9))`
>
> *   Thus, to get the timestamp in seconds of 24 hours *in the future*, you would use:
>     *   `tomorrowTS=$(($currentTS + 24 * 60 * 60))`

</details>

# Note on arrays

You will notice the line:

```
declare -a toBackup
```

in the script.

This line declares a variable called `toBackup`, which is an array.
An array contains a list of values, and items can be appended to arrays using the syntax:

```
myArray+=($myVariable)
```

When you print (or `echo`) an array you will see its string representation, which is simply all of its values separated by spaces:

```
$ declare -a myArray
$ myArray+=("Linux")
$ myArray+=("is")
$ myArray+=("cool!")
$ echo $myArray
Linux is cool!
```

This will be useful later in the script where you will pass the array `$toBackup`, consisting of the names of all files that need to be backed up, to the `tar` command. This will archive all files at once!

# Task 9

1.  Within the `$()` expression inside the `for` loop, write a command that will return all files and directories in the current folder.

<details>
<summary>Click here for Hint</summary>

> There is a very clean way of doing this using `ls`

</details>

# Task 10

1.  Inside the for loop, you want to check whether the `$file` was modified within the last 24 hours.

*   To get the last-modified date of a file in seconds, use `date -r $file +%s`
*   Then compare the value to `yesterdayTS`
    *   Idea: `if [[ $file_last_modified_date > $yesterdayTS ]]` then the file was updated within the last 24 hours!

2.  Since much of this wasn't covered in the course, for this task you may copy the code below and paste it into the double round brackets `(())`:

```
`date -r $file +%s` > $yesterdayTS
```

{: codeblock}

# Task 11

1.  In the `if`-`then` statement, add the `$file` that was updated in the past 24-hours to the `toBackup` array.
2.  Since much of this wasn't covered in the course, you may copy the code below and place after the `then` statement for this task:

```
toBackup+=($file)
```

{: codeblock}

# Checkpoint

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/save.png" width="50%" height="auto" align="center">

Friendly reminder to save your work to your local computer!

# Task 12

1.  After the `for` loop, **compress** and **archive** the files, using the `$toBackup` array of filenames, to a file with the name `backupFileName`.

<details>
<summary>Click here for Hint</summary>

> Use `tar -czvf $backupFileName ${toBackup[*]}`

</details>

# Task 13

Now the file `$backupFileName` is created in the current working directory.

1.  Move the file `backupFileName` to the destination directory located at `destAbsPath`.

You are now done the coding portion of the lab!

# Task 14

1.  Open a new terminal by clicking on the menu bar and selecting **Terminal**->**New Terminal**, as in the image below:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/new-terminal.png" width="50%" height="auto">

*   This will open a new terminal at the bottom of the screen as seen below:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/terminal_bottom_screen.png" width="50%" height="auto">

# Task 15

1.  Save the file you're working on (`backup.sh`) and make it executable.

<details>
<summary>Click here for Hint</summary>

> Use the `chmod` command with the correct options

</details>

2.  Verify the file is executable using the `ls` command with the `-l` option:

```
ls -l backup.sh
```

{: codeblock}

3.  Take a screenshot of the output of the command above and save as `15-executable.jpg` (or `.png`)

# Task 16

1.  Download the following `zip` file with the `wget` command:

```
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip
```

{: codeblock}

2.  Unzip the archive file:

```
unzip -DDo important-documents.zip
```

{: codeblock}

(`-DDo` to overwrite and not restore original modified date)

Update the file's last modified date to now:

```
touch important-documents/*
```

{: codeblock}

3.  Test your script using the following command:

```
./backup.sh important-documents .
```

4.  This should have created a file called `backup-[CURRENT_TIMESTAMP].tar.gz` in your current directory

5.  Take a screenshot of the output of `ls -l` and save as `16-backup-complete.jpg` (or `.png`)

# Task 17

1.  **Copy** (don't `mv`) the `backup.sh` script into the `/usr/local/bin/` directory.

    *   Note: You may need to use `sudo cp` in order to create a file in `/usr/local/bin/`

2.  Using `crontab`, schedule your `/usr/local/bin/backup.sh` script to backup the `important-documents` folder every 24 hours to your home directory (`~`).

3.  Take a screenshot of the output of `crontab -l` and save as `17-crontab.jpg` (or `.png`)

# Task 18

1.  Save the current working file (`backup.sh`) with CTRL-S \[Windows/Linux], ⌘-S \[MAC] or navigating to **File**->**Save** as seen below:

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/file-save.png" width="50%" height="auto">

2.  Download the file to your local computer by navigating to **File**->**Download** as seen below:

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/images/file-download.png" width="50%" height="auto">

    (You may save the file as `backup.sh`)

3.  You will later submit this file will for peer-grading.

# Congratulations!

You have completed the final lab for this course!
