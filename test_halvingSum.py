import halvingSum

def test_case1() :
	assert halvingSum.halvingSum(25) == 47

def test_case2() :
        assert halvingSum.halvingSum(127) == 247

def test_case3() :
        assert halvingSum.halvingSum(1000) == 1994

def test_case4() :
        assert halvingSum.halvingSum(1) == 1

def test_case5() :
        assert halvingSum.halvingSum(100) == 197

def test_case6() :
        assert halvingSum.halvingSum(512) == 1023

