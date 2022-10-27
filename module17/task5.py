#Задача 5. Разворот
str_input = input("Введите строку: ")
str_input = str_input[str_input.find('h') + 1:str_input.rfind('h')]
print("Развёрнутая последовательность между первым и последним h: ", end = '')
print(str_input[::-1])
