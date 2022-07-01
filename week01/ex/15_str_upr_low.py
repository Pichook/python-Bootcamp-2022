# Write a program to input a string and split the string into two equal strings. Convert and
# display the first half into uppercase and second half into lowercase If nothing is passed for
# the string, the program should display “The string is empty

sent = input("Enter words here: ")
x = sent.isdigit()
if x == True:
    print("Invalid Input.")
else:
    if sent == '':
        print("The string is empty.")
    else:
        a = sent[0:len(sent)//2]
        b = sent[len(sent)//2:len(sent)+1]
        print(a.upper() + b.lower())
