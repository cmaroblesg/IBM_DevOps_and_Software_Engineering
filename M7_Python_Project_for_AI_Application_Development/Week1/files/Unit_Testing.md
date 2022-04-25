# Hands-on Lab: Unit Testing

<center>
    <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

## Unit Testing Lab

Estimated time needed: **30** minutes

## Objectives

After completing this lab you will be able to:

*   Write unit tests to test a function.
*   Run unit tests and interpret the results.

# About Theia

Theia is an open source IDE(Integrated Development Environment), that can be run on desktop or on cloud. You will be using the Theia IDE to do this lab. When you log into the Theia environment, you are presented with a 'dedicated computer on the cloud' exclusively for you. This is available to you as long as you work on the labs. Once you log off, this 'dedicated computer on the cloud' is deleted along with any files you may have created. So, it is a good idea to finish your labs in a single session. If you finish part of the lab and return to the Theia lab later, you may have to start from the beginning. Plan to work out all your Theia labs when you have the time to finish the complete lab in a single session.

# Create a new python file named mymodule.py

On the window to the right, click on the **File** menu and select **New File** option, as shown in the image below.<br> <br><br>
![New File](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/menu_file_new.png) <br><br>
A pop up appears with title **New File**, as shown in the image below.<br> <br><br>
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/file_new_popup.png) <br><br>
Enter "mymodule.py" as the file name and click **OK**.<br><br>
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/file_new_popup2.png) <br><br>
A file "mymodule.py" will be created for you. <br><br>

You are now ready to add code to mymodule.py

Copy and paste the below code into mymodule.py

```
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2


def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2
```

{: codeblock}

You should see a screen like this now.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/module.png)

Save the file by using the Save option in the File Menu.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/save_file.png)

# Write Unit Tests

## Write the unit tests for square function

Let us write test cases for these three scenarios.

*   When 2 is given as input the output must be 4.
*   When 3.0 is given as input the output must be 9.0.
*   When -3 is given as input the output must not be -9.

## Write the unit tests for double function

Let us write test cases for these three scenarios.

*   When 2 is given as input the output must be 4.
*   When -3.1 is given as input the output must be -6.2.
*   When 0 is given as input the output must be 0.

## Create a new file and name it as test_mymodule.py

Copy and paste the below code into test_mymodule.py

```
import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
        

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
unittest.main()

```

{: codeblock}

You should see a screen like this now.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/testcase.png)

# Run tests

To run tests, select the test_mymodule.py file in the IDE and click on the 'Play' button.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/play_button.png)

This will run the tests.

You should see a screen like this now.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab%20-%20Unit%20Testing/images/testresult.png)

An `OK` in the last line indicates that all tests passed successfully.

`FAILED` in the last line indicates that at least one test has failed, and python prints which test or tests failed.

# Write unit tests for the given function

Here is a function that accepts two arguments and returns their sum.

Copy and paste the below code into mymodule.py and the save the file.

```
def add(a,b):
    """
    This function returns the sum of the given numbers
    """
    return a + b

```

{: codeblock}

<br>
Write test cases for these scenarios.
* When 2 and 4 are given as input the output must be 4.
* When 0 and 0 are given as input the output must be 0.
* When 2.3 and 3.6 are given as input the output must be 5.9.
* When the strings 'hello' and 'world' are given as input the output must be 'helloworld'.
* When 2.3000 and 4.300 are given as input the output must be 6.6.
* When -2 and -2 are given as input the output must **not** be 0. (Hint : Use assertNotEqual)

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |

Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0222ENSkillsNetwork23455715-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
