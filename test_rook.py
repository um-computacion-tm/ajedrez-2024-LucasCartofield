import unittest
from rook import Rook
from board import Board
from pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 1, direction='vertical_down')
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 1, direction='vertical_up')
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions(4, 1, direction='vertical_down')
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions(4, 1, direction='vertical_down')
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_horizontal_right(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 1, direction='horizontal_right')
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 4, direction='horizontal_left')
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_invalid_diagonal_move(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 0, rook)
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )
        self.assertFalse(is_possible)

if __name__ == "__main__":
    unittest.main()





'''import unittest
from rook import Rook
from board import Board
from pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        board.clear_board()  #clear the board

        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        board.clear_board() 

        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook) #sets the rook at the coordinates (4, 1)

        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
   import unittest
from rook import Rook
from board import Board
from pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 1, direction='vertical_down')
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 1, direction='vertical_up')
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions(4, 1, direction='vertical_down')
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions(4, 1, direction='vertical_down')
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_horizontal_right(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 1, direction='horizontal_right')
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions(4, 4, direction='horizontal_left')
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_invalid_diagonal_move(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 0, rook)
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )
        self.assertFalse(is_possible)

if __name__ == "__main__":
    unittest.main()     )
        
if __name__ == '__main__':
    unittest.main()

    #parametros...
    #[el tablero]
    #[el lugar de la torre]
    #[el lugar a donde quiere llegar]
    #verificar...'''