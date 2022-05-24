# ORM: MicroServices w/ Serverless
## Introduction
In this module, you’ll learn how to use actions, triggers and rules that help you quickly accomplish your cloud application programming tasks. You’ll be guided step-by-step through how to create and invoke action retrieve results. Then, you’ll discover how to invoke an action using parameters and how to bind specified default parameters to an action. Next, learn how triggers and rules help you organize and reduce programming complexity. Then, delve the benefits of exposing actions as APIs, the benefits of implementing web actions, and how using API gateways eases application development. Finally examine the advantages and constraints of container tools like Kubernetes. All programming tools, including container tools such as Kubernetes have specific challenges. Round out this module’s learning with insights about how IBM Code Engine addresses common Kubernetes challenges.

## Learning Objectives
* Create and invoke actions, including sequence actions using IBM Cloud Functions actions
* Retrieve the result of an action invocation
* Invoke an action with parameters​ and bind default parameters to an action
* Identify, describe, and create a trigger and a rule and disable a rule. Then create a trigger and a rule that causes the trigger to invoke an action
* Explain why programmers expose actions as APIs
* Identify the benefits of web actions
* Describe how IBM Cloud Functions work with an integrated API Gateway

## Summary
Congratulations! You have completed this module. At this point in the course, you know that:
* You can create Cloud Functions actions using source code
*Actions can pass parameters and apply default values​. Actions can call other actions by using a pre-installed OpenWhisk library​. Sequences are a type of action and are created by chaining together existing actions. You can invoke actions using either blocking or non-blocking invocations. Activation records are stored for each invocation and you can use the activation record to obtain the invocation’s response
* IBM Cloud Functions provides packages that you can use and bind to specify default parameters. You can create packages to group your actions, manage default parameters, and share entities with other users.
* A rule associates one trigger with one action. When the associated trigger is fired, rules invoke actions. Using multiple rules can cause a trigger to invoke multiple actions or an action to be invoked by multiple triggers 
* Web actions create a public URL that you can use to invoke an action rather than using triggers and rules. After creating a web action, you can use the Cloud Functions integrated API Gateway to expose web actions via an API.
* You can use the API Gateway to perform robust API management on your behalf, such as routing and rate limiting.

## Laboratories:
* [**Hands-on Lab 2:** Creating IBM Cloud Functions Entities](./files/Creating_IBM_Cloud_Functions_Entities.pdf)
