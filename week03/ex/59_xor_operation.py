def or_operation(hex1, hex2):
    
    dec1 = int(str(hex1), 16)
    dec2 = int(str(hex2), 16)

    bin1 = bin(dec1)
    bin2 = bin(dec2)

    x_or = bin(0b110011 ^ 0b111101)
    print(f"or_operation({hex1}, {hex2})\n")
    print(bin1[2:])
    print(bin2[2:], "\n")
    # if len(x_or) != len(bin1):
    #     # n = len(bin1) - len(x_or) 
    #     new_xor = x_or.ljust()
    #     print(new_xor[2:])
    #     return
    print(" ", x_or[2:])

or_operation(33, '3d')
