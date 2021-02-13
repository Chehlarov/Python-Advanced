start = int(input())
end = int(input())


def is_valid(el):
    return any(el % i == 0 for i in dividers)


dividers = {i for i in range(2, 11)}
results = [el for el in range(start, end + 1) if is_valid(el)]
print(results)
