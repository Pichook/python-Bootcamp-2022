
from genericpath import isfile
import os


x = os.listdir()
list=[]
def current_folder():
    for i in range(len(x)):
        if os.path.isdir(x[i]):
            list.append((x[i], "Folder"))
        elif os.path.isfile(x[i]):
            list.append((x[i], "File"))
        else: 
            return list
    print(list)

current_folder()

        
    
