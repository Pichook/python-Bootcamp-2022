# Write a python function that receives a list and a slice_number in the arguments. The
# # function must return a new list which is retrieved after slicing the list from front and rear
# # with the slice_number. If the second argument is 2 then 2 numbers at the front and back
# # must be removed in the returned list.

def slice_list(list, slice_number):
    new_list = list[slice_number: -slice_number]
    return new_list

my_list = [50,10,62,32,64,78,90]
print(my_list)
slice_num = int(input("Enter number here: "))
result = slice_list(my_list, slice_num)

if result == []:
    print("Input out of bound.")
else:
    print(result)
