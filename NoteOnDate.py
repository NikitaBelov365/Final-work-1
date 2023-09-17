import json

from NoteChanging import note_changing


class NoteOnDate:
    pass


def note_on_date():
    date = input("Введите дату в формате гггг-мм-дд: ").strip()
    file = "database.md"
    try:
        with open(file, 'r+') as file:
            decoded_data = []
            for line in file:
                try:
                    decoded_line = json.loads(line)
                    decoded_data.append(decoded_line)
                except json.JSONDecodeError as e:
                    print(f"Ошибка декодирования JSON в строке: {line.strip()}")
                    print("Ошибка:", e)
            counter = 0
            for i in decoded_data:
                if i["Дата"][:10] == date:
                    print(i)
                    counter += 1
            if counter == 0:
                print("Нет заметок на эту дату")
        note_changing(file, decoded_data)
    except FileNotFoundError:
        print(f"База данных '{file}' не найдена")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file}':", e)
