class Rectangle:

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.width * self.height

    def __setattr__(self, key, value):
        if key in ("width", "height"):
            raise AttributeError("You can't change this attribute")
        else:
            super().__setattr__(key, value)

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        else:
            raise AttributeError("Wrong attribute")

x = Rectangle(4,5)

print(x.area())

try:
    x.width = 4
except AttributeError as e:
    print(e)

try:
    print(x.temp)
except AttributeError as e:
    print(e)