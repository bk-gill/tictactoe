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


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None
    moves_left = 9

    while moves_left > 0 and not winner:
        print_board(board)
        print("It's", current_player, "turn.")

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            current_player = "O" if current_player == "X" else "X"
            moves_left -= 1
        else:
            print("Invalid move! Try again.")

    print_board(board)

    if winner:
        print("Player", winner, "wins!")
    else:
        print("It's a tie!")


play_game()
