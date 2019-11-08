def swapNeighbouringDigits(a) :
	return int(''.join([x[1]+x[0] for x in [`a`[i*2:(i+1)*2] for i in range(len(`a`) / 2 )] ]))
	
