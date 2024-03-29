def prime_gener(border):

    for i in range(1, border + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


x = prime_gener(29)
for i in x:
    print(i)
