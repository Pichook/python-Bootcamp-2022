from genericpath import exists
import os

def write_file(filename, content):
    check = exists(filename)

    if check == False:
        new_file = open(filename, 'x')
        new_file.write(content)
        new_file.close()
        print('11')

    elif check == True:
        while True:
            ans = input("Are you sure you want to replace <FILENAME>? [Y/N] ")
            if ans == 'y' and 'Y':
                new_file2 = open(filename, 'w')
                new_file2.write(content)
                new_file2.close()
                print('111')
                break

            elif ans == 'n' and 'N':
                print('0')
                break

            else: 
                print("Invalid Option")
                continue

write_file('banana.txt', "Banana used to have seeds.")

    