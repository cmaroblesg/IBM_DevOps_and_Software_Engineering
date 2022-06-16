# Introduction to Test Driven Development
## Introduction
This module provides an overview of test driven development (TDD). You will learn what TDD is and discover the three basic steps in the TDD workflow, also known as the Red/Green/Refactor workflow. You will find out why TDD is important for DevOps and all automated testing. You will also discover popular testing tools for TDD and closely examine the features of several such tools for Python. This module also covers essential methods for performing TDD. You will explore two ways to run TDD tests: Python’s built-in test runner called unittest and the more feature-rich module called Nose. You will learn what assertions are and how to use them to test code. You will discover why you need to include both happy and sad paths in your test module. You will also find out what test fixtures are and how to use them to establish an appropriate initial state for each test.

## Learning Objectives
* Describe test driven development (TDD) and explain its benefits for DevOps
* List popular testing tools for TDD and summarize their features
* Run TDD tests by using unittest and the Nose module
* Discuss how testing frameworks help developers build assertions
* Explain the purpose of using assertions
* Summarize the role of happy paths and sad paths in testing
* Write test assertions
* Summarize the purpose of using test fixtures
* Create an initial testing state by using test fixtures

## Introduction to Test Driven Development: Summary & Highlights
Congratulations! You have completed this lesson. At this point in the course, you know:  
* In TDD, test cases drive code design.
* The Red/Green/Refactor workflow includes three steps:
* Write a failing unit test case for the code you wish you had
* Write just enough code to pass this test case
* Refactor the code to improve its quality
* TDD saves development time and ensures that the code works as expected.
* To create a DevOps pipeline, you must automate all testing.
* The xUnit series is one of the most popular testing frameworks for TDD, while others include Jasmine for JavaScript, Mocha for Node.js, and SimpleTest for PHP.
* The two most popular testing frameworks for Python are PyUnit and Pytest. Two other popular testing frameworks for Python are Doctest and RSpec.
* Nose is a Python test runner that can add color to test output and call the code coverage tool.

## Methods for Test Driven Development: Summary & Highlights
Congratulations! You have completed this module. At this point in the course, you know:  
* To run TDD tests in Bash, you can call unittest or call nosetests if Nose is installed.
* Unlike unittest, Nose can color code test results, report code coverage, and list missing test cases.
* Testing frameworks provide tools that simplify testing conditions.
* Assertions are checks to determine if tests have passed or failed.
* To create assertions in Python, developers can use the assert() function or any additional PyUnit asserts.
* Happy paths verify that a function returns positive outcomes when expected, while sad paths verify that a function responds to exceptions appropriately and without breaking.
* Test fixtures establish a known initial state before and after each test.
* Test fixtures are helpful for many testing situations such as creating mock objects and loading a database with a known set of data.
* Test fixtures operate at three levels of specificity:
  * Module
  * Test case
  * Test

## Laboratories
* [**Hands-on Lab 1:** Running test with nose](./files/lab1_running_test_with_nose.pdf)
* [**Hands-on Lab 2:** Writing tests assertions](./files/lab2_writing_test_assertions.pdf)
* [**Hands-on Lab 3:** Test fixtures](./files/lab3_test_fixtures.pdf)

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
