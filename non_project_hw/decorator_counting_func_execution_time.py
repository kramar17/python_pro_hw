import time


def measure_time(func):
    def closure(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    return closure


@measure_time
def some_function():
    time.sleep(2)


