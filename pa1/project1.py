import os

cwd = os.getcwd() # keep track of which directory being used in system

# database creation (folder)
def create_database(new_dir):
    try:
        path = os.path.join(cwd, new_dir)
        os.mkdir(path)
        print('Database ' + new_dir + ' created.')
    except FileExistsError:
        print('!Failed to create database' + new_dir + ' because it already exists.')

# database deletion (folder)
#def delete_database():
    

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
            print('delete db')
        elif('USE' in input_list):
            print('use db')
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