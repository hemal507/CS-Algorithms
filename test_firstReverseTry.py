import firstReverseTry

def test_case1() :
	assert firstReverseTry.firstReverseTry([1,2,3,4,5]) == [5,2,3,4,1]

def test_case2() :
	assert firstReverseTry.firstReverseTry([]) == []

def test_case3() :
	assert firstReverseTry.firstReverseTry([123]) == [123]

def test_case4() :
	assert firstReverseTry.firstReverseTry([-1,1]) == [1,-1]

def test_case5() :
	assert firstReverseTry.firstReverseTry([23, 54, 12, 3, 4, 56, 23, 12, 5, 324]) == [324, 54, 12, 3, 4, 56, 23, 12, 5, 23]
