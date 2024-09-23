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
            self.__positions__[0][0] = Rook("BLACK", self) # Black
            self.__positions__[0][7] = Rook("BLACK", self) # Black
            self.__positions__[7][7] = Rook("WHITE", self) # White
            self.__positions__[7][0] = Rook("WHITE", self) # White

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
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

        # Check if the moved piece is a pawn
        if isinstance(origin, Pawn):
            # Check if the pawn reached the last row (row 0 for white, row 7 for black)
            if (origin.get_color() == "WHITE" and to_row == 0) or (origin.get_color() == "BLACK" and to_row == 7):
                # Promote the pawn to a queen
                promoted_piece = Queen(origin.get_color(), self)
                self.set_piece(to_row, to_col, promoted_piece)
                print(f"Pawn at ({to_row}, {to_col}) promoted to Queen.")