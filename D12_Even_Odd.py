def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    result = []
    if command == "even":
        result = list(filter(lambda x: int(x) % 2 == 0, numbers))
    elif command == "odd":
        result = list(filter(lambda x: int(x) % 2 != 0, numbers))
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
