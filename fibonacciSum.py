def fibonacciSum(n):
    i = [1]
    j = 2
    r=[]
    while j <= n :
	i.insert(0,j)
	j += i[1]
    for f in i:
        if f <= n:
            r.insert(0,f)
            n -= f
    return r

#print(fibonacciSum(20))
