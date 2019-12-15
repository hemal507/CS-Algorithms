import checkIncreasingSequence

def test_case1() :
	assert checkIncreasingSequence.checkIncreasingSequence([1, 3, 8]) == True

def test_case2() :
        assert checkIncreasingSequence.checkIncreasingSequence([2, 2, 3]) == False

def test_case3() :
        assert checkIncreasingSequence.checkIncreasingSequence([2, 2]) == False

def test_case4() :
        assert checkIncreasingSequence.checkIncreasingSequence([1, 2, 4, 6, 11]) == True

def test_case5() :
        assert checkIncreasingSequence.checkIncreasingSequence([1, 3, 1, 2, 3]) == False

def test_case6() :
        assert checkIncreasingSequence.checkIncreasingSequence([9]) == True

