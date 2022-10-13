#Задача 9. Анализ слова 2

str = input("Введите слово: ")
lst_intro_end = str[::-1]
if str == lst_intro_end:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
 