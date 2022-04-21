<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/project/images/IDSNlogo.png" width="200" height="200">

# Part 2 - GitHub CLI

**Estimated Time:** 60 minutes

## About This SN Labs Cloud IDE

This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia.

**Important Notice about this lab environment**
Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete this lab in a single session, to avoid losing your data.

## Scenario

Congratulations on starting your company's journey with Git and GitHub by open sourcing the simple interest calculator bash script. Your changes have been accepted and merged into a new global [repository](https://github.com/ibm-developer-skills-network/jbbmo-Introduction-to-Git-and-GitHub). Other developers have contributed to this repository over time as well. Your team has found a mistake in one of the markdown files. You are asked to fork this repository and fix the mistake by using Git CLI in the provided lab environment and opening a pull request.

## Objectives

After completing this lab you will have demonstrated that you can:

1.  Fork the upstream repository into your own account.
2.  Clone the code locally in the lab environment.
3.  Create a branch in the repository.
4.  Create a Pull Request from the forked repository to the upstream repository.
5.  Merge the branch back into the `main` branch.
6.  Revert a change that you made earlier.

**Note:** Throughout this lab you will be prompted copy and paste URLs into a notepad and save the notepad on your own device. These URLs will be uploaded for peer review in the Final Submission section of the course. You can use any notepad app to keep note of your URLs.

## Task 8: Fork the repository

1.  Log in to GitHub and fork this project's [sample source repository](https://github.com/ibm-developer-skills-network/jbbmo-Introduction-to-Git-and-GitHub).

2.  **Save the URL of your forked repository in a notepad to submit later for peer review.**

## Task 9: Fix the typo and submit the first pull request

1.  Clone the forked repository in the lab environment.

2.  Create a branch named `bug-fix-typo`.

3.  Change the footer in the main README.md file from

    ```
    © 2022 XYZ, Inc.
    ```

    to

    ```
    © 2021 XYZ, Inc.
    ```

4.  Add and commit your fix with a meaningful message.

5.  Push your fix to your forked repository (the origin) in the same branch. You will need to generate a personal access token from GitHub.com to use as your password in this step. Follow the instructions in the lab named **[Generate GitHub personal access token](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0131EN-SkillsNetwork/labs/create-personal-token/instructions.md.html)**.

6.  Create a pull request to the original upstream repository.

7.  Once the PR is closed by the GitHub bot, **save the URL in a notepad to submit later for peer review.**

8.  Merge the `bug-fix-typo` branch back into your main branch. This is an important step before you continue with Task 10.

## Task 10: Revert the typo and submit a second pull request

1.  Check out the main branch. The file should now read:
    ```
    © 2021 XYZ, Inc.
    ```
2.  Create a new branch named `bug-fix-revert`.
3.  Revert back the change you implemented in the previous task using the `git revert` command. The file should now read:
    ```
    © 2022 XYZ, Inc.
    ```
4.  Push the revert to your repository in the `bug-fix-revert` branch.
5.  Create a new pull request. As before, your second PR is closed automatically. **Save the URL of this PR in a notepad to submit later for peer review**

## Checklist

Save your notepad file locally for use in your submission later in this course. Check that you have all 3 URLs noted.

## Summary

Congratulations! You have completed both parts of the final project. You have demonstrated that you know how to create an open source project in Git, make changes to that project and make it available to the community. You can fork a GitHub repository, clone that repository to your local system, make changes to the local repository, commit the changes locally, push it back to your GitHub fork, and create a pull request to add your update to the original repository.

## Author(s)

<h4> Upkar Lidder <h4/>

## Changelog

| Date       | Version | Changed by      | Change Description                          |
| ---------- | ------- | --------------- | ------------------------------------------- |
| 2021-12-29 | 0.1     | Upkar Lidder    | Initial instructions for the final project  |
| 2022-01-13 | 0.2     | Alison Woolford | Updates to instructions for learner clarity |
| 2022-01-13 | 1.0     | Upkar Lidder    | Final version                               |

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
