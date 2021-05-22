import re
# функции сортировки, регулярные выражения

# my_list = [-2,5,-12,67,12]
# my_list = ["qwe", "QW", "1", "!@#", "ASDfgh", "AZXC"]

# my_list.sort(reverse=True)
# new_list = sorted(my_list, key=len)

# print(my_list)
# print(new_list)
#########################################################################
def sort_by_age(pers_dict):
    age = pers_dict["age"]
    return age


def sort_by_name(pers_dict):
    return pers_dict["name"]


def sort_by_name_len(pers_dict):
    name_len = len(pers_dict["name"])
    return name_len


def sort_by_name_len_and_alphabet(pers_dict):
    name = pers_dict["name"]
    return len(name), name

persons = [
    {"name": "John", "age": 72},
    {"name": "Stephany", "age": 12},
    {"name": "Jack", "age": 42},
    {"name": "Jacob", "age": 37},
    {"name": "Annsy", "age": 29},
]

new_persons = sorted(persons, key=lambda x: x["name"])
print(new_persons)
new_persons = sorted(persons, key=sort_by_name_len)
print(new_persons)
####################################################################
# def sort_by_bday(pers_dict):
#     age = pers_dict["age"]
#     ages = re.findall(r'[0-9]+', age)
#     if len(ages) > 1:
#         return int(ages[1])
#     else:
#         return 1000000
#
# persons = [
#     {"name": "John", "age": "Годы жизни: 1823 - 1887"},
#     {"name": "Jack", "age": " 1878 -- 1905 "},
#     {"name": "Stephany", "age": "345 BC - 234"},
# ]
#
# new_persons = sorted(persons, key=sort_by_bday)
# print(new_persons)
