list=[]

def message_converter(str):
    for i in str:
        con_i = ord(i)
        hex_i = hex(con_i)
        list.append(hex_i[2:].upper())
    rejoin = ''.join(list)
    print(f"message_converter('{str}')\n")
    print(rejoin)

message_converter("Hello")