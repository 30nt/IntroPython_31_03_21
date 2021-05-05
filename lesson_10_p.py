################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string
import random


def create_dir(dir_name):
    os.makedirs(dir_name, exist_ok=True)


def create_alphabet_files(dirname):
    alphabet = string.ascii_lowercase
    for symbol in alphabet:
        create_file(dirname, symbol, alphabet)


def create_file(dirname, symbol, alphabet):
    filename = os.path.join(dirname, f"{symbol}.txt")
    with open(filename, "w") as file:
        file.write(alphabet.replace(symbol, symbol.upper()))


def do_tanos_click(dir):
    files = sorted(os.listdir(dir))
    random.shuffle(files)
    files = files[: len(files) // 2]
    for file in files:
        os.remove(os.path.join(dir, file))


dirname = "alphabet"
create_dir(dirname)
create_alphabet_files(dirname)
do_tanos_click(dirname)