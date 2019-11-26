import calcFinalScore

def test_case1() :
	assert calcFinalScore.calcFinalScore([4, 2, 4, 5], 3) == 57

def test_case2() :
        assert calcFinalScore.calcFinalScore([4, 2, 4, 5], 5) == 12

def test_case3() :
        assert calcFinalScore.calcFinalScore([], 5) == 0

def test_case4() :
        assert calcFinalScore.calcFinalScore([5, 3, 1, 9], 4) == 116

def test_case5() :
        assert calcFinalScore.calcFinalScore([3, 9, 0, 50], 1) == 2500

def test_case6() :
        assert calcFinalScore.calcFinalScore([8, 8, 39, 33, 29, 35], 4) == 4676

