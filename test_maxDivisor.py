import maxDivisor

def test_case1() :
	assert maxDivisor.maxDivisor(1,10,3) == 9

def test_case2() :
	assert maxDivisor.maxDivisor(6,7,2) == 6

def test_case3() :
	assert maxDivisor.maxDivisor(-99,-96,5) == -1

