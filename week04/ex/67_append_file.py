import os
from datetime import datetime


def append_file():
    text = ''
    new_text = open("bananab.txt", 'a')
    while True:
        text = input("$: ")
        if text == 'EXIT': 
            break
        else:

            today = datetime.today()
            dt_str = today.strftime("%d/%m/%Y %H:%M:%S")
            new_text.write(f"[{dt_str}] {text} ")
    new_text.close()
        

append_file()    
