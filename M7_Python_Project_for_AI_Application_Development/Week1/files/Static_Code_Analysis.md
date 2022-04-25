# Hands-on Lab: Static Code Analysis

<center>
    <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

## Static Code Analysis Lab

Estimated time needed: **30** minutes

## Objectives

After completing this lab you will be able to:

*   Install pylint package
*   Run Static Code Analysis on a python program
*   Check the compliance score of a python program.
*   Fix common mistakes and improve the compliance score.

# Install the pylint package

*   Open a new terminal
*   At the terminal, run the below command.
*   pip3 install pylint
*   This should install the pylint package.

# Create a sample python file for static code analysis

Create a new file named **sample1.py**

Copy and paste the below code into **sample1.py**

```
def add(number1, number2):
    return number1 + number2

num1 = 4
num2 = 5
total = add(num1, num2)
print("The sum of {} and {} is {}".format(num1, num2, total))
```

{: codeblock}

Save the file **sample1.py**

# Run pylint

*   Open a terminal
*   run the below command
*   pylint sample1.py
*   Pylint goes through every line of code and gives you a list all the non-compliant lines.
*   Pylint gives you a compliance score (10 being maximum).

# Correct the mistakes identified by pylint.

*   Based on the report given by pylint changes were made to this code to address the following issues.
    *   Exactly one space required after comma
    *   Exactly one space required around assignment
*   Create a new file named **sample2.py**
*   Copy and paste the below code into **sample2.py**

```

def add(number1, number2):
    return number1 + number2

NUM1 = 4
num2 = 5
total = add(NUM1, num2)
print("The sum of {} and {} is {}".format(NUM1, num2, total))

```

{: codeblock}

Save the file **sample2.py**

# Run pylint

*   Open a terminal
*   run the below command
*   pylint sample2.py
*   This will give you the compliance score.
*   This time you should see the score improve.

# Your task

Improve the score in sample2.py to a perfect 10 by correcting all the issues pointed out by pylint. If cant figure out how to solve some issues it is helpful to google the pylint message.

# Congratulations!

You now know how to perform static code analysis.

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-01-29        | 1.1     | Rav Ahuja         | Formatting & license changes       |
| 2020-11-25        | 1.0     | Ramesh Sannareddy | Created initial version of the lab |

Copyright © 2020 IBM Corporation. All rights reserved.
