import leastCommonDenominator

def test_case1() :
	assert leastCommonDenominator.leastCommonDenominator([2, 3, 4, 5, 6]) == 60

def test_case2() :
        assert leastCommonDenominator.leastCommonDenominator([34, 6, 3, 5, 3]) == 510

def test_case3() :
        assert leastCommonDenominator.leastCommonDenominator([49, 23, 15, 20, 2, 42, 21, 34]) == 1149540

def test_case4() :
        assert leastCommonDenominator.leastCommonDenominator([2]) == 2

