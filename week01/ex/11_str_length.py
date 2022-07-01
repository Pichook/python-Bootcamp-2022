# Write a program that ask for a string and display the string length. If nothing is passed inside
# the input function, the program will display “The string is empty.”

sentence = input("Enter words: ")
if sentence == '':
    print("The String is empty.")
else:
    print(len(sentence))

