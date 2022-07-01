# Write a program in python to input a number and store into the variable “num”. Add all odd
# number  and  even  numbers  into  a  separate variables “oddSum”  and  “evenSum”. And
# calculate  the  average  value  of  odd  numbers  and  even  numbers  and  display  them  on  the
# console
evenSum = 0
oddSum = 0
list_even = []
list_odd = []
num = input("Enter number: ")
x = num.isdigit()
if x != True:
    print("Not Valid.")
else:
    number=int(num)
    for i in range(number + 1):
        if i % 2 == 0:
            list_even.append(i)
            evenSum += i
        else:
            list_odd.append(i)
            oddSum += i

print(f"Average of evensum: {evenSum/len(list_even)}")
print(f"Average of oddsum: {oddSum/len(list_odd)}")
