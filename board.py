"""
    board.py
    ~~~~~~~~

    This module contains the Board class.

    author: Sharad Shivmath
"""


class Board:
    def __init__(self, human_symbol, ai_symbol):
        """
        Constructor for Board object.
        Initialize array, and store human and AI symbols.
        """
        self.arr = [' ']*9  # Blank spaces are stored as single white space
        self.human_symbol = human_symbol
        self.ai_symbol = ai_symbol

    def print_board(self):
        """Prints the array in game format."""
        for i in range(9):
            if i == 0 or i == 1 or i == 4 or i == 7:
                print self.arr[i], '|',
            elif i == 3 or i == 6:
                print '---------'
                print self.arr[i], '|',
            elif i == 2 or i == 5 or i == 8:
                print self.arr[i]

    def make_human_entry(self, cell_num):
        """Fill array with human player's input."""
        # Cells are numbered naturally for human player
        if self.arr[cell_num-1] == ' ':
            self.arr[cell_num-1] = self.human_symbol
            return True
        else:
            return False

    def is_board_full(self):
        """Returns True if the board array is full."""
        if ' ' in self.arr:
            return False
        else:
            print '-------------'
            print ' Its a Draw!'
            print '-------------'
            return True

    def get_arr(self):
        """Getter function for array."""
        return self.arr

    def get_symbols(self):
        """Getter function for symbols."""
        return {'human_symbol': self.human_symbol, 'ai_symbol': self.ai_symbol}

    def make_ai_entry(self, index, symbol):
        """Fill array with AI player's input."""
        self.arr[index] = symbol
