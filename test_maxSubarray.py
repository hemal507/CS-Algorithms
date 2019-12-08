import maxSubarray

def test_case1() :
	assert maxSubarray.maxSubarray([-1, 7, -2, 3, 4, 0, 1, -1]) == 13

def test_case2() :
	assert maxSubarray.maxSubarray([-1, -2, -5, -1]) == 0

def test_case3() :
	assert maxSubarray.maxSubarray([1, -1, 2, 3, -1]) == 5

