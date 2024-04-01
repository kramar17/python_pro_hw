def upgrade_numbers(number):
    return (number**2) - 1


def my_summ(some_numbers_list):
    result = 0
    for i in some_numbers_list:
        result += upgrade_numbers(i)
    return result
        

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_summ(some_list))
