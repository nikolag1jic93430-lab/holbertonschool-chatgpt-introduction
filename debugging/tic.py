#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

def check_winner(board):
    # rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def read_index(prompt):
    """
    Read a valid index 0, 1, or 2 from the user.
    Keeps asking until the input is valid.
    """
    while True:
        s = input(prompt).strip()
        try:
            value = int(s)
        except ValueError:
            print("Invalid input: please enter a number (0, 1, or 2).")
            continue

        if value not in (0, 1, 2):
            print("Out of range: please enter 0, 1, or 2.")
            continue

        return value

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # draw check BEFORE asking more moves (if board already full)
        if board_full(board):
            print("It's a draw!")
            break

        row = read_index("Enter row (0, 1, or 2) for player " + player + ": ")
        col = read_index("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # check winner AFTER placing
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
