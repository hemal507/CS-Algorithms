def maxSubarray(A) :
	a=b=0
	for x in A:
	    a = max(x, a+x)
	    b = max(a, b)
	return b


#print(maxSubarray([-1, 7, -2, 3, 4, 0, 1, -1]))
print(maxSubarray( [1, -1, 2, 3, -1]))
