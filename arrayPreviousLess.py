def arrayPreviousLess(n) :
	r=[]
	for i in range(len(n)) :
		k=-1
		for j in range(i) :
			if n[j] < n[i] :
				k=n[j]
		r.append(k)
	return r

print(arrayPreviousLess([3,5,2,4,5]))
print(arrayPreviousLess([7,   7, 8,  3, 4, 4,  2, 5, 6, 7, 7]))

'''

[3,  5,  2, 4, 5]
[-1, 3, -1, 2, 4]

[2,   2,  1, 3, 4, 5, 5, 3]
[-1, -1, -1, 1, 3, 4, 4, 1]

[3,   2,  1]
[-1, -1, -1]


[3,  5,  2, 4, 5]
[-1, 3, -1, 2, 4]


[100, 101, 102]
[-1 , 100, 101]

[7,   7, 8,  3, 4, 4,  2, 5, 6, 7, 7]
[-1, -1, 7, -1, 3, 3, -1, 2, 5, 6, 6]
'''


