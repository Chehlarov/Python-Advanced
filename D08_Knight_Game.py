def check_knight_connections(m, r, c):
    connections = 0
    n = len(m)
    if m[r][c] == 'K':
        if r - 2 >= 0 and c - 1 >= 0 and m[r - 2][c - 1] == 'K':
            connections += 1
        if r - 2 >= 0 and c + 1 < n and m[r - 2][c + 1] == 'K':
            connections += 1
        if r + 2 < n and c - 1 >= 0 and m[r + 2][c - 1] == 'K':
            connections += 1
        if r + 2 < n and c + 1 < n and m[r + 2][c + 1] == 'K':
            connections += 1

        if r - 1 >= 0 and c - 2 >= 0 and m[r - 1][c - 2] == 'K':
            connections += 1
        if r - 1 >= 0 and c + 2 < n and m[r - 1][c + 2] == 'K':
            connections += 1
        if r + 1 < n and c - 2 >= 0 and m[r + 1][c - 2] == 'K':
            connections += 1
        if r + 1 < n and c + 2 < n and m[r + 1][c + 2] == 'K':
            connections += 1
    return connections


n = int(input())
table = []

for _ in range(n):
    table.append(list(input()))

removed_knights = 0

while True:
    max_connections = 0
    max_r, max_c = 0, 0

    for r in range(n):
        for c in range(n):
            current_connections = check_knight_connections(table, r, c)
            if current_connections > max_connections:
                max_connections = current_connections
                max_r = r
                max_c = c
    if max_connections > 0:
        table[max_r][max_c] = '0'
        removed_knights += 1
    else:
        print(removed_knights)
        exit(0)
