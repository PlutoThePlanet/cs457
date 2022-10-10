import os
import shutil

cwd = os.getcwd() # keep track of which directory being used in system (when switched)
home_dir = os.getcwd()

# cleans up the extra '(' and ')' when taking in table data
def cleanList(arr):
    new_string = ', '.join(str(x) for x in arr)   # joins all array elements into one string
    clean_string = new_string[1:-1]               # erase beginning and end parenthesis
    return clean_string

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
        global cwd
        cwd = home_dir
        cwd = os.path.join(cwd, db)
        os.chdir(cwd)
        print('Using Database ' + db + '.')
    except FileNotFoundError:
        print('!Failed to use ' + db + ' because it does not exist.')
        
# table creation (new file with data)
def create_tbl(tbl, data):
    clean_data = cleanList(data)            # returns str of "cleaned" data w/o beginning and end parenthesis
    new_data = clean_data.split(', ')       # return str back to an array
    
    test_file = os.path.join(cwd, tbl)
    if(not os.path.exists(test_file)):
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
        print('Table ' + tbl + ' created.')
    except FileNotFoundError:
        print('!Failed to delete ' + tbl + ' because it does not exist.')

# table update (file)
# def update_tbl(tbl):
    

# table query (file)
def query_tbl(tbl):
    test_file = os.path.join(cwd, tbl)
    if(os.path.exists(test_file)):
        with open(tbl, 'r') as fp:
            print(fp.read())
    else:
        print('!Failed to query table ' + tbl + ' because it does not exist.')

# main fct that handles user input
def main():
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
        elif('ALTER' in input_list):
            print('alter tbl')
        elif('SELECT' in input_list):
            query_tbl(input_list[3])

# ensures main fct is called first
if __name__ == "__main__":
    main()