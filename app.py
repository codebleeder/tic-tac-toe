
from board import Board
from interactions import get_human_symbol, get_cell_num

if __name__ == '__main__':

	symbols = get_human_symbol()
	b = Board(symbols['human_symbol'], symbols['computer_symbol'])
	'''
	while b.is_board_full() is False:
		b.print_board()
		cell_num = get_cell_num()
		while b.make_human_entry(cell_num) is False:
			print 'The cell is occupied!'
			cell_num = get_cell_num()
	'''

	'''
	# vertical check
	b.make_human_entry(1)
	b.make_human_entry(5)
	b.make_human_entry(7)
	
	b._Board__make_computer_entry(2)
	b._Board__make_computer_entry(8)
	b.print_board()
	print b._Board__check_for_winning_move()
	'''

	# diagonal check
	b.make_human_entry(2)
	b.make_human_entry(5)
	b.make_human_entry(7)
	
	b._Board__make_computer_entry(2)
	b._Board__make_computer_entry(8)
	b.print_board()
	print b._Board__check_for_winning_move()
			