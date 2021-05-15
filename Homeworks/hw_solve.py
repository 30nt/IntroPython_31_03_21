my_str = "sssssssssssssssssssssssssssssssssssssssssafygajksfkasdkabsjsjsajg"
# 5
res_5 = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        res_5.append(symbol)
# print(res_5)

# 6
my_str_1 = "asjufygajsfbk"
my_str_2 = "SDHGFbjasgmh"
res_6 = list(set(my_str_1).intersection(set(my_str_2)))
# print(res_6)

# 7
res_7 = []
for symbol in res_6:
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_7.append(symbol)
# print(res_7)

# HW8
persons = [
    {"name": "John", "age": 73},
    {"name": "Stephany11", "age": 12},
    {"name": "Jack", "age": 12},
    {"name": "Jacob", "age": 37},
    {"name": "Stephany12", "age": 12},
]
ages = []
names_len = []
for person in persons:
    ages.append(person["age"])
    names_len.append(len(person["name"]))

min_age = min(ages)
long_name_len = max(names_len)
# а)
# for person in persons:
#     if person["age"] == min_age:
#         print(person["name"])
# res_8_1 = [person["name"] for person in persons if person["age"] == min_age]
# print(res_8_1)
# б)
# print("------------")
# for person in persons:
#     if len(person["name"]) == long_name_len:
#         print(person["name"])
# в)
# print("------------")
# mean_age = sum(ages) / len(ages)
# print(mean_age)

my_dict_1 = {1: 1, 22: 22, 11: 11, 3: 3}
my_dict_2 = {11: 1111, 22: 2222, 111: 111}
# 1)
common_keys = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
print(common_keys)
# 2)
first_keys = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
print(first_keys)
# 3)
first_dict = {key: value for key, value in my_dict_1.items() if key in first_keys}
print(first_dict)
# 4)
res_dict = {**my_dict_1, **my_dict_2}
for key in common_keys:
    res_dict[key] = [my_dict_1[key], my_dict_2[key]]
print(res_dict)