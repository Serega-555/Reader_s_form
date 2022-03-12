import os
import codecs


def copy_file(poisk):
    mas = []
    for line in poisk:
        mas.append(line)
    return mas


def change(poisk, config, id):
    a = copy_file(poisk)

    mas = ("Идентификатор: ", "\nФамилия Имя Отчество: ",
           "\nМесто учебы(Работы): ", "\nДомашний адрес: ",
           "\nНомер телефона: ", "\nПаспорт: ", "\nСеместр и группа: ")

    poisk = codecs.open(config + id + ".txt", "w", encoding="UTF-8")

    for i in range(len(mas)):
        num = input("Переписать " + mas[i] + " на: ")
        if num == "":
            poisk.write(a[i])
        else:
            poisk.write(mas[i] + num)



# def copy_file(config, poisk):
#     new_change = codecs.open(config + 'promej.txt', 'w', encoding="UTF-8")
#     copy = poisk.read(10)
#     while len(copy):
#         new_change.write(copy)
#         copy = poisk.read(10)
#     poisk.close()
#     new_change.close()
#
#
# def change(config, id):
#     mas = ("Идентификатор: ", "\nФамилия Имя Отчество: ",
#            "\nМесто учебы(Работы): ", "\nДомашний адрес: ",
#            "\nНомер телефона: ", "\nПаспорт: ", "\nСеместр и группа: ")
#     new_change = codecs.open(config + 'promej.txt', 'r', encoding="UTF-8")
#     poisk = codecs.open(config + id + ".txt", "w", encoding="UTF-8")
#
#     p = new_change.readline()
#     for i in range(len(mas)):
#         #poisk.write(mas[i] + input("Переписать " + mas[i] + " на: "))


def seach_and_change(config):
    id = input("Введите идентификатор читателя: ")
    poisk = codecs.open(config + id + ".txt", "r", encoding="UTF-8")

    if os.path.isfile(config + id + ".txt") == True:
        print("Такой пользователь существует\n1 открыть\n2 изменить\n3 ничего не делать")
        num = input("Что необходимо сделать: ")
        if num == "1":
            print(poisk.read())
            poisk.close()
        elif num == "2":
            change(poisk, config, id)
    else:
        print("Такого пользователя нет")
        poisk.close()

seach_and_change("E:\Рабочий стол\Project\Reader s form\students\\")