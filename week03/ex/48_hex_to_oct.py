def hex_to_oct(num):
    for char in num:
        if ((char < '0' or char>'9') and (char <'a' or char > 'f') and (char <'A' or char > 'F')):
            print("This is not a hexa-decimal number")
            return
    dec = int(num, 16)
    oct_num = oct(dec)[2:]
    print(oct_num)

hex_to_oct('2b9')
hex_to_oct('2B9')
hex_to_oct('apple')