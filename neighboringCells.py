def neighboringCells(a):
        g = range
        l = len
        r = l(a)-1
        for i in g(r+1) :
                c = l(a[i])-1
                for j in g(c+1) :
                        a[i][j] = (i > 0) + (i < r)  + (j > 0) + (j < c)
        return a
    

