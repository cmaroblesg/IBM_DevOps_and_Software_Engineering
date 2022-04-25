<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
</center>

# Peer Review Assignment - Developers

Estimated time needed: **60** minutes

## Objectives

In this assignment you will:

*   Use Watson APIs to create functions.
*   Create a function that translates English to French.
*   Create a function that translates French to English.
*   Run coding standards check against the functions above.
*   Write unit tests to test the above functions.
*   Run unit tests and interpret the results.
*   Package the above functions and tests as a standard python package.

> **Important Notice** - Please keep in mind that sessions for this lab environment are not persisted. If you will not be completing the entire lab in one sitting, please save your code outisde of this environment, so you can resume your work without loss.

<details><summary><i>👉 Click here for instructions to save your code on github</i></summary>
Change to the project directory

```
cd /home/projects/xzceb-flask_eng_fr
```

{: codeblock}

Run these following commands replacing your github username and the email you use for loggin into github as appropriate.

```
git config --global user.email youremail@domain.com
git config --global user.name your_github_username

```

{: codeblock}

```
git add .
```

{: codeblock}

```
git commit -m"Temporary changes"
```

{: codeblock}

```
git push
```

{: codeblock}

</details>

## Provision Watson Translation Service

*   Before you start, ensure you have provisioned an instance of the Watson Language Translator service and have API information available.

## **Task1:** Write a function that translates English text to French in translator.py

1.  Open a terminal window by using the menu in the editor: Terminal > New Terminal.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/new_terminal.png" style="margin-top:10px; margin-bottom:10px">

2.  Go to the project home directory.

    ```
    cd /home/project
    ```

    {: codeblock}

3.  Run the following command to Git clone the project directory from the clone URL you had copied in the prework lab.

    ```
    [ ! -d 'xzceb-flask_eng_fr' ] && git clone <paste_your_repo_name>
    ```

    {: codeblock}

4.  Change to the `final_project` folder.

    ```
    cd /home/project/xzceb-flask_eng_fr/final_project
    ```

    {: codeblock}

5.  Create folder named `machinetranslation` and change to that directory.

    ```
    mkdir machinetranslation
    cd machinetranslation
    ```

    {: codeblock}

6.  Install the packages that you will be using in this code, namely `ibm_watson` and `python-dotenv`.

    ```
    pip3 install -q PyJWT==1.7.1 flask-appbuilder==3.4.4 markupsafe==1.1.1 httpx==0.20 Flask ibm-watson python-dotenv
    ```

    {: codeblock}

7.  Create a file `.env` under the `machinetranslation` directory, which maps the apikey and url of the Language Translator Service that you created in the IBM Cloud.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/environmentfile.png" style="margin-top:10px;margin-bottom:10px;">

    > <details><summary>👉 Click here to see where the credentials can be copied from</summary><img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/languagetranslator_credentials.png" widht="75%" style="border: solid 1px grey"></details>

     </details>

8.  In the explorer, go to the `machinetranslation` directory and create a new file called `translator.py`. Enter the following lines of code.

    ```py
    import json
    from ibm_watson import LanguageTranslatorV3
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    import os
    from dotenv import load_dotenv

    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']
    ```

    {: codeblock}

9.  Add code to create an instance of the IBM Watson Language translator in `translator.py`.
    > Hint : You may refer to the IBM Watson Language Translation API documents <a href="https://cloud.ibm.com/apidocs/language-translator?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0222ENSkillsNetwork23455715-2021-01-01&code=python">here.</a>

> 📷 Take a screenshot of your functions and save it as a .jpg or .png with the filename `translator_instance`.  You will be prompted to upload the screenshot in the Peer Assignement that follows.

10. Add function **englishToFrench** which takes in the `englishText` as a string argument, in `translator.py`. Use the instance of the Language Translator you created previously, to translate the text input in English to French and return the French text.

    ```python
    def englishToFrench(englishText):
        #write the code here
        return frenchText
    ```

    {: codeblock}

📷 Take a screenshot of your functions and save it as a .jpg or .png with the filename `e2f_translator_function`.  You will be prompted to upload the screenshot in the Peer Assignement that follows.

11. Add function **frenchToEnglish** which takes in the `frenchText` as a string argument, in `translator.py`. Use the instance of the Language Translator you created previously, to translate the text input in French to English and return the English text.

    ```python
    def frenchToEnglish(frenchText):
        #write the code here
        return englishText
    ```

    {: codeblock}

> 📷 Take a screenshot of your functions and save it as a .jpg or .png with the filename `f2e_translator_function`.  You will be prompted to upload the screenshot in the Peer Assignement that follows.

# **Task 2:** Write the unit tests for English to French translator and French to English translator function  in tests.py

1.  Create a new file called `tests.py` in the `machinetranslation` directory.
2.  Write at least 2 tests in `tests.py` for each method
3.  Test for null input for `frenchToEnglish`
4.  Test for null input for `englishToFrench`.
5.  Test for the translation of the world 'Hello' and 'Bonjour'.
6.  Test for the translation of the world 'Bonjour' and 'Hello'.
7.  Take a screenshot of your unit tests and save it as a .jpg or .png with the filename `translation_unittests`.

# **Task 3:** Check your code against python coding standards

1.  Run `pylint translator.py` to check the coding standard compliance in your code. Refer to this [exercise](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Static%20Code%20Analysis/Static_Code_Analysis.md.html) you did earlier, if needed.
2.  Make sure your rating is at least 7.
3.  📷 Take a screenshot of the output of the pylint analysis report showing your score and save it as a .jpg or .png with the filename `pylint_score`.

# **Task 4:** Run tests

