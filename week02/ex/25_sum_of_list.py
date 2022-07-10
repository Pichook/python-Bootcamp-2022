# Write a python function that receives a list in the arguments and return the sum of the list.

# num = int(input("Enter number here: "))
def random_tuple(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    print(sum)
random_tuple([20,15,10,30])
