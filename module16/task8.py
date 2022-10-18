#Задача 8. Считалка

lst = []
n_people = int(input("Кол-во человек: "))
n_del = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {n_del}-й человек")
print()
for i in range(1, n_people + 1):
    lst.append(i)
begin = 0
for i in range(n_people - 1):
    print("Текущий круг людей:", lst)
    print("Начало счёта с номера", lst[begin])
    if begin != 0 or i == 0:
        i_del = n_del % ((n_people - i) - (begin - 1))
    else:
        i_del = begin % ((n_people - i))
    print("Выбывает человек под номером", lst[i_del])
    lst.remove(lst[i_del])
    begin = i_del % (n_people - i - 1)
    print()
print("Остался человек под номером", lst[i_del])
