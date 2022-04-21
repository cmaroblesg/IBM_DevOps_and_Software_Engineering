# Lab: Create and merge a branch in your GitHub repository

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/IDSNlogo.png" width="200" height="200">

**Estimated time**: 15 minutes

## Objectives

After completing this lab you will be able to:

1.  Create a branch
2.  Commit changes to a child branch
3.  Open a pull request
4.  Merge a pull request into the main branch

## Prerequisites

This hands-on lab requires you to have created a GitHub account and added a project to it, as covered in the [Getting started with GitHub](GitHub1\_Getting_Started.md.html) lab.

> NOTE: In the past the default branch in your GitHub repo used the name `master`. Effective Oct 1. 2020, all new GitHub repositories use the more inclusive term `main` as the name of the default branch instead of `master`.

## 1. Create a branch

You can create or delete branches using your repository's GitHub web page. To add a branch to your repository, complete the following steps:

1.  Go to you repository's main page. Note that when you created your repository, the **main** branch was created for you:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Check_Repo.png "Check Repo")

2.  At the top of the file list, locate the **Branch** drop-down menu. (By default, the menu displays **Branch: main**.) Click the drop-down menu, type the name of the branch you want to create, and press Enter on your keyboard.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Enter_branch_name.png "Enter_branch_name")

    Your repository now has two branches: **Main** and **Child_Branch**. You can click the drop-down menu to see your branches.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Branch_number_changed.png "Branch_number_changed")

Any files that were in the **main** branch have now been copied to **Child_Branch**. Note, however, that when you add or edit a file in **Child_Branch**, that change will not automatically be made in the **main** branch.

## 2. Add a file to a branch

To add a file to your new branch, ensure that **Child_Branch** (or whatever name you gave your branch) is displayed in the **Branch** drop-down menu and complete the following steps:

1.  Click **Add file > Create new file** to create a file in the repository.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Create_file_branch.png "Create_file_branch")

2.  Type a name and extension for the file -- for example, `testchild.py` -- and add the following lines to the body of the new file:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Add_content_branch.png "Add_content_branch")

3.  Scroll to the bottom of the page, add a description of the file you are about to add (note that the description is optional), and click **Commit**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Commit_branch_file.png "Commit_branch_file")

    The file is added to your child branch.

## 3. Open a pull request

The file that you added to your child branch is not automatically added to the **main** branch. (You can check this by using the **Branch** drop-down menu to go to the **main** branch; note that there is no `testchild.py` file in the file list):

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Master_check.png "Master_check")

You can also compare the two branches and open a *pull request*, which will enable you to copy the changes that you've made in the child branch -- in this case, adding a new file -- to the **main** branch.

1.  In **Child_Branch**, click the **Compare & pull request** button.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Compare_Pull.png "Compare_Pull")

2.  Scroll to the bottom of the page and note that there is **1 changed file** listed.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/File_Changed.png "File_Changed")

3.  Scroll up and note that GitHub is comparing the **main** and **Child_Branch** branches and that there are no conflicts between the two. Optionally, you can add a comment to the pull request. Click **Create pull request**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Create_Pull_Request.png "Create_Pull_Request")

    The pull request is created and can now be merged by a repository administrator.

## 4. Merge a pull request

To merge a pull request into a project, complete the following steps:

1.  Click the **Pull requests** tab. A list of pending pull requests is displayed.

2.  Click the pull request that you want to merge into the main project. If you are satisfied with the changes, click **Merge pull request** to accept the pull request and merge the updates. (You can add a comment if you choose.)

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Merge_Request.png "Merge_Request")

3.  When you click **Merge pull request**, a **Confirm merge** button is displayed. Click that button to complete the merge.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Confirm_Merge.png "Confirm_Merge")

    The pull request has now been merged successfully. Note that you can delete the child branch because your changes have been incorporated into the **main** branch.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Merge_Success.png "Merge_Success")

    Check the list of files in the **main** branch to confirm that it now includes the file that you added in the pull request.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/File_Add_Master.png "File_Add_Master")

## Summary

Congratulations! You've now learned how to create a branch, edit and commit  changes in that branch, open a pull request, and merge the pull request into your main project. We encourage you to continue to experiment with branches and pull requests to become more familiar with the concepts and processes.

## Tutorial details

**Author:**

*   Malika Singla

**Other contributor:**

*   Rav Ahuja

**Changelog:**

| Date       | Version | Changed by    | Change Description                                                                  |
| ---------- | ------- | ------------- | ----------------------------------------------------------------------------------- |
| 2022-01-14 | 0.4     | Rav Ahuja     | Added note about main branch                                                        |
| 2020-07-16 | 0.4     | Malika Singla | Spell check, steps added                                                            |
| 2020-07-14 | 0.3     | Rav Ahuja     | Changed logo, updated title, intro, objectives, added Effort, Authors and Changelog |
| 2020-07-13 | 0.2     | Malika Singla | Added to GitLab and made some formatting changes, added objectives, etc.            |
| 2020-06-30 | 0.1     | Malika Singla | Drafted initial version                                                             |
