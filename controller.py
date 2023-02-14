import json
from datetime import datetime
import os.path
import view as v

path = 'Notes/'


def show_list(a):
    load_numerate = list((enumerate(os.listdir(path), start=1)))
    file_numbers = int(len([f for f in os.listdir(path)
                           if os.path.isfile(os.path.join(path, f))]))
    list_of_notes = os.listdir(path)
    if a == 1:
        return load_numerate
    if a == 2:
        return file_numbers
    if a == 3:
        return list_of_notes

def create_note():
    title = input('Введите заголовок: ')
    text = input('Введите текст заметки: ')
    date = datetime.now()
    id_number = 1 + show_list(2)
    to_json = {'ID': id_number, 'title': title, 'Text': text, 'Date': date.strftime('%Y-%m-%d %H:%M')}

    with open(path + title + '.json', 'w', encoding="utf8") as f:
        f.write(json.dumps(to_json, ensure_ascii=False))
    print("Ваша заметка сохранена")
    return v.menu1()


def load_note(note):
    with open(path + show_list(3)[note], 'r', encoding="utf8") as f:
        file = json.load(f)
    print(f'Заголовок - {file["title"]}\nТекст заметки - {file["Text"]}')
    return v.menu2()


def edit_note(note):
    new_text = input('Введите изменения в заметке: ')
    with open(path + show_list(3)[note], 'r+', encoding="utf-8") as f:
        file = json.load(f)
        file['Text'] = new_text
        file['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(f'Заголовок - {file["title"]}\nТекст заметки - {file["Text"]}')

    with open(path + show_list(3)[note], 'w', encoding="utf-8") as outputfile:
        outputfile.write(json.dumps(file, ensure_ascii=False))
    print("файл изменен")
    return v.menu1()


def delete_note(note):
    path1 = path + show_list(3)[note]
    os.remove(path1)
    print('Заметка удалена')
    return v.menu1()

files = filter(os.path.isfile, os.listdir(path))
files = [os.path.join(path, f) for f in files]
files.sort(key=lambda x: os.path.getmtime(x))
