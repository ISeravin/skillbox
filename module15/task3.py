#Задача 3. Клетки
lst = []
number = int(input("Количество клеток: "))
for i in range(1, number + 1):
    print(f"Эффективность {i} клетки: ", end = '')
    rang = int(input())
    lst.append(rang)

print("Неподходящие значения: ", end = '')
for i in range(len(lst)):
    if lst[i] < i:
        print(lst[i], end = ' ')