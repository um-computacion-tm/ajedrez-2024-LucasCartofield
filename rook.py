from piece import Piece


class Rook(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♖"  # white rook symbol
        elif self.__color__ == "BLACK":
            return "♜"  # black rook symbol
