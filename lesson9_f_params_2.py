# функции
import random

MIN_LIMIT = -10
MAX_LIMIT = 10


# DRY
def create_point():
    point = (random.randint(MIN_LIMIT, MAX_LIMIT), random.randint(MIN_LIMIT, MAX_LIMIT))
    return point


def create_triangle():
    triangle = {"A": create_point(),
                "B": create_point(),
                "C": create_point()}  # генератор словаря
    return triangle


def create_triangles_list(count):
    triangles = [create_triangle() for _ in range(count)]
    return triangles


def print_triangles(triangles):
    for triangle in triangles:  # область видимости
        print(triangle)


count = 2
triangles_1 = create_triangles_list(count)
triangles_2 = create_triangles_list(4)
print_triangles(triangles_1)
print('------------------')
print_triangles(triangles_2)
