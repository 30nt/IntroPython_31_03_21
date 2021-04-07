# переменные
# тип переменных
# приведение типов
# тип bool


# перменная - именованный объект
number = 1000
print(number)
number = "Hello"
print(number)
# print = 1000
# print(1)

number = 10
my_number = 23
result = number + my_number
print(result)

# переименование переменных
qwe = 123
asd = qwe
asd = qwe + 3
qwe = 5
# asd = 4
print(asd)

# типы данных
number = 10
print(number, type(number))

number = 1.0
print(number, type(number))

number = "10"
print(number, type(number))

# ввод с клавиатуры
value = input("Введи целое число:")
print(value, type(value))
result = int(value) * 2
print(result)


# приведение типов
# int -> float
value = -10
res = float(value)
print(res)

# int -> str
value = 10
res = str(value)
print(res)

# float -> int
value = -10.99 # отрезает все после .
res = int(value)
print(res)

# float -> str
value = 10.34
res = str(value)
print(res)

# str -> int
value = "100"  # если "выглядит" как целое число
res = int(value)
print(res)

# str -> float
value = "-1.034" # если "выглядит" как число с точкой
res = float(value)
print(res)

# str_1 = "I'm a sting"
# value = 12
# result = str(value)

# тип bool - логический тип. True/False
bool_value = 31 != 3
print(bool_value, type(bool_value))
value = 23 % 2 == 1
print(value)

# приведение к типу bool
# int -> bool
value = -10
res = bool(value) # True, кроме 0
print(res)

# float -> bool
value = 0.00000000000001
res = bool(value) # True, кроме 0.0
print(res)

# str -> bool
value = "False"
res = bool(value) # True, кроме ""
print(res)

# логические операторы
tea = False
coffe = True

res_bool = not tea
res_bool = tea and coffe
res_bool = tea or coffe
print(res_bool)