import replaceMiddle

def test_case1() :
	assert replaceMiddle.replaceMiddle([7, 2, 2, 5, 10, 7]) == [7, 2, 7, 10, 7]

def test_case2() :
        assert replaceMiddle.replaceMiddle([-5, -5, 10]) == [-5, -5, 10]

def test_case3() :
        assert replaceMiddle.replaceMiddle([45, 23, 12, 33, 12, 453, -234, -45]) == [45, 23, 12, 45, 453, -234, -45]

def test_case4() :
        assert replaceMiddle.replaceMiddle( [2, 8]) == [10]

def test_case5() :
        assert replaceMiddle.replaceMiddle([-12, 34, 40, -5, -12, 4, 0, 0, -12]) == [-12, 34, 40, -5, -12, 4, 0, 0, -12]

def test_case6() :
        assert replaceMiddle.replaceMiddle([9, 0, 15, 9]) == [9, 15, 9]

def test_case7() :
        assert replaceMiddle.replaceMiddle([-6, 6, -6]) == [-6, 6, -6]

def test_case8() :
        assert replaceMiddle.replaceMiddle( [26, 26, -17]) ==  [26, 26, -17]

def test_case9() :
        assert replaceMiddle.replaceMiddle([-7, 5, 5, 10]) == [-7, 10, 10]

