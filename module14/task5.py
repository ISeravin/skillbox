#Наименьший делитель

def nok(num):
    res = 1
    while num > res:
        res += 1
        if num % res == 0:
            break
    return res


number = int(input("Введите число: "))

print("Наименьший делитель, отличный от единицы:", nok(number))