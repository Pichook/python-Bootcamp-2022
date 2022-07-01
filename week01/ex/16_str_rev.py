# Write a program to input a string and split the string into two equal strings. Convert and
# display the first half into reverse order of the actual string and second half should be in the
# actual order. If nothing is passed for the string, the program should display “The string is
# empty.”

sent = input("Enter sentence here: ")
x = sent.isdigit()
if x == True:
    print("Invalid Input.")
else:
    if sent == '':
        print("The string is empty.")
    else:
        a = sent[(len(sent)//2)-1::-1]
        b = sent[len(sent)//2:len(sent)+1]
        print(a+b)
