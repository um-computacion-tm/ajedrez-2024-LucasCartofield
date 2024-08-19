from piece import Piece


class King(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♕"  # white king symbol
        elif self.__color__ == "BLACK":
            return "♛"  # black king symbol