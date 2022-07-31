def dec_to_hexa(num):
    num = int(num)
    hexa = hex(num)[2:]
    print(hexa.upper())

dec_to_hexa(1500)