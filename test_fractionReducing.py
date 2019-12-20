import fractionReducing

def test_case1() :
	assert fractionReducing.fractionReducing([2, 6]) == [1, 3]

def test_case2() :
	assert fractionReducing.fractionReducing([4, 1]) == [4, 1]

def test_case3() :
	assert fractionReducing.fractionReducing([5, 10]) == [1, 2]
