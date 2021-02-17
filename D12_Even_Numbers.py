data = list(map(int, input().split()))
result = list(filter(lambda x: x % 2 == 0, data))

print(result)
