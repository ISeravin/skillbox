#Задача 3. Случайные соревнования
import random
lst1 = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
lst2 = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
print("Первая команда:", lst1)
print("Вторая команда:", lst2)
print("Победители тура:", [lst1[x] if lst1[x] > lst2[x] else lst2[x] for x in range(20)])