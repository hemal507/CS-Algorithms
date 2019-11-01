import divisorsPairs

def test_case1() :
	assert divisorsPairs.divisorsPairs([1, 3, 2]) == 2

def test_case2() :
	assert divisorsPairs.divisorsPairs([2, 4, 8]) == 3 

def test_case3() :
	assert divisorsPairs.divisorsPairs([42]) == 0 
