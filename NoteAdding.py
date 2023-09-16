import datetime
import json
import os

class NoteAdding:
    @staticmethod
    def noteAdding(fileName, header, text):

        with open(fileName, 'a+') as file:
            file.seek(0)
            lines = file.readlines()
            count = len(lines)
            if count == 0:
                id = 1
            else:
                id = count+1
                print(len(file.readlines()))
            today = datetime.date.today().strftime("%Y-%m-%d")
            outputData = {
                "id": id,
                "Заголовок": header,
                "Текст": text,
                "Дата": today
            }
            print(outputData)
            json_data = json.dumps(outputData)
            file.write(json_data + "\n")
            print("Добавлено похоже")
