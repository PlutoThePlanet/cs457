import os
import shutil

cwd = os.getcwd() # keep track of which directory being used in system (when switched)

# database creation (folder)
def create_database(new_dir):
    try:
        path = os.path.join(cwd, new_dir)
        os.mkdir(path)
        print('Database ' + new_dir + ' created.')
    except FileExistsError:
        print('!Failed to create database' + new_dir + ' because it already exists.')

# database deletion (folder)
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
        cwd = os.path.join(cwd, db)
        os.chdir(cwd)
        print('Using Database ' + db + '.')
    except FileNotFoundError:
        print('!Failed to use ' + db + ' because it does not exist.')
        
# table creation (file)
#def create_tbl():
    

# table deletion (file)
#def felete_tbl():
    

# table update (file)
#def update_tbl():
    

# table query (file)
#def query_tbl():
    

# main fct that handles user input
def main():
    print(cwd)
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
            print('create tbl')
        elif('DROP' in input_list and 'TABLE' in input_list):
            print('delete tbl')
        elif('ALTER' in input_list):
            print('alter tbl')
        elif('SELECT' in input_list):
            print('tbl data')

# ensures main fct is called first
if __name__ == "__main__":
    main()