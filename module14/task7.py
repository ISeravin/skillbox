#Задача 7. Годы
def test_digits(num):
    count = 0
    while True:
        while num > 0:
            digit = num % 10
            count += 1
            num //= 10
        if count == 4:
            break
        else:
            return False

first_year = int(input("Введите первый год: "))
test_digits(first_year)
second_year = int(input("Введите второй год: "))
test_digits(second_year)