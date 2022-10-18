#Задача 10. Симметричная последовательность
n, lst, rev_lst = int(input("Кол-во чисел: ")), [], []
for i in range(n):
    number = int(input("Число: "))
    lst.append(number)
print()
print("Последовательность:", lst)
for i in range(len(lst) - 1, -1, -1):
    rev_lst.append(lst[i])


while True:
    if lst[len(lst) - 1] == rev_lst[0]:
        rev_lst.remove(rev_lst[0])
    else:
        break
print("Нужно приписать чисел:", len(rev_lst))
print("Сами числа:", rev_lst)