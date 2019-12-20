def fractionReducing(fraction) :
	n,d=fraction
	i=2
	while i <= n or i <= d:
		if n % i == 0 and d % i == 0 :
			n/=i
			d/=i
		else :
			i+=1
	return [n,d]


print(fractionReducing([2,6]))
print(fractionReducing([1,4]))
			
