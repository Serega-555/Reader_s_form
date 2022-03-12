# import os
#
#
# def del_student(config):
#     id = input("Введите номер читателя для удаления: ")
#
#     if os.path.isfile(config + id + '.txt') == True: #Проверяет есть ли файл с похожим id
#         if input("Точно удалить данного пользователя?(y/n)") == "y":
#             os.remove(config + id + ".txt")
#             print("Пользователь удален")
#     else:
#         print("Такого пользователя нет в системе")


name = "индустриализация"
print(name[0:8] + name[-1])