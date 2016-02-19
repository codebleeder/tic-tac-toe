from app.board import Board 
import unittest

class BoardUnitTest(unittest.TestCase):
	def setUp(self):
		self.board = Board(human_symbol = 'x', ai_symbol = 'o')
	
	def test_if_board_object_can_be_instantiated(self):
		self.assertTrue(board.human_symbol == 'x' and board.ai_symbol == 'o')
		self.assertTrue(len(board.arr) == 9)

	def test_if_board_prints(self):
		self.board.print_board()