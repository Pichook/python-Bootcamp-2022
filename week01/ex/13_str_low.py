# Write a program to input a string and convert that into lowercase If nothing is passed for the
# string, the program should display “The string is empty.”
sent = input("Enter in CAPITAL please: ")
x = sent.isdigit()
if x == True:
    print("Invalid input.")
else:
    if sent == '':
        print("The string is empty.")
    else:
        x = sent.lower()
        print(f"Lower: {x}")
