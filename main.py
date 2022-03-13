from new_student import new_student as new
from del_student import del_student as delete
from search import seach_and_change
import codecs

#-----------------------------------------------------------------------
config_file = codecs.open('config.txt', 'r', encoding='UTF-8')
config = config_file.read()
#----------------------------------------------------------------------

def info():
    print("""
        Данная программа предназначена для работы в библиотеке
        Она заменяет базу картотеки, что облегчает работу с читателями.
        Она имеет небольшой функционал.
        Создать нового пользователя.
        Удалить пользователя
    """)
    start()
#----------------------------------------------------------------------
print("""
0 краткая информация
1 создать нового читателя
2 удалить пользователя
3 поиск 
x выход из приложения
""")

fun = {
    1:new,
    2:delete,
    3:seach_and_change
}

#----------------------------------------------------------------------

def start():
    num = input("Введите число нужного действия >> ")
    try:
        if num == "x":
            pass
        elif num == "0":
            info()
        else:
            fun[int(num)](config)
    except:
        print("Вы ввели неправильные данные")
        start()



if __name__ == "__main__":
    start()


config_file.close()