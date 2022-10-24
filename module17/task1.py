# Задача 1. Гласные буквы.

str_input = input("Введите текст: ")
lst = [symbol for symbol in str_input if symbol in "аоиеёэыуюяАОИЕЁЭЫУЮЯ"]
print("Список гласных букв: ", lst)
print("Длина списка: ", len(lst))
