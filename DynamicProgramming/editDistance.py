def editDistance(s, t):
    x = len(s)
    y = len(t)
    r = [[None for i in range(y + 1)] for j in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0:
                r[i][j] = j
            elif j == 0:
                r[i][j] = i
            elif s[i-1] == t[j-1]:
                r[i][j] = r[i - 1][j - 1]
            else:
                r[i][j] = 1 + min(r[i][j - 1], r[i - 1][j], r[i - 1][j - 1])
    return r[x][y]


print(editDistance('CART', 'MATCH'))
