def magicalWell(a, b, n) :
	return sum([ (a+i)*(b+i) for i in range(n)  ])

magicalWell = lambda a,b,n : sum( (a+i)*(b+i) for i in range(n) )
