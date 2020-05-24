def binomialCoefficient(n, k) :
    b = [ [0 for i in range(k + 1)] for j in range(n + 1)]
    for i in range(n + 1) :
        for j in range(min(i, k) + 1) :
            if j == 0 or i == j :
                b[i][j] = 1
            else :
                b[i][j] = b[i-1][j-1] + b[i-1][j]
    #print(b)
    return b[n][k]


print(binomialCoefficient(50, 10))