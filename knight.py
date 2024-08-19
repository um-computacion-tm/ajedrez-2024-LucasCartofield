from piece import Piece


class Knight(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♘"  # white knight symbol
        elif self.__color__ == "BLACK":
            return "♞"  # black knight symbol