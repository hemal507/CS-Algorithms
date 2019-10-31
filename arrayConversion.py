def arrayConversion(inputArray):
	s=0
	while len(inputArray) > 1 :
		if s % 2 == 0 :
			inputArray = [x+y for x,y in zip(inputArray[:-1:2],inputArray[1::2])] 
		else :
			inputArray = [x*y for x,y in zip(inputArray[:-1:2],inputArray[1::2])]
		s += 1
	return inputArray[0]

