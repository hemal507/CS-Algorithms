def arrayMaximalAdjacentDifference(a) :
	return max( [abs(x-y) for x,y in zip(a[:-1],a[1:]) ]   )

print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))
