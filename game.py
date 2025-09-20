# Tic-Tac-Toe

# number of squares in one row
board_size = 3

# playing field
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_board():
    """ Display the playing field"""
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)


def game_move(index, char):
    """Making a move"""
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False

    board[index - 1] = char
    return True


def check_winning():
    """Checking winning one of the players"""
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal lines
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical lines
        (0, 4, 8), (2, 4, 6)              # diagonal lines
    )

    for pos in win_combination:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            return board[pos[0]]

    return False


def start_game():
    # current player
    current_player = 'X'
    # step number
    step = 1
    show_board()

    while step <= 9:
        try:
            index = input(current_player + "'s turn. Enter playing field number (0 - exit): ")
            if index.strip() == "":
                print("Empty input! Please enter a number 1–9 (or 0 to exit).")
                continue

            index = int(index)
        except ValueError:
            print("Invalid input! Please enter a number 1–9 (or 0 to exit).")
            continue

        if index == 0:
            print("Game stopped by user.")
            return

        # if move successfully done
        if game_move(index, current_player):
            print("Move is done")
            show_board()

            # check win immediately after a move
            winner = check_winning()
            if winner:
                print(winner + " has won!")
                return

            # switch player
            current_player = 'O' if current_player == 'X' else 'X'
            step += 1
        else:
            print("Number is wrong! Please, try again!")

    print("Draw! The game is over!")


print("Welcome to the Tic-Tac-Toe game!")
start_game()
