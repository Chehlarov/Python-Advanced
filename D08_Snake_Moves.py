rows, cols = [int(x) for x in input().split()]

word = input()
matrix = []
i = 0

for r in range(rows):
    matrix.append([])
    for c in range(cols):
        matrix[r].append(word[i % len(word)])
        i += 1
    if r % 2 == 1:
        matrix[r].reverse()

for el in matrix:
    print(''.join(el))
