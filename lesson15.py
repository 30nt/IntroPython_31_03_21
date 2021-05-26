import os
import string
import random


class AlphabetWorker:
    def __init__(self, dirname):
        self.dirname = dirname
        self._alphabet = string.ascii_lowercase
        self.dirname_list = []
        self._create_dir()

    def _create_dir(self):  # метод экземпляра класса
        os.makedirs(self.dirname, exist_ok=True)

    def _dirname_info(self):
        return sorted(os.listdir(self.dirname))

    def create_alphabet_files(self):
        for symbol in self._alphabet:
            self._create_file(symbol)
        self.dirname_list = self._dirname_info()  ####### lesson16

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
        self.dirname_list = self._dirname_info()


alphabet_worker = AlphabetWorker("alphabet")
# alphabet_worker.__alphabet = "tmp"
# print(alphabet_worker.__alphabet)
# print(dir(alphabet_worker))


# alphabet_worker.create_alphabet_files()
# print(alphabet_worker.dirname_list)
# alphabet_worker.do_tanos_click()
# print(alphabet_worker.dirname_list)
# alphabet_worker.do_tanos_click()
# print(alphabet_worker.dirname_list)
# alphabet_worker.do_tanos_click()
# print(alphabet_worker.dirname_list)



# state_1 = alphabet_worker.dirname_info()
# print(state_1)
# alphabet_worker.do_tanos_click()
# state_2 = alphabet_worker.dirname_info()
# print(state_2)
# alphabet_worker.do_tanos_click()
# state_3 = alphabet_worker.dirname_info()
# print(state_3)

