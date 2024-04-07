from abc import ABC, abstractmethod
import math


class Figure(ABC):

    def count_perimetr(self):
        return NotImplementedError

    def count_area(self):
        return NotImplementedError


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def count_perimetr(self):
        return 2 * math.pi * self.radius

    def count_area(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):

    def __init__(self, a, b, c):
        if (a + b) < c or (a + c) < b or (b + c) < a:
            raise ValueError("You can`t create this triangle")
        self.a = a
        self.b = b
        self.c = c

    def count_perimetr(self):
        return self.a + self.b + self.c

    def count_area(self):
        p = self.count_perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count_perimetr(self):
        return self.x * 2 + self.y * 2

    def count_area(self):
        return self.x * self.y


figure_1 = Circle(3)
figure_2 = Triangle(2, 3, 4)
figure_3 = Rectangle(2, 5)


def my_func(item):
    return f'{item.count_perimetr()}, {item.count_area()}'


print(my_func(figure_1))
print(my_func(figure_2))
print(my_func(figure_3))
