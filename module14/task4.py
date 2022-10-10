#Задача 4. Число наоборот 3


def integer_and_fractional(num):
    rev_int_number = reversed(round(num))
    rev_fractional_number = reversed(100 * round((num % 1), 2))
    return rev_int_number + (rev_fractional_number / 100)


def reversed(num):
    flag = True
    res = 0
    while num > 0:
        digit = num % 10
        num //= 10
        #убираем ведущие нули
        while flag == True:
            if digit == 0:
                break
            else:
                flag = False
        if flag == False:
            res = (10 * res) + digit
    return res

n_input, k_input = float(input("Введите первое число: ")), float(input("Введите второе число: "))

print("Первое число наоборот:", integer_and_fractional(n_input))
print("Второе число наоборот:", integer_and_fractional(k_input))

print("Сумма:", integer_and_fractional(n_input) + integer_and_fractional(k_input))




