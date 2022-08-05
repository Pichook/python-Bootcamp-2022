list=[]
def or_operation(hex1, hex2):
    
    dec1 = int(str(hex1), 16)
    dec2 = int(str(hex2), 16)

    bin1 = bin(dec1)
    bin2 = bin(dec2)

    for i in range(0, len(bin1)-1):
        b1 = bin1[i]
        b2 = bin2[i]
        if (b1 == '1' or b2 == '0') or (b1 == '0' or b1 == '1') or (b1 == '1' or b2 == '1'):
            list.append('1')
        elif b1 == '0' or b2 == '0':
            list.append('0')
    rejoin = ''.join(list)
    print(f"or_operation({hex1}, {hex2})\n")
    print(bin1[2:])
    print(bin2[2:], "\n")
    print(rejoin)


or_operation (33, '3d')





#     print(f"or_operation({hex1}, {hex2})\n")
#     print(bin1[2:])
#     print(bin2[2:], "\n")
#     # if len(x_or) != len(bin1):
#     #     # n = len(bin1) - len(x_or) 
#     #     new_xor = x_or.ljust()
#     #     print(new_xor[2:])
#     #     return
#     print(" ", x_or[2:])

# or_operation(33, '3d')

