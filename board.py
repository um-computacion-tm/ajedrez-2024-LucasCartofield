from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn
from exceptions import OutOfBoard



class Board:
    def __init__(self, for_test = False):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        if not for_test:
            starting_place = {
                Rook: [("BLACK", [(0, 0), (0, 7)]), ("WHITE", [(7, 0), (7, 7)])],
                Knight: [("BLACK", [(0, 1), (0, 6)]), ("WHITE", [(7, 1), (7, 6)])],
                Bishop: [("BLACK", [(0, 2), (0, 5)]), ("WHITE", [(7, 2), (7, 5)])],
                King: [("BLACK", [(0, 3)]), ("WHITE", [(7, 3)])],
                Queen: [("BLACK", [(0, 4)]), ("WHITE", [(7, 4)])],
                Pawn: [("BLACK", [(1, i) for i in range(8)]), ("WHITE", [(6, i) for i in range(8)])],
            }

            for piece, color_positions in starting_place.items():
                for color, positions in color_positions:
                    for position in positions:
                        row, col = position
                        self.__positions__[row][col] = piece(color, self)

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    board_str += ". "  # for empty spaces
                else:
                    board_str += piece.__str__() + " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece
    
    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)