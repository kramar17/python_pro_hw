def cube_of_numbers(border):
    if not isinstance(border, int):
        raise TypeError("Border must be a integer number")
    if border == 0:
        raise ValueError("Border can`n be a zero")
    result_list = []
    for item in range(2, border + 1):
        result_list.append(item**3)
        yield result_list


x = cube_of_numbers(10)
for i in x:
    print(i)
