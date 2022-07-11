string = str(input("Please input a paragraph: "))
searched_word = str(input("Please input a search string: "))

def countOccurrence(string, word):
    banana = string.count(word)
    return banana

search = countOccurrence(string, searched_word)
print(f"There are {search} occurrences.")
print("Do you want to replace the text [Y/N]?")
answer = input("[Y/N]: ")
# while True:
if answer == 'n' and 'N':
    print("Oh! You don't like to replace, Do you want to check again [Y / N]?")
    answer2 = str(input("[Y / N]: "))
    while True:
        if answer2 == 'y' and 'Y':
            string = str(input("Please input a paragraph: "))
            searched_word = str(input("Please input a search string: "))
            search = countOccurrence(string, searched_word)
            print(f"There are {search} occurrences.")
            print("Do you want to replace the text [Y/N]?")
            answer = input("[Y/N]: ")
            if answer == 'y':
                replace = input("Please input a replacement string: ")
                num = int(input("How many occurrences do you want to replace? "))
                text_replace = string.replace(searched_word, replace, num)
                print(f"{num} words have been replaced from the paragraph")
                print(text_replace)
                break
            elif answer == 'n':
                break
        elif answer2 == 'n' and 'N':
            break
elif answer == 'y' and 'Y':
    replace = input("Please input a replacement string: ")
    num = int(input("How many occurrences do you want to replace?"))
    text_replace = string.replace(searched_word, replace, num)
    print(f"{num} words have been replaced from the paragraph")
    print(text_replace)
else:
    while True:
        print("Please give proper input.")
        print("Do you want to replace the text [Y/N]?")
        answer = input("[Y/N]: ")
    # while True:
        if answer == 'n' and 'N':
            print("Oh! You don't like to replace, Do you want to check again [Y / N]?")
            answer2 = str(input("[Y / N]: "))
            # while True:
            if answer2 == 'y' and 'Y':
                string = str(input("Please input a paragraph: "))
                searched_word = str(input("Please input a search string: "))
                search = countOccurrence(string, searched_word)
                print(f"There are {search} occurrences.")
                print("Do you want to replace the text [Y/N]?")
                answer = input("[Y/N]: ")

                if answer == 'y' and 'Y':
                    replace = input("Please input a replacement string: ")
                    num = int(input("How many occurrences do you want to replace? "))
                    text_replace = string.replace(searched_word, replace, num)
                    print(f"{num} words have been replaced from the paragraph")
                    print(text_replace)
                    break
                elif answer == 'n' and 'N':
                    continue
            elif answer2 == 'n' and 'N':
                break
        elif answer == 'y' and 'Y':
            replace = input("Please input a replacement string: ")
            num = int(input("How many occurrences do you want to replace? "))
            text_replace = string.replace(searched_word, replace, num)
            print(f"{num} words have been replaced from the paragraph")
            print(text_replace)
            break



