# 1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

# 2. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 1 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.
import random
import string


def generate_string(min_limit, max_limit):
    str_list = [random.choice(string.ascii_lowercase) for _ in range(random.randint(min_limit, max_limit))]
    return "".join(str_list)


def create_spaces(some_str):
    some_str_list = list(some_str)
    space_number = 0
    while space_number < len(some_str_list):
        new_space = random.randint(2,11)
        space_number += new_space
        if space_number < len(some_str_list):
            some_str_list[space_number] = " "
    return "".join(some_str_list)


def create_upper_case(some_str):
    list_str = some_str.split()
    list_str = [word.capitalize() for word in list_str]
    return " ".join(list_str)


def transform_string(some_str):
    new_str = create_spaces(some_str)
    new_str = create_upper_case(new_str)
    return new_str


my_string = generate_string(100, 200)
new_str = transform_string(my_string)
print(new_str)