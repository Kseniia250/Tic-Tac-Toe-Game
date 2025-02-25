# Tic-Tac-Toe

# number of squares in one row
board_size = 3

# playing field
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def show_board():
    """ Display the playing field"""
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('', board[i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|') * 3)

def game_move(index, char):
    """Making a move"""
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return  False

    board[index-1] = char
    return True

def check_winning():
    """Checking winning one of the players"""
    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), #horizontal lines
        (0, 3, 6), (1, 4, 7), (2, 5, 8), #vertical lines
        (0, 4, 8), (2, 4, 6)             #diagonal lines
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return  win

def start_game():
    # current player
    current_player = 'X'
    # step number
    step = 1
    show_board()

    while step < 10 and check_winning() == False:
        index = int(input(current_player + "'s turn." + " Enter playing field number (0 - exit):"))
        if index == 0:
            break

        #if move successfully done
        if game_move(int(index), current_player):
            print("Move is done")

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            show_board()
            step += 1
        else:
            print("Number is wrong! Please, try again!")

    if (step == 10):
        print("Draw! The game is over! ")
    else:
        print(check_winning() + " has won")

print("Welcome to the Tic-Tac-Toe game!")
start_game()