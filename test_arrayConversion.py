import  arrayConversion

def test_case1() :
	assert arrayConversion.arrayConversion([1, 2, 3, 4, 5, 6, 7, 8]) == 186

def test_case2() :
        assert arrayConversion.arrayConversion([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 64

def test_case3() :
        assert arrayConversion.arrayConversion([3, 3, 5, 5]) == 60

def test_case4() :
        assert arrayConversion.arrayConversion([-1, 1, 2, 3, 5, 5, 3, 7]) == 100

def test_case5() :
        assert arrayConversion.arrayConversion([99]) == 99

def test_case6() :
        assert arrayConversion.arrayConversion([99, 1]) == 100

def test_case7() :
        assert arrayConversion.arrayConversion([34, 60, -9, -67, -100, -27, 100, 21]) == -22511
