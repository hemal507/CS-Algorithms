import isSmooth

def test_case1() :
	assert isSmooth.isSmooth([7, 2, 2, 5, 10, 7]) == True

def test_case2() :
        assert isSmooth.isSmooth([-5, -5, 10]) == False

def test_case3() :
        assert isSmooth.isSmooth([4, 2]) == False

def test_case4() :
        assert isSmooth.isSmooth([45, 23, 12, 33, 12, 453, -234, -45]) == False

def test_case5() :
        assert isSmooth.isSmooth([-12, 34, 40, -5, -12, 4, 0, 0, -12]) == True

def test_case6() :
        assert isSmooth.isSmooth([-6, 6, -6]) == False


