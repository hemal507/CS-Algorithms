import arrayMaximalAdjacentDifference

def test_case1 () :
	assert arrayMaximalAdjacentDifference.arrayMaximalAdjacentDifference([2, 4, 1, 0]) == 3

def test_case2() :
        assert arrayMaximalAdjacentDifference.arrayMaximalAdjacentDifference( [1, 1, 1, 1]) == 0

def test_case3() :
        assert arrayMaximalAdjacentDifference.arrayMaximalAdjacentDifference([-1, 4, 10, 3, -2]) == 7

def test_case4() :
        assert arrayMaximalAdjacentDifference.arrayMaximalAdjacentDifference( [10, 11, 13]) == 2

def test_case5() :
        assert arrayMaximalAdjacentDifference.arrayMaximalAdjacentDifference([-2, -2, -2, -2, -2]) == 0

def test_case6() :
        assert arrayMaximalAdjacentDifference.arrayMaximalAdjacentDifference([-1, 1, -3, -4]) == 4



