#Задача 10. Шифр Цезаря

str_input = input("Введите сообщение: ")
sdvig = int(input("Введите сдвиг: "))
lst = []
print("Зашифрованное сообщение: ", end = '')

# ord('а') = 1072
# ord('я') = 1103
for sumbol in str_input:
    if 1072 <= ord(sumbol) <= 1103:
        if sdvig + ord(sumbol) > 1103:
            el = (sdvig + ord(sumbol)) % 1103
            el += 1071
        else:
            el = sdvig + ord(sumbol)
        print(chr(el), end = '')
    else:
        print(sumbol, end = '')