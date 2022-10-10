#Задача 3. Сумма и разность
def sum_all_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

number = int(input("Введите число: "))
print("Сумма чисел:", sum_all_digits(number))
print("Количество цифр в числе:", count_digits(number))
print("Разность суммы и количества цифр:", sum_all_digits(number) - count_digits(number))