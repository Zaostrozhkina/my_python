from functools import reduce

my_list = [n for n in range(100, 1001) if n % 2 == 0]


def my_f(n_1, n_2):
    return n_1 * n_2


print(my_list)
print(reduce(my_f, my_list))
