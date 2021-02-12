# matrix = [
#     [1, 2, 3],
#     [1, 2, 3]
# ]

# matrix = [[0]*5 for _ in range(5)]
# print(matrix)
def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1],
            [1, 3],
        ]
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for r in range(rows_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()
matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        matrix_sum += row[c]

print(matrix_sum)
print(matrix)