# Hands-on Lab: Get familiar with fork and pull requests

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/IDSNlogo.png" width="200" height="200">

<b>Effort</b> : 30 mins

## Objectives

After completing this lab, you will be able to use git commands to manage upstream repositories:

1.  create a personal access token
2.  fork existing repository using the UI
3.  clone forked repository in the lab environment
4.  create a new branch
5.  make changes locally
6.  add and commit to the local branch
7.  push changes to the forked repository
8.  create a pull request to the upstream repository

## Pre-requisites

This lab is designed to be run on Skills Network - Cloud IDE which is runs on a Linux system in the cloud and already has git installed.
If you intend to run this lab on your own system, please ensure you have git (on Linux or macOS) or GitBash (on Windows) installed.

# Exercise 1: Generate personal access token

The first step is to generate an access token from GitHub.com. Follow the lab named **[Generate GitHub personal access token](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/create-personal-token/instructions.md.html)** and copy the access token to use as password in the steps below.

# Exercise 2: Fork the repository

To fork a source repository, complete the following steps:

1.  Log in to GitHub and go to this project's [sample source repository](https://github.com/ibm-developer-skills-network/gkpbt-css-circle). This is the upstream repository for your project.

2.  At the top right of the screen, click **Fork** and select your own GitHub account as the destination for the fork.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/github-fork-upstream.png)

A copy of the source repository has now been added as one of your GitHub repositories. This is the origin repository for your repository.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/origin-repo.png)

# Exercise 3: Clone the forked repository

A clone is a local copy of a repository. Before you can clone the forked repository, you first need its HTTPS URL, which provides secure access to it.

To clone the forked repository, complete the following steps:

1.  In your list of repositories, click the forked repository. On the repository's main page, click the **Code** button.

2.  Click the clipboard icon to copy the URL. Make sure the `HTTPS` tab is active.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/github-origin-https.png)

3.  Let's export this URL in an environment variable so it's available for us to use in the later steps:

    ```
    export ORIGIN=<your repository HTTPS URL>
    ```

    {: codeblock}

4.  Open the terminal in the lab environment by using the menu in the editor: Terminal > New Terminal.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-terminal.png)

5.  Run the following command with the `HTTPS` URL you copied earlier:

    ```
    git clone $ORIGIN
    ```

    {: codeblock}

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-clone.png)

    The command clones the repository that is on GitHub into your current directory.

# Exercise 4: Explore the cloned repo

To become familiar with the cloned repo, complete the following steps:

1.  Click on the Explorer icon as shown in the following image:

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-project.png)

2.  Click on Project and expand the folder of the project you just cloned. You can open the files in the editor on the right side by clicking on the file name.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-editor.png)

# Exercise 5: Create the `feature-circle-500` branch

We will now add a new feature to the source code. We are asked to make the circle bigger with a size of 500x500. Before we make this change, we will create a new branch.

1.  Navigate to our repository using `cd gkpbt-css-circle` {: codeblock}

2.  Create a new branch using the `git checkout -b feature-circle-500` {: codeblock} command. Notice that we used a single command instead of creating a branch and then checking it out. The `-b` flag creates the branch if it does not already exist.

3.  You can check that you are in the new branch by using the `git status` command.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-new-branch.png)

# Exercise 6: Make required code changes

1.  Let's change the width and height to 500px each. Open the `style.css` file from the file explorer and change the code as follows:

    ```
    .blue {
                background-color:blue
    }
    .circle{
                border-radius:50%;
                width:500;
                height:500px;
    }
    ```

    {: codeblock}

2.  If you do a `git status` {: codeblock} at this point, you will see a change is shown. This change is not staged at this point, but Git is aware of it.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-change-status.png)

3.  Optionally, you can use the `git diff` command to see the changes in more detail:

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-git-diff.png)

    Notice the text in red was deleted and the text in green was added. Essentially, we changed the height and width from 300px to 500px each.

# Exercise 7: Add and commit your changes

A commit is Git's way of recording your file changes, similar to how you might save an edited document. To commit the change that you made in the previous exercise, you first need to add it to a staging area. Git will then take the staged snapshot of changes and commit them to the project. Remember, Git will never change files unless you explicitly ask it to.

To commit your new file, complete the following steps:

1.  To move the changes from your working project directory to the staging area, type the following command in the Terminal window:

    ```
    git add .
    ```

    {: codeblock}

    The `git add` command has several options. The single `.` adds all untracked files in the current directory and subdirectories to the staging area. Alternatively, you can add the single file you created by using the `git add style.css` command. Finally, you can use `git add -A` to recursively add all files from the top level git folder.

2.  If you check the status at this point, you will see the file has changed from Untracked to `Changes to be committed`:

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-add-status.png)

3.  To commit the new file to the local repository, you need to first tell git who you are. Type in the following commands to set your email and username. The email should be the same as your GitHub email.

    Set your email:

    ```
    git config --global user.email "email@example.com"
    ```

    {: codeblock}

    Set your name:

    ```
    git config --global user.name "Your Name"
    ```

    {: codeblock}

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-git-config.png)

4.  Type the following command in the Terminal window to commit the file. **Note**: It's always a good practice to add a description for the commit so you can remember what the change was if you have to refer to it later. We add a description using `-m`, followed by our message:

    ```
    git commit -sm "Changing the height and the width of the circle"
    ```

    {: codeblock}

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-commit.png)

