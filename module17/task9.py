#Задача 9. Список списков

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# lst = []
# for i in range(len(nice_list)):
#     for j in range(len(nice_list[i])):
#         for k in range(len(nice_list[i][j])):
#             lst.append(nice_list[i][j][k])
# print(lst)
print("Ответ:", [k for i in nice_list for j in i for k in j])