def specialPolynomial(x,n) :
	c=0
	for i in range(1000) :
		c += pow(x,i)
		print(c , ' : ',i)
		if c > n :
			return i-1

print(specialPolynomial(1,100))

