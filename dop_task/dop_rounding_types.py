# Реализуйте следующие типы округления:
# 1. К ближайшему целому
# 2. К большему
# 3. К меньшему
# 4. 
# Пользоваться модулем math и функцией round нельзя.

def nearest_integer(num):
    res = int(num // 1)
    return res

def more_integer(num):
    if num % 1 == 0:
        res = int(num // 1)
    else:
        res = int(num // 1) + 1
    return res

def lesser_integer(num):
    if num % 1 > 0:
        res = int(num // 1)
    else:
        res = int(num // 1) - 1
    return res

def banking(num):
    res = int(abs(num) * 100)
    if res % 2 != 0:
        res += 1
    if num < 0:
        res = 0 - res
    return res / 100

number = float(input("Введите число: "))
print("Округление числа к ближайшему целому:", nearest_integer(number))
print("Округление числа к большему целому:", more_integer(number))
print("Округление числа к меньшему целому:", lesser_integer(number))
print("Банковское округление числа:", banking(number))