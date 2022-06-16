---
markdown-version: v1
tool-type: theia
title: labs/module2/lab1_running_test_with_nose
branch: lab-441-instruction
version-history-start-date: 2022-04-08T19:53:44.000Z
---

::page{title="Hands-On Lab: Running Test With Nose"}

**Estimated time needed:** 30 minutes

Welcome to the **Running Tests with Nose** lab. In this lab, you will learn how to use fundamental tools for running unit tests in Python.

## Learning Objectives

After completing this lab, you will be able to:

*   Install Nose, Pinocchio, and Coverage
*   Run unit tests with unittest and Nose
*   Produce color-coded test output
*   Add coverage reports to your test output

::page{title="About Theia"}

Theia is an open-source IDE (Integrated Development Environment), that can be run on desktop or on cloud. You will be using the Theia IDE to do this lab. When you log into the Theia environment, you are presented with a 'dedicated computer on the cloud' exclusively for you. This is available to you as long as you work on the labs. Once you log off, this 'dedicated computer on the cloud' is deleted along with any files you may have created. So, it is a good idea to finish your labs in a single session. If you finish part of the lab and return to the Theia lab later, you may have to start from the beginning. Plan to work out all your Theia labs when you have the time to finish the complete lab in a single session.

::page{title="Set Up the Lab Environment"}

You have a little preparation to do before you can start the lab.

Open a terminal window by using the menu in the editor: Terminal > New Terminal.

![Terminal](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_terminal.png "Terminal")

In the terminal, if you are not already in the `/home/projects` folder, change to your project folder now.

```bash
cd /home/project
```

## Clone the Git Repository

Now let's get the code that you need to test. To do this, you will use the `git clone` command to clone the git repository:

```bash
git clone https://github.com/ibm-developer-skills-network/duwjx-tdd_bdd_PracticeCode.git
```

Your output should look similar to the image below:

![Git Clone](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_git_clone.png "Git Clone")

## Change into the Lab Folder

Once you have cloned the repository, change to the directory named: `duwjx-tdd_bdd_PracticeCode`

```bash
cd duwjx-tdd_bdd_PracticeCode
```

To go into the first set of labs, change into the `labs/01_running_tests_with_nose/` directory:

```bash
cd labs/01_running_tests_with_nose/
```

List the contents of this directory to see the artifacts for this lab.

```bash
ls -l
```

The directory should look like the listing below:

![List files](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_ls.png "List files")

***Note:*** *You must have a few exercise files that you will be running in the steps to follow.*

You can also view the files cloned in the file explorer.

![File explorer](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_file_explorer.png "File explorer")

::page{title="Step 1: Working with unittest"}

You are ready to run your first tests. The `unittest` module is built into Python 3. You can invoke it through the Python interpreter by passing it the argument `-m` to run a module, and then `unittest` to give it the name of the module that you want to run.

In the terminal, run the following command to run the tests using the Python `unittest` package:

```bash
python3 -m unittest
```

In the output you will see that all 11 tests passed as indicated by the 11 dots. Had there been any errors, you would have seen the letter `E` in place of the dot, representing an error in that test.

![Unittest 1](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_unittest1.png "Unittest 1")

::page{title="More verbose output"}

You can make the output more useful by adding the `-v` flag to turn on verbose mode. Run the command below for more useful output:

```bash
python3 -m unittest -v
```

![Unittest 2](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_unittest2.png "Unittest 2")

Also notice that verbose mode gives you lots of duplicate information like the test function name followed by the docstring. Next, you will see how `nose` handles this.

::page{title="Step 2: Working with Nose"}

There is a test runner called **nose** that you can use to produce better test output. It is a Python package that you can install using the Python package manager `pip` utility.

Install Nose using `pip`:

```bash
pip install nose
```

> ***Note:*** *To refresh your memory on Nose, review the “Running Tests with Nose” video.*

To see verbose output from `nose`, run `nosetests -v`. The verbose output from Nose will return nicer output than from unittest because it only returns the docstring comments:

```bash
nosetests -v
```

![Nose](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_nose.png "Nose")

::page{title="Step 3: Adding color with Pinocchio"}

