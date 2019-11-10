def isSum(value):
	return bool(([i for i in range(100) if sum(range(i)) == value]+[0])[0])

print(isSum(10))
