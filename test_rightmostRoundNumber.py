import rightmostRoundNumber

def test_case1() :
	assert rightmostRoundNumber.rightmostRoundNumber([0, 5, 10, 15]) == 2

def test_case2() :
        assert rightmostRoundNumber.rightmostRoundNumber([1, 2, 3, 4, 5]) == -1

def test_case3() :
        assert rightmostRoundNumber.rightmostRoundNumber([100000]) == 0

def test_case4() :
        assert rightmostRoundNumber.rightmostRoundNumber([1, 2, 3, 5, 6]) == -1

def test_case5() :
        assert rightmostRoundNumber.rightmostRoundNumber([10, 0]) == 1
