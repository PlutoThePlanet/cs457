# Paige Mortensen
# CS 457 PA 3
# 11/18/22

import os
import shutil
import re

cwd = os.getcwd()         # keep track of which directory being used in system (when switched, so you can stay there for mult. actions)
home_dir = os.getcwd()    # always able to refer back to original "home" directory (used for switching between databases)

# cleans up the extra '(' and ')' when taking in table data
def cleanTableData(arr):
    new_string = ', '.join(str(x) for x in arr)   # joins all array elements into one string
    clean_string = new_string[1:-1]               # erase beginning and end parenthesis
    return clean_string

# cleans up the input values when inserting a new record
def cleanValues(values):
    val1 = values[9:-3] 			# remove extra chars and ()
    val2 = val1.replace("'", "") 	# remove quotes if any
    final_vals = val2.split(',') 	# split data into an array on commas
    return final_vals

# seperates input into array of "words", removing any extra chars in the process (for update, delete fct - where extra usr input is needed)
def parse_input():
    usr_in = input("")                          # get input
    words = re.split("[ \t,;']", usr_in)        # seperate on special chars
    index = 0
    while index < len(words):
        if(words[index] == ""):                 # if the index is empty b/c of the char seperation
            words.pop(index)                    # remove from array
        else:
            index +=1
    return words

# seperates input to create a new table into a usable array ######################################
def parse_new_table_input(usr_in):
    words = re.split("[ \t ;']", usr_in)    # seperate on special chars
    index = 0
    while index < len(words):
        if(words[index] == ""):             # if the index is empty b/c of the char seperation
            words.pop(index)                # remove from array
        else:
            index +=1
    extra_words = words[2].split("(")       # extract the title of the table from extra data
    words.pop(2)                            # delete the old data
    words.insert(2, extra_words[0])         # add fixed data back to array
    words.insert(3, extra_words[1])
    words[6] = (words[6])[0:-1]             # remove the extra ) from the last element
    return words

# database creation (new folder)
def create_database(new_dir):
    try:
        path = os.path.join(cwd, new_dir)
        os.mkdir(path)
        print('Database ' + new_dir + ' created.')
    except FileExistsError:
        print('!Failed to create database' + new_dir + ' because it already exists.')

# database deletion (delete folder)
def delete_database(dir):
    try:
        path = os.path.join(cwd, dir)
        shutil.rmtree(path)
        print('Database ' + dir + ' deleted.')
    except FileNotFoundError:
        print('!Failed to delete ' + dir + ' because it does not exist.')

# set working database
def use_database(db):
    try:
        global cwd                            # make sure to stay in working dir (for multiple actions)
        cwd = home_dir                        # make sure you can see all databases (go up dir tree if needed)
        cwd = os.path.join(cwd, db)
        os.chdir(cwd)                         # switch to desired database
        print('Using Database ' + db + '.')
    except FileNotFoundError:
        print('!Failed to use ' + db + ' because it does not exist.')
        
# table creation (new file with data)
def create_tbl(tbl, data):
    test_file = os.path.join(cwd, tbl)
    if(not os.path.exists(test_file)):             # make sure the file doesn't already exist 
        with open(tbl, 'w') as fp:
            for i in data:                     # iterate through elements
                if(i.__contains__(',')):
                    fp.write(i[0:-1])              # write the data but ignore the , at the end of the string
                    fp.write(' | ')                # and write a dividing ' | ' if there was a ','
                else:
                    fp.write(i + ' ')              # else just write the data as usual
        print('Table ' + tbl + ' created.')
    else:
        print('!Failed to create table' + tbl + ' because it already exists.')
        
# table deletion (file)
def delete_tbl(tbl):
    try:
        os.remove(tbl)
        print('Table ' + tbl + ' deleted.')
    except FileNotFoundError:
        print('!Failed to delete ' + tbl + ' because it does not exist.')

# insert new data into file
def insert_info_tbl(data):
    values = str(data[3:])
    new_values = cleanValues(values)			# preps data to be inserted
    test_file = os.path.join(cwd, data[2])  	# print data to file
    if(os.path.exists(test_file)):
        with open(data[2], 'a') as fp:
            fp.write('\n')
            for i in new_values:
                fp.write(i)
                fp.write(' | ')
        print('1 new record inserted.')
        return new_values
    else:
        print('!Failed to insert data into table ' + data[2] + ' because it does not exist.')

# update desired elements in table
def updateTable(tbl, tbl_elements, set_var, set_value, where_var, where_value):
    updates = 0
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):                 # make sure the file exists
        if(set_var == "pid"):                      # set all necessary vaiables 
            set_var = 0
        elif(set_var == "name"):
            set_var = 1
        elif(set_var == "price"):
            set_var = 2
        else:
            print("!Failed to update table because " + tbl + " does not exist.")
        if(where_var == "pid"):
            where_var = 0
        elif(where_var == "name"):
            where_var = 1
        elif(where_var == "price"):
            where_var = 2
        else:
            print("!Failed to update table because " + tbl + " does not exist.")

        for row in tbl_elements:                           # update desired elements and count # modified
            if(row[where_var] == where_value):
                row[set_var] = set_value
                updates +=1
                
        if(updates == 1):                                  # notify user
            print("1 record modified.")
        else:
            print(str(updates) + " records modified.")
            
        with open(tbl, 'w') as fp:                         # re-write file w/ updated info
            fp.write('pid int | name varchar(20) | price float \n')
            for row in tbl_elements:
                for element in row:
                    fp.write(str(element) + " | ")
                fp.write("\n")
    else:
        print('!Failed to insert data into table ' + tbl + ' because it does not exist.')
    
