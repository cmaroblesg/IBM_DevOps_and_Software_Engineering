<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/FinalProject_Coursera/images/IDSNlogo.png" width="200" height="200">

# Python Project for AI: Scenario and Review Criteria

**Estimated time needed:** 2 hours

You are working for an IT services company and your company has just won a big project with an hotel in Quebec, Canada serving customers with a large French-speaking population. While most communication will happen in English, there is a scope for personal touch if French is used in communication.
You are going to develop some chatbots for the client. The chances that the customer base the client is dealing with is largely French-speaking is high. So you would like to develop a server with end points that allow you to translate from English to French and from French to English.

You are given a skeleton structure, on top which you are expected to build the functionality.

## Review Criteria –  marks total

1.  Use Watson APIs to create Language Translator Service. (1)

2.  Create an instance of the Language Translator Service in your Python code. (1)

3.  Create a function that translates English to French. (2)

4.  Create a function that translates French to English. (2)

5.  Write unit tests to test the above functions. (4)

    a. assertEqual frenchToEnglish

    b. assertNotEqual frenchToEnglish

    c. assertEqual englishToFrench

    d. assertNotEqual englishToFrench

6.  Run coding standards check against the functions above. (3)

7.  Run unit tests and interpret the results. (4)

8.  Package the above functions and tests as a standard python package. (2)

9.  Ensure server.py includes code to
    *   Import translator.py
    *   provide root end point which renders index.html
    *   provide end point to translate from French to English
    *   provide end point to translate from English to French

10. Check the endpoints of the application(2)

    *   The endpoint frenchToEnglish works - Translates text as expected

    *   The endpoint englishToFrench works - Translates text as expected

## Next Steps

Be sure to read the overview before starting with the step-by-step instructions.

## Author(s)

<h4> Lavanya <h4/>

## Changelog

| Date       | Version | Changed by | Change Description                   |
| ---------- | ------- | ---------- | ------------------------------------ |
| 2021-05-06 | 1.0     | Lavanya    | Created new instructions for project |
