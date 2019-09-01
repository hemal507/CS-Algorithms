def maxSumSegments(inputArray):
	segments=[]
	for i in range(len(inputArray)) :
		maxSum,position=0,0
		for j in range(len(inputArray)-i) :
			s=sum(inputArray[j:j+i+1])
			if s > maxSum :
				maxSum=s
				position=j	
		segments.append(position)
	return segments
   

print(maxSumSegments([-1,2,1,3,-1]))
