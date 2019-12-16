import maxDigit

def test_case1() :
	assert maxDigit.maxDigit(111) == 1

def test_case2():
	assert maxDigit.maxDigit(132) == 3

def test_case3() :
	assert maxDigit.maxDigit(0) == 0
