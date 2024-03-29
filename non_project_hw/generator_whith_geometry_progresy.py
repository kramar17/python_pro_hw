def my_generator(start, step, count):
    if not (isinstance(start, (int, float)) and isinstance(step, (int, float))):
        raise TypeError("elements of progression must be a numbers")
    if start == 0:
        raise ValueError("Start of geometry progression can`t be zero")
    if step == 0:
        raise ValueError("Step can`t be a zero")
    if count == 0:
        raise ValueError("Count of elemens can`t be a zero")
    current = start
    for _ in range(count):
        yield current
        current *= step


x = my_generator(1, 3, 10)
for i in x:
    print(i)