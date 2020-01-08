def arrayConversion(inputArray):
	s=0
	while len(inputArray) > 1 :
		if s % 2 == 0 :
			inputArray = [x+y for x,y in zip(inputArray[:-1:2],inputArray[1::2])] 
		else :
			inputArray = [x*y for x,y in zip(inputArray[:-1:2],inputArray[1::2])]
		s += 1
	return inputArray[0]


def arrayConversion(inputArray) :
        k=0
        while len(inputArray) > 1 :
                inputArray = [ [i+j, i*j][k%2] for i,j in zip(inputArray[::2],inputArray[1::2] ) ]
                k += 1
        return inputArray[0]
