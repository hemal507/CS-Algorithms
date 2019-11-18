'''
def rightmostRoundNumber(inputArray):
    for i in inputArray[::-1] :
        if i % 10 ==  0 :
            return inputArray.index(i)
    return -1
'''

def rightmostRoundNumber(i) :
	return ([i.index(x) for x in i[::-1] if x %10 == 0    ] + [-1] )[0]
        
print(rightmostRoundNumber([1,2,30,4,5,6,90,8454,6,876,2342,435]))

