import numpy as np
import exact_cover

DTYPE = exact_cover.io.DTYPE_FOR_ARRAY

RAW_SHAPES = {
    "F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    "I": [[1, 1, 1, 1, 1]],
    "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
    "P": [[1, 1, 1], [1, 1, 0]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 1, 1], [1, 0, 1]],
    "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}

PENTOMINOS = [np.array(shape, dtype=DTYPE) for shape in RAW_SHAPES.values()]


BOARD_3_20 = np.zeros((3, 20), dtype=DTYPE)


# Fonction pour calculer toutes les translations possibles d'une pièce sur un plateau
def compute_all_translations(piece, board):
    piece_height, piece_width = piece.shape
    board_height, board_width = board.shape
    translations = []

    # Parcourir chaque position possible sur le plateau
    for row in range(board_height - piece_height + 1):
        for col in range(board_width - piece_width + 1):
            # Extrait une sous-matrice du plateau de la taille de la pièce
            sub_board = board[row:row + piece_height, col:col + piece_width]
            
            # Vérifier si la pièce peut être placée sans recouvrir d'obstacles
            if np.all((piece == 1) & (sub_board == 0)):
                translations.append((row, col))

    return translations

