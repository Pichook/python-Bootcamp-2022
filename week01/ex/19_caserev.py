# Write a program to input a string and replace lowercase with uppercase and uppercase with
# lowercase If nothing is passed for the string, the program should display “The string is empty.

word = input("enter:")
word1 = " "
if word == '':
    print("The string is empty.")
else:
    for i in range(0, len(word)):
        if word[i].islower():
            word1 += word[i].upper()
        else:
            word1 += word[i].lower()
    print(word1)
