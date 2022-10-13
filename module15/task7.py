#Задача 7. Контейнеры

from __future__ import barry_as_FLUFL


containers_list = []
number = int(input("Количество контейнеров: "))
weight_pred = 200
for _ in range(number):
    weight = int(input("Введите вес контейнера: "))
    while True:
        if weight >= 200:
            weight = int(input("[Error] Все веса не превышают 200. Введите снова: "))
        elif weight > weight_pred:
            weight = int(input("[Error] Контейнеры лежат в ряд в порядке невозрастания. Введите снова: "))
        else:
            break
    weight_pred = weight
    containers_list.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))
while True:
    if weight >= 200:
        weight = int(input("[Error] Все веса не превышают 200. Введите снова: "))
    else:
        break

for i in range(len(containers_list)):
    if new_weight > containers_list[i]:
        print("Номер, который получит новый контейнер:", i + 1)
        break

