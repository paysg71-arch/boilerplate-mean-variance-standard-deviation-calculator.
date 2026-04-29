import numpy as np

def calculate(lst):
    # Si la liste contient moins (ou plus) de 9 éléments, on lève une exception
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # On convertit la liste en une matrice Numpy de 3x3
    matrix = np.array(lst).reshape(3, 3)
    
    # On calcule les valeurs demandées
    # axis=0 correspond aux colonnes, axis=1 correspond aux lignes
    # L'appel sans 'axis' correspond à la matrice aplatie (flattened)
    # .tolist() permet de convertir les types Numpy en types natifs Python
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }
    
    return calculations
