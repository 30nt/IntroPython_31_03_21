# standart_dict = {'dict': 1, 'dictionary': 2, 3: "asd"}
# short='dict'

# person = {"name": "Michail",
#           "age": 19}
#
# by_type_dict = dict(name="Michail", age=19)

# by_type_dict = dict(short=short, long='dictionary')
# standart_dict["key_1"] = "value_1"
# print(standart_dict)

# list_keys = list("qwerty")
# list_values = list("123456")

# list_keys = ["asd", "zxc", "qwe", "123"]
# list_values = [1,2,3,4,5,6,7,8,9,]
#
# by_zip_dict = dict(zip(list_keys, list_values))
# print(by_zip_dict)

# list_keys = ['a', 'b']
# result = {key: 100 for key in list_keys}
# print(result)

ascii_table = {chr(numb): numb for numb in range(ord("a"), ord("z") + 1)}
# print(ascii_table)
# tmp_val = 100 in ascii_table  # in проверяето ТОЛЬКО КЛЮЧИ!
# print(tmp_val)
#
# for key in ascii_table: # преребор только КЛЮЧИ
#     print(key, ascii_table[key])

# new_dict = ascii_table.copy()
# new_dict["test"] = "test"
# print(new_dict)
# print(ascii_table)

# key = 100
# value = ascii_table.get(key)
# print(value)

# for key, value in ascii_table.items():
#     print(key, value)

dict_1 = {1:11, 2:2, 3:33}
dict_2 = {14:11, 24:22, 3:11}
#
# result = list(set(dict_1.values()).intersection(set(dict_2.values())))
# print(result)

# keys = list(ascii_table.keys())
# print(keys)

# НЕ ИМЕЕТ СМЫСЛА:
# new_dict = {value: key for key, value in dict_2.items()}
# print(new_dict)

# total_dict = dict_1.copy()
# total_dict = {}
# total_dict.update(dict_1)
# total_dict.update(dict_2)
# print(total_dict, dict_1)

# total_dict = {**dict_2, **dict_1}
# print(total_dict, dict_2)

price_list = [{"bread": 10}, {"water": 10}, {"banana": 2000}, {"water": 12}]
min_value_list = []
for price in price_list:
    min_value_list.append(list(price.values())[0])
min_value = min(min_value_list)
for price in price_list:
    if list(price.values())[0] == min_value:
        print(list(price.keys())[0])

value_list = {}
for price in price_list:
    value_list[list(price.values())[0]] = list(price.keys())[0]
min_value = min(value_list)
print(value_list[min(value_list)])