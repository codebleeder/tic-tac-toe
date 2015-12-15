def get_symbol():
	human_symbol = raw_input('Welcome! To start playing Tic-Tac-Toe, type the symbol of your choice: x or o: ')
	if human_symbol == 'x':
		symbols = {'human_symbol': 'x', 'ai_symbol':'o'}		
		return symbols

	elif human_symbol == 'o':
		symbols = {'human_symbol': 'o', 'ai_symbol':'x'}
		
		return symbols
	else:
		print 'invalid symbol entered!'
		return get_human_symbol()

def get_cell_num():
	try:
		cell_num = int(raw_input('Enter a cell number between 1 and 9: '))
	except ValueError:
		print 'Invalid input! enter a number'
		return get_cell_num()

	if cell_num < 1 or cell_num > 9:
		print 'Number not within range!'
		return get_cell_num()
	else:		
		return cell_num
		
def make_move(board_object):
	cell_num = get_cell_num()
	while board_object.make_human_entry(cell_num) is False:
		print 'The cell is occupied!'
		make_move(board_object)	
