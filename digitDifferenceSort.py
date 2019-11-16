def digitDifferenceSort(a) :
	r=[]
	for i in a :
		r.append(max(int(x) for x in `i`) - min(int(y) for y in `i`) )
	return [w[0] for w in  (sorted( zip(a,r,range(len(a))) , key=lambda x: (x[1] ,-x[2]  ) ))]
