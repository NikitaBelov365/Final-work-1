import json
import datetime


class NoteChanging:
    pass


def note_changing(file, decoded_data):
    print("Хотите изменить какую-либо запись?")
    print("Для ДА введите 1")
    print("Для НЕТ введите 2")
    confirmation = input("Введите сюда 1 или 2: ")
    while confirmation not in {'1', '2'}:
        confirmation = input("Введите сюда 1 или 2: ")
    if confirmation == '1':
        with open('database.md', 'w') as my_file:
            while True:
                try:
                    number = int(input("Введите id заметки, которую хотите изменить: "))
                    break
                except ValueError:
                    print("Ошибка! Введите число.")
            for i in decoded_data:
                if i["id"] == number:
                    correct = False
                    header = ""
                    text = ""
                    while not correct:
                        header = input("Озаглавьте заметку: ")
                        text = input("Введите текст заметки: ")
                        print("Ваша заметка: ")
                        print(f"Заголовок: {header}, текст: {text}")
                        print("Всё верно? Если верно - введите 1, если хотите что-то поправить введите 2")
                        confirmation = 0
                        while confirmation not in {'1', '2'}:
                            confirmation = input("Введите сюда 1 или 2: ")
                        if confirmation == '1':
                            correct = True
                    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    i = {
                        "id": number,
                        "Заголовок": header,
                        "Текст": text,
                        "Дата": today
                    }
                json_data = json.dumps(i)
                my_file.write(json_data + "\n")
            print("Заметка добавлена")
    else:
        print("Спасибо за использование приложения :*")
