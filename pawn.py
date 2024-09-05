from piece import Piece


class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_positions(self, row, col):
        possibles = []
        direction = 1 if self.get_color() == "WHITE" else -1

        #forward movement
        next_row = row + direction
        if self.__board__.is_empty(next_row, col):
            possibles.append((next_row, col))

        #double forward movement on first turn
            if (self.get_color() == "white" and row == 1) or (self.get_color() == "black" and row == 6):
                double_row = row + 2 * direction
                if self.__board__.is_empty(double_row, col):
                    possibles.append((double_row, col))  
                    
            ...