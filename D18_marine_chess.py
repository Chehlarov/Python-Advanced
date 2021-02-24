def add_move_to_board(board, move, symbol):
    move = move - 1
    if board[move // 3][move % 3] == " ":
        board[move // 3][move % 3] = symbol
        return True
    return False


def print_board(board):
    # print(board)
    for el in board:
        print("| ", end='')
        print(*el, sep=" | ", end=" |\n")


def has_player_won(board, current_player, symbol):
    for row in board:
        if all(map(lambda x: x == symbol, row)):
            return True
    inverted_board = [[board[j][i] for j in range(3)] for i in range(3)]
    for row in inverted_board:
        if all(map(lambda x: x == symbol, row)):
            return True

    primary_diagonal = [board[i][i] for i in range(3)]
    if all(map(lambda x: x == symbol, primary_diagonal)):
        return True
    secondary_diagonal = [board[i][2 - i] for i in range(3)]
    if all(map(lambda x: x == symbol, secondary_diagonal)):
        return True

    return False


def start_game():
    # Ask player 1 and 2 name
    p1_name = input("Player one name: ")
    p2_name = input("Player two name: ")

    # Ask player 1 symbol
    while True:
        p1_symbol = input(f"{p1_name} would like to play with 'X' or 'O'?")
        if p1_symbol in {"X", "O"}:
            break
    p2_symbol = "O" if p1_symbol == 'X' else 'X'

    # enumerate board
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")

    # board = [[" "]*3]*3 this makes shallow copy and doesn't work
    board = [[" "] * 3 for _ in range(3)]

    # print which player starts the game
    current_player = p1_name
    current_player_symbol = p1_symbol
    next_player = p2_name
    next_player_symbol = p2_symbol

    print(f"{current_player} starts the game")

    # Game loop
    while True:
        # ask current player for move (1-9)
        move = int(input(f"{current_player} choose a free position [1-9]"))

        while not add_move_to_board(board, move, current_player_symbol):
            print("This position is already used")
            move = int(input(f"{current_player} choose a free position [1-9]"))

        # print board
        print_board(board)

        # check if current player won
        if has_player_won(board, current_player, current_player_symbol):
            print(f"{current_player} has won!")
            break

        # switch players
        current_player, next_player = next_player, current_player
        current_player_symbol, next_player_symbol = next_player_symbol, current_player_symbol


start_game()
