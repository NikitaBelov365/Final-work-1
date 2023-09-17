from NoteOnDate import note_on_date
from ReadAll import read_all


class NoteReading:
    pass


def note_reading():
    print("Немного выбора: \n"
          "Вы хотите прочитать все заметки? Введите 1\n"
          "Вы хотите прочитать заметки от определённой даты? Введите 2")
    confirmation = None
    while confirmation not in {'1', '2'}:
        confirmation = input("Введите сюда 1 или 2: ")
    if confirmation == '1':
        read_all()
    else:
        note_on_date()
