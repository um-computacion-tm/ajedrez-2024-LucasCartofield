from piece import Piece


class Pawn(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♙"  # white pawn symbol
        elif self.__color__ == "BLACK":
            return "♟"  # black pawn symbol