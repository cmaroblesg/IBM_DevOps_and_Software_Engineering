## Generate an SSH key

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/GitHubLabs/images/IDSNlogo.png" width="200" height="200">

**Estimated time**: 20 minutes

## What is an SSH key?

An SSH key is an access credential in the SSH protocol. Its function is similar to that of user names and passwords, but the keys are primarily used for automated processes.

## Generating an SSH key

To generate an SSH key, complete the following steps:

1.  Launch a terminal. If you are using Windows, launch Git Bash.

2.  Type the following command in your terminal, replacing \<your email address> with the email address that is linked to your Github account. When you have typed the command, press Enter.

    `ssh-keygen -t rsa -b 4096 -C "<your email address>"`

    A new SSH key is generated.

3.  You will be prompted to enter a directory to save the key. You can simply press Enter to accept the default location, which is an .ssh folder in the home directory. This means you will be able to locate the key in `~/.ssh/id_rsa`.

4.  You will be prompted to choose a passphrase. You also have the option not to create a passphrase. To skip the passphrase, press Enter twice to confirm that the passphrase is empty.

5.  **Optional**: To navigate to the .ssh directory, and check the contents of the directory, run the following commands in the terminal:

    `cd ~/.ssh`

    and then,

    `ls`

    When you list the contents of the .ssh directory, you should see `id_rsa` and `id_rsa.pub` in the list of contents, where `id_rsa` is the private version of your key and `id_rsa.pub` is the public version of your key.

6.  You now need to add the SSH key to the ssh-agent, which helps with the authentication process. To start the ssh-agent, run the following command in the terminal:

    `eval "$(ssh-agent -s)"`

7.  To add the key to the agent, run the following command in the terminal:

    `ssh-add ~/.ssh/id_rsa`

## Summary

Congratulations! You have now learned how to generate the SSH key.

## Tutorial details

**Author:**

*   Malika Singla
*   Sannareddy Ramesh

**Changelog:**

| Date       | Version | Changed by        | Change Description                                           |
| ---------- | ------- | ----------------- | ------------------------------------------------------------ |
| 2020-08-23 | 0.4     | Ramesh Sannareddy | Modified step1 to include instructions for windows and linux |
| 2020-07-22 | 0.3     | Malika Singla     | Removed quotes and replaced with italic                      |
| 2020-07-16 | 0.2     | Malika Singla     | Spell check, step number added                               |
| 2020-07-15 | 0.1     | Malika Singla     | Initial version created                                      |

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
