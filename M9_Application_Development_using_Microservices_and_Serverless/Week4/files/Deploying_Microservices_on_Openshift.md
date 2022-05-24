# Deploying Microservices on OpenShift

You will have the opportunity to deploy a containerized application on OpenShift.

## Learning Objectives

*   Access the OpenShift console
*   Deploy an application on OpenShift using a git repository
*   Explore the OpenShift build and route

# Step 1: Access the OpenShift Console

This lab environment includes access to an OpenShift cluster. Accessing the OpenShift console is the easiest way to get started with OpenShift.

1.  Click **OpenShift Console** in this lab environment.

![OpenShift console button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%204/images/openshift_console_button.png)

2.  When the console loads, ensure that you are in the developer perspective.

![Developer perspective](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%204/images/developer_perspective.png)

# Step 2: Deploy an Application on OpenShift

1.  Click **+Add** in the left navigation to create an application on OpenShift.

2.  Click **From Git**. This will let us deploy an application directly from a git repo.

3.  Enter https://github.com/sclorg/nodejs-ex.git as the git repo URL.

This should automatically select the Node.js builder image since OpenShift detects that this is a Node.js app. This is a sample application provided by OpenShift.

4.  Leave all the default options and click **Create** at the bottom. This will take you to the topology view.

5.  Note the application in the topology view. It provides links to several key things. The outer circle is the application. The inner circle is the deployment. The GitHub logo links out to the git repository used for this deployment. This two arrows in a circle link to the build for this app. This will be a green checkmark if the build is complete. And the arrow pointing out of a box links to the route for this app. The route is what makes the app available on the internet.

![Topology deployment](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0250EN-SkillsNetwork/labs/module%204/images/topology_deployment.png)

# Step 3: Explore the Deployment Resources

Let's explore the resources that we mentioned above that come with this deployment.

1.  Click the two arrows in a circle. This will take you to the logs for the build. The build takes the git repository and builds it into a container that can run on OpenShift.

2.  The logs for the build show how the git repository is downloaded, a Dockerfile is generated, and the built container image is pushed to the registry.

3.  Click **Topology** to return.

4.  Click the arrow coming out of the box. This is the route. This will launch this sample app.

5.  Read through the welcome note and instructions for this app. This is maintained by OpenShift, so we cannot guarantee that all links will redirect, but reading through it will give you some basic insights into powerful OpenShift features.

# Summary

In this final project, you have leveraged the serverless and microservices knowledge that you acquired throughout this course. You interacted with IBM Cloud to provision two types of services: a Cloudant database and Cloud Object Storage. You created actions and sequences to store entries in and retrieve entries from the Cloudant Database. You exposed those sequences using web actions and an API. And finally, you hosted the front end for the guestbook web application as a microservice on OpenShift and as static files on Cloud Object Storage.
