import random

def print_board(board):
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print("\n-------------")


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def get_player_move(board):
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))

    if board[row][col] != " ":
        print("Invalid move! Try again.")
        return get_player_move(board)

    return row, col


def get_computer_move(board):
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append((row, col))

    return random.choice(available_moves)


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None
    moves_left = 9

    game_mode = input("Select game mode (PvP/PvC): ")
    if game_mode.lower() == "pvp":
        is_player_vs_player = True
    else:
        is_player_vs_player = False

    while moves_left > 0 and not winner:
        print_board(board)
        print("It's", current_player, "turn.")

        if (is_player_vs_player and current_player == "X") or not is_player_vs_player:
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)
            print("Computer selects row:", row, "and column:", col)

        board[row][col] = current_player
        winner = check_winner(board)
        current_player = "O" if current_player == "X" else "X"
        moves_left -= 1

    print_board(board)

    if winner:
        if is_player_vs_player:
            print("Player", winner, "wins!")
        else:
            if winner == "X":
                print("You win!")
            else:
                print("Computer wins!")
    else:
        print("It's a tie!")


play_game()
