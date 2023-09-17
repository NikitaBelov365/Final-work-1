from NoteCreating import note_creating
from NoteReading import note_reading


class MainMenu:
    pass


def main_menu():
    print("Что вы хотите сделать:")
    print("Введите 1 чтобы создать заметку.")
    print("Введите 2 чтобы просмотреть заметки.")
    confirmation = None
    while confirmation not in {'1', '2'}:
        confirmation = input("Введите сюда 1 или 2: ")
    if confirmation == '1':
        note_creating()
    else:
        note_reading()
