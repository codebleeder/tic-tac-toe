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

	

	def __check_for_winning_move(self):
		# Horizontal check
		for i in range(0, 7, 3):
			horizontal_triplet = self.arr[0+i:3+i]
			if horizontal_triplet.count(self.computer_symbol) == 2 and horizontal_triplet.count(' ') == 1:
				return {'winning_move_present': True, 'index': self.arr[0+i:3+i].index(' ')+i}
		

		# Vertical check
		for j in range(0, 3):
			vertical_triplet = [self.arr[j], self.arr[j+3], self.arr[j+6]]
			if vertical_triplet.count(self.computer_symbol) == 2 and vertical_triplet.count(' ') == 1:
				return {'winning_move_present': True, 'index' : vertical_triplet.index(' ')*3+j}

		

		# diagonal check
		diagonal_triplet1 = [self.arr[0], self.arr[4], self.arr[8]]
		if diagonal_triplet1.count(self.computer_symbol) == 2 and diagonal_triplet1.count(' ') == 1:
			return {'winning_move_present': True, 'index' : diagonal_triplet1.index(' ')*4}
		diagonal_triplet2 = [self.arr[2], self.arr[4], self.arr[6]]
		if diagonal_triplet2.count(self.computer_symbol) == 2 and diagonal_triplet2.count(' ') == 1:
			return {'winning_move_present': True, 'index' : diagonal_triplet1.index(' ')*4}
		return {'winning_move_present': False, 'index': 0}
		
	'''
	def __make_computer_entry(self, index):
		check = __check_for_winning_move()
		if check['winning_move_present'] == True:
			self.arr[check[index]] = computer_symbol
		else:
			print 'winning move not present'
	'''

	def __make_computer_entry(self, index):
		self.arr[index] = self.computer_symbol




