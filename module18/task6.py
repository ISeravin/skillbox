#Задача 6. Сжатие
def encode(text):
    k, lst = 1, []
    for symbol in range(len(text)):
        if text[symbol] == text[symbol + 1: symbol + 2]:
            k += 1
            continue
        lst.append(text[symbol] + str(k))
        k = 1
    return lst

str_input = input("Введите строку: ")
print("Закодированная строка:", ''.join(encode(str_input)))
