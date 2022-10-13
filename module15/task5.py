#Задача 5. КиноКрепкий

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 
        'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
love_films = []
add = int(input("Сколько фильмов хотите добавить? "))
for i in range(add):
    name_film = input("Введите название фильма: ")
    for j in range(len(films)):
        if name_film == films[j]:
            love_films.append(name_film)
            break
    else:
        print(f"Ошибка: фильма {name_film} у нас нет :(")
print("Ваш список любимых фильмов: ", end = '')
print(', '.join(map(str, love_films)))
