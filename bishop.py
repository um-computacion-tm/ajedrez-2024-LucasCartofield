from piece import Piece


class Bishop(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♗"  # white bishop symbol
        elif self.__color__ == "BLACK":
            return "♝"  # black bishop symbol