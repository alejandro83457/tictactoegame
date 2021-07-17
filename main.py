"""
TicTacToe Game
Name: Alejandro Martinez
Version: 0.1.0

Text-based TicTacToe game.
"""

import random
import numpy as np

board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]
symbols = ['X', 'O']


def show_board():
    """ Prints current board """
    print(*board, sep='\n')


def get_move():
    """ Decided to make it a func because it's kind of dense."""
    return int(input("Enter row: ")) - 1, int(input("Enter col: ")) - 1


def is_valid_move(move):
    """ Checks if move is valid on board"""
    spot = board[move[0]][move[1]]
    # Checking for blank or taken spot
    if '_' == spot not in symbols:
        board[move[0]][move[1]] = symbols[turn]
        return True
    return False


def check_game():
    # Checks game for winner. If no winner returns false.
    if board[0].count(symbols[turn]) == 3:
        announce_winner()
        return True

    if board[1].count(symbols[turn]) == 3:
        announce_winner()
        return True

    if board[2].count(symbols[turn]) == 3:
        announce_winner()
        return True

    # Transposed the board to keep logic clean.
    trans_board = np.array(board).T.tolist()
    if trans_board[0].count(symbols[turn]) == 3:
        announce_winner()
        return True

    if trans_board[1].count(symbols[turn]) == 3:
        announce_winner()
        return True

    if trans_board[2].count(symbols[turn]) == 3:
        announce_winner()
        return True

    # Converted to extract main diagonal.
    diagonal_board_1 = np.array(board).diagonal().tolist()
    if diagonal_board_1.count(symbols[turn]) == 3:
        announce_winner()
        return True

    # Converted to extract secondary diagonal.
    diagonal_board_2 = np.array(np.fliplr(board)).diagonal().tolist()
    if diagonal_board_2.count(symbols[turn]) == 3:
        announce_winner()
        return True

    # Checks if game is over.
    total = 0
    for row in board:
        total += row.count('_')
    if total == 0:
        print('\nGAME OVER. NO ONE WON.')
        return True

    return False


def announce_winner():
    # Function to remove clutter
    print(f"\nTHE WINNER IS {symbols[turn]}!!")


# Beginning of main loop.
print('WELCOME TO MY TIC-TAC-TOE GAME !!')

# Will randomize turn.
turn = random.randint(0, 1)
while True:
    # oscillation for turn
    turn += 1
    turn = turn % 2
    print(f"\nIt is {symbols[turn]}'s turn")

    show_board()
    move = get_move()

    # Tests for valid move and adds it to board
    while True:
        if is_valid_move(move):
            break
        print('Not valid move. Try again.')
        move = get_move()

    # Var decides if game is over.
    end_game = check_game()
    if end_game:
        break

show_board()