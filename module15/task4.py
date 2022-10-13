#Задача 4. Видеокарты

number = int(input("Количество видеокарт: "))
lst = []
lst_intro_max = []
for i in range(1, number + 1):
    print(f"{i} Видеокарта: ", end = '')
    model = int(input())
    lst.append(model)
print("Старый список видеокарт:", lst)
for i in range(len(lst)):
    if lst[i] != max(lst):
        lst_intro_max.append(lst[i])
print("Новый список видеокарт:", lst_intro_max)