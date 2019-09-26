import correctLineup

def test_case1() :
	assert correctLineup.correctLineup([1, 2, 3, 4, 5, 6]) == [2, 1, 4, 3, 6, 5]

def test_case2() :
        assert correctLineup.correctLineup([13, 42]) == [42, 13]

def test_case3() :
        assert correctLineup.correctLineup([2, 3, 1, 100, 99, 45, 22, 28]) == [3, 2, 100, 1, 45, 99, 28, 22]

def test_case4() :
        assert correctLineup.correctLineup([85, 32, 45, 67, 32, 12, 45, 67]) == [32, 85, 67, 45, 12, 32, 67, 45]

def test_case5() :
        assert correctLineup.correctLineup([60, 2, 24, 40]) == [2, 60, 40, 24]
