import isArithmeticProgression

def test_case1():
	assert isArithmeticProgression.isArithmeticProgression([1, 4, 7]) == True

def test_case2():
        assert isArithmeticProgression.isArithmeticProgression([2, 4, 7]) == False

def test_case3():
        assert isArithmeticProgression.isArithmeticProgression([1, 3, 1]) == False

def test_case4():
        assert isArithmeticProgression.isArithmeticProgression([-7, -5, -3, -1]) == True

def test_case5():
        assert isArithmeticProgression.isArithmeticProgression([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True


