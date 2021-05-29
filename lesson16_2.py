# декораторы

import os
import string
import random


class AlphabetWorker:
    def __init__(self, dirname):
        self.dirname = dirname
        self._alphabet = string.ascii_lowercase
        # self._dirname_list = []
        self._create_dir()

    @property
    def dirname_list(self):
        return sorted(os.listdir(self.dirname))

    def _create_dir(self):  # метод экземпляра класса
        os.makedirs(self.dirname, exist_ok=True)

    def create_alphabet_files(self):
        for symbol in self._alphabet:
            self._create_file(symbol)
        # self._dirname_list = self._dirname_info()  ####### lesson16

    def _create_file(self, symbol):
        filename = os.path.join(self.dirname, f"{symbol}.txt")
        with open(filename, "w") as file:
            file.write(self._alphabet.replace(symbol, symbol.upper()))

    def do_tanos_click(self):
        files = sorted(os.listdir(self.dirname))
        random.shuffle(files)
        files = files[: len(files) // 2]
        for file in files:
            os.remove(os.path.join(self.dirname, file))
        # self._dirname_list = self._dirname_info()


# alphabet_worker = AlphabetWorker("alphabet")
# alphabet_worker.create_alphabet_files()
# alphabet_worker.do_tanos_click()
# print(alphabet_worker.dirname_list)


class Rect:
    def __init__(self, w, h):
        self._w = w
        self._h = h
        self._area = self._get_area()

    def _get_area(self):
        return self._w * self._h

    @staticmethod
    def perimeter(a, b):
        return (a + b) * 2

    @property
    def area(self):
        return self._area

rect_1 = Rect(2,5)
print(rect_1.area)

per_1 = rect_1.perimeter(10,5)
print(rect_1.__class__.__name__)