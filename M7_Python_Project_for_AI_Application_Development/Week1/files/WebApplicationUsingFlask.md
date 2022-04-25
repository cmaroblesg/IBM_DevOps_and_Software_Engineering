# Hands-on Lab: Web Application using Flask

<center>
    <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

## Web Application using Flask

Estimated time needed: **30** minutes

## Objectives

After completing this lab you will be able to:

*   Install flask
*   Create API end points in python
*   Create and run a web application using Flask

# SetUp

1.  Open a terminal window by using the menu in the editor: Terminal > New Terminal. <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/new-terminal.png" width="75%">

2.  Install the flask package that you will need to complete the exercises.

```
pip3 install flask==1.1.4
```

{: codeblock}

3.  In the terminal, change to your project folder.

```
cd /home/project
```

{: codeblock}

4.  Clone the git repository.

```
git clone https://github.com/ibm-developer-skills-network/rlkee-flaskproject.git
```

{: codeblock}

5.  Change to the directory named **rlkee-flaskproject/practice_labs**.

```
cd rlkee-flaskproject/practice_labs
```

{: codeblock}

6.  List the contents of this directory to see the artifacts for this lab. You must have a few exercise files that you will be running in the steps to follow.

```
ls
```

7.  You can also view the files cloned in the explorer.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/clone_filesexplore.png" width="50%">

# Exercise 1: First WebApplication

In this exercise we are just building a very primitive web application with `flask`, which serves one root endpoint `/` and returns **Hello World!** string when the endpoint is accessed. The root endpoint is when you just type the IP address and the port. For example, `http://127.0.0.1:5000` is a root endpoint.

1.  In the files explorer view FirstWebApplication.py.

    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/firstWebApplication.png" width="75%">

2.  In the terminal run the following command.

```
python3 FirstWebApplication.py
```

{: codeblock}

3.  This will start the server. You should see the following on your screen, indicating the server is running and is waiting for requests. Note down the port number. The default port number is 5000.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/firstwebapp_server_running.png" width="75%">

4.  Click on the Launch Application on the menu bar.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/firstWebApplication_launch.png" width="75%">

5.  Enter the port number at which the server is running.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/firstwebapp_launchapp_port.png" width="75%">

6.  A new browser tab opens up.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/helloworldbrowser.png" width="75%" style="border:solid 1px grey">

7.  Close the browser tab.

8.  Press Ctrl+C in the terminal to stop the server.

# Exercise 2: WebApplication with Template Rendering and static resources

In this exercise, we will go further than just a primitive web application. We will create a **Book Manager** web application.
This application will render HTML page as template, through the
root endpoint `/`. We will also have other endpoints which will be used internally by the HTML page through  Javascript.

1.  In the terminal, check if you are in the practice_labs directory. If not change to that directory with the following command.

```
cd /home/project/rlkee-flaskproject/practice_labs
```

{: codeblock}

2.  Analyze the code in bookManager.py in the explorer. See the end points that are being served. Exlpore the templates and the static folder. Observe, how the code in `index.html` uses the templates and the static files.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/bookmanagerfiles.png" width="75%" style="border:solid 1px grey">

3.  In the terminal run the following command, to start the application server.

```
python3 bookManager.py
```

{: codeblock}

4.  You will see the server running on port 5000, the default port.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/bookmanager_server.png" width="75%" style="border:solid 1px grey">

5.  Click on **launch application** and enter the port number `5000` just as you did in the previous exercise.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/launchapplication_bookmgr.png" width="75%">

6.  Enter the port number `5000` and click **OK** to launch the broswer tab.

     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/bookmanager_browser.png" width="75%" style="border:solid 1px grey">

7.  Enter *Book* and *Author* and click on **Add Book** and see the list of books added.

Congratulations! You have completed this lab section. You should now be familiar with creating Web Application with Flask.

## Authors

Lavanya

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
| ----------------- | ------- | ---------- | ---------------------------------- |
| 2021-05-14        | 0.1     | Lavanya    | Created initial version of the lab |

Copyright © 2020 IBM Corporation. All rights reserved.
