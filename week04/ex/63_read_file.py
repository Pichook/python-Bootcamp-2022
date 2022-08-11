

from genericpath import exists
import os

def read_file(line):

    check_file = exists(line)
    if check_file == True:
        file = open(line, 'r')
        x = file.readlines()
        lin = ''.join(x)
        print(lin)
        file.close()
    else:
        print("Invalid FILENAME")


read_file('new.txt')