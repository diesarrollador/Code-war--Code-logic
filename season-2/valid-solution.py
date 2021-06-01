"""Escribe una función que acepta una matriz 2D que representa un tablero de Sudoku
y devuelve verdadero si es una solución válida, o falso
en caso contrario. Las celdas del tablero de sudoku también
pueden contener ceros, que representarán celdas vacías.
Los tableros que contienen uno o más ceros se consideran soluciones inválidas."""
def valid_solution(board):
    if len(board) != 9 : return False
    for fila in board:
        if len(set(fila)) != 9 or sum(set(fila)) != 45 or 0 in fila : return False
    cont, lista = 0, list()
    columna = list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
    for i in columna:
        if len(set(i)) != 9 or sum(set(i)) != 45:
            cont += 1
    if cont > 0 : return False
    
    # Obtiene las submatrices 3 x 3 
    for i in range(3):
        for j in range(3):
            lista.extend(sum([fila[i*3 : (i+1)*3] for fila in board[j*3 : (j+1)*3]], []))
            if len(set(lista)) != 9 or sum(set(lista)) != 45 : return False 
            return True

# TEST CASES
print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]))  # Output True

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]
]))  # Output False
