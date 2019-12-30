def reverseToSort(a):
	l=len(a)
	for i in range(l-1) :
		for j in range(i+1, l+1) :
			s = a[i:j]
 			if sorted(a) == a[:i] + s[::-1] + a[j:] :
				return len(set(a)) == len(a)

	return False
print(reverseToSort([-1, 5,4,3,2,8]))    
print(reverseToSort([1, 3, 2, 5, 4, 6]))