Another way to make your output look better is with a plugin called `pinocchio`. With this plugin, you can get output as a specification similar to **Rspec** and also add color to the output. The color really gives you the Red/Green/Refactor workflow that TDD is famous for.

Install `pinocchio` using `pip`.

```bash
pip install pinocchio
```

To get nicer formatting and a colorful output, run `nose` again and add the `--with-spec --spec-color` parameters:

```bash
nosetests --with-spec --spec-color
```

> Note: In the output, green color indicates that all tests have passed. In case any test fails, the color for that test in the output will be red. Also note that you no longer need the `-v` because `--with-spec` already gives verbose output.

![Pinocchio](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_pinocchio.png "Pinocchio")

::page{title="Step 4: Adding test coverage"}

To know if you’ve written enough tests, you need to know how many lines of code your tests cover. The `coverage` tool will calculate the number of lines of code executed during your tests, against the total lines of code, and report that as a percentage of coverage.

Install the `coverage` tool so that you can check your test coverage:

```bash
pip install coverage
```

Next, call `coverage` through `nose` by adding the `--with-coverage` parameter.

```bash
nosetests --with-spec --spec-color --with-coverage
```

![Coverage](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_coverage.png "Coverage")

::page{title="Step 5: Create missing coverage report"}

One useful feature of the coverage tool is that it can report which lines of code are missing coverage. With that information, you know the lines for which you need to add more test cases so that your testing executes those missing lines of code.

To get the missing coverage report, run the below command in the terminal:

```bash
coverage report -m
```

![Coverage Missing](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_coverage_missing.png "Coverage Missing")

These test cases produce 100% coverage but notice that a new column has been added with the **Missing** heading. This is where any line numbers would show up for lines without test coverage.

::page{title="Step 6: Automating these parameters"}

Up until now you have typed out a lot of command parameters when running tests with nose. Alternatively, you can save all the parameters in a configuration file so that you don't have to type them in every time.

Create a new file named `setup.cfg` under `duwjx-tdd_bdd_PracticeCode/labs/01_running_tests_with_nose` directory. Here are the steps:

1.  On the window to the right, click the File menu and select the New File option, as shown in the image below:

![New File](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_new_file.png "New File")

2.  A pop-up appears with title New File, as shown in the image below. Enter `setup.cfg` as the file name and then click OK.

![Setup](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_setup.png "Setup")

3.  A file `setup.cfg` will be created for you.

::openFile{path="/home/project/duwjx-tdd_bdd_PracticeCode/labs/01_running_tests_with_nose/setup.cfg"}

4.  Copy and paste the below code into `setup.cfg`:

```ini
[nosetests]
verbosity=2
with-spec=1
spec-color=1
with-coverage=1
cover-erase=1
cover-package=triangle

[coverage:report]
show_missing = True
```

> Do not forget to save the setup.cfg file.

![Setup Config](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_setup_cfg.png "Setup Config")

::page{title="Step 7: Run nosetests with config"}

Now that you have established your `setup.cfg` file, go to your terminal and run `nosetests` without any parameters:

```bash
nosetests
```

> Now you’ve applied all your parameters and gotten colorful output, by simply running **nosetests**.

![Nosetests](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0241EN-SkillsNetwork/labs/module2/images/01\_nosetests.png "Nosetests")

::page{title="Conclusion"}

### Congratulations on Completing the Lab on Running Tests with Nose

You now know how to run basic and verbose unit tests with Nose. You also know how to use the Pinocchio and Coverage plugins to produce nicer test output that really brings the Red/Green/Refactor workflow to life. Feel free to play around with these commands some more or move on to the next lesson.

Now you should use these tools in your own projects to produce actionable test cases reports.

## Author(s)

John Rofrano

## Contributor(s)

Srishti Srivastava

## Changelog

| Date       | Version | Changed by | Change Description     |
| ---------- | ------- | ---------- | ---------------------- |
| 2022-04-08 | 1.0     | Srishti    | Create new lab         |
| 2022-04-17 | 1.1     | Rofrano    | Fixed image links      |
| 2022-04-17 | 1.2     | Zach Rash  | Proofreading and edits |

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
