"""Escribe una función que acepta una matriz 2D que representa un tablero de Sudoku
y devuelve verdadero si es una solución válida, o falso
en caso contrario. Las celdas del tablero de sudoku también
pueden contener ceros, que representarán celdas vacías.
Los tableros que contienen uno o más ceros se consideran soluciones inválidas."""
def valid_solution(board):
    if len(board) != 9 : return False
    for fila in board:
        if len(set(fila)) != 9 or sum(set(fila)) != 45 or 0 in fila : return False
    t1 = board[0][:3] + board[1][:3] + board[2][:3]
    t2 = board[0][3:6] + board[1][3:6] + board[2][3:6]
    t3 = board[0][6:] + board[1][6:] + board[2][6:]
    t4 = board[3][:3] + board[4][:3] + board[5][:3]
    t5 = board[3][3:6] + board[4][3:6] + board[5][3:6]
    t6 = board[3][6:] + board[4][6:] + board[5][6:]
    t7 = board[6][:3] + board[7][:3] + board[8][:3]
    t8 = board[6][3:6] + board[7][3:6] + board[8][3:6]
    t9 = board[6][6:] + board[7][6:] + board[8][6:]
    cont=0
    if (len(set(t1)) == 9) or (sum(set(t1)) == 45) or (len(set(t2)) == 9) or (sum(set(t2)) == 45) or (len(set(t3)) == 9) or (sum(set(t3)) == 45) or (len(set(t4)) == 9) or (sum(set(t4)) == 45) or (len(set(t5)) == 9) or (sum(set(t5)) == 45) or (len(set(t6)) == 9) or (sum(set(t6)) == 45) or (len(set(t7)) == 9) or (sum(set(t7)) == 45) or (len(set(t8)) == 9) or (sum(set(t8)) == 45) or (len(set(t9)) == 9) or (sum(set(t9)) == 45):
        columna = list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
        for i in columna:
            if len(set(i)) != 9 or sum(set(i)) != 45:
                cont += 1
        if cont > 0 : return False
        return True
    return False

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
