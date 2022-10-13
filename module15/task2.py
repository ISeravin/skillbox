# Задача 2. Турнир.

list_all = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
list = []
for i in range(len(list_all)):
    if i % 2 == 0:
        list.append(list_all[i])
print("Первый день:", list)