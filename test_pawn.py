import unittest
from pawn import Pawn
from board import Board


class TestPawn(unittest.TestCase):

    def test_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )

    def test_not_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_eat_left_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 6)]
        )

    def test_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

    def test_not_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4)]
        )

    def test_not_initial_white_block(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_not_initial_black_block(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(5, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(4, 4)
        self.assertEqual(
            possibles,
            []
        )

'''import unittest
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
        self.assertFalse(self.black_pawn.valid_positions(6, 4, 4, 4))'''  
...