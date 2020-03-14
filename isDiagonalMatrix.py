def isDiagonalMatrix(matrix):
    l=len(matrix)
    for i in range(l) :
        for j in range(l) :
            if i != j and matrix[i][j] != 0 :
                return False
    return True