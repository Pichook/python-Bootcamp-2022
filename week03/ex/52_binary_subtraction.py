def binary_subtraction(num1, num2):
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    print("Num 1: ", bin1)
    print("Num 2: ", bin2)
    sub = num1 - num2
    print("Difference (Binary): ", bin(sub)[2:])
    print("Difference (Decimal): ", sub)

binary_subtraction(60, 50)
