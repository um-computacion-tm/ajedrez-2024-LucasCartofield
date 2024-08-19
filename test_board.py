import unittest
from rook import Rook
from board import Board

class TestBoard(unittest.TestCase):
    
    def test_initial_positions(self):
        board = Board()

        # Testing the black rooks' initial positions
        self.assertIsInstance(board.get_piece(0, 0), Rook)      #assertIsInstance checks if the object is an instance of the 'rook' class
        self.assertEqual(board.get_piece(0, 0).__color__, "BLACK")  #asserEqual checks that the rook in this specific position is the correct color
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).__color__, "BLACK")
        
        # Testing the white rooks' initial positions
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).__color__, "WHITE")
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).__color__, "WHITE")

        # Testing that the remaining board positions are empty (None)
        for row in range(8):
            for col in range(8):
                if (row, col) not in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                    self.assertIsNone(board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()
