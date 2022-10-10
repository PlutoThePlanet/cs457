# Programming Assignment 1

== Overview
python 3, run with command 'python project1.py < PA1_test.sql' or write desired queries by hand when prompted by terminal.

In this assignment, we were required to write a program that allows a database user to manage database metadata with simple functions such as add, delete, etc. with the help of multiple databases and tables.


== Functions
Function: 'main()'
Input: n/a
Use: user input is accepted either line-by-line or via a pre-written file. The input is then parsed and desired functionality is determined and carried out

Function: 'query_tbl(tbl)'
Input: name of table to be printed
Use: this function prints all data contained within a desired table

Function: 'update_tbl(tbl, data)'
Input: name of table to be created, data to be added
Use: new data is added to a desired table

Function: 'delete_tbl(tbl)'
Input: name of table to be deleted
Use: this function deletes the desired table and all of its corresponding data (as long as the table still exists within the working directory)

Function: 'create_tbl(tbl, data)'
Input: name of database to be created, data to be input 
Use: this function creates a new table within the working database and adds desired data to aforementioned table

Function: 'use_database(db)'
Input: the database we want to work in for the foreseeable future
Use: 

Function: 'delete_database(dir)'
Input: name of database to be deleted
Use: this function deletes the desired database (as long as it exists) along with all of its tables and corresponding data

Function: 'create_database(new_dir)'
Input: name of database to be created
Use: if this database does not already exist, this function creates a new database that is able to hold multiple tables full of data

Function: 'cleanList(arr)'
Input: array of data, where the first and last elements need parenthesis removed
Use: a helper function that "cleans" the input data of its beginning and ending parenthesis. This function helps when data is initially written to its table.