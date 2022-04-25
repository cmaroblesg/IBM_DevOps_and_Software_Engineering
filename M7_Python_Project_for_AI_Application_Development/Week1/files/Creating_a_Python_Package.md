<center>
    <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Creating a Python Package

Estimated time needed: **30** minutes

## Objectives

In this lab you will :

*   Create a module named basic
*   Add two functions to the module basic
*   Create a module named stats
*   Add two functions to the module stats
*   Create a python package named mymath
*   Verify that the package is working

# Lab

### Create Package

*   On the window to the right, click on the **View** menu and select **Explorer** option, as shown in the image below.

<br><br>
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/menu_explorer.png)

*   Your IDE now should look like the image below.

<br><br>
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/explorer_view.png)

*   On the window to the right, click on the **File** menu and select **New Folder** option, as shown in the image below.

<br><br>
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/menu_new_folder.png)

*   Enter **mymath** and click OK as shown in the image below.

<br><br>
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/new_folder_popup.png)

# Create the first module

*   Create a python module named basic

Create a file named **basic.py**. <br><br>

Copy and paste the below code into basic.py

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

def add(a, b):
    """
    This function returns the sum of given numbers
    """
    return a + b
```

{: codeblock}

You should see a screen like this now.

Save the file **basic.py**

# Create the second module

*   Create a module named stats

Create a file named **stats.py**. <br><br>

Copy and paste the below code into stats.py

```
def mean(numbers):
    """
    This function returns the mean of the given list of numbers
    """
    return sum(numbers)/len(numbers)


def median(numbers):
    """
    This function returns median of the given list of numbers
    """
    numbers.sort()
   
	if len(numbers) % 2 == 0:
	   median1 = numbers[len(numbers) // 2]
	   median2 = numbers[len(numbers) // 2 - 1]
	   mymedian = (median1 + median2) / 2
	else:
	   mymedian = numbers[len(numbers) // 2]
	return mymedian
```

{: codeblock}

You should see a screen like this now.

Save the file **stats.py**

# Create **init**.py

*   Create the file `__init__.py`

Copy and paste the below code into `__init__.py`

```
from . import basic
from . import stats
```

{: codeblock}

Save the file `__init__.py`

Now your directory structure should look like

```
mymath
mymath/__init__.py
mymath/basic.py
mymath/statistics.py
```

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/dir_structure.png)

You are done creating a package

# Verify the package

*   On the window to the right, click on the **Terminal** menu and select **New Terminal** option, as shown in the image below.
*   You will see a terminal open up on the bottom of the screen like the one in the image below.<br>

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/new_terminal.png)<br>

*   At the terminal type **python3** to invoke python interpreter.
*   Once the python interpreter is loaded.
*   At the python prompt type **import mymath**
*   If the above command runs without errors, it is an indication that the mymath package is successfully loaded.
*   At the python prompt type **mymath.basic.add(3,4)**
*   You should see an output *7* on the screen.
*   At the python prompt type **mymath.stats.mean(\[3,4,5])**
*   You should see an output *4.0* on the screen.
*   Type **exit()** to quit python interpreter.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module%206/Lab-%20Creating%20a%20Python%20Package/images/package_testing.png)

## Create a new module named geometry and add to the mymath package.

*   Create a module name geometry
*   Add a function named `area_of_rectangle` that takes length and breadth as input and returns the area of a rectangle.
*   Add a function named `area_of_circle` that takes radius as input and returns the area of a circle.
*   Modify the `__init__.py` to include this module.
*   Import and test the function `area_of_circle` from python terminal.

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |

Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0222ENSkillsNetwork23455715-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
