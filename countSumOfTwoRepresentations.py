def countSumOfTwoRepresentations(n,l,r) :
	c=0
	for i in range(l,r+1) :
		if n-i >= i :
			c += (n-i <= r)
	return c

print(countSumOfTwoRepresentations(24,8,16))

		
