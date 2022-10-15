#Задача 4. Вечеринка
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: ", guests)
    answer = input("Гость пришёл или ушёл? ")
    #буквы 'е' и 'ё'
    if answer == 'пришёл' or answer == 'пришел':
        name = input("Имя гостя: ")
        if len(guests) < 6:
            print(f"Привет, {name}!")
            guests.append(name)
        else:
            print(f"Прости, {name}, но мест нет.")      
        print()
    elif answer == 'ушёл' or answer == 'ушел':
        name = input("Имя гостя: ")
        print(f"Пока, {name}!")
        guests.remove(name)
        print()
    elif answer == 'Пора спать':
        print("\nВечеринка закончилась, все легли спать.")
        break
    else:
        print("Пришел кто-то или ушел? Или вообще, пора спать?")
        print()
        
