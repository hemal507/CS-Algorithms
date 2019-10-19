import mathPractice

def test_case1() :
	assert mathPractice.mathPractice([1,2,3,4,5,6]) == 71

def test_case2() :
        assert mathPractice.mathPractice([8,9]) == 17

def test_case3() :
        assert mathPractice.mathPractice([0,8,15]) == 120

def test_case4() :
        assert mathPractice.mathPractice([3, 18, 5, 17, 7, 12, 3, 14]) == 2612

def test_case5() :
        assert mathPractice.mathPractice([9, 19, 2, 2, 7, 3, 0, 0, 6, 11, 14, 18, 11, 7, 9, 6, 8, 4, 13, 11]) == 1778151
