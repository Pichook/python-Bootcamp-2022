import random

def random_nums(num):
    sum = 0
    for i in range(1, num+1):
        rand = random.randint(1, 8)
        print(f"Dice {i}: {rand}")
        sum += rand
    print('='*10)
    print("RESULT: ", sum)
    print('='*10)




Intro = "Welcome to the dices game!"
print(Intro)

roll = input("Enter the number of dices you want to roll: ")
true_roll = roll.isdigit()
sum = 0
list = []
if true_roll == True:
    roll = int(roll)
    if roll == 1:
        print("RESULT: ", random.randint(1, 8))
    elif roll >=2 and roll <=8:
        random_nums(roll)
    elif roll > 8:
        while True:
            print("USAGE: The number must be between 1 and 8")
            roll = input("Enter the number of dices you want to roll: ")
            roll_int = int(roll)
            if roll_int > 8:
                continue
            else:
                if roll_int == 1:
                    print("RESULT: ", random.randint(1, 8))
                elif roll_int >= 2 and roll_int <= 8:
                    random_nums(roll_int)
            break
elif (true_roll == False) or roll == '':
    while True:
        print("USAGE: The number must be between 1 and 8")
        roll = input("Enter the number of dices you want to roll: ")
        true_roll2 = roll.isdigit()
        if true_roll2 == False:
            continue
        elif true_roll2 == True:
            roll = int(roll)
            if roll == 1:
                print("RESULT: ", random.randint(1, 8))
            elif roll >= 2 and roll <= 8:
                random_nums(roll)
            elif roll > 8:
                while True:
                    print("USAGE: The number must be between 1 and 8")
                    roll = input("Enter the number of dices you want to roll: ")
                    roll_int = int(roll)
                    if roll_int >8:
                        continue
                    else:
                        if roll_int == 1:
                            print("RESULT: ", random.randint(1, 8))
                        elif roll_int >= 2 and roll_int <= 8:
                            random_nums(roll_int)
                    break
        break
