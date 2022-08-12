# from genericpath import exists
# import os
# import shutil


# def auto_folder(list):

#     for i in range(len(list)):
        
#         if os.path.exists(list[i]):
#             while True:
#                 q = input("Are you sure you want to replace <FOLDER_NAME>? [Y/N] ")
                
#                 if q == 'y':
#                     shutil.rmtree(list[i])
#                     d = os.getcwd()
#                     path = os.path.join(d, list[i])
#                     os.makedirs(path)
#                     print('1')
#                     break

#                 elif q == 'n':
#                     print('0')
#                     break

#                 else: 
#                     print("Invalid Option")
#                     continue
#         else:
#             d = os.getcwd()
#             path = os.path.join(d, list[i])

#             os.mkdir(path)
#             print('11')



# list = ['fol33', 'fol44']
# auto_folder(list)

import requests
BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    "category": 'electronic'
}

response = requests.patch(f"{BASE_URL}/products/21", json=updated_product)
print(response.json())


