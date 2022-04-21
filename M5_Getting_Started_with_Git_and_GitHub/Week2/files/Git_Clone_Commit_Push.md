## Hands-on Lab: Cloning, committing and pushing your GitHub repo from the command line.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/IDSNlogo.png" width="200" height="200">

<b>Effort</b> : 30 mins

## Objectives

After completing this lab you will be able to:

1.  Clone your GitHub repository locally.
2.  Make changes to the cloned files.
3.  Add a new file.
4.  Check the status.
5.  Commit changes.
6.  Push the changes back to GitHub.

## Pre-requisites

GitHub account, with a project in it, as illustrated in the [this lab](GitHub1\_Getting_Started.md.html).

GitBash or git installed on your local desktop, as in [this lab](GitBash_Install.md.html).

Create ssh keys,  as in  [this lab](SSH_Key.md.html)

Add SSH Key to GitHub,  as in  [this lab](GitHub_AddSSHtoRepo.md.html)

## Exercise 1: Clone a repo

To clone a repo, you need the ssh url of the repo.

1.  To get the ssh url, login into  GitHub.

2.  Navigate to the repo you wish to clone.

3.  Click on the 'Code' button.

4.  Click on the 'clipboard icon' to copy the url. Paste this url where you can access it later.

![ssh url](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/github-ssh-url-copy.png)

5.  On your desktop open a terminal.(gitbash if you are using windows os)

6.  Navigate to a directory where you wish to clone the repo.

7.  Run the command "git clone <your repo ssh url>"

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/git-clone.png)

8.  This will clone the repo on GitHub into your current directory.

9.  You can see all the downloaded files under a directory named as your repo name.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/git-clone-output.png)

change to the simple_interest_calulator directory and list the files to verify all the files got downloaded

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/list-files.png)

## Exercise 2: Make changes to cloned files.

Using your favourite editor make the changes to the html file.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/edit-code.png)

git status will show all the modified files.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/git-status.png)

## Exercise 3: Add a new file to the local repo

Let us add a new file to the local repo.

Using a text editor, create a new file "browser-support.txt".

Add "Chrome, Firefox, Edge" into the file.

Save the file.

## Exercise 4: Check the status

Run "git status" to see info on the modified files.

Let us add the file for committing.

Run "git add browser-support.txt"

## Exercise 5: Commit the changes

git commit will record all the changes into the local stating area.

To commit the changes you have made. Run git commit with a message like this.

git commit -m 'added a new file browser-support.txt'

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/git-commit.png)

Now all the changes you have made thus far, get committed locally.

## Excercise 6: Generate Personal Access Token

1.  Verify your email address if it hasn’t been verified on Github.

2.  In the upper-right corner of any page, click your profile photo, then click Settings.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/profile_settings.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

3.  In the left sidebar, click Developer settings.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/dev_settings.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

4.  In the left sidebar, click Personal access tokens and click on `Generate Tokens`

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/PAT.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

5.  Give your token a descriptive name. To give your token an expiration, select the Expiration drop-down menu, then click a default or use the calendar picker. Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select repo.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/new_personal_token.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

6.  Click Generate token and make a note of it.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/generate_token.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

7.  Make sure you copy the token and keep it safe. It is not visible to you again.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/copy_token.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

> **Treat your tokens like passwords and keep them a secret.**

> Once you have a token, you can enter the Personal Access Token as password when performing Git operations.

## Excercise 7: Push the code to GitHub

The git `push` command will enable you to sync all the changes made locally to the GitHub web repository.

```
  1. Run the following command with your actual HTTPS link:

     `git push [HTTPS link]`

     You will be prompted by git for your username and password.

  2. Type your GitHub username and for the password, enter the personal access token you generated in the previous task. When you are authenticated, all committed changes are synced with your GitHub repository.
```

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/git-push.png)

You can now visit the GitHub repository page and check to ensure that the revised and newly added files are in place.

## Summary

In this lab, you have learned how to clone a GitHub repository, make changes to it, commit the changes locally, and push it back to GitHub.

## Author(s)

<h4> Ramesh Sannareddy <h4/>

### Other Contributor(s)

Rav Ahuja

## Changelog

| Date       | Version | Changed by        | Change Description      |
| ---------- | ------- | ----------------- | ----------------------- |
| 2020-08-23 | 1       | Ramesh Sannareddy | Initia version created. |
|            |         |                   |                         |
