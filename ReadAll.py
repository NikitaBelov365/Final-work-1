import json

import NoteChanging


class ReadAll:
    pass


def read_all():
    files = "database.md"
    try:
        with open(files, 'r+') as file:
            decoded_data = []
            for line in file:
                try:
                    decoded_line = json.loads(line)
                    decoded_data.append(decoded_line)
                except json.JSONDecodeError as e:
                    print(f"Ошибка декодирования JSON в строке: {line.strip()}")
                    print("Ошибка:", e)
            for i in decoded_data:
                print(i)
        NoteChanging.note_changing(file, decoded_data)
    except FileNotFoundError:
        print(f"База данных '{file}' не найдена")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file}':", e)
