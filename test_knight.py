import unittest
from knight import Knight

class TestKnightMoves(unittest.TestCase):

    def test_knight_moves_edge(self):
        #Test knight's moves from the edge of the board (0, 0)
        knight = Knight()
        start_position = (0, 0)
        expected_moves = [(2, 1), (1, 2)]
        self.assertCountEqual(knight.knight_moves(start_position), expected_moves)

    def test_knight_moves_corner(self):
        #Test knight's moves from the corner of the board (7, 7)
        knight = Knight()
        start_position = (7, 7)
        expected_moves = [(5, 6), (6, 5)]
        self.assertCountEqual(knight.knight_moves(start_position), expected_moves)

    def test_knight_moves_invalid_position(self):
        ...

if __name__ == "__main__":
    unittest.main()