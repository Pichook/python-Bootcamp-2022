def binary_addition(num1,  num2):
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    print("Number 1: ", bin1)
    print("Number 2: ", bin2)
    sum = num1 +num2
    print("Sum (Binary): ", bin(sum)[2:])
    print("Sum (Decimal): ", sum)

binary_addition (60, 50)