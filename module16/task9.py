#Задача 9. Друзья
n_friends = int(input("Кол-во друзей: "))
n_debts = int(input("Долговых расписок: "))
lst = []
for i in range(n_friends):
    lst.append(0)
print()
for i in range(1, n_debts + 1):
    print(f"{i}-я расписка")
    to_whom = int(input("Кому: "))
    from_whom = int(input("От кого: "))
    money = int(input("Сколько: "))
    for i_f in range(1, n_friends + 1):
        if from_whom == i_f:
            lst[i_f - 1] += money
        elif to_whom == i_f:
            lst[i_f - 1] -= money
    print()

print("Баланс друзей:")
for i_f in range(1, n_friends + 1):
    print(f"{i_f}:", lst[i_f - 1])
