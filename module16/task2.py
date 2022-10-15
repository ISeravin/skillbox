#Задача 2. Шеренга

lst1, lst2 = [], []
print("Отсортированный список учеников: ", end = '')
for two in range(160, 176, 2):
    lst1.append(two)
for three in range(162, 180, 3):
    lst1.append(three)
lst1.extend(lst2)
print(sorted(lst1))