from board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # validate coords
        if piece is None:
            raise ValueError("There is no piece in that position")
        if piece.color != self.__turn__:
            raise ValueError("It's not your turn yet")
        

        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()

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

