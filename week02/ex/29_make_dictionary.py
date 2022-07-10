# Write a python function that receives a list of integers and a tuple of strings in the
# arguments. The function must return a dictionary which is formed with the list element as
# keys and tuple elements as the values.


def make_dictionary(list, tuple):
    my_dict = dict(zip(list, tuple))
    print(my_dict)

list = [50,10,62]
tuple = ("B", "T", "D")
make_dictionary(list, tuple)


