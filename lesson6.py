#for range enumerate
# break continue
# my_list = ['qw', 'sd', 'rty', 'tyu', 'zxc']
# result = []
# for value in my_list:
#     new_value = value.upper()
#     result.append(new_value)
# print(result)

# for index in range(len(my_list)):
#     value = my_list[index]
#     if len(value) == 2:
#         continue
#     value = value.upper()
#     result.append(value)
# print(result)

# for index in range(len(my_list)):
#     value = my_list[index]
#     if not index % 2:
#         new_value = value.upper()
#     else:
#         new_value = value
#     result.append(new_value)
# print(result)
#
# for index in range(len(my_list)):
#     value = my_list[index]
#     if not index % 2:
#         value = value.upper()
#     result.append(value)
# print(result)

# for index, value in enumerate(my_list):
#     if not index % 2:
#         value = value.upper()
#     result.append(value)
# print(result)




# Дана строка My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!
# Составить строку из больших букв этого предложения
# Составить строку из маленьких букв этого предложения
# Составить строку из больших гласных букв этого предложения
# Составить строку из маленьких согласных букв этого предложения
# Составить строку из букв этого предложения, заменив большие буквы на маленькие и наоборот
# Составить строку из символов этого предложения по следующему правилу:
# Большие буквы в алфавитном порядке. Затем маленькие гласные буквы в алфавитном порядке.
# Потом маленькие согласные буквы в алфавитном порядке.
# Затем другие символы в порядке, в котором они есть в предложении.

some_string = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# result = []
# for symbol in some_string:
#     if symbol.isupper():
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# for symbol in some_string:
#     if symbol.islower():
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# for symbol in some_string:
#     if symbol.isupper() and symbol.lower() in "eyuioa":
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# for symbol in some_string:
#     if symbol.islower() and symbol.lower() not in "eyuioa":
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# for symbol in some_string:
#     if symbol.islower():
#         symbol = symbol.upper()
#     elif symbol.isupper():
#         symbol = symbol.lower()
#     result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# big_letter = []
# small_a = []
# small_b = []
# symbols = []
# for symbol in some_string:
#     if symbol.isupper():
#         big_letter.append(symbol)
#     elif symbol in "eyuioa":
#         small_a.append(symbol)
#     elif symbol.isalpha():
#         small_b.append(symbol)
#     else:
#         symbols.append(symbol)
# result = sorted(big_letter) + sorted(small_a) + sorted(small_b) + symbols
# result_str = "".join(result)
# print(result_str)


# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

# my_list = [2763, 85, 9, 341, 12]
#
# my_results = []
#
# for value in my_list:
#     if value > 100:
#         my_results.append(value)
# print(my_results)


# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

# my_list = [2763, 85, 9, 341, 12]
# print(id(my_list))
# if len(my_list) < 2:
#     my_list.append(0)
# else:
#     last_value = my_list[-1] + my_list[-2]
#     my_list.append(last_value)
# print(id(my_list))

# my_list = my_list + [0] if len(my_list) < 2 else my_list + [my_list[-1] + my_list[-2]]
# print(id(my_list))

# 4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))

# my_string = '0123456789'
# result = []
# for symb_1 in my_string:
#     for symb_2 in my_string:
#         result.append(int(symb_1 + symb_2))
# print(result)
#
# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# zero_count = str(number).count("0")
# print(zero_count, type(number))

def count_zero(number):
    zero_count = str(number).count("0")
    return zero_count

number = 8734687003485349000
zero_count = count_zero(number)
print(zero_count, type(number))

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# zero_count = len(str(number)) - len(str(int(str(number)[::-1])))
# zero_count = len(str(number)) - len(str(number).rstrip("0"))
# print(zero_count)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
#
# my_list_1 = [8,6, 7,3,2]
# my_list_2 = [1,2, 6,3,-2]
# my_result = my_list_1[::2] + my_list_2[1::2]
# my_result = []
# my_result.extend(my_list_1[::2])
# my_result.extend(my_list_2[1::2])


# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
# my_list = [1,2,3,4]
# new_list = my_list[1:] + my_list[:1]
# print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list.append(my_list.pop(0))
# print(my_list)
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

# example = "43 больше чем 34 но     меньше чем 56"
# parts = example.split()
# result = []
# for value in parts:
#     if value.isdigit():
#         result.append(int(value))
# res = sum(result)
# print(res)


# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"

l_index = my_str.find(l_limit)
r_index = my_str.rfind(r_limit)
res = my_str[l_index + 1 : r_index]


# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str = 'abcde'
if len(my_str) % 2:
    my_str += "_"
result = []
for index in range(len(my_str) // 2):
    index = index * 2
    new_str = my_str[index: index + 2]
    result.append(new_str)
print(result)



# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответо

my_list = [2,4,1,5,3,9,0,7]
res = 0

for index in range(len(my_list)):
    if index in [0, len(my_list) - 1]:
        continue
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        res += 1
print(res)



"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить
элементы на четных местах из my_list_1,
а потом все элементы на нечетных местах из my_list_2.
"""

