import check as c
import controller as con


def StartMenu():
    print('Добро пожаловать')
    print('Меню программы')
    print('======================================================================================')
    return menu1()


def menu1():
    print("1. Создать новую заметку!")
    print("2. Просмотреть список заметок!")
    print("3. Выйти из программы!")
    value = c.InputNumbers_menu("Введите номер нужного пункта: ")
    match value:
        case 1:
            con.create_note()
        case 2:
            menu2()
        case 3:
            exit_from_app()


def menu2():
    num_exit = con.show_list(2) + 1
    print(con.show_list(1))
    print(f'{num_exit}. Вернуться в главное меню')
    num_note = c.InputNumbers_menu4('Выберите нужную заметку: ')
    if num_note == num_exit:
        menu1()
    else:
        menu3(num_note-1)


def menu3(note):

    print('1. Редактировать заметку')
    print('2. Удалить заметку')
    print('3. Просмотреть заметку')
    print('4. Вернуться в предыдущее меню')
    answer = c.InputNumbers_menu3('Какое действие будем производить?: ')
    match answer:
        case 1:
            con.edit_note(note)
        case 2:
            con.delete_note(note)
        case 3:
            print(con.load_note(note))
            menu2()
        case 4:
            menu2()


def exit_from_app():
    print('Для завершения работы программы нажмите -----> любой символ, для продолжения -----> enter')
    status = input()
    if status == '':
        menu1()
    else:
        quit('Всего доброго!')
