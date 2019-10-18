import checkEqualFrequency

def test_case1() :
	assert checkEqualFrequency.checkEqualFrequency([1, 2, 2, 1]) == True

def test_case2() :
        assert checkEqualFrequency.checkEqualFrequency([1, 2, 2, 3, 1, 3, 1, 3]) == False

def test_case3() :
        assert checkEqualFrequency.checkEqualFrequency([239]) == True

def test_case4() :
        assert checkEqualFrequency.checkEqualFrequency([239, 240, 241]) == True

def test_case5() :
        assert checkEqualFrequency.checkEqualFrequency([1, 1, 1, 1, 1]) == True

def test_case6() :
        assert checkEqualFrequency.checkEqualFrequency( [100000000, 400000000, 200000000, 400000000, 200000000, 100000000]) == True

