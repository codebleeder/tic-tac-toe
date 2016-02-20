from app.board import Board 
import unittest


class BoardUnitTest(unittest.TestCase):
	def setUp(self):
		self.board = Board(human_symbol = 'x', ai_symbol = 'o')
	
	def test_if_board_object_can_be_instantiated(self):
		self.assertTrue(self.board.human_symbol == 'x' and self.board.ai_symbol == 'o')
		self.assertTrue(len(self.board.arr) == 9)

	def test_if_board_prints(self):
		self.board.print_board()

	def test_make_human_entry(self):
		for i in range(0,9):
			self.board.make_human_entry(i+1)
			self.assertTrue(self.board.arr[i] == 'x')
		# check for out-of-range values
		self.board.make_human_entry(0) 
		print 'should print: Please enter a number between 1 and 9'
		self.board.make_human_entry(2) 
		print 'should print: Cell occupied! Enter an unoccupied cell'

	def __fill_and_test_symbol(symbol):
		for i in range (0, 9):
			self.board.make_entry(i, symbol)
			if symbol == 'human_symbol'
				self.assertTrue(self.board.arr[i] == 'x')
			else:
				self.assertTrue(self.board.arr[i] == 'o')

	def test_make_entry_valid_human_symbol(self):
		# test for human symbol
		# valid, empty cell numbers:
		__fill_and_test_symbol('human_symbol')
	
	def test_make_entry_valid_ai_symbol(self):
			# test for AI symbol
		# valid, empty cell numbers:
		__fill_and_test_symbol('ai_symbol')
		