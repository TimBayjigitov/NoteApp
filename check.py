import controller as c
import view as v


def InputNumbers_menu(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(inputText))
            if number < 4:
                is_OK = True
            else:
                print('Нужно выбрать существующий пункт')
        except ValueError:
            print("Нужно вести цифру нужного пункта")
    return number

def InputNumbers_menu2(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(inputText))
            if 1 <= number <= 2:
                is_OK = True
        except ValueError:
            print("это не цифра")
    return number

def InputNumbers_menu3(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(inputText))
            if 5 > number > 0:
                is_OK = True
        except ValueError:
            print("Такого действия не существует, выберите существующее действие из меню")
    return number

def InputNumbers_menu4(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(inputText))
            if number <= c.show_list(2):
                is_OK = True
            elif number == c.show_list(2) +1:
                v.menu1()
            else:
                print("номера с такой заметкой не существует")
        except ValueError:
            print("Введите номер заметки")
    return number