
from board import Board
from interactions import get_human_symbol, get_cell_num

if __name__ == '__main__':

	symbols = get_human_symbol()
	b = Board(symbols['human_symbol'], symbols['computer_symbol'])
	
	while b.is_board_full() is False:
		b.print_board()
		cell_num = get_cell_num()
		while b.make_human_entry(cell_num) is False:
			print 'The cell is occupied!'
			cell_num = get_cell_num()
	