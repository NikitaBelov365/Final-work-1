from NoteCreating import noteCreating
from NoteReading import noteReading


class MainMenu:
    pass


def mainMenu():
    print("Что вы хотите сделать:")
    print("Введите 1 чтобы создать заметку.")
    print("Введите 2 чтобы просмотреть заметки.")
    confirmation = None
    while confirmation not in {'1', '2'}:
        confirmation = input("Введите сюда 1 или 2: ")
    if confirmation == '1':
        noteCreating()
    else:
        noteReading()
