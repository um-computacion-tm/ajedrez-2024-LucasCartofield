import unittest
from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn
from board import Board

class TestBoard(unittest.TestCase):

    def test_initial_positions(self):
        board = Board()

        # Testing the black rooks' initial positions
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(board.get_piece(0, 0).get_color(), "BLACK")
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).get_color(), "BLACK")
        
        # Testing the white rooks' initial positions
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).get_color(), "WHITE")
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).get_color(), "WHITE")

        # Testing the black knights' initial positions
        self.assertIsInstance(board.get_piece(0, 1), Knight)
        self.assertEqual(board.get_piece(0, 1).get_color(), "BLACK")
        self.assertIsInstance(board.get_piece(0, 6), Knight)
        self.assertEqual(board.get_piece(0, 6).get_color(), "BLACK")

        # Testing the white knights' initial positions
        self.assertIsInstance(board.get_piece(7, 1), Knight)
        self.assertEqual(board.get_piece(7, 1).get_color(), "WHITE")
        self.assertIsInstance(board.get_piece(7, 6), Knight)
        self.assertEqual(board.get_piece(7, 6).get_color(), "WHITE")

        # Testing the black bishops' initial positions
        self.assertIsInstance(board.get_piece(0, 2), Bishop)
        self.assertEqual(board.get_piece(0, 2).get_color(), "BLACK")
        self.assertIsInstance(board.get_piece(0, 5), Bishop)
        self.assertEqual(board.get_piece(0, 5).get_color(), "BLACK")

        # Testing the white bishops' initial positions
        self.assertIsInstance(board.get_piece(7, 2), Bishop)
        self.assertEqual(board.get_piece(7, 2).get_color(), "WHITE")
        self.assertIsInstance(board.get_piece(7, 5), Bishop)
        self.assertEqual(board.get_piece(7, 5).get_color(), "WHITE")

        # Testing the black king's initial position
        self.assertIsInstance(board.get_piece(0, 3), King)
        self.assertEqual(board.get_piece(0, 3).get_color(), "BLACK")

        # Testing the white king's initial position
        self.assertIsInstance(board.get_piece(7, 3), King)
        self.assertEqual(board.get_piece(7, 3).get_color(), "WHITE")

        # Testing the black queen's initial position
        self.assertIsInstance(board.get_piece(0, 4), Queen)
        self.assertEqual(board.get_piece(0, 4).get_color(), "BLACK")

        # Testing the white queen's initial position
        self.assertIsInstance(board.get_piece(7, 4), Queen)
        self.assertEqual(board.get_piece(7, 4).get_color(), "WHITE")

        # Testing the black pawns' initial positions
        for col in range(8):
            self.assertIsInstance(board.get_piece(1, col), Pawn)
            self.assertEqual(board.get_piece(1, col).get_color(), "BLACK")

        # Testing the white pawns' initial positions
        for col in range(8):
            self.assertIsInstance(board.get_piece(6, col), Pawn)
            self.assertEqual(board.get_piece(6, col).get_color(), "WHITE")

        # Testing that the remaining board positions are empty (None)
        occupied_positions = [(0, i) for i in range(8)] + [(1, i) for i in range(8)] + \
                             [(7, i) for i in range(8)] + [(6, i) for i in range(8)]
        for row in range(8):
            for col in range(8):
                if (row, col) not in occupied_positions:
                    self.assertIsNone(board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()