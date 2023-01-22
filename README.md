![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Company Database
<br>
Company Database is a sqlite3 database created using Python and it runs in Code Institute Mock Terminal on Heroku platform.

Users can create three classes of employees: administrators, developers, managers. Administrators can add, remove, update and fetch other employees using a simple terminal interface.

![Project View](https://github.com/KhanRana/company_employees/blob/c851af1e852f1af9abcc7528656b35b5859e5521/images/compare.png)

# How it Works
Company Database is build on sqlit3, a built-in python database module for light application and testing. The Database first ask for an admin details and add him/her to the databse. Then it asks the admin to selecet from 6 different options to choose the operation. Once the user exits the system it will for terminate the program and erase the data.

# Features
 - Data Validity
 - Add Data
 - Update Data
 - Retrieve Data
 - Erase Data

## Data Validity
![Data Valid](https://github.com/KhanRana/company_employees/blob/d2fcfe4fa521973f0c2eb42c6495066f70976074/images/data%20validity.png)

## Add Data
![Add Data](https://github.com/KhanRana/company_employees/blob/d2fcfe4fa521973f0c2eb42c6495066f70976074/images/add_data.png)

## Update Data
![Data update](https://github.com/KhanRana/company_employees/blob/d2fcfe4fa521973f0c2eb42c6495066f70976074/images/update_records.png)

## Retrieve Data
![Data retrieval](https://github.com/KhanRana/company_employees/blob/d2fcfe4fa521973f0c2eb42c6495066f70976074/images/fetch_data.png)

## Erase Data
![Data erase](https://github.com/KhanRana/company_employees/blob/d2fcfe4fa521973f0c2eb42c6495066f70976074/images/terminate_erase.png)

 



## Future Features
 - Check for dulicate records and do not add if exist already
 - Allow user to change mutiple values
 - Have a more comprehensive database with other features such as secure entry etc.

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Data Model
I decided to create employee class and two more subclass that inherit from it. A seperate database is creted using sqlite for database.

The classes can be used in python code to build more complext databases.

## Testing
 - PEP8 without any problem
 - Data Validity test done 
 - I have tested the application in both my terminal and Heroku

## Bugs
 - I had to press key twice for it to run the users options, I realised I was calling the same function twice - fixed
 - Got stuck in infinite loop, It was loop the wrong function, moved it and problem solved - fixed

## Validator
 - PythonChecker
 -  PEP8

 No Errors were returned

## Deployment
 - Create gitHub repository from CI template
 - Create new Heroku app
 - Buildback python and NodJS
 - Link Heroku app to github
 - Deploy the App

# Acknowledgements
 - Code institute for amazing lessons and templates
 - All developers who post their work on Youtube that has helped alot
 - To the Author of Python Crash Course