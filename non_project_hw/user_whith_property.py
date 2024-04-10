class User:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    def __setattr__(self, key, value):
        if key in ("first_name", "last_name"):
            raise AttributeError("You can't change this attribute")
        else:
            super().__setattr__(key, value)

    def __getattr__(self, item):
        if item not in self.__dict__.keys():
            return "You don`t have this attribute"


test_user = User("vova", "putin")

try:
    test_user.first_name = "huilo"
except AttributeError as e:
    print(e)
print(test_user.age)