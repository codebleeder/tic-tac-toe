"""
    human.py
    ~~~~~~~~

    This module contains functions related to the human player.

    author: Sharad Shivmath
"""


def get_symbol():
    """Asks the human player to choose x or o, and returns the symbol."""
    human_symbol = raw_input(
                '''Welcome! To start playing Tic-Tac-Toe,
Type the symbol of your choice: x or o: '''
        )
    if human_symbol == 'x':
        symbols = {'human_symbol': 'x', 'ai_symbol': 'o'}
        return symbols

    elif human_symbol == 'o':
        symbols = {'human_symbol': 'o', 'ai_symbol': 'x'}

        return symbols
    else:
        print 'invalid symbol entered!'
        return get_symbol()


def __get_cell_num():
    """Asks the human player a cell number and returns it."""
    try:
        cell_num = int(raw_input('Enter a cell number between 1 and 9: '))
    except ValueError:
        print 'Invalid input! enter a number'
        return __get_cell_num()

    # Check for a valid number
    if cell_num < 1 or cell_num > 9:
        print 'Number not within range!'
        return __get_cell_num()
    else:
        return cell_num


def make_move(board_object):
    """Fills the game board with human player's symbols."""
    cell_num = __get_cell_num()
    entry_result = board_object.make_human_entry(cell_num)
    # Keep asking until an empty cell is specified
    while entry_result is False:
        print 'The cell is occupied!'
        cell_num = __get_cell_num()
        entry_result = board_object.make_human_entry(cell_num)
