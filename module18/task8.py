#Задача 8. Бегущая строка
def max_ord_str(str_inp):
    res = 0
    for symbol in str_inp:
        if ord(symbol) > res:
            res = ord(symbol)
    return res


def text_with_sdvig(str_input, sdvig):
    lst = []
    n = len(str_input)
    max_ord = max_ord_str(str_input)
    for sumbol in str_input:
        if sdvig + ord(sumbol) > max_ord:
            el = (sdvig + ord(sumbol)) % max_ord
            el += (max_ord - n)
        else:
            el = sdvig + ord(sumbol)
        lst.append(chr(el))
    return ''.join(lst)


str_input_1 = input("Первая строка: ")
str_input_2 = input("Вторая строка: ")


for i in range(1, len(str_input_1) + 1):
    if text_with_sdvig(str_input_1, i) == str_input_2:
        print(f"Первая строка получается из второй со сдвигом {i}")
        break
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")