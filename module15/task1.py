# Задача 1. Генерация списка
lst = []
number = int(input("Введите число: "))
for i in range(number + 1):
    if i % 2 == 1:
        lst.append(i)
print("Список из нечётных чисел от одного до N:", lst)