from functools import reduce


def multiply1(*args):
    result = 1
    for el in args:
        result *= el

    return result


def multiply(*args):
    return reduce(lambda x, y: x * y, args)


print(multiply(2, 3, 4))
