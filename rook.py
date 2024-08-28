from piece import Piece


class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

def possible_positions_vd(self, row, col):
    #la columna es igual, recorrer las filas
    possibles = []
    #range(inicio, fin que no esta incluido)
    for next_row in range(row + 1, 8):
        possibles.append((next_row, col))
    return possibles

def possible_positions_va(self, row, col):
    possibles = []
    for next_row in range(row - 1, -1, -1):
        possibles.append((next_row, col))
    return possibles