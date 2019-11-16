def digitDifferenceSort(a) :
	r=[]
	for i in a :
		r.append(max(int(x) for x in `i`) - min(int(y) for y in `i`) )
	return [w[0] for w in  (sorted( zip(a,r,range(len(a))) , key=lambda x: (x[1] ,-x[2]  ) ))]

print(digitDifferenceSort([152, 23, 7, 887, 243]))
print(digitDifferenceSort([]))
print(digitDifferenceSort( [561, 798, 132, 339, 218, 724, 462, 332, 9, 343, 592, 34, 95, 292, 626, 970]))
print(digitDifferenceSort([8, 76, 7, 26, 7, 60, 87, 77, 72, 61, 13, 60, 8, 32, 48, 63, 82, 56, 17, 18, 28, 85, 95, 69, 95]))
print(digitDifferenceSort([714, 13, 804, 419, 97, 850, 440, 215, 836, 408, 743, 131, 364, 846, 80, 403, 720, 618, 118, 892, 711, 682, 427, 949, 624]))
print(digitDifferenceSort([13098, 1308, 12398, 52433, 213, 424, 213, 243, 12213, 54234, 99487, 81892, 1, 97897]))

