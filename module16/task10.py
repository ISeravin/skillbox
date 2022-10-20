#Задача 10. Симметричная последовательность

def is_palindrome(num_lst):
    rev_lst = []
    for i_num in range(len(num_lst) - 1, -1, -1):
        rev_lst.append(num_lst[i_num])
    if num_lst == rev_lst:
        return True
    else:
        return False


n, lst, new_nums, answer = int(input("Кол-во чисел: ")), [], [], []
for i in range(n):
    number = int(input("Число: "))
    lst.append(number)
print()
print("Последовательность:", lst)

for i_nums in range(0, len(lst)):
    for j_elem in range(i_nums, len(lst)):
        new_nums.append(lst[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(lst[i_answer])
        answer.reverse()
        break
    new_nums = []

print("Нужно приписать чисел:", len(answer))
print("Сами числа:", answer)