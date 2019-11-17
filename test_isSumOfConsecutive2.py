import isSumOfConsecutive2

def test_case1() :
	assert isSumOfConsecutive2.isSumOfConsecutive2(9) == 2

def test_case2() :
        assert isSumOfConsecutive2.isSumOfConsecutive2(8) == 0 


def test_case3() :
        assert isSumOfConsecutive2.isSumOfConsecutive2(15) == 3


def test_case4() :
        assert isSumOfConsecutive2.isSumOfConsecutive2(24) == 1


def test_case5() :
        assert isSumOfConsecutive2.isSumOfConsecutive2(13) == 1


def test_case6() :
        assert isSumOfConsecutive2.isSumOfConsecutive2(25) == 2


def test_case7() :
        assert isSumOfConsecutive2.isSumOfConsecutive2(99) == 5

