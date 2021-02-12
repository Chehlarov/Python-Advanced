# def check_for_square(m, r, c):
#    return m[r][c] == m[r + 1][c]  == m[r][c + 1] == m[r + 1][c + 1]


rows, cols = [int(x) for x in input().split()]

matrix = []
counter = 0

for _ in range(rows):
    row_values = input().split()
    matrix.append(row_values)

for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r + 1][c] == matrix[r][c + 1] == matrix[r + 1][c + 1]:
            counter += 1

print(counter)
