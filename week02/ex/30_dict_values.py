
my_dict = {120: ("Visal", "Borey", "Sovann"), 130: ("Hout","Mouyleng","Pidor"), 140: ("Nary", "Misora", "Masaki")}

val = my_dict.values()
x = tuple(val)

def join_tuple_string(dict) -> str:
   return ' '.join(dict)

# joining all the tuples
result = map(join_tuple_string, x)

# converting and printing the result
val_list = list(result)
print(val_list)

def dict_values(dict):
   key = dict.keys()
   key_list = list(key)
   for i in range(0, len(dict)):
      print(key_list[i], ':', val_list[i])
      if i < len(dict)-1:
         print("*****")

dict_values(my_dict)
