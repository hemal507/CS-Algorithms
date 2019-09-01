import maxSumSegments

def test_case1() :
	assert maxSumSegments.maxSumSegments([3, -3, 2, 2, 1, -5, 0]) == [0, 2, 2, 0, 0, 0, 0]

def test_case2() :
	assert maxSumSegments.maxSumSegments([-1, -1, -1, -1]) ==   [0, 0, 0, 0]

def test_case3() :
	assert maxSumSegments.maxSumSegments([-1, 2, 1, 3, -2]) == [3, 2, 1, 0, 0]
