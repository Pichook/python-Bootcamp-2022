# In this program you need to create a function that takes a string and return a list. The
# function must split the string at every space character. If the string is empty you need to
# return an empty list.


def fun_split(str):
    x = str.split()
    print(x)

fun_split(input(f"Enter line here: "))