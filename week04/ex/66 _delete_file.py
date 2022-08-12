import os
import shutil

def delete_file(name):
    while True: 
        ans = input("Are you sure you want to delete <FILENAME>? [Y/N] ")
        if ans.lower() == 'y':
            if os.path.isfile(name):
                os.remove(name)
                print('1')
                break
            elif os.path.isdir(name):
                shutil.rmtree(name)
                print('1')
                break
        elif ans.lower() == 'n':
            print('0')
            break
        else: 
            print('invalid Option')
            continue

delete_file('fol23')
        
    