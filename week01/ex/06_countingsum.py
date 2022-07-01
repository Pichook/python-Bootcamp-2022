# Write a program in python to input numbers continuously until the user enters “stop”. Each
# time  the  user  inputs  a  number  it  must  be  added  to  the  integer  variable  “sum”.  If  the  user
# inputs anything other than a valid number show him a warning message “The input must be
# a valid number” and  then  continue  getting  the  input  again.  Once  user  enters  “stop”  then
# the program must display “The Sum is: <Sum of the given numbers>” and stop execution.
i = ''
while i != 'stop':
    number = input("Enter number here: ")
    x = number.isdigit()
    if x == False:
        print("The input must be a valid number.")
        break
    else:
        num = int(number)
        print(num)
    i = input("Write stop to stop loop: ")
if i == 'stop':
    while x == True:
        sum = num +num
    print(f"The sum is {sum}")
