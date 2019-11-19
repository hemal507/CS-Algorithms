def crossingSum(x, a, b):
        return sum( x[a] + [x[y][b] for y in range(len(x)) if y != a] )


