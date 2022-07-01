# Write a program to input a string and display the ASCII values of all characters of the string.
#
# c = input("Enter: ")
# print(ord(c))

c = input("Enter here: ")
list=[]
for i in range(0, len(c)):
    list.append(c[i])
for i in list:
    print(f"{i} = {ord(i)}")
