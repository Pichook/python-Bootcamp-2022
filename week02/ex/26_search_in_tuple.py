# Write a python function that receives a tuple and search number in the arguments and
# return the index of the search number from the tuple. If the search number is not found in
# the tuple return “Element not found in the tuple”.


def index_search(tuple, sno):
    for i in range(0, len(tuple)):
        if tuple[i] == sno:
            return i + 1
    else:
        return -1

tuple = (1, 55, 21, 62, 2)
print(tuple)
sno = int(input("Enter searched number: "))
search = index_search(tuple, sno)

if search == -1:
    print("Element not found in the tuple.")
else:
    print(f"Element is found at {search}")