list=[]

def and_operation(hex1, hex2):

    #change args to decimals
    dec1 = int(str(hex1), 16)
    dec2 = int(str(hex2), 16)

    #change decs to binaries
    bin1 = (bin(dec1)[2:])
    bin2 = (bin(dec2)[2:])


    for i in range(0, len(bin1)):
        bin1_el = bin1[i]
        bin2_el = bin2[i]
        if (bin1_el == '1' and bin2_el == '0') or (bin1_el == '0' and bin2_el == '1'):
            list.append('0')
        elif (bin1_el == '1' and bin2_el == '1') or (bin1_el == '0' and bin2_el == '0'):
            list.append('1')
    rejoin = ''.join(list)
    print(f"\nand_operation({hex1}, {hex2})\n")
    print(bin1)
    print(bin2, "\n")
    print(rejoin)


and_operation(33, '3d')

    



