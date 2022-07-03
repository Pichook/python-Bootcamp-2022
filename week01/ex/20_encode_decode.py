# Write a program to input a string and encode and decode it with the above ROT13 system.
# Prompt the user to input 1 to encode and the string to encode. Prompt the user to input 2 and
# to input the encoded string to be decoded


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetBig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rot13(sent):
    sent1 = ''
    for i in sent:
        if i in alphabet:
            if alphabet.index(i)<13:
                sent1 += alphabet[alphabet.index(i) + 13]
            else:
                sent1 += alphabet[alphabet.index(i) - 13]
        elif i in alphabetBig:
            if alphabetBig.index(i)<13:
                sent1 += alphabetBig[alphabetBig.index(i) + 13]
            else:
                sent1 += alphabetBig[alphabetBig.index(i) - 13]
        else:
            sent1 += i
    return sent1

choice = int(input("1 for encode \n2 for decode \nEnter: "))
if choice == 1:
    x = input("Enter words to be encoded: ")
    print("The encoded text is: ", rot13(x), "\nDo you want to continue?")
    answer = input("Answer: ")
    if answer == 'Yes' or 'yes':
        choice1 = int(input("1 for encode \n2 for decode \nEnter: "))
        if choice1 == 1:
            x = input("Enter words to be encoded: ")
            print("The encoded text is: ", rot13(x), "[Y/N]")
        elif choice1 == 2:
            z = input("Enter words to be decoded: ")
            print("The decoded text is: ", rot13(z))
    elif answer == 'No' or 'no':
        print("Thank you.")

elif choice == 2:
    z = input("Enter words to be decoded: ")
    print("The decoded text is: ", rot13(z), "\nDo you want to continue?")
    answer = input("Answer: ")
    if answer == 'Yes' or 'yes':
        choice1 = int(input("1 for encode \n2 for decode \nEnter: "))
        if choice1 == 1:
            x = input("Enter words to be encoded: ")
            print("The encoded text is: ", rot13(x))
        elif choice1 == 2:
            z = input("Enter words to be decoded: ")
            print("The decoded text is: ", rot13(z))
    elif answer == 'No' or 'no':
        print("Thank you.")
