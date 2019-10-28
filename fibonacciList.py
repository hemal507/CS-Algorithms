def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x, y: x+[x[-2]+x[-1]], range(n-2), [0, 1])]

