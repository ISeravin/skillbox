# Задача 9. Сообщение

str_input = input('Сообщение: ')
new = ''
i_start = 0
for i in range(len(str_input)):
    if str_input[i].isalpha() == False:
        new_word = str_input[i_start:i]
        new += new_word[::-1] + str_input[i]
        i_start = i + 1
    elif str_input[i].isalpha() == True and i == len(str_input) - 1:
        new_word = str_input[i_start:i]
        new += new_word[::-1]
print("Новое сообщение:", new)