# Lab: Adding an SSH key to GitHub

<img style="float:left;" src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/IDSNlogo.png" width="200" height="200">

**Estimated time**: 15 minutes

## Prerequisites

This hands-on lab requires you to have already generated an SSH key. See the [Generating an SSH key](SSH_Key.md.html) lab for instructions.

## Steps

To add an SSH key to GitHub, you need to copy the SSH key that you generated in the previous lab. Open a terminal and then complete the following steps:

1.  In the terminal, run the following command:

    `cat ~/.ssh/id_rsa.pub | clip`

    **Note**: If `clip` doesn't work, run `cat ~/.ssh/id_rsa.pub` in the command line and the copy the output.

2.  Sign in to GitHub. At the top right, click the drop-down menu on your profile image and select **Settings**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/settings.png)

3.  From the "Personal settings" menu, select **SSH and GPG keys**, as shown in the following image:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/SSHKey_option_new.png)

4.  Click **New SSH key**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/AddNewSSH.png)

5.  Enter a title for the new SSH key. In the **Key** field, paste the key that you copied in step 1, above. The pasted key should include **Your email address** at the end, as shown in the following image:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0105EN-Coursera/labs/GitHub/images/add_ssh_keytoaccount_new.png)

6.  Click **Add SSH Key**. The SSH key is added to your account.

## Summary

Congratulations! You have now learned how to add an SSH key to GitHub.

## Tutorial details

**Author:**

Malika Singla

**Changelog:**

| Date       | Version | Changed by    | Change Description                              |
| ---------- | ------- | ------------- | ----------------------------------------------- |
| 2020-07-16 | 0.2     | Malika Singla | Spell check, screenshot updated and steps added |
| 2020-07-15 | 0.1     | Malika Singla | Initial version created                         |

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
