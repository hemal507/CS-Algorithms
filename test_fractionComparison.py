import fractionComparison

def test_case1() :
	assert fractionComparison.fractionComparison([3, 4], [6, 8]) == '='

def test_case2() :
        assert fractionComparison.fractionComparison([3, 2], [2, 5]) == '>'

def test_case3() :
        assert fractionComparison.fractionComparison([3, 5], [2, 3]) == '<'
