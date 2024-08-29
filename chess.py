from board import Board


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
        piece = self.__board__.get_piece(from_row, from_col)        
        # validate coords
        if piece is None:
            raise ValueError("There is no piece in that position")
        if piece.__color__ != self.__turn__:
            raise ValueError("It's not your turn yet")
        self.change_turn()

        #move the piece
        self.__board__.set_piece(to_row, to_col, piece)
        self.__board__.set_piece(from_row, from_col, None)

        #change player turn
        self.change_turn()

        #check if the final place has a piece of the same color as the player
        destination = self.__board__.get_piece(to_row, to_col)
        if destination is not None and destination.get_color() == self.__turn__:
            raise ValueError("Cannot move to a position occupied by your own piece")

        #check if the move is legal (within bounds)
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Move is out of bounds")

    def show_board(self):
        board_piece = self.__board__.show_board()
        return board_piece
    
    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

