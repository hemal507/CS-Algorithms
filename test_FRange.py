import FRange

def test_case1() :
	assert FRange.rangeFloat([5]) == [0, 1, 2, 3, 4] 

def test_case2() :
        assert FRange.rangeFloat([0.5, 7.5]) == [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]

def test_case3() :
        assert FRange.rangeFloat([-1.1, 2.4, 0.3]) == [-1.1, -0.8, -0.5, -0.2, 0.1, 0.4, 0.7, 1, 1.3, 1.6, 1.9, 2.2]

def test_case4() :
        assert FRange.rangeFloat([5.6, 3.2]) == []

def test_case5() :
        assert FRange.rangeFloat( [-3.2, -123, 10]) == []

def test_case6() :
        assert FRange.rangeFloat([-4]) == []

def test_case7() :
        assert FRange.rangeFloat([10, 10, 3]) == []

def test_case8() :
        assert FRange.rangeFloat([33.3]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

def test_case9() :
        assert FRange.rangeFloat([10.4, 3.2, -1.2]) == [10.4, 9.2, 8, 6.8, 5.6, 4.4, 3.2]
