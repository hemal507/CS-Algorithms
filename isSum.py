def isSum(value):
	#return bool(([i for i in range(100) if sum(range(i)) == value]+[0])[0])
	r=0
	a=1
	while value > r :
		r+= a
		a+=1
	return value == r
print(isSum(10))
