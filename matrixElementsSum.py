def matrixElementsSum(matrix):
    ret = 0
    for i in range(len(matrix[0])) :
        for j in range(len(matrix)) :
            if matrix[j][i] != 0 :
                ret += matrix[j][i]
            else:
                break
    return ret

print(matrixElementsSum([[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]))