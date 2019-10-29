def piecesOfDistinctLengths(s):
	r = 0
	i = 1
	while r < s :
	    i+=1
	    r+=i
	return i - 1

'''
print(piecesOfDistinctLengths(14))
print(piecesOfDistinctLengths(3))
print(piecesOfDistinctLengths(4))
'''
