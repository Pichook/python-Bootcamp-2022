# Write a program in python to input a number and store into the variable “num”. Add all odd
# number and even numbers into a separate variables “oddSum” and “evenSum”. Display the
# sum of odd and even number.

sum_even = 0
sum_odd = 0
num = int(input("Enter number: "))
for i in range(num+1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(sum_even)
print(sum_odd)

