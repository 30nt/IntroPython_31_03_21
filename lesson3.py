# if условие:
#     блок действий если условие Да
# elif условие2:
#     блок действий если условие2 Да
# .....
# else:
#     блок действий если Нет


value = -100
if value > 10:
    print(value, "> 10")
elif value < 10:
    print(value, "< 10")
else:
    print(value, "== 10")
print("Finish!")

value = 123
if not (value % 2 or value % 3):
    print(value, "делится на 6")
elif not value % 2:
    print(value, "делится на 2")
elif not value % 3:
    print(value, "делится на 3")
else:
    print(value, "не делится на 2 и 3")

# Тернарный оператор
number = 12.5

# if number % 2:
#     result = "Нечетное"
# else:
#     result = "Четное"

result = "Нечетное" if number % 2 else "Четное"

print(result)

# форматирование строк
# Строка - неизменяемый объект
value = -100
print(value, "> 10")
print(f"{value} > 10")

filename = "lesson3.py"
path = "IntroPython"
# full_path = path + "/" + filename
full_path = f"{path}/{filename}"
print(full_path)

print(len(full_path))

if "oPy" in full_path:
    print("!!!")

print(full_path[-3]) # обращение по индексу

print(full_path[13:21])  # срез от .. до. (Правый конец не включаем)
print(full_path[-3:-1])
print(full_path[-3:])
print(full_path[:3])
print(full_path[:])
print(full_path[::2])  # третий параметр - шаг
print(full_path[1::2])
print(full_path[-3:-10:-1])  # можно ошибиться
new_path = full_path[-10:-3]
new_path = new_path[::-1]
print(new_path)

# цикл while

value = 10
while value < 20:
    print(value)
    value += 1
######################################################
go_ahead = True
while go_ahead:
    print(value)
    value += 1
    if value >= 20:
        go_ahead = False