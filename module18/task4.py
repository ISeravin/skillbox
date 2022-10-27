#Задача 4. Заглавные буквы
str_input = input("Введите строку: ").split()
for i in range(len(str_input)):
    for symbol in str_input[i]:
        sumbol = symbol.upper()
        break
print(str_input)
