#Задача 7. IP-адрес 2

while True:
    ip_input = input("Введите IP: ")
    if ip_input.count('.') != 3:
        print("Адрес — это четыре числа, разделённые точками.")
    else:
        k1, k2 = 0, 0
        
        for i in ip_input.split('.'):
            if i.isdigit() == True:
                k1 += 1
                if int(i) > 255:
                    k2 += 1
                    print(f"{i} превышает 255.")
            else:
                print(f"{i} — это не целое число.")
        if k1 == 4 and k2 == 0:
            print("IP-адрес корректен.")
            break

