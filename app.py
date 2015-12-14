
from board import Board
from interactions import get_human_symbol

if __name__ == '__main__':
	symbols = get_human_symbol()
	b = Board(symbols['human_symbol'], symbols['computer_symbol'])
	