def divNumber(k, l, r):
    t = 0
    for i in range(l,r+1) :
	t +=  len([x for x in range(1,i+1) if i % x == 0]) == k
    return t    

def divNumber(k, l, r):
    g=range
    return sum([sum([i % x == 0 for x in g(1,i+1)]) == k  for i in g(l,r+1)])
