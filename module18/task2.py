#Задача 2. Самое длинное слово
str_input = input("Введите строку: ").split()
max_str = 0
for i in range(len(str_input)):
    if len(str_input[i]) > max_str:
        res = str_input[i]
        max_str = len(str_input[i])

print("Введите строку:", res)
print("Длина этого слова:", len(res))