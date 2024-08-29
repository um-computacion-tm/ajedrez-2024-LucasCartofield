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
        self.__positions__[0][0] = Rook("BLACK", self) # Black
        self.__positions__[0][7] = Rook("BLACK", self) # Black
        self.__positions__[7][7] = Rook("WHITE", self) # White
        self.__positions__[7][0] = Rook("WHITE", self) # White
        self.__positions__[0][1] = Knight("BLACK", self) # Black
        self.__positions__[0][6] = Knight("BLACK", self) # Black
        self.__positions__[7][1] = Knight("WHITE", self) # White
        self.__positions__[7][6] = Knight("WHITE", self) # White
        self.__positions__[0][2] = Bishop("BLACK", self) # Black
        self.__positions__[0][5] = Bishop("BLACK", self) # Black
        self.__positions__[7][5] = Bishop("WHITE", self) # White
        self.__positions__[7][2] = Bishop("WHITE", self) # White
        self.__positions__[0][3] = King("BLACK", self) # Black
        self.__positions__[7][3] = King("WHITE", self) # White        
        self.__positions__[0][4] = Queen("BLACK", self) # Black
        self.__positions__[7][4] = Queen("WHITE", self) # White
        self.__positions__[1][0] = Pawn("BLACK", self) # Black
        self.__positions__[1][1] = Pawn("BLACK", self) # Black
        self.__positions__[1][2] = Pawn("BLACK", self) # White
        self.__positions__[1][3] = Pawn("BLACK", self) # White
        self.__positions__[1][4] = Pawn("BLACK", self) # Black
        self.__positions__[1][5] = Pawn("BLACK", self) # Black
        self.__positions__[1][6] = Pawn("BLACK", self) # White
        self.__positions__[1][7] = Pawn("BLACK", self) # White
        self.__positions__[6][0] = Pawn("WHITE", self) # Black
        self.__positions__[6][1] = Pawn("WHITE", self) # Black
        self.__positions__[6][2] = Pawn("WHITE", self) # White
        self.__positions__[6][3] = Pawn("WHITE", self) # White
        self.__positions__[6][4] = Pawn("WHITE", self) # Black
        self.__positions__[6][5] = Pawn("WHITE", self) # Black
        self.__positions__[6][6] = Pawn("WHITE", self) # White
        self.__positions__[6][7] = Pawn("WHITE", self) # White

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