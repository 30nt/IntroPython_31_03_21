# циклы

my_list = ['q', 'aaaa', "3", "Fox", '123', '.']

for value in my_list:
    if not value.isdigit():
        print(value)

my_string_1 = "12"
my_string_2 = "34"
for symb_1 in my_string_1:
    for symb_2 in my_string_2:
        print(symb_1 + symb_2)


# типы данных: кортеж, список

my_t = (1, 2, 3, 3.14, "qwe", "tuple")  # итерируемый неизменяемый объект
my_l = [1, 2, 3, 3.14, "qwe", "list"]  # итерируемый изменяемый объект

print(my_t, type(my_t))
print(my_l, type(my_l))

new_t = tuple(my_l)
new_l = list(my_t)

print(new_t, type(new_t))
print(new_l, type(new_l))

print(my_t[2:5:2], my_l[2:5:2])

index = 3
value_l = my_l[index]
print(value_l)

print(my_l)
my_l[0] = "test"
print(my_l)

# print(my_t)
# my_t[0] = "test"
# print(my_t)

my_list_tuple = ([1,2], my_l)
my_list_tuple[0][1] = "test"
print(my_list_tuple)

new_list = [[1], [2], "test"] * 3
print(new_list)

test_list = [1,2,3]
print(id(test_list))
new_list = [test_list.copy()] * 3
print(new_list, id(new_list[-1]))
test_list[-1] = "test"
print(test_list)
print(new_list)

my_list = []
my_list.append("a")
my_list.append("v")
my_list.pop()
print(my_list)

test_list = list("qwerty")
test_list[1] = "W"
print(test_list)
new_str = ''.join(test_list)
print(new_str)



# строки и методы срок
my_str = "123djfyawyest"
my_str = my_str + my_str[::-1]
print(my_str)

value = input("xhhz")
print(value * 2)



len_str = len("qwerty")
print(len_str)

print_str = print("qwerty")
print(print_str)

my_str = "D'Artanian ttTtt"
new_str = 'ООО "Рога и копыта"'
full_str= '''D'Artanian and ООО "Рога и копыта"'''

print(my_str.rfind('n'))

my_str = my_str.replace("ttttt", "asd")
print(my_str)

value = input()
if value.isdigit():
    res = int(value)
    print(res * 3)

my_str = my_str.upper().count("T")
print(my_str)