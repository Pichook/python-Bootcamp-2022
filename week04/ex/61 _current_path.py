import os

def current_path(str):
    if str == 'yes':
        print("\n", os.getcwd(), "\n")

    else:
        print ("-1")

current_path('yes')