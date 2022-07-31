
def dec_to_bin(num):
    num = int(num)
    return bin(num)[2:]


num = int(input())
print(f"dec_to_bin({num})")
x = dec_to_bin(num)
print(x)




