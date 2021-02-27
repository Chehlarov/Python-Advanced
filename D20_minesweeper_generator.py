n = int(input())
bomb_count = int(input())

NEIGHBOURS = ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1))
field = [[0 for _ in range(n)] for _ in range(n)]


def count_nearby_mines(r, c):
    for el in NEIGHBOURS:
        r_n = r + el[0]
        c_n = c + el[1]
        if 0 <= r_n < n and 0 <= c_n < n and field[r_n][c_n] != '*':
            field[r_n][c_n] += 1


for _ in range(n):
    r, c = eval(input())
    field[r][c] = '*'
    count_nearby_mines(r, c)

for row in field:
    print(*row, sep=' ')

