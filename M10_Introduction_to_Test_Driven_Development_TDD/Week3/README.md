# Advanced Methods for Test Driven Development
## Introduction
This module covers advanced methods for TDD. You will learn about test coverage: why it’s important, how to increase it by using test coverage reports, and why you should keep testing even at full test coverage. You will discover the value of testing against fake data and how to use factories to generate this data. You will also explore mocking, a process for mimicking the behavior of real objects, and you will find out the testing situations for which mocking is useful. You will learn how to use two common methods for mocking: patching a function call and mocking entire objects.

## Learning Objectives
* Explain what patching is and when developers should use it
* Explain what mock objects are and why they are useful for testing
* Implement the Mock and MagicMock classes in Python
* Explain the importance of test coverage
* Increase test coverage by using test coverage reports
* Discuss the importance of factories and fakes for testing
* Generate fakes by using a factory
* Define mocking and describe situations for which developers should mock

## Summary & Highlights
Congratulations! You have completed this module. At this point in the course, you know:  
* The higher the test coverage, the more confident developers can be that their code works as expected.
* Missing test coverage reports can help developers identify lines of code that still need test cases.
* Factories and fakes are useful for creating and maintaining a large amount of test data.
  * Factories generate fakes with realistic test data.
  * Fakes behave like real objects during testing, so developers test fakes like they test real data.
* Mocking is a process for creating objects that mimic the behavior of real objects.
* Developers should mock whenever they want to isolate tests from a remote component or external system.
* Patching is a mocking technique by which developers change the behavior of a function call.
* Python’s mock library provides two patching techniques:
  * Patching a function’s return value
  * Replacing a function with another function (the side effect technique)
* Mock objects are objects that mimic the behavior of real objects in ways that you can control.
* To make a Mock or MagicMock object mimic a given object, specify that real object’s name in the spec parameter.

## Laboratories
* [**Hands-on Lab 4:** Test Coverage](./files/lab4_test_coverage.pdf)
* [**Hands-on Lab 5:** Factories and Fakes](./files/lab5_factories_and_fakes.pdf)
* [**Hands-on Lab 6:** Mocking Projects](./files/lab6_mocking_objects.pdf)
