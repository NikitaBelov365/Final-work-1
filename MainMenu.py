from NoteCreating import NoteCreating
class MainMenu:
    @staticmethod
    def mainMenu():
        print("Что вы хотите сделать:")
        print("Введите 1 чтобы создать заметку.")
        print("Введите 2 чтобы просмотреть заметки.")
        confirmation = None
        while confirmation not in {'1', '2'}:
            confirmation = input("Введите сюда 1 или 2: ")
            print(confirmation)
        if confirmation == '1':
            NoteCreating.noteCreating()