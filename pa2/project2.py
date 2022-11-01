# Paige Mortensen
# CS 457 PA 2
# 10/31/22

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
def cleanValues(arr):
    new_string = ', '.join(str(x) for x in arr)   # joins all array elements into one string
    clean_string = new_string[7:-1]               # erase beginning info and end parenthesis
    res1 = clean_string.replace(',', "")		  # Deleting all occurrences of character(s)
    res2 = res1.replace('\t', "")
    res3 = res2.replace(' ', "")
    new_values = res3.split("'")
    return new_values

# seperates input into array of "words", removing any extra chars in the process (for update)
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
    clean_data = cleanTableData(data)            # returns str of "cleaned" data w/o beginning and end parenthesis
    new_data = clean_data.split(', ')       # return str back to an array
    
    test_file = os.path.join(cwd, tbl)
    if(not os.path.exists(test_file)):             # make sure the file doesn't already exist 
        with open(tbl, 'w') as fp:
            for i in new_data:                     # iterate through elements
                if(i.__contains__(',')):
                    fp.write(i[0:-1])              # write the data but ignore the , at the end of the string
                    fp.write(' | ')                # and write a dividing ' | ' if there was a ','
                else:
                    fp.write(i + ' ')              # else just write the data as usual
            # fp.write('\n')
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
    values = data[3:]
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

# update desired elements in table ###########################################################################################
def updateTable(tbl, tbl_elements, set_var, set_value, where_var, where_value):
    filePath = os.path.join(os.getcwd(), tbl)
    if(not os.path.exists(filePath)):
        print("!Failed to update table " + tbl + " because it does not exist.")
    else:
        if(set_var == "pid"):
            set_var = 0
        elif(set_var == "name"):
            set_var = 1
        elif(set_var == "price"):
            set_var = 2
        else:
            print("!Failed to update table because " + set_var + " does not exist.")
        
        if(where_var == "pid"):
            where_var = 0
        elif(where_var == "name"):
            where_var = 1
        elif(where_var == "price"):
            where_var = 2
        else:
            print("!Failed to update table because " + where_var + " does not exist.")
        numUpdated = 0
        
        for row in tbl_elements:
            if(row[where_var] == where_value):
                row[set_var] = set_value
                numUpdated +=1
            
        if(numUpdated == 1):
            print("1 record modified.")
        else:
            print(str(numUpdated) + " records modified.")
            
        f = open(tbl, "w")
        for row in tbl_elements:
            for element in row:
                f.write(str(element) + " | ")
            f.write("\n")
        f.close()
        ####################################################################################
    
# table query (file)
def query_tbl(tbl):
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):
        with open(tbl, 'r') as fp:
            print(fp.read())               # print entire entry
    else:
        print('!Failed to query table ' + tbl + ' because it does not exist.')

# main fct that handles user input
def main():
    table_elements = []
    while (True):
        user_in = input('')                                           # take in and parse user input
        user_in = user_in.replace(';', '')
        input_list = user_in.split(' ')
        
        if ('--' in input_list):                                      # determine and run desired fct
            pass
        elif('.EXIT' in input_list):
            print('All done.')
            exit()
        elif('CREATE' in input_list and 'DATABASE' in input_list):
            create_database(input_list[2])
        elif('DROP' in input_list and 'DATABASE' in input_list):
            delete_database(input_list[2])
        elif('USE' in input_list):
            use_database(input_list[1])
        elif('CREATE' in input_list and 'TABLE' in input_list):
            create_tbl(input_list[2], input_list[3:])
        elif('DROP' in input_list and 'TABLE' in input_list):
            delete_tbl(input_list[2])
        elif('insert' in input_list):
            table_elements.append(insert_info_tbl(input_list))
        ###########################################################################
        elif('update' in input_list): 
            setWords = parse_input()      # prompts the user for first line of input and seperates into array
            set_var = setWords[1]         # what element are we changing
            set_value = setWords[3]       # what value of this are we changing to
            whereWords = parse_input()    # prompts the user for second line of input and seperates into array
            where_var = whereWords[1]     # what element are we looking at
            where_value = whereWords[3]   # what value are we looking for
            updateTable(input_list[1], table_elements, set_var, set_value, where_var, where_value)
            # update_tbl(table_elements, input_list[1])
        ###########################################################################
        elif('select' and '*' in input_list): # print the entire table
            query_tbl(input_list[3])

# ensures main fct is called first
if __name__ == "__main__":
    main()
