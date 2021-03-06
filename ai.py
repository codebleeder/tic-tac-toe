"""
    ai.py
    ~~~~~

    This module contains functions related to the AI player.

    author: Sharad Shivmath
"""

from board import Board


def __check_for_winning_move(board_obj, symbol):
    """Checks if there is any winning move for the given symbol."""
    arr = board_obj.get_arr()
    # A triplet(3 cells - Horizonal/vertical/diagonal)
    # contains a winning move if it contains one empty
    # cell and 2 symbols of either AI or human player

    # Horizontal check
    for i in range(0, 7, 3):
        horizontal_triplet = arr[0+i:3+i]
        if (horizontal_triplet.count(symbol) == 2 and
                horizontal_triplet.count(' ') == 1):
            return {'winning_move_present': True,
                    'index': arr[0+i:3+i].index(' ')+i}

    # Vertical check
    for j in range(0, 3):
        vertical_triplet = [arr[j], arr[j+3], arr[j+6]]
        if (vertical_triplet.count(symbol) == 2 and
                vertical_triplet.count(' ') == 1):
            return {'winning_move_present': True,
                    'index': vertical_triplet.index(' ')*3+j}

    # diagonal check
    diagonal_triplet1 = [arr[0], arr[4], arr[8]]
    if (diagonal_triplet1.count(symbol) == 2 and
            diagonal_triplet1.count(' ') == 1):
        return {'winning_move_present': True,
                'index': diagonal_triplet1.index(' ')*4}
    diagonal_triplet2 = [arr[2], arr[4], arr[6]]
    if (diagonal_triplet2.count(symbol) == 2 and
            diagonal_triplet2.count(' ') == 1):
        return {'winning_move_present': True,
                'index': diagonal_triplet2.index(' ')*2+2}
    return {'winning_move_present': False, 'index': 0}


def __find_empty_corner(board_obj):
    arr = board_obj.get_arr()
    if arr[0] == ' ':
        return 0
    elif arr[2] == ' ':
        return 2
    elif arr[6] == ' ':
        return 6
    elif arr[8] == ' ':
        return 8
    else:
        return None


def __find_empty_side(board_obj):
    arr = board_obj.get_arr()
    if arr[1] == ' ':
        return 1
    elif arr[3] == ' ':
        return 3
    elif arr[5] == ' ':
        return 5
    elif arr[7] == ' ':
        return 7
    else:
        return None


def make_move(board_obj):
    """Main algorithm of AI player."""

    symbols = board_obj.get_symbols()
    human_symbol = symbols['human_symbol']
    ai_symbol = symbols['ai_symbol']

    # Check for any winning moves for the AI player
    check1_result = __check_for_winning_move(board_obj, ai_symbol)
    if check1_result['winning_move_present'] is True:
        print '---------- '
        print ' AI wins! '
        print '---------- '
        board_obj.make_ai_entry(check1_result['index'], ai_symbol)
        return True

    # Check for any winning moves for the Human player
    check2_result = __check_for_winning_move(board_obj, human_symbol)
    if check2_result['winning_move_present'] is True:
        # print "Player's winning move blocked!"
        board_obj.make_ai_entry(check2_result['index'], ai_symbol)
        return False

    # Check for corner places and fill them if available
    empty_corner = __find_empty_corner(board_obj)
    if empty_corner is not None:
        board_obj.make_ai_entry(empty_corner, ai_symbol)
        return False

    # Check the center cell and fill if empty
    if board_obj.get_arr()[4] == ' ':
        board_obj.make_ai_entry(4, ai_symbol)
        return False

    # Fill any of the empty sides
    empty_side = __find_empty_side(board_obj)
    if empty_side is not None:
        board_obj.make_ai_entry(empty_side, ai_symbol)
        return False
