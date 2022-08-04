def oct_to_hex(num):
    num = str(num)
    for char in num:
        if (char < '0') or (char >= '8'):
            print("This is not an octal number")
            return
    dec = int(num, 8)
    hexa = hex(dec)[2:]
    print(hexa.upper())


oct_to_hex(1271)
oct_to_hex(78)
oct_to_hex('ban2')
