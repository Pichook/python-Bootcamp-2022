

def hex_to_dec(num):
    num = str(num)
    for char in num:
        if ((char < '0' or char >'9') and (char < 'A'  or char > 'F')):
            print("This is not a hexa-decimal number")
            return
    a = int(num, 16)
    print(a)

    
# hex_to_dec('BA1')
# hex_to_dec('HH')
hex_to_dec(251)







