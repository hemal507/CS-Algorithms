def isSumOfConsecutive2(n):
	r=0
	for i in range(1,n) :
		s,l = n,i
		while s > 0 :
			s -= l
			l += 1
		if s == 0 :
			r += 1
	return r
			