As you can see, `git status` now says there is nothing to commit and the working tree is clean. The new file is now ready to be pushed from your local system to origin on GitHub.

# Exercise 8: Merge your branch back into main branch

If you are happy with your changes in the `feature-circle-500` branch, you can now merge it back into your local `main` branch by following these steps:

1.  Confirm that you are currently in the `feature-circle-500` branch.
    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-branch-confirm.png)

2.  Check out the `main` branch

    ```
    git checkout main
    ```

    {: codeblock}

    If you run `git branch` again, you should see the `*` against the `main` branch.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-confirm-branch-main.png)

3.  Merge the \`\`branch into`main`.

    ```
    git merge feature-circle-500
    ```

    {: codeblock}

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-git-merge.png)

4.  Confirm the change was merged by using the `git log` command. We are using `--oneline` flag to display logs more concisely.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-merge-confirm.png)

# Exercise 9: Delete the `feature-circle-500` branch

Since you are done making the change, let's delete the `feature-circle-500` branch. Follow these steps:

1.  Ensure you are on the `main` branch. If not, check it out first

    ```
     git checkout main
    ```

    {: codeblock}

2.  Delete the `feature-circle-500` branch
    ```
    git branch -d feature-circle-500
    ```
    {: codeblock}

3.  You can confirm the branch was deleted by listing all branches

    ```
    git branch
    ```

    {: codeblock}

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/git-branch-delete.png)

# Exercise 10: Push your changes to origin

This push will synchronize all the changes you made on your local system with your fork repository on GitHub.

To push your update to GitHub, complete the following steps:

1.  In the Terminal window, run the following command:

    ```
    git push origin main
    ```

    {: codeblock}

    Once you submit that command, vs code will bring up a dialog on the top of the screen for your username and password. The username is your GitHub email The password is the token you created in **Exercise 1**.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-git-username-password.png)

    If your username and password were accepted, you should see the changes pushed to GitHub in the terminal.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-git-push-confirm.png)

2.  Go to the fork repository in your GitHub account and verify that the local changes have now been added to the main branch.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/lab-main-ui-confirm.png)

# Exercise 11: Create a pull request

The final step is to request that the original project pull in the changes you've made to your fork. To merge your changes to the original repository, you need to create a pull request.

To create a pull request, complete the following steps:

1.  Ensure you are on the **Code** tab. Click on the **Contribute** button and then on **Open pull request**.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/cli-lab-pull-request-start.png)

2.  In the "Comparing changes" panel, GitHub shows you that it is comparing the main branch of your fork to the main branch of the original repository, and that your changes can be merged. Click the **Create pull request** button.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/cli-lab-compare-pr.png)

3.  You are taken to the **Open pull request** screen. Notice that your commit message appears as the title of the pull request. Since we signed the commit, the body contains the email you configured in the previous step.

    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/cli-pr-screen.png)

**Note**: For the purposes of this lab, your pull request will be processed and closed automatically. **Copy the URL of this pull request as you will need to submit it for peer review.**

You should see the following message in your pull request after a few minutes:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/git-fork-pr-commands/images/cli-lab-auto-close-pr.png)

# Exercise 12: Practice on your own

1.  Create a new branch called `feature-add-color`.

    <details><summary>Click here for the solution</summary>

    ```bash
    git branch feature-add-color

    ```

    {: codeblock}

     </details>

2.  Make `feature-add-color` the active branch.

    <details><summary>Click here for the solution</summary>

    ```bash
    git checkout feature-add-color

    ```

    {: codeblock}

     </details>

3.  Add another css rule as follows:
    ```
    .red {
         background-color:red
     }
    ```
    {: codeblock}

4.  Stage this change.

    <details><summary>Click here for the solution</summary>

    ```bash
    git add -A

    ```

    {: codeblock}

     </details>

5.  Commit the changes in your `feature-add-color`.

    <details><summary>Click here for the solution</summary>

    ```bash
    git commit -sm 'adding red color feature'

    ```

    {: codeblock}

     </details>

6.  Merge the changes in `feature-add-color` into `main`.

    <details><summary>Click here for the solution</summary>

    ```bash
    git checkout main && git merge feature-add-color

    ```

    {: codeblock}

     </details>

7.  delete the `feature-add-color` branch.

    <details><summary>Click here for the solution</summary>

    ```bash
    git branch -d feature-add-color

    ```

    {: codeblock}

    </details>

8.  Create a new pull request for this feature in the upstream repository using the GitHub UI.

## Summary

In this lab, you have learned how to fork an upstream repository into your own account and then clone it locally in the lab environment. You then learned how to synchronize changes in your local repository with remote GitHub repositories using pull requests.

## Author(s)

<h4> Upkar Lidder <h4/>

### Other Contributor(s)

<h4> Richard Ye <h4/>

## Changelog

| Date       | Version | Changed by   | Change Description               |
| ---------- | ------- | ------------ | -------------------------------- |
| 2022-01-17 | 1.0     | Upkar Lidder | Initial version created          |
| 2022-01-27 | 1.1     | Richard Ye   | Corrected and added instructions |
