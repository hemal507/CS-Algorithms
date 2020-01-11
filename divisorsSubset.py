def divisorsSubset(subset, n):
	return sum([all([i%j == 0 for j in subset]) for i in range(1,n+1) ])
print(divisorsSubset([2,3],13))        

