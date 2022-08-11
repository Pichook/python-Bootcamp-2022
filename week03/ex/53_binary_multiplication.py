def binary_multiplication(dec1, dec2):
    bin1 = bin(dec1)
    bin2 = bin(dec1)

    mult = dec1 * dec2

    print(f"binary_multiplication({dec1}, {dec2})\n")

    print("Num 1: ", bin1[2:], "\n")
    print("Num 2: ", bin2[2:], "\n")
    
    print("Difference (Binary):", bin(mult)[2:], "\n")
    print("Difference (Decimal):", str(mult).replace('0b', ''), "\n")

binary_multiplication(60, 50)