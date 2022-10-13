#Задача 6. Анализ слова
str = input("Введите слово: ")
str_list = list(str)

# for symbol in str:
#     str_list.append(symbol)

# for i in range(len(str_list)):
#     print(str_list[i], end = '')

count = 0
for i in str_list:
    same = 0
    for j in str_list:
        if j == i:
            same += 1
            if same == 2:
                count += 1
                break
print("Количество уникальных букв:", len(str_list) - count)
            
    
# word = input('Введите слово: ')
# letters = list(word)
# total = 0
# for i in letters:
# same_letters = 0
# for j in letters:
# if j == i:
# same_letters += 1
# if same_letters > 2:
# continue
# elif same_letters == 2:
# total += 1
# break
    