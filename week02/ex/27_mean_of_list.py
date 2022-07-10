# Write a python function that receives a list of integers in the arguments and return the mean
# (Average) of the list elements.

def mean_of_list(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
        avg = sum/len(list)
    print(sum)
    print(avg)



my_list = [50,10,62,32]
mean_of_list(my_list)