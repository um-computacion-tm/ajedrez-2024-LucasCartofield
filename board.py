from rook import Rook


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White

    def show_board(self):
        board_piece = ""
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    board_piece += ". "  # for empty spaces
                else:
                    board_piece += piece.get_unicode_symbol() + " "
            board_piece += "\n"
        return board_piece