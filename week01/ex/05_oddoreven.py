# Write a program in python to input a number and write the condition to check if the number
# entered is odd or even. Display “The number you have entered is Odd” or “The number
# you have entered is Even” based on the user input. If the user has entered anything other
# than a valid number then display “Not a valid Number”

num = input("Enter number here: ")

x = num.isdigit()
if x == True:
    number = int(num)
    if number % 2 == 0:
        print("The number you have entered is even.")
    else:
        print("The number you have entered is odd.")
else:
    print("Not a valid number")


