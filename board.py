from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

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


    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def show_board(self):
        board_piece = ""
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    board_piece += ". "  # for empty spaces
                else:
                    board_piece += piece.__str__() + " "
            board_piece += "\n"
        return board_piece

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def show_board(self):
        board_piece = ""
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    board_piece += ". "  # for empty spaces
                else:
                    board_piece += piece.__str__() + " "
            board_piece += "\n"
        return board_piece