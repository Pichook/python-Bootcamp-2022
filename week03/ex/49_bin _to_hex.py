def bin_to_hex(num):
    num = str(num)
    for char in num:
        if char <'0' or char > '1':
            print("This is not a binary number")
            return
    dec = int(num, 2)
    hexa = hex(dec)[2:]
    print(hexa)

bin_to_hex(11001101)
bin_to_hex('num')
bin_to_hex(27)