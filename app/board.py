# Board class is the game's main datastructure

class Board:
	def __init__(self, human_symbol, ai_symbol):
		self.arr = [' ']*9 # A blank space is represented by a whitespace
		self.human_symbol = human_symbol
		self.ai_symbol = ai_symbol

	def print_board(self):
		'''Prints the array in game format'''
		for i in range(9):
			if i == 0 or i == 1 or i == 4 or i == 7:
				print self.arr[i], '|',
			elif i == 3 or i == 6:
				print '----------'
				print self.arr[i], '|',
			elif i == 2 or i == 5 or i == 8:
				print self.arr[i]
				