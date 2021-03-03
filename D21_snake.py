n = int(input())
field = []
MOVES = {'up': (-1, 0),
         'down': (1, 0),
         'left': (0, -1),
         'right': (0, 1)
         }
row_s = 0
col_s = 0
total_eaten_food = 0

for r in range(n):
    line = input()
    field.append([el for el in line])
    if 'S' in line:
        row_s = r
        col_s = line.index('S')

# game loop
while total_eaten_food < 10:
    move = input()
    if move == '':
        break
    field[row_s][col_s] = '.'
    row_s += MOVES[move][0]
    col_s += MOVES[move][1]
    if row_s < 0 or row_s >= n or col_s < 0 or col_s >= n:
        break
    if field[row_s][col_s] == '*':
        total_eaten_food += 1
    if field[row_s][col_s] == 'B':
        field[row_s][col_s] = '.'
        for r in range(n):
            if 'B' in field[r]:
                row_s = r
                col_s = field[r].index('B')
    field[row_s][col_s] = 'S'

if total_eaten_food == 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {total_eaten_food}")

for row in field:
    print(*row, sep="")
