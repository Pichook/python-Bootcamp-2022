# Write  a  python  program  to  input  a  number  ānā  and  generate  random  numbers  between
# 2000  to  3000(both  numbers  inclusive)  for  ānā  times.  Find  and  display  the  sum  of  even
# numbers from the generated random numbers.
import random

num = int(input("Enter number for random numbers: "))
sum = 0

for i in range(num):
    r1 = random.randint(2000, 3000)
    print("Number: ", r1)
    sum = sum + r1
print("Total: ", sum)
