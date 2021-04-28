# функции
import random


# DRY
def create_point():
    point = (random.randint(-10, 10), random.randint(-10, 10))
    return point


def create_triangle():
    triangle = {"A": create_point(), "B": create_point(), "C": create_point()}  # генератор словаря
    return triangle


def create_triangles_list():
    triangles = [create_triangle() for _ in range(count)]
    return triangles


def print_triangles():
    for triangle in triangles:  # область видимости
        print(triangle)


count = 2
triangles = create_triangles_list()
print_triangles()
