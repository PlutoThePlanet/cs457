# Programming Assignment 1

## Overview
python 3: Run with command `python project1.py < PA1_test.sql` or write desired queries by hand when prompted by terminal

In this assignment, we were required to write a program that allows a database user to manage database metadata with simple functions such as add, delete, etc. Databases and tables are both used to assist in organizing this data.



## Functions
Function: `main()`<br />
Input: n/a<br />
Use: user input is accepted either line-by-line or via a pre-written file. The input is then parsed and desired functionality is determined and carried out
<br />
<br />
Function: `query_tbl(tbl)`<br />
Input: name of table to be printed<br />
Use: this function prints all data contained within a desired table
<br />
<br />
Function: `update_tbl(tbl, data)`<br />
Input: name of table to be created, data to be added<br />
Use: new data is added to a desired table
<br />
<br />
Function: `delete_tbl(tbl)`<br />
Input: name of table to be deleted<br />
Use: this function deletes the desired table and all of its corresponding data (as long as the table still exists within the working directory)
<br />
<br />
Function: `create_tbl(tbl, data)`<br />
Input: name of database to be created, data to be input<br />
Use: this function creates a new table within the working database and adds desired data to aforementioned table
<br />
<br />
Function: `use_database(db)`<br />
Input: the database we want to work in<br />
Use: as long as it exists, this function lets us work within a desired database for the foreseeable future
<br />
<br />
Function: `delete_database(dir)`<br />
Input: name of database to be deleted<br />
Use: this function deletes the desired database (as long as it exists) along with all of its tables and corresponding data
<br />
<br />
Function: `create_database(new_dir)`<br />
Input: name of database to be created<br />
Use: if this database does not already exist, this function creates a new database that is able to hold multiple tables full of data
<br />
<br />
Function: `cleanList(arr)`<br />
Input: array of data, where the first and last elements need parenthesis removed<br />
Use: a helper function that "cleans" the input data of its beginning and ending parenthesis. This function helps when data is initially written to its table.
