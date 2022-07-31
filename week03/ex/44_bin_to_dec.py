def bin_to_dec(bina):
    set_c = {'0', '1'}
    set_b = set(str(bina))
    if (set_b == set_c or set_b == 0 or set_b == 1):
        dec = 0
        i = 0
        bina = int(bina)
        while bina != 0:
            rem = bina % 10
            dec = dec + rem * pow(2, i)
            bina = bina // 10
            i += 1
        print(dec)
    else: 
        print("This is not a binary number")


bin_to_dec(110011)
# bin_to_dec(2)
bin_to_dec('asd')