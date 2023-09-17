import datetime
import json


class NoteAdding:
    pass


def noteAdding(fileName, header, text):
    with open(fileName, 'a+') as file:
        file.seek(0)
        lines = file.readlines()
        count = len(lines)
        if count == 0:
            noteNumber = 1
        else:
            noteNumber = count + 1
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        outputData = {
            "id": noteNumber,
            "Заголовок": header,
            "Текст": text,
            "Дата": today
        }
        json_data = json.dumps(outputData)
        file.write(json_data + "\n")
        print("Заметка добавлена")
