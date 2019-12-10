'''
def countInversionsNaive(inputArray):
	r = 0 
	for i in range(len(inputArray)) :
		for j in range(i+1,len(inputArray)) :
			r+= inputArray[i] > inputArray[j]
	return r
'''
def countInversionsNaive(A) :
	return sum([A[x]>A[y] for x in range(len(A)) for y in range(x+1,len(A))])

print(countInversionsNaive([1, 3, 2, 0]))

