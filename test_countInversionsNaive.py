import countInversionsNaive

def test_case1() :
	assert countInversionsNaive.countInversionsNaive( [1, 3, 2, 0]) == 4

def test_case2() :
        assert countInversionsNaive.countInversionsNaive( [1, 4, 10, 4, 2]) == 4

def test_case3() :
        assert countInversionsNaive.countInversionsNaive([1, 2, 3, 4, 5]) == 0

def test_case4() :
        assert countInversionsNaive.countInversionsNaive([5, 4, 3, 2, 1]) == 10

def test_case5() :
        assert countInversionsNaive.countInversionsNaive([-1, -2, 3, -4, 5]) == 4
