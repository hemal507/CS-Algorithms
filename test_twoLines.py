import twoLines

def test_case1() :
	assert twoLines.twoLines([1, 2], [2, 1], 0, 2) == "any"

def test_case2() :
        assert twoLines.twoLines([1, 2], [2, 1], -1, 2) == "first"

def test_case3() :
        assert twoLines.twoLines([1, 2], [2, 1], 0, 3) == "second"

def test_case4() :
        assert twoLines.twoLines([1, 2], [1, 0], -1000, 1000) == "first"

def test_case5() :
        assert twoLines.twoLines([1, 0], [-1, 0], -239, 239) == "any"

def test_case6() :
        assert twoLines.twoLines([1, 0], [-1, 0], -999, 998) == "second"
