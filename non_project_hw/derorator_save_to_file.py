import random


def save_to_file(func):
    def closure(*args, **kwargs):
        file1 = open("my_file.txt", "a")
        file1.write(f"\n{func(*args, **kwargs)}")
        file1.close()

    return closure


@save_to_file
def my_func(some_num):
    return random.randint(1, 100) * some_num


my_func(10)
