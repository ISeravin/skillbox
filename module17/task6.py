#Задача 6. Сжатие списка

import random
n = int(input("Количество чисел в списке: "))
lst = [random.randint(0, 2) for _ in range(n)]
print("Список до сжатия:", lst)

# for _ in range(lst.count(0)):
#     lst.remove(0)
#     lst.extend([0])
# for _ in range(lst.count(0)):
#     lst.remove(0)

print("Список после сжатия:", [x for x in lst if x])