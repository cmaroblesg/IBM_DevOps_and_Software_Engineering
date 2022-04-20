## Lab: Getting started with GitHub

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/IDSNlogo.png" width="200" height="200">

**Estimated time**: 10 minutes

In this lab, you will get started with GitHub by creating a GitHub account and project. You will then add a file to the project using the GitHub web interface.

## Objectives

After completing this lab, you will be able to:

1.  Describe GitHub
2.  Create a GitHub account
3.  Add a project / repository
4.  Create and edit a file
5.  Upload and commit a file

## GitHub overview

Before we learn to use GitHub, let's first review Git. *Git* is an open source version-control system for software development. It is simply a place where you can collect all your folders and files for a project. This collection of folders and files is usually called a repository.

*GitHub* is a Git repository hosting service, but it adds many of its own features. While Git is a command-line tool and you also need to host and maintain a server using the command line, GitHub provides the Git server for you, as well as a web-based graphical interface. It also provides access control and several collaboration features, such as wikis and basic task management tools, for every project.

GitHub provides cloud storage for source code, supports all popular programming languages, and streamlines the iteration process. GitHub includes a free plan for individual developers and for hosting open source projects.

## 1. Creating a GitHub account

To create an account in GitHub, complete the following steps:

1.  Go to the [Join GitHub page](https://github.com/join) and create an account. **Note**: If you already have a GitHub account, log in now.

2.  Provide the necessary details to create an account as shown below. When you have finished, click **Create account**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Create_account.PNG)

3.  Click **Verify** to verify the account and then click **Done**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Verify.PNG "Verify")

4.  After you have verified, click **Join a Free Plan**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/JoinFreePlan.PNG "Join Free Plan")

5.  Select your reasons for joining GitHub and click **Complete Setup**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/CompleteSetup.PNG "Complete Setup")

6.  You will receive a verification email from GitHub. Click the enclosed link to verify your email. **Note**: If you do not receive a verification email, click **Resend verification email**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/VerifyEmailAddress.PNG "Verify Email Address")

    When you have verified your email, you will see a screen that looks like this:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/EmailVerfied.png "Email Verified")

## 2: Add a project / repository

To add a new repository, complete the following steps:

1.  At the top right of the GitHub home page, click on the "+" icon and select **New repository**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Create_repo.png "New Repo")

2.  Enter a repository name and select the **Initialize this repository with a README** check box.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Repo_details.png "Repo Details")

3.  Click **Create repository**. The repository is created and its home page is displayed.

Next, you'll start editing the repository.

## 3: Create and edit a file

**Edit a file**

Although you will normally create a file before you edit it, in this case the `README.md` file has already been created for you. To edit that file, complete the following steps:

1.  Your repository root folder contains just one file: `README.md`. Click the pencil icon at the right to edit the file.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Edit_file.png "Edit File")

2.  Add some text to the file.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Add_text.png "Add Text")

3.  Scroll to the bottom of the file and click **Commit changes**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Commit.png "Commit")

4.  Confirm that the text you added to the file has been saved.

**Create a new file**

1.  Click on the repository name to go back to the main branch, similar to this repository called `testrepo`.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Add_file1.png "Add_file1")

2.  Click **Add file** and select **Create new file** to create a new file in the repository.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Create_new_file.png "Create New File")

3.  Enter a file name and extension; for example, `firstpython.py`. Add the lines of code displayed in the following image to your file:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/Add_filename.png "Add filename")

4.  Scroll to the bottom of the page. You can optionally add a description of your update (for example, "Adding a new file"). Click **Commit** to create your new file.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/commit_newfile.png "Commit New file")

    Your file is now added to your repository and the repository listing shows when the file was added or last revised.

## 4. Upload and commit a file

To upload a local file and commit it to your repository, complete the following steps:

1.  On your repository page, click **Add file** and then select **Upload files** to upload a file.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/upload.png "Upload")

2.  Click **choose your files** and choose a file from your computer. You can upload any file (for example, a .txt, .ipynb, or .png file) to the repository.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/select_files.png "Select files")

3.  When the file finishes uploading, click **Commit changes**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/commit_upload.png "Commit Uplaod")

    Your file is uploaded in the repository.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/check_change.png "Check change")

## Summary

Congratulations! In this lab, you have learned how to create a new repository, add a new file, edit a file, upload a file, and commit your changes. We encourage you to continue to update your repository to become familiar with the processes that you have learned.

## Tutorial details

**Authors:**

*   Romeo Kienzler
*   Malika Singla

**Other contributors:**

*   Rav Ahuja
*   Upkar Lidder

**Changelog:**

| Date       | Version | Changed by     | Change Description                                                                  |
| ---------- | ------- | -------------- | ----------------------------------------------------------------------------------- |
| 2020-08-18 | 0.6     | Upkar Lidder   | Updated GitHub Overview section                                                     |
| 2020-07-16 | 0.5     | Malika Singla  | Spell check, step number added                                                      |
| 2020-07-14 | 0.4     | Rav Ahuja      | Changed logo, updated effort, title, intro, objectives, added Authors and Changelog |
| 2020-07-13 | 0.3     | Malika Singla  | Added to GitLab and made some formatting changes, added objectives, etc.            |
| 2020-07-03 | 0.2     | Malika Singla  | Ported to markdown and added GitHub account signup, new screenshots, etc.           |
| 2020-06-30 | 0.1     | Romeo Kienzler | Drafted initial version                                                             |

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
