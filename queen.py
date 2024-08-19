from piece import Piece


class Queen(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♔"  # white queen symbol
        elif self.__color__ == "BLACK":
            return "♚"  # black queen symbol