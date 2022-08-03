
def oct_to_dec(num):
    x = num.isdigit()
    set_num = set(str(num))
    if (x == True) and ('9' not in set_num):
        dec = 0
        i = 0
        num = int(num)
        while num != 0:
            rem = num % 10
            dec = dec + rem * pow(8, i)
            num = num // 10
            i += 1
        print(dec)
    else: 
        print("This is not an octal number")

oct_to_dec('750')
oct_to_dec('das')
oct_to_dec('759')