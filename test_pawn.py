import unittest
from pawn import Pawn
from board import Board
from piece import Piece

class TestPawn(unittest.TestCase):

    def setUp(self):

        self.board = Board()
        self.white_pawn = Pawn("white", self.board)
        self.black_pawn = Pawn("black", self.board)
        self.board.place_piece(self.white_pawn, 1, 4) 
        self.board.place_piece(self.black_pawn, 6, 4) 

    def test_white_pawn_standard_move(self):
        # Test the white pawn's single move forward
        self.assertTrue(self.white_pawn.valid_positions(1, 4, 2, 4))
        self.assertFalse(self.white_pawn.valid_positions(1, 4, 3, 4)) 
         
    def test_black_pawn_standard_move(self):
        # Test the black pawn's single move forward
        self.assertTrue(self.black_pawn.valid_positions(6, 4, 5, 4))
        self.assertFalse(self.black_pawn.valid_positions(6, 4, 4, 4))  
...