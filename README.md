# Loan Qualifier Application

This application takes in a loan applicants data then automatically filters through a list of lenders qualifications then it compiles and saves the list of lenders the loan applicant would qualify for. It is a quick and easy way to sort through potential loan data for applicants and choose the best fitting loans from a filtered list.

---

## Technologies

This project uses the Python Programming language as well as the following libraries
    
    - Questionary
    - Fire
    - Sys
    - Pathlib
    - CSV


---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

To install you will want to pull the entire QUALIFIER folder from github including all of its subfolders
    
    * Subfolders
        * data (folder)
        * qualifier (a qualifier subfolder, not the main folder)
        * tests (folder)
        * app.py (the application itself)

---

## How it works

1) First the user will enter the data source (**./data/daily_rate_sheet.csv**)
    A) this data will then be processed by the *load_bank* function and turned into a list
2) The user will be prompted for the following
    A) Credit Score
    B) Monthly Debt
    C) Monthly Income
    D) Loan Amount
    E) Home Value
3) The following data will be run through the *calculator* functions to determine the Debt to Income ratio and the Loan to Value Ratio
4) Then the app will filter out the list of Lenders 
    * Requested Loan Amount must be less than or equal to the Lenders Maximum Loan Amount
    * Users Credit Score must be greater than or equal to the Lenders Minimum Credit Score
    * Users Debt to Income Ratio must be less than or equal to the Lenders Maximum DTI Ratio
    * Users Loan to Value Ratio must be less than or equal to the Lenders Maximum LTV Ratio
5) The user will be informed of the number of Lenders that meet all of the criteria in step 4 and asked if they would like to save the list of lenders
6) If the user selects "Yes" then they will be asked to name the file which will then be saved as a CSV in the **/data/output** file
7) If the user chooses not to save the data the application will close.
---

## Usage

Overall it should be a very simple application to use, all you need to do is run the app.py program and follow the prompts in the CLI. 

1) When asked for the CSV path to source the data (the first CLI prompt) type **./data/daily_rate_sheet.csv** 
2) Once that has been entered the CLI will prompt you for the customers data 
3) Finally if you wish to save the data just type in the name you would like to save it under and the app will save it as a CSV file in the data/output folder.

---

## Contributors

Colin Benjamin

Linkedin: [Colin Benjamin](https://www.linkedin.com/in/colinbenjamin/)
    
email: cbenjamin33@gmail.com

---

## License

MIT
