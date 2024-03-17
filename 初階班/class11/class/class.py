# def hello(name):
#     print(f'hello {name}')

# name = input()
# hello(name)

# def my_min(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# x = my_min(1, 2)
# print('my_min:', x)

import random


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append()
        random.randint(1, 6)
    return dice


cnt = int(input('輸入丟骰子的次數:'))
print(roll_dice(cnt))