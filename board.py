import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

class Board:
	def __init__(self, human_symbol, computer_symbol):
		self.arr = [' ']*9
		self.human_symbol = human_symbol
		self.computer_symbol = computer_symbol
		self.empty_cells = range(1,10) # To help user not to overwrite

	def print_board(self):
		for i in range(9):
			if i == 0 or i == 1  or i == 4  or i==7:
				print self.arr[i], '|', 
			elif i == 3 or i == 6:
				print '---------'
				print self.arr[i], '|', 
			elif i == 2 or i == 5 or i == 8:
				print self.arr[i]

	def make_human_entry(self, cell_num):
		if self.arr[cell_num-1] == ' ':
			self.arr[cell_num-1] = self.human_symbol
			return True
		else:
			return False

	def is_board_full(self):
		if ' ' in self.arr:
			return False
		else:
			return True 

	def make_computer_entry(self):
		
