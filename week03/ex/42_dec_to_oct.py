def dec_to_oct(num):
    num = int(num)
    return oct(num)[2:]

conv = dec_to_oct(98)
print(conv)