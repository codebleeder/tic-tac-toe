"""
    app.py
    ~~~~~~

    The main function of the Tic-Tac-Toe game

    author: Sharad Shivmath
"""

from board import Board
import ai
import human

if __name__ == '__main__':
    symbols = human.get_symbol()
    b = Board(symbols['human_symbol'], symbols['ai_symbol'])
    game_over = False

    # For the game to end, either the board should be full,
    # in which case it will be a draw, or one of the players
    # should win.
    while b.is_board_full() is False and game_over is False:
        b.print_board()
        human.make_move(b)
        game_over = ai.make_move(b)
    b.print_board()
    print '------------'
    print ' Game over!'
    print '------------'
