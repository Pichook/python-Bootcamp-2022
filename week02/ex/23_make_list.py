# You will write a function that take 3 parameters, combine them and return the parameters
# as a List. However, you function must support any number of arguments

list = []
def make_list(peri1, str, peri2):
    list.append(peri1)
    list.append(str)
    list.append(peri2)
    print(list)

make_list(21,"Hello", 45)