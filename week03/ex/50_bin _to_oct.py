def bin_to_oct(num):
    for char in num:
        if char < '0' or char > '1':
            print("This is not a binary number")
            return
    dec = int(num, 2)
    octa = oct(dec)[2:]
    print(octa)

bin_to_oct('11001101')
bin_to_oct('222')
bin_to_oct('ashda')
