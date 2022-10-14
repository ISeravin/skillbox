# Задача 10. Сортировка

def lst_imput():
    list = []
    for i in range(int(input('Количество цифр в списке: '))):
        list.append(int(input(f'Введите {i+1} число: ')))
    return list

# lst = [1, 4, -3, 0, 10]
lst = lst_imput()
print("Изначальный список:", lst)
# print("Отсортированный список:", sorted(lst))
for i in range(len(lst)):
    for current in range(i, len(lst)):
        if lst[i] > lst[current]:
            lst[current], lst[i] = lst[i], lst[current]
            
print("Отсортированный список:", lst)

