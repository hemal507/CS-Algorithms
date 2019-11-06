def divNumber(k, l, r):
    t = 0
    for i in range(l,r+1) :
	t +=  len([x for x in range(1,i+1) if i % x == 0]) == k
    return t            

