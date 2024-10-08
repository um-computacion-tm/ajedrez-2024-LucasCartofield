from piece import Piece

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles
    
    def possible_positions_hr(self, row, col):
        #horizontal right: moves right across the board increasing column index
        possibles = []
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles

    def possible_positions_hl(self, row, col):
        #horizontal left: moves left across the board decreasing column index
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles