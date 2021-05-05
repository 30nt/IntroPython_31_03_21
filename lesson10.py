# работа с файлами txt, json
import os
from os import path
import json

def list_writer(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def list_reader(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data

filename = "test.json"
data = [1,2,{3: 3.14},4,(5, 6)]
print(data[-1])
list_writer(filename, data)
data_new = list_reader(filename)
print(type(data_new))

# with open("lesson2.py", "r") as txt_file:
#     # data = txt_file.read()  # все одна строка
#         data = txt_file.readlines()  # построчно
#
# print(data)
# data.append("# test \n#TEST\n")

# data = ["sudygf", "usagfygf", "asujfygau"]
#
# with open("lesson2_test.py", "w") as txt_file:
#     txt_file.write("\n".join(data))


# source_dir = "Homeworks"
# files = os.listdir(source_dir)  # listdir не алфавитный порядок
# files = sorted(files)
# print(files)
# total_files = []
# for filename in files:
#     path_filename = path.join(source_dir, filename)
#     if path.isfile(path_filename):
#         total_files.append(filename)
# print(total_files)

# current_dir = os.getcwd()
# print(current_dir)

# new_dir = os.path.join(source_dir, "tmp")
# print(new_dir)
# files = os.listdir(new_dir)
# print(files)

# try:
#     os.mkdir("tmp_3/tmp_2/tmp_1")
# except FileExistsError:
#     pass

# os.makedirs("tmp_3/tmp_2/tmp_1", exist_ok=True)
