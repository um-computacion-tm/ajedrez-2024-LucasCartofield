from piece import Piece


class Rook(Piece):

    def get_unicode_symbol(self):
        if self.__color__ == "WHITE":
            return "♖"  # white rook symbol
        elif self.__color__ == "BLACK":
            return "♜"  # black rook symbol

    def is_legal_move(self, from_row, from_col, to_row, to_col, board):
        # Check if the move is vertical or horizontal
        if from_row != to_row and from_col != to_col:
            return False