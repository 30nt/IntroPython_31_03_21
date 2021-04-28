# функции
import random


# DRY
def create_point(min_limit, max_limit):
    point = (random.randint(min_limit, max_limit), random.randint(min_limit, max_limit))
    return point


def create_triangle(min_limit, max_limit):
    triangle = {"A": create_point(min_limit, max_limit),
                "B": create_point(min_limit, max_limit),
                "C": create_point(min_limit, max_limit)}  # генератор словаря
    return triangle


def create_triangles_list(count, min_limit, max_limit):
    triangles = [create_triangle(min_limit, max_limit) for _ in range(count)]
    return triangles


def print_triangles(triangles):
    for triangle in triangles:  # область видимости
        print(triangle)


count = 2
min_limit = -10
max_limit = 10
triangles_1 = create_triangles_list(count, min_limit, max_limit)
triangles_2 = create_triangles_list(4, min_limit, max_limit)
print_triangles(triangles_1)
print('------------------')
print_triangles(triangles_2)

