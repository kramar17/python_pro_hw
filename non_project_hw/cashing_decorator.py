def cache_results(func):
    cache_dict = dict()

    def closure(*args, **kwargs):
        nonlocal cache_dict
        if args not in cache_dict.keys():
            cache_dict[args] = func(*args, **kwargs)
            return func(*args, **kwargs)
        else:
            return cache_dict[args]
    return closure


@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))  # Обчислюється
print(fibonacci(10))  # Використання кешу
