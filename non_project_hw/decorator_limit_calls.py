def limit_calls(max_calls):
    def my_decorator(func):
        counter = 0

        def closure(*args, **kwargs):
            nonlocal counter
            if counter < max_calls:
                func(*args, **kwargs)
                counter += 1
            else:
                raise ValueError("Too much calls of function")
        return closure
    return my_decorator


@limit_calls(4)
def some_function():
    print("Виклик функції")


