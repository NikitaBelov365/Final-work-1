import os


class MarkDownCreating:
    pass


def mark_down_creating(file):
    path = os.path.join(os.getcwd(), file)

    if os.path.exists(path):
        print(f"Добавляем в  {file}.")
    else:
        open(path, 'w').close()
        print(f"База данных {file} успешно создана.")
