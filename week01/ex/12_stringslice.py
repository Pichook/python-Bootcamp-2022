# Write a program that ask for a string and divide the string into two equal strings and display.
# If nothing is passed for the string, the program should display “The string is empty.”

string = input("Write here: ")
if string == '':
    print("The string is empty.")
else:
    a = string[0:len(string)//2]
    b = string[len(string)//2:len(string)+1]
    print(a+b)

