# Paige Mortensen
# CS 457 PA 4
# 12/18/22

import os
import shutil
import re

cwd = os.getcwd()           # keep track of which directory being used in system (when switched, so you can stay there for mult. actions)
home_dir = os.getcwd()      # always able to refer back to original "home" directory (used for switching between databases)
fileChangeFlag = 0          # file has been modified and can be comitted (somethng changed = 1, unchanged = 0)

# reads stored data from file into useable array
def file_to_array(tbl):
    data_arr = []
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):          # make sure the file exists
        with open(tbl, 'r') as file:
            for line in file:
                line = line.strip() 		# remove \n char
                data = line.split(" ")
                data_arr.append(data)		# create 2d array
            for i in data_arr:
                for j in i:
                    if(j == "|"):
                        i.remove(j)
        temp_str_1 = (data_arr[0][0] + " " + data_arr[0][1])
        temp_str_2 = (data_arr[0][2] + " " + data_arr[0][3])
        temp_arr = []
        temp_arr.append(temp_str_1)
        temp_arr.append(temp_str_2)
        data_arr.pop(0)
        data_arr.insert(0, temp_arr)
        return data_arr
    else:
        print('!The table(s) you are looking for does not exist.')

# cleans up input of beginning and ending ()
def cleanValues(values):
    clean_vals = []
    for elem in values:
        clean_val_1 = elem.replace('(', '')
        clean_val_2 = clean_val_1.replace(')', '')
        clean_vals.append(clean_val_2)
    return clean_vals

# seperates input into array of "words", removing any extra chars in the process (for update, delete fct - where extra usr input is needed)
def parse_input():
    usr_in = input("")                          # get input
    words = re.split("[ \t,;']()", usr_in)        # seperate on special chars
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
        print('!Failed to create database ' + new_dir + ' because it already exists.')

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
    cleanData = cleanValues(data)
    test_file = os.path.join(cwd, tbl)
    if(not os.path.exists(test_file)):             # make sure the file doesn't already exist 
        with open(tbl, 'w') as fp:
            fp.write('lockFlag = 0\n')             # the file begins as unlocked
            for i in cleanData:                    # iterate through elements
                if(i.__contains__(',')):
                    fp.write(i[0:-1])              # write the data but ignore the , at the end of the string
                    fp.write(' | ')                # and write a dividing ' | ' if there was a ','
                else:
                    fp.write(i + ' ')              # else just write the data as usual
        print('Table ' + tbl + ' created.')
    else:
        print('!Failed to create table ' + tbl + ' because it already exists.')
        
# table deletion (file)
def delete_tbl(tbl):
    try:
        os.remove(tbl)
        print('Table ' + tbl + ' deleted.')
    except FileNotFoundError:
        print('!Failed to delete ' + tbl + ' because it does not exist.')

# insert new data into file
def insert_info_tbl(data):
    new_values = ((data[4])[1:-1]).split(',')

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

def query_tbl():
    pass

# handles completing transaction(s) within file
def transaction(usr_in, fileData):
    setVal = usr_in[5]
    whereVal = usr_in[9]

    fp = open(usr_in[1], 'r')
    lockLine = fp.readline()
    if('1' in lockLine):
        print('Error: Table ' + usr_in[1] + ' is locked!')
        return
    fp.close()

    # test_file = os.path.join(cwd, usr_in[1])
    with open(usr_in[1], 'w') as fp:
        # change data
        for row in fileData:
            if(row[0] == whereVal):
                row[1] = setVal

        fp.write('lockFlag = 1\n')            # lock file
        fp.write('seat int | status int\n')   # write data to file
        for row in fileData:
                for element in row:
                    fp.write(str(element) + " | ")
                fp.write("\n")
    fileChangeFlag = 1 # the file needs to be comitted

# main fct that handles user input
def main():
    table_elements = []
    while (True):
        user_in = input('')                    # take in and parse user input
        user_in = user_in.replace(';', '')
        input_list = user_in.split(' ')
        
        if ('--' in input_list[0]):               # determine and run desired fct
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
            create_tbl(input_list[2], input_list[3:])
        elif('drop' in input_list and 'table' in input_list):
            delete_tbl(input_list[2])
        elif('insert' in input_list):
            table_elements.append(insert_info_tbl(input_list))
        elif('select' and '*' in input_list):
            query_tbl()
        elif('transaction' in input_list):
            transaction_in = parse_input()
            transaction(transaction_in, table_elements) # may need to save returned values in array to update table_elements
            # update table_elements with their new values
            
# ensures main fct is called first
if __name__ == "__main__":
    main()