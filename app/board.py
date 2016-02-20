# Board class is the game's main datastructure

class Board:
	def __init__(self, human_symbol, ai_symbol):
		self.arr = [' ']*9 # A blank space is represented by a whitespace
		self.human_symbol = human_symbol
		self.ai_symbol = ai_symbol

	def print_board(self):
		'''Prints the array in game format'''
		print ''
		for i in range(9):
			if i == 0 or i == 1 or i == 4 or i == 7:
				print self.arr[i], '|',
			elif i == 3 or i == 6:
				print '----------'
				print self.arr[i], '|',
			elif i == 2 or i == 5 or i == 8:
				print self.arr[i]

	def make_human_entry(self, cell_num):
		"""Fill array with human player's input."""
		# Cells are numbered naturally for human player
		if cell_num < 1 or cell_num > 9:
			print 'Please enter a number between 1 and 9'
		elif self.arr[cell_num-1] != ' ':
			print 'Cell occupied! Enter an unoccupied cell'
		else:
			self.arr[cell_num-1] = self.human_symbol

	def make_ai_entry(self, cell_num):
		'''Fill array with AI player's input.'''
		# Cells are numbered from 0 to 8
		self.arr[cell_num] = self.ai_symbol

	def make_entry(self, cell_num, symbol_type):
		if cell_num < 0 or cell_num > 8:
			print 'Range error! Enter a number between 0 and 8'
		elif self.arr[cell_num] != ' ':
			print 'Cell occupied! Enter an unoccupied cell'
		else:
			if symbol_type == 'human_symbol':
				self.arr[cell_num] = self.human_symbol
			else:
				self.arr[cell_num] = self.ai_symbol 				