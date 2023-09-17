from MarkDownCreating import markDownCreating
from NoteAdding import noteAdding


class NoteCreating:
    pass


def noteCreating():
    file = "database.md"
    markDownCreating(file)
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
    noteAdding(file, header, text)
