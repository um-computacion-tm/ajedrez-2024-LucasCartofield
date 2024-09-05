from board import Board
from exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()


        #check if the final place has a piece of the same color as the player
        destination = self.__board__.get_piece(to_row, to_col)
        if destination is not None and destination.get_color() == self.__turn__:
            raise ValueError("Cannot move to a position occupied by your own piece")

        #check if the move is legal (within bounds)
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Move is out of bounds")

    def show_board(self):
        return str(self.__board__)
    
    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
