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

def three_identical_digits(num1, num2):
    count = 0
    for num in range(num1, num2 + 1):
        num_dig = num
        num_pred = num_dig % 10
        num_dig //= 10
        while num_dig > 0:
            digit = num_dig % 10
            if digit == num_pred:
                count += 1      
            num_dig //= 10
        
        if count == 2:
            print(num)
        num_pred = 0
        count = 0


first_year = int(input("Введите первый год: "))
while test_digits(first_year) == False:
    first_year = int(input("[Error] Введите четырехзначное число: "))
second_year = int(input("Введите второй год: "))
while test_digits(second_year) == False:
    second_year = int(input("[Error] Введите четырехзначное число: "))
print(f"Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:")
three_identical_digits(first_year, second_year)
