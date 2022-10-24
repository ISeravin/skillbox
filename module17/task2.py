# Задача 2. Генерация
n = int(input("Введите длину списка: "))
print("Результат:", [1 if x % 2 == 0 else x % 5 for x in range(n)])