#Задача 3. Файлы

spec_symbol = '@№$%^&*().'
extension_file = ['.txt','.docx']
name_file = input("Название файла: ")
while True:
    for symbol in spec_symbol:
        if name_file.startswith(symbol):
            print("Ошибка: название начинается на один из специальных символов.")
            name_file = input("[Error] Введите название файла снова: ")
    if name_file.endswith('.txt') == False and name_file.endswith('.docx') == False:
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
        name_file = input("[Error] Введите название файла снова: ")
    else:
        print("Файл назван верно.")
        break