# Write a function that receives an argument and generate random number between 0 to 100
# for n times based on the argument and stored in a tuple. Display the tuple and return the
# sum of numbers to the caller.
import random
num = int(input("Enter number here: "))
def random_tuple(num):
    sum =0
    num = int(num)
    list = []
    for i in range(1, num+1):
        number = random.randint(0, 100)
        print(f"Random number {i}: {number}")
        list.append(number)
        sum += number
    print(tuple(list))
    print(sum)

random_tuple(num)


