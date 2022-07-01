# Write a program in python to input numbers continuously until the user enters “stop”. Each
# time  the  user  inputs  a  number  it  must  be  added  to  the  integer  variable  “sum”.  If  the  user
# inputs anything other than a valid number show him a warning message “The input must be
# a valid number” and  then  continue  getting  the  input  again.  Once  user  enters  “stop”  then
# the program must display “The Sum is: <Sum of the given numbers>” and stop execution.

sum = 0
while True:
    number = input("Enter number here: ")
    if number == "stop":
        break
    else:
        if number.isdigit():
            num = int(number)
            sum += num
        else:
            print("The input must be a valid number")
print(f"Sum of given number: {sum}")
