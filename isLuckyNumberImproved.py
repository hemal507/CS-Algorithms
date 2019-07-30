def isLucky_improved(n) :
	s = map(int,str(n))
	return sum(e - s.pop() for e in s)  == 0

