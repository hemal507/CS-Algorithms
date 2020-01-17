def numbersGrouping(a) :
    rd = dict()
    for i in a :
        v = (i-1) // 10000
        rd[v] = rd.get(v,1) + 1
    return len(rd) + len(a)

#print(numbersGrouping( [20000, 239, 10001, 999999, 10000, 20566, 29999]   ))