1.  At the terminal run the command
    ```
    python3 tests.py
    ```
    {: codeblock}

2.  📷 Take a screenshot of test results and save it as a .jpg or .png with the filename **unit_test_results**.

# **Task 5:** Package the above functions and tests as a standard python package.

1.  Create `__init__.py` file in the directory `machinetranslation`.

2.  Create a folder called `tests` under the newly created folder

3.  Copy the unit `tests` into the tests folder

> 📷 Take a screenshot of the folder structure of the package ( From the menu go to View -> Explorer to set the explorer view) and save it as a .jpg or .png with the filename `package_folder_structure`.

# **Task 6:** Import the package into server.py and create flask end points

1.  Import the package `machinetranslation` in server.py.

2.  In the server.py, for end-point `/`, implement a method that renders the `index.html`.

3.  In the space provided in server.py for end-point `/englishToFrench` implement a method that uses the appropriate translation function through the package you created in the previous part. The function should take the English text as input through the request parameter and return a string.

4.  In the space provided in server.py for end-point `/frenchToEnglish` implement a method that uses the appropriate translation function through the package you created in the previous part. The function should take the French text as input through the request parameter and return a string.

5.  Push the code to GitHub.

<details><summary><i>👉 Click here for instructions to push your code to github</i></summary>Change to the project directory

```
cd /home/projects/xzceb-flask_eng_fr
```

{: codeblock}

*   Run these following commands replacing your github username and the email you use for loggin into github as appropriate.

```
git config --global user.email youremail@domain.com
git config --global user.name your_github_username

```

{: codeblock}

```
git add .
```

{: codeblock}

```
git commit -m"Final changes"
```

{: codeblock}

## Task - Generate Personal Access Token

*   Verify your email address if it hasn’t been verified on Github.

*   In the upper-right corner of any page, click your profile photo, then click Settings.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/profile_settings.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

*   In the left sidebar, click Developer settings.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/dev_settings.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

*   In the left sidebar, click Personal access tokens and click on `Generate Tokens`

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/PAT.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

*   Give your token a descriptive name. To give your token an expiration, select the Expiration drop-down menu, then click a default or use the calendar picker. Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select repo.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/new_personal_token.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

*   Click Generate token and make a note of it.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/generate_token.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

*   Make sure you copy the token and keep it safe. It is not visible to you again.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/copy_token.png" style="margin-left:30px;margin-top:10px;margin-bottom:10px;width:75%;border: solid 1px grey">

> **Treat your tokens like passwords and keep them a secret.**

> Once you have a token, you can enter the Personal Access Token as password when performing Git operations.

> The git `push` command will enable you to sync all the changes made locally to the GitHub web repository.

*   Run the following command with your actual HTTPS link:

    ```
    git push [HTTPS link]
    ```

    {: codeblock}

    You will be prompted by git for your username and password.

*   Type your GitHub username and for the password, enter the personal access token you generated in the previous task. When you are authenticated, all committed changes are synced with your GitHub repository.

You can now visit the GitHub repository page and check to ensure that the revised and newly added files are in place.

</details>

# **Task 7:** Run the server

1.  Change to the project directory and run the server from your terminal.

```
cd /home/project/xzceb-flask_eng_fr/final_project && python3 server.py
```

{: codeblock}

2.  You will see that the server starts up in port 8080.

3.  Click on `Launch Application` from the menu and connect to port 8080.

4.  A new browser window opens up with the index page.
    *   📷 Take a screen shot of the translation from English to French
    *   📷 Take a screen shot of the translation from French to English

# **Task 8:** (Optional) Deploy the application on IBM Cloud.

> Note : This will only work if Cloud Foundry is available.

1.  Change to the `final_project` directory.

    ```
    cd /home/projects/xzceb-flask_eng_fr/final_project
    ```

    {: codeblock}

2.  Login to the ibmcloud with your email and enter your password when prompted.

    ```
    ibmcloud login -u <your email>
    ```

    {: codeblock}

3.  Set the target region and owner. Run the followinf command after you  replace `REGION` with your region and the `OWNER` with your email id.

    ```
    ibmcloud target --cf-api https://api.REGION.cf.cloud.ibm.com -r REGION -o OWNER
    ```

    {: codeblock}

4.  Create an account space called `translator`.

    ```
    ibmcloud account space-create translator
    ```

    {: codeblock}

5.  Target the account space you just created.

    ```
    ibmcloud target -s translator
    ```

    {: codeblock}

6.  Replace line 3 in the `manifest.yml` to give a name for your web application.

7.  Deploy the application.

    ```
    ibmcloud app push
    ```

    {: codeblock}

8.  The route for your web application will be printed on the screen. Copy it to connect to it after the application successfully deploys.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/deploy_app.png" style="margin-top:10px;margin-bottom:10px">

    > Troubleshoot: You can check the logs by running, `ibmcloud cf logs <appname> --recent`

9.  You can see your deployed application listed in the [Cloud Foundry](https://cloud.ibm.com/cloudfoundry/public?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0222ENSkillsNetwork23455715-2021-01-01). To make changes and push your app again, stop and delete the application from [Cloud Foundry](https://cloud.ibm.com/cloudfoundry/public) and then execute `ibmcloud app push`.

# Congratulations!

You have completed the tasks for this project. In the peer assignement that follows, you will be required to upload the screenshots you saved in this lab.

## Authors

Lavanya

### Other Contributors

Ramesh Sannareddy

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
| ----------------- | ------- | ---------- | ---------------------------------- |
| 2021-05-14        | 1.0     | Lavanya    | Created initial version of the lab |

Copyright © 2020 IBM Corporation. All rights reserved.
