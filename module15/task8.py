# Задача 8. Бегущие цифры

shift = int(input("Сдвиг: "))
list1 = [1, 2, 3, 4, 5]
list2 = []

print("Изначальный список:", list1)
list2 = list1[-shift:] + list1[: -shift]
print("Сдвинутый список:", list2)
