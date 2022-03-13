# Managing Applications with Kubernetes
## Introduction
In this module, you will learn about some key concepts such as ReplicaSets, autoscaling, rolling updates, ConfigMaps, Secrets, and service bindings, and how they can be used to manage Kubernetes applications. You will learn how to use ReplicaSets to scale applications to meet increasing demand, and then use the autoscaling feature to make this scaling dynamic, as per demand. Using the rolling updates feature, you will learn how to publish updates to your application and also roll back the changes without creating any noticeable interruptions for your users. Storing hard-coded configuration variables and sensitive information in code is never a good idea. You will learn how to use ConfigMaps and Secrets to provide configuration variables and sensitive information to your deployments and keep your code clean. Finally, you will perform a hands-on exercise to scale and update applications deployed in Kubernetes.

## Learning Objectives
* Describe how a ReplicaSet is used to scale your application.
* Explain how to create a ReplicaSet using the CLI and a YAML file.
* Discuss what autoscaling is and how it can be used to dynamically scale an application
* Explain what a rolling update is and how to use rolling updates to publish and revert changes made to your application.
* Describe what a ConfigMap is and the different ways in which you can create ConfigMaps.
* Explain what a Secret is, the different ways to create a Secret, and how to use it to provide sensitive information to your application.
* Explain what service binding is and how to bind an external service to your deployment.
* Use a ConfigMap to store application configuration
* Apply rolling updates to an application
* Scale an application with a ReplicaSet

## Laboratory
* [Hands-on Lab: Scaling and Updating Applications](./files/labs.cognitiveclass.ai.pdf)
