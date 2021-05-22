################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string
import random


class AlphabetWorker:
    def __init__(self, dirname):
        self.dirname = dirname
        self.alphabet = string.ascii_lowercase
        self.dirname_list = []
        self.create_dir()

    def create_dir(self):  # метод экземпляра класса
        os.makedirs(self.dirname, exist_ok=True)

    def dirname_info(self):
        self.dirname_list = os.listdir(self.dirname)

    def create_alphabet_files(self):
        for symbol in self.alphabet:
            self.create_file(symbol)

    def create_file(self, symbol):
        filename = os.path.join(self.dirname, f"{symbol}.txt")
        with open(filename, "w") as file:
            file.write(self.alphabet.replace(symbol, symbol.upper()))

    def do_tanos_click(self):
        files = sorted(os.listdir(self.dirname))
        random.shuffle(files)
        files = files[: len(files) // 2]
        for file in files:
            os.remove(os.path.join(self.dirname, file))


alphabet_worker = AlphabetWorker("alphabet")
alphabet_worker.create_alphabet_files()
alphabet_worker.do_tanos_click()
print(alphabet_worker.dirname_list)
alphabet_worker.dirname_info()
print(alphabet_worker.dirname_list)
# dirname = "alphabet"
# create_dir(dirname)
# create_alphabet_files(dirname)
# do_tanos_click(dirname)
