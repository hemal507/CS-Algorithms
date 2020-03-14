def isDiagonalMatrix(matrix):
    l=len(matrix)
    return not (any([matrix[x][y] != 0 and x != y for x in range(l) for y in range(l)]))
    #
    # for i in range(l) :
    #     for j in range(l) :
    #         if i != j and matrix[i][j] != 0 :
    #             return False
    # return True