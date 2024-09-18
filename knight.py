from piece import Piece


class Knight(Piece):
    white_str = "♞"
    black_str = "♘"

    
def knight_moves(position):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    row, col = position
    
    valid_moves = []
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            valid_moves.append((new_row, new_col))
    
    return valid_moves