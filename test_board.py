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

        # Expected positions for each type of piece
        starting_positions = {
            Rook: [("BLACK", [(0, 0), (0, 7)]), ("WHITE", [(7, 0), (7, 7)])],
            Knight: [("BLACK", [(0, 1), (0, 6)]), ("WHITE", [(7, 1), (7, 6)])],
            Bishop: [("BLACK", [(0, 2), (0, 5)]), ("WHITE", [(7, 2), (7, 5)])],
            King: [("BLACK", [(0, 3)]), ("WHITE", [(7, 3)])],
            Queen: [("BLACK", [(0, 4)]), ("WHITE", [(7, 4)])],
            Pawn: [("BLACK", [(1, i) for i in range(8)]), ("WHITE", [(6, i) for i in range(8)])],
        }

        # Test each piece's initial positions on the board
        for piece, color_positions in starting_positions.items():
            for color, positions in color_positions:
                for row, col in positions:
                    piece_instance = board.get_piece(row, col)
                    self.assertIsInstance(piece_instance, piece)
                    self.assertEqual(piece_instance.get_color(), color)

        # Test that all other positions are empty
        occupied_positions = {pos for positions in starting_positions.values() for _, pos_list in positions for pos in pos_list}
        for row in range(8):
            for col in range(8):
                if (row, col) not in occupied_positions:
                    self.assertIsNone(board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()