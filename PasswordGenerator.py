# генератор паролей
from typing import Any

import random
import string

# Назначаем источники исходных знаков для генерации пароля
lower = string.ascii_lowercase  # lower case latin
upper = string.ascii_uppercase  # upper case latin
digit = string.digits  # arabic digits


def capitals():  # define new function to select 3 uppercase letters
    capitals = []
    for x in range(3):
        capitals += random.choice(upper)
    return capitals


def digits():  # define new function to select 4 digits
    digits = []
    for x in range(4):
        digits += random.choice(digit)
    return digits


def others():  # define new function to fill the rest of 15 numbers w lowercase letters
    others = []
    for x in range(15 - len(capitals()) - len(digits())):
        others += random.choice(lower)
    return others


def generator():  # define a function to compile all products from prev. 3 functions and shuffle within the passphrase
    passw = capitals() + digits() + others()
    password = "".join(random.sample(passw, 15))
    return password


for i in range(10):  # print 10 random passwords to check the integrity
    print(generator())

# запустите ячейку несклько раз: пароли меняются