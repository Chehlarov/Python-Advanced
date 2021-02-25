text = input()

try:
    n = int(input())
    print(text * n)
except ValueError:
    print("THe number must be integer")

