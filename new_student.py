# file_path = "path/to/file.txt"
# Для проверки существования заданного пути используйте функцию os.path.exists:
#
# import os.path
# os.path.exists(file_path)
# Но она вернет True и для файла и для директории.
#
# os.path.isfile проверит именно на наличие файла.

import codecs
import os

def new_student(config):


    id = input("Персональный номер: ")

    if os.path.isfile(config + id + '.txt') == True:  # Проверяет есть ли файл с похожим id
        print("Пользователь с таким именем уже существует")
    else:
        if input("Создать нового пользователя\nс таким идентификатором?(y/n)" ) == "y":
            new = codecs.open(config + id + '.txt', 'w', encoding="UTF-8")
            new.write("Идентификатор: " + id)
            new.write("\nФамилия Имя Отчество: " + input("ФИО: "))
            new.write("\nМесто учебы(Работы): " + input("Место учебы(работы): "))
            new.write("\nДомашний адрес: " + input("Домашний адрес: "))
            new.write("\nНомер телефона: " + input("Телефон: "))
            new.write("\nПаспорт: " + input("Паспорт: "))
            new.write("\nСеместр и группа: " + input("Группа и семестр\n(для других читателей поставьте -): "))
            print("Пользователь создан")
            new.close()



