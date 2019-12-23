import improperFractionToMixed

def test_case1() :
	assert improperFractionToMixed.improperFractionToMixed([7, 2]) == [3, 1, 2]

def test_case2() :
	assert improperFractionToMixed.improperFractionToMixed([10, 3]) == [3, 1, 3]

def test_case3() :
	assert improperFractionToMixed.improperFractionToMixed([23, 22]) == [1, 1, 22]

def test_case4() :
	assert improperFractionToMixed.improperFractionToMixed([18, 7]) == [2, 4, 7]
