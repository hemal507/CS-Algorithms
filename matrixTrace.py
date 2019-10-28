def matrixTrace(a):
    return sum([a[x][x] for x in range(len(a)) ])

print(matrixTrace([[1, 1, 1], [0, 5, 0], [2, 1, 3]]))
