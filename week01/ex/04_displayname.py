# Write a program in python that prompts “Input your name:” (The program waits for your
# input) and once you input name, prompts “Input number of times to print” (The program
# waits for your input). Display the name for number of times mentioned by the user. If the
# user didn’t enter name display “No name entered

name = input("Enter name here: ")
number = int(input("Enter number of loops: "))

for i in range(0, number):
    print(name.capitalize())

if name == '':
    print("No name entered.")