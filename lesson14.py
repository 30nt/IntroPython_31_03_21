# класс
# атрибут класса
# экземпляр класса
# атрибут экземпляра класса
# метод экземпляра класса


class Point:  # класс
    ## плохая практика использовать атрибут класса
    # x = 0  # атрибут класса
    # y = 0  # атрибут класса
    def __init__(self, x, y):
        self.x = x
        self.y = y

point_A = Point(3, 4)  # экземпляр класса
print(point_A.x)
# point_A.x = 10
# # point_A.y = 10
point_B = Point(5,-5)  # экземпляр класса
print(point_B.x)
# point_B.x = -21  # атрибут экземпляра класса
# point_C = Point()  # экземпляр класса
# point_C.x = -45
# print(point_A.x, point_B.x, point_C.x, Point.x)
