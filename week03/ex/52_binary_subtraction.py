# def binary_subtraction(num1, num2):
    # bin1 = bin(num1)[2:]
def flip(num):
    if num == 1:
        return 0
    else:
        return 1


def com_bin(num2):
    bin2 = bin(num2)[2:]
    new_b2 = []
    if '1' not in new_b2:
        for j in range(len(bin2)-1, -1, -1):
            b2 = bin2[j]
            if b2 == '0':
                new_b2.append('0')
            elif b2 == '1':
                new_b2.append('1')
    elif '1' in new_b2:    
        for k in range(len(bin2)-len(new_b2), -1, -1):
            rev = flip(k)
            new_b2.append(rev)

    rejoin1 = ''.join(new_b2[::-1])
    print(bin2)
    print(rejoin1)
com_bin(12)









    # bin1_len = len(bin1)
    # carry = "0"
    # list = []
    # for i in range(bin1_len-1, -1, -1):
    #     b1 = bin1[i]
    #     b2 = bin2[i]
    #     if b1 == '0' and b2 == '0' and carry == '0':
    #         list.append('0')
    #         carry = 0
    #     elif b1 == '1' and b2 == '1' and carry == '0':
    #         list.append('0')
    #         carry = '0'
    #     elif b1 == '0' and b2 == '1' and carry == '2':
    #         list.append('')

# import numpy as np

# mat = np.array([[1, 2, 3], [4, 5, 6]])
# print (mat)
    