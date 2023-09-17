from MarkDownCreating import mark_down_creating
from NoteAdding import note_adding


class NoteCreating:
    pass


def note_creating():
    file = "database.md"
    mark_down_creating(file)
    print("Давайте создадим заметку")
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
    note_adding(file, header, text)
