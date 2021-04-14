# while числа
# debug mode
# обработка исключений
# ord, chr
# сортировка sort, sorted

# from random import randint
#
# main_value = randint(1, 10)
# go_game = True
# count = 5
# print("Угадай число от 1 до 10")
# while go_game and count:
#     value = input("Твоя попытка:")
#     try:
#         value = int(value)
#         if value == main_value:
#             go_game = False
#             print("ПОБЕДА!")
#         elif value > main_value:
#             print("Это число меньше")
#         else:
#             print("Это число больше")
#         count -= 1
#     except (ValueError, TypeError):
#         pass

# ord_value = ord("z")
# print(ord_value)
# chr_value = chr(98)
# print(chr_value)

# my_list = [12, 34, 5, 1, -6, 100]
# my_list.sort()
# print(my_list)
# new_list = sorted(my_list, reverse=True)
# print(new_list)
# print(my_list)
#
# print(sum(my_list))

# my_list = list("qwertyFGH123(*&")
# new_list = sorted(my_list)


"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
# my_str = 'blablacar'
# my_symbol = "bla"
#
# result = my_str.count(my_symbol)


"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
# my_str = 'blablablacar'
# my_symbol = "bla"
# count = my_str.count(my_symbol)
# symbol_list = [my_symbol] * count
# for line in symbol_list:
#     print(line)
# for _ in range(count):
#     print(my_symbol)
#
# pass


"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
# my_str = "bla BLA car"
# result_str = ""
# for symbol in my_str.upper():
#     if symbol not in result_str:
#         result_str += symbol    # result_str = result_str + symbol
# print(len(result_str))

# my_str = "bla BLA car"
# result_str = []
# for symbol in my_str.upper():
#     if symbol not in result_str:
#         result_str.append(symbol)
# print(len(result_str))


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# my_str = "sdhasfaknhkgfjabc"
# my_list = []
# # print(id(my_list))
# # my_list = list(my_str[::2])
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list)





"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
# my_list = []
# my_str = "qwerty"
# str_index = [1,4,3,3,2,0,5,5,1,0,0,3]
# for index in str_index:
#     my_list.append(my_str[index])
# print(my_list)






"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""

my_number = 1276412341283412348028042647251000

count = len(str(my_number))
print(count)



"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""

# max_digit = max(str(my_number))
# print(max_digit)

"""
10)
Дано целое число. Составить число с цифрами в обратном порядке.
"""

# new_value = int(str(my_number)[::-1])
# print(new_value)

"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""

new_value = int(''.join(sorted(str(my_number), reverse=True)))
pass