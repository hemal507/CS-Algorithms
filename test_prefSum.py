import prefSum 

def test_case1() :
	assert prefSum.prefSum([1,2,3]) == [1,3,6]

def test_case2() :
        assert prefSum.prefSum([1, 2, 3, -6]) == [1,3,6,0]

def test_case3() :
        assert prefSum.prefSum([0,0,0]) == [0,0,0]

def test_case4() :
        assert prefSum.prefSum([1, 123, 23]) == [1,124,147]

def test_case5() :
        assert prefSum.prefSum([24, -16, -46, 36, 11, -18, -44, 19]) == [24, 8, -38, -2, 9, -9, -53, -34]

