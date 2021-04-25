"""複数の引数をタプルとして受け取る"""


def my_sum(*args):
    return sum(args)

def print_args(*args):
    print(args)

print(my_sum(1, 2, 3, 4))
# 10

print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# 55

print_args(1, 2, 3)
# (1, 2, 3)