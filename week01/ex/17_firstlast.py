# Write a program to input a string and get the first and last character of the string. If nothing is
# passed for the string, the program should display “The string is empty.”

sent = input("Enter word here: ")
x = sent.isdigit()
if x == True:
    print("Invalid Input.")
else:
    if sent == '':
        print("The string is empty.")
    else:
        a = sent[0]
        b = sent[-1]
        print("First letter: ", a)
        print("Last letter: ", b)