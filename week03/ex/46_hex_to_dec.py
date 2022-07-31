

def hex_to_dec(s):
    for char in s:
        if ((char < '0' or char >'9') and (char < 'A'  or char > 'F')):
            print("This is not a hexa-decimal number")
            return
    a = int(s, 16)
    print(a)

    
hex_to_dec('BA1')
hex_to_dec('HH')







