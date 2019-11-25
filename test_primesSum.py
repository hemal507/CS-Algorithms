import primesSum

def test_case1() :
	assert primesSum.primesSum(10, 20) == 60

def test_case2() :
        assert primesSum.primesSum(1, 7) == 17

def test_case3() :
        assert primesSum.primesSum(5, 10) == 12

def test_case4() :
        assert primesSum.primesSum(24, 28) == 0

def test_case5() :
        assert primesSum.primesSum(13, 13) == 13


