# Introduction to Test Driven Development (TDD)
## Introduction to Testing

This module provides an overview of software testing. You will learn about the importance of testing through an example: the development of the Apollo 11 Lunar Module’s guidance system. You will discover the numerous problems that occur when developers do not test their code. Then you will explore the four levels of testing and find out when each appears in the traditional release cycle. You will learn what test driven and behavior driven development are and why both are essential for effective testing. You will discover the purpose of test cases and witness their value through a demonstration.

## Learning Objectives
* Explain the importance of testing
* Summarize the problems that occur when developers do not test their code
* Describe each level of the software testing process
* Summarize each phase of the traditional release cycle
* Compare and contrast test driven development (TDD) and behavior driven development (BDD)
* Explain why developers need both TDD and BDD
* Summarize the purpose for using test cases

## ULR Links:
* [Agile Data](http://agiledata.org/)

## Summary & Highlights
Congratulations! You have completed this module. At this point in the course, you know:  
* Testing verifies that your software will work as expected when you or others use it.
* Testing prevents future code breaks and compatibility issues.
* Testing reduces overall development time.
* The software testing process includes four levels: unit, integration, system, and acceptance.
* The level of testing that developers perform varies throughout the phases of the traditional release cycle.
* Test cases drive code design in both behavior driven development (BDD) and test driven development (TDD).
* BDD focuses on the system from the outside in, while TDD focuses on the system from the inside out.
* Developers use BDD for integration and acceptance testing but use TDD for unit testing.
* Test cases help developers identify and fix parts of their code that can break.

## Codes:
```python
**Code 01:**
def area_of_a_triangle(base, height):
  return (base/2)*height

test_data=[(3.5, 8.5),  # Float
           (2, 5),      # Integer
           (0, 5),      # Zero
           (-2, 5),     # Negative
           (True, 5),   # Boolean
           ("base", 5)] # String

for data in test_data:
  print(f"The area of a triangle {data}"\
        f" is: {area_of_a_triangle(*data)}")
```
