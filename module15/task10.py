# Задача 10. Сортировка

lst = [1, 4, -3, 0, 10]
print("Изначальный список:", lst)
#print("Отсортированный список:", sorted(lst))

for i in range(len(lst)):
    if lst[i::] > lst[i + 1::]:
        lst[i + 1::] = lst[i::]
print("Отсортированный список:", lst)