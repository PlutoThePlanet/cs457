# Programming Assignment 1

## Overview
python 3: Run with command `python project1.py < PA1_test.sql` or write desired queries by hand when prompted by terminal

In this assignment, we were required to write a program that allows a database user to manage database metadata with simple functions such as add, delete, etc. Databases and tables are both used to assist in organizing this data. In order to handle multiple databases, each database consists of its own folder of multiple tables. Each table is a file nested within a database/folder. Each database can hold multiple tables/files and all metadata is held in a table/file.



## Functions
**Function**: `main()`<br />
**Input**: n/a<br />
**Use**: user input is accepted either line-by-line or via a pre-written file. The input is then parsed and desired functionality is determined and carried out<br />
**Implementation**: continue to prompt for user input until the user decides to exit (via `while` loop). Read in user input - while removing the `;` - and section input by spaces into an array (one word for each index). Perform various tests on said input to dertermine which function should be run (via `elif` statements).
<br />
<br />
**Function**: `query_tbl(tbl)`<br />
**Input**: name of table to be printed<br />
**Use**: this function prints all data contained within a desired table<br />
**Implementation**: take in the name of the table to be read and, if the table exists, print out all the data within the file. Else, let the user know that the file does not exist.
<br />
<br />
**Function**: `update_tbl(tbl, data)`<br />
**Input**: name of table to be created, data to be added<br />
**Use**: new data is added to a desired table<br />
**Implementation**: take in the name of the table where you want to add data and, if the table exists, open the table/file in append mode and add the passed-in data to the end of the row. Else, let the user know that the file does not exist.
<br />
<br />
**Function**: `delete_tbl(tbl)`<br />
**Input**: name of table to be deleted<br />
**Use**: this function deletes the desired table and all of its corresponding data (as long as the table still exists within the working directory)<br />
**Implementation**: take in the name of the table that you want to be deleted, and try to delete that table. If an error is thrown becaue the table does not exist, inform the user.
<br />
<br />
**Function**: `create_tbl(tbl, data)`<br />
**Input**: name of database to be created, data to be input<br />
**Use**: this function creates a new table within the working database and adds desired data to aforementioned table<br />
**Implementation**: take in the name of a new table and the data you would like added to it. "Clean" the data by removing the beginning and ending parenthesis (pass data to `cleanList`. Try to create this new table/file. If an error is thrown because this table already exists and or its name is already in use within the working database, inform the user. To add in the data, open the file in writing mode and as you loop through the indices of your data array, check if the data contains a `,`. If a piece of data contains a comma, you know that a spacer `|` needs to be addded after. Ignore the comma when printing this piece of data to the table/file and then add a spacer. Continue this process for your entire data list.
<br />
<br />
**Function**: `use_database(db)`<br />
**Input**: the database we want to work in<br />
**Use**: as long as it exists, this function lets us work within a desired database for the foreseeable future<br />
**Implementation**: take in the name of the database that you want to be working in. Make sure your system is viewing your original "home" directory (where all databases are made) and try to change your working directory to the desired database. If an error is thrown because the desired database does not exist, inform the user. If the database does exist, all future action will be performed within this database (until the user decides to switch to another database or back to the "home" directory.
<br />
<br />
**Function**: `delete_database(dir)`<br />
**Input**: name of database to be deleted<br />
**Use**: this function deletes the desired database (as long as it exists) along with all of its tables and corresponding data<br />
**Implementation**: take in the name of the desired database to be deleted. Try to delete the database. If an eror is thrown because this database doesn't exist, inform the user.
<br />
<br />
**Function**: `create_database(new_dir)`<br />
**Input**: name of database to be created<br />
**Use**: if this database does not already exist, this function creates a new database that is able to hold multiple tables full of data<br />
**Implementation**: take in the name of the database you want to create. Try to make this database within the home directory. If an error is thrown because this database  already exists and or its name is already in use within the working database, inform the user.
<br />
<br />
**Function**: `cleanList(arr)`<br />
**Input**: array of data, where the first and last elements need parenthesis removed<br />
**Use**: a helper function that "cleans" the input data of its beginning and ending parenthesis. This function helps when data is initially written to its table.<br />
**Implementation**: take in the array of data you want "cleaned". Iterate through the array of data, adding to a seperate variable of type `string`. Once you have iterated through the entire data set, create a "clean" string of data by coppying the first string into the second, but ignoring the first and last characters (in this case, the parenthesis). Seperate this "clean" data back into an array and return to caller.
