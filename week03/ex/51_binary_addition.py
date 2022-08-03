def binary_addition(num1,  num2):
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    print("Num 1: ", bin1)
    print("Num 2: ", bin2)
    bin1_len = len(bin1)
    carry = "0"
    list = []
    for i in range(bin1_len-1, -1, -1):
        b1 = bin1[i]
        b2 = bin2[i]
        if b1 == '0' and b2 == '0' and carry == '0':
            list.append('0')
            carry = '0'
        elif b1 == '1' and b2 == '1' and carry == '0':
            list.append('0')
            carry = '1'
        elif b1 == '1' and b2 == '1' and carry == '1':
            list.append('1')
            carry = '1'
        elif(b1 == '1' and b2 == '0' and carry == '0') or (b1 == '0' and b2 == '1' and carry == '0') or (b1 == '0' and b2 == '0' and carry == '1'):
            list.append('1')
            carry = '0'
        else: 
            list.append('0')
            carry = '1'
    if carry == '1':
        list.append('1')    
    rejoin = ''.join(list[::-1])
    print("Sum (Binary): ", rejoin)
    print("Sum (Decimal): ", int(rejoin, 2))
binary_addition (60, 50)


