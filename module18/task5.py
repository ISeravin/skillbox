#Задача 5. Пароль

password_input, n, k = input("Придумайте пароль: "), 0, 0

while True:
    for symbol in password_input:
        if symbol.isdigit() == True:
            n += 1
        elif symbol.istitle() == True:
            k += 1
    if n > 2 and k > 0:
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
        password_input = input("Придумайте пароль: ")
