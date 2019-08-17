import arrayPreviousLess

def test_case1() :
	assert arrayPreviousLess.arrayPreviousLess([3, 2, 1]) == [-1,-1,-1]


def test_case2() :
        assert arrayPreviousLess.arrayPreviousLess([7, 7, 8, 3, 4, 4, 2, 5, 6, 7, 7]) == [-1, -1, 7, -1, 3, 3, -1, 2, 5, 6, 6]
