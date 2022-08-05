def binary_subtraction(dec1, dec2):
    bin1 = bin(dec1)
    bin2 = bin(dec1)

    sub = dec1 - dec2
    str_sub = str(sub).replace('0b', '')

    print(f"binary_subtraction({dec1}, {dec2})\n")

    print("Num 1: ", bin1[2:], "\n")
    print("Num 2: ", bin2[2:], "\n")

    print("Difference (Binary):", bin(sub)[2:], "\n")
    print("Difference (Decimal):", str_sub, "\n")

binary_subtraction(60, 50)