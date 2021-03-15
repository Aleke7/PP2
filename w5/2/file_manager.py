import os

current_url = os.getcwd()

def checking(url):
    if os.path.isfile(url):
        return 'file'
    if os.path.isdir(url):
        return 'dir'

while True:
    if checking(current_url) == 'file':
        print(f'Current opened file {current_url} has several options\nChoose one of them:')
        print('\ta) Print "1" if you want to delete this file')
        print('\tb) Print "2" if you want to rename this file')
        print('\tc) Print "3" if you want to add content to this file')
        print('\td) Print "4" if you want to rewrite content of this file')
        print('\te) Print "5" if you want to return to the parent directory')
        print('\tf) Print "0" if you want to finish work')
    
        my_option = input()

        if my_option == '1':
            os.remove(current_url)
        elif my_option == '2':
            changed_name = input('Print a new name for this file:\n')
            os.rename(os.name, changed_name)
        elif my_option == '3':
            with open(current_url, 'a') as f:
                add = input('Write a text to add to this file:\n')
                f.write(add)
        elif my_option == '4':
            with open(current_url, 'w') as f:
                rewrite = input('Write a text to rewrite content of this file:\n')
                f.write(rewrite)
        elif my_option == '5':
            os.chdir('..')
            print(f'Returned to the parent directory')
        elif my_option == '0':
            print('Work with this file is finished.')
            print('If you want to continue working, start the program again.')
            break
        else:
            print('There is no such option. Please select the option from the list\n')

    if checking(current_url) == 'dir':
        print(f'Current opened directory {current_url} has several options\nChoose one of them:')
        print('\ta) Print "1" if you want to rename this directory')
        print('\tb) Print "2" if you want to print the number of files in this directory')
        print('\tc) Print "3" if you want to print the number of directories in this directory')
        print('\td) Print "4" if you want to list content of this directory')
        print('\te) Print "5" if you want to add file to this directory')
        print('\tf) Print "6" if you want to add new directory to this directory')
        print('\tg) Print "0" if you want to finish work')

        my_option = input()

        if my_option == '1':
            changed_name = input('Print a new name for this directory:\n')
            os.rename(os.name, changed_name)
            os.chdir(changed_name)
        elif my_option == '2':
            files = []
            for i in os.listdir(current_url):
                if os.path.isfile(i):
                    files.append(i)
            print(f'The number of files in this directory: {len(files)}')
        elif my_option == '3':
            dirs = []
            for i in os.listdir(current_url):
                if os.path.isdir(i):
                    dirs.append(i)
            print(f'The number of directories in this directory: {len(dirs)}')
        elif my_option == '4':
            print('The list content of the directory:')
            l = os.listdir(current_url)
            for i in range(len(l)):
                print(f'\t{i + 1}) --> {l[i]}')
                
        elif my_option == '5':
            name_of_file = input('Print the name of new file:\n')
            with open(name_of_file, 'w') as f:
                f.write('')
        elif my_option == '6':
            name_of_dir = input('Print the name of new directory:\n')
            os.mkdir(name_of_dir)
        elif my_option == '0':
            print('Work with this file is finished.')
            print('If you want to continue working, start the program again.')
            break
        else:
            print('There is no such option. Please select the option from the list\n')