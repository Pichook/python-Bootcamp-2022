from genericpath import isfile
from genericpath import exists
from datetime import datetime
import shutil
import os


class FileLib:

    def current_path(self):
        print("\n", os.getcwd(), "\n")

    def inspect(self):
        x = os.listdir()
        list=[]
        for i in range(len(x)):
            if os.path.isdir(x[i]):
                list.append((x[i], "Folder"))
            elif os.path.isfile(x[i]):
                list.append((x[i], "File"))
            else: 
                return list
        print(list)
    
    def read(self, line):

        check_file = exists(line)
        if check_file == True:
            file = open(line, 'r')
            x = file.readlines()
            lin = ''.join(x)
            print(lin)
            file.close()
        else:
            print("Invalid FILENAME")

    def write(self, filename, content):
        check = exists(filename)

        if check == False:
            new_file = open(filename, 'x')
            new_file.write(content)
            new_file.close()
            print('1')

        elif check == True:
            new_file2 = open(filename, 'w')
            new_file2.write(content)
            new_file2.close()
            print('1')


    def create_folder(self, folder_list):

        for i in range(len(folder_list)):
            
            if os.path.exists(folder_list[i]):
                shutil.rmtree(folder_list[i])
                d = os.getcwd()
                path = os.path.join(d, folder_list[i])
                os.makedirs(path)
                print('1')
            else:
                d = os.getcwd()
                path = os.path.join(d, folder_list[i])

                os.mkdir(path)
                print('1')

    def remove(self, name):
            if os.path.isfile(name):
                os.remove(name)
                print('1')
                
            elif os.path.isdir(name):
                shutil.rmtree(name)
                print('1')
    
    def append(self, filename, content):
        new_text = open(filename, 'a')
        today = datetime.today()
        dt_str = today.strftime("%d/%m/%Y %H:%M:%S")
        new_text.write(f"\n[{dt_str}] {content} ")
        new_text.close()
    
# FileLib().remove('fol333')
# list = ['fol23', 'fol49', 'fol333']
# FileLib().create_folder(list)
# FileLib().write('banana.txt', "Banana used to be wild.")
# FileLib().read("banana.txt")
# FileLib().current_path()
# FileLib().inspect()
# FileLib().append("banana1.txt", "Nothing's wrong about potassium.")