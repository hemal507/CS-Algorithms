import kthDigit

def test_case1() :
	assert kthDigit.kthDigit(578943,2) == 7

def test_case2() :
        assert kthDigit.kthDigit(786543,1) == 7

def test_case3() :
        assert kthDigit.kthDigit(786543,2) == 8

def test_case4() :
        assert kthDigit.kthDigit(786543,6) == 3

def test_case5() :
        assert kthDigit.kthDigit(786543,7) == -1

