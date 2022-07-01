sent = input("Enter in lowercase please: ")
x = sent.isdigit()
if x == True:
    print("Invalid input.")
else:
    if sent == '':
        print("The string is empty.")
    else:
        x = sent.upper()
        print(f"Capital: {x}")