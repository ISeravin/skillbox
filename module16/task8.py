#Задача 8. Считалка

lst = []
n_people = int(input("Кол-во человек: "))
n_del = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {n_del}-й человек")
print()
for i in range(1, n_people + 1):
    lst.append(i)


i_del = 0
while len(lst) > 1:
    print("Текущий круг людей:", lst)
    begin = i_del % len(lst)
    print("Начало счёта с номера", lst[begin])
    i_del = (begin + n_del - 1) % len(lst)
    print("Выбывает человек под номером", lst[i_del])
    lst.remove(lst[i_del])
    print()
print("Остался человек под номером", lst[0])