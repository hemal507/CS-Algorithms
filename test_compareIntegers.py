import compareIntegers

def test_case1() :
	assert compareIntegers.compareIntegers("12","13") == "less"

def test_case2() :
        assert compareIntegers.compareIntegers("875","799") == "greater"

def test_case3() :
        assert compareIntegers.compareIntegers("1000","1000") == "equal"

def test_case4() :
        assert compareIntegers.compareIntegers("1010","999") == "greater"

def test_case5() :
        assert compareIntegers.compareIntegers("49","500") == "less"
