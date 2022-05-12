![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/IDSNlogo.png){ width=200 height=200 }

# Exploring IBM Cloud Functions

**Estimated time needed:** 20 minutes

In this lab, you will have the opportunity to begin exploring IBM Cloud Functions. You will use the IBM Cloud console to interact with the various IBM Cloud Functions entities and familiarize yourself with the interface.

## Objectives

After completing this lab, you will be able to:

1.  Access the IBM Cloud Functions interface in the cloud console
2.  View getting started information for Cloud Functions
3.  Create an IBM Cloud Functions namespace
4.  View the interface for creating and listing entities
5.  View the cloud shell where CLI commands can be used to interact with Cloud Functions

## Exercise 1 : Log in to IBM Cloud and Access Cloud Function

In this exercise you will log into your IBM Cloud account in a web browser, visit the IBM Cloud console, and peruse the IBM Cloud Functions UI.

1.  Go to the [IBM Cloud console](https://cloud.ibm.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMCD0250ENSkillsNetwork23783333-2021-01-01). Log in with your account.

2.  There are a few ways to access the Cloud Functions interface. The easiest way is to click on it in the left navigation.

![Functions left nav](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/functions_left_nav.png)

1.  This brings you to the overview page. To begin, read the contents of this overview page. There are descriptions, features, and use cases that can help you better understand the tool.

## Exercise 2 : Getting Started with IBM Cloud functions

In this exercise you will browse the getting started information provided in the Cloud Functions interface.

1.  Click **Getting Started** in the navigation menu to open the dropdown.

![Getting started nav](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/getting_started_nav.png)

1.  Click the **Pricing** option to view pricing for functions. The exercises in these labs will not cost you anything.

2.  Click the **Concepts** option if you want to review some IBM Cloud Functions concepts.

## Exercise 3 : Create a Namespace

In this exercise you will create a namespace to house the other entities you create within Cloud Functions.

1.  At the top of your screen, note that you are likely targeting a namespace already. This is a default namespace created for you. Don't worry if you're not targeting one; you'll create one next.

2.  Go to the namespaces dropdown and click **Create Namespace**.

![Create namespace dropdown](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/create_namespace_dropdown.png)

1.  Fill out the namespace details. Give it a name like **\<your_initials>\_test** or whatever you would like. You can keep the default resource group and location or change them if you'd like. You can optionally give it a description.

2.  Click **Create** to create the namespace.

3.  Note that you should know be targeting your new namespace.

4.  Click **Namespace Settings** in the navigation menu.

![Namespace settings nav](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/namespace_settings_nav.png)

1.  Review the details of your namespace. Much of this information was populated by your in the previous step. Note the assigned GUID for this namespace, as well as the ability to delete the namespace.

## Exercise 4 : Exploring IBM Cloud Functions Entities

In this exercise you will explore how to create and view various other entities within IBM Cloud Functions.

1.  Return to the overview page by clicking **Functions** at the top of the navigation menu.

![Functions nav](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/functions_nav.png)

1.  Click **Start Creating**.

2.  Look at the many entities you can create within IBM Cloud Functions. These include actions, sequences, and triggers.

3.  Click **Action** to view how an action is set up.

4.  On this page you can create actions by providing a name, selecting or creating an enclosing package, and choosing a runtime. Don't create one yet; you'll do this in a subsequent lab.

5.  Click **Actions** in the navigation menu in order to view the actions list. Since you have no actions, there will only be a button to create an action. But this is where actions will be listed. The same is true for triggers and APIs.

![Actions nav](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/actions_nav.png)

## Exercise 5 : View the Cloud Shell

In this exercise you will open a session of the Cloud Shell to see how IBM Cloud CLI commands can easily be run.

1.  At the top right of the cloud console, click the icon that looks like a terminal. This opens a new tab.

![Cloud shell icon](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%202/images/cloud_shell_icon.png)

Once this loads, you will be in a session of the cloud shell. The cloud shell is a browser-based terminal environment that provides all the tools needed to work with IBM Cloud in one convenient place. Installing CLIs and dependencies on your local machine can be time-consuming or difficult. The Cloud Shell provides the IBM Cloud CLI, plugins for IBM Cloud services, and other common CLI utilities like `git`, in order for you to get up and running more quickly.

1.  Type `ibmcloud` into the terminal and hit enter. This will list the top-level commands available with the IBM Cloud CLI.

The videos in this course demonstrate how to use CLI commands to work with Cloud Functions, but the labs often use the web interface instead. Feel free to perform any actions in the Cloud Shell instead of in the UI if you want to practice that way as well. For additional practice, you can perform actions in both places.

## Conclusion

In this lab you logged into IBM Cloud and accessed the IBM Cloud Functions UI. From there, you explored the interface, including how to create and view entities, and how to view getting started information. This is a great foundation for creating with IBM Cloud Functions, which you'll be doing next!

## Author(s)

[Alex Parker](https://github.com/ajp-io)

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
