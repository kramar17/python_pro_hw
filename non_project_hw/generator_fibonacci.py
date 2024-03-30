def generator_fibonacci(how_much_numbers):
    a = 0
    b = 1
    for i in range(how_much_numbers):
        yield a
        a, b = b, a + b


x = generator_fibonacci(10)
for i in x:
    print(i)