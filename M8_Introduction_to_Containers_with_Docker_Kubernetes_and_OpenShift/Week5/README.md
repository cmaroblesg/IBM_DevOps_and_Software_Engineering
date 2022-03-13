# Final Assignment
## Introduction
For the Final Project, you will put into practice the tools and concepts learned in this course, and deploy a simple guestbook application with Docker and Kubernetes.The entire application will be deployed and managed on OpenShift.

## Learning Objectives
* Build and deploy a simple guestbook application.
* Use OpenShift image streams to roll out an update.
* Deploy a multi-tier version of the guestbook application.
* Create a Watson Tone Analyzer service.
* Bind the Tone Analyzer service to your application.
* Autoscale the guestbook app.

## Readings
### Introduction to Final Project
The final assignment of this course is a project that will encourage you to use many of the tools and concepts that you've learned so far in this course. As you complete the project, you will need to take some screenshots to verify what you have done so that it can be graded in the Peer-graded Assignment. The final project is conducted on an OpenShift cluster.

To start, you will deploy a simple guestbook application that uses in-memory storage to retain the guestbook entries. Afterward, you will deploy a multi-tier web application that consists of a web front end, a Redis master and replicated slaves for storage, as well as an analyzer service that analyzes the tone of entries left in the guestbook. In order to utilize the analyzer service, you will have to create a free instance of Tone Analyzer in your personal IBM Cloud account.

Let's get started!

While IBM values the use of inclusive language, terms that are outside of IBM’s direct influence are sometimes required for the sake of maintaining user understanding. As other industry leaders join IBM in embracing the use of inclusive language, IBM will continue to update the documentation to reflect those changes.

* [Final Project: Scenario and Review Criteria](./files/projectScenario.pdf)
* [Hands-on Lab: Build and Deploy a Simple Guestbook App](./files/labs.cognitiveclass.ai.pdf)
