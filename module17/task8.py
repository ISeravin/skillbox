#Задача 8. Развлечение
import random

n_sticks = int(input("Количество палок: "))
n_throws = int(input("Количество бросков: "))
lst = ['I' for _ in range(n_sticks)]

for throw in range(n_throws):
    print('Бросок', throw + 1, end = '. ')
    left_i = random.randint(1, n_sticks)
    print('Сбиты палки с номера', left_i)
    right_i = random.randint(left_i, n_sticks)
    print('по номер ', right_i)

for stick in range(left_i, right_i + 1):
    lst[stick - 1] = '.'

print('\nРезультат:', ''.join(lst))