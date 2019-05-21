# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

if __name__ == '__main__':

    for i in range(1, 10):
        os.mkdir("dir_" + str(i))

    for i in range(1, 10):
        os.rmdir("dir_" + str(i))

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    dir_list = os.listdir(os.getcwd())
    for i in dir_list:
        if os.path.isdir(i):
            print(i)

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    filename = os.path.realpath(__file__).split("/")[-1]
    os.system(f"cp {filename} copy_{filename}")

# функции для normal:


def view_content_of_the_folder():
    lst = []
    for x in os.listdir('.'):
        if os.path.isdir(x):
            lst.append(x)
    print(lst)


def change_dir():
    dir_name = input("Введите название папки в которую хотите перейти: ")
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_name)
    os.chdir(dir_path)
    print(f"Вы перешли в {dir_name}")


def new_dir():
    dir_name = input("Введите имя папки: ")
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_name)
    os.mkdir(dir_path)
    print(f"Папка {dir_name} создана")


def del_dir():
    dir_name = input("Введите имя папки: ")
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_name)
    os.rmdir(dir_path)
    print(f"Папка {dir_name} создана")
