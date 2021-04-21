# генераторы списков
# множества
# словари

# person = {}
# my_empty_set = set()

# person = {"name": "John",
#           "age": 23,
#           "job": ["cop", "doctor"],
#           "address": {"city": "Dnipro",
#                       "street": "Polya"}}
#
# print(person["address"]["city"])
#
# triangle = {
#     "A": {"x": 2, "y":4},
#     "B": (3, 7),
#     "C": (-2, -1)
# }
# print(triangle["A"]["x"])

# key = "NEW"
# value = [1,2,3]
# dummy = {key: value}
# print(dummy)
# dummy["New"] = "Hello"
# print(dummy['new'])










# множества set
# my_list = ["/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Hillel/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Hillel/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/"]

# my_set = set(my_list)
# print(my_set, type(my_set))

# my_path_p = "/home/dn220879zva/PycharmProjects/Pandas@/"
# my_path_h = "/home/dn220879zva/PycharmProjects/Hillel#/"
#
# my_path_p_set = set(my_path_p)
# my_path_h_set = set(my_path_h)

# path_union_set = my_path_p_set.union(my_path_h_set)
# path_union_set_2 = my_path_p_set | my_path_h_set
# print(path_union_set)
# print(path_union_set_2)
# print(path_union_set_3)
# my_path_p_set.update(my_path_h_set)
# print(my_path_p_set)
# path_intersection_set = my_path_p_set.intersection(my_path_h_set)
# path_union_set_2 = my_path_p_set & my_path_h_set
# print(path_intersection_set)
# print(path_union_set_2)

# path_difference_set = my_path_h_set.difference(my_path_p_set)
# print(path_difference_set)



# my_path_set = set(my_path)
# print(len(my_path_set), my_path_set)
# value = my_path_set[-1]
# print(value)

################
# my_list = ['qwe', 'rt', 'rt', 'rt', "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g"]
# for line in set(my_list):
#     count = my_list.count(line)
#     print(line, count)





# генераторы списков
# my_list = ["/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/",
#            "/home/dn220879zva/PycharmProjects/Pandas/"]
# [print(path) for path in my_list]

# my_list = list(range(100))

# my_list = []
# for number in range(15):
#     my_list.append(number ** 2)
# print(my_list)
#
# my_list_gen = [number ** 2 for number in range(15)]
# print(my_list_gen)
# str_list = [str(value) for value in my_list_gen]
# result_number = int(''.join(str_list))
# print(result_number)
#
# alphabet_list = [chr(index) for index in range(ord("a"), ord("z") + 1)]
# print(alphabet_list)

# my_list = ['qwe', 'asdas', '123', 234, 45]
# new_list = [value * 2  + "___" + value for value in my_list if type(value) == str and len(value) > 3]
# print(new_list)


"""
7)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
# my_list_1 = [1, 3, 5, 7, 9]
# my_list_2 = [20, 30, 40, 50, 10]
# my_result = []
#
# range_len = min(len(my_list_1), len(my_list_2))
#
# for index in range(range_len):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
#
# if len(my_list_1) > len(my_list_2):
#     tail_list = my_list_1[range_len:]
# else:
#     tail_list = my_list_2[range_len:]
#
# # tail_list = my_list_1[range_len:] if len(my_list_1) > len(my_list_2) else my_list_2[range_len:]
#
# my_result += tail_list
#
# print(my_result)