# table query (file)
def query_tbl(tbl):
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):
        with open(tbl, 'r') as fp:
            print(fp.read())               # print entire entry
    else:
        print('!Failed to query table ' + tbl + ' because it does not exist.')

# select desired element(s)
def select_element(tbl, table_elements, select_list, where_var, where_value, operation):
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):                   # make sure the file exists
        if(where_var == "pid"):                      # update where_var index
            where_var = 0
        elif(where_var == "name"):
            where_var = 1
        elif(where_var == "price"):
            where_var = 2
        for i, item in enumerate(select_list):       # update elements to print
            if(select_list[i] == "pid"):
                select_list[i] = 0
                print('pid int | ', end = '')
            elif(select_list[i] == "name"):
                select_list[i] = 1
                print('name varchar(20) | ', end = '')
            elif(select_list[i] == "price"):
                select_list[i] = 2
                print('price float', end = '')
        print('\r')
        for i, item in enumerate(table_elements):
            if(operation == '!='):
                if(float(table_elements[i][where_var]) != float(where_value)):
                    for j in select_list:                                      # then iterate through what elements we want printed
                        print(table_elements[i][j] + ' | ', end = '')
                    print('\r')
    else:
        print('!Failed to select elements from ' + tbl + ' because it does not exist.')
        
# delete desired element(s)
def delete_element(tbl, operation, table_elements, where_var, where_value):
    deletes = 0
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):                                                 # make sure the file exists
        if(where_var == "pid"):
            where_var = 0
        elif(where_var == "name"):
            where_var = 1
        elif(where_var == "price"):
            where_var = 2
        
        for i, item in enumerate(table_elements):
            if(operation == '<'):
                if(float(table_elements[i][where_var]) < float(where_value)):
                    table_elements.remove(table_elements[i])
                    deletes += 1
            elif(operation == '='):
                if(str(table_elements[i][where_var]) == str(where_value)):
                    table_elements.remove(table_elements[i])
                    deletes += 1
            elif(operation == '>'):
                if(float(table_elements[i][where_var]) > float(where_value)):
                    table_elements.remove(table_elements[i])
                    deletes += 1
    else:
        print("!Failed to delete elements because " + tbl + " does not exist.")
        
    if(deletes == 1):                                                              # notify user
            print("1 record deleted.")
    else:
        print(str(deletes) + " records deleted.")
            
    with open(tbl, 'w') as fp:                                                     # re-write file w/ updated info
        fp.write('pid int | name varchar(20) | price float \n')
        for row in table_elements:
            for element in row:
                fp.write(str(element) + " | ")
            fp.write("\n")

# main fct that handles user input
def main():
    table_elements = []
    while (True):
        user_in = input('')                    # take in and parse user input
        user_in = user_in.replace(';', '')
        input_list = user_in.split(' ')
        
        if ('--' in input_list):               # determine and run desired fct
            pass
        elif('.exit' in input_list):
            print('All done.')
            exit()
        elif('CREATE' in input_list and 'DATABASE' in input_list):
            create_database(input_list[2])
        elif('drop' in input_list and 'database' in input_list):
            delete_database(input_list[2])
        elif('USE' in input_list):
            use_database(input_list[1])
        elif('create' in input_list and 'table' in input_list):
            table_words = parse_new_table_input(user_in) # parses the input fresh for input
            create_tbl(table_words[2], table_words[3:])
        elif('drop' in input_list and 'table' in input_list):
            delete_tbl(input_list[2])
        elif('insert' in input_list):
            table_elements.append(insert_info_tbl(input_list))
        elif('update' in input_list): 
            set_arr = parse_input()      # prompts the user for first line of input and seperates into array
            set_var = set_arr[1]         # what element are we changing
            set_value = set_arr[3]       # what value of this are we changing to
            where_arr = parse_input()    # prompts the user for second line of input and seperates into array
            where_var = where_arr[1]     # what element are we looking at
            where_value = where_arr[3]   # what value are we looking for
            updateTable(input_list[1], table_elements, set_var, set_value, where_var, where_value)
        elif('select' and '*' in input_list):
            query_tbl(input_list[3])
        elif(('select' in input_list) and ('*' not in input_list)):
            select_list = []
            select_list.append(input_list[1].replace(',', ''))
            select_list.append(input_list[2])                       # get elements to print
            tbl_arr = parse_input()                                 # get table to use
            tbl = tbl_arr[1]
            where_arr = parse_input()                               # find what conditions to use when searching
            where_var = where_arr[1]
            operator = where_arr[2]
            where_value = where_arr[3]
            select_element(tbl, table_elements, select_list, where_var, where_value, operator)
        elif('delete' in input_list):
            where_arr = parse_input()     # prompts the user for first line of input and seperates into array
            where_var = where_arr[1]      # what element are we looking at
            operation = where_arr[2]      # what comparison do we make
            where_value = where_arr[3]    # what value are we looking for
            delete_element(input_list[2], operation, table_elements, where_var, where_value)

# ensures main fct is called first
if __name__ == "__main__":
    main()